# Integration Contracts

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Architecture / integration lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Evaluation lead; GxP lead |
| Status | Draft — Stage 3 |
| Related requirements / ADRs | ADR-003, 004, 008–010; artefact 09 ACs; `evaluation/contracts/` |

## Purpose

Define versioned integration and workflow contracts for AEGIS v1: request/response shapes, read-only source adapters, error/authz semantics, and the Stage 3 contract-test gate.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `evaluation/contracts/batch_response.schema.json` | Package v | Batch I/O | Fail-closed |
| E-002 | `evaluation/contracts/pv_response.schema.json` | Package v | PV I/O | Fail-closed |
| E-003 | `evaluation/contracts/supply_response.schema.json` | Package v | Supply I/O | Fail-closed |
| E-004 | `evaluation/contracts/evidence_item.schema.json` | Package v | Evidence citation | source_preserved=true |
| E-005 | `evaluation/contract_samples/*` | Package | Positive/negative samples | Not full product tests |
| E-006 | `tools/test_contracts.py` run 2026-08-07 | Local | 6/6 PASS | See evidence note |
| E-007 | `starter/api_samples/*` | Brownfield samples | LIMS v1/v2, tool manifests | Defective by design |

## 1. Workflow response contracts (system of interaction)

| Workflow | Schema | Critical consts / enums |
|---|---|---|
| Batch evidence | E-001 | workflow=`batch_evidence`; execution_status=`not_executed`; readiness_state enum |
| PV intake | E-002 | workflow=`pv_intake`; execution_status=`not_executed` |
| Supply options | E-003 | workflow=`supply_options`; no_side_effects=`true`; options[].status=`draft` |
| Shared | authorization{user,purpose,checked_at,decision}; evidence[]; contradictions; gaps; abstentions; human_review; audit | additionalProperties=false |

**Extension rule:** Participant may version-extend only with compatibility tests and preserved fail-closed boundaries (`starter/contracts/WORKFLOW_CONTRACTS.md`).

## 2. Evidence item contract

| Field | Rule |
|---|---|
| source, record_id, authority | Required strings |
| effective_at | string or null |
| retrieved_at | required |
| facts | object (verbatim-oriented) |
| integrity.sha256 | 64 hex |
| integrity.source_preserved | const true |

## 3. Source adapter contracts (read-only)

| Source | Direction | Notes |
|---|---|---|
| `data/*.csv` challenge sets | Read | Immutable; hash-protected |
| knowledge_catalog + knowledge/*.md | Read | Filter by trust/status/effective |
| IAM entitlements | Read | Prefer users_entitlements.iam_state over cache |
| MES/LIMS/inventory SoR | Out of band / simulated via CSV | **No write** adapters in v1 |
| Tool manifests | Read + verify signature | Reject poisoned write tools |

## 4. Request contract (logical)

| Field | Required | Notes |
|---|---|---|
| request_id | yes | Idempotency key |
| workflow | yes | batch_evidence / pv_intake / supply_options |
| as_of | yes | Temporal bound |
| user / purpose | yes | Authz |
| object ids | yes | batch_id / case package / event_id |
| mode | yes | `deterministic` \| `model_assist` (default deterministic) |

## 5. Error and denial semantics

| Condition | Behavior |
|---|---|
| Schema invalid output | Reject; do not return partial regulated conclusion |
| Authz deny | authorization.decision=deny; no evidence fabrication |
| Unapproved unit mapping | Contradiction/abstention; no converted pass |
| Untrusted instruction doc | Ignore as command; optional gap/security flag |
| Model disabled / offline | Deterministic path or explicit manual handoff |

## 6. Event semantics

| Event | Payload gist | Side effects |
|---|---|---|
| EvidenceAssessed | batch pack hash | none to SoR |
| PvIntakeAssembled | case_ids + pack hash | none |
| SupplyOptionsDrafted | event_id + options hash | none |
| AuthorizationDenied | user/purpose/reason | none |

## 7. Contract tests (Stage 3 exit)

| Suite | Result | Evidence |
|---|---|---|
| positive_batch / pv / supply | PASS | E-006 |
| negative_batch_prohibited / pv_prohibited / supply_side_effect | PASS | E-006 |
| Command | `python tools/test_contracts.py` | `submission/evidence/contract_tests_stage3.md` |

**Deferred to Stage 4–5 (not Stage 3 artefacts):** PUB-09–15 participant-defined non-executing contracts (security/reliability/privacy/…).

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | OpenAPI not yet published | Agent coding friction | Architecture | Stage 5 | Open |
| R-002 | Assumption | Package schemas sufficient for v1 POC | May need version bump | Architecture | Stage 5 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Fail-closed boundaries | §1–2 | test_contracts.py | E-006 | PASS |
| Read-only integrations | §3 | ADR-004 | This artefact | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Evaluation lead | Reviewer | Contract gate met for Stage 3 | PASS logged | 2026-08-07 |
