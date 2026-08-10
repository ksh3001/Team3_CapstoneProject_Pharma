# Data Governance and Integrity

> Phase 2. EXISTS / USABLE / GOVERNED / MISSING discovery. Contradictions preserved.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Domain–evidence lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP lead; Security–privacy lead |
| Status | Draft |
| Related requirements / ADRs | RUB-05; DEC-010 |

## Purpose

Inventory challenge datasets and knowledge trust, define source authority by context/time, and record identity/DI conflicts without normalizing them away.

## Evidence register

| Evidence ID | Source path / record | Fact used |
|---|---|---|
| E-001 | `data/DATASET_PROFILE.csv` | Profiled datasets + hashes |
| E-002 | `data/DATA_DICTIONARY.csv` | Column semantics |
| E-003 | `data/RELATIONSHIP_MODEL.csv` | Required links + declared exceptions |
| E-004 | `submission/evidence/inject_evidence_register.csv` | 84 inject → evidence paths |
| E-005 | `submission/evidence/knowledge_trust_catalogue.csv` | Trust/instruction eligibility |
| E-006 | `submission/evidence/anchor_conflict_register.md` | Anchor conflicts |
| E-007 | `data/interface_mappings.csv` | Unapproved unit map |
| E-008 | `FILE_HASHES.csv` | Immutable challenge hashes (300 OK) |

## 1. Dataset inventory and classification

| Class | Examples | Governance note |
|---|---|---|
| Operational transactional | batches, lab_results, icsr_cases, shipments, inventory | System-of-record candidates per field; vignette scale |
| Master / identity | portfolio_products, substance_master, medicinal_products, idmp_mappings | High collision risk (INJ-008, INJ-045) |
| Interface / mapping | interface_mappings, api contract samples | Approval flag mandatory (E-007 approved=no) |
| Knowledge controlled | knowledge/*.md via catalog | Trust ≠ presence |
| Security / entitlements | users_entitlements, access_cache, tool_catalog | Freshness required |
| Evaluation fixtures | evaluation/public_fixtures | Inputs only, hashed slices |
| Missing / stub | PV-1020, NCS310-S26031 batch master gap, LG-42 readings | Declared exceptions — MISSING register |

**Four questions**

| Question | Finding |
|---|---|
| EXISTS? | 139+ synthetic datasets + 32 knowledge docs + 84 injects |
| USABLE? | Usable for training reconciliation; many rows are vignettes; profile before treating as analytics truth |
| GOVERNED? | Catalog + hashes + relationship rules; knowledge trust mixed |
| MISSING? | Absolute lead-time baseline (Phase 1 open); declared relationship stubs; eCTD referenced-missing themes |

## 2. Source authority by object/context/time

| Object | Prefer authority | Temporal rule | Reject / demote |
|---|---|---|---|
| Batch lab result | LIMS result + approved interface mapping | Result effective/as-of; not “latest file wins” | Unapproved conversion (E-007) |
| Batch policy | Approved effective SOP (e.g. K-006) | effective date ≤ as-of | K-007 superseded; K-998 untrusted |
| PV clock | Receipt events with source timestamps | Preserve multi-clock evidence | Single “best” clock invented by model |
| Listedness | Jurisdiction-applicable label/CCDS authority | As-of + market | Cross-region collapse |
| Entitlement | IAM current state | checked_at at request | access_cache alone |
| Tool definition | Signed/approved manifest | Version pin | tool_manifest_poisoned |

## 3. Identity and master-data conflicts

| Conflict | Evidence | Disposition |
|---|---|---|
| Potency units mg/L vs ug/mL spec | lab_results LR-88 + interface_mappings | Surface; no convert |
| ICSR duplicate cluster | duplicate_candidates | Candidates only |
| IDMP / product codes | INJ-045 evidence paths | Map with uncertainty |
| Compound local code collision | INJ-008 | Keep both until governed resolution |
| Recall lot not in batch extract | RELATIONSHIP declared_exception | Gap, not delete |
| Logger LG-42 no readings | RELATIONSHIP notes | Gap |

## 4. Quality and ALCOA

| Attribute | Case pressure | Control |
|---|---|---|
| Attributable | Shared lab accounts (INJ-030) | Flag shared credentials |
| Legible / contemporaneous | eBR back-entry (INJ-025) | Preserve downtime linkage |
| Original | Certificate transcription (INJ-036) | Prefer signed source lineage |
| Accurate | Unit mismatch (INJ-024) | Conflict state |
| Complete | Release packet gaps (INJ-028); eCTD gap (INJ-048) | Gap list |
| Consistent | Validation-state ambiguity (INJ-031) | Multi-label surfaced |
| Enduring / available | Audit trail disabled window (INJ-029) | DI incident flag |

## 5. Lineage and provenance model

Minimum provenance fields for any material fact: `source`, `record_id`, `authority`, `effective_at`, `retrieved_at`, `sha256`, `source_preserved=true` (aligns `evidence_item.schema.json`).

**Citation ≠ provenance:** listing a CSV path is insufficient without authority/as-of/integrity and conflict path.

## 6. Retention / privacy / residency tensions

| Tension | Inject | Rule |
|---|---|---|
| DSR delete vs GxP/legal hold | INJ-061 | Surface conflict; no silent delete |
| Cross-border secondary use | INJ-060 | Purpose check |
| Backup residency | INJ-064 | Flag unapproved region |
| Genomic re-ID | INJ-059 | Minimise / abstain |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-001 | Gap | Full DATASET_PROFILE walkthrough not duplicated here | Open — cite E-001 |
| R-002 | Assumption | Vignette row counts sufficient for conflict demos | Accepted |
| R-003 | Risk | Future ETL “cleans” declared exceptions | Control via INV-07 |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| 84 injects evidence-mapped | inject_evidence_register.csv | Done |
| Knowledge trust catalogued | knowledge_trust_catalogue.csv | Done |
| Unit conflict preserved | anchor_conflict_register.md | Done |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Pending | GxP lead | — |
