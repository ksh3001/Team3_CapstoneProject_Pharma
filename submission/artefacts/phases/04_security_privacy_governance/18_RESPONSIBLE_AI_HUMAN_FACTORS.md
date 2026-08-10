# Responsible AI and Human Factors

> Team3 Phase 4 artefact (template 18). Aligns with Prompt 04 gen_AI boundaries and INJ-071…074.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Product / GxP / Security |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Quality; PV; Supply; Evaluation |
| Status | Phase 4 — provisional |
| Related | ADR-002; D-007; `gen_ai_boundaries.md`; INJ-071…074 |

## Purpose

Define human accountability, automation-bias controls, abstention UX, language/accessibility limits, and competency expectations so AEGIS remains advisory under hypothesis framing.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-HF-01 | `case/INTEGRATED_CASE.md` D11 | INJ-071…074 |
| E-HF-02 | `artefacts/prompts/04_ddd/gen_ai_boundaries.md` | Rules vs AI; HITL matrix |
| E-HF-03 | `artefacts/phases/01_qualify/03_STAKEHOLDER_DECISION_RIGHTS.md` | Decision rights |
| E-HF-04 | `data/model_performance.csv`; `usability_findings.csv` | Language / a11y signals |
| E-HF-05 | pytest continuity / AC | LLM off; narrator refuse |

## 1. Human accountability

| Decision | Accountable human (outside AEGIS) | AEGIS role |
|---|---|---|
| Batch certification / disposition | EU QP / Quality | Evidence pack only |
| Final PV / reportability | Safety Physician | Intake packet; no finals |
| Allocation / ship / recall | Supply Governance Board | Draft options; no_side_effects |
| Entitlement grant / revoke | IAM admin | AuthZ check + audit |
| Untrusted doc elevation | Security + Quality | Quarantine event |

AI must not grant entitlement or resolve material conflicts alone.

## 2. Automation bias and contestability

| Control | Why (inject) |
|---|---|
| Dual-cite conflicts; no silent winner | Prevent green-path on omitted deviation (INJ-071) |
| LLM off by default; no disposition language from narrator | Reduce persuasive wrong summaries |
| Schema reject prohibited fields | Contest machine “decisions” that are illegal in contract |
| Audit snapshots with citations | Reviewer can contest pack completeness |
| Fuzzy auto-merge blocked | AMB-PV-01 |

## 3. Uncertainty and abstention UX

| Signal | UX / API behaviour |
|---|---|
| AuthZ deny | Stop; no pack; reason code |
| Unit / clock / authority conflict | Conflict objects; readiness not green for prohibited claims |
| Missing baseline / evidence | Abstain; hypothesis framing on ROI |
| AI-disabled | Explicit mode; narrator refused (AC-051) |

POC is CLI-first — messages must remain machine-readable and non-stack-trace.

## 4. Language/subgroup performance

| Finding | Stance |
|---|---|
| INJ-072 Arabic/Hindi lower extraction quality | Do **not** claim parity; flag multilingual narratives for human review; no auto-final |
| Assessed path | Deterministic rules over generative extraction |
| Eval gap | Subgroup graders deferred to Phase 6 TEVV |

## 5. Accessibility

| Finding | Stance |
|---|---|
| INJ-073 colour-only / keyboard gaps | Demo UI not production-ready; CLI primary for assessed path |
| Warnings | Prefer text status codes (`deny`, `quarantine`, `conflict`) over colour alone |
| Residual | Full a11y audit open — production blocker for UI path |

## 6. Training and competency

| Role | Competency expectation |
|---|---|
| Reviewers | Understand assist≠decide; read citations before accept |
| Operators | Offline / AI-disabled runbook (AC-052 drill still deferred) |
| Sponsors | Hypothesis framing — no false ROI from Missing baselines |

## 7. Monitoring and feedback

| Signal | Owner |
|---|---|
| AuthZ deny rate / revoke lag | Security |
| Quarantine events | Security + Quality |
| SideEffectGuard trips | Supply + Security |
| Reviewer override / feedback | Process owner (fixtures: reviewer_feedback.csv) |
| Gate fail | Evaluation |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-HF-01 | Risk | Automation bias if narrator later enabled without UX | Open |
| R-HF-02 | Gap | Accessibility + language TEVV incomplete | Open Phase 6 |
| R-HF-03 | Gap | AC-052 continuity drill | Open Phase 7 |

## Traceability and acceptance

| Claim | Control | Evidence | Result |
|---|---|---|---|
| Humans retain material authority | Decision rights + contracts | D-007; AC-023/030/041 | Pass |
| Automation bias mitigated in POC | Dual-cite; LLM off | INJ-071 controls | Pass (POC) |
| Language/a11y limits disclosed | §4–5 | Residual open | Partial |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Product | Owner | UI a11y not claimed | CLI assessed path | 2026-08-07 |
