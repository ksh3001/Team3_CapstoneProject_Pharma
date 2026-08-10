# Business Case

> Team3 completed artefact. Facts cite challenge evidence; interpretations and decisions are labelled.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Product / value lead |
| Version / date | 0.3 / 2026-08-07 |
| Reviewers | GxP lead; Evaluation lead |
| Status | Phase 1 complete (v0.3 re-run) — framing mode `hypothesis` |
| Related requirements / ADRs | RUB-01, RUB-03; D-003, D-005, D-006; INJ-001…006 |
| Prompt alignment | `prompts/PROMPT_LIBRARY.md` §1; `prompts/01_discovery.md`; `prompts/02_scqa_minto.md` |

## Purpose

Support a **testable qualification** (not a locked genAI build mandate) for a narrow evidence-assist intervention across three mandatory workflows, without automating prohibited accountability. Completion criteria: measurable problem, baseline (known vs Unknown labeled), no-AI comparison, value hypothesis, scope exclusions, and stop/pivot/falsifiers — per Prompt library “Qualify the problem” and Prompt 02 SCQA Answer.

**Prompt spine citations:** `submission/artefacts/prompts/01_discovery/`; `…/02_scqa/scqa_minto_decision_narrative.md`.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-BC-01 | `data/board_requests.csv` BR-01 | Board request; due 2026-11-30 | Target −14% `release_lead_time`; constraint: no specification or Quality-authority change | Single synthetic row; metric definition not fully operationalized here |
| E-BC-02 | `data/kpi_conflicts.csv` | Functional KPI table (as packaged) | Manufacturing 98% schedule adherence; Quality 96% RFT; Safety 100% expedited on-time; Clinical DB lock 2026-09-15 | Conflicting incentives by design (INJ-002) |
| E-BC-03 | `data/no_ai_baselines.csv` | Process-excellence estimates (as packaged) | master_data_repair 38%/10w; rules_workflow 27%/6w; genai_assist 51%/14w | Estimates are challenge claims, not measured NTG baselines |
| E-BC-04 | `data/ai_use_boundaries.csv` | Enterprise AI boundary extract | Allowed reconcile/cite/flag/abstain (batch); extract/normalize/cluster/cite (PV); generate options (supply). Prohibited release/reject/reprocess/recall; final causality/seriousness/reportability; reserve/allocate/ship | Aligns with hard gates |
| E-BC-05 | `data/decision_rights.csv` | Decision-rights extract | Batch certification / ICSR reportability: AI authority none; stock allocation: draft only | Binding for product scope |
| E-BC-06 | `data/cost_model.csv` | Cost model extract | Inference 184000 USD/mo; observability 31000; human_quality_review and medical_review listed as 0 | Incomplete cost model (INJ-077 theme) |
| E-BC-07 | `data/staff_rates.csv` | Loaded rates | Quality reviewer 92; Safety physician 165; Regulatory strategist 148 USD/hr | Used to expose hidden review cost |
| E-BC-08 | `data/portfolio_products.csv` | Portfolio | NCX-101 patent_months=19; NCB-204 batch/trial convergence risk; NCS-310 shortage/cold-chain; NCR-415 genomic privacy | Urgency and workflow focus products |
| E-BC-09 | `case/INTEGRATED_CASE.md` §§2–5 | Challenge case | Fragmented systems; mandatory workflows A/B/C; fail-closed properties | Narrative authority for scenario, not measured KPI |
| E-BC-10 | `case/STAKEHOLDER_PACK.md` | Stakeholder evidence pack | QP/PV/Quality retain human-only final authority | Complements CSV stakeholders |

## 1. Problem statement and affected decisions

**Fact:** Board request BR-01 requires −14% release lead time without changing registered specifications or weakening independent Quality authority (E-BC-01; INJ-001).

**Fact:** Functional KPIs pull in different directions—throughput, right-first-time, expedited safety timeliness, and clinical database lock (E-BC-02; INJ-002).

**Interpretation:** The binding operational problem is not “lack of a model,” but **slow, error-prone cross-system evidence reconciliation** under conflicting incentives, with pressure to cut cycle time while preserving human accountability.

**Affected decisions (human-owned):** EU batch certification readiness assessment inputs; PV case intake completeness and clock reconstruction; supply shortage / cold-chain **option** selection for governance approval.

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What problem are we solving? | Reduce time and rework to assemble trustworthy, cited evidence packs for batch review readiness, PV intake support, and supply options—without changing specs or Quality authority | Product lead | E-BC-01, E-BC-09 |
| Which decisions are affected? | Inputs to QP certification readiness; Safety Physician intake triage; Supply Governance Board option review | GxP lead | E-BC-05, E-BC-10 |
| What must remain human? | Batch certification, ICSR reportability/final safety conclusions, stock allocation/reservation/shipment | GxP / Security | E-BC-04, E-BC-05; D-005 |

