# Token Efficiency and AI FinOps

> Team3 Phase 5 artefact (template 23). Honest TCO under **hypothesis** — package `cost_model.csv` is incomplete for human review.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — FinOps / Product |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Evaluation; Architecture |
| Status | Phase 5 — provisional; **no ROI proof** |
| Related | ADR-002; NFR-01; F-004; RR-01; D-006 |

## Purpose

Explain assessed-path token strategy (avoidance), incomplete cost model, human-review gap, and budget alerts so FinOps does not invent savings from Missing baselines.

## Evidence register

| Evidence ID | Source | Fact used | Limitation |
|---|---|---|---|
| E-FO-01 | `data/cost_model.csv` | inference 184000; human_quality_review 0; medical_review 0; observability 31000 | TCO incomplete (F-004) |
| E-FO-02 | `data/staff_rates.csv` | Rates exist | Not wired to hours |
| E-FO-03 | ADR-002; AC-051 | LLM off assessed | By design |
| E-FO-04 | NFR-01/13/14 | 0 LLM; doc scan ≤32; ≤20 steps | POC |
| E-FO-05 | MetricsCollector | Latency JSON local | Not cost ledger |

## 1. Workload baseline

| Item | Response |
|---|---|
| Assessed workload | Deterministic batch / PV / supply / authz / evaluate on fixtures |
| Inference workload assessed | **0** calls |
| Ops pack volume / cycle-time | **Unknown** — P0 Missing |
| Review hours | **Unknown** — cost_model shows 0 USD/mo (not “free”) |

## 2. Model/routing strategy

| Strategy | Decision |
|---|---|
| Default | No model — rules + ACL + schemas |
| Optional narrator | Port exists; **disabled** assessed; enable only after ADR-002 revisit |
| Routing | N/A while LLM=0 |
| Model registry | Hash mismatch (INJ-070) blocks future enablement |

## 3. Context and token budgets

| Budget | POC rule |
|---|---|---|
| Assessed tokens | **0** |
| If narrator enabled later | Bound context to cited evidence only; no bulk case dump; max docs NFR-13 |
| Steps | ≤20 per request (NFR-14) |
| Denial-of-wallet | Kill switch = AI-disabled mode; no unbounded agent loops |

## 4. Caching and avoided inference

| Lever | Effect |
|---|---|
| Deterministic packs | Avoids summary tokens entirely on assessed path |
| AuthZ deny early | Avoids wasted workflow compute for revoked users |
| Doc quarantine | Avoids retrieving untrusted text into any future prompt |
| **Do not** cache IAM allow after revoke | Security > token save (INJ-067) |

## 5. Human-review and validation cost

| Cost element | Package signal | Team3 treatment |
|---|---|---|
| human_quality_review | 0 USD/mo | **Gap** — must acquire hours×rates before TCO |
| medical_review | 0 USD/mo | **Gap** — same |
| inference | 184000 | Not incurred on assessed path; do not claim “saved 184k” without baseline workload |
| observability | 31000 | Partial — local files ≠ prod observability spend |
| Validation / CSA / TEVV labor | Not in cost_model | Material omitted cost |

**Decision:** Publish **incomplete TCO** flag; refuse net-savings narrative under hypothesis.

## 6. Cost per successful task

| Metric | Value |
|---|---|
| Assessed $ inference / successful pack | **$0** (no calls) |
| Fully loaded $ / successful pack | **Unknown** (review hours Missing) |
| Demo success definition | Hard-gate pass + schema-valid pack/options |

## 7. Budget alerts and vendor shock

| Control | POC | Production need |
|---|---|---|
| Token budget alert | N/A while LLM=0 | Required before narrator enable |
| Vendor price shock | Avoided by no vendor on assessed path | Multi-model exit plan (tmpl 27 later) |
| Cost regression gate | pytest asserts LLM off | Add token counters if AI enabled |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-FO-01 | Gap | cost_model human lines = 0 | Open — P0 |
| R-FO-02 | Risk | Claiming inference savings as board benefit | Blocked |
| R-FO-03 | Assumption | LLM remains off for assessed scoring | ADR-002 |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Assessed LLM cost = 0 | AC-051; NFR-01 | Pass |
| Full TCO known | cost_model | **Fail / Unknown** |
| No false ROI | hypothesis; RR-01 | Pass (discipline) |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 FinOps | Owner | Incomplete TCO explicit | Aligns F-004 / D-013 | 2026-08-07 |
