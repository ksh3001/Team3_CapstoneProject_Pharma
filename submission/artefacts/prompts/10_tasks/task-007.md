# task-007 — Failing tests: Batch evidence AC-020–023

| Field | Entry |
|---|---|
| Task ID | task-007 |
| Status | ready |
| Depends on | 001,002,003 |
| FR / area | FR-003 |
| Maps AC / NFR | AC-020, AC-021, AC-022, AC-023 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Write failing tests for LR-88 unit conflict, not_executed, conflicted readiness, and prohibited disposition rejection.

## 2. Specs to load

- submission/specs/features/FR-003-batch-evidence-pack.md
- submission/specs/features/acceptance_criteria_register.md
- submission/specs/api/api_contracts.md (§ batch_evidence)
- submission/specs/data/state_transitions.md
- submission/specs/testing/ac_test_plan.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Implementing batch workflow in this task.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] LR-88-style unit conflict fixture → Conflict recorded
- [ ] Assert execution_status not_executed / no disposition fields
- [ ] Assert material conflict ⇒ not ready_for_authorized_review
- [ ] Assert prohibited disposition payload rejected
- [ ] Confirm fail before task-015

## 5. Acceptance checks

Proves: **AC-020, AC-021, AC-022, AC-023** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
