# ADR-010 — Decision audit snapshot on every workflow response

| Field | Entry |
|---|---|
| Status | **proposed** |
| Date | 2026-08-06 |
| Owners | GxP; Evaluation; Architecture |
| Related BC | Shared kernel audit; BC-MEASURE |
| C4 | Evidence & Audit Store; all workflow services |
| FR | all; FR-007 |

## Evidence basis

- **Fact:** Contracts require audit object; DoD demands provenance.
- **Fact:** Hard gate on provenance/authority/effective date.

## Context

Forces: minimal logging vs inspection-ready evidence.

## Decision

Every workflow response persists an **audit snapshot**: request_id, user, purpose, as_of, authz decision, schema/contract versions, mode (offline/AI-disabled), citations list hashes, gate results, idempotency key. Snapshots land in local store (ADR-006).

## Alternatives considered

1. Log only errors — rejected (fails defence).  
2. External SIEM only — deferred.  
3. Response-embedded + local snapshot — **chosen**.

## Drivers

DoD §2–6; SUBMISSION_EVIDENCE_STANDARD.

## Consequences

- Easier: exportable defence trail.  
- Harder: storage growth.  
- Risk: PII in PV narratives — minimize; synthetic training data in POC.

## Guardrails

- BR-003, BR-062; no audit rewrite to erase Conflicts.

## NFRs

- 100% of allow-path assessed responses have audit snapshot; missing audit = gate fail.

## Security / privacy

Retention follow synthetic policy; no live credentials.

## Operational impact

Export via evidence-export script; monitor snapshot write failures.

## Validation

- AC-003, AC-063; spot-check PUB runs have audit.

## Revisit triggers

- When production e-records/signatures apply (Part 11/Annex 11 analysis) requiring signed audit — new ADR; or snapshot write failure rate > **1%** over a week.
