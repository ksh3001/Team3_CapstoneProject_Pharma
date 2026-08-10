# AEGIS Evidence Assist — Final Solution Proposal

| Field | Entry |
|---|---|
| Prompt | `prompts/13_solution_proposal.md` |
| Skills | `exec-communication`; Lean rollup from Prompt 12 |
| Audience | Board / CQO / CISO / PV / Supply sponsors; defence panel |
| As-of | 2026-08-06 |
| Assurance basis | `12_assurance/evaluation_report.md` |

---

## 0. Evidence confidence summary (lead with scarcity)

| Item | Status |
|---|---|
| **Framing mode** | **`hypothesis`** — not upgraded to decision-ready |
| Artifact status | **provisional** (PRD, DDD, C4, contracts) |
| Sufficiency (Prompt 01) | Material P0 baselines **Missing/Partial** (cycle-time, review hours; package hash CRLF residual) |
| Assurance | Hard-control ACs **verified** on fixtures; ops outcomes largely **`inconclusive (data scarcity)`** |
| Demo path | **conditional-go** (disclose residuals) |
| Production / validated DSS | **no-go** |

**Known:** Fail-closed assist patterns work on package fixtures (AuthZ revoke+cache; unit conflict dual-cite; doc quarantine; no disposition/reservation; LLM off).  
**Assumed:** Interim conflict block lists, multilingual always-HITL, released-only supply, dual-cite clocks.  
**Unknown:** Ops median/p90 pack cycle-time; actual review hours; board −14% achievability; fuzzy threshold; full continuity drill pass.

Sponsors should fund **evidence acquisition and Control** before genAI scale or production authority transfer — not only the solution vision below.

---

## 1. Problem statement (SCQA compressed)

**Situation.** NovaCura Therapeutics Group (NTG, fictional challenge estate) must improve evidence flow for batch readiness, PV intake, and supply planning under board pressure for −14% release lead time (BR-01) without weakening Quality authority.

**Complication (assumption-heavy magnitude).** Evidence is slow and conflict-prone across brownfield systems (**hypothesized** ops waste). Package **observed** defects include unit/spec mismatch (LR-88), unapproved mappings, revoked user with active cache, untrusted knowledge, quarantine treated as available, and starter reservation side effects. Inference cost is modeled high while human review hours are uncounted. AI-EVIDENCE validation state is conflicted — blocking any “validated decision support” claim.

**Question.** What should Team3 qualify first so reconciliation waste can fall **without** transferring regulated accountability to software?

---

## 2. Governing answer (Minto)

**Continue the Measure-first hybrid experiment; demo the fail-closed Evidence Assist PoC; do not authorize production GxP decision support.**

| MECE reason | Summary |
|---|---|
| **R1 Control first** | Prohibited actions and side effects are blocked and tested — accountability stays human |
| **R2 Narrow assist** | Cite/flag/abstain/options only — matches `ai_use_boundaries` and decision rights |
| **R3 Parallel no-AI** | MDM + rules remain the preferred waste removers; genAI stays off by default |
| **R4 Measure gap** | Cycle-time/review baselines Unknown — ROI and −14% claims would invent facts |
| **R5 Assurance** | Demo conditional-go; production no-go until scarcity and DoD gaps close |

---

## 3. PRD scope (this version)

**In scope (demonstrated intent):** batch evidence reconciliation support; PV intake support; supply option drafting; purpose-bound AuthZ; authority-aware documents; offline/AI-disabled continuity design; evaluation hard gates; Measure instrumentation.

**Out of scope (non-negotiable):** autonomous disposition/release; final PV seriousness/causality/expectedness/reportability/signal confirmation; reserve/allocate/ship/quality-status change/recall; mandatory genAI/RAG; claiming board −14% as PoC pass; “validated GxP DSS” while AI-EVIDENCE conflicts.

---

## 4. Target operating workflow (day-to-day + HITL)

