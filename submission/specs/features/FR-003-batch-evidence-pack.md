# FR-003 — Batch evidence pack reconciliation

| Field | Entry |
|---|---|
| Feature ID | FR-003 |
| Name | Batch evidence pack reconciliation |
| Owning context | BC-BATCH |
| Status | provisional |
| Matching/confidence | Identity: exact batch_id only (see checklist) |

## Actors

- Quality / QP support reviewer
- EU Qualified Person (consumer of pack; decides outside)
- System BatchEvidencePack builder

## Preconditions

- FR-001 allow for purpose batch_evidence and batch object.
- batch_id and as_of provided.
- Upstream evidence accessible via anti-corruption mapping.

## Happy path

1. Reviewer requests BatchEvidencePack for batch_id at as_of.
2. System gathers Evidence Items (lab, genealogy, EM, deviations, release packet signals, etc.) with citations.
3. System applies FR-002 applicable documents.
4. System detects Conflicts (e.g. unit vs spec) and Gaps; records Abstentions when unresolved.
5. System sets readiness_state to one of: insufficient_evidence | conflicted_evidence | ready_for_authorized_review.
6. System emits pack with execution_status not_executed; human_review requirements listed.

## Exceptions / alternate paths

- Unit mismatch or unapproved conversion mapping → Conflict + Abstention; must not silent convert (POL-NO-SILENT-UNIT).
- Missing release-packet element → Gap; readiness cannot be ready_for_authorized_review if material gap open (rule AMB-BATCH-01 until enumerated).
- AuthZ deny → stop (FR-001).
- Attempt to include disposition fields → reject output (fail closed).

## Business rules

- BR-020: BatchEvidencePack must not contain batch disposition, release, reject, reprocess, relabel, or recall decisions (POL-NO-DISPOSITION).
- BR-021: execution_status must be not_executed.
- BR-022: readiness_state must be exactly one of insufficient_evidence, conflicted_evidence, ready_for_authorized_review.
- BR-023: When reported unit and specification unit disagree, or conversion mapping approved=no, system must record Conflict and must not convert values.
- BR-024: Every material claim in the pack must be cited as Evidence Item or covered by Abstention/Gap.
- BR-025: ready_for_authorized_review is input to human review only — not certification.

## Acceptance criteria

- AC-020: Given LR-88 style unit≠spec on the batch, when pack is produced, then a Conflict is present and potency is not asserted as within-spec via conversion.
- AC-021: Given a completed pack, when inspected, then execution_status is not_executed and no disposition fields exist.
- AC-022: Given material unresolved Conflict, when readiness_state is set, then it is conflicted_evidence or insufficient_evidence — not ready_for_authorized_review.
- AC-023: Given negative prohibited disposition payload shape, when validated, then it is rejected.

## HITL / AI boundaries

- Rules own conflicts/invariants. Optional AI may summarize cited conflicts only (off by default); must not set disposition or clear Conflicts. EU QP owns certification outside.

## Out of scope

- Performing batch certification; changing specs; MES write-back; API schemas (Prompt 08).

## Ambiguities

- AMB-BATCH-01: Exhaustive checklist of material gaps for readiness — Unknown; until listed, any open Conflict on potency/sterility/genealogy/QP packet blocks ready_for_authorized_review.
- AMB-BATCH-02: Full event vs report time fields per evidence class — P1 clock dictionary.
