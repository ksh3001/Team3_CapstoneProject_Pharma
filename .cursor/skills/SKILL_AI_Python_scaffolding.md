---
name: ai-python-scaffolding
description: >-
  Build and harden Python services that call an LLM — agents, RAG pipelines,
  function-calling tools, AI APIs and chatbots. Covers typed Pydantic v2 contracts,
  provider drift absorption, resilient typed clients with retries, function-calling
  validation, request/response models, contract tests, ports and adapters, and the
  production layers on top: type checking in CI, config and secrets, bounded
  concurrency, streaming, token budgets, telemetry, circuit breakers, prompt-injection
  containment, caching, idempotency, lifecycle and evals. Trigger proactively whenever
  a request involves calling a model — including "build an app that uses GPT/Claude" or
  "add an endpoint that calls the model" — and when auditing an AI service for
  production readiness.
---

# AI Python Scaffolding

Scaffolding is the structure built **before and underneath** an AI feature: typed
contracts, validation, resilient clients, tests and clean layering. It is what stops
the system collapsing when a response arrives in the wrong shape, a rate limit hits, a
tool argument is hallucinated, or a vendor is swapped. The cost of a defect grows the
later it is caught, so every technique here moves detection to the moment bad data
enters, rather than the moment it reaches a user.

**Part A — Foundations** is the harness itself: build it in the same pass as the
feature, not as a follow-up refactor. **Part B — Hardening** is what production adds:
apply it by triage, not all at once.

Concrete templates for everything below: [code_patterns.md](code_patterns.md).

## How much to apply

Default to all of Part A whenever code calls a model. A demo and a production service
should differ in scope, not in whether boundaries are typed and tested. If the user
explicitly wants a throwaway script, say which items you are skipping and why, and
offer to harden afterwards.

Part B is different: adding all eleven areas to a service that needs two is its own
failure. Match the work to the symptom.

| Symptom or stage | Add first |
|---|---|
| Any code that calls a model | All of Part A |
| Going to production at all | B1 enforcement, B2 config, B6 telemetry, B10 health |
| Bursts of 429s under load | B3 bounded concurrency, then B7 breaker |
| Slow perceived response | B4 streaming |
| Surprise bill, untrusted callers | B5 token caps and budget |
| Retrieved or user text in prompts | B8 allow-list and output escaping |
| Provider outage took the service down | B7 breaker, then fallback |
| "It got worse after we changed the prompt" | B11 evals |
| Refactors break things silently | B1 type checker in CI |

## The runtime ordering principle

Once built, these are layers around a single call, and the order is the design:

```
cache? → circuit breaker → budget guard → [ timeout → retry → validate ] → telemetry
 free      microseconds      no network         the expensive part
```

Each layer exists to avoid paying for the next. **Test for placing any new layer:** does
it prevent work, or only observe it? If it prevents work, it goes earlier.

---

# Part A — Foundations

Build in this order. Each layer sits underneath the next.

## A1. Typed foundations

**Type hints on every function boundary**, especially anything touching model output,
request data, or another team's code. Without them a tool returning `usage` as `"42"`
crashes three layers deep at 2 a.m. instead of failing where it entered.

**Pydantic v2 strict mode** for everything crossing a trust boundary — API requests,
model and tool JSON, config, queue messages, third-party responses. Lax mode coerces
`"21"` into `21`, hiding the fact that the model returned the wrong type. Strict mode
refuses to guess, so you see the misbehaviour instead of inheriting a subtle bug.

**`extra` goes opposite ways on each side.** On inputs you own, `extra="forbid"` so a
hallucinated field is named and rejected. On provider payloads, `extra="ignore"` —
vendors legitimately add keys like `usage` and `id`, and forbidding them turns a good
response into an outage.

