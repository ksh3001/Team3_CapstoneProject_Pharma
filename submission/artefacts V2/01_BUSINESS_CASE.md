# Business Case

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual participant names/roles to be entered by the team; see Assumption A-001) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | INJ-001, INJ-002, INJ-003, INJ-004, INJ-005, INJ-006; ASSESSMENT_RUBRIC RUB-01 (business case and no-AI comparison) |

## Purpose

This artefact supports the Phase 1 "Qualify" decision required by `runbooks/PARTICIPANT_RUNBOOK.md`: whether an AI Forward Deployed Engineering intervention is justified at all, and if so, how narrowly it must be scoped, before any model or agent design begins. Accountable owner: capstone team, pending sign-off by a nominated Business/Quality sponsor role-play. Completion criteria: problem, baseline, no-AI alternative, value hypothesis, scope, assumptions and stop/pivot criteria are evidenced and traceable to source data, per `requirements/ARTEFACT_EXPECTATIONS.md` and `DEFINITION_OF_DONE.md` §1.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `data/board_requests.csv` (BR-01) | Board request, due 2026-11-30 | Board requires a 14% reduction in end-to-end release lead time, with the explicit constraint "no specification or Quality-authority change" | Single-row source; no baseline lead-time value supplied, only the target delta — baseline must be derived separately (see Gap R-002) |
| E-002 | `data/kpi_conflicts.csv` | Functional KPI targets, undated | Manufacturing: schedule_adherence 98%; Quality: right_first_time 96%; Safety: expedited_on_time 100%; Clinical: database_lock 2026-09-15 | Confirms INJ-002 (conflicting success metrics) — no single function is rewarded for cross-functional cycle time |
| E-003 | `data/no_ai_baselines.csv` | Process-excellence team estimate (INJ-003), undated | `master_data_repair`: 38% estimated value / 10 weeks; `rules_workflow`: 27% estimated value / 6 weeks; `genai_assist`: 51% estimated value / 14 weeks | Estimates only, not measured outcomes; percentages are not confirmed additive across options (see Assumption A-002) |
| E-004 | `data/ai_use_boundaries.csv` | Executive prohibition (INJ-006), undated | Per use case, allowed vs. prohibited AI actions: batch evidence (allowed: reconcile/cite/flag/abstain; prohibited: release/reject/reprocess/recall); PV intake (allowed: extract/normalize/cluster/cite; prohibited: final causality/seriousness/reportability); supply planning (allowed: generate options; prohibited: reserve/allocate/ship) | Directly bounds the maximum permissible scope of any AI component regardless of value case |
| E-005 | `data/portfolio_products.csv` | Portfolio master, undated | NCX-101 (small molecule, marketed, 19 months to patent cliff, US/EU, risk: label divergence); NCB-204 (mAb, phase III scale-up, 108 months, Global, risk: batch/trial convergence); NCS-310 (sterile injectable, marketed/shortage, 44 months, Global, risk: cold-chain/sterility); NCR-415 (gene therapy, research, 144 months, EU/US, risk: genomic privacy) | Confirms INJ-004 (patent-cliff urgency) concentrates on NCX-101, 19 months to exclusivity loss |
| E-006 | `data/commercial_forecast.csv` | Commercial forecast, undated | NCX-101: 310,000 annual units, EU, confidence 0.62; NCB-204: 42,000 annual units, US, confidence 0.41 | Forecast confidence is below 0.7 for both rows — material uncertainty, not to be presented as a firm number |
| E-007 | `data/decision_rights.csv` | Decision-rights register, undated | batch certification → EU Qualified Person, ai_authority = none; ICSR reportability → Safety Physician, ai_authority = none; stock allocation → Supply Governance Board, ai_authority = draft only | Independently corroborates E-004: no regulated decision may carry AI authority beyond drafting |
| E-008 | `data/stakeholders.csv` | Stakeholder register, undated | ST-01 EU Qualified Person (EU, priority: evidence completeness); ST-02 Manufacturing VP (Global, priority: supply continuity); ST-03 Global Safety Head (Global, priority: reporting timeliness) | Row set is abbreviated relative to the fuller `case/STAKEHOLDER_PACK.md` narrative register — both cited, neither overrides the other |
| E-009 | `case/INTEGRATED_CASE.md` lines 48–53 (INJ-001…INJ-006) | Case narrative, embedded-inject rule (§6): all conditions disclosed, no later injects | Board compression target, conflicting metrics, no-AI challenge, patent-cliff urgency, acquisition integration, prohibited optimization | Case explicitly states participants may conclude a workflow/AI component is unjustified but must prove the decision |

