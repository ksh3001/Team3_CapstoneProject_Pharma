# Product and Service Blueprint

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `01_BUSINESS_CASE.md`, `03_STAKEHOLDER_DECISION_RIGHTS.md` §2/§4; INJ-071, INJ-072, INJ-073, INJ-069, INJ-079 |

## Purpose

Defines who uses the three workflows day-to-day, exactly what they are and are not allowed to do, where a human must physically look at evidence before acting, and what happens when the AI is degraded, wrong or unavailable. Accountable owner: capstone team. Completion criteria: every intended use maps to an allowed-action row in `data/ai_use_boundaries.csv`; every prohibited use maps to a failing contract test; the automation-bias failure already evidenced (INJ-071) has a specific design countermeasure, not a general statement.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-301 | `data/candidate_outputs.csv` + `data/reviewer_feedback.csv` | Recorded review event, undated | Output `CO-1` (workflow: batch_review) stated "All critical evidence complete; recommend progression" while omitting an "open sterility excursion"; status = `unsafe_candidate`. Reviewer `QR-11` action = "accepted" in 19 seconds, comment "looked complete" | This is the concrete instance of INJ-071 (automation bias) — a single row, but a real recorded failure, not a hypothetical |
| E-302 | `data/usability_findings.csv` | Usability audit, undated | "keyboard navigation" = high severity, fail; "colour-only hold warning" = high severity, fail | Matches INJ-073; a "hold" status conveyed by colour only is safety-relevant, not cosmetic |
| E-303 | `data/model_performance.csv` | Model evaluation slices, undated | `PV-NER-4` entity_f1: English 0.91, Hindi 0.67, Arabic 0.63 | Matches INJ-072; a 24–28 point F1 gap on the exact model proposed for PV narrative extraction |
| E-304 | `data/downtime_events.csv` | Incident log, undated/ongoing | `DT-1`: MES/QMS/historian down for ransomware containment, 2026-07-22T16:00Z–2026-07-23T08:00Z (16 hours). `DT-2`: AI primary region outage starting 2026-08-01T01:00Z, end = "open" (unresolved at time of evidence capture) | Matches INJ-069 and INJ-079; DT-2 being still "open" means an AI-disabled continuity path is not hypothetical, it is presently required |
| E-305 | `knowledge/BATCH_RELEASE_EVIDENCE_POLICY.md` (K-006, approved 2026-06-01) | Synthetic NovaCura Global Policy | "Never treat AI output as batch disposition or certification"; "Do not infer a regulated decision, execute a side effect, or hide conflicting evidence" | Approved-status policy document; authority is scenario-internal, not real-world | 
| E-306 | `knowledge/SUPPLY_ALLOCATION_ETHICS.md` (K-029, approved 2026-05-28) | Synthetic NovaCura Global Policy | "Use only quality-released stock in executable planning"; "Require accountable governance for allocation decisions" | Same scenario-internal authority caveat as E-305 |
| E-307 | `knowledge/AI_GXP_BOUNDARY.md` (K-003, approved 2026-05-01) | Synthetic NovaCura Global Policy | "AI may support evidence review but cannot replace accountable GxP decisions"; consumer must "abstain or escalate when applicability cannot be established" | Governs all three workflows generically; K-006/K-029 are workflow-specific applications of it |
| E-308 | `01_BUSINESS_CASE.md` E-004 / `03_STAKEHOLDER_DECISION_RIGHTS.md` §2 | Prior artefacts, this team | Allowed/prohibited action lists and RACI matrix for all three workflows | Carried forward, not re-derived |

## 1. Personas and jobs-to-be-done

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Persona — Quality Reviewer (e.g. `QR-11`) | Job to be done: assemble and check a release-evidence packet before EU QP certification. Evidenced failure mode: will accept a plausible-looking AI summary in under 20 seconds without checking the underlying evidence (E-301). Design implication: the interface must make skipping evidence inspection *harder*, not just possible-but-discouraged. | Capstone team | E-301 |
| Persona — EU Qualified Person | Job to be done: certify batch release using complete, traceable evidence; final accountability remains here regardless of AI output (E-305, `03_STAKEHOLDER_DECISION_RIGHTS.md` §2). | Capstone team | E-305, `03_STAKEHOLDER_DECISION_RIGHTS.md` |
| Persona — PV Case Intake Analyst / Safety Physician | Job to be done: process ICSR intake across languages (including Hindi/Arabic narratives, E-303) with duplicate detection, terminology normalization and listedness evidence — but never final causality/seriousness/reportability (`01_BUSINESS_CASE.md` E-004). | Capstone team | E-303, E-004 |
| Persona — Supply Governance Board member / planner | Job to be done: review AI-generated allocation *options* under shortage, using only quality-released stock (E-306) — never execute allocation directly. | Capstone team | E-306 |
| Explicitly not a persona | Any role empowered to accept an AI conclusion as final without inspecting cited evidence — E-301 shows this is a real failure mode to design *against*, not a persona to design *for*. | Capstone team | E-301 |

