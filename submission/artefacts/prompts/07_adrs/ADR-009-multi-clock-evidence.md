# ADR-009 — Preserve multi-clock evidence (no silent single clock)

| Field | Entry |
|---|---|
| Status | **proposed** (interim: dual-cite always on disagreement) |
| Date | 2026-08-06 |
| Owners | Domain; PV; Architecture |
| Related BC | BC-PV; shared as_of |
| C4 | PV Intake Service; Evidence Items |
| FR | FR-004; AMB-BATCH-02 |

## Evidence basis

- **Fact:** INJ-038 reporting-clock conflict; continuity of as_of in contracts.
- **Fact:** BR-034 disagreeing clocks remain visible.
- **Assumption:** Event vs report vs receipt semantics per dataset still partially Unknown (P1 backlog).

## Context

Forces: one “canonical time” for UX vs compliance clock reconstruction.

## Decision

For assessed POC, when awareness/receipt/report times disagree, **cite all** in clock_evidence and require human review. Do not collapse to a single chosen clock in system output. Workflow as_of is request parameter, not a substitute for source clocks.

## Alternatives considered

1. Earliest awareness always wins — rejected without policy SoT.  
2. Latest receipt always wins — rejected.  
3. Dual/multi cite + HITL — **chosen** interim.

## Drivers

POL clocks; hard gate against unresolved conflict presented as resolved.

## Consequences

- Easier: inspection defence.  
- Harder: more HITL Waiting.  
- Risk: ambiguity remains until P1 dictionary — acceptable under hypothesis.

## Guardrails

- BR-034; ready/final reportability never auto-set from a picked clock.

## NFRs

- Silent single-clock collapse incidents in suites = **0**.

## Security / privacy

Accurate clocks reduce wrongful expedited handling from fake rules.

## Operational impact

Queue metric: clock_resolution reviews.

## Validation

- AC-032; PUB PV clock fixtures.

## Revisit triggers

- When P1 clock dictionary + PV policy names authoritative clock per jurisdiction — update ADR with explicit precedence table; or if clock-review queue p95 wait > **4 h** forcing prioritization rules.
