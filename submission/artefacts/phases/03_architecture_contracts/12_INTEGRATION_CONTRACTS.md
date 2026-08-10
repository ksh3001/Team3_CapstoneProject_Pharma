# Integration Contracts

> Team3 Phase 3 artefact (template 12).

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Architecture / Build |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Security; Evaluation |
| Status | Phase 3 complete |
| Related | `submission/src/contracts/` v1.0.0-poc; `api_contracts.md` |

## Purpose

Define versioned I/O contracts, ACL read integrations, and explicit non-integrations (writes).

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-IC-01 | `submission/src/contracts/*.schema.json` | Pinned copies |
| E-IC-02 | `evaluation/contracts/` | Package authority |
| E-IC-03 | `artefacts/prompts/08_technical/api_contracts.md` | Endpoint shapes |
| E-IC-04 | `data/tool_manifest_poisoned.json` | Poison fixture exists |

## 1. System/interface inventory

| Interface | Direction | Mode |
|---|---|---|
| Challenge CSV/knowledge | Read | ACL only |
| IAM entitlements CSV | Read | Authoritative |
| Access cache CSV | Read | Non-authoritative |
| Workflow CLI/API | In/Out | Local |
| LLM endpoint | Out | Disabled |
| MES/WMS/Safety write APIs | — | **Not integrated** |
| tool_manifest_poisoned | — | **Must not load** |

## 2. Versioned input contracts

| Workflow | Required inputs |
|---|---|
| batch_evidence | request_id, batch_id, purpose, as_of, user, mode, idempotency_key |
| pv_intake | request_id, case_ids, purpose, as_of, user, mode, idempotency_key |
| supply_options | request_id, event_id, purpose, as_of, user, mode, idempotency_key |
| authz/check | user, purpose, object_type, object_id, as_of |
| evaluate/run | request_id, suite, user, purpose, as_of, idempotency_key |

## 3. Versioned output contracts

| Schema | Critical constants |
|---|---|
| batch_response | workflow=batch_evidence; execution_status=not_executed; readiness enum |
| pv_response | workflow=pv_intake; no final safety fields |
| supply_response | no_side_effects=true; options status=draft |
| evidence_item | authority, effective_at, integrity.sha256, source_preserved=true |

Participant pin: `submission/src/contracts/VERSION.md` → **1.0.0-poc**.

## 4. Error and idempotency

Error envelope without stacks; 403 authz; 422 prohibited/schema; 409 idempotency/side-effect; Idempotency-Key 8–128 chars.

## 5. AuthZ and tool boundary

Purpose-bound check every workflow; poisoned tool manifest not on load path (phase3 test).

## 6. Compatibility / evolution

`additionalProperties: false`; additive fields require version bump + Evaluation approval.

## 7. Non-functional integration constraints

Offline deterministic; no challenge writes; latency best-effort (p95 load inconclusive).

## Risks, assumptions and unresolved gaps

| ID | Description | Status |
|---|---|---|
| R-IC-01 | validate.py still points CONTRACTS at package path | Accepted (pin copies for evidence) |
| R-IC-02 | Production API authn not specified | Deferred |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Schemas pinned | src/contracts | Pass |
| Writes not integrated | ADR-003 + tests | Pass |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Team3 Architecture | Owner | 2026-08-07 |
