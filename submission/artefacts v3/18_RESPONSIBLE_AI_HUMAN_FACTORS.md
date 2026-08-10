# Responsible AI and Human Factors

> Phase 4. Humans remain accountable; UX must fight automation bias, language inequity, and accessibility failure.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Product–value + GxP (HF) |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Security; Evaluation; Architecture |
| Status | Draft |
| Related requirements / ADRs | INJ-071…074; artefact 04; DEC-012; QRM H-08 |

## Purpose

Specify how the assist presents uncertainty and conflicts so reviewers cannot treat it as a silent decision engine — and how language/accessibility gaps are handled without fabricating completeness.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | INJ-071 / candidate_outputs; reviewer_feedback | Automation bias in batch review |
| E-002 | INJ-072 / model_performance; icsr_cases | Language inequity |
| E-003 | INJ-073 / usability_findings | Accessibility failure |
| E-004 | INJ-074 / stakeholders; decision_rights | Role conflict |
| E-005 | artefact 04 blueprint | Human review touchpoints |
| E-006 | Air Canada chatbot precedent (skill) | Operator liable for assistant claims |

## 1. Human accountability

| Decision | Accountable human | AI role |
|---|---|---|
| Batch disposition | EU QP | Package only |
| PV final safety / reportability | Safety Physician | Intake support only |
| Supply allocate/ship/recall | Supply Governance Board | Draft options only |
| Trust exception | Security + steward | Deny/abstain |

**UI copy rule:** Never label readiness_state as “approved” or “released”.

## 2. Automation bias and contestability

| Control | Design |
|---|---|
| Conflict-first layout | Contradictions/gaps/abstentions above any summary |
| No single green banner | ready_for_authorized_review ≠ disposition |
| Contestability | Reviewer can mark “disagree with packaging” → audit event |
| Omitted-critical check | If model used, deterministic detectors still own conflict list |
| Role conflict (INJ-074) | decision_rights wins; UI shows owner, not requester preference |

## 3. Uncertainty and abstention UX

| State | Presentation |
|---|---|
| insufficient_evidence | Explicit missing items list |
| conflicted_evidence | Paired citations; no auto-pick |
| abstentions | Reason codes (unit/time/authority/trust) |
| AuthZ deny | Plain language + refresh path |
| Model confidence low | Route to HITL; never side effect |

## 4. Language/subgroup performance

| Risk (INJ-072) | Control |
|---|---|
| Non-English ICSR under-extracted | Preserve verbatim; flag language; require human review |
| Model performance skew | Assessed path prefers deterministic extractors; model optional |
| Eval | Subgroup slice in Phase 6 TEVV (language tags if present) |

## 5. Accessibility

| Risk (INJ-073) | Control |
|---|---|
| Color-only status | Text + icon + state string |
| Keyboard / contrast | Minimal app must meet basic WCAG-minded checks for defence demo |
| Screen reader | Structured headings for evidence/contradictions/gaps |
| Finding from usability_findings | Track as defect if blocks review task |

## 6. Training and competency

| Audience | Required understanding |
|---|---|
| QP / Safety / Supply | Assist is not a decision; prohibited acts listed |
| Operators | AI-disabled path; how to refresh IAM |
| Builders | Never weaken negative tests to ship |

## 7. Monitoring and feedback

| Signal | Action |
|---|---|
| Reviewer override / disagree rate | Product + GxP review |
| Prohibited attempt blocks | Security incident note |
| Language abstention rate | Improve extractors / staffing |
| Accessibility defects | Block demo claims if critical path broken |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-421 | Risk | Bias controls mostly design-time until UI exists | Residual H-08 | Product | Open Phase 5 |
| A-023 | Assumption | Conflict-first presentation materially reduces bias vs summary-first | HF | Product | Open — validate Phase 6 |

## Traceability and acceptance

| Claim | Control | Test / eval | Result |
|---|---|---|---|
| Humans accountable | §1 / DEC-012 | Review | Draft |
| Bias mitigations specified | §2–3 | HF unscripted Phase 6 | Specified |
| Language/a11y gates | §4–5 | TEVV subgroups | Specified |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | Product + GxP | Pending | | |
