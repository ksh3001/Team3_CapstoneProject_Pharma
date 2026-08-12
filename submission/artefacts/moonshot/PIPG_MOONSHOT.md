# Moonshot: Prompt-Injection Protection Gateway (PIPG)

| Field | Entry |
|---|---|
| Branch | `Moon-shot-research` |
| Status | Concept / design (implementation under `submission/`) |
| Scope | Shared control plane in front of Batch, PV, and Supply workflows |
| Safety boundary | Advisory only — never batch disposition, final PV decisions, allocation, shipment, or recall |

---

## 1. What the moonshot idea is about

### 1.1 One-liner

A fail-closed **Prompt-Injection Protection Gateway** that sits in front of every Batch / PV / Supply path and treats documents, retrieval chunks, free text, and tool manifests as **untrusted data** unless authority, purpose, and signed permissions are proven at execution time.

### 1.2 Problem

In the AEGIS-PHARMA brownfield estate, AI-assisted workflows will ingest:

- Documents that look like SOPs but carry hidden bypass instructions (e.g. “ignore quality holds”).
- Fake “policies” that invent illegal auto-actions (e.g. auto-submit every social mention).
- Tool manifests that escalate from read to regulated write (e.g. disposition = READY).
- Draft, superseded, or research notes that must never become runtime instructions.

If any of these become **model or tool instructions**, the system crosses the package hard line: autonomous regulated action. Generic chat “guardrails” are not enough. The package needs **authority-aware instruction quarantine** across documents, tools, and prompts.

### 1.3 Product claim

> No retrieved document, free-text narrative, or tool manifest can become an instruction that weakens a quality hold, invents a PV obligation, or writes disposition — even if a model would obey it. Attempts are preserved as adversarial evidence and block release if controls fail.

### 1.4 Why this is a moonshot (not a filter)

| Ordinary injection filter | PIPG moonshot |
|---|---|
| String / classifier on user chat | GxP-aware instruction vs evidence split |
| Model decides what to ignore | Catalog status, authority, and signatures beat model confidence |
| Text-only focus | Includes **tool-plane** poisoning |
| Cloud LLM dependent | Deterministic offline path mandatory |
| Soft warning | Fail-closed; failed gates block release |

### 1.5 Fit to this challenge package

| Package surface | Hook |
|---|---|
| INJ-065 | Prompt injection in supplier deviation (`knowledge/MALICIOUS_SUPPLIER_DEVIATION.md`, K-998) |
| INJ-066 | Tool-manifest poisoning (`data/tool_manifest_poisoned.json`, `batch_status_plus`) |
| PUB-03 | Public fixture: prompt injection, document authority, quality hold |
| PUB-05 | Untrusted fake PV rule (K-999) must not become policy |
| Eval suite #5 | Retrieval authority, supersession, poisoning, prompt-injection tests |
| Eval suite #8 | Agent path, tool authorization, idempotency, replay |
| Scoring hard gate | Fail if unsigned tools or untrusted documents are used as instructions |
| Release gate | Block on untrusted instructions / failed critical security tests |
| DoD §4 | Must test prompt injection, poisoning, tool abuse, excessive agency |
| Knowledge | `ZERO_TRUST_AI_TOOLS.md`, `AI_GXP_BOUNDARY.md`, `AGENT_BUDGET_AND_STOP_POLICY.md` |
| Template | `templates/16_THREAT_ABUSE_MODEL.md` (§ Prompt/retrieval poisoning, Tool abuse) |
| Coverage | `TC-INJ-065`, `TC-INJ-066` (Security gate) |

---

## 2. Core design principles

