# Business Case

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Product / value lead (Team 3) |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Domain & evidence lead (independent no-AI challenge) |
| Status | Draft |
| Related requirements / ADRs | Phase 1; Prompts 01–03; INJ-001–006; hard gates SCR |

## Purpose

Support the board/capability decision: what bounded intervention Project AEGIS-PHARMA should pursue first to reduce evidence-reconciliation lead time across Quality, Safety and Supply **without** changing registered specifications or weakening independent Quality / PV / allocation accountability.

**Narrative class:** `hypothesis` approaching capability `decision-ready` — Situation/Complication are fact-backed; numeric value percentages in `no_ai_baselines.csv` are estimates (not measured baselines).

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `data/board_requests.csv` BR-01 | Board request; due 2026-11-30 | Target −14% release lead time; constraint: no specification or Quality-authority change | Single request row; baseline lead time Unknown |
| E-002 | `data/kpi_conflicts.csv` | Functional KPI targets (as recorded) | Manufacturing 98% schedule adherence; Quality 96% RFT; Safety 100% expedited on-time; Clinical DB lock 2026-09-15 | Targets conflict; not reconciled |
| E-003 | `data/no_ai_baselines.csv` | Process-excellence estimates | master_data_repair 38%/10w; rules_workflow 27%/6w; genai_assist 51%/14w | Estimated value_pct — not measured |
| E-004 | `data/portfolio_products.csv` | Portfolio snapshot | NCX-101 patent_months=19; NCB-204 phase_III_scaleup risk batch/trial; NCS-310 marketed_shortage | Forecast confidence separate |
| E-005 | `data/commercial_forecast.csv` | Forecast | NCX-101 EU 310000 units conf 0.62; NCB-204 US 42000 conf 0.41 | Confidence moderate/low |
| E-006 | `data/ai_use_boundaries.csv` | AI use boundary register | Allowed reconcile/cite/flag/abstain; PV extract/normalize/cluster; supply options only. Prohibited disposition/final PV/reserve-allocate-ship | Binding for solution design |
| E-007 | `data/decision_rights.csv` | Decision rights | Batch certification / ICSR reportability AI authority=none; stock allocation draft only | Aligns with hard gates |
| E-008 | `data/cost_model.csv` | Cost model | inference 184000 USD/mo; human_quality_review 0; medical_review 0; observability 31000 | Human review cost omitted (INJ-077) |
| E-009 | `data/staff_rates.csv` | Loaded rates | Quality reviewer 92; Safety physician 165; Regulatory strategist 148 USD/hr | Used to challenge zeroed review cost |
| E-010 | `case/INTEGRATED_CASE.md` §2–4 | Case narrative | Converging batch/PV/supply crises; three mandatory workflows | Synthetic case |
| E-011 | `case/STAKEHOLDER_PACK.md` | Stakeholder pack | QP/PV/Quality accountability human-only; Manufacturing vs Quality conflict | Deliberate conflicts |
| E-012 | `starter/baseline_diagnostics.py` output | Diagnostic clue | Stale entitlement cache; model hash mismatch; unapproved unit mapping; untrusted knowledge | Incomplete assessment by design |

## SCQA / Minto (Prompt 02)

**Situation (fact):** NovaCura operates fragmented LIMS/MES/eBR/QMS/safety/supply systems (`case/SOURCE_SYSTEM_FACT_PACK.md`). Board request BR-01 requires −14% release lead time by 2026-11-30 without specification or Quality-authority change (E-001).

**Complication (fact + derivation):** Concurrent batch genealogy/unit/OOS conflicts, PV duplicate/clock/listedness issues, and cold-chain/shortage pressures (E-010) collide with conflicting KPIs (E-002). AI is prohibited from regulated conclusions (E-006/E-007). Current cost model prices inference but zeros human Quality/medical review (E-008 vs E-009). Process-excellence estimates show substantial non-GenAI value (E-003).

**Question:** What bounded capability should AEGIS deliver first to cut evidence-reconciliation time while preserving human accountability and an offline/AI-disabled path?

**Answer (capability-level; hypothesis on % value):** Ship a **deterministic, fail-closed evidence-reconciliation and option-drafting capability** for the three mandatory workflows, front-loading master-data/rules remediation and Measure instrumentation; treat generative AI as an optional, replaceable assist behind contracts — never as the authority for disposition, final PV, or allocation.

### Minto pyramid

1. **Governing answer:** Bounded reconciliation + draft options + HITL; no autonomous regulated decisions.
2. **MECE supports:** (a) Board constraint preserves Quality authority (E-001/E-007); (b) No-AI options already claim 38%+27% estimated value (E-003); (c) Fail-closed contracts already executable (`tools/test_contracts.py` PASS); (d) Cost model understates human review (E-008/E-009); (e) Continuity requires manual runbooks (`data/continuity_requirements.csv`).

## 1. Problem statement and affected decisions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Core problem | Evidence required for batch-review readiness, PV intake clocks/duplicates, and supply options is scattered, conflicting, and slow to reconcile under inspection pressure | Product/value lead | E-010; INJ-021–028, 037–044, 051–058, 050 |
| Affected decisions | QP release readiness review; Safety physician reportability/causality (human); Supply Governance Board allocation (human) | Accountable roles per E-007 | `decision_rights.csv` |
| What must not be automated | release/reject/reprocess/recall; final causality/seriousness/reportability; reserve/allocate/ship | Security/GxP leads | E-006; scoring hard gates |

