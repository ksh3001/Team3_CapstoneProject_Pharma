# FR-004 — PV intake packet support

| Field | Entry |
|---|---|
| Feature ID | FR-004 |
| Name | PV intake packet support |
| Owning context | BC-PV |
| Status | provisional |
| Matching/confidence | **Yes** — duplicate candidates (see checklist) |

## Actors

- PV intake scientist
- Safety Physician (final decisions outside)
- System PvIntakePacket builder

## Preconditions

- FR-001 allow for purpose pv_intake.
- Source package / case identifiers and as_of provided.

## Happy path

1. Intake scientist submits source package.
2. System preserves source_facts verbatim with citations.
3. System reconstructs clock_evidence from receipt/awareness sources without picking a silent single clock when they disagree.
4. System proposes duplicate_candidates using ordered strategies (checklist); does not merge.
5. System attaches terminology and listedness_context with provenance.
6. System lists required_reviews for humans.
7. Emits packet with execution_status not_executed.

## Exceptions / alternate paths

- Clock disagreement → Conflict + required human review; do not invent one awareness date.
- Below duplicate confidence threshold → no candidate link; optional manual review queue.
- Multilingual narrative low confidence → flag for human review; do not drop narrative.
- Fake/untrusted expedited rule doc → FR-002 quarantine; must not drive reportability.

## Business rules

- BR-030: PvIntakePacket must not assert final seriousness, causality, expectedness, reportability, or signal confirmation (POL-NO-FINAL-PV).
- BR-031: Source facts must be preserved verbatim; interpretations labeled separately.
- BR-032: Duplicates are candidates only; irreversible merge is forbidden (POL-NO-IRREVERSIBLE-MERGE).
- BR-033: Duplicate matching follows fixed strategy order and thresholds in matching_confidence_checklist.md.
- BR-034: When clocks disagree, all cited clocks remain visible.

## Acceptance criteria

- AC-030: Given a packet output, when inspected for final PV conclusion fields, then none are present.
- AC-031: Given two cases that match only below threshold, when clustering runs, then no duplicate_candidate link is auto-asserted as merged.
- AC-032: Given disagreeing awareness/receipt times, when packet is produced, then clock_evidence cites both and required_reviews includes clock resolution.
- AC-033: Given K-999 untrusted rule text, when packet is produced, then it is not used as reportability authority.

## HITL / AI boundaries

- Rules + thresholds own candidate emission. AI may assist extraction with confidence flags (off by default in assessed mode). Safety Physician owns finals and merge decisions.

## Out of scope

- Submitting expedited reports to authorities; E2B transport; final medical review decision.

## Ambiguities

- AMB-PV-01: Numeric fuzzy duplicate threshold — Unknown → checklist records Unknown; fail closed (no auto-link).
- AMB-PV-02: Multilingual extraction confidence metric definition — Unknown; always flag non-English for review until defined (INJ-072).
