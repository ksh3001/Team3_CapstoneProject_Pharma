# FR-006 — Offline deterministic and AI-disabled continuity

| Field | Entry |
|---|---|
| Feature ID | FR-006 |
| Name | Offline deterministic and AI-disabled continuity |
| Owning context | Shared runtime / Reliability |
| Status | provisional |
| Matching/confidence | N/A |

## Actors

- Any entitled workflow user
- Operations / continuity owner
- System runtime mode controller

## Preconditions

- FR-001–005 capabilities exist in deterministic form.
- Continuity requirements known: batch/supply 14-day AI outage with manual runbook; PV max_ai_outage_hours=0.

## Happy path

1. Default assessed mode is deterministic offline (no model call).
2. User completes FR-003/004/005 without generative AI.
3. On AI-disabled signal, system refuses model ports and continues rules paths.
4. Manual runbook steps are available for human continuation.

## Exceptions / alternate paths

- Model region outage → enter AiDisabledMode; do not hang waiting for inference.
- PV intake requested with AI required flag → reject AI dependency; proceed rules-only or manual (hours=0).
- Kill switch → halt optional AI; preserve audit.

## Business rules

- BR-050: Assessed default mode must not require live model inference.
- BR-051: AI-disabled mode must keep FR-003/004/005 rules paths available or explicitly route to documented manual runbook.
- BR-052: PV continuity must not depend on model availability (max_ai_outage_hours=0).

## Acceptance criteria

- AC-050: Given model endpoint unavailable, when batch pack is requested in assessed mode, then pack still produces via deterministic path or controlled manual handoff — not a hard hang on inference.
- AC-051: Given AI-disabled mode, when optional narrator is invoked, then it is refused and rules path remains.
- AC-052: Given continuity drill checklist, when executed for batch/supply 14-day and PV without inference, then drill can complete using documented steps.

## HITL / AI boundaries

- AI optional only. Continuity is human + rules.

## Out of scope

- Full DR site design; vendor SLA contracts (later artefacts).

## Ambiguities

- AMB-CONT-01: Exact manual runbook step texts — to be authored in Phase 7 runbooks; feature requires their existence as AC-052 evidence.
