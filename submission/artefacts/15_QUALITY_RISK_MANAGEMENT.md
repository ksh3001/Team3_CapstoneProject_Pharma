# Quality Risk Management

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | GxP & quality lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Security lead; Product lead |
| Status | Draft — Stage 3 |
| Related requirements / ADRs | ICH Q9(R1) as method anchor; artefacts 06, 09–14; hard gates |

## Purpose

Identify quality/safety risks from AEGIS misuse or failure, prioritize controls, and record residual risk accepted for the Stage 3 architecture — without claiming production GxP certification.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `sources/LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md` | Local guide | QRM connects hazard→control→residual | Training summary |
| E-002 | Scoring hard gates | `requirements/SCORING_MODEL.md` | Unconditional fail conditions | Binding for pass |
| E-003 | `submission/artefacts/06_DATA_GOVERNANCE_INTEGRITY.md` | Stage 2 | Integrity inject clusters | Draft |
| E-004 | `submission/artefacts/11_ADR_REGISTER.md` | Stage 3 | Controls via ADRs | Draft |
| E-005 | Contract test results | Stage 3 | Negatives PASS | evidence/contract_tests_stage3.md |

## 1. Risk assessment (selected)

| ID | Hazard | Severity | Detectability | Prob. (w/o control) | Risk | Primary controls | Residual |
|---|---|---|---|---|---|---|---|
| QRM-01 | AI/system issues batch disposition | High | Low if silent | Med | High | No disposition fields; schema gate; ADR-004 | Low if tests maintained |
| QRM-02 | Final PV decision automated | High | Low if silent | Med | High | PV schema; ADR-009; human review | Low |
| QRM-03 | Stock reserved/allocated by tool | High | Med | Med | High | no_side_effects; SideEffectGuard | Low |
| QRM-04 | Silent unit conversion | High | Low | Med | High | ADR-008; abstain | Med until AC-003 automated |
| QRM-05 | Untrusted SOP injection followed | High | Low | Med | High | ADR-006; Stage 4 tests | Med until PUB-03 proven in POC |
| QRM-06 | Stale entitlement used | High | Med | Med | High | ADR-005; AC-008 | Med until coded |
| QRM-07 | Automation bias (incomplete summary accepted) | High | Low | Med | High | Show contradictions/gaps; training; INJ-071 tests | Med |
| QRM-08 | Fabricated uncited facts | High | Med | Med | High | EvidenceItem required; graders | Med until Stage 6 |
| QRM-09 | AI outage blocks critical review | Med | High | Med | Med | ADR-012; continuity | Low–Med |
| QRM-10 | Understated human-review cost → unsafe go-live | Med | Med | High | Med | FinOps include staff_rates; Stage 6 | Open |

## 2. Risk control strategy

| Principle | Application |
|---|---|
| Inherent safety | Structural impossibility of prohibited fields/writes |
| Detection | Schema validation; authz deny; conflict displays |
| Procedural | HITL for regulated decisions; AI-disabled runbooks |
| Monitoring | Audit logs; failed-gate blocks release |

## 3. Residual risk acceptance (Stage 3)

| Residual | Accept? | Condition |
|---|---|---|
| Schema samples PASS but full inject suite not yet coded | Conditional yes for Stage 3 only | Stage 5 must implement AC-003/008–011 |
| Threat tests for injection/poisoning not yet executed | **Not accepted for defence** | Stage 4–5 required |
| KG deferral | Accepted for v1 | Revisit triggers in artefact 08 |

## 4. Review triggers

| Trigger | Action |
|---|---|
| New tool/model/prompt | Re-enter QRM + change control |
| Hard-gate near miss | CAPA + stop release |
| Measure shows rules close BR-01 gap | Pivot GenAI scope (artefact 01) |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Full FMEA scoring numeric calibration TBD | Prioritization coarse | GxP | Stage 6 | Open |
| R-002 | Risk | Residual Med items if Stage 4 skipped | Defence fail | Security/GxP | Stage 4 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Top hazards controlled structurally | QRM-01–03 | Contract negatives PASS | E-005 | PASS |
| Integrity hazards linked to ADRs | QRM-04–06 | Stage 5 tests | E-004 | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Security lead | Reviewer | Injection residual must not be closed at Stage 3 | Explicit in §3 | 2026-08-07 |
| Product lead | Reviewer | Cost risk QRM-10 retained | Stage 6 FinOps | 2026-08-07 |