## 1. Problem statement and affected decisions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What is the measurable problem? | End-to-end batch/trial/safety/supply evidence reconciliation is slow and fragmented enough that the Board has set a formal 14% end-to-end release-lead-time reduction target (E-001), while functional incentives actively conflict (E-002): Manufacturing is rewarded for throughput, Quality for deviation containment, Supply for service level, Clinical for database-lock speed. No function owns cross-functional cycle time. | Capstone team | This artefact + `templates/02_DMAIC_WORKBOOK.md` |
| Which decisions does this affect? | Three regulated decision classes are in scope per `case/INTEGRATED_CASE.md` §4 and `data/decision_rights.csv` (E-007): batch certification (EU Qualified Person), ICSR reportability (Safety Physician), stock allocation (Supply Governance Board). None may receive AI decision authority — only "none" or "draft only". | EU QP / Safety Physician / Supply Governance Board (role-played) | E-007, E-004 |
| Is the 14% target compatible with the non-negotiable constraint? | E-001's constraint is explicit: the reduction must occur "without changing registered specifications or weakening independent Quality authority." Any intervention that speeds review by narrowing Quality's evidentiary scrutiny is disqualified by definition, not merely undesirable. | Capstone team | E-001 |
| Who bears legal/regulatory accountability if the intervention is wrong? | Unchanged from today: EU QP for batch certification, Safety Physician for reportability, Supply Governance Board for allocation (E-007). The intervention may only inform these roles, never substitute for them, consistent with `.cursor/rules/pharma-fde.mdc`. | Named accountable roles (unchanged) | E-007, `.cursor/rules/pharma-fde.mdc` |

## 2. Baseline and evidence

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What is the current release-lead-time baseline? | Not directly supplied. `data/board_requests.csv` gives only the target delta (-14%) and due date (2026-11-30), not an absolute current-state figure. | Capstone team to derive from `batches.csv`/`release_packets.csv` timestamps in Phase 2 (Investigate) | Gap R-002 (below) |
| What functional KPIs exist today and do they conflict? | Yes — confirmed conflict (E-002): schedule_adherence (Manufacturing, 98%), right_first_time (Quality, 96%), expedited_on_time (Safety, 100%), database_lock (Clinical, fixed date 2026-09-15). Optimizing any one in isolation can work against end-to-end lead time (e.g., maximizing right_first_time can add review cycles). | Capstone team | E-002 |
| What portfolio pressure motivates urgency? | NCX-101 loses exclusivity in 19 months (E-005, matches INJ-004). NCS-310 is simultaneously in marketed/shortage state with cold-chain/sterility risk — relevant to Workflow C scope. NCB-204 is in phase III scale-up with batch/trial convergence risk — relevant to Workflows A and B jointly. | Capstone team | E-005 |
| How reliable is the commercial upside used to justify investment? | Low-to-moderate: forecast confidence is 0.62 (NCX-101/EU) and 0.41 (NCB-204/US) (E-006). Any ROI case must present these as ranges, not point estimates, and must not imply precision the source data does not carry. | Capstone team | E-006 |

