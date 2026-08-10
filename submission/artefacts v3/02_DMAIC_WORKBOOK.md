# DMAIC Workbook

> Phase 1 qualification workbook. Aligns with `process-and-lean-discovery` skill: measure before AI; non-AI fixes first where evidence supports.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Product–value lead (named TBD) |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Domain/evidence lead; GxP lead |
| Status | Draft |
| Related requirements / ADRs | RUB-01, RUB-03; artefacts 01, 03, 04 |

## Purpose

Establish Define–Measure–Analyse–Improve–Control framing for evidence-reconciliation lead time under BR-01, and sequence treatments so GenAI is not the default first lever.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `data/board_requests.csv` BR-01 | Board | −14% release lead time; no spec/Quality-authority change | Synthetic |
| E-002 | `data/no_ai_baselines.csv` | Process excellence vignette | Value%/duration for three options | Estimates |
| E-003 | `data/kpi_conflicts.csv` | Functional targets | Conflicting KPIs | No single owner |
| E-004 | `data/ai_use_boundaries.csv` | AI boundary | Allowed vs prohibited | Binding |
| E-005 | `starter/baseline_diagnostics.py` output | Clue-only diagnostic | Stale entitlement; model hash; unapproved unit map; untrusted knowledge | Incomplete by design |
| E-006 | `case/INTEGRATED_CASE.md` D04–D08, D10 | Case injects | Unit mismatch, genealogy, clocks, cold-chain, injection | Qualitative |
| E-007 | `data/decision_rights.csv` | Decision rights | Human accountability | Binding |

## 1. Define

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Problem / goal | Reduce evidence-reconciliation burden contributing to release lead time toward BR-01 −14%, without changing specs or Quality authority (E-001) | Product–value | Artefact 01 |
| Scope | Three advisory workflows only (E-004) | Architecture | Artefact 04 |
| Stakeholders / CTQ | QP: evidence completeness; Safety: reporting timeliness; Mfg/Supply: continuity — CTQ = evidence-complete package ready for authorized human decision | Domain | Artefact 03 |
| Out of scope | Autonomous disposition, final PV conclusions, stock execution (E-004/E-007) | GxP | Hard gates |
| AI assumption forbidden | Define does **not** assume GenAI is the solution (skill + INJ-003) | Product–value | No-AI comparison in 01 |

## 2. Measure

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| End-to-end release lead time | **Open measurement** — absolute baseline not in package; only −14% relative target (E-001) | Evaluation | Instrument in Phase 2 |
| Touch vs wait | **Open measurement** — case implies wait in handoffs/systems (E-006); no timestamps for full VSM | Domain | Evidence map |
| First-pass yield (evidence package) | **Definition (decision):** % of reviewer packages that require no return for missing authority/unit/time/provenance before human decision | GxP + Evaluation | To instrument |
| Cost per evidence-complete decision | **Definition (decision):** human-review minutes × rates + infra/token (if any) + rework loops; tokens alone insufficient (INJ-077 foreshadow) | FinOps/Evaluation | Later artefact 23 |
| Directional option values | **Fact (E-002):** master_data 38%/10w; rules 27%/6w; genai 51%/14w | Product–value | Cited estimates |
| Control defects already visible | **Fact (E-005):** unapproved unit mapping; stale entitlement cache; untrusted knowledge present | Security + Domain | Diagnostics capture |

### Metric formulas (as defined for this case)

| Metric | Formula / rule | Source status |
|---|---|---|
| Board target progress | `(baseline_lead_time − current_lead_time) / baseline_lead_time` | Baseline open |
| Evidence-package FPY | `packages_accepted_first_pass / packages_submitted` | To instrument |
| Prohibited-action rate | `count(prohibited_attempts_blocked_or_failed)`; target attempts executed = 0 | Contract tests later |
| Option value (vignette) | Use E-002 percentages as **directional only** | Estimate |

## 3. Analyse

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Dominant waste classes (DOWNTIME) | **Waiting** (cross-system reconciliation); **Defects** (unit/authority/clock conflicts — E-006); **Extra processing** (re-gathering evidence); **Non-utilised talent** (QP/Safety time on packaging not judgment) | Domain | Waste register below |
| Is model accuracy the root cause? | **No evidence that it is dominant.** Visible defects are identity/unit/time/authority/control (E-005/E-006). Treat as process/data/control causes first. | Product–value | Aligns with Lean skill hypothesis test |
| Top root causes (candidate) | RC1 unapproved/silent unit semantics; RC2 entitlement cache lag; RC3 equal-trust of untrusted docs; RC4 conflicting KPI incentives (E-003); RC5 fragmented authority/effective-date handling | Domain + Security | Phase 2 deepen |
| Treatment classes | Master-data resolution; deterministic validation; evidence packaging; constrained grounded AI; selective tools — **not** autonomous agents | Architecture | Improve §4 |

