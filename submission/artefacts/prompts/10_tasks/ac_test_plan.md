# AC → Test Plan

| Field | Entry |
|---|---|
| Prompt | `prompts/10_implementation_tasks.md` |
| Source ACs | `submission/specs/features/acceptance_criteria_register.md` |
| Mirror | `submission/specs/testing/ac_test_plan.md` |

Every in-scope AC has a test task, or an explicit deferral with risk.

| AC ID | Test task ID(s) | Implement task | Test type | Status |
|---|---|---|---|---|
| AC-001 | task-005 | task-012 | unit / integration (fixture contractor_77) | **pass** (Prompt 11) |
| AC-002 | task-005 | task-012 | unit / integration | **pass** (Prompt 11) |
| AC-003 | task-005 | task-012, task-021 | unit + audit persistence | **pass** (Prompt 11) |
| AC-010 | task-006 | task-013 | unit (K-998/K-999) | **pass** (Prompt 11) |
| AC-011 | task-006 | task-013 | unit (K-006/K-007) | **pass** (Prompt 11) |
| AC-012 | task-006 | task-013 | unit (K-026) | **pass** (Prompt 11) |
| AC-020 | task-007 | task-015 | unit / integration (LR-88) | **pass** (Prompt 11) |
| AC-021 | task-007 | task-015 | contract / unit | **pass** (Prompt 11) |
| AC-022 | task-007 | task-015 | unit | **pass** (Prompt 11) |
| AC-023 | task-007 | task-015 | negative contract | **pass** (Prompt 11) |
| AC-030 | task-008 | task-016 | negative schema / unit | **pass** (Prompt 11) |
| AC-031 | task-008 | task-016 | unit (no fuzzy auto-merge) | **pass** (Prompt 11) |
| AC-032 | task-008 | task-016 | unit (dual clocks) | **pass** (Prompt 11) |
| AC-033 | task-008 | task-016 | unit (K-999) | **pass** (Prompt 11) |
| AC-040 | task-009 | task-017 | unit (quarantine inventory) | **pass** (Prompt 11) |
| AC-041 | task-009 | task-017 | contract / unit | **pass** (Prompt 11) |
| AC-042 | task-009 | task-017 | unit (no reservation) | **pass** (Prompt 11) |
| AC-043 | task-009 | task-017 | negative contract | **pass** (Prompt 11) |
| AC-050 | task-010 | task-018 | unit / integration (model down) | **pass** (Prompt 11) |
| AC-051 | task-010 | task-018 | unit (AI-disabled narrator refuse) | **pass** (Prompt 11) |
| AC-052 | task-024 (scaffold) | Phase 7 drill execution | checklist / e2e drill | **deferred** — scaffold in pilot; full pass evidence residual until runbooks (AMB-CONT-01). Risk: continuity claim incomplete until drill. |
| AC-060 | task-011 | task-019 | integration / evaluate suite | **pass** (Prompt 11) |
| AC-061 | task-011 | task-019 | integration / evaluate suite | **pass** (Prompt 11) |
| AC-062 | task-011 | task-019 | integration / evaluate suite | **pass** (Prompt 11) |
| AC-063 | task-011 | task-019, task-022 | unit (result shape) | **pass** (Prompt 11) |

See also: `submission/artefacts/prompts/11_build/ac_test_plan_results.md`.

**Blocked (not an AC enablement):** fuzzy threshold tests that would encode a guessed number — forbidden until task-025 unblocked.
