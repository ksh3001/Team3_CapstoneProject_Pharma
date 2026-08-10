# Architecture Decision Register

> Team3 Phase 3 artefact (template 11). Full ADRs: `artefacts/prompts/07_adrs/ADR-*.md` (**10 ADRs**).

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Architecture |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Security; GxP; Evaluation |
| Status | Phase 3 — index + phase confirmation |
| Related | Prompt 07 decision_index; architecture_review **conditional** |

## Purpose

Register consequential ADRs (≥10) and link them to C4/tests.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-ADR-01 | `artefacts/prompts/07_adrs/decision_index.md` | ADR-001…010 |
| E-ADR-02 | `architecture_review.md` | conditional |
| E-ADR-03 | pytest AC + phase3 suites | Guardrails held |

## 1. ADR index

| ADR | Title | Status | Test / control link |
|---|---|---|---|
| ADR-001 | Deterministic offline default | accepted (POC) | AC-050 |
| ADR-002 | LLM optional off default | proposed | AC-051; NFR-01 |
| ADR-003 | No write adapters assessed | accepted (POC) | AC-041–043 |
| ADR-004 | IAM over cache | accepted (POC) | AC-001 |
| ADR-005 | Single Workflow Runtime POC | proposed | app_api dispatch |
| ADR-006 | Local evidence/audit store | proposed | working/audit |
| ADR-007 | Duplicate matching fail-closed | accepted (POC) | AC-031 |
| ADR-008 | Per-source ACL adapters | proposed | AC-020; forbid_write |
| ADR-009 | Multi-clock evidence | proposed | AC-032 |
| ADR-010 | Decision audit snapshot | proposed | AC-003; NFR-11 |

## 2. Context and forces

Hypothesis framing; hard gates; brownfield conflict; board speed vs Quality authority; offline continuity.

## 3. Decisions and consequences

Sacrificed: always-on genAI, write-plane automation, fuzzy auto-merge, cache-convenient auth. Kept: fail-closed assist.

## 4. Alternatives considered

Per individual ADR files (genAI-first, microservice swarm, WMS writes, fuzzy threshold guesses — rejected).

## 5. Validation

Architecture review conditional; AC suite + `test_phase3_prohibited` green.

## 6. Revisit triggers

Side-effect>0; authz allow on contractor_77; LLM call on assessed path; fuzzy enable without threshold; write-plane request → reopen 06–08.

## 7. Compliance mapping

ADRs support DoD §2–4 and scoring hard gates; not a validated GxP DSS claim.

## Risks, assumptions and unresolved gaps

| ID | Description | Status |
|---|---|---|
| R-ADR-01 | ADR-002/009 blocked on baselines/clock dict | Open |
| R-ADR-02 | Review not elevated to pass | Accepted |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| ≥10 ADRs | Index §1 | Pass |
| Material ADRs tested | §1 test links | Pass |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Team3 Architecture | Owner | 2026-08-07 |
