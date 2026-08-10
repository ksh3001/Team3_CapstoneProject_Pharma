# ADR-003 — No operational write adapters in assessed mode

| Field | Entry |
|---|---|
| Status | **accepted** (POC assessed mode) |
| Date | 2026-08-06 |
| Owners | GxP; Security; Architecture |
| Related BC | BC-SUPPLY, BC-BATCH, BC-PV |
| C4 | PROHIBITED edges to Exec/WMS/MES; SideEffectGuard |
| FR | FR-005; FR-003; FR-007 |

## Evidence basis

- **Fact:** `ai_use_boundaries.csv` prohibits reserve/allocate/ship; decision_rights draft only for allocation.
- **Fact:** Starter `plan_supply` creates reservation_status — anti-pattern.
- **Fact:** Hard gates / supply schema require `no_side_effects`.

## Context

Forces: planners want “one-click reserve” vs fail-closed assessed scoring.

## Decision

Assessed mode **deploys no write adapters** to MES/WMS/Safety execution APIs. SupplyOptionSet is advisory only; SideEffectGuard asserts no reservation/allocation/shipment/status/recall mutations. Batch/PV services never write disposition/final conclusions to SoRs.

## Alternatives considered

1. Write tools with human confirmation — rejected for assessed POC (still side-effect capable).  
2. Separate “execution plane” service — deferred to production ADR; not in assessed map.  
3. No write adapters assessed — **chosen**.

## Drivers

POL-NO-SIDE-EFFECTS; POL-NO-DISPOSITION; POL-NO-FINAL-PV; scoring hard gates.

## Consequences

- Easier: prove PROHIBITED paths absent by construction.  
- Harder: demo less “end-to-end ops.”  
- Risk: production pressure to add writes — requires new ADR + tests before enablement.

## Guardrails

- POL-040–043; C4 red dashed PROHIBITED links; schema rejects execution fields.

## NFRs

- Side-effect count in assessed suites = **0**.  
- Architecture dependency check: no source-write client modules linked in assessed build.

## Security / privacy

Reduces excessive agency / tool abuse (INJ-066).

## Operational impact

No rollback of external state (none written). Alert on SideEffectGuard trip = P1 security/GxP.

## Validation

- AC-040–043, AC-021, AC-060–061; filesystem/DB assert no reservation files; negative contract samples.

## Revisit triggers

- When production execution plane is approved by Supply Governance + CISO with dual control AND assessed suite still proves advisory path intact; or any SideEffectGuard trip in pilot (>**0** events).
