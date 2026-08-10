# Stakeholder and Decision Rights

> Phase 1 qualification. Preserves independent Quality/Safety authority per BR-01 and `decision_rights.csv`.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Product–value lead (named TBD) |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP lead; Security lead |
| Status | Draft |
| Related requirements / ADRs | RUB-02; INJ-002, INJ-006, INJ-074 |

## Purpose

Make accountable human decision rights explicit for the three workflows, map incentive conflicts, and define escalation so AI remains advisory.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `data/stakeholders.csv` | Stakeholder list | ST-01 QP (evidence completeness); ST-02 Mfg VP (supply continuity); ST-03 Safety Head (reporting timeliness) | Vignette |
| E-002 | `data/decision_rights.csv` | Decision rights | Batch certification → EU QP, AI none; ICSR reportability → Safety Physician, AI none; stock allocation → Supply Governance Board, AI draft only | Binding for case |
| E-003 | `data/kpi_conflicts.csv` | Functional KPIs | Conflicting targets across Mfg/Quality/Safety/Clinical | Incentive tension |
| E-004 | `data/ai_use_boundaries.csv` | AI boundaries | Allowed assist vs prohibited acts | Binding |
| E-005 | `data/board_requests.csv` BR-01 | Board | No Quality-authority change | Constraint |
| E-006 | `case/INTEGRATED_CASE.md` INJ-074 | Case | Global process owner vs local legal accountability | Role conflict inject |

## 1. Stakeholder map

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Primary consumers | EU Qualified Person (batch evidence package); Global Safety Head / Safety Physician (PV package); Manufacturing VP + Supply Governance Board (supply options) | Product–value | E-001/E-002 |
| Priority axes | Completeness vs continuity vs timeliness — not automatically aligned (E-001/E-003) | Product–value | Conflict register §3 |
| Capstone delivery team | Product/value, Domain/evidence, Architecture/build, GxP, Security/privacy, Evaluation/reliability, Ops/handover — **named persons TBD (DEC-004)** | Team-3 | Charter 00 |
| External/regulatory | Inspection readiness (INJ-050 foreshadow) — system must support evidence pull, not replace accountable roles | GxP | Later defence |

## 2. RACI/RAPID decision matrix

| Decision | Recommend (AI/system) | Agree / Input | Perform / Decide (Accountable) | AI authority (E-002/E-004) |
|---|---|---|---|---|
| Batch evidence readiness state | System may propose insufficient / conflicted / ready_for_authorized_review | QA, Lab, CMO liaisons | **EU Qualified Person** decides certification | **none** for certification |
| Batch disposition (release/reject/…) | **Prohibited** for AI | — | QP / Quality system | Prohibited |
| PV duplicate/clock/listedness packaging | System may extract, cluster, cite | Affiliate PV, coding | **Safety Physician** for reportability | **none** for final reportability |
| Final seriousness/causality/signal | **Prohibited** for AI | — | Safety Physician / governance | Prohibited |
| Supply option drafting | System may generate **draft** options | Supply, Quality holds, CMO | **Supply Governance Board** allocates | **draft only** |
| Reserve/allocate/ship/recall | **Prohibited** for AI | — | Supply Governance Board / Quality | Prohibited |
| Tool allow-list / model change | Security + Architecture propose | GxP | Change control board (to be named) | Controlled |

## 3. Incentive conflicts

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Manufacturing vs Quality | Schedule adherence 98% vs RFT 96% (E-003) — throughput pressure vs containment | Do not let AI “clear” evidence to hit schedule (E-005) | BR-01 |
| Safety vs speed | Expedited_on_time 100% vs careful duplicate/clock reconciliation | AI must not finalize reportability to hit clock | E-002/E-004 |
| Clinical lock vs manufacturing | DB lock 2026-09-15 vs batch/trial convergence (NCB-204) | Separate contexts; no silent eligibility automation | Portfolio + clinical injects later |
| Global uniformity vs local accountability | INJ-074 theme (E-006) | Local legal roles remain accountable; AI cannot override | Artefact policy |

## 4. Independent review and segregation of duties

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Quality independence | Board forbids Quality-authority change (E-005); AI cannot become release authority | GxP | Hard gate |
| Build vs assure | Capstone build lead ≠ sole GxP reviewer for defence | Team-3 | Working agreements |
| Security review | Injection/poisoning/tool abuse reviewed independent of feature builder | Security | Later threat model |
| Dual control on side effects | Any future side-effect tool requires human confirmation; assessed mode keeps side effects disabled | Architecture + Security | Contracts |

## 5. Escalation and override

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Conflicted evidence | System abstains / marks conflicted; escalates to accountable human (E-002) | Workflow owner | readiness_state / required_reviews |
| Stale or denied authZ | Deny by default; escalate to IAM/owner | Security | PUB-09 later |
| Attempted prohibited action | Fail closed; incident log; no override by model | Security + GxP | Negative tests |
| Emergency / outage | AI-disabled continuity; humans use manual runbooks — no “break glass” AI disposition | Ops | Continuity requirements |

## 6. Training and adoption

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Training need | Reviewers must understand abstention, citation, and that AI summaries are non-authoritative (automation bias inject foreshadow) | Ops + GxP | Later artefact 18 |
| Adoption metric | Use of evidence-complete packages by named roles — **not** seat count alone | Product–value | Exec-communication skill |
| Multilingual | Safety narratives Arabic/Hindi quality gap foreshadowed (INJ-072) — adoption plan must not assume English-only | Evaluation | Subgroup tests later |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Named human owners for capstone roles TBD | Weak RACI | Team-3 | Before Hour 7 | Open |
| R-002 | Risk | Incentive conflicts cause pressure to weaken abstention | Safety/GxP incident | Product + GxP | Continuous | Open |
| R-003 | Assumption | Supply Governance Board is the correct allocation accountable body | Wrong escalation path | Domain | Confirm in Phase 2 | Accepted from E-002 |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| AI has no batch certification authority | E-002 | Prohibited disposition tests | decision_rights.csv | Bound |
| AI draft-only for supply | E-002/E-004 | no_side_effects tests | supply schema | Bound |
| Independent Quality authority preserved | E-005 | Defence narrative | board_requests.csv | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | GxP lead | — | — | — |