1. **Instruction plane vs evidence plane** — Untrusted content may be hashed, stored, and cited; it must never drive prompts, rules, or tools.
2. **Deny by default** — Unknown, draft, superseded, or untrusted authority ⇒ not instruction-eligible.
3. **PIPG before workflows** — Batch / PV / Supply only consume a gated context.
4. **Deterministic first** — Catalog + manifest + permission rules before any LLM classifier.
5. **Fail closed** — On ambiguity: abstain, escalate `human_review`, keep `execution_status: not_executed`.
6. **Preserve adversarial evidence** — Do not silently delete K-998 / K-999; flag the attempt in audit.
7. **AI-disabled continuity** — Same trust rules apply when inference is off.
8. **No regulated side effects** — Gateway prevents writes; it never performs disposition / PV / allocation.

---

## 3. Architecture

### 3.1 Placement relative to existing workflows

```text
Request (user, purpose, workflow, as-of)
        │
        ▼
┌─────────────────────────────────┐
│ AuthZ (user × purpose × object) │
└────────────────┬────────────────┘
                 ▼
┌─────────────────────────────────┐
│ PIPG (NEW control plane)        │
│  - document trust classify      │
│  - injection quarantine         │
│  - tool manifest verify         │
│  - prompt assembly guard        │
│  - budget / stop hooks          │
│  - security audit emit          │
└────────────────┬────────────────┘
         allow / evidence_only / deny
      ┌──────────┼──────────┐
      ▼          ▼          ▼
   Batch       PV        Supply
   evidence    intake    options
      │          │          │
      └──────────┴──────────┘
                 ▼
  Contract response:
  evidence, contradictions, gaps, abstentions,
  human_review, audit, execution_status: not_executed
```

Workflows keep domain logic (reconcile evidence, duplicates, draft options). They do **not** call raw retrieval or tools without a PIPG decision.

### 3.2 New shared components

| Component | Responsibility |
|---|---|
| PIPG Gateway | Single API: may this item instruct the run? |
| Document Trust Classifier | Uses `knowledge_catalog` status, authority, effective date, jurisdiction |
| Injection Quarantine | Detects / flags embedded bypass instructions; marks evidence-only |
| Tool Manifest Verifier | Approved signed allowlist only; rejects poisoned manifests |
| Capability Policy Engine | Maps tool permissions to workflow-allowed capabilities |
| Prompt Assembly Guard | Builds instruction context only from instruction-eligible sources |
| Gateway Audit Emitter | Records attempt, decision, reason codes, content hashes |
| Stop / Budget Hook | Enforces step/tool/token stop conditions before escalation |

### 3.3 Workflow-specific touchpoints

| Workflow | PIPG addition |
|---|---|
| Batch | Gate applicable documents before readiness logic; refuse disposition-write tools; PUB-03 / K-998 never uplift readiness |
| PV | Gate policy-like retrieval before obligations; K-999 never creates auto-submit duty; escalate `required_reviews` |
| Supply | Deny tools that reserve / allocate / ship / change quality status; options remain draft with `no_side_effects: true` |

### 3.4 Versioned interfaces (submission-owned)

```text
GatewayRequest
  user, purpose, workflow, as_of, mode
  candidate_documents[], candidate_chunks[], candidate_tools[]

GatewayDecision (per item)
  disposition: instruction_allowed | evidence_only | denied
  reason_codes[], integrity_hash, authority_snapshot

GatedContext
  instruction_sources[]   # may influence prompts/rules
  evidence_only_sources[] # cite / preserve only
  denied_tools[]
  security_events[]
```

Package response contracts remain the source of truth for workflow outputs. PIPG outcomes fold into `evidence`, `contradictions`, `gaps`, `abstentions`, `human_review`, and `audit`.

---

## 4. Implementation

### 4.1 Suggested `submission/` layout

