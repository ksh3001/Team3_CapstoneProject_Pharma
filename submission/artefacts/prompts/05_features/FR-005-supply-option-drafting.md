# FR-005 — Supply option drafting

| Field | Entry |
|---|---|
| Feature ID | FR-005 |
| Name | Supply option drafting |
| Owning context | BC-SUPPLY |
| Status | provisional |
| Matching/confidence | N/A for allocation decision; product identity exact |

## Actors

- Supply planner
- Supply Governance Board (allocation outside)
- System SupplyOptionSet builder

## Preconditions

- FR-001 allow for purpose supply_options.
- Shortage/cold-chain event_id, as_of, inventory snapshot, constraints available.

## Happy path

1. Planner requests options for event_id at as_of.
2. System loads inventory with quality_status; treats only permitted statuses as available for options.
3. System ranks draft options; lists violated constraints and approvals_required.
4. System sets no_side_effects true; execution_status not_executed.
5. Planner exports set for governance.

## Exceptions / alternate paths

- Quarantine (or non-released) stock → not counted as available; may appear under quality_holds / constraints.
- Any attempt to reserve/allocate/ship/change status/recall → reject; no writes.
- AuthZ deny → stop.

## Business rules

- BR-040: SupplyOptionSet.no_side_effects must be true (POL-NO-SIDE-EFFECTS).
- BR-041: Output must not include reservation, allocation, shipment, quality-status change, or recall execution properties.
- BR-042: Units with quality_status quarantine must not be included in available supply for ranking unless an explicit constraint path flags them as unavailable/hold.
- BR-043: Assessed mode must not create or persist draft reservations in any store.

## Acceptance criteria

- AC-040: Given NCB-204 Global quarantine units present, when options are drafted, then those units are not treated as available supply.
- AC-041: Given a completed SupplyOptionSet, when inspected, then no_side_effects is true and no reservation/allocation/shipment fields exist.
- AC-042: Given starter-like request to set reservation_status created, when feature runs, then it does not create a reservation and fails closed if such field is demanded.
- AC-043: Given negative side-effect contract sample shape, when validated, then it is rejected.

## HITL / AI boundaries

- Rules own availability and no_side_effects. Optional AI may narrate option trade-offs from cited constraints (off by default). Board owns allocation.

## Out of scope

- ERP/WMS execution; transport booking; recall initiation; ethics final allocation choice.

## Ambiguities

- AMB-SUP-01: Full list of quality_status values allowed as available — Unknown beyond released vs quarantine observed; default only explicit released (or synonym list TBD in Prompt 08).
- AMB-SUP-02: Ranking weights for ethics constraints — Unknown; list constraints and require human approval rather than hidden weighted optimize.
