# Product and Service Blueprint

> Phase 1 qualification. Defines intended/prohibited uses and human-review touchpoints for the three fail-closed workflows. No implementation.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Product–value lead (named TBD) |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP lead; Architecture lead |
| Status | Draft |
| Related requirements / ADRs | RUB-02, RUB-08; E-004 ai_use_boundaries; workflow skills |

## Purpose

Describe the service users experience when using evidence-reconciliation **assist** — what the system may do, must never do, where humans decide, and how failure/recovery works — so Phase 3+ contracts and POC stay inside authority bounds.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `data/ai_use_boundaries.csv` | AI boundary | Allowed/prohibited per workflow | Binding |
| E-002 | `data/decision_rights.csv` | Decision rights | Accountable humans; AI none/draft only | Binding |
| E-003 | `data/stakeholders.csv` | Stakeholders | QP, Mfg VP, Safety Head priorities | Vignette |
| E-004 | `starter/contracts/WORKFLOW_CONTRACTS.md` + `evaluation/contracts/*.schema.json` | Package contracts | Fail-closed response shapes | Executable later |
| E-005 | `.cursor/skills/gxp-evidence-reconciliation.md` etc. | Skill bounds | Batch/PV/supply skill limits | Short skills |
| E-006 | `data/usability_findings.csv` / INJ-072–073 (case) | HF injects | Accessibility & language risks | To deepen Phase 4 |
| E-007 | `data/board_requests.csv` BR-01 | Board | Lead-time pressure without authority change | Constraint |

## 1. Personas and jobs-to-be-done

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Persona A — EU Qualified Person | JTBD: Obtain an evidence-complete, conflict-surfaced batch readiness package before certification decision | QP accountable (E-002) | Batch workflow |
| Persona B — Safety Physician / PV scientist | JTBD: Intake support with duplicates/clocks/listedness context without losing verbatim uncertainty | Safety Physician (E-002) | PV workflow |
| Persona C — Supply planner / governance | JTBD: See ranked **draft** shortage/cold-chain options with constraints and approvals required | Supply Governance Board (E-002) | Supply workflow |
| Persona D — Capstone operator (AI-disabled) | JTBD: Continue packaging via deterministic/manual path when models unavailable | Ops | Continuity |

## 2. Intended and prohibited uses

| Workflow | Intended (allowed) — E-001 | Prohibited — E-001/E-002 |
|---|---|---|
| **Batch evidence** | Reconcile, cite, flag gaps/contradictions, abstain, propose readiness_state for authorized review | Release, reject, reprocess, relabel, recall; any `batch_disposition` |
| **PV intake** | Extract, normalize (without destroying verbatim), cluster duplicates, cite clocks/terminology/listedness, list required reviews | Final causality, seriousness, expectedness, reportability, signal confirmation |
| **Supply planning** | Generate draft options with constraints, quality holds, approvals_required; `no_side_effects: true` | Reserve, allocate, ship, change quality status, initiate recall; reservations |

**Product principle:** AI/system output is an **evidence packaging assist**, not a decision. Success = faster evidence-complete handoff to the accountable human.

## 3. Frontstage/backstage workflow

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Frontstage (user) | Select workflow → provide object IDs / purpose / as-of → receive structured package (evidence, contradictions, gaps, abstentions, human_review) → human decides outside or beside system | Product | Later UI |
| Backstage | Load challenge/submission data; check authZ; apply trust/authority filters; deterministic conflict detectors; optional model behind port (future); emit schema-valid response with `execution_status: not_executed` | Architecture | Contracts E-004 |
| Line of visibility | Users see citations and conflicts; users do **not** see raw tool write paths (none in assessed mode) | Security | Tool policy later |
| Sequence with non-AI | Master-data/rules fixes remain outside or upstream of assist (artefact 02) | Product | DEC-010 |

## 4. Human review touchpoints

| Touchpoint | Trigger | Accountable role | AI role |
|---|---|---|---|
| Batch certification | readiness_state ready_for_authorized_review **or** conflicted/insufficient escalated | EU QP | Package only |
| PV medical/safety review | required_reviews includes safety physician; duplicate/clock conflicts | Safety Physician | Package only |
| Supply allocation meeting | Draft options + approvals_required | Supply Governance Board | Draft only |
| Trust exception | Untrusted doc / stale authZ / unsigned tool | Security + data steward | Deny / abstain |
| Automation-bias check | AI summary present | Reviewer must see omitted critical items surfaced as gaps | Never hide gaps |

## 5. Failure and recovery journey

| Failure | User-visible behaviour | Recovery |
|---|---|---|
| Conflicted units/identity/time | readiness/PV/supply shows contradictions; abstention | Human resolves with source authority; no silent convert |
| AuthZ deny | Request denied with reason | Refresh IAM; no cache-only allow |
| Untrusted instruction in doc | Doc not executable; flagged | Use approved effective SOP only |
| Model outage | Deterministic/AI-disabled path | Manual runbook; no degraded autonomous writes |
| Prohibited request | Schema/tool rejection | Incident note; no override by model |
| Partial agent resume (supply) | No duplicate reservations (side effects off) | Idempotent draft regenerate |

## 6. Accessibility and multilingual experience

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Accessibility | Case flags keyboard/colour-only risks (INJ-073 / usability findings) — **requirement**: warnings not colour-only; keyboard operable demonstrator | Product + Evaluation | Phase 4/6 tests |
| Multilingual | PV language inequity foreshadowed (INJ-072) — system must surface uncertainty, not silently drop non-EN/DE content | Evaluation | Subgroup suite |
| Phase 1 status | Requirements noted; UX not built | Architecture | Open |

## 7. Success measures

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Primary | Reduction in time-to-evidence-complete package for Personas A–C (open measurement to instrument) | Evaluation | Align artefact 01 |
| Quality guardrails | 0 prohibited executions; conflicts not presented as resolved; citations present for material facts | GxP + Evaluation | Contract/TEVV |
| Adoption | Named accountable roles use packages in review — not seat metrics alone | Product | Artefact 03 |
| Continuity | Successful AI-disabled path demonstration | Ops | Defence item |
| Non-goals | Autonomous release rate; “cases closed by AI”; stock reserved by AI | All | Hard fail if pursued |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | UI/accessibility not designed | Demo risk | Product | Phase 5 app | Open |
| R-002 | Risk | Users treat readiness_state as release authority | Regulatory incident | GxP | Training + UX copy | Open |
| R-003 | Assumption | Three personas cover mandatory workflows | Missing persona | Product | Phase 2 | Accepted for v1 |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Intended/prohibited uses documented | §2 | Hour-7 review | ai_use_boundaries.csv | Draft |
| Human touchpoints named | §4 | RACI match artefact 03 | decision_rights.csv | Draft |
| Fail-closed journeys defined | §5 | Later negative tests | evaluation/contracts | Bound |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | GxP lead | — | — | — |
| Pending | Architecture lead | — | — | — |
