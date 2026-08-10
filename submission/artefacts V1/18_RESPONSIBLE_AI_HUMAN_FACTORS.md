# Responsible AI and Human Factors

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Product / value lead + Security/privacy lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP lead; Domain lead |
| Status | Draft — Stage 4 |
| Related requirements / ADRs | INJ-071–074; artefact 03–04; ADR-001, 011–012; NFR-006/007 |

## Purpose

Define human oversight, automation-bias controls, accessibility, multilingual equity, and role conflict handling so AEGIS remains assistive under conflicting incentives.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `data/candidate_outputs.csv`; `reviewer_feedback.csv` | HF evidence | Automation bias — omitted critical deviation accepted (INJ-071) | Synthetic |
| E-002 | `data/model_performance.csv`; `icsr_cases.csv` | Performance | Arabic/Hindi lower quality vs EN/DE (INJ-072) | Synthetic |
| E-003 | `data/usability_findings.csv` | Usability | Colour-only warnings; keyboard gaps (INJ-073) | Synthetic |
| E-004 | `data/stakeholders.csv`; `decision_rights.csv` | Rights | Global vs local accountability (INJ-074) | Binding |
| E-005 | `submission/artefacts/03_STAKEHOLDER_DECISION_RIGHTS.md` | Stage 1 | HITL matrix | Draft |
| E-006 | `submission/artefacts/04_PRODUCT_SERVICE_BLUEPRINT.md` | Stage 1 | Review touchpoints | Draft |

## 1. Human oversight model

| Workflow | AI/system may | Human must |
|---|---|---|
| Batch | Cite/flag/abstain; readiness_state | QP/authorized reviewer decides certification |
| PV | Extract/cluster/cite; list required_reviews | Safety physician final decisions |
| Supply | Draft options + approvals_required | Supply Governance executes outside system |
| Override | Never self-approve | Accountable role + reason in audit |

## 2. Automation bias controls

| Control | Design |
|---|---|
| Forced conflict visibility | contradictions/gaps cannot be hidden behind a green summary |
| No single “approve all” | Pack shows itemized evidence |
| Critical omission tests | INJ-071-style fixtures must fail if deviation dropped |
| Training | Train on abstention and challenge behaviour (artefact 03 §6) |

## 3. Multilingual and subgroup equity

| Issue | Control |
|---|---|
| Language inequity (INJ-072) | Show uncertainty; require human review; Stage 6 subgroup gate |
| Release gate | Missing subgroup evidence blocks release (EVALUATION_PLAN) |
| Deterministic v1 | Reduces silent NLP disparity; when model on, measure per language |

## 4. Accessibility

| Finding | Requirement |
|---|---|
| Colour-only warnings (INJ-073) | Text + icon/pattern; not colour alone |
| Keyboard operation | All critical paths keyboard operable |
| Contestability | Clear path to escalate/override |

## 5. Role conflict and adoption

| Conflict | Resolution principle |
|---|---|
| Global process owner vs local QP/Safety legal duty | Local accountable role wins on regulated decision (INJ-074) |
| Manufacturing speed vs Quality completeness | Quality evidence completeness binding for release readiness |
| Adoption | Measure review burden; do not ship summaries that suppress gaps |

## 6. Emergency stop / AI-disabled

| Control | Link |
|---|---|
| Kill switch / offline mode | ADR-012; continuity_requirements |
| Manual journey | Artefact 04 §5; Stage 7 runbooks |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | UI not yet built — a11y tests pending | Stage 5–6 | Product | POC UI | Open |
| R-002 | Risk | Automation bias persists if UX emphasizes “score” | Hard-gate cultural fail | HF/Quality | Design review | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| HITL explicit | §1 | Defence demo | E-005 | Draft |
| Bias/language/a11y risks logged | §§2–4 | Stage 6 suites | E-001–003 | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| GxP lead | Reviewer | Local accountability preserved | §5 | 2026-08-10 |
