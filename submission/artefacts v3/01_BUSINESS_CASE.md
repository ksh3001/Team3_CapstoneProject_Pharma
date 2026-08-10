# Business Case

> Participant working template completed for Phase 1 qualification. Facts cite challenge evidence; open measurements and assumptions are labelled.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Product–value lead (named owner TBD — DEC-004) |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP lead; Security lead (pending named assignment) |
| Status | Draft |
| Related requirements / ADRs | RUB-01, RUB-03; INJ-001, INJ-002, INJ-003, INJ-006; DEC-010 |

## Purpose

Support the Hour-7 qualification decision: whether a **bounded, fail-closed AI-assisted evidence-reconciliation intervention** is justified versus no-AI alternatives, within board constraints and without weakening Quality/Safety authority.

**Completion criteria:** measurable problem, cited baselines, no-AI comparison, narrower AI scope than the business problem, and explicit stop/pivot thresholds.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `data/board_requests.csv` BR-01 | Board request; due 2026-11-30 | Release lead time target **−14%**; constraint: no specification or Quality-authority change | Synthetic challenge record |
| E-002 | `data/no_ai_baselines.csv` | Process-excellence estimate (challenge vignette) | master_data_repair 38%/10w; rules_workflow 27%/6w; genai_assist 51%/14w | Estimates only — not measured plant data |
| E-003 | `data/kpi_conflicts.csv` | Functional KPI targets | Mfg schedule_adherence 98%; Quality RFT 96%; Safety expedited_on_time 100%; Clinical DB lock 2026-09-15 | Conflicting incentives; no single enterprise KPI owner |
| E-004 | `data/ai_use_boundaries.csv` | Executive AI boundary | Allowed/prohibited uses for batch, PV, supply | Binding prohibited-action set |
| E-005 | `data/decision_rights.csv` | Decision rights matrix | QP / Safety Physician / Supply Governance Board retain AI-none or draft-only | Legal accountability remains human |
| E-006 | `data/portfolio_products.csv` | Portfolio | NCB-204 phase_III_scaleup; NCS-310 cold-chain/sterility risk; NCX-101 patent_months=19 | Urgency context, not a release metric |
| E-007 | `data/stakeholders.csv` | Stakeholder priorities | QP: evidence completeness; Mfg VP: supply continuity; Safety Head: reporting timeliness | Three priority axes |
| E-008 | `case/INTEGRATED_CASE.md` §2–4 | Case narrative | Fragmented systems; evidence reconciliation mandate; three mandatory workflows | Narrative; not quantitative baseline |

## 1. Problem statement and affected decisions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What is the problem? | **Fact (E-001):** Board requires −14% end-to-end release lead time by 2026-11-30 without changing registered specifications or Quality authority. **Interpretation (E-008):** Lead time is dominated by evidence reconciliation across fragmented LIMS/MES/EBR/QMS/safety/supply systems, not by a single model accuracy gap. | Product–value lead proposes; Board accepts problem framing | Business case reviewed at Hour 7 |
| Which decisions are affected? | Batch-review readiness packaging; PV intake support packaging; supply option drafting. **Not affected (E-004/E-005):** batch certification, ICSR reportability, stock allocation execution. | Decision rights owners remain QP / Safety Physician / Supply Governance Board | `03_STAKEHOLDER_DECISION_RIGHTS.md` |
| SCQA Question | Should NTG fund a **fail-closed evidence-reconciliation assist** for three workflows, sequenced after/with master-data and rules fixes, under BR-01 constraints? | Product–value lead | Hour-7 go/conditional-go on qualification |

## 2. Baseline and evidence

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Current baseline lead time (hours/days) | **Open measurement** — package does not supply a numeric current-state release lead time. Only the relative −14% target exists (E-001). | Evaluation lead to define measurement method in Phase 2 | Measurement plan before POC KPI claims |
| No-AI value estimates | **Fact (E-002):** master_data_repair ≈38% value / 10 weeks; rules_workflow ≈27% / 6 weeks; genai_assist ≈51% / 14 weeks | Compare options in §3 | Trace to `no_ai_baselines.csv` |
| KPI tension | **Fact (E-003):** Manufacturing rewards schedule adherence; Quality rewards RFT; Safety rewards expedited on-time; Clinical rewards DB lock date — simultaneous optimization creates reconciliation pressure | Do not optimize one KPI by weakening Quality authority (E-001) | KPI conflict register in DMAIC |
| Portfolio pressure | **Fact (E-006):** NCX-101 exclusivity pressure (19 months); NCB-204 batch/trial convergence; NCS-310 shortage/cold-chain | Scope POC to NCB-204 / NCS-310 / PV anchors first | Anchor entities in EXECUTION_PLAN |

