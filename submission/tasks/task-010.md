# task-010 — Failing tests: Continuity AC-050–051

| Field | Entry |
|---|---|
| Task ID | task-010 |
| Status | ready |
| Depends on | 001,002 |
| FR / area | FR-006 |
| Maps AC / NFR | AC-050, AC-051 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Write failing tests that model-down uses deterministic path and AI-disabled refuses narrator while rules remain.

## 2. Specs to load

- submission/specs/features/FR-006-offline-ai-disabled-continuity.md
- submission/specs/architecture/ADR-001-deterministic-offline-default.md
- submission/specs/architecture/ADR-002-llm-optional-off-default.md
- submission/specs/architecture/boundary_and_degraded_mode.md
- submission/specs/testing/ac_test_plan.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Full 14-day org continuity drill evidence (AC-052 deferred).

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Simulate model down → deterministic path, not hang
- [ ] AI-disabled → narrator refused; rules path remains
- [ ] Confirm fail before task-018

## 5. Acceptance checks

Proves: **AC-050, AC-051** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