1. Entitled user requests pack/options with purpose + as_of.  
2. AuthZ checks IAM (cache never sole authority) → deny stops work.  
3. Read-only ACL pulls facts; Applicable Documents filter instructions.  
4. System emits cited Evidence Items, Conflicts/Gaps/Abstentions, readiness or draft options — **not** decisions.  
5. HITL mandatory on conflicts, clock disagreements, duplicate manual assessment, quarantine/authz denies, multilingual flags.  
6. QP / Safety Physician / Supply Governance Board decide outside the system.  
7. AI-disabled/manual path remains available; narrator/LLM off in assessed mode.

---

## 5. Measurable outcomes

| Outcome | Target | Baseline | PoC result |
|---|---|---|---|
| Prohibited-action block rate | 100% fixtures | N/A control | **met** |
| False “resolved” conflicts | 0 | Unknown ops | **met** on LR-88 path |
| Supply side effects | 0 | Starter unsafe | **met** |
| AuthZ revoke+cache | Deny | Scenario known | **met** |
| Pack cycle-time proxy | Improve vs instrumented baseline | **Unknown** | emit only — **inconclusive** |
| Review hours in TCO | Tracked × staff rates | Hours **Unknown** | template only |
| Continuity drill AC-052 | Pass | Unknown | **deferred** |
| Board −14% lead time | Enterprise | **Unknown** | **not** PoC CTQ |

---

## 6. Domain ownership (DDD)

| Bounded context | Owner | AI / system right |
|---|---|---|
| BC-AUTHZ | Security / CISO | Decision emit only; deny-by-default |
| BC-DOCAPPLY | Document control | Filter; never treat untrusted as instruction |
| BC-BATCH | Quality / QP support | Assist readiness input; **no** certification |
| BC-PV | PV / Global Safety | Intake assist; **no** final safety calls |
| BC-SUPPLY | Supply + Governance Board | Draft options; **no** execution |
| BC-MEASURE | Evaluation / Quality Systems | Gates; do not mutate packs to pass |

---

## 7. Feature & AC summary

| FR | Specified | Verified (Assurance) |
|---|---|---|
| FR-001 AuthZ | Yes | AC-001–003 **pass** |
| FR-002 Documents | Yes | AC-010–012 **pass** |
| FR-003 Batch | Yes | AC-020–023 **pass** |
| FR-004 PV | Yes (fuzzy blocked) | AC-030–033 **pass**; fuzzy untested by design |
| FR-005 Supply | Yes | AC-040–043 **pass** |
| FR-006 Continuity | Yes | AC-050–051 **pass**; AC-052 **deferred** |
| FR-007 Evaluate/Measure | Yes | AC-060–063 **pass** |

---

## 8. Target architecture (provisional C4)

- **Context:** Assist Quality/PV/Supply users; external humans retain certification/reportability/allocation.  
- **Containers:** Single Workflow Runtime; AuthZ; read ACL adapters; local Evidence/Audit store; Evaluate gates; Mode controller; LLM port **no-op**. **No** write-execution plane.  
- **Meets requirements by:** fail-closed AuthZ, schema validation, SideEffectGuard, deterministic offline default.  
- **Status:** provisional — production IAM/DocMgmt/TEVV/HTTP hardening still required (`11_build/poc_vs_production.md`).

*Major architecture change ⇒ reopen Prompts 06–08 (`structural_reopen` gate).*

---

## 9. Key decisions and trade-offs (ADRs)

| Decision | Sacrificed / accepted |
|---|---|
| ADR-001 Deterministic offline default | No always-on model path |
| ADR-002 LLM off by default | Token/speed “magic”; enable gated on Measure |
| ADR-003 No write adapters | End-to-end execution automation |
| ADR-004 IAM over cache | Convenience of stale gateway allow |
| ADR-007 Fuzzy fail-closed | Some duplicate FN → more HITL Waiting |
| ADR-009 Dual-cite clocks | Single “chosen” clock convenience |

---

## 10. Technical contract highlights

