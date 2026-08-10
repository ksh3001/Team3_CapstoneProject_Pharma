# Stakeholder and Decision Rights

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Product / value lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | GxP & quality lead |
| Status | Draft |
| Related requirements / ADRs | Artefact 01; `case/STAKEHOLDER_PACK.md`; `data/stakeholders.csv`; `data/decision_rights.csv`; INJ-002, INJ-074 |

## Purpose

Make accountable human decision rights explicit for AEGIS-supported workflows and document incentive conflicts that can pressure unsafe automation.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `case/STAKEHOLDER_PACK.md` | Case stakeholder pack | Mandates, incentives, concerns, authorities | Synthetic |
| E-002 | `data/stakeholders.csv` | Stakeholder rows | ST-01 EU QP evidence completeness; ST-02 Mfg VP supply continuity; ST-03 Global Safety Head reporting timeliness | Sparse sample |
| E-003 | `data/decision_rights.csv` | Decision rights | Batch certification / ICSR reportability AI=none; stock allocation draft only | Binding |
| E-004 | `data/kpi_conflicts.csv` | KPI targets | Mfg/Quality/Safety/Clinical conflict | INJ-002 |
| E-005 | `data/ai_use_boundaries.csv` | AI boundaries | Allowed vs prohibited per workflow | Binding |

## 1. Stakeholder map

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| EU Qualified Person | Needs complete release evidence; final certification human-only | QP accountable | E-001, E-002 ST-01, E-003 |
| Chief Quality Officer | Protects independent Quality authority; inspection readiness | CQO policy | E-001 |
| Global Head of PV / Safety Physician | Timely consistent cases; final safety decisions human-only | Safety Physician for reportability | E-001, E-003 |
| Manufacturing VP | Supply continuity / schedule adherence — tension with holds | Ops only; never independent release | E-001, E-002 ST-02, E-004 |
| Supply Chain VP | Service continuity; allocation needs approvals | Supply Governance Board | E-001, E-003 |
| CISO / DPO | Tool poisoning, stale auth, privacy/minimisation vs retention | Security/Privacy risk acceptance | E-001 |
| Clinical Ops / Biostatistics / Investigators | Protocol integrity; resist opaque AI transforms | Clinical governance | E-001 |
| Procurement vs Architecture | Bundled vendor vs substitutability | Contracting with control owners | E-001 conflicts |

## 2. RACI/RAPID decision matrix

| Decision | Accountable (A) | AI authority | Consult / Inform | Evidence |
|---|---|---|---|---|
| Batch certification / disposition | EU QP | none | Quality, Manufacturing (I) | E-003 |
| Declare batch evidence ready for review | QP / delegated reviewer | reconcile/cite/flag/abstain only | QA | E-005 |
| ICSR reportability / seriousness / causality / expectedness / signal confirmation | Safety Physician / PV Head | none for finals; extract/cluster/cite allowed | Affiliates, medical | E-003, E-005 |
| Stock allocation / reservation / shipment / recall initiation | Supply Governance Board (+ Quality where status) | draft options only | Manufacturing, Clinical demand | E-003, E-005 |
| Accept AI system for GxP-relevant use | CQO + validation owner | n/a | CISO, DPO | E-001 |
| Override AI abstention | Same accountable human role | cannot self-approve | Audit trail required | Working agreement |

## 3. Incentive conflicts

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Speed vs completeness | Manufacturing 98% schedule adherence vs Quality 96% RFT / QP evidence completeness | CQO binding on release evidence | E-004, E-002 |
| Safety timeliness vs quality of coding | Safety 100% expedited on-time vs multilingual/duplicate uncertainty | PV Head — no silent merge | E-004; INJ-037–039 |
| Global standardization vs local accountability | Global process owners vs QP/Safety legal accountability | Local accountable role wins on regulated decision | E-001 INJ-074 |
| Privacy vs GxP retention | DPO minimisation vs legal hold LH-44 / retention rules | Restriction/segregation not blind delete | `legal_holds.csv`, `retention_rules.csv`, `deletion_requests.csv` |

## 4. Independent review and segregation of duties

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Build vs assure | Build lead artefacts reviewed by Evaluation lead on contracts | Team charter | `team_charter_and_working_agreements.md` |
| GxP vs security | GxP artefacts reviewed by Security lead and vice versa | Team charter | Same |
| AI cannot certify | ai_authority=none for certification/reportability | System control | E-003 |
| Stale entitlement | Revoked IAM user must not retain AI gateway access | CISO | `users_entitlements.csv` contractor_77 |

## 5. Escalation and override

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Conflict unresolved | System abstains; escalate to accountable role | Workflow engine | Contract abstentions |
| Inspection surge (72h) | Traceable evidence pack; no fabrication | Regulatory + Quality | INJ-050 |
| Emergency stop | Kill switch / AI-disabled continuity | CISO + ops | continuity_requirements; knowledge AI_DISABLED_CONTINUITY |
| Override AI | Human accountable role only; reason + audit | Same as decision matrix | E-003 |

## 6. Training and adoption

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Automation bias risk | Reviewers may accept incomplete AI summaries (INJ-071) | HF / Quality training | Later artefact 18 |
| Accessibility | Colour-only warnings / keyboard gaps (INJ-073) | Product | Later tests |
| Multilingual | Arabic/Hindi extraction weaker (INJ-072) | PV + Eval | Subgroup gates |
| Adoption principle | Train on abstention and conflict display, not “trust the summary” | Product | This § |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Risk | KPI pressure bypasses evidence completeness | Hard-gate failure | CQO | Ongoing | Open |
| R-002 | Gap | Full RACI for all 15 stakeholders not yet workshopped | Ambiguous consult paths | Product | Phase 2 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| AI authority none for certification/reportability | Decision matrix | Prohibited-action tests | E-003 | Pending build |
| Conflicts documented | §3 | Checkpoint C1 | This artefact | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| GxP lead | Reviewer | QP independence explicit | Confirmed in §2 | 2026-08-07 |
