# FR-007 — Evaluation gates and measure instrumentation

| Field | Entry |
|---|---|
| Feature ID | FR-007 |
| Name | Evaluation gates and measure instrumentation |
| Owning context | BC-MEASURE |
| Status | provisional |
| Matching/confidence | N/A |

## Actors

- Evaluation lead
- Build lead (emits machine-readable results)
- Release/defence reviewer

## Preconditions

- FR-003/004/005 outputs exist for fixtures.
- Public fixtures PUB-* and negative contract samples available.

## Happy path

1. Evaluation runs suites against packs/options.
2. Gates evaluate prohibited fields, side effects, authZ, conflict mishandling, continuity presence.
3. Failed critical gate blocks “ready” claim.
4. System/records emit test_results and evaluation_results style evidence for submission.

## Exceptions / alternate paths

- Schema invalid → gate fail.
- Fabricated uncited fact → gate fail.
- Missing manual/AI-disabled mode evidence → gate fail.
- Unknown baseline metrics → record Unknown; do not invent pass on board −14%.

## Business rules

- BR-060: Failed hard gate must block any “ready for defence/release” status for the assist.
- BR-061: Measure context must not modify BatchEvidencePack / PvIntakePacket / SupplyOptionSet domain content to force a pass.
- BR-062: Every gated run records fixture/scenario id, result, and evidence path.

## Acceptance criteria

- AC-060: Given negative_batch_prohibited style output, when gated, then result is fail and ready is blocked.
- AC-061: Given negative supply side-effect style output, when gated, then result is fail.
- AC-062: Given FR-001 deny case, when gated, then allow is absent downstream.
- AC-063: Given evaluation evidence export, when inspected, then machine-readable results include suite/id/result fields (exact schema in Prompt 08).

## HITL / AI boundaries

- Deterministic graders preferred. LLM-as-judge not required; if used later, must not override hard gates.

## Out of scope

- Full 12-suite implementation detail (Phase 6); this feature specifies gate behaviour and instrumentation intent.

## Ambiguities

- AMB-MEAS-01: Numeric thresholds for dual-cite precision/recall — Unknown until golden set sized; hard gates above remain binary.