- Endpoints: `/v1/authz/check`, batch/pv/supply workflows, `/v1/evaluate/run`, `/v1/health`.  
- Schemas: `evaluation/contracts/*`, `additionalProperties: false`.  
- Readiness enum ≠ disposition; `execution_status=not_executed`; supply `no_side_effects=true`.  
- Errors: envelope without stack traces; 403 authz; 422 prohibited; 409 side-effect/idempotency.  
- NFRs: LLM calls 0 assessed; side effects 0; authz deny 100% on fixture; audit snapshots local.

---

## 11. Safety, security, privacy, governance

- Purpose-bound AuthZ at execution time; revoke beats cache.  
- Untrusted/draft/superseded docs not instructional.  
- Prohibited regulated actions fail closed (tested).  
- Privacy: challenge synthetic data; production must add minimisation/retention/cross-border controls (gap).  
- Governance: HITL on critical conflicts; decision rights unchanged; no validated-DSS claim.

---

## 12. Data and integration strategy

- **Sources:** package CSVs / knowledge catalog via read-only ACL (anti-corruption).  
- **Flows:** request → AuthZ → ACL → reconcile/cite → validate → audit/metrics.  
- **Prohibited writes:** no MES/WMS/Safety write-back; challenge `data/`/`knowledge/` immutable.  
- **Production:** real SoT APIs + signed tools — new ADR if write plane ever required.

---

## 13. Evidence acquisition & data-access plan

| Priority | Obtain | From | Unblocks |
|---|---|---|---|
| P0 | Median/p90 pack cycle-time | Manufacturing / Quality ops | Framing → decision-ready; ROI honesty |
| P0 | Knowledge SoT usage rules at as-of | Document control | Retrieval/policy confidence |
| P0 | Entitlement SoT policy (IAM vs cache) beyond CSV | IAM / CISO | Multi-role production AuthZ |
| P1 | Human review hours samples | Quality / PV / Supply | Honest TCO |
| P1 | Clock field dictionary | Data stewardship | ADR-009 strengthen |
| P1 | Continuity drill execution | Ops | AC-052 |
| P2 | Fuzzy golden set ≥50 + threshold | PV / Evaluation | AMB-PV-01 |
| P2 | LF-normalized package hash audit | Facilitator / Build | A-001 residual |

---

## 14. Lean summary

**Removed / prevented (PoC):** silent unit convert; stale-auth allow; untrusted instruction use; quarantine-as-available; fake reservation; premature LLM token path; guessed fuzzy merges.  
**Still open:** brownfield hunt Waiting (ops Unknown); HITL queue depth; review-hour cost waste; continuity drill; full TEVV.  
**Control:** hard gates + named owners (`12_assurance/control_plan.md`); Measure-first before AI scale.

---

## 15. Human adoption & operating model

- Reviewers work from **cited packs** and exception queues, not spreadsheet reconstruction.  
- SMEs spend time on Conflicts/Abstentions, not rote lexical “ready.”  
- Supply planners receive **draft options + constraints** for Governance Board — never silent reservations.  
- Training: readiness ≠ release; AI off means rules still run.  
- Adoption metric: review hours logged (template exists; ops sampling needed).

---

## 16. Phased roadmap

| Phase | Milestone | Gate |
|---|---|---|
| **Now** | Demo PoC + disclose residuals | Assurance conditional-go |
| **M1 Measure** | Acquire P0 baselines; continuity drill; HITL queue metrics | Exit hypothesis or explicit assume |
| **M2 Harden** | Real IAM/DocMgmt ACL; role matrix; TEVV expansion | Security/GxP review |
| **M3 Scale?** | Optional LLM/narrator only if ADR-002 triggers met | Sponsor + Measure pass |
| **Production** | Only after no-go blockers cleared + sponsor accept | Explicit production go |

Front-load discovery/instrumentation; do not fund agent/RAG scale in M1.

---

## 17. Delivery assumptions (must remain true)