## 2. Intended and prohibited uses

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Workflow A intended use | Reconcile, cite, flag, abstain on batch-review evidence (E-308). Prohibited: release/reject/reprocess/relabel/recall (E-308, E-305). | Capstone team | E-308, E-305 |
| Workflow B intended use | Extract, normalize, cluster, cite on PV intake (E-308). Prohibited: final causality/seriousness/expectedness/reportability/signal-confirmation (E-308). | Capstone team | E-308 |
| Workflow C intended use | Generate non-executing supply/cold-chain options using only quality-released stock (E-306, E-308). Prohibited: reserve/allocate/ship/change quality status/initiate recall without explicit authorized human approval (E-308, E-306). | Capstone team | E-308, E-306 |
| What happens if applicability cannot be established (e.g., stale policy, ambiguous jurisdiction)? | Per E-307, the system must abstain or escalate — it must not silently proceed using the nearest-matching policy. This applies to all three workflows equally. | Capstone team | E-307 |
| Is "recommend progression" language (as used in E-301) itself a prohibited use? | Yes, on inspection — "recommend progression" reads as a release-adjacent recommendation, closer to a disposition hint than a neutral evidence citation. Output language must be restricted to evidence status (complete/incomplete/contradictory) and never a progression/disposition verb. This is a concrete wording constraint for prompt/schema design, not just a policy statement. | Capstone team | E-301, E-305 |

## 3. Frontstage/backstage workflow

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Frontstage (what the persona sees) | A structured evidence packet view: each cited fact linked to its source record, authority, effective date and any detected conflict — modeled on `evaluation/contracts/evidence_item.schema.json` — not a single free-text summary (directly counters the E-301 failure mode, where a single-sentence summary hid an open sterility excursion). | Capstone team | E-301, `evaluation/contracts/evidence_item.schema.json` |
| Backstage (what the system does before the persona sees anything) | Retrieval with authority/effective-date checks (E-307); contradiction and gap detection against the workflow-specific policy (E-305/E-306); abstention where applicability is unresolved; structured-output validation against the relevant contract schema before display (already passing per `tools/test_contracts.py`). | Capstone team | E-307, `tools/test_contracts.py` |
| Boundary between frontstage and backstage | The backstage must never resolve a conflict on the persona's behalf and only show the resolution — per E-305/E-307, conflicting evidence must be exposed, not hidden, even if the system has a "likely" answer. | Capstone team | E-305, E-307 |

## 4. Human review touchpoints

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What specific design countermeasure follows from E-301 (19-second acceptance of an unsafe candidate)? | (1) The UI must require expanding/viewing each cited evidence item before an "accepted" action is enabled (no default-visible one-line summary that can be accepted without expansion); (2) any output flagged internally as bordering on `unsafe_candidate`-type risk (e.g., an open deviation/excursion exists in the same batch) must force a mandatory secondary field ("evidence reviewed: yes/no per item") rather than a single accept button; (3) review actions under an evidence-based minimum dwell time threshold should be logged for supervisory sampling, not blocked (blocking review time is itself a usability risk) but visible for oversight. | Capstone team | E-301 |
| Who reviews the reviewers? | Not yet assigned — carried forward from `03_STAKEHOLDER_DECISION_RIGHTS.md` R-102 (no assigned reviewer of AI abstention/acceptance patterns). This blueprint's countermeasure (above) only works if someone owns watching for a repeat of the QR-11 pattern. | Capstone team | `03_STAKEHOLDER_DECISION_RIGHTS.md` R-102 |
| Does a human review touchpoint exist for Workflow C options before any action? | Yes, by requirement — E-306 mandates accountable governance for allocation decisions; the blueprint places the Supply Governance Board review strictly between "AI generates options" and any downstream action, with no direct path from AI output to execution. | Capstone team | E-306 |

