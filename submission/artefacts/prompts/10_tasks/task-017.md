# task-017 — Implement supply options + SideEffectGuard (FR-005)

| Field | Entry |
|---|---|
| Task ID | task-017 |
| Status | ready |
| Depends on | 009,012,013,014 |
| FR / area | FR-005 |
| Maps AC / NFR | AC-040, AC-041, AC-042, AC-043 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Implement supply_options with released-only availability, no_side_effects, and SideEffectGuard fail-closed.

## 2. Specs to load

- submission/specs/features/FR-005-supply-option-drafting.md
- submission/specs/api/api_contracts.md (§ supply_options)
- submission/specs/architecture/ADR-003-no-write-adapters-assessed.md
- submission/specs/api/module_rules.md (§ SideEffectGuard)
- submission/specs/data/data_model.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Reserve/allocate/ship/status/recall execution.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Implement workflows/supply.py + SideEffectGuard
- [ ] released-only availability; options only
- [ ] Make task-009 tests pass

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