## 2. Baseline and evidence

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Current-state baseline | Brownfield estate spans LIMS, MES, EBR, QMS, RIM, safety DB, serialization, spreadsheets, vendor portals; identifiers/time/authority inconsistent (`case/INTEGRATED_CASE.md` §2). Starter path shows lexical “ready,” equal trust of knowledge MD, and supply reservation mutation (`starter/legacy_pharma.py`) | Domain lead | Case §2; starter as anti-pattern evidence |
| Lead-time target | −14% release lead time by 2026-11-30, with Quality-authority constraint | Product lead | E-BC-01 |
| Portfolio pressure | NCX-101 exclusivity pressure (19 months); NCB-204 and NCS-310 concentrate batch/PV/supply risk | Product lead | E-BC-08; INJ-004 |
| Cost baseline gap | Published cost model zeroes human Quality and medical review while carrying large inference spend—baseline understates full operating cost | Evaluation / FinOps | E-BC-06, E-BC-07; INJ-077 |
| Measurable proxy KPIs (Team3) | (1) Median hours to complete evidence pack for a batch readiness review; (2) % packs with unresolved identity/unit/time/authority conflicts correctly flagged (not silently closed); (3) PV intake packets with clock provenance complete; (4) Supply option sets with `no_side_effects` and zero inventory mutations; (5) Full operating cost = inference + observability + measured human review hours × rates | Evaluation lead | To be instrumented in Phase 6; thresholds justified pre-result |

## 3. No-AI alternative

| Option | Estimated value % | Duration weeks | Source |
|---|---:|---:|---|
| master_data_repair | 38 | 10 | E-BC-03 |
| rules_workflow | 27 | 6 | E-BC-03 |
| genai_assist | 51 | 14 | E-BC-03 |

**Interpretation:** GenAI assist claims the highest single-option value but longest duration. Master-data repair plus rules/workflow redesign can be sequenced sooner and attack root causes named in D01–D05 (identity, units, authority, validation state).

**Decision D-006 (Phase 1, hypothesis experiment):** Prefer a **Measure-first hybrid qualification order**: (1) master-data repair and rules/workflow redesign as primary value levers; (2) a **narrow deterministic evidence-assist POC** (optional later LLM narrative assist only) bounded by E-BC-04/E-BC-05; (3) do **not** select genAI as the sole intervention or as a substitute for MDM/rules. Framing remains `hypothesis` until acquisition backlog P0 items (cycle-time baseline, knowledge SoT, entitlement SoT) land — see Prompt 01 sufficiency scores.

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Is AI mandatory? | No. Package allows deterministic non-LLM design. No-AI baselines claim material value without generative AI | Product / Architecture | E-BC-03; A-002; PACKAGE_SCOPE |
| Buy/build/partner | Build narrow offline-capable assist under Team3 control; partner only for substitutable model ports with exit (INJ-078/083 themes deferred to artefacts 23/27) | Architecture | D-003 |
| What no-AI delivers first | Identifier/unit/authority repair; checklist and schema gates; manual runbooks for 14-day batch/supply AI outage and PV without inference | Domain / Reliability | E-BC-03; `continuity_requirements.csv` |

## 4. Value hypothesis and metric tree

**Hypothesis:** If NTG first reduces evidence conflicts via master-data and rules, and then uses a fail-closed assist to cite gaps/contradictions/options, then release-pack cycle time and PV intake rework fall **without** increasing Quality or Safety override rates—and without autonomous disposition.

**Metric tree**

- Outcome: release lead time (board); expedited PV on-time; shortage option latency to governance
- Drivers: evidence-pack completeness time; conflict-detection precision/recall (human-graded); abstention rate on unresolved conflicts; prohibited-action attempt blocks
- Costs: inference (if any) + observability + human review hours × staff rates (force non-zero review cost vs E-BC-06 zeros)
- Constraints: zero autonomous release/PV-final/allocate; Quality authority unchanged (E-BC-01)

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Primary value claim | Cycle-time and rework reduction in evidence reconciliation; improved inspection-ready provenance | Product | E-BC-01, E-BC-09 |
| Counter-metric | Independent Quality/Safety override and reopen rates must not worsen | GxP | Stakeholder pack concerns |
| Cost honesty | Business case must include human review at staff rates even if cost_model lists 0 | FinOps | E-BC-06, E-BC-07 |

