# Product and Service Blueprint

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Product / value lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Domain & evidence lead; GxP lead |
| Status | Draft — provisional pending Measure baselines |
| Related requirements / ADRs | Artefacts 01–03; Prompts 02–03; `ai_use_boundaries.csv`; mandatory workflows |

## Purpose

Define the product intent for AEGIS-PHARMA v1: who it serves, intended vs prohibited uses, service journey with HITL, and success measures — without APIs, schemas, or architecture lock-in.

**Narrative class carried forward:** `hypothesis` on value percentages; capability recommendation is bounded reconciliation + draft options.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `submission/artefacts/01_BUSINESS_CASE.md` | Phase 1 | SCQA answer + scope | Draft |
| E-002 | `data/ai_use_boundaries.csv` | Boundary register | Allowed/prohibited per workflow | Binding |
| E-003 | `data/decision_rights.csv` | Decision rights | Human accountability | Binding |
| E-004 | `data/continuity_requirements.csv` | Continuity | Manual runbooks required | Binding |
| E-005 | `case/INTEGRATED_CASE.md` §4 | Case | Three mandatory workflows | Synthetic |
| E-006 | `case/STAKEHOLDER_PACK.md` | Stakeholders | Personas/concerns | Synthetic |

## 1. Personas and jobs-to-be-done

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| EU QP / batch reviewer | JTBD: assemble trustworthy evidence pack; see gaps/conflicts before certification | Product | E-003, E-006 |
| Safety case intake scientist / physician | JTBD: intake with verbatim preserved; see duplicates/clocks/listedness context; decide human | Product | E-002, E-003 |
| Supply planner | JTBD: generate ranked draft recovery options under quality holds/constraints | Product | E-002, E-003 |
| Quality / PV / Supply leadership | JTBD: inspect audit trail; operate when AI down | Product | E-004 |
| Non-persona | Model vendor / autonomous agent as decision-maker — excluded | GxP | E-002 |

## 2. Intended and prohibited uses

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Intended — Batch | Reconcile, cite, flag, abstain; readiness states only | GxP | E-002 |
| Intended — PV | Extract, normalize (non-destructive), cluster duplicates, cite clocks/terminology/listedness | PV | E-002 |
| Intended — Supply | Generate draft options; list approvals/holds; `no_side_effects` | Supply | E-002 |
| Prohibited | release/reject/reprocess/recall; final causality/seriousness/reportability/signal; reserve/allocate/ship; clinical eligibility automation | Security/GxP | E-002, E-003 |
| Prohibited UX | Present unresolved conflict as resolved; silent unit conversion | Domain | Package scope |

## 3. Frontstage/backstage workflow

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Frontstage | User selects object (batch/case/event), purpose, as-of time; sees cited evidence, contradictions, gaps, abstentions, required reviews | Product | Contract required fields |
| Backstage | Authority/effective-date checks; entitlement check; unit/terminology provenance; audit log; no write-back to disposition/allocation | Architecture (later) | E-002 |
| Current-state (as-is) | Manual swivel-chair across LIMS/MES/QMS/safety/supply spreadsheets | Domain | SOURCE_SYSTEM_FACT_PACK |
| To-be (v1) | Single reconciliation/options desk with HITL; deterministic core | Product | E-001 |

## 4. Human review touchpoints

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Batch | Any conflict/gap/abstention → QP/authorized reviewer | QP | readiness_state enum |
| PV | Required reviews list; no final fields in system of record from AI | Safety Physician | E-002 |
| Supply | Approvals_required + quality_holds before any human execution outside system | Supply Board | E-002 |
| Override | Accountable human only; reason captured | Same roles | Artefact 03 |

## 5. Failure and recovery journey

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Model/region outage | Continue via AI-disabled manual runbook within continuity limits | Reliability | E-004 |
| Untrusted document / poisoned tool | Deny instruction-following; flag for security/quality | Security | INJ-065/066 |
| Stale authorization | Deny by default | Security | users_entitlements |
| Checkpoint corruption | No duplicate side effects — side effects disabled in assessed mode | Build | INJ-080 pattern |

## 6. Accessibility and multilingual experience

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Accessibility | Must not rely on colour-only warnings; keyboard operable (INJ-073) | Product | Later usability tests |
| Multilingual PV | Arabic/Hindi narratives lower extraction quality (INJ-072) — show uncertainty; require human review | PV/Eval | Subgroup gates |
| Language inequity control | Release blocked if critical subgroup evidence missing | Eval | EVALUATION_PLAN |

## 7. Success measures

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Outcome | Contribution to −14% release lead time without Quality-authority change | Product | board_requests BR-01 |
| Safety | 0 prohibited autonomous decisions in tests | Security | contract negatives PASS |
| Quality of assist | Conflicts/gaps cited with provenance; abstain when unresolved | Domain | PUB fixtures |
| Cost | Fully loaded cost includes human review hours | FinOps | cost_model + staff_rates |
| Continuity | Manual path demonstrated | Reliability | E-004 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Assumption | Deterministic-first UX acceptable to QP/PV users | Adoption risk | Product | Pilot | Open |
| R-002 | Gap | Detailed service times Unknown | Blueprint timings TBD | Eval | Measure | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Intended/prohibited uses explicit | §2 | Prohibited-action tests | E-002 | Draft |
| HITL touchpoints named | §4 | Defence demo | Artefact 03 | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| GxP lead | Reviewer | Prohibited uses match boundaries | Confirmed | 2026-08-07 |