```text
submission/
  src/
    gateway/
      __init__.py
      service.py              # PIPG entrypoint
      trust_catalog.py        # knowledge_catalog adapter
      injection_quarantine.py
      tool_verifier.py
      capability_policy.py
      prompt_guard.py
      audit.py
      models.py               # GatewayRequest / Decision / GatedContext
    authz/
      service.py
    workflows/
      batch.py
      pv.py
      supply.py
    contracts/
      validate.py
    runtime/
      mode.py                 # deterministic_offline / ai_disabled
      idempotency.py
    app_api.py                # dispatch: AuthZ → PIPG → workflow
  tests/
    test_pipg_document_injection.py
    test_pipg_tool_poison.py
    test_pipg_fake_policy.py
    test_pipg_workflow_integration.py
    test_pipg_ai_disabled.py
  artefacts/
    moonshot/
      PIPG_MOONSHOT.md        # this document
  evaluation/
    adversarial/              # participant fixtures beyond PUB-*
  runbooks/
    INCIDENT_PIPG.md
    AI_DISABLED_CONTINUITY.md
```

### 4.2 Implementation phases

#### Phase A — Deterministic wedge (minimum credible demo)

1. Load trust metadata from `data/knowledge_catalog.csv`.
2. Implement Document Trust Classifier:
   - `status == untrusted` (K-998, K-999) ⇒ `evidence_only` or `denied` for instruction use.
3. Implement Tool Manifest Verifier:
   - Allow only approved read tools (e.g. `batch_status_read` with signature).
   - Reject `data/tool_manifest_poisoned.json` / `batch_status_plus` (disposition write + postAction).
4. Wire AuthZ → PIPG → Batch for PUB-03 path.
5. Emit audit security events; keep `execution_status: not_executed`.
6. Tests: INJ-065 / INJ-066 style negatives must fail closed.

#### Phase B — All three workflows

1. Extend gateway calls to PV (PUB-05 / K-999) and Supply (side-effect tool deny).
2. Prompt Assembly Guard: instruction context excludes evidence-only sources.
3. Merge quarantine into workflow `abstentions` / `human_review`.
4. Idempotent gateway decisions per `request_id`.
5. Release-gate check: any instruction use of untrusted/unsigned material fails evaluate.

#### Phase C — Hardening (moonshot depth)

1. Pattern library for embedded instructions (ignore holds, mark ready, auto-submit, etc.) with deterministic detectors.
2. Supersession / draft / research-note handling (`BATCH_RELEASE_POLICY_OLD`, `RESEARCH_NOTE_UNAPPROVED`).
3. Couple stale AuthZ (INJ-067): revoked user cannot obtain instruction-allowed context.
4. Budget/stop integration (`AGENT_BUDGET_AND_STOP_POLICY.md`).
5. Optional secondary LLM classifier **behind** deterministic gates (never sole control); disabled in `ai_disabled` mode.
6. Living assurance evidence: map PIPG controls to threat-model §3–4 and assurance-case claims.

### 4.3 Reference decision algorithm (deterministic)

```text
for each candidate document/chunk:
  lookup catalog (id, status, authority, effective_at, hash)
  if status in {untrusted, draft, superseded, unknown} or authority not applicable:
      mark evidence_only (or denied if workflow forbids even citing without review)
  if body matches injection patterns (bypass hold, set disposition, ignore policy):
      mark evidence_only + security_event=prompt_injection_attempt
  if instruction_allowed and purpose/AuthZ ok:
      add to instruction_sources
  else:
      add to evidence_only_sources or denied

for each candidate tool:
  require approved signed manifest
  require permissions ⊆ workflow allowlist
  if permission implies disposition/PV-final/allocate/ship/recall:
      deny + security_event=tool_poison_or_overprivilege
  else if verified:
      allow tool for this run

if any high-risk unresolved conflict:
  stop / abstain / human_review
  do not call side-effect tools
  do not elevate readiness or invent PV obligations
```

### 4.4 Demo script (package assets)

