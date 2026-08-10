# AC → Test Plan

| Field | Entry |
|---|---|
| Prompt | `prompts/10_implementation_tasks.md` |
| Source ACs | `submission/specs/features/acceptance_criteria_register.md` |
| Mirror | `submission/specs/testing/ac_test_plan.md` |

Every in-scope AC has a test task, or an explicit deferral with risk.

| AC ID | Test task ID(s) | Implement task | Test type | Status |
|---|---|---|---|---|
| AC-001 | task-005 | task-012 | unit / integration (fixture contractor_77) | planned |
| AC-002 | task-005 | task-012 | unit / integration | planned |
| AC-003 | task-005 | task-012, task-021 | unit + audit persistence | planned |
| AC-010 | task-006 | task-013 | unit (K-998/K-999) | planned |
| AC-011 | task-006 | task-013 | unit (K-006/K-007) | planned |
| AC-012 | task-006 | task-013 | unit (K-026) | planned |
| AC-020 | task-007 | task-015 | unit / integration (LR-88) | planned |
| AC-021 | task-007 | task-015 | contract / unit | planned |
| AC-022 | task-007 | task-015 | unit | planned |
| AC-023 | task-007 | task-015 | negative contract | planned |
| AC-030 | task-008 | task-016 | negative schema / unit | planned |
| AC-031 | task-008 | task-016 | unit (no fuzzy auto-merge) | planned |
| AC-032 | task-008 | task-016 | unit (dual clocks) | planned |
| AC-033 | task-008 | task-016 | unit (K-999) | planned |
| AC-040 | task-009 | task-017 | unit (quarantine inventory) | planned |
| AC-041 | task-009 | task-017 | contract / unit | planned |
| AC-042 | task-009 | task-017 | unit (no reservation) | planned |
| AC-043 | task-009 | task-017 | negative contract | planned |
| AC-050 | task-010 | task-018 | unit / integration (model down) | planned |
| AC-051 | task-010 | task-018 | unit (AI-disabled narrator refuse) | planned |
| AC-052 | task-024 (scaffold) | Phase 7 drill execution | checklist / e2e drill | **deferred** — scaffold in pilot; full pass evidence residual until runbooks (AMB-CONT-01). Risk: continuity claim incomplete until drill. |
| AC-060 | task-011 | task-019 | integration / evaluate suite | planned |
| AC-061 | task-011 | task-019 | integration / evaluate suite | planned |
| AC-062 | task-011 | task-019 | integration / evaluate suite | planned |
| AC-063 | task-011 | task-019, task-022 | unit (result shape) | planned |

**Blocked (not an AC enablement):** fuzzy threshold tests that would encode a guessed number — forbidden until task-025 unblocked.