- Challenge evidence remains read-only; no silent normalization of regulated facts.  
- AI authority stays none on certification/reportability; draft-only on allocation.  
- Assessed path stays deterministic / LLM-off unless ADR-002 accepted.  
- Write/execution plane stays absent unless ADR-003 superseded with reopen 06–08.  
- Framing stays `hypothesis` until P0 baselines acquired or labeled assumed.

---

## 18. Residual risks (accepted / deferred)

See `12_assurance/residual_risk_register.md`. Material: Unknown cycle-time/review hours (RR-01); AC-052 (RR-02); AI-EVIDENCE triple-state (RR-05); incomplete TEVV (RR-09); fuzzy FN (RR-04 accepted fail-closed); CRLF verify (RR-06).

**`inconclusive (data scarcity)` must not be treated as pass.**

---

## 19. Sponsor decisions required

| # | Decision | Options | Team3 recommendation |
|---|---|---|---|
| S1 | Demo the PoC under hypothesis framing? | Yes / No | **Yes** (conditional-go) |
| S2 | Grant P0 data access (cycle-time, SoT policies)? | Grant / Defer | **Grant** — unblocks decision-ready |
| S3 | Fund SME time for review-hour sampling + continuity drill? | Fund / Defer | **Fund** |
| S4 | Production / validated DSS path now? | Go / No-go | **No-go** |
| S5 | Enable LLM in assessed path? | Enable / Keep off | **Keep off** until Measure |
| S6 | Authorize write/execution plane? | Authorize / Deny | **Deny** (keep ADR-003) |
| S7 | Accept residual risks RR-01/05 for messaging beyond demo? | Accept / Reject | **Reject** overclaim; accept only with written residual |

---

## 20. Demonstrated in PoC vs required for production

| | **Demonstrated (PoC)** | **Required for production** |
|---|---|---|
| Runtime | Deterministic CLI workflows + tests (25 pass) | Hardened service, IAM/OIDC, observability |
| Controls | Fixture hard gates | Full TEVV, ops SLOs, incident/continuity evidence |
| Data | Package ACL reads | SoT APIs, jurisdiction, signature/hash |
| Claims | Assist-only under hypothesis | Decision-ready framing + cleared validation inventory |

---

## 21. DDD stage 16 handover

Owners and blockers: `12_assurance/production_readiness.md`.  
**Handover stance:** pilot demo package with residuals disclosed; **production authority not transferred**.

---

## Appendix A — Framework & spec artifact index

| Stage | Artefacts | Specs / mirrors |
|---|---|---|
| 01 Discovery | `artefacts/prompts/01_discovery/` | — |
| 02 SCQA | `artefacts/prompts/02_scqa/` | — |
| 03 PRD | `artefacts/prompts/03_prd/` | `specs/product/` |
| 04 DDD | `artefacts/prompts/04_ddd/` | — |
| 05 Features | `artefacts/prompts/05_features/` | `specs/features/` |
| 06 C4 | `artefacts/prompts/06_c4/` | `specs/architecture/` |
| 07 ADRs | `artefacts/prompts/07_adrs/` | `specs/architecture/` |
| 08 Technical | `artefacts/prompts/08_technical/` | `specs/api|data|testing/` |
| 09 Lean | `artefacts/prompts/09_lean_dmaic/` | — |
| 10 Tasks | `artefacts/prompts/10_tasks/` | `tasks/`, `specs/testing/ac_test_plan.md` |
| 11 Build | `artefacts/prompts/11_build/` + `submission/src|tests` | — |
| 12 Assurance | `artefacts/prompts/12_assurance/` | — |
| 13 Proposal | `artefacts/prompts/13_proposal/` | — |
| Phase 0–1 | `artefacts/phases/00_preflight/`, `01_qualify/` | — |

**Run (demo):** `PYTHONPATH=submission python -m pytest submission/tests -q` · `PYTHONPATH=submission python -m src.app_api /v1/health`
