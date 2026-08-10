# task-011 — Failing tests: Evaluation gates AC-060–063

| Field | Entry |
|---|---|
| Task ID | task-011 |
| Status | ready |
| Depends on | 001,002,003 |
| FR / area | FR-007 |
| Maps AC / NFR | AC-060, AC-061, AC-062, AC-063 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Write failing tests that prohibited batch, supply side-effect, and authz-bypass packs fail gates with machine-readable results.

## 2. Specs to load

- submission/specs/features/FR-007-evaluation-gates-measure.md
- submission/specs/features/acceptance_criteria_register.md
- submission/specs/api/api_contracts.md (§ evaluate/run)
- submission/specs/testing/ac_test_plan.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Implementing evaluate runner in this task.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Prohibited batch output ⇒ gate fail
- [ ] Supply side-effect output ⇒ gate fail
- [ ] AuthZ deny ⇒ no downstream allow pack
- [ ] Results include suite/id/result machine-readable
- [ ] Confirm fail before task-019

## 5. Acceptance checks

Proves: **AC-060, AC-061, AC-062, AC-063** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
