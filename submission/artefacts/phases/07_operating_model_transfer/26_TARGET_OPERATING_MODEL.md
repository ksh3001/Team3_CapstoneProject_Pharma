# Target Operating Model

> Team3 Phase 7 artefact (template 26). Operating model for **demo/pilot assist** — not a production validated-DSS org design.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Product / Ops |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Security; GxP; Evaluation |
| Status | Phase 7 — provisional (hypothesis) |
| Related | D-007; Prompt 13 §15; production_readiness; Phase 4–6 |

## Purpose

Define capabilities, forums, run/change/control roles, service management, AI-asset governance, competency, and KPIs so handover transfers **demo authority with residuals**, not production go.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-TOM-01 | `artefacts/prompts/13_proposal/solution_proposal.md` §15–16 | Adoption + roadmap |
| E-TOM-02 | `12_assurance/production_readiness.md` | Domain owners |
| E-TOM-03 | Phase 1 decision rights; Phase 4 AuthZ matrix | Accountability |
| E-TOM-04 | `capability_owners.csv` | Machine-readable RACI slice |

## 1. Capabilities and ownership

| Capability | Owner | AEGIS role |
|---|---|---|
| Purpose-bound AuthZ | Security / CISO | Check + audit |
| Document applicability | Document control | Quarantine / include |
| Batch evidence assist | Quality / QP support | Pack only — QP certifies outside |
| PV intake assist | PV / Global Safety | Packet only — Safety decides outside |
| Supply options draft | Supply + Governance Board | Draft options — Board allocates |
| Evaluate / hard gates | Evaluation / Quality Systems | Block ready |
| Continuity / AI-disabled | Ops + Architecture | Mode kill switch |
| Product framing / claims | Product + CQO | Hypothesis until P0 |

Companion: [`capability_owners.csv`](capability_owners.csv).

## 2. Decision forums

| Forum | Decides | Does not decide |
|---|---|---|
| Capstone Team3 standup | POC scope, ADR reopen flags | Regulated release/PV/allocation |
| Evaluation gate review | ready_blocked / demo conditional-go | Production go alone |
| Quality / QP context | Certification (outside AEGIS) | — |
| Safety Physician context | Final PV (outside) | — |
| Supply Governance Board | Allocation (outside) | — |
| Sponsor forum | S1–S7 (Prompt 13) | Must not rubber-stamp ROI without baselines |

## 3. Run/change/control roles

| Function | Run | Change | Control |
|---|---|---|---|
| Runtime CLI/workflows | Build / Ops | Architecture | Evaluation gates |
| Contracts/schemas | Build | Architecture + Evaluation approval | additionalProperties denial |
| Entitlements | Security | IAM admin | AuthZ audits |
| Knowledge corpus | Doc control | Doc control + Security quarantine | Applicability tests |
| Optional LLM port | — (off) | ADR-002 revisit | Mode controller |
| Write plane | **Absent** | Requires ADR-003 reopen | SideEffectGuard |

## 4. Service management

| Item | POC TOM | Production gap |
|---|---|---|
| Service hours | Best-effort workshop | Defined SLA |
| Incident | Phase 6 playbook | On-call + SIEM |
| Request types | Pack / options / evaluate | Ticketed SoR integrations |
| Continuity | Unit AI-disabled | AC-052 drill evidence |

## 5. Model/data/prompt/tool governance

| Asset | Governance |
|---|---|
| Model | None on assessed path; registry hash before enable (INJ-070) |
| Prompts | N/A assessed; if narrator later — versioned, cited-only context |
| Tools | No poisoned manifest; no write tools |
| Data | Challenge immutable; purpose-bound ACL; privacy Phase 4 |
| Schemas | VERSION 1.0.0-poc pin; Evaluation for bumps |

## 6. Competency and training

| Audience | Must know |
|---|---|
| Reviewers | Assist ≠ decide; read citations; contest conflicts |
| Operators | Offline / ai_disabled; never expose unbound without authn |
| Sponsors | Hypothesis framing; incomplete TCO; prod no-go |
| New joiners | Run `pytest submission/tests`; read residual register |

## 7. KPIs and continuous improvement

| KPI | POC status | Target next |
|---|---|---|
| Hard-gate pass rate | Met (pytest) | Keep 100% |
| Side effects / LLM assessed | 0 / 0 | Keep |
| Pack cycle-time median/p90 | **Unknown** | P0 acquire (M1) |
| Review hours × rates | **Unknown** | P0/P1 sample |
| HITL queue depth/age | Unmeasured | Instrument M1 |
| Continuity drill | Deferred | Execute ≤90d |

Improve via Measure-first — do not fund agent/RAG scale in M1.

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-TOM-01 | Gap | Org AIMS / validated ops not stood up | Accepted training |
| R-TOM-02 | Risk | TOM misread as production go | Mitigate via § Purpose + D-012 |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Owners named for BCs | §1 + CSV | Pass |
| Production authority not transferred | Purpose + forums | Pass |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Product | Owner | Demo TOM only | Aligns D-012 | 2026-08-07 |
