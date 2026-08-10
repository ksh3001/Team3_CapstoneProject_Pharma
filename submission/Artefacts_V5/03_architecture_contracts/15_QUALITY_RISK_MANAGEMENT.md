# Quality Risk Management

> Team3 Phase 3 artefact (template 15). ICH Q9 **lens** for assessed scope.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Quality / Architecture |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | GxP; Security; Evaluation |
| Status | Phase 3 — provisional (hypothesis) |
| Related | CSA (14); ADR register; Phase 1 risks |

## Purpose

Identify, score (qualitative), and control risks for the assist POC; escalate where residual risk exceeds board tolerance for production.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-QRM-01 | Phase 1 qualify risks | Baseline / framing |
| E-QRM-02 | Hard gates / DoD | Non-negotiable controls |
| E-QRM-03 | architecture_review conditional | Residual architecture risk |

## 1. Risk register (assessed)

| Risk ID | Hazard | Severity | Detectability | Control | Residual |
|---|---|---|---|---|---|---|
| QRM-01 | Unauthorized access via stale cache | High | Med | IAM>cache; AC-001 | Low |
| QRM-02 | Autonomous disposition / status change | Critical | High (if tested) | Schema reject; no write plane | Low (POC) |
| QRM-03 | Final PV / wrong merge | Critical | Med | No finals; no fuzzy | Low (POC) |
| QRM-04 | Inventory reservation / ship | Critical | High | SideEffectGuard | Low (POC) |
| QRM-05 | Poisoned tool/doc influence | High | Med | Quarantine; no manifest load | Low–Med |
| QRM-06 | Unit / conflict silent choice | High | Med | Dual-cite; conflict policy | Med |
| QRM-07 | LLM hallucination on assessed path | High | Low–Med | LLM off; narrator refuse | Low |
| QRM-08 | False ROI / cycle-time claims | Med | Low | Hypothesis framing; Missing baselines | Med (accepted) |
| QRM-09 | Ontology/KG as decision authority | High | Med | D-004/D-016 out of scope | Low |
| QRM-10 | Continuity drill unproven (AC-052) | Med | Low | Deferred Phase 7 | Med |

## 2. Risk acceptance

Production go remains **no-go** until baselines, continuity drill, and security artefacts close residual Med items where required by Evaluation.

## 3. Review cadence

Revisit on ADR reopen triggers; after Phase 4 security; after Phase 7 TEVV.

## Risks, assumptions and unresolved gaps

| ID | Description | Status |
|---|---|---|
| R-QRM-01 | Qualitative scores only | Accepted |
| R-QRM-02 | Hypothesis framing limits benefit claims | Accepted |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Critical hazards controlled by design | §1 QRM-02…04 | Pass |
| Residual risks explicit | §2 | Pass |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Team3 Quality | Owner | 2026-08-07 |
