# Stakeholder and Decision Rights

> Team3 completed artefact. Maps enterprise accountability vs system authority for the three workflows.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Product / value lead (with GxP lead) |
| Version / date | 0.3 / 2026-08-07 |
| Reviewers | Security / privacy lead; Domain lead |
| Status | Phase 1 complete (v0.3) — provisional under `hypothesis` framing |
| Related requirements / ADRs | RUB-02; INJ-002, INJ-006, INJ-074; D-005 |
| Prompt alignment | Prompt 01 stakeholder decisions; Prompt 03 PRD personas; Prompt library qualify constraints |

## Purpose

Define who is affected, who decides, where incentives conflict, and how segregation of duties and escalation work so the POC cannot absorb regulated accountability. Completion: RACI/RAPID for key decisions, conflict register, and escalation paths agreed — consistent with Prompt 02 authority boundary and Prompt 03 users.

**Cited:** `prompts/01_discovery/evidence_register.md` §5; `prompts/03_prd/prd.md` §1.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-ST-01 | `case/STAKEHOLDER_PACK.md` | Stakeholder evidence pack | Mandates, incentives, concerns, decision authority for CMO, CQO, QP, PV head, Clinical Ops, RA, Manufacturing, Supply, DPO, CISO, Biostats, Patient Safety, Investigators, Works Council, Procurement | Broader than CSV |
| E-ST-02 | `data/stakeholders.csv` | Packaged subset | ST-01 EU QP (evidence completeness); ST-02 Manufacturing VP (supply continuity); ST-03 Global Safety Head (reporting timeliness) | Only 3 rows |
| E-ST-03 | `data/decision_rights.csv` | Decision-rights extract | Batch certification → EU QP, AI none; ICSR reportability → Safety Physician, AI none; stock allocation → Supply Governance Board, AI draft only | Binding |
| E-ST-04 | `data/kpi_conflicts.csv` | KPI table | Manufacturing/Quality/Safety/Clinical target conflict | INJ-002 |
| E-ST-05 | `data/ai_use_boundaries.csv` | AI boundaries | Allowed/prohibited per use case | Hard-gate aligned |
| E-ST-06 | `case/INTEGRATED_CASE.md` INJ-074 | Role conflict inject | Global standardization vs local legal accountability | Must preserve local authority |

## 1. Stakeholder map

| Stakeholder | Interest in AEGIS | System role (allowed) | Must not lose |
|---|---|---|---|
| EU Qualified Person (ST-01) | Complete release evidence | Consumer of readiness report; never auto-certify | Final certification |
| Chief Quality Officer | Inspection readiness; independent Quality | Policy and risk acceptance outside model | Independent Quality authority (BR-01 constraint) |
| Global Safety Head (ST-03) / Safety Physician | Timely, consistent intake | Intake assist; duplicate/clock flags | Final seriousness/causality/reportability |
| Manufacturing VP (ST-02) | Continuity / schedule | Read-only ops context for evidence | Cannot bypass Quality holds via AI |
| Supply Chain VP / Supply Governance Board | Shortage response | Draft options only | Allocation/reservation execution |
| CISO | Tool poisoning, stale auth | Deny-by-default tooling | Security veto on unsigned tools |
| DPO | Purpose limitation, minimization | Privacy constraints on retrieval/export | Lawful basis decisions |
| Clinical Ops / Investigators | Trial integrity | Cited protocol/version conflicts | Eligibility/clinical confirmation |
| Works Council | Role clarity, no unfair surveillance | Transparency of AI telemetry | Consultation rights where applicable |
| Procurement | Vendor exit / concentration | Substitutable ports | Bundled lock-in without exit |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Primary users of POC | QP support staff / Quality reviewers; PV intake scientists; supply planners preparing governance packs | Product | E-ST-01, E-ST-02 |
| Accountable executives | CQO (quality system), Global PV Head (safety system), Supply Governance Board (allocation) | GxP | E-ST-01, E-ST-03 |

## 2. RACI/RAPID decision matrix

Legend: R = Recommend (system may draft), A = Accountable human, C = Consult, I = Inform. AI column is maximum system authority.

| Decision | Human A | Human R/C | AI authority | RAPID note |
|---|---|---|---|---|
| Batch certification / disposition | EU QP | Quality review, Manufacturing (C) | none | Agree/Perform remain human |
| Evidence-pack completeness call (readiness input) | Quality reviewer / QP support | System recommends gaps | recommend/cite/abstain only | Input ≠ certification |
| ICSR reportability / final causality / seriousness | Safety Physician | PV intake (C) | none | E-ST-03 |
| Duplicate candidate clustering | Safety Physician (A on merge) | Intake scientist | cluster candidates only; no irreversible merge | Abstain if uncertain |
| Stock allocation / reservation / shipment | Supply Governance Board | Supply planner | draft options only | E-ST-03 |
| Tool enablement in assessed mode | CISO + system owner | Architecture | deny unsigned/poisoned | Execution-time check |
| Accept residual risk to proceed | CQO / accountable process owner | Security, GxP | none | Assurance case later |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Does AI hold any A? | No for certification, reportability, allocation | GxP | E-ST-03, E-ST-05 |

