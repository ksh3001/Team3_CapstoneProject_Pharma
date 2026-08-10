# Elevator Pitch and Defence

> Team3 Phase 8 artefact (template 30). Executive + technical defence under **hypothesis** framing.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Product / Whole team |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Evaluation; Security; GxP; Sponsors |
| Status | Phase 8 — ready for defence |
| Related | Prompt 13 proposal; Phases 0–7; D-012/D-026 |

## Purpose

Deliver a 60-second pitch, 5-minute executive narrative, control boundary proof, residual-risk honesty, and the decision requested of sponsors — backed by live failure demos.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-DEF-01 | `artefacts/prompts/13_proposal/solution_proposal.md` | Governing answer |
| E-DEF-02 | `failure_demo_results.csv` | 8/8 demos pass |
| E-DEF-03 | Phase 5 assurance case C0/C0′ | Demo vs prod claims |
| E-DEF-04 | Phase 7 prod checklist | no_go / conditional_go |
| E-DEF-05 | pytest suite | 51+ tests green |

## 1. 60-second pitch

**AEGIS is a fail-closed Evidence Assist for NovaCura’s fictional Quality, PV, and Supply workflows — not a decision engine.**

It cites and flags conflicts, drafts supply options, and stops revoked users, poisoned instructions, dispositions, reservations, and AI narration on the assessed path. Hard gates are green on package fixtures. We recommend a **conditional demo** and a clear **production no-go** until cycle-time and review-hour baselines, a continuity drill, and fuller TEVV close. Humans keep certification, final PV, and allocation. Framing remains **hypothesis** — we will not invent a −14% board win from Missing data.

## 2. Five-minute executive narrative

1. **Pressure:** Board wants faster release evidence without weakening Quality authority.  
2. **Reality:** Brownfield conflicts, stale AuthZ cache, untrusted docs, quarantine-as-available, and uncounted review cost. Inference is modeled high; human review lines are zero in the cost model — TCO is incomplete.  
3. **Choice:** Hybrid Measure-first — MDM/rules first; narrow deterministic assist; genAI off by default.  
4. **What we built:** CLI runtime for batch / PV / supply + AuthZ + evaluate; schemas reject prohibited fields; SideEffectGuard; offline/AI-disabled modes.  
5. **What we proved live:** Deny contractor_77; reject disposition; block reservation; refuse narrator; entitled pack still returns `not_executed` with conflicts visible.  
6. **What we did not prove:** Ops cycle-time cut, continuity drill, full 12-suite TEVV, Act class, validated DSS.  
7. **Ask:** Approve conditional demo; fund P0 Measure; deny production DSS and write-plane now.

## 3. Problem and measurable impact

| Claim type | Status |
|---|---|
| Control outcomes (AuthZ, no disposition/side effects, LLM=0) | **Measured on fixtures** — met |
| Pack cycle-time / board −14% | **Unknown** — do not claim |
| Review-hour TCO | **Unknown** — cost_model gap |
| Continuity 14-day drill | **Deferred** (AC-052) |

Impact we defend: **prevented unsafe automation** and **honest scarcity labeling**, not invented ROI.

## 4. Bounded intervention

| In | Out |
|---|---|
| Cite / flag / abstain / draft options | Disposition / release / recall |
| Purpose-bound AuthZ | Entitlement grant by AI |
| Quarantine untrusted docs | Treating poison as policy |
| Draft supply options | Reserve / allocate / ship |
| PV intake packet | Final seriousness/causality/reportability |
| Optional LLM port | LLM on assessed path |

## 5. Strongest control boundary

**IAM over cache + schema wall + no write adapters + AI kill switch.**

Live demos D1–D4 prove the negative path; D5–D8 prove assist still works without transferring authority.

## 6. Evidence and residual risk

| Evidence | Pointer |
|---|---|
| Failure demos | `failure_demo_results.csv` (8/8) |
| Assurance case | Phase 5 tmpl 21 |
| TEVV honesty | Phases 5–6 |
| Residuals blocking prod | RR-01, RR-02, RR-05, RR-09 |

## 7. Decision requested

| # | Decision | Team3 ask |
|---|---|---|
| S1 | Demo PoC under hypothesis? | **Yes** (conditional-go) |
| S2 | Grant P0 data access? | **Grant** |
| S3 | Fund SME review-hour + drill? | **Fund** |
| S4 | Production / validated DSS now? | **No-go** |
| S5 | Enable LLM assessed? | **Keep off** |
| S6 | Authorize write plane? | **Deny** |
| S7 | Accept RR-01/05 for beyond-demo claims? | **Reject overclaim** |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-DEF-01 | Risk | Panel hears “works” as “production ready” | Mitigate via §1/§7 |
| R-DEF-02 | Gap | No browser UI — CLI demos only | Accepted POC |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Pitch matches no-go/conditional-go | §1 + Phase 7 | Pass |
| Live failure demos | failure_demo_results.csv | Pass 8/8 |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Product | Owner | Defence pack complete | Phase 8 exit | 2026-08-07 |