## 5. Failure and recovery journey

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Scenario: source systems down (ransomware containment) | `DT-1` shows MES, QMS and historian offline for 16 hours during active containment (E-304). During this window, Workflow A cannot retrieve current genealogy/deviation data — it must explicitly report "source unavailable, evidence as of last successful retrieval at [timestamp]," never silently substitute stale data as current. | Capstone team | E-304 |
| Scenario: AI platform itself down | `DT-2` shows the AI primary region outage is still "open" (unresolved) in the supplied evidence (E-304) — this is not a drill, it is the present state described by the case. All three workflows must have a documented manual-fallback path usable *right now* with zero AI availability, consistent with INJ-082 (14-day AI-disabled continuity requirement). | Capstone team | E-304, INJ-082 |
| What must the journey never do during degraded mode? | Silently fail over to a secondary/cached AI region without disclosing the failover (this itself is untested per `01_BUSINESS_CASE.md`'s traceability gaps) or present degraded-mode output with the same confidence framing as normal-mode output. | Capstone team | E-304 |

## 6. Accessibility and multilingual experience

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Known accessibility failures | Keyboard navigation: high severity, fail. Colour-only hold-status warning: high severity, fail (E-302). A colour-only "hold" indicator is a direct safety risk if it appears anywhere in batch-review or supply-planning UI, since a hold status conveyed only by colour can be missed by colour-blind or screen-reader users. | Capstone team | E-302 |
| Known multilingual quality gap | `PV-NER-4` entity extraction F1: English 0.91 vs. Hindi 0.67 vs. Arabic 0.63 (E-303) — a 24–28 point gap. This means PV intake output for Hindi/Arabic narratives must carry a visibly lower-confidence / mandatory-manual-review flag, not be presented with the same trust level as English output. | Capstone team | E-303 |
| Design consequence | Both findings must be resolved (or explicitly mitigated with a compensating control) before Workflow B or any hold/warning-bearing UI in Workflow A/C ships — E-302's severity is "high," not cosmetic, and E-303's gap directly risks under-flagging safety-relevant narratives in exactly the languages most likely spoken by patients in some of NTG's markets (E-303, `case/INTEGRATED_CASE.md` INJ-072). | Capstone team | E-302, E-303 |

## 7. Success measures

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What must NOT be a success measure | Speed of acceptance / time-to-accept for review actions — optimizing this metric would reward exactly the E-301 failure pattern (a 19-second accept of an unsafe candidate). | Capstone team | E-301 |
| What should be measured instead | Rate of evidence-item expansion before accept/reject actions; rate of correctly-flagged contradictions/gaps against known injected defects (using the public fixtures and the team's own adversarial set per `evaluation/EVALUATION_PLAN.md`); subgroup parity of extraction quality across languages (closing, not just documenting, the E-303 gap); zero occurrences of prohibited-action language (E-301's "recommend progression" pattern) in any output sample. | Capstone team | E-301, E-303, `evaluation/EVALUATION_PLAN.md` |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-301 | Risk | Single recorded instance (E-301) of automation bias exists; true rate/frequency across reviewers is unknown from a 1-row sample | Medium — countermeasures in §4 are justified by a real event but not yet validated at scale | Capstone team | Phase 5 (Break and recover), reviewer-behaviour test set | Open |
| R-302 | Gap | No owner yet assigned for supervisory review of reviewer behaviour (carried from `03_STAKEHOLDER_DECISION_RIGHTS.md` R-102) | Medium | Capstone team | Phase 3 (Specify) | Open |
| R-303 | Risk | Accessibility failures (E-302) are both rated "high" and currently unresolved — any interim demo UI inherits this risk until fixed | High for any UI conveying hold/warning status | Capstone team | Before any UI demo involving hold states | Open |
| R-304 | Risk | AI primary-region outage (E-304, `DT-2`) has no recorded end time — treated as still open; manual fallback must be assumed as the current operating mode, not a contingency | High | Capstone team | Immediate — informs Phase 4 build priority | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Output never uses disposition/progression language (§2) | Prompt/schema constraint on output vocabulary | Not yet implemented as an automated check | `evaluation/contracts/batch_response.schema.json` | Pending — needs a new negative fixture for "recommend progression"-style wording |
| Evidence-item expansion required before accept (§4) | Frontend interaction design | Not yet built | `submission/app/` (pending) | Pending |
| Manual fallback usable with zero AI availability (§5) | AI-disabled continuity design | Cross-referenced to `knowledge/AI_DISABLED_CONTINUITY.md` (not duplicated here) | — | Pending |
| Subgroup language parity tracked (§6/§7) | Evaluation suite 10 (`evaluation/EVALUATION_PLAN.md`) | Not yet implemented | `submission/evaluation/` (pending) | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