## 3. No-AI alternative

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What do non-AI baselines claim (INJ-003)? | `data/no_ai_baselines.csv` (E-003): `master_data_repair` alone = 38% of estimated value in 10 weeks; `rules_workflow` alone = 27% of estimated value in 6 weeks; `genai_assist` = 51% of estimated value in 14 weeks. | Capstone team | E-003 |
| Does GenAI's higher estimated value justify its longer timeline and added regulated-boundary risk? | Not on this evidence alone. `rules_workflow` reaches 27% value in under half the time of `genai_assist` (6 vs. 14 weeks) with materially lower novel-technology and GxP-validation risk. `master_data_repair` (38%/10 weeks) directly attacks a plausible root cause of reconciliation delay (identifier/unit/authority inconsistency, per `case/SOURCE_SYSTEM_FACT_PACK.md`) without introducing any generative-AI GxP boundary question at all. | Capstone team — recommend sequencing, not exclusion | E-003, E-009 |
| Can non-AI options be combined to approach or exceed the GenAI estimate? | Unresolved on current evidence — the 38%/27%/51% figures are independent single-option estimates from `no_ai_baselines.csv` with no stated interaction/overlap model. Assuming simple additivity (38%+27%=65%) is not justified by the source and is flagged as Assumption A-002, not a fact. | Capstone team to test in Phase 2/3 (e.g., via `templates/02_DMAIC_WORKBOOK.md`) | Gap R-003 |
| What is the recommended sequencing? | Provisional (subject to Phase 2 evidence): sequence `master_data_repair` → `rules_workflow` first (lower risk, faster, addresses root-cause identity/authority conflicts that also block any future AI layer), then scope AI narrowly only to the residual gap that rules and clean master data cannot close — evidence reconciliation across systems with no common identifier, which is the stated purpose of Workflow A. This keeps AI's role additive and bounded rather than foundational. | Capstone team | E-003, E-004, `case/SOURCE_SYSTEM_FACT_PACK.md` |

## 4. Value hypothesis and metric tree

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Top-level metric | End-to-end release lead time, target -14% vs. baseline, by 2026-11-30, with zero specification changes and zero reduction in independent Quality authority (E-001). | Board (source of target) | E-001 |
| Supporting metrics (must not be optimized in isolation) | schedule_adherence ≥98% (Manufacturing); right_first_time ≥96% (Quality); expedited_on_time = 100% (Safety); database_lock by 2026-09-15 (Clinical) — all four from E-002, held as guardrails, not targets to trade off against lead time. | Respective functional VPs (role-played) | E-002 |
| AI-attributable value hypothesis (Workflow A) | AI-assisted evidence reconciliation reduces the *time to assemble a complete, contradiction-flagged evidence packet* for QP review — not the QP's review or certification time itself, and not by narrowing what the QP sees. Value claim must be evidenced empirically in Phase 5 (Break and recover) via before/after cycle-time measurement, not asserted here. | Capstone team | To be produced: `submission/evaluation/` cycle-time results |
| Non-value / explicitly excluded metrics | Any metric measuring speed of batch release, PV case closure, or stock allocation decisions themselves is out of scope — these remain human-only per E-004/E-007 and must never appear as an AI KPI. | Capstone team | E-004, E-007, `.cursor/rules/pharma-fde.mdc` |

