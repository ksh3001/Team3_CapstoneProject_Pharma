# GxP Lifecycle Validation

> Team3 Phase 3 artefact (template 13). Alignment: Prompt 08 / DoD lifecycle framing — **not** a claim of validated GxP DSS.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Quality / Architecture |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | GxP; Evaluation |
| Status | Phase 3 — provisional (hypothesis) |
| Related | CSA (14); QRM (15); PHASE3_CHECKPOINT |

## Purpose

Map assessed POC activities to a GAMP-style lifecycle **lens** without asserting production CSV completion.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-GxP-01 | DoD / scoring hard gates | Fail-closed assist boundary |
| E-GxP-02 | AC suite + phase3 tests | Verification evidence for POC |
| E-GxP-03 | Phase 1–2 artefacts | URS/risk context incomplete (hypothesis) |

## 1. Intended use (URS lens)

Assist Quality/PV/Supply with evidence assembly and options under fail-closed AuthZ. **Out of intended use:** disposition, final PV, allocate/ship/recall, quality-status change.

## 2. Spec / design / build stages (POC)

| Stage | Artefact | Status |
|---|---|---|
| URS / FR | Phase 1 + Prompt 05 | Partial — P0 baselines Missing |
| Design | C4 + ADRs + contracts | Phase 3 |
| Build | `submission/src/` | POC complete |
| Verification | pytest AC + phase3 | Green |
| Validation (prod) | IQ/OQ/PQ / change control | **Not claimed** |

## 3. Risk-based approach

See QRM (15). High-risk functions are **blocked by design** rather than mitigated by monitoring alone.

## 4. Data integrity (ALCOA+)

Evidence items require authority, effective_at, integrity hash, source_preserved; dual-cite on conflict; audit snapshots (ADR-010).

## 5. Continuity / AI-disabled

Deterministic offline and AI-disabled paths required (ADR-001/002); LLM off by default.

## 6. Change control (POC)

Contract version bumps require Evaluation approval; structural reopen triggers in ADR register.

## Risks, assumptions and unresolved gaps

| ID | Description | Status |
|---|---|---|
| R-GxP-01 | No validated system claim | Accepted |
| R-GxP-02 | AC-052 continuity drill deferred | Open Phase 7 |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Lifecycle lens documented | This file | Pass |
| No production validation claim | §2 | Pass |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Team3 Quality | Owner | 2026-08-07 |
