# DMAIC Workbook

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Product / value lead + Evaluation lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Domain & evidence lead |
| Status | Draft — Define/Measure started Phase 1; Analyze/Improve/Control deepen in Prompt 09 |
| Related requirements / ADRs | Artefact 01; Prompts 01–03; INJ-003, 075–077, 082 |

## Purpose

Define the improvement problem and Measure plan for evidence-reconciliation lead time across the three mandatory workflows, without treating estimated `% value` rows as measured baselines.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `data/board_requests.csv` BR-01 | Board; due 2026-11-30 | −14% release_lead_time target | Baseline Unknown |
| E-002 | `data/no_ai_baselines.csv` | Estimates | 38%/27%/51% options | Not measured |
| E-003 | `data/kpi_conflicts.csv` | Functional KPIs | Conflicting targets | Incentive waste driver |
| E-004 | `data/cost_model.csv` + `staff_rates.csv` | Cost evidence | Inference priced; human review $0 | Hidden review cost |
| E-005 | `data/continuity_requirements.csv` | Continuity | Manual runbooks required; batch/supply 14d; PV hours=0 | AI-disabled Control |
| E-006 | `starter/baseline_diagnostics.py` | Clue | 4 integrity findings | Incomplete |
| E-007 | `submission/artefacts/01_BUSINESS_CASE.md` | Phase 1 | SCQA answer + scope | Draft |

## 1. Define

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Problem | Reconciliation of multi-system evidence for batch readiness, PV intake, and supply options is slow and error-prone under conflicting KPIs | Product | E-001, E-003, E-007 |
| In-scope improvement | Fail-closed reconciliation + draft options + HITL; master-data/rules first | Product | Artefact 01 §3–5 |
| Out of scope | Autonomous regulated decisions; silent unit/conflict resolution | GxP | `ai_use_boundaries.csv` |
| Customer of process | EU QP, Safety physician, Supply Governance Board | Decision rights | `decision_rights.csv` |
| Early wastes (hypothesized) | Waiting (approvals/data); Extra processing (re-checks); Defects (unit/hash/authority); Motion (system switching); Token/Model waste if GenAI unbounded | Domain | E-003, E-006; mark hypothesized |
| Success measures | See Measure; align to BR-01 contribution + zero hard-gate breaches | Eval | §2 |

## 2. Measure

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| M1 Release reconciliation cycle time | **Unknown** baseline — must instrument before claiming −14% | Eval | E-001 |
| M2 Conflict/gap detection rate | Count of cited contradictions/gaps per batch/case/event vs silent pass | Eval | Contract fields |
| M3 Prohibited-action attempts blocked | 100% of negative contract fixtures fail closed | Build | `test_contracts.py` PASS |
| M4 Human review hours | Currently $0 in cost_model — measure actual Quality/medical hours at staff_rates | FinOps | E-004 |
| M5 AI-disabled operability | Manual path for batch/PV/supply within continuity limits | Reliability | E-005 |
| M6 Subgroup/language quality | Non-English PV extraction quality (INJ-072) — baseline Unknown | Eval | Later suite |
| Measure-first rule | Because framing is hypothesis on %, do not scale GenAI before M1/M4 sampling | Product | E-002 |

## 3. Analyse

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Root cause themes (preliminary) | Identity/unit/time/authority conflicts; fragmented SoT; stale auth; untrusted docs; KPI speed pressure | Domain | E-006; SOURCE_SYSTEM_FACT_PACK |
| Why GenAI alone insufficient | Estimated non-AI value large; prohibited autonomy; cost model incomplete | Product | E-002, E-004 |
| Deeper Analyze | Full DOWNTIME + AI-waste registers deferred to Prompt 09 after contracts | Eval | Prompt 09 |

## 4. Improve

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Improve-1 | Master-data + interface unit approval workflow | Domain | interface_mappings approved=no |
| Improve-2 | Deterministic three-workflow engines against schemas | Build | evaluation/contracts |
| Improve-3 | Current authorization check (deny stale cache) | Security | users_entitlements |
| Improve-4 | Optional LLM behind interface only after Measure | Architecture | Artefact 01 |
| Not yet | Agent topologies, KG — unjustified until DDD/KG decision (Phase 2) | Architecture | Prompt 04/08 |

## 5. Control

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Release gates | Schema fail / fabricated fact / unresolved conflict presented as resolved / stale auth / untrusted instructions / prohibited side effect / missing manual mode → block | Eval | EVALUATION_PLAN |
| Continuity | AI-disabled runbooks required | Reliability | E-005 |
| Cost control | Denial-of-wallet + include human review in FinOps | Security/FinOps | INJ-076/077 |
| Revisit | If M1 shows rules/master-data close gap, pivot GenAI scope | Product | Artefact 01 §6 |

## 6. Failure modes and verification

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Silent unit conversion | Must abstain/flag; mapping approved=no | GxP | interface_mappings |
| Untrusted SOP as instruction | Must not follow injection text | Security | knowledge_catalog untrusted; INJ-065 |
| Automation bias | Reviewer accepts incomplete summary | HF lead | INJ-071 later tests |
| Verification now | Contract positive/negative tests PASS | Build | preflight_report |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | M1 baseline Unknown | Cannot close BR-01 claim | Eval | Phase 6 | Open |
| R-002 | Assumption | Early waste list hypothesized | Wrong Improve order | Domain | Prompt 09 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Define complete for Phase 1 | SCQA in artefact 01 | Checkpoint C1 | artefacts 01–02 | Draft |
| Measure plan lists Unknowns | §2 | Prompt 09 deepen | This artefact | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Domain lead | Reviewer | Keep Analyze thin until evidence map | Accepted — Prompt 09 | 2026-08-07 |