## 3. Incentive conflicts

| Conflict | Parties | Risk to AEGIS | Mitigation |
|---|---|---|---|
| Speed vs evidence completeness | Manufacturing vs Quality/QP | Pressure to mark “ready” | Readiness enums without disposition; QP completeness priority for EU release path |
| Throughput vs deviation containment | Manufacturing vs Quality | Hide gaps | Dual-cite conflicts; abstain |
| Service level vs quality status | Supply vs Quality | Treat quarantine as available | Options must respect quality status; no status change |
| Global standard vs local accountability | Global process owner vs QP/Safety officers | Override local legal duty | INJ-074: local A retained; system shows jurisdiction |
| Privacy min vs GxP preserve | DPO vs Quality/Legal | Wrong deletion or over-retention | Purpose tags; escalate Q-005 class issues |
| Automation vs explainability | Clinical Ops vs Biostats/Investigators | Opaque transforms | Deterministic graded paths; no silent eligibility change |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Binding constraint when incentives clash | BR-01: no Quality-authority weakening; decision_rights AI=none/draft only | Product / GxP | E-ST-04, board_requests, E-ST-03 |

## 4. Independent review and segregation of duties

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| SoD rule | Builder of assist ≠ sole acceptor of residual GxP risk; Security reviews tool manifests; Evaluation sets gates before demos claimed “ready” | Whole team | Team charter |
| Independent Quality | Quality/QP retain veto on evidence sufficiency; system cannot certify | GxP | E-ST-01 |
| Dual control for high-impact options | Supply draft options require governance approval before any external execution system is invoked (out of POC scope) | Supply / GxP | E-ST-03 |
| No self-attestation | Prohibited-action tests owned by Evaluation/Security, not only Build | Evaluation | Phase 3 plan |

## 5. Escalation and override

| Trigger | Escalate to | System behaviour | Human override |
|---|---|---|---|
| Unresolved identity/unit/time/authority conflict | Domain lead + accountable reviewer | Abstain; do not “resolve” | Human documents governed resolution with citations |
| Stale entitlement / purpose mismatch | CISO / IAM | Deny | Re-issue entitlement; no cache trust |
| Poisoned or untrusted instruction in document | Security + Quality | Quarantine as data; never as tool instruction | Manual review of source |
| Demand to auto-release / auto-allocate | GxP + Product | Refuse; stop feature | Only human systems of record outside assist |
| Emergency stop / kill switch | On-call + process owner | Halt inference and side-effect ports | Manual runbooks (AI-disabled) |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Contestability | Reviewers can reject assist output and record reason; outputs are advisory inputs | Product | Artefact 04 human touchpoints |

## 6. Training and adoption

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Training focus | What the system must not do; how to read abstentions; how to run AI-disabled path; how to spot automation bias (INJ-071) | Product / HF | Artefacts 04, 18 later |
| Adoption risk | Global owners push uniform automation against local QP/Safety (INJ-074) | Product | Keep local A in RACI |
| Accessibility | Colour-only warnings and keyboard gaps are known inject themes (INJ-073)—blueprint must not rely on colour alone | HF | Artefact 04 §6 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-ST-01 | Gap | `stakeholders.csv` has only three rows | Under-coverage if CSV-only | Domain | Use stakeholder pack as primary | Mitigated |
| R-ST-02 | Risk | Manufacturing priority overrides QP completeness | Hard-gate / inspection failure | GxP | KPI conflict reviews | Open |
| R-ST-03 | Assumption | Supply Governance Board exists as named in decision_rights | Unclear real membership | Product | Case packs / later data | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Human oversight & decision rights | RACI + authz gateway | Authz deny tests (Phase 3+) | `submission/artefacts/phases/01_qualify/03_STAKEHOLDER_DECISION_RIGHTS.md` | Phase 1 complete |
| AI authority none/draft only | Contracts + product scope | Negative contract tests | `decision_rights.csv` | Bound |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 GxP | GxP | Confirm AI holds no A on certification/reportability | Confirmed via E-ST-03 | 2026-08-06 |
| Team3 Security | Security | Escalation for poisoned tools required | Added to §5 | 2026-08-06 |