## 5. Scope and exclusions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| In scope | The three mandatory workflows exactly as bounded in `case/INTEGRATED_CASE.md` §4: (A) GxP evidence reconciliation for batch-review readiness — identify gaps/contradictions/lineage only; (B) PV case-intake and signal-support — intake, duplicate detection, normalization, authority/clock/listedness evidence only; (C) bounded supply-shortage/cold-chain recovery planning — traceable options only. | Capstone team | `case/INTEGRATED_CASE.md` §4 |
| Explicitly out of scope / prohibited regardless of technical feasibility | Batch release/reject/reprocess/relabel/recall; final PV seriousness/causality/expectedness/reportability/signal-confirmation; inventory status change, capacity reservation, allocation, shipment or recall initiation without explicit authorized human approval (E-004, matching `case/INTEGRATED_CASE.md` §4 verbatim). | Capstone team | E-004 |
| Acquisition-integration scope question (INJ-005) | The recently acquired biotech's incompatible identifiers/cloud tenancy/quality procedures (per `data/organisations.csv`/`data/system_inventory.csv`, referenced in `case/INTEGRATED_CASE.md` INJ-005) are treated as a brownfield-integration input to Workflow A's evidence-authority model, not as a separate workflow. | Capstone team | INJ-005 |
| Products in scope | All four portfolio products (E-005) are potentially touched by the three workflows (NCX-101/labeling; NCB-204/batch+trial; NCS-310/cold-chain+sterility; NCR-415/genomic privacy), but the POC test data should prioritize NCB-204 and NCS-310 given their direct alignment with Workflows A and C. | Capstone team | E-005 |

## 6. Assumptions, stop/pivot criteria

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| A-001 | Team member names/roles are not recorded in supplied evidence and are not fabricated here; the team must complete the "Document control" table before submission. | Team | Team to close before final submission |
| A-002 | `no_ai_baselines.csv` value percentages (38/27/51) are treated as independent, non-additive estimates unless Phase 2/3 analysis (DMAIC) establishes an interaction model. No combined non-AI value figure is asserted in this document. | Capstone team | `templates/02_DMAIC_WORKBOOK.md` |
| Stop criterion | If Phase 2 evidence shows `master_data_repair` + `rules_workflow` alone plausibly close the majority of the lead-time gap without a generative-AI component, the team must be willing to conclude — per `case/INTEGRATED_CASE.md` §3 — that a full AI workflow is unjustified, and scope down accordingly. | Capstone team | Phase 2 DMAIC evidence |
| Pivot criterion | If evidence-authority conflicts (contextual by object/jurisdiction/effective time, per `case/SOURCE_SYSTEM_FACT_PACK.md`) prove too numerous for deterministic rules alone, narrow AI scope strictly to authority-conflict flagging (abstain-and-cite), not resolution. | Capstone team | Phase 2/3 evidence register |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Assumption | Team/owner identity not yet recorded (see A-001) | Low — administrative | Team | Before final submission | Open |
| R-002 | Gap | No absolute baseline release-lead-time figure supplied; only a -14% target delta (E-001) | High — cannot claim measured 14% improvement without a baseline | Capstone team | Phase 2 (Investigate) | Open |
| R-003 | Assumption | Non-AI option values (E-003) assumed non-additive pending interaction analysis | Medium — affects whether AI is justified at all | Capstone team | Phase 2/3 DMAIC | Open |
| R-004 | Risk | Board target (E-001) and functional KPI guardrails (E-002) may be structurally in tension (e.g., right_first_time vs. lead time) | High — could make -14% unachievable without a genuine trade-off decision, which is the Board's to make, not the AI's | Board (role-played) | Ongoing | Open |
| R-005 | Gap | Commercial forecast confidence is below 0.7 for both rows in E-006 | Medium — value case must present ranges, not point estimates | Capstone team | Before benefits-realisation sign-off | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Intervention does not weaken Quality authority (E-001) | Decision-rights model (E-007); prohibited-action contract | `evaluation/contract_samples/negative_batch_prohibited.json` via `tools/test_contracts.py` | `evaluation/contracts/batch_response.schema.json` | PASS (already verified — rejects prohibited batch actions) |
| AI scope matches `ai_use_boundaries.csv` exactly | Structured-output contracts (batch/pv/supply schemas) | `tools/test_contracts.py` | `evaluation/contract_samples/*` | PASS (6/6, already run) |
| No-AI alternative genuinely compared, not pro-forma | This artefact §3 | Team review | `templates/02_DMAIC_WORKBOOK.md` (pending) | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