## 3. No-AI alternative

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Master-data repair alone | **Fact (E-002):** estimated 38% of target value in 10 weeks — material, faster than genAI-alone calendar | Prefer as **first wave** for identity/unit/authority collisions | Phase 2 evidence map owns master-data gaps |
| Rules / workflow redesign | **Fact (E-002):** 27% / 6 weeks — fastest calendar; addresses handoffs/waiting (Lean) | Prefer for deterministic checks (unit mapping approval, entitlement freshness) | DMAIC Improve sequence |
| GenAI assist alone | **Fact (E-002):** 51% / 14 weeks — highest estimated value but longest and still must respect E-004 | Only as **assist** after/with non-AI waves; never autonomous | Hard gates in scoring model |
| Combined recommendation | **Decision:** Sequence master-data + rules first for solvable identity/unit/control waste; add constrained GenAI for cross-system evidence packaging where humans still reconcile narrative/conflict clusters. GenAI scope **narrower** than BR-01 business problem. | Product–value + Architecture | DEC-010 |

## 4. Value hypothesis and metric tree

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Value hypothesis | Reducing **time-to-evidence-complete package** for authorized reviewers (not time-to-autonomous-decision) can contribute toward BR-01 −14% **without** changing specs or Quality authority | Product–value | Defence value case |
| CTQ tree (summary) | Board need: faster release lead time → driver: fewer reconciliation loops → CTQs: evidence completeness rate; conflict surfacing latency; first-pass evidence package yield; cost per evidence-complete decision; zero prohibited autonomous acts | GxP + Evaluation | DMAIC Measure set |
| Primary success metric | **Time-to-evidence-complete readiness package** for batch/PV/supply support jobs (definition to be instrumented — currently open measurement) | Evaluation lead | Must not use “batch released by AI” as success |
| Guardrail metrics | Prohibited-action attempt = 0; stale-authz denies; untrusted-instruction rejects; AI-disabled continuity operable | Security + GxP | Hard gates |

## 5. Scope and exclusions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| In scope | Three fail-closed workflows: batch evidence readiness; PV intake/signal **support**; supply draft options | Architecture | Artefact 04; contracts |
| Out of scope / prohibited | Release/reject/reprocess/relabel/recall; final PV seriousness/causality/expectedness/reportability/signal; reserve/allocate/ship/quality-status change (E-004) | All leads | Contract negatives |
| Excluded products for v1 POC | Full NCR-415 gene-therapy commercial path (privacy-heavy); treat as future | Product–value | Portfolio risk E-006 |
| Architecture exclusion (Phase 1) | No model selection, RAG platform, or agent topology decisions yet | Architecture | Phase 3–5 |

## 6. Assumptions, stop/pivot criteria

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| A-P1-01 | Relative −14% can be pursued without a published absolute baseline if we instrument current-state during Phase 2 | Evaluation | Open measurement closure |
| A-P1-02 | `no_ai_baselines.csv` percentages are comparable directional estimates, not audited finance numbers | Product–value | Labelled as estimates in all decks |
| Stop | Any design that requires AI to hold disposition/reportability/allocation authority (violates E-004/E-005) | GxP + Security | Immediate stop |
| Pivot | If master-data + rules deliver ≥ board-acceptable portion of −14% with lower residual GxP risk, defer GenAI or shrink to rules-only packaging | Product–value / Board | Hour-7 and Hour-34 reviews |
| Pause | Offline/AI-disabled path not demonstrable before defence | Ops / Evaluation | Continuity gate |

## 7. Benefits-realisation plan

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Wave 0 (now–Hour 12) | Qualify + evidence map; freeze intended/prohibited uses | Domain + Product | Artefacts 01–04; inject register start |
| Wave 1 | Deterministic reconciliation + contracts (non-model) | Architecture | Phase 3–5 deterministic mode |
| Wave 2 | Optional bounded inference behind ports (scaffolding Part A) only if Wave 1 gaps remain | Architecture | SKILL_AI_Python_scaffolding |
| Benefits tracking | Track evidence-complete cycle time, human-review minutes, prohibited-action blocks, cost per successful assist | Evaluation + FinOps | Artefact 22–23 later |
| Realisation owner | Named workflow owners: QP (batch package consumer), Safety Physician (PV), Supply Governance Board (options) | Per E-005 | RACI in artefact 03 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Absolute current release lead time not in package | Cannot prove −14% numerically yet | Evaluation | Phase 2 measurement | Open |
| R-002 | Risk | KPI conflicts drive local optimization against Quality authority | False “throughput wins” | Product + GxP | Continuous | Open |
| R-003 | Assumption | GenAI 51% estimate is optimistic if trust/control overhead dominates | Over-invest in model | Product | Hour-34 cost review | Open |
| R-004 | Risk | Named role owners still TBD (DEC-004) | Weak accountability | Team-3 | Before Hour 7 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| AI scope narrower than BR-01 problem | Intended/prohibited uses (04) | Review vs E-004 | This artefact §5–6 | Draft |
| No autonomous regulated decisions | Decision rights (E-005) | Contract negatives (later) | `ai_use_boundaries.csv` | Bound |
| No-AI alternatives compared | §3 | Hour-7 qualification | `no_ai_baselines.csv` | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | GxP lead | — | — | — |
| Pending | Product–value | — | — | — |