| Step | Asset | Expected PIPG behavior |
|---|---|---|
| 1 | `knowledge/MALICIOUS_SUPPLIER_DEVIATION.md` + PUB-03 | Quarantine; cite as evidence; do not clear quality hold or mark ready |
| 2 | `knowledge/FAKE_PV_EXPEDITED_RULE.md` + PUB-05 | Do not treat as PV policy; escalate human review |
| 3 | `data/tool_manifest_poisoned.json` vs approved read manifest | Deny tool load/execute |
| 4 | `data/knowledge_catalog.csv` K-998/K-999 | Catalog `untrusted` wins over document body claims |
| 5 | `data/tool_catalog.csv` (`batch_status_plus` = no) | Non-approved tools never enter runtime |
| 6 | Evaluate / security gates | TC-INJ-065 / TC-INJ-066 style tests pass; release blocked if gateway bypassed |

### 4.5 Test requirements (write before / with code)

| Suite | Assert |
|---|---|
| Document injection | K-998 never appears in instruction_sources |
| Fake policy | K-999 never creates auto-submit obligation |
| Tool poison | Poisoned manifest never authorized |
| Workflow integration | Batch/PV/Supply cannot bypass gateway |
| AI-disabled | Same deny/quarantine outcomes with LLM off |
| Release gate | Evaluate fails if untrusted used as instruction |

### 4.6 Runtime modes

| Mode | PIPG behavior |
|---|---|
| `deterministic_offline` | Catalog + manifest + pattern rules only (default assessed path) |
| `ai_disabled` | Identical trust rules; no model-based detector; workflows run manual/rules path |

---

## 5. Non-goals

- Autonomous batch disposition, final PV decisions, stock reservation/allocation/shipment, quality-status change, or recall initiation.
- Silently rewriting or deleting adversarial documents.
- Claiming validated GxP DSS or EU AI Act conformity from PIPG alone.
- Using an LLM as the only injection detector.
- Per-workflow one-off “ignore malicious text” prompts as a substitute for the gateway.

---

## 6. Success criteria

1. PUB-03 and poisoned-tool paths fail closed with auditable security events.
2. Untrusted catalog entries cannot enter instruction context.
3. All three workflows consume only `GatedContext`.
4. Package scoring hard gate on unsigned tools / untrusted instructions is demonstrably enforced.
5. AI-disabled path preserves the same instruction quarantine.
6. Defence can show attack → quarantine → abstain/escalate → no regulated execution, with evidence hashes.

---

## 7. Build order (practical)

1. Models + trust catalog adapter + tool verifier.
2. Gateway service + audit emitter.
3. Wire Batch (PUB-03) end-to-end.
4. Negative tests for INJ-065 / INJ-066.
5. Wire PV + Supply.
6. Prompt assembly guard + release-gate hook.
7. Runbooks + threat-model / assurance-case linkage.

---

## 8. Related challenge paths (read-only evidence)

- `case/INTEGRATED_CASE.md` — INJ-065, INJ-066, required operating properties
- `DEFINITION_OF_DONE.md` — security and evaluation obligations
- `evaluation/EVALUATION_PLAN.md` — suites #5, #8; release gates
- `evaluation/public_scenarios.json` — PUB-03, PUB-05
- `evaluation/contracts/*.schema.json` — workflow response shape
- `data/knowledge_catalog.csv`, `data/tool_catalog.csv`, `data/tool_manifest_poisoned.json`
- `knowledge/MALICIOUS_SUPPLIER_DEVIATION.md`, `knowledge/FAKE_PV_EXPEDITED_RULE.md`
- `knowledge/ZERO_TRUST_AI_TOOLS.md`, `knowledge/AI_GXP_BOUNDARY.md`
- `starter/api_samples/tool_manifest_approved.json`
- `templates/16_THREAT_ABUSE_MODEL.md`, `templates/21_ASSURANCE_CASE.md`
- `requirements/SCORING_MODEL.md` — hard gates

---

## 9. Document control

| Field | Entry |
|---|---|
| Title | PIPG Moonshot — concept and implementation |
| Location | `submission/artefacts/moonshot/PIPG_MOONSHOT.md` |
| Challenge evidence | Not modified; all build work stays under `submission/` |
| Next step | Implement Phase A under `submission/src/gateway/` with failing adversarial tests first |
