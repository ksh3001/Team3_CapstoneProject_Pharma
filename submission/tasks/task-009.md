# task-009 — Failing tests: Supply options AC-040–043

| Field | Entry |
|---|---|
| Task ID | task-009 |
| Status | ready |
| Depends on | 001,002,003 |
| FR / area | FR-005 |
| Maps AC / NFR | AC-040, AC-041, AC-042, AC-043 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Write failing tests for quarantine exclusion, no_side_effects, no reservation, and side-effect shape rejection.

## 2. Specs to load

- submission/specs/features/FR-005-supply-option-drafting.md
- submission/specs/architecture/ADR-003-no-write-adapters-assessed.md
- submission/specs/api/api_contracts.md (§ supply_options)
- submission/specs/testing/ac_test_plan.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

WMS writes; implementing supply workflow here.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Quarantine inventory not in available supply
- [ ] no_side_effects true; no execution/reservation fields
- [ ] Side-effect contract shape rejected
- [ ] Confirm fail before task-017

## 5. Acceptance checks

Proves: **AC-040, AC-041, AC-042, AC-043** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
