# Data Governance and Integrity

> Team3 Phase 2 artefact (template 06).

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Domain / Data stewardship |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Security/privacy; GxP; Architecture |
| Status | Phase 2 complete — provisional |
| Related | RUB-04…06; `DATA_DICTIONARY.csv`; `DATASET_PROFILE.csv`; inject register |

## Purpose

Inventory challenge datasets, declare source authority and integrity controls for the assist, and state what must never be written back. Completion: inventory classified; SoT by object; conflict/identity handling; ALCOA+ view; lineage; stewardship.

## Evidence register

| Evidence ID | Source | Fact used | Limitation |
|---|---|---|---|
| E-DG-01 | `data/DATASET_PROFILE.csv` | **139** profiled CSV datasets with sha256 | Package inventory |
| E-DG-02 | `data/DATA_DICTIONARY.csv` | Field semantics examples (e.g. LR-88, contractor_77) | Not full ops dictionary |
| E-DG-03 | `data/knowledge_catalog.csv` | 32 docs; trust/status/effective | Mixed trust |
| E-DG-04 | `inject_evidence_register.csv` | 84 injects mapped to sources | Initial assessment |
| E-DG-05 | `evaluation/contracts/*.schema.json` | Output integrity shapes | Assessed contracts |

## 1. Dataset inventory and classification

| Class | Examples | Use in AEGIS |
|---|---|---|
| Identity / AuthZ | `users_entitlements`, `access_cache` | BC-AUTHZ SoT = IAM file |
| Quality / Lab | `lab_results`, `oos_investigations`, `interface_mappings` | BC-BATCH evidence |
| Manufacturing | genealogy/EBR-related CSVs | BC-BATCH (read) |
| Safety / PV | `icsr_cases`, `safety_receipts`, `adverse_events`, `duplicate_candidates` | BC-PV |
| Supply | `inventory`, `shipments` | BC-SUPPLY |
| Knowledge / policy | `knowledge_catalog` + `knowledge/*.md` | BC-DOCAPPLY |
| Governance / cost | `board_requests`, `decision_rights`, `cost_model`, `staff_rates` | Qualify/Control |
| Validation | `validation_inventory`, `system_inventory` | GxP claims boundary |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| How many datasets? | 139 profiled CSVs + 32 knowledge docs | Domain | E-DG-01, E-DG-03 |
| Challenge write policy | **0 writes** to `data/`, `knowledge/` | Build | D-001; NFR-12 |

## 2. Source authority by object/context/time

| Object | Authoritative source (POC) | Override forbidden |
|---|---|---|
| Entitlement | `users_entitlements.iam_state` | `access_cache` alone |
| Lab result value/unit | LIMS row as packaged | Silent convert via unapproved mapping |
| Document instruction | approved+approved trust at as_of | untrusted/draft/superseded |
| Inventory availability | `quality_status=released` only for options | Quarantine/unknown as available |
| PV clocks | Dual-cite receipts + awareness | Picking one clock silently |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| as_of required? | Yes for workflows | Architecture | API contracts |

## 3. Identity and master-data conflicts

| Conflict class | Package signal | Handling |
|---|---|---|
| Unit ≠ spec unit | LR-88 mg/L vs ug/mL | Conflict; no silent convert |
| Unapproved mapping | `interface_mappings.approved=no` | Conflict / block readiness |
| Product alias | NCB-204 vs NCB204 / brand_alias | Exact/strong_key only; no fuzzy auto |
| Revoked + cached user | contractor_77 | Deny |
| Validation triple-state | AI-EVIDENCE inventories disagree | No validated-DSS claim |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Silent merge allowed? | **Never** | GxP / Domain | CONFLICT_RESOLUTION_POLICY |

## 4. Quality and ALCOA+ assessment

| Attribute | POC posture |
|---|---|
| Attributable | user/purpose/checked_at on AuthZ; audit snapshots |
| Legible | verbatim facts in Evidence Items; dual-cite conflicts |
| Contemporaneous | as_of + retrieved_at on evidence |
| Original | `source_preserved=true`; sha256 of facts |
| Accurate | Conflicts flagged rather than “corrected” |
| + Complete / Consistent / Enduring / Available | Gaps/abstentions explicit; challenge data immutable; continuity path |

## 5. Lineage and transformation controls

- Lineage string on inject register: `challenge:<sources>`.  
- Transformations allowed: classify, cite, flag, abstain — **not** invent values or convert units.  
- Output schemas deny unknown properties.

## 6. Retention, residency and legal hold

| Topic | POC | Production gap |
|---|---|---|
| Retention | Working audits under `submission/working/` only | Org retention schedule |
| Residency | Local offline | Cross-border controls |
| Legal hold | Out of POC scope | Document in Phase 4 privacy artefact |

## 7. Stewardship and issue remediation

| Issue type | Steward | Remediation |
|---|---|---|
| Unit/mapping | QC / integration | Approve mapping or keep conflict |
| Entitlement SoT | IAM / CISO | IAM > cache policy |
| Knowledge trust | Document control | Quarantine / supersede |
| Inject assessment | Team3 Domain | Update register status from UNASSESSED |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-DG-01 | Gap | Full LF hash audit Partial (CRLF) | Open A-001 |
| R-DG-02 | Gap | Review-hour / cycle-time baselines Missing | Open P0 |
| R-DG-03 | Assumption | 139 CSVs sufficient for POC workflows | Accepted POC |

## Traceability and acceptance

| Claim | Control | Evidence | Result |
|---|---|---|---|
| No challenge writes | ACL forbid_write | tests + NFR-12 | Pass (POC) |
| Authority filters | Doc/AuthZ rules | AC-001, AC-010 | Pass |

## Review record

| Reviewer | Role | Finding | Date |
|---|---|---|---|
| Team3 Domain | Owner | Accept provisional inventory | 2026-08-07 |
