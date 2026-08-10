# Privacy and Ethics

> Team3 Phase 4 artefact (template 17). Privacy-by-design for assessed POC — **not** a DPIA approval or legal opinion. Synthetic training data (A-003).

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Privacy / Security |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | DPO lens; GxP; Legal awareness |
| Status | Phase 4 — provisional |
| Related | INJ-059…064; K-020; D09; Phase 2 data governance |

## Purpose

Map purposes, data classes, consent/secondary-use constraints, minimisation, residency, and ethics trade-offs for AEGIS assist. Completion: privacy controls stated with inject traceability and residual gaps (legal hold, production cross-border).

## Evidence register

| Evidence ID | Source | Fact used | Limitation |
|---|---|---|---|
| E-PR-01 | `case/INTEGRATED_CASE.md` D09 | INJ-059…064 | Narrative |
| E-PR-02 | `knowledge/PRIVACY_AND_PSEUDONYMISATION.md` (K-020) | Minimise; linkage assess | Approved knowledge; still verify applicability |
| E-PR-03 | `data/consents.csv`; `deletion_requests.csv`; `data_residency.csv` | Fixture signals | Not production systems |
| E-PR-04 | `artefacts/phases/02_domain_evidence/06_DATA_GOVERNANCE_INTEGRITY.md` | ALCOA+ / purpose tags | Legal hold deferred here |
| E-PR-05 | LICENSE / START_HERE | Synthetic training only | A-003 |

## 1. Purpose and data map

| Data class | Purpose in POC | Workflow | Out of purpose |
|---|---|---|---|
| Batch / QC extracts | batch_evidence | FR-003 | Commercial targeting |
| ICSR / PV case extracts | pv_intake | FR-004 | Affiliate-wide identifiable dump (INJ-068) |
| Inventory / shortage | supply_options | FR-005 | Reservation/allocation execution |
| Entitlements | AuthZ | FR-001 | Granting access via AI |
| Knowledge docs | Applicability | FR-002 | Untrusted as policy |
| Genomic / support free text | **Not ingested for assessed path** | — | INJ-059/062 risk — abstain |

## 2. Permission/consent assumptions

| Item | Response | Owner | Status |
|---|---|---|---|
| Training package consent | Synthetic; no real data principals | Evaluation | A-003 |
| EU trial → global model training (INJ-060) | **Out of assessed POC**; secondary use blocked | Privacy / Product | Deny until lawful basis |
| Research → commercial (INJ-063) | Blocked — not a purpose | Privacy | Deny |
| Production consent SoT | Unknown — Q-class open | Legal | Abstain |

## 3. Minimisation and pseudonymisation

| Control | POC behaviour |
|---|---|
| Field minimisation | Workflows pull purpose-scoped CSV rows via ACL; no bulk case export |
| Direct identifiers | Prefer synthetic case/batch ids; avoid free-text dumps in logs |
| Pseudonymisation (K-020) | Policy cited; assessed path does not join genomic rare-disease sets |
| Linkage risk (INJ-059) | Do not assemble highly identifying combinations in packs |

## 4. Secondary use and re-identification

| Hazard | Control | Residual |
|---|---|---|
| Secondary model training on EU trial data | LLM off; no training export job | Low in POC |
| Re-ID via rare combinations | Exclude genomic path from assessed workflows | Med if later enabled |
| Patient-support free text over-collection (INJ-062) | Not a source for packs | Low |

## 5. Residency and cross-border controls

| Item | Response |
|---|---|
| POC residency | Local disk under `submission/`; challenge tree read-only |
| INJ-064 unapproved backup region | **Not operated** in POC; production must enforce residency allow-list |
| Cross-border instructional docs | local_approved not globally instructional (AMB-DOC-01) |
| Claim | No “GDPR compliant” assertion from this artefact |

## 6. Rights, retention and legal hold

| Topic | Decision |
|---|---|
| Deletion vs GxP preserve (INJ-061) | **Escalate** — do not auto-erase regulated records; DPO + Quality/Legal |
| Retention | POC working/audit retained for evaluation; no production retention schedule claimed |
| Legal hold | Out of automated POC; human process required (Phase 2 deferred → here) |
| DPDP / GDPR rights | Awareness only — identity verify + evidence trail before any erasure workflow in production |

## 7. Ethical trade-offs and oversight

| Trade-off | Stance |
|---|---|
| Speed (board −14%) vs privacy min | Purpose-bound assist; no Quality-authority change |
| Privacy delete vs trial integrity | Preserve + escalate (INJ-061) |
| Uniform global automation vs local accountability | Local QP/Safety retain decisions (INJ-074) |
| Oversight | DPO constraint on retrieval/export; Security on quarantine |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-PR-01 | Gap | Full privacy leakage suite not run | Med | Evaluation | Open Phase 6 |
| R-PR-02 | Gap | Production DPIA / cross-border transfer mechanism | High | Privacy / Legal | Open — prod no-go |
| R-PR-03 | Assumption | Synthetic data only in assessed path | Critical if violated | Whole team | A-003 Open |

## Traceability and acceptance

| Claim | Control | Test / evidence | Result |
|---|---|---|---|
| Purpose limitation | AuthZ purposes | AC-001–003; matrix | Pass |
| No secondary training use in POC | LLM off; no export | AC-051; this file | Pass |
| Deletion conflict handled by escalation | Policy §6 | Documented | Pass (process) |
| Production privacy readiness | — | R-PR-02 | Fail / no-go |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Privacy | Owner | Legal hold & DPIA residual | Accepted for Phase 4; blocks production | 2026-08-07 |
