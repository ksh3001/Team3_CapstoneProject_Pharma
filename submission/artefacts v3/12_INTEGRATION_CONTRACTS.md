# Integration Contracts

> Phase 3. Versioned read-only contracts for LIMS v1/v2, MES, E2B, IDMP. No silent unit conversion.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Architecture + Domain |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP; Evaluation |
| Status | Draft |
| Related requirements / ADRs | ADR-037/038; INV-02; INJ-024/045; api_contract_versions.csv |

## Purpose

Pin inbound interface shapes, ACL translation rules, time/identity semantics, and error/idempotency behaviour so the evidence core does not invent fields or write back to sources.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | `data/api_contract_versions.csv` | LIMS v1/v2 field names; E2B_R3 |
| E-002 | `data/interface_mappings.csv` | CRO_LAB_TO_LIMS mg/L→ug/mL unapproved |
| E-003 | `data/interface_events.csv` | timeout/retry/idempotency themes |
| E-004 | `data/system_inventory.csv` | LIMS-4 GxP critical |
| E-005 | `data/idmp_mappings.csv` / medicinal_products | IDMP identity conflicts (INJ-045) |
| E-006 | evaluation/contracts | Outbound assist schemas |
| E-007 | ADR-037/038 | Read-only; dual ACL |

## 1. System/interface inventory

| System / API | Direction | Classification | Owner (case) | Assessed mode |
|---|---|---|---|---|
| LIMS result v1 | Inbound read | GxP critical | QC | Fixture/CSV |
| LIMS result v2 | Inbound read | GxP critical | QC | Fixture/CSV |
| MES / EBR / genealogy | Inbound read | GxP | Manufacturing | Fixture/CSV |
| Safety ICSR E2B_R3 | Inbound read | GxP / PV | Safety | Fixture/CSV |
| IDMP / medicinal product map | Inbound read | Regulatory | Regulatory | Fixture/CSV |
| WMS / inventory / cold-chain | Inbound read | Supply | Supply | Fixture/CSV |
| IAM entitlements | Inbound read | Security | Security | Fixture |
| Assist workflow responses | Outbound to human | Advisory | Digital | Schema v1 |
| Any source write | **PROHIBITED** | — | — | Denied |

## 2. Versioned input contracts

### LIMS result

| Version | Unit field | Status field | ACL rule |
|---|---|---|---|
| v1 | `unit` | `status` | Preserve raw; map to canonical only if approved mapping exists |
| v2 | `ucum_code` | `lifecycleState` | Preserve raw; do not coerce v1 labels into v2 enums silently |

**Conflict rule (INJ-024):** If `interface_mappings.approved != yes/true`, emit contradiction; **never** apply `1:1_assumed` conversion.

### MES / EBR

| Concept | Contract note |
|---|---|
| Step / exception events | Source timestamps kept distinct from retrieval time |
| Genealogy edges | Missing edges → gap (INV-07), not fabricated links |
| Change control / hotfix | Vendor hotfix without validation evidence → gap/abstention |

### Safety ICSR (E2B_R3)

| Concept | Contract note |
|---|---|
| Precision | Marked variable in api_contract_versions — do not over-precise |
| Clocks | Source event vs receipt vs awareness kept separate |
| Duplicates | Candidates only; no merge side effect |
| Output ban | No `final_reportability` / seriousness / causality finals |

### IDMP

| Concept | Contract note |
|---|---|
| Product identity | Conflicting IDMP mappings → contradiction (INJ-045) |
| Golden record | Not auto-merged; Master Data context surfaces conflict |

## 3. Versioned output contracts

| Workflow | Schema | Key consts |
|---|---|---|
| Batch | batch_response.schema.json | workflow=batch_evidence; execution_status=not_executed |
| PV | pv_response.schema.json | workflow=pv_intake; execution_status=not_executed |
| Supply | supply_response.schema.json | no_side_effects=true; options.status=draft |

Outbound version: **v1.0** adopted (DEC-030). Extensions only via submission overlay + tests.

## 4. Units and terminology

| Rule | Behaviour |
|---|---|
| Approved mapping | May present both source and canonical with citation |
| Unapproved mapping | Contradiction + abstain from numeric compare |
| Terminology drift | Record vocabulary version in evidence facts when present |
| Silent convert | **Forbidden** |

## 5. Time and identity semantics

| Clock | Use |
|---|---|
| `effective_at` | Authority/applicability of fact |
| `retrieved_at` | When assist loaded the record |
| `as_of` | Request temporal point for eligibility |
| Source vs receipt (PV) | Both cited in clock_evidence |

| Identity | Rule |
|---|---|
| Batch / case / event ids | Opaque strings from source; no rewrite |
| Crosswalks | Explicit mapping tables; conflicts preserved |

## 6. Error / idempotency / replay

| Concern | Contract |
|---|---|
| Source timeout | Gap + abstention; no invent fill |
| Retry | Safe because read-only; honor idempotency_key if present in interface_events |
| Replay | Same request_id + as_of → same advisory package (deterministic core) |
| Partial failure | Fail closed for that evidence slice; do not mark ready_for_review on missing critical DI |

## 7. Compatibility and contract tests

| Test | Expected Phase 3 |
|---|---|
| `python tools/test_contracts.py` | GREEN |
| `submission/tests/test_schema_contracts.py` | GREEN |
| LIMS v1/v2 ACL unit tests | Deferred Phase 5 (loaders) — specified here |
| Runtime IAM/tool/instruction gates | RED (`test_prohibited_runtime_gates.py`) |

### Planned loader acceptance (Phase 5)

| Case | Expect |
|---|---|
| LIMS v1 row with unit only | Loads; facts.unit preserved |
| LIMS v2 row with ucum_code | Loads; facts.ucum_code preserved |
| CRO_LAB_TO_LIMS unapproved | contradictions includes unit_mapping_unapproved |
| E2B precision variable | No forced decimal normalization |
| IDMP conflict | contradictions includes identity_conflict |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-321 | Gap | Live LIMS/MES not available — fixtures stand in | Integration realism | Architecture | Accepted for POC |
| A-018 | Assumption | api_contract_versions rows are complete for scored paths | Missed field drift | Domain | Open |

## Traceability and acceptance

| Claim | Control | Test | Result |
|---|---|---|---|
| Dual LIMS ACL | ADR-038 | Phase 5 loader tests | Specified |
| No source writes | ADR-037 | C4 PROHIBITED + import policy | Draft |
| Unapproved unit map | INV-02 | INJ-024 fixture | Phase 5 |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | Domain + Architecture | Pending | | |
