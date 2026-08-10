# Ontology and Semantic Layer

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Domain & evidence lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Architecture lead |
| Status | Draft — Stage 2 |
| Related requirements / ADRs | Artefact 05; Prompt 04; terminology/IDMP/alias datasets |

## Purpose

Define the minimum semantic layer (concepts, identifiers, time, jurisdiction, units, vocabularies) so AEGIS can cite and compare evidence without inventing a full enterprise ontology or requiring a graph database.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `submission/artefacts/05_DDD_CONTEXT_MAP.md` | Stage 2 | Ubiquitous language + contexts | Draft |
| E-002 | `data/controlled_vocabularies.csv` | Vocab v2026-1 | dose_form / route codes | Sparse |
| E-003 | `data/terminology_versions.csv` | MedDRA | 27.1 legacy_cases; 28.0 current_global | Dual version |
| E-004 | `data/product_master_aliases.csv` | Aliases | NCB204 / brand → NCB-204 | Incomplete universe |
| E-005 | `data/idmp_mappings.csv` | IDMP | ambiguous_strength_presentation | Conflict |
| E-006 | `data/timezone_rules.csv` (case INJ-018) | Time rules | DST/local vs UTC issues exist in estate | Clinical-linked |
| E-007 | `data/interface_mappings.csv` | Units | Unapproved conversion | Binding constraint |

## 1. Competency questions

| CQ | Needed for workflow | Answer approach |
|---|---|---|
| CQ-1 What evidence applies to batch B at as-of T? | Batch | Filter by batch_id + effective dating + authority |
| CQ-2 Are two lab values comparable (same unit/method)? | Batch | Require approved unit mapping; else abstain |
| CQ-3 Are cases A/B duplicate candidates? | PV | Shared identifiers/aliases + time windows; human decides merge |
| CQ-4 Which MedDRA version coded this AE? | PV | Persist terminology version on code |
| CQ-5 Which inventory lots are eligible for draft options under quality holds? | Supply | Join inventory + quality status + constraints; no status write |
| CQ-6 Which document is effective policy for purpose P at T? | All | knowledge_catalog status/effective/supersedes/trust |

## 2. Core concepts and relations

| Concept | Relations | Notes |
|---|---|---|
| MedicinalProduct | hasAlias; maybeMapsTo IdmpProduct | Ambiguity allowed |
| Batch | producedAs; hasLabResult; hasDeviation; hasReleasePacket | Genealogy may be incomplete |
| LabResult | hasUnit; hasStatus (incl. OOS/OOT/invalid disagreement) | Multi-status preserved |
| IcsrCase | hasReceipt; hasAdverseEvent; maybeDuplicateOf | Candidate only |
| Shipment | hasLogger; hasTemperatureExcursion | Association may be disputed |
| InventoryLot | hasQualityStatus; constrainedBy AllocationPolicy | Status not changed by AEGIS |
| EvidenceItem | cites Record; hasAuthority; asOf | Required on outputs |
| Actor | hasEntitlement; hasPurpose | Checked at runtime |

## 3. Identifiers and aliases

| Rule | Detail | Evidence |
|---|---|---|
| Canonical product | Prefer portfolio product_id (e.g. NCB-204) | portfolio_products |
| Aliases | Record alias→canonical with provenance | E-004 |
| IDMP | If mapping_status ≠ clear, expose ambiguity | E-005 |
| Case IDs | Keep source case IDs; cluster via duplicate_candidates | icsr / duplicates |
| Never | Collapse distinct entities because strings look similar | E-001 |

## 4. Temporal and jurisdictional semantics

| Dimension | Rule |
|---|---|
| As-of | Assessment time bound; effective documents filtered by effective ≤ as-of and not superseded |
| Event vs report time | Preserve both when present; do not coerce |
| Timezone | Do not assume UTC; flag mixed local/UTC/DST (INJ-018 pattern) |
| Jurisdiction | Policy/doc jurisdiction must match purpose (EU QP vs US etc.) |
| Later timestamp | Not automatically more authoritative than signed approved record |

## 5. Controlled vocabularies and units

| Area | Approach |
|---|---|
| Dose form / route | Use controlled_vocabularies where present; versioned | E-002 |
| MedDRA | Carry version; do not silently upgrade 27.1→28.0 | E-003 |
| Units | Only approved interface_mappings; else abstain | E-007 |
| Quality status terms | Preserve source vocabulary; map only via explicit table | — |

## 6. Entitlements and policy context

| Context field | Use |
|---|---|
| user, role, purpose, object | Authorization decision allow/deny |
| tool signature / allow-list | Tool invocation |
| document trust | approved vs untrusted/superseded/draft |
| data residency / hold | Restrict export/deletion actions |

## 7. Versioning and validation

| Asset | Versioning |
|---|---|
| Semantic rules | Version with artefact 07; changes via review |
| Contracts | evaluation/contracts schema versions |
| Vocabularies | Retain source version fields |
| Validation | Competency questions → deterministic tests in Stage 5 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Controlled vocab coverage sparse (2 rows) | Many terms remain free text | Domain | Master-data work | Open |
| R-002 | Assumption | CSV + rules sufficient vs formal OWL ontology for v1 | May revisit | Architecture | Stage 3 ADR | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Competency questions listed | §1 | Tests map CQ→AC in artefact 09 | This artefact | Draft |
| Unit/time/jurisdiction rules explicit | §4–5 | Negative unit/time tests | E-006, E-007 | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Architecture lead | Reviewer | Keep ontology minimal for v1 | Accepted | 2026-08-07 |
