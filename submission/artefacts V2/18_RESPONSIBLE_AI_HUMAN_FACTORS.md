# Responsible AI and Human Factors

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `04_PRODUCT_SERVICE_BLUEPRINT.md`; INJ-071, INJ-072, INJ-073, INJ-074; `ai_use_boundaries.csv` |

## Purpose

Converts observed human-factor failures (19-second acceptance of an unsafe candidate, language F1 gaps, accessibility fails, role conflict) into design and operating controls so AI support does not displace accountable human judgment. Accountable owner: CQO / Human Factors lead (role-played). Completion criteria: each INJ-071–074 has a concrete UX or process control, not only a policy sentence.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-1801 | `data/candidate_outputs.csv` + `data/reviewer_feedback.csv` | Review event, undated | `CO-1` unsafe_candidate ("recommend progression", omitted sterility excursion); reviewer `QR-11` accepted in **19 seconds**, comment "looked complete" | INJ-071 — single but concrete automation-bias event |
| E-1802 | `data/model_performance.csv` | Eval slices, undated | `PV-NER-4` entity_f1: EN 0.91, HI 0.67, AR 0.63; `TRN-OMICS-2` AUROC Group-A 0.86 vs Group-B 0.61 | INJ-072 language/subgroup inequity |
| E-1803 | `data/usability_findings.csv` | Usability audit | keyboard navigation = high/fail; colour-only hold warning = high/fail | INJ-073 |
| E-1804 | `data/stakeholders.csv` + `data/decision_rights.csv` | Stakeholder / RACI evidence | Role conflict inject INJ-074 (incentive and decision-right tension) | Detail in `03_STAKEHOLDER_DECISION_RIGHTS.md` |
| E-1805 | `data/ai_use_boundaries.csv` | Boundary register | Allowed vs prohibited actions per use case | Hard product constraint |
| E-1806 | `04_PRODUCT_SERVICE_BLUEPRINT.md` | Prior artefact | Personas, prohibited "recommend progression" language, AI-disabled continuity | Carried forward |

## 1. Human accountability

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Who remains accountable? | EU QP (batch), safety physician (PV finals), Supply Governance Board (allocation/recall initiation). AI never holds these rights (E-1805, E-1806). | Per RACI | `03_STAKEHOLDER_DECISION_RIGHTS.md` |
| What must the human still do? | Inspect cited evidence before accepting readiness/cluster/option drafts; record override/escalation reasons. | CQO | E-1801, E-1806 |
| Role conflict | Decision rights and incentives can pull reviewers toward speed over completeness (E-1804, E-1801). Design must not reward 19-second accepts. | Capstone team | E-1801, E-1804 |

## 2. Automation bias and contestability

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Observed failure | Unsafe candidate accepted in 19s because it "looked complete" (E-1801). | Capstone team | E-1801 |
| Design countermeasures | (1) Ban disposition/progression verbs in outputs (`contracts.FORBIDDEN_DISPOSITION_TERMS`). (2) Surface contradictions/gaps/open quality events before any "complete" signal (`workflow_batch`). (3) Require explicit evidence-item acknowledgment in future UI (not yet built in `submission/app`). (4) Time-to-accept monitoring as a quality metric, not a productivity KPI. | Capstone team | E-1801; `contracts.py`; `workflow_batch.py` |
| Contestability | Reviewer must be able to reject, escalate, or request more evidence; AI output is a draft packet, not a decision. | CQO | E-1805 |

## 3. Uncertainty and abstention UX

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| When must the system abstain? | Integrity fail, out-of-scope language, unresolved identity/unit/authority, stale auth, unconfirmed hold link, schema violation — already encoded in gateway/gates/workflows. | Capstone team | `model_gateway`, `privacy_gates`, workflows |
| UX principle | Abstention must be a first-class state (visible, explainable reason codes), not an empty screen or a softened "low confidence" that still looks actionable. Colour-only warnings are forbidden (E-1803). | Capstone team | E-1803 |
| Gap | `submission/app` UI not built — abstention UX is specified here and in outputs' structured fields only. | Capstone team | Gap R-1801 |

## 4. Language/subgroup performance

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Language inequity | PV-NER-4 Hindi/Arabic F1 far below English (E-1802); validated-scope routing blocks out-of-scope languages; missing artifact record blocks even English selection today (R-1004). | Capstone team | E-1802; `model_gateway.py` |
| Subgroup inequity | TRN-OMICS-2 Group-B AUROC 0.61 vs 0.86 Group-A (E-1802) — out of Workflow A/B/C POC scope but proves slice metrics are mandatory before any clinical/omics AI use. | Capstone team | E-1802 |
| Decision | No model inference in production path until integrity + slice gates pass; offline deterministic path remains default. | Capstone team | CSA artefact 14 conclusion |

## 5. Accessibility

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Failures | Keyboard navigation fail; hold warning colour-only (E-1803). | Capstone team | E-1803 |
| Decision | Any future `submission/app` must: full keyboard path for review actions; hold/conflict states with text + icon + not colour-alone; contrast sufficient for status chips. | Capstone team | E-1803; Gap R-1801 |
| Safety relevance | Colour-only hold is a patient-safety control failure, not cosmetic UI debt. | CQO | E-1803 |

## 6. Training and competency

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Required competency | Reviewers must be trained that AI packets can omit critical events (E-1801) and that speed-of-accept is not success. | CQO | E-1801 |
| Gap | No competency matrix or training record in challenge evidence for AI-assisted review roles. | Capstone team | Gap R-1802 |

## 7. Monitoring and feedback

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Signals to monitor | Accept/reject/escalate rates; time-to-accept; contradiction override rate; language-slice F1; accessibility audit status; gate deny rates (auth, tokens, purpose). | Capstone team | E-1801–E-1803 |
| Feedback loop | Reviewer comments (as in E-1801) must feed CAPA / model-validation backlog — "looked complete" is a defect signal. | CQO | E-1801 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1801 | Gap | No participant UI yet to enforce evidence-acknowledgment / a11y controls | High for human-factors claims | Capstone team | Before UI demo | Open |
| R-1802 | Gap | No AI-reviewer competency/training records in evidence | Medium | CQO | Operating model artefact 26 | Open |
| R-1803 | Risk | Productivity pressure recreates 19s accepts even with good UX | High | CQO / Site leadership | Ongoing | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| No disposition language in outputs | `FORBIDDEN_DISPOSITION_TERMS` | `test_workflow_batch.py` | E-1801 | PASS |
| Out-of-scope language blocked | `check_validated_scope` | `test_model_gateway.py` | E-1802 | PASS |
| Accessibility remediation | Future app requirements | Not yet tested | E-1803 | Open |
| Automation-bias UX (forced evidence view) | Specified | Not yet implemented | E-1801 | Open |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | CQO (role-played) | — | — | — |
