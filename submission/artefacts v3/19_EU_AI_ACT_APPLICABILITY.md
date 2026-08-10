# EU AI Act Applicability

> Phase 4. Awareness / delivery design only — **not** a legal classification or “Act compliant” claim.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Security–privacy + GxP |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Product; Architecture |
| Status | Draft |
| Related requirements / ADRs | DEC-010/012; artefact 04/13; trust-risk-security skill |

## Purpose

Frame likely EU AI Act questions for NovaCura’s advisory evidence assist so delivery controls stay conservative and open legal items are escalated — not self-certified.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | artefact 04 / ai_use_boundaries | Advisory intended use; prohibited autonomous acts |
| E-002 | artefact 13 | GxP-relevant support; not release system |
| E-003 | decision_rights.csv | Named human decision owners |
| E-004 | Package scope | Synthetic training vignette |
| E-005 | trust-risk-security skill | Deployer vs provider; escalate classification |

## 1. Intended purpose and actor role

| Item | Working position (escalate) |
|---|---|
| Intended purpose | Evidence packaging assist for human GxP/safety/supply decisions |
| NovaCura role (case) | Likely **deployer** of an internal assist; if building/hosting the model system, provider obligations may also attach |
| Capstone team role | Design/build of POC controls — not conformity assessment body |

## 2. System and component boundary

| In AI system boundary | Out of boundary |
|---|---|
| Optional LLM port, retrieval, response packaging UI | Validated LIMS/MES/QMS source systems |
| Deterministic detectors + schemas | Human QP/Safety/Supply decisions |
| Tool allowlist enforcement | Physical manufacturing execution |

## 3. Risk classification analysis

| Lens | Working analysis | Open question |
|---|---|---|
| Prohibited AI | Not designed for social scoring / exploitation etc. | Confirm no prohibited pattern creeps in |
| High-risk (Annex III-style) | Healthcare/GxP adjacency + influence on safety-related human decisions may attract heightened scrutiny | **Legal must classify** — do not self-declare high-risk or not |
| GPAI | Only if a general-purpose model is integrated as component | Provider obligations may flow via supplier |
| Limited / transparency | If chatbot-like UI, users must know they interact with AI | UX labelling required |

**Delivery posture:** Design **as if** heightened obligations apply (HITL, logging, risk mgmt, human oversight) while marking formal class as **unresolved**.

## 4. Prohibited/high-risk/transparency considerations

| Topic | Control already chosen |
|---|---|
| Human oversight | Mandatory; no autonomous regulated acts |
| Transparency | Label assist; show conflicts/uncertainty |
| Accuracy/robustness | Contract tests; offline deterministic mode |
| Data governance | Provenance, purpose, residency flags |
| Logging | Audit object on every response |

## 5. Provider/deployer obligations

| Obligation theme | POC mapping |
|---|---|
| Instructions for use | Artefact 04 + runbooks (Phase 7) |
| Human oversight | Artefacts 03, 18 |
| Risk management | Artefacts 15, 16, 20 |
| Post-market monitoring | Monitoring § in 18/20 — lightweight for POC |
| Fundamental rights impact | Privacy artefact 17; escalate DPIA if real data |

## 6. Evidence and assumptions

| ID | Statement |
|---|---|
| A-024 | Formal EU AI Act class is an open legal question; capstone uses conservative controls without claiming conformity |
| Fact | Assessed mode is synthetic/offline |
| Decision | DEC-041: no “EU AI Act compliant” claim in defence materials |

## 7. Change triggers

| Trigger | Action |
|---|---|
| Scope expands to autonomous disposition/reportability/allocate | **Stop** (DEC-011) + reclassify |
| Real patient data / production deploy | Legal + DPIA/AIA before go-live |
| GPAI model swap | Supplier file + eval refresh |
| UI becomes customer-facing chatbot | Transparency duties review |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-431 | Gap | No external legal opinion | Mis-class risk | Privacy/GxP | Open |
| A-024 | Assumption | Conservative advisory design is acceptable interim posture | Under/over control | Legal escalate | Accepted for POC |

## Traceability and acceptance

| Claim | Control | Evidence | Result |
|---|---|---|---|
| No conformity claim | DEC-041 / §6 | Defence checklist | Draft |
| Oversight & logging present | §4–5 | Contracts + audit field | Draft |
| Open class documented | §3 | This artefact | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | GxP / Privacy | Pending | | |
