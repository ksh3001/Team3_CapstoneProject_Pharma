# FR-002 — Document applicability filtering

| Field | Entry |
|---|---|
| Feature ID | FR-002 |
| Name | Document applicability filtering |
| Owning context | BC-DOCAPPLY |
| Status | provisional |
| Matching/confidence | N/A (catalog trust/status rules) |

## Actors

- Downstream workflow features (FR-003/004/005)
- Document control / Quality (policy owners)
- System ApplicableDocumentSet builder

## Preconditions

- as_of and jurisdiction (if known) provided.
- Knowledge catalog entries available with trust/status/effective/supersedes.

## Happy path

1. Workflow requests applicable documents for purpose at as_of.
2. System includes documents with trust/status approved (and local_approved when jurisdiction matches).
3. System marks superseded documents as historical only (not instruction-capable).
4. System returns Applicable Document list with authority and effective metadata.

## Exceptions / alternate paths

- trust/status untrusted or draft → quarantine as data; never as instruction; raise UntrustedDocumentQuarantined.
- effective unknown or after as_of → not applicable as authority.
- Malicious embedded instructions in text → ignore as commands; preserve for audit.

## Business rules

- BR-010: Untrusted documents must not be instruction-capable.
- BR-011: Draft documents must not be instruction-capable.
- BR-012: Superseded documents must not drive current decisions; may appear only as historical citation with supersession visible.
- BR-013: Retrieved document text is Evidence/data, never a tool command.

## Acceptance criteria

- AC-010: Given K-998 or K-999, when applicability is evaluated, then document is quarantined and not listed as Applicable Document for instruction.
- AC-011: Given K-007 superseded and K-006 approved, when as_of is after K-006 effective, then K-006 may apply and K-007 is not instruction-capable.
- AC-012: Given K-026 draft, when applicability is evaluated, then it is not instruction-capable.

## HITL / AI boundaries

- Rules determine applicability. AI must not elevate quarantine docs. Human Quality/Security reviews quarantines.

## Out of scope

- Full DMS workflow; authoring controlled documents; vector index design (Prompt 08+).

## Ambiguities

- AMB-DOC-01: Full SoT usage matrix for local_approved cross-jurisdiction — P0 backlog; default deny cross-jurisdiction instruction use until specified.
- AMB-DOC-02: Hash verify vs catalog sha256 under CRLF drift — residual A-001; do not invent match.