**Absorb provider drift in exactly one place**, a `@model_validator(mode="before")` that
maps every known response shape onto one internal shape. This is the fix for the
canonical failure: staging returns `{"text", "finish_reason"}`, production returns
`{"message": {"content"}, "stop_reason"}`, and untyped code crashes in front of the
client. The model did not break — the contract assumption did.

**Async for I/O.** Model calls spend 2–20 seconds waiting on the network. `async`
overlaps that waiting; it does not make anything faster. Never call a blocking function
inside async code — one `time.sleep` or sync HTTP call freezes every in-flight request.
Async is for I/O, not CPU work.

**Lock dependencies from the first commit**, with whatever tool the project uses. An
unpinned transitive dependency that ships overnight is a bug nobody wrote.

## A2. The resilient typed client

Never scatter raw SDK calls across the codebase. Wrap the provider in **one typed client
class**: typed input in, validated object out. Every call then flows through a single
choke-point, so adding a retry, swapping a vendor, or adding cost tracking is one edit.

Treat failure as normal: rate limits, timeouts, transient 5xx, malformed output, auth
and config errors, network drops. The call crosses the public internet to someone
else's busy servers.

Layered inside the client: **timeout**, then **retry transient errors** with exponential
backoff plus jitter and capped attempts, then **validate inside the loop** — a malformed
payload is a provider failure, not a caller failure. Circuit breaker and fallback come
in B7.

| Retry | Do not retry |
|---|---|
| 429, 503, timeouts, connection resets | 400 / 422 — the request is wrong |
| Read-only or idempotent operations | 401 / 403 — fix the key, not the retry |
| | Non-idempotent side effects without an idempotency key |

Jitter is not decoration: without it every worker retries on the same instant and the
retry storm outlasts the blip that caused it. Check the SDK's own retry count before
setting yours, or the two multiply.

**Error taxonomy**, mapped by the adapter: `TransientError` (retry is reasonable),
`PermanentError` (give up now), and a serializable `TypedError` returned to callers or
back to the model with `code`, `message` and `retryable`.

## A3. Function-calling contracts

The model is probabilistic; your code is deterministic and will execute whatever it is
handed. The schema is the seatbelt between them.

1. **Define the schema before the function body.** Tight constraints narrow the blast
   radius before the model replies. One Pydantic model does three jobs: generates the
   tool definition, validates the reply, documents the contract.
2. **Parse then validate.** Arguments arrive as a JSON string, so `json.loads` first,
   then `model_validate`. They are a proposal, never a fact.
3. **Return errors to the model.** Function-calling loops self-correct — feed back the
   field name and the constraint that failed and the next turn usually fixes itself.
   Validation is a conversation, not a dead end.
4. **Guard intent, not just shape.** Schema-valid is not business-valid.
   `delete_records(filters={})` satisfies any schema and deletes every row. Anything
   destructive needs a business-rule and authorization check after validation.

There is no trusted tool call: a 99%-reliable model over a million calls sends ten
thousand bad ones. B8 adds a third gate in front of these.

## A4. The API edge

The edge knows HTTP and nothing else. Reuse the A1 types and the framework validates
requests, serializes responses and generates docs from them alone.

**Declare both models on every endpoint, always.** The request model keeps bad data
**out**; the response model keeps internal data **in** by whitelisting exactly which
fields leave. Returning a raw dict "just this once" is how `raw_prompt`,
`internal_cost_usd` and a debug `user_email` escape unnoticed for months.

A 422 on a wrong-typed field is strict mode working, not a bug. The generated API spec
is the single source of truth shared by frontend, tests and partners, and cannot drift
because it comes from the models.

## A5. Tests as a gate

Write tests alongside the code. Use fixtures for reusable setup and parametrize for edge
cases.

**Never call a real model in a unit test.** It is slow, costs money, needs a key, and
returns a different answer each run, so the test fails randomly regardless of your code.
If the port from A6 is clean you do not even need a mocking library — inject a fake
adapter. If you cannot inject one, the boundary is tangled, and that is the finding.

