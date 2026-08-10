# ADR-007 — Fail-closed duplicate matching without fuzzy until threshold known

| Field | Entry |
|---|---|
| Status | **accepted** (POC assessed mode) |
| Date | 2026-08-06 |
| Owners | PV domain; Evaluation |
| Related BC | BC-PV |
| C4 | PV Intake Service |
| FR | FR-004; matching_confidence_checklist |

## Evidence basis

- **Fact:** AMB-PV-01 fuzzy threshold Unknown; checklist forbids guessed thresholds.
- **Fact:** POL-NO-IRREVERSIBLE-MERGE; BR-032–033.

## Context

Forces: miss duplicates vs false merges harming safety clocks/cases.

## Decision

Duplicate strategies: exact ID → strong deterministic key bundle only. **No fuzzy auto-link** until a numeric threshold is approved. Below that, queue `duplicate_manual_assessment`.

## Alternatives considered

1. Fuzzy at 0.8 “industry default” — rejected (invents number).  
2. Always human-only clustering — acceptable but slower; keep exact/strong first.  
3. Fail-closed without fuzzy — **chosen**.

## Drivers

Hypothesis scarce data; patient safety risk of bad merges.

## Consequences

- Easier: no false-accept merges.  
- Harder: more Waiting on manual duplicate queue.  
- Risk: missed true duplicates — HITL review list mitigates.

## Guardrails

- BR-032–033; no irreversible merge APIs.

## NFRs

- Auto-merge count in assessed suites = **0**.  
- Fuzzy links emitted = **0** until threshold ADR update.

## Security / privacy

Avoid wrong-patient joins; minimize over-linkage.

## Operational impact

Monitor duplicate_manual_assessment queue depth; alert if depth > **Unknown** TBD after Measure.

## Validation

- AC-031; fixture with near-match narratives must not auto-merge.

## Revisit triggers

- When labeled duplicate golden set ≥ **50** pairs yields precision ≥ **0.95** at a chosen threshold under offline eval — then new ADR may enable fuzzy at that number.
