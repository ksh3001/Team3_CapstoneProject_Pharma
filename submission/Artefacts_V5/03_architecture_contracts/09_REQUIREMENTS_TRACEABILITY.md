# Requirements and Traceability

> Team3 Phase 3 artefact (template 09).

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Evaluation / Architecture |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Product; GxP |
| Status | Phase 3 complete — provisional |
| Related | FR-001…007; AC register; ADRs; RUB-05,07,09 |

## Purpose

Trace material requirements from business/hard gates through features, contracts, tests, and controls so nothing critical is untested. Completion: RTM covering ACs + hard gates.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-RT-01 | `artefacts/prompts/05_features/acceptance_criteria_register.md` | AC-001…063 |
| E-RT-02 | `artefacts/prompts/05_features/feature_index.md` | FR-001…007 |
| E-RT-03 | `DEFINITION_OF_DONE.md` §2–4 | Hard fail-closed properties |
| E-RT-04 | `submission/tests/` | AC + Phase 3 prohibited suites |
| E-RT-05 | `submission/src/contracts/` | Versioned schemas 1.0.0-poc |

## 1. Stakeholder and business requirements

| Req ID | Statement | Source |
|---|---|---|
| BRQ-01 | −14% release lead time context; no Quality-authority change | BR-01 |
| BRQ-02 | Assist only; humans retain certification/reportability/allocation | decision_rights |
| BRQ-03 | Offline + AI-disabled continuity | continuity_requirements |
| BRQ-04 | Honest TCO incl. review hours | cost_model gap |

## 2. Functional requirements

| FR | Name | Primary ACs |
|---|---|---|
| FR-001 | Purpose-bound AuthZ | AC-001–003 |
| FR-002 | Document applicability | AC-010–012 |
| FR-003 | Batch evidence pack | AC-020–023 |
| FR-004 | PV intake | AC-030–033 |
| FR-005 | Supply options | AC-040–043 |
| FR-006 | Continuity modes | AC-050–052 |
| FR-007 | Evaluate / Measure | AC-060–063 |

## 3. Non-functional / control requirements

| ID | Requirement | NFR / gate |
|---|---|---|
| NFRQ-01 | LLM calls = 0 assessed | NFR-01 |
| NFRQ-02 | Side effects = 0 | NFR-02 |
| NFRQ-03 | Schema additionalProperties false | NFR-04/05 |
| NFRQ-04 | Challenge tree immutable | NFR-12 |

## 4. Requirements → design → test → control (RTM)

| Req / AC | Design artefact | Test | Control |
|---|---|---|---|
| AC-001 | ADR-004; AuthZ service | `test_ac_authz` / `test_phase3_prohibited` | IAM>cache |
| AC-010 | BC-DOCAPPLY; FR-002 | `test_ac_documents` / malicious file assert | Quarantine |
| AC-020 | ADR-008; batch workflow | `test_ac_batch` / phase3 unit | Dual-cite |
| AC-023 | batch schema + validator | `test_phase3_prohibited` | 422 disposition |
| AC-030 | pv schema | `test_ac_pv` / phase3 finals | No finals |
| AC-031 | ADR-007 | `test_ac_pv` / phase3 merge | No auto-merge |
| AC-040–043 | ADR-003; SideEffectGuard | `test_ac_supply` / phase3 reservation | no_side_effects |
| AC-050–051 | ADR-001/002 | `test_ac_continuity` | Mode controller |
| AC-052 | Continuity stub | deferred drill | Phase 7 |
| AC-060–063 | Evaluate runner | `test_ac_evaluate` | Hard gates |
| Poisoned tool manifest | Integration contracts | `test_phase3_prohibited` | Not loaded |
| BRQ-02 hard gates | DoD §2 | phase3 + AC suite | Fail closed |

Machine-readable companion: [`rtm_matrix.csv`](rtm_matrix.csv).

## 5–7. Coverage, gaps, change control

| Gap | Handling |
|---|---|
| AC-052 full drill | Deferred Phase 7 |
| Full 12 TEVV suites | Phase 6 |
| Purpose↔role matrix thin | Residual D-A01 |

Changes to RTM require Evaluation + Architecture approval; do not weaken schema `additionalProperties`.

## Risks, assumptions and unresolved gaps

| ID | Description | Status |
|---|---|---|
| R-RT-01 | AC-052 inconclusive | Open |
| R-RT-02 | Hypothesis framing — cycle-time not traced to measured baseline | Open |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Material ACs mapped to tests | §4 + pytest | Pass (except AC-052 deferred) |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Team3 Evaluation | Owner | 2026-08-07 |
