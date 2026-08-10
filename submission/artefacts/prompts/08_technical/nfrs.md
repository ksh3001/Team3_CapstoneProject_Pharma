# Non-Functional Requirements (POC)

Measurable only. Unknowns labeled.

| ID | NFR | Target | Measure |
|---|---|---|---|
| NFR-01 | Assessed mode LLM calls | **0** per suite run | count inference attempts |
| NFR-02 | Side effects in assessed supply/batch/pv | **0** writes to exec systems / reservations | SideEffectGuard + FS assert |
| NFR-03 | AuthZ fail-closed on IAM revoke | **100%** deny | AC-001 |
| NFR-04 | Schema validation on workflow responses | **100%** of responses validated | validator |
| NFR-05 | Prohibited-field rejection | **100%** of negative fixtures fail closed | contract tests |
| NFR-06 | Batch pack latency (deterministic, local, PUB-01 class) | p95 **≤ 30 s** (assumed POC laptop budget) | timer |
| NFR-07 | PV pack latency (deterministic local) | p95 **≤ 30 s** | timer |
| NFR-08 | Supply options latency | p95 **≤ 30 s** | timer |
| NFR-09 | Health endpoint | **200** with `llm_enabled=false` in assessed | probe |
| NFR-10 | Idempotent replay | same key+body ⇒ same `request_id` body hash | replay test |
| NFR-11 | Audit snapshot coverage | **100%** allow-path responses | AC-063/ADR-010 |
| NFR-12 | Challenge tree immutability | **0** writes under `data/`,`knowledge/` | hash/watch |
| NFR-13 | Retrieval corpus per request | ≤ **32** knowledge docs scanned; only Applicable returned | counter |
| NFR-14 | Max workflow steps | ≤ **20** bounded steps per request | step counter |
| NFR-15 | Clean-room setup | `scripts/setup` success on Python 3.10+ stdlib-first | CI/manual |

**Out of scope NFR (production):** multi-region HA, RPO/RTO enterprise DR — deferred beyond POC.