## 2. Baseline and evidence

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Lead-time baseline | Numeric current release lead time **Unknown** in supplied CSVs; only −14% target exists | Evaluation lead — Measure backlog | E-001; mark Unknown |
| No-AI estimates | master_data_repair 38%/10w; rules_workflow 27%/6w; genai_assist 51%/14w | Product lead — treat as hypothesis | E-003 |
| Integrity baseline clues | Unapproved mg/L→µg/mL mapping; revoked user still active in AI gateway; model hash mismatch; untrusted knowledge | Domain lead | E-012; `interface_mappings.csv`; `users_entitlements.csv`; `model_artifacts.csv` |
| Portfolio pressure | NCX-101 exclusivity 19 months; NCB-204 scale-up; NCS-310 shortage | Product lead | E-004, E-005 |

## 3. No-AI alternative

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Master-data repair | Estimated 38% value in 10 weeks — must remain in scope even if AI proceeds | Domain lead | E-003 INJ-003 |
| Rules / workflow redesign | Estimated 27% value in 6 weeks — prefer for unit/authority/clock rules | Architecture lead | E-003 |
| GenAI assist alone | Estimated 51%/14w but longest; cannot justify skipping Measure or human review cost | Product lead | E-003, E-008 |
| Decision | Do **not** select GenAI as first-line without bundling master-data + rules + HITL; AI optional behind interface | Product + Domain (challenger) | This artefact §3 |

## 4. Value hypothesis and metric tree

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Primary metric | Release evidence-reconciliation cycle time (contribute to BR-01 −14%) | Product lead | E-001 |
| Quality metric | % batch packets reaching `ready_for_authorized_review` without fabricated resolution of conflicts | GxP lead | Contract readiness_state enum |
| PV metric | Time-to-complete intake pack with clock evidence + duplicate candidates for human review; 0 autonomous reportability | PV accountable | E-006 |
| Supply metric | Time-to-produce ranked **draft** options with `no_side_effects=true` | Supply governance | E-006 |
| Cost metric | Fully loaded cost = inference + human review (Quality/medical rates) + observability | FinOps/Eval lead | E-008, E-009 |
| Stop if | Hard gate breached; or no Measure baseline after pilot window; or human-review cost ignored in go-live case | Product lead | §6 |

## 5. Scope and exclusions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| In scope (v1) | Three workflows: batch evidence reconciliation; PV intake/signal support; supply/cold-chain option drafting; offline/AI-disabled continuity | Build lead | E-010; E-006; continuity_requirements |
| Out of scope | Autonomous batch disposition; final PV decisions; stock reservation/allocation/shipment/recall; clinical eligibility determination; changing registered specifications | GxP/Security | E-001, E-006, E-007 |
| Explicit exclusion | Do not “clean” deliberate data conflicts in challenge evidence | Domain lead | `PACKAGE_SCOPE_AND_ASSUMPTIONS.md` |

## 6. Assumptions, stop/pivot criteria

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| A-P1-01 | `no_ai_baselines` percentages are estimates, not measured | Product | E-003 |
| A-P1-02 | Offline deterministic mode is mandatory for assessment regardless of later model choice | Build | Package scope |
| Stop | Any path enables prohibited side effect or uses untrusted doc/tool as instruction | Security | Hard gates |
| Pivot | If Measure shows ≥80% of BR-01 gap closed by master-data+rules alone, defer GenAI scale-up | Product | E-003 |
| Pause | If AI-disabled runbooks cannot operate batch/PV/supply within continuity limits | Reliability | continuity_requirements |

## 7. Benefits-realisation plan

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Phase A | Instrument baselines; master-data/rules for units, clocks, authority | Domain + Eval | Measure plan in artefact 02 |
| Phase B | Deterministic three-workflow POC against public fixtures | Build | PUB-01–08 |
| Phase C | Optional model assist behind contracts; FinOps includes human review | Architecture + Eval | E-008/E-009 fix |
| Benefits proof | Before/after reconciliation time + failed-gate rate + review hours | Eval lead | Artefact 22 later |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Current release lead-time baseline Unknown | Cannot prove −14% yet | Eval | Phase 6 Measure | Open |
| R-002 | Risk | Cost model zeros human review | Overstated AI ROI | Product | Before defence | Open |
| R-003 | Assumption | Estimated no-AI % value directionally useful | Wrong prioritization | Domain | Pilot Measure | Open |
| R-004 | Risk | KPI conflicts drive unsafe speed pressure | Bypass evidence completeness | CQO/QP | Ongoing | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| No autonomous disposition/PV final/allocate | Fail-closed schemas | `tools/test_contracts.py` | `evaluation/contracts/*` | PASS |
| No-AI comparison documented | Business case §3 | Checkpoint C1 review | This artefact | Draft |
| Board constraint respected | Scope exclusions | Defence prohibited-action demo | E-001, E-006 | Pending build |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Domain & evidence lead | Challenger | GenAI % must not suppress master-data/rules | Captured in §3 Decision | 2026-08-07 |