**Assert the contract, not the wording.** `assert reply == "The total is ₹118."` passes
today and fails tomorrow on a rephrase; a suite full of false alarms gets ignored, which
is worse than no tests. Assert **shape** (does it parse into the schema, are required
fields present and typed) and **properties** (summary under 50 words, score in range,
enum among the allowed values).

**Gate merges on it.** A model upgrade that renames `full_name` to `name` still "works"
at runtime while the frontend shows blanks. A contract test goes red the moment the
field moves.

## A6. Ports and adapters

Business rules should not know whether data came from one vendor or another, from which
database, or over HTTP or a queue.

A **port** is an interface the core defines in terms of *your* types. An **adapter**
implements it and is the only place a vendor SDK may be imported. The core depends only
on the port, so swapping vendors, databases, or real-for-fake becomes configuration
rather than surgery.

Four rules: the core imports no SDK, no SQL and no framework; every external system sits
behind a port; the adapter is chosen once at a composition root; and tests prove the
seams, because if you can inject a fake the boundary is clean.

---

# Part B — Hardening

## B1. Enforce the contracts you declared

Type hints are not checked at runtime, and Pydantic only guards boundaries you modelled.
Without a type checker in CI, "everything is typed" is a convention nobody verifies and
a wrong annotation looks exactly like a right one. This is the largest single gap,
because it undermines A1.

Run three gates in CI on every change: lint, strict type check, then tests against a
fake provider. Enable the linter's async rules — they statically catch the blocking call
inside an async function that otherwise surfaces only under load. Start strict on new
code; on existing code enable it per module, working inward from the core.

## B2. Configuration and secrets

Configuration is a contract too. Validate it at startup so a missing key is a boot
failure naming the field, not a 500 on the first production request.

Wrap secrets in a type that cannot print, so a settings object caught in a traceback
does not leak the key, and unwrap only inside the adapter. The core reads settings, never
the environment directly. Forbid unknown variables so a misspelling is an error rather
than silence. Commit an example env file with every key present and every value blank.

## B3. Bound concurrency to the provider's limits

Overlapping I/O is the point of async, but unbounded fan-out is a rate-limit generator.
Firing fifty calls at once produces 429s, and with retries underneath, each of the fifty
retries and amplifies the burst.

Cap in-flight calls with a semaphore sized from the provider's published
requests-per-minute and tokens-per-minute, and keep the limit in settings. Collect
failures rather than raising, so one bad item does not discard forty-nine good results.
Share one HTTP client across the process; per-call clients discard connection pooling.

## B4. Stream without losing the contract

Streaming is usually a product requirement. It breaks two assumptions that hold
everywhere else.

**Output validation no longer happens on the way out** — a framework cannot inspect a
stream, so the response whitelist from A4 does not apply. Build every frame from a typed
model; never forward provider chunks verbatim. **The success status is already sent**, so
a failure ten seconds in cannot become a 502; it travels as a terminal event in the
stream. Validate the accumulated text once the stream closes.

Retries stop applying after the first byte, since replaying text the user already saw is
worse than failing. Treat client disconnects as normal, but record cost and token
accounting for the partial response before cancellation propagates.

## B5. Cap the spend

An LLM endpoint is the rare place where one careless request costs real money and no
correctness scaffolding notices. Always send a maximum output length — without it a
model that fails to stop generates until the context window is exhausted, on your
account. Cap input length at the request model, which is cheaper still.

Guard a rolling budget at the choke-point, before the call, and raise a **permanent**
error: waiting does not create budget, so the retry layer must not attempt it again.

## B6. Telemetry for failures that raise nothing

AI services degrade without erroring: quality drops after a model upgrade, latency
triples, cost doubles after a prompt edit. Emit one structured event per call with
request id, provider, model, outcome, attempt, latency, tokens and cost.