## 5. Scope and exclusions

**In scope (POC):** Workflows A `batch_evidence`, B `pv_intake`, C `supply_options` with versioned contracts, offline deterministic mode, AI-disabled continuity, evaluation gates.

**Out of scope / excluded:** Autonomous batch disposition; final PV decisions; inventory reservation/allocation/shipment; quality-status change; recall initiation; changing registered specifications; weakening QP/Quality independent authority; clinical eligibility determination.

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Narrower than business problem? | Yes—assist evidence readiness and options only; board lead-time goal is enterprise outcome, not a license to automate certification | Product | E-BC-01, E-BC-04 |
| Systems touched (read) | Challenge `data/` CSVs, `knowledge/` with authority filter, public fixtures; no mutation of package `data/` | Build | D-001 |

## 6. Assumptions, stop/pivot criteria

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Key assumptions | A-002 deterministic core sufficient for assessed mode; E-BC-03 percentages are directional only; human review cost currently understated in cost_model | Product | Assumptions log |
| Stop | Any path enables prohibited action; cannot preserve provenance/authority/time/units; cannot operate 14 days AI-disabled for batch/supply (and PV without inference per continuity CSV); unreproducible eval | Whole team | Hard gates; continuity_requirements.csv |
| Pivot | If MDM+rules alone meet ≥ board-relevant cycle-time proxy without assist, defer/cancel generative features and keep schema/checklist tooling only | Product | E-BC-03; measured Phase 6 |
| Pause | Unresolved identity/unit/authority conflicts treated as “resolved” by software; or exec pressure to auto-release | GxP | R-002 |

## 7. Benefits-realisation plan

| Wave | Action | Owner | Evidence of benefit |
|---|---|---|---|
| 0–2 weeks | Qualify problem; freeze intended/prohibited uses | Product / GxP | This artefact; artefact 04 |
| 2–10 weeks | Master-data repair backlog from evidence register (Phase 2+) | Domain | Conflict closure tickets with dual citation |
| Parallel 6 weeks | Rules/workflow checklists and contract gates | Architecture | Failing→passing prohibited-action tests |
| Capstone POC window | Deterministic three-workflow assist + offline/manual paths | Build | PUB fixtures; `--final` structure |
| Defence | Report residual risk and go/conditional-go/pivot/stop | Whole team | Artefact 30 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-BC-01 | Risk | Board −14% target drives prohibited automation | Hard-gate failure | Product / GxP | Any release/disposition feature request | Open |
| R-BC-02 | Gap | True current lead-time distribution not in package | Proxy KPIs required | Evaluation | Phase 6 instrumentation | Open |
| R-BC-03 | Assumption | no_ai_baselines percentages are comparable and additive only with caution | Over/under-claim value | Product | Better measurement | Open |
| R-BC-04 | Risk | Zeroed human review in cost_model hides true TCO | False positive ROI | FinOps | Artefact 23 | Open |

## SCQA summary (from Prompt 02)

| Element | Content |
|---|---|
| Situation | Fragmented brownfield; BR-01 −14% lead time without Quality-authority change |
| Complication | KPI conflict; unsafe starter; MDM/rules vs genAI estimates; Unknown cycle-time baseline |
| Question | What capability to qualify/test first without transferring accountability? |
| Answer | Measure-first hybrid experiment: MDM+rules + narrow deterministic assist; genAI optional/off by default |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Qualify the problem (Prompt library §1) | SCQA + this business case | Phase 1 prompt revise | `prompts/02_scqa/scqa_minto_decision_narrative.md` | Aligned |
| Sufficiency / framing mode | Prompt 01 register | Hypothesis until P0 backlog | `prompts/01_discovery/evidence_register.md` | `hypothesis` |
| Measurable problem + no-AI challenge | Business case + DMAIC | Phase 1 review | `submission/artefacts/phases/01_qualify/01_BUSINESS_CASE.md` | Provisional complete |
| Hard-gate scope | Intended/prohibited uses | Contract negatives | `ai_use_boundaries.csv`; artefact 04 | Bound |
| Cost honesty | FinOps model includes human review | Artefact 23 later | `cost_model.csv` + `staff_rates.csv` | Deferred |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 GxP lead | GxP | Confirm exclusions match decision_rights | Accepted D-005/D-006 | 2026-08-06 |
| Team3 Evaluation lead | Evaluation | Proxy KPIs needed until true baseline measured | Accepted R-BC-02 | 2026-08-06 |
