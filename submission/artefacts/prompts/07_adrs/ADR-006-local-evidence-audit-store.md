# ADR-006 — Local evidence and audit store for POC

| Field | Entry |
|---|---|
| Status | **proposed** |
| Date | 2026-08-06 |
| Owners | Architecture; Evaluation |
| Related BC | Shared audit; BC-MEASURE |
| C4 | Evidence & Audit Store |
| FR | FR-007; all emit audit |

## Evidence basis

- **Fact:** Offline assessed mode; submission evidence must be exportable locally.
- **Assumption:** File/JSON (or local SQLite) suffices for POC audit volume.

## Context

Forces: enterprise ledger vs offline reproducibility.

## Decision

Persist packs, AuthorizationDecisions, gate results, and hashes in a **local Evidence & Audit Store** under `submission/` working paths (files and/or SQLite). No mandatory remote ledger in assessed POC.

## Alternatives considered

1. External immutable ledger service — deferred production.  
2. Memory-only — rejected (no defence evidence).  
3. Local store — **chosen**.

## Drivers

DoD evidence export; offline; ADR-001.

## Consequences

- Easier: clean-room zip of evidence.  
- Harder: weaker WORM guarantees.  
- Risk: tampering — mitigate with export hashes (`file_hashes.csv`) and read-only challenge data.

## Guardrails

- BR-061 Measure must not rewrite packs to force pass; store writes append audit, not silent conflict clears.

## NFRs

- Evidence export completes on local disk; integrity via sha256 manifest. RPO for POC store = **last export** (manual).

## Security / privacy

No credentials in store; purpose-tagged records; synthetic data only.

## Operational impact

Backup = copy submission/evidence. Reset script clears working store without touching challenge package.

## Validation

- Evidence export script; hash_submission; AC-063.

## Revisit triggers

- When regulatory e-sign/WORM required for production records OR store size > **1 GB** active audit without retention policy.
