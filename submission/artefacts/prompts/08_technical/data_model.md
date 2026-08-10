# Data Model — AEGIS Evidence Assist (POC)

| Field | Entry |
|---|---|
| Prompt | `prompts/08_technical_design.md` |
| Persistence | Local Evidence & Audit Store (ADR-006) — JSON files and/or SQLite |
| Never write back | Challenge package `data/`, `knowledge/`; MES/WMS/Safety execution systems (ADR-003) |

## Entities (logical)

### AuthorizationDecision

| Field | Type | Notes |
|---|---|---|
| user | string | |
| purpose | enum | batch_evidence, pv_intake, supply_options, evaluate |
| object_type | enum | |
| object_id | string | |
| as_of | datetime UTC | |
| checked_at | datetime UTC | |
| decision | allow\|deny | |
| reason | string | |
| iam_state_observed | string | |
| cache_state_observed | string\|null | never sole allow basis |

### EvidenceItem

Align to `evidence_item.schema.json`:

| Field | Type | Notes |
|---|---|---|
| source | string | adapter/source system id |
| record_id | string | |
| authority | string | |
| effective_at | string\|null | |
| retrieved_at | string | |
| facts | object | verbatim values; include `unit` when quantitative |
| integrity.sha256 | 64 hex | |
| integrity.source_preserved | const true | |

### Conflict / Gap / Abstention

| Field | Type | Notes |
|---|---|---|
| id | string | |
| type | conflict\|gap\|abstention | |
| objects | string[] | record ids |
| description | string | |
| blocking_ready | boolean | |

### BatchEvidencePack

Fields required by `batch_response.schema.json` + local `stored_at`, `content_sha256`.

**Must never store:** disposition/release/reject/recall fields.

### PvIntakePacket

Per `pv_response.schema.json`.

**Must never store:** final safety conclusion fields; irreversible merge flags as executed.

### SupplyOptionSet

Per `supply_response.schema.json` with `no_side_effects=true`.

**Must never store/write:** reservation/allocation/shipment/status-change/recall execution records.

### AuditSnapshot (ADR-010)

| Field | Type |
|---|---|
| request_id | string |
| workflow | string |
| mode | deterministic_offline\|ai_disabled |
| contract_versions | object |
| authz_ref | string |
| citation_hashes | string[] |
| gate_result | pass\|fail\|n_a |
| idempotency_key | string |
| created_at | datetime UTC |

### EvaluationRunResult

| Field | Type |
|---|---|
| run_id | string |
| suite | string |
| fixture_id | string |
| gate | pass\|fail |
| ac_ids | string[] |
| evidence_path | string |
| ready_blocked | boolean |

## Identity & time semantics

| Concept | Rule |
|---|---|
| batch_id | Exact string match only |
| case_id | Exact / strong_key per matching_thresholds |
| as_of | Request UTC instant for applicability |
| Source clocks | Multi-cite on disagreement (ADR-009); do not collapse |
| Units | Never silent convert; Conflict if unit≠spec or mapping approved=no |

## Relationships

- Pack 1—* EvidenceItem (citations)  
- Pack 1—* Conflict/Gap/Abstention  
- Pack 1—1 AuditSnapshot  
- EvaluationRun *—* Pack (by fixture)

## Quality status (supply availability) — assumed for POC

| quality_status | Available for options? |
|---|---|
| released | yes |
| quarantine | **no** (AMB-SUP-01 assumed) |
| other/unknown | **no** (fail closed) |
