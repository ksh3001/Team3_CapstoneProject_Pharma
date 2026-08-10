# Requirements and Traceability

> Phase 2 bridge from qualification + evidence map to later contracts/tests. Not a full SRS.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Architecture + Product–value |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP; Evaluation |
| Status | Draft |
| Related requirements / ADRs | RUB-07; artefacts 01–08; DEC-010/012/020 |

## Purpose

Trace stakeholder needs and inject-driven obligations to functional/non-functional/GxP requirements and to the evidence/tests that will prove them.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | artefacts 01–04 | Qualification boundaries |
| E-002 | `inject_evidence_register.csv` | 84 inject obligations |
| E-003 | `ai_use_boundaries.csv` / `decision_rights.csv` | Prohibited acts |
| E-004 | `evaluation/contracts/*.schema.json` | Fail-closed shapes |
| E-005 | `EVALUATION_PLAN.md` | Suite classes |
| E-006 | artefact 08 | No KG in v1 |

## 1. Stakeholder and business requirements

| ID | Requirement | Source | Acceptance |
|---|---|---|---|
| BR-Q1 | Pursue −14% release lead time without Quality-authority change | BR-01 | Qualification + measurement plan |
| BR-Q2 | Compare and sequence no-AI alternatives | INJ-003 / no_ai_baselines | Artefact 01–02 |
| BR-Q3 | Preserve independent QP/Safety/Supply accountability | decision_rights | Artefact 03 |
| BR-Q4 | Narrow AI to evidence packaging assist | DEC-010 | Artefact 04 |

## 2. Functional requirements

| ID | Requirement | Workflow | Trace to inject cluster |
|---|---|---|---|
| FR-B1 | Produce batch evidence package with contradictions/gaps/abstentions | Batch | D04, D05 subset |
| FR-B2 | Never emit disposition / never execute disposition tools | Batch | INJ-006, contracts |
| FR-B3 | Surface unapproved unit mappings as conflicts | Batch | INJ-024 |
| FR-P1 | Produce PV intake support with duplicate candidates & clock evidence | PV | D06 |
| FR-P2 | Never finalize reportability/seriousness/causality/signal | PV | INJ-006, contracts |
| FR-S1 | Produce draft supply options with constraints & quality holds | Supply | D08 |
| FR-S2 | no_side_effects true; no reservations | Supply | INJ-080, contracts |
| FR-T1 | Deny stale entitlements; reject untrusted instructions; approved tools only | Cross | D10 |
| FR-T2 | Offline deterministic mode + AI-disabled path | Cross | D13 |
| FR-K1 | v1 uses relational evidence mesh, not KG DB | Cross | DEC-020 |

## 3. Non-functional requirements

| ID | Requirement | Target / note |
|---|---|---|
| NFR-1 | Reproducible setup/test/evaluate offline | Scripts later |
| NFR-2 | Every material fact citable with integrity | evidence_item schema |
| NFR-3 | Fail closed on schema/prohibited fields | additionalProperties false |
| NFR-4 | Subgroup/language/accessibility considered in eval | INJ-072/073 |
| NFR-5 | Token/cost + human-review economics measured | INJ-075–077 |
| NFR-6 | Idempotent draft regeneration; no duplicate side effects | INJ-080 |

## 4. GxP, safety, security and privacy requirements

| ID | Requirement | Gate |
|---|---|---|
| GxP-1 | ALCOA+ provenance preserved | Data integrity gate |
| GxP-2 | No autonomous batch disposition | GxP disposition gate |
| SAF-1 | No final PV safety conclusions | PV decision gate |
| SUP-1 | No inventory/allocation execution | Supply execution gate |
| SEC-1 | Injection/poisoning/stale authZ denied | Security gate |
| PRI-1 | Purpose/residency/DSR conflicts surfaced | Privacy gate |

## 5. Traceability matrix (sample — full inject list in CSV)

| Requirement | Inject IDs (representative) | Future test class | Evidence path |
|---|---|---|---|
| FR-B3 | INJ-024 | gxp_evidence_and_prohibited_disposition | lab_results; interface_mappings |
| FR-P1 | INJ-037, INJ-038 | pv_boundary_and_source_fidelity | icsr; duplicates; receipts |
| FR-S2 | INJ-080, INJ-051 | supply_constraint_and_no_side_effect | agent_runs; shipments |
| FR-T1 | INJ-065–067 | security_zero_trust_and_agent_abuse | knowledge_catalog; tools; entitlements |
| FR-T2 | INJ-079, INJ-082 | outage_recovery_exit_and_retirement | downtime; continuity |
| BR-Q2 | INJ-001–003 | business_value_and_no_ai | board; baselines |

Complete 84-row operational trace: `submission/evidence/inject_evidence_register.csv`.

## 6. Open requirements for Phase 3+

| Item | Phase |
|---|---|
| Versioned contract extensions + failing prohibited tests | 3 |
| C4 + ADR register (≥10) | 3 |
| Threat model detail | 4 |
| POC implementation | 5 |
| Full TEVV suites PUB-01…15 | 6 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-001 | Gap | Not every INJ has a dedicated FR row (CSV is system of record) | Accepted |
| R-002 | Assumption | Contract schemas remain the I/O spine | Accepted |

## Traceability and acceptance

| Claim | Result |
|---|---|
| Business → functional → inject CSV | Done |
| Prohibited acts traced | Done |
| KG decision traced to FR-K1 | Done |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Pending | Evaluation lead | — |
