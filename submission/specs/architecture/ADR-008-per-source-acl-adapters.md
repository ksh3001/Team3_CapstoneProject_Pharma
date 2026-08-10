# ADR-008 — Per-source ACL adapters (not mega-ingest lake)

| Field | Entry |
|---|---|
| Status | **proposed** |
| Date | 2026-08-06 |
| Owners | Architecture; Domain/evidence |
| Related BC | ACL supporting; BC-BATCH/PV/SUPPLY |
| C4 | Read Connectors + ACL |
| FR | FR-003/004/005 |

## Evidence basis

- **Fact:** Unit/contract version conflicts (LR-88; LIMS v1/v2); SOURCE_SYSTEM_FACT_PACK says no universal SoT.
- **Derivation:** One lake without ACL recreates equal-trust / silent conversion defects.

## Context

Forces: fast dump-all ingest vs anti-corruption.

## Decision

Implement **per-source-family ACL adapters** that emit Evidence Items in ubiquitous language (with source, authority, units, times). Do not build a single untyped mega-ingest lake for assessed POC.

## Alternatives considered

1. Dump all CSV to one store and query loosely — rejected.  
2. Full canonical MDM platform first — parallel programme (deferred FR), not blocker for ACL.  
3. Per-source ACL — **chosen**.

## Drivers

POL-NO-SILENT-UNIT; DDD ACL; ADR-C08.

## Consequences

- Easier: testable unit/authority mapping per source.  
- Harder: more adapter code.  
- Risk: adapter sprawl — limit to sources needed by PUB fixtures + core workflows.

## Guardrails

- Adapters never silent-convert units; emit Conflict instead.  
- Adapters read-only toward sources.

## NFRs

- Adapter count bounded to fixture-needed sources in POC; each declares mapping version.  
- Staleness surfaced: as_of vs extract time shown; max acceptable staleness **Unknown** until Measure.

## Security / privacy

Purpose filters at AuthZ before adapter fetch; no cross-purpose bulk pull.

## Operational impact

Version adapters with schema tests; rollback = prior adapter version.

## Validation

- AC-020; contract evidence_item shape; ACL unit tests per adapter.

## Revisit triggers

- When onboarded source families > **10** without shared mapping toolkit; or silent conversion defect escapes (>**0** in gates).
