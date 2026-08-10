# C4 Architecture

> Team3 Phase 3 artefact (template 10). Canonical detail: `artefacts/prompts/06_c4/`.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Architecture |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Security; GxP |
| Status | Phase 3 — provisional (matches Prompt 06) |
| Related | ADR-001…010; BC map Phase 2 |

## Purpose

Record system context, containers, components, and prohibited edges for the assessed POC.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-C4-01 | `artefacts/prompts/06_c4/*` | Full C4 set |
| E-C4-02 | `submission/src/` | Implemented runtime shape |
| E-C4-03 | architecture_review.md | conditional |

## 1. System context

Persons: Quality/QP support, PV intake, Supply planner. External: SoR extracts (read), human decision contexts (QP/Safety/Supply Board), optional LLM (off). AEGIS assists; does not certify/finalize/allocate.

## 2. Container view

| Container | Role |
|---|---|
| Workflow Runtime (CLI/API) | AuthZ → ACL → workflows → validate |
| Rules & Gate Engine | POL-* / evaluate |
| Evidence & Audit Store | Local `submission/working/` |
| Read Connectors + ACL | Challenge data read-only |
| Model Adapter | No-op default |
| Demo UI | Optional thin; CLI sufficient for POC |
| Execution adapters | **Not deployed** (PROHIBITED) |

## 3. Component view

AuthZ service; document applicability; batch/pv/supply workflows; SideEffectGuard; mode controller; metrics; evaluate runner; schema validators.

## 4. Code view

Layout per `module_rules.md`: `authz/`, `evidence/`, `docs/`, `workflows/`, `contracts/`, `runtime/`, `ports/`, `evaluate/`.

## 5. Trust & degraded mode

IAM>cache; doc quarantine; deterministic_offline / ai_disabled; LLM never on assessed path. See `boundary_and_degraded_mode.md`.

## 6. Mapping to requirements

FR-001…007 → containers above; AC hard gates → Rules & Evaluate.

## 7. Open architecture choices

Demo UI tech (C09) residual; production IAM/HTTP hardening deferred Phase 4–7.

## Risks, assumptions and unresolved gaps

| ID | Description | Status |
|---|---|---|
| R-C4-01 | Review conditional under hypothesis | Accepted |
| R-C4-02 | No write plane — pressure may return | Blocker if requested |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| No exec write container | C4 + ADR-003 + tests | Pass |
| Matches DDD BCs | Phase 2 context map | Pass |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Team3 Architecture | Owner | 2026-08-07 |