**Never log prompts or completions by default** — they are the highest-PII payload in
the system and the first thing an engineer reaches for. Log a hash, or a redacted
preview behind a flag that is off in production.

Beyond error rate and latency, alert on two AI-specific signals: **validation-failure
rate**, which is drift happening live before any test catches it, and **cost per
request**, which catches a prompt change that tripled token usage.

## B7. Circuit breaker and fallback

Retries alone make an outage worse: when the provider is truly down every caller burns
the full attempt budget before failing, so each waits the maximum time to be told no.

A breaker opens after consecutive failures, fails fast while open, and allows one trial
call after a cooldown to decide the next state. Check it **before** the retry loop, never
inside it.

**Fallback, in preference order:** a cached answer for an identical request; a cheaper
model behind a second adapter; an explicit degraded response. Silently downgrading
quality without surfacing it is its own incident.

## B8. Contain prompt injection

Any text you did not write is untrusted input: retrieved documents, user messages,
scraped pages, uploaded files, the output of previous tool calls. A model cannot
reliably separate your instructions from instructions embedded in content it was asked
to process.

Keep untrusted content out of the instruction channel — instructions in the system role,
material in a delimited block, never concatenated. Delimiters reduce the success rate
but never eliminate it, so never make them the only layer.

**Bound the blast radius instead of winning the argument.** The tools available during a
request are chosen by your code, not the model, and should be the minimum that request
needs. Then a fully successful injection still reaches only tools that were already safe.
This makes three gates in order: **allow-list, then shape, then intent**.

Model output is untrusted too: escape it for HTML, parameterise it for SQL, keep it out
of shells, and remember that a summariser feeding an agent is an injection path
laundered through two hops. Put any content-safety service behind a port, distinguish
its four outcomes — passed, intervened with a reason, not configured, service error —
and never let it fail open silently.

## B9. Caching and idempotency

Cache on `(model, prompt, temperature, max_output)`, but only at temperature zero where
the call is meant to be deterministic; above zero caching removes the variation that was
the reason for it. Cache the *validated* object, with a TTL short enough that a model
upgrade does not serve stale answers for weeks.

Idempotency matters more for tool calls than completions: a model repeating a
create-record call after a timeout it never saw resolve produces a duplicate the user
sees. Take a caller-supplied key, store the result against it, return it on a repeat.

## B10. Startup, health and shutdown

Build settings, HTTP client, adapter, breaker and budget once at a single composition
root and close them on shutdown. That function is the only code that knows which vendor
is in use, which is what keeps the A6 swap a config change.

Expose two separate endpoints. **Liveness** answers "is this process alive" and must not
call the provider, or a blip makes the orchestrator restart healthy instances and turn
degradation into an outage. **Readiness** answers "should traffic come here" and may
reflect local state such as whether the circuit is open.

Set the termination grace period **above** the request timeout, or shutdown kills
in-flight calls that were about to succeed and that you have already paid for.

## B11. Evals, separate from contract tests

| | Contract test (A5) | Eval |
|---|---|---|
| Asks | Did the shape hold? | Is the output any good? |
| Provider | Faked | Real |
| Runs | Every change | Nightly, and on prompt changes |
| Cost | Free, deterministic | Slow, paid, non-deterministic |

Keep a versioned golden set of twenty to fifty inputs with expected **properties**, never
expected text, stored beside the code so a prompt change and its results land in the same
commit. **Gate on regression, not absolutes** — 0.92 falling to 0.71 is the signal; a
fixed threshold blocks everything or nothing. If a model judges the output, pin the judge
and its prompt, set temperature to zero, and validate its reply through a strict schema.

---

## Traps that bite

Each of these looks like a library bug the first time.

- **A `str`-Enum field under `strict=True` rejects the plain string the provider sends.**
  `finish_reason: FinishReason` will not accept `"stop"`; it demands an enum instance.
  Use `Literal["stop", ...]` for wire-facing fields — identical JSON schema, validates
  plain strings — or coerce inside the before-validator. Bites hardest on tool arguments,
  where every value arrives as a string from `json.loads`.