### DOWNTIME register (initial)

| Waste | Where | Evidence | Magnitude | Impact | VA / B-NVA / Waste |
|---|---|---|---|---|---|
| Waiting | Cross-system package assembly | E-006, E-008 case | Open | Lead time | B-NVA / Waste mix |
| Defects | Unit, genealogy, clocks, listedness | E-006 | Open | Rework, risk | Waste |
| Extra processing | Re-keying, PDF transcription themes | Case DI injects | Open | Cycle time | Waste |
| Non-utilised talent | Reviewers assembling packs | E-007 priorities | Open | Cost | B-NVA |

### AI-specific waste (forward-looking)

| Waste | Appearance | Treatment bias |
|---|---|---|
| Token / context | Oversized doc dumps (starter summarise concatenates) | Bound context; authority filter |
| Retrieval | Untrusted/outdated SOP treated as instruction | Trust gates |
| Model | Using GenAI where unit mapping rule suffices | Prefer rules (E-002/E-005) |
| Human-review | AI summary accepted despite omitted deviation (INJ-071 foreshadow) | HITL + abstention |

## 4. Improve

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Sequence | **1)** Master-data + interface unit governance **2)** Rules/workflow for authZ freshness & trust filters **3)** Constrained GenAI assist for multi-source packaging only where 1–2 leave residual narrative/conflict clustering need | Product + Architecture | DEC-010 |
| Future-state principle | Deterministic checks on low-risk paths; humans retain disposition/reportability/allocation (E-004/E-007) | GxP | Artefact 04 |
| Where AI may act | Recommend / cite / flag / abstain — **never execute** regulated acts | Security + GxP | Contracts |
| Where AI must not act | Batch disposition; final PV conclusions; reserve/allocate/ship | All | Hard stop |
| Expected impact (directional) | Non-AI waves address sizable share of E-002 value faster; GenAI adds residual packaging value if controls hold | Product–value | Revisit Hour 34 |

## 5. Control

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Process controls | Versioned contracts; additionalProperties false; execution_status not_executed; no_side_effects true | Architecture | `evaluation/contracts/` |
| Governance controls | Decision rights unchanged (E-007); independent Quality/Safety authority | GxP | Artefact 03 |
| Release gates | Schema fail, uncited fact, silent unit convert, stale authz, untrusted instruction, prohibited conclusion → block release | Evaluation | EVALUATION_PLAN |
| Continuity | AI-disabled mode required for 14-day-class continuity (INJ-082 foreshadow) | Ops | Later runbook |
| KPI governance | Do not let Manufacturing schedule_adherence override Quality RFT packaging completeness | Product + GxP | E-001 constraint |

## 6. Failure modes and verification

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| FM-01 AI releases batch | Violates E-004 | Deny by construction | Negative contract tests |
| FM-02 Silent unit conversion | Known defect class E-005/E-006 | Surface conflict; never auto-convert | PUB-01 / PUB-12 later |
| FM-03 Untrusted SOP as instruction | E-005 untrusted knowledge | Authority check | PUB-03 later |
| FM-04 Stale entitlement allows access | E-005 | Deny | PUB-09 later |
| FM-05 GenAI selected without no-AI proof | Violates Phase 1 exit | Hour-7 review against artefact 01 §3 | Qualification gate |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Absolute lead-time baseline missing | Weak benefits proof | Evaluation | Phase 2 | Open |
| R-002 | Assumption | E-002 percentages are directionally usable | Mis-sequencing investment | Product | Hour 7 | Accepted for qualification |
| R-003 | Risk | KPI conflicts persist after tooling | Local workarounds | Product | Continuous | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Non-AI first sequencing | Improve §4 | Hour-7 review | E-002 | Draft |
| Model accuracy not assumed root cause | Analyse §3 | Evidence map Phase 2 | E-005/E-006 | Draft |
| Fail-closed control | Control §5 | Contract suite | evaluation/contracts | Bound |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | Domain lead | — | — | — |
