# Production Readiness

> Team3 Phase 7 artefact (template 28). Canonical stance: demo **conditional-go** / production **no-go** (D-012).

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Evaluation / Product |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Security; GxP; Architecture; Sponsors |
| Status | Phase 7 — **production no-go** |
| Related | Prompt 12 residual risks; Phase 5 scorecard; Phase 6 TEVV |

## Purpose

Record readiness checklist, open defects/risk acceptances, security/privacy/GxP gates, performance, ops support, and explicit go/no-go conditions for production vs demo.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-PRD-01 | `12_assurance/production_readiness.md` | PoC vs prod table |
| E-PRD-02 | `residual_risk_register.md` | RR-01/02/05/09 blockers |
| E-PRD-03 | Phase 5 scorecard; Phase 6 tevv results | Honesty map |
| E-PRD-04 | `production_readiness_checklist.csv` | Machine checklist |
| E-PRD-05 | pytest suite | Hard gates green |

## 1. Readiness checklist

| Item | Demo | Production |
|---|---|---|
| Three workflows fail-closed | **Ready** | Pattern only — needs SoT IAM/DocMgmt |
| Hard-gate tests green | **Ready** | Required + live integrations |
| AuthZ IAM>cache pattern | **Ready** (CSV) | Real IAM/OIDC required |
| Offline / AI-disabled unit | **Ready** | Drill evidence required (AC-052) |
| Full TEVV 12 suites | Partial | **Not ready** |
| Validated GxP DSS claim | Out of scope | **Not ready** / denied now |
| Observability / on-call | Local files | **Not ready** |
| P0 baselines / honest TCO | Missing | **Not ready** |
| EU AI Act class | Abstained (Q-EU-01) | Legal required |

Companion: [`production_readiness_checklist.csv`](production_readiness_checklist.csv).

## 2. Open defects and risk acceptances

| ID | Item | Disposition |
|---|---|---|
| RR-01 | Cycle-time / review-hour Unknown | Accept for **demo messaging only**; block ROI |
| RR-02 | AC-052 drill missing | Deferred — blocks prod |
| RR-05 | No validated DSS | Accept — no claim |
| RR-09 | Incomplete TEVV | Deferred — blocks prod |
| RR-04 | Fuzzy FN | Accept fail-closed |
| RR-03 | Thin QP-only AuthZ roles | Accept POC |
| AMB-PV-01 | Fuzzy blocked | Open-blocked |

## 3. Security/privacy/GxP gates

| Gate | Status |
|---|---|
| Prohibited actions fail closed | **Pass** (tests) |
| Poisoned tool/doc controls | **Pass** (POC) |
| Privacy full suite / DPIA | **Fail / open** for prod |
| Part 11 / Annex 11 validation package | **Not claimed** |
| Remote access / SSO hardening | **Fail** for prod |

## 4. Performance and capacity

| Topic | Status |
|---|---|
| p95 ≤30s under load | **inconclusive** (RR-12) |
| Capacity / HA / DR | Out of POC |
| Token DoW | N/A (LLM=0) |

## 5. Operational support

| Topic | Status |
|---|---|
| Runbooks | Phase 6 IR + this TOM — **partial** |
| On-call / paging | **Absent** |
| Continuity drill | **Open** |
| Handover owners | Named in template 26 |

## 6. Release/rollback decision

| Track | Decision |
|---|---|
| Demo / pilot showcase | **Conditional-go** — disclose residuals; hypothesis framing |
| Production release | **No-go** — do not deploy as GxP DSS or write-plane system |
| Rollback | N/A for undelivered prod; demo = git + re-pytest |

## 7. Conditions for go/no-go

**Production go requires all of:**

1. P0 baselines acquired or explicitly assumed in writing (clears RR-01 path)  
2. AC-052 continuity drill evidence (RR-02)  
3. TEVV expansion to Evaluation-agreed bar (RR-09)  
4. Real IAM + purpose matrix beyond QP-only CSV  
5. Security/privacy residual acceptance by CISO/DPO  
6. Legal Act classification (Q-EU-01) if market-facing  
7. Sponsor written acceptance of remaining residuals  
8. **Still** no write-plane unless ADR-003 superseded with full reopen  

**Demo go requires:** pytest green; evaluate `ready_blocked=false`; residual disclosure; no ROI overclaim.

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-PRD-01 | Risk | Pressure to treat conditional demo as prod go | Open |
| R-PRD-02 | Gap | Clean-room `--final` / artefact-30 defence next phase | Open Phase 8 |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Production no-go documented | §6–7 + CSV | Pass |
| Demo conditional-go documented | §6 | Pass |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Evaluation | Owner | No-go upheld | Aligns D-012/D-021 | 2026-08-07 |