- **`extra="forbid"` on a provider response turns a good reply into an outage** the day
  the vendor adds a key. Forbid on your inputs, ignore on their payloads.
- **`gather` over a list is unbounded concurrency.** It is the standard example and it
  generates the very 429s the retry layer then amplifies. Always bound it (B3).
- **Strict `int` and `float` do not interchange.** `temperature: float` rejects `0`.
- **A retry after the first streamed byte** replays text the user already saw.
- **An SDK's built-in retries multiply with yours.** Check before setting attempts.

## Definition of done

**Foundations**

- [ ] Every function boundary has type hints
- [ ] Model output parses into a Pydantic v2 strict model
- [ ] Provider drift is absorbed in one before-validator, not at call sites
- [ ] Inputs forbid extra fields; provider payloads ignore them
- [ ] I/O is async; the event loop is never blocked
- [ ] Each client is typed, with timeout, capped retries, backoff and jitter
- [ ] Transient and permanent failures are distinguished, and only transient retried
- [ ] Tool arguments are parsed then validated before execution
- [ ] Destructive tools have a business-rule and authorization guard
- [ ] Endpoints declare both a request and a response model
- [ ] Tests fake the provider and assert shape and properties, never wording
- [ ] Contract tests gate every merge
- [ ] Providers sit behind ports; the core imports no SDK, SQL or framework

**Hardening**

- [ ] A type checker runs in CI in strict mode and passes
- [ ] A linter runs in CI with async-blocking rules enabled
- [ ] Dependencies are locked; dev tooling is a separate group
- [ ] Settings load through a validated model and fail at startup
- [ ] Secrets cannot print and are absent from the repository
- [ ] An example env file documents every required variable
- [ ] Fan-out is bounded by a limit derived from the provider's rate limits
- [ ] One HTTP client is shared and closed at shutdown
- [ ] Every call sends a maximum output length; input length is capped
- [ ] A budget guard can refuse a call before it is paid for
- [ ] A circuit breaker fails fast while the provider is down
- [ ] A fallback path exists and is explicit, not silent
- [ ] Streaming reports failure in-band and validates the accumulated result
- [ ] Untrusted content is delimited, never concatenated into instructions
- [ ] The tool set per request is the minimum that request needs
- [ ] Tool calls pass allow-list, then shape, then intent
- [ ] Model output is escaped or parameterised before HTML, SQL or a shell
- [ ] Safety checks sit behind a port and never fail open silently
- [ ] One structured event per call, with latency, tokens and cost
- [ ] Prompts and completions are not logged by default
- [ ] Validation-failure rate and cost per request are monitored
- [ ] Liveness and readiness are separate; neither calls the provider
- [ ] The termination grace period exceeds the request timeout
- [ ] A versioned golden set asserts properties, not text
- [ ] Evals run nightly and on prompt changes, gating on regression
- [ ] Any judge model is pinned and its output validated

## Applying this

When **building**, work Part A in order as you write the feature — a model written up
front is cheaper than one retrofitted after the untyped version already works. Pull
templates from [code_patterns.md](code_patterns.md) rather than reinventing them. Add
Part B by triage. If scope is tight, state which items you are deferring rather than
skipping them silently.

When **auditing**, start with `python scripts/audit.py <package>` — static analysis, no
dependencies, covering the mechanically decidable foundations and exiting non-zero on a
failure. It cannot judge whether retries are capped or destructive tools guard intent,
so it reports those as warnings with the evidence to read by hand. Then walk the rest of
the checklist and report each gap as **the failure it will cause**, then the fix. "No budget guard" is a rule violation; "one oversized prompt in a
loop can run up an unbounded bill, and nothing stops it" is a finding someone acts on.
Fix in dependency order — contracts, port, client, edge, tests — then by triage.
