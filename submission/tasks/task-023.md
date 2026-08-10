# task-023 — Review-hour log template (M-06)

| Field | Entry |
|---|---|
| Task ID | task-023 |
| Status | ready |
| Depends on | 001 |
| FR / area | FR-007 Measure |
| Maps AC / NFR | PRD human review TCO; M-06 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Add a review-hour logging template/CSV under submission for TCO using staff_rates.csv rates (hours may be estimated/labeled).

## 2. Specs to load

- submission/artefacts/prompts/09_lean_dmaic/dmaic_plan.md (M-06)
- submission/specs/product/prd.md (§3 human review hours)
- submission/specs/features/FR-007-evaluation-gates-measure.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Claiming measured ops hours without label; FinOps automation.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Add submission/artefacts/ or submission/evidence/ review-hour template
- [ ] Columns for role, hours, rate reference, notes, assumption label
- [ ] Do not invent production hours as measured fact

## 5. Acceptance checks

Proves: **PRD human review TCO; M-06** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
