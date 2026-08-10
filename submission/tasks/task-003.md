# task-003 — Contract schema validators

| Field | Entry |
|---|---|
| Task ID | task-003 |
| Status | ready |
| Depends on | 001 |
| FR / area | foundation |
| Maps AC / NFR | NFR-04/05; BR-061 prep |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Wrap evaluation/contracts schemas with additionalProperties denial and validate workflow response shapes.

## 2. Specs to load

- submission/specs/api/api_contracts.md
- submission/specs/testing/nfrs.md (NFR-04/05)
- evaluation/contracts/ (package schemas — read-only)
- submission/specs/api/module_rules.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Feature implementations; inventing new schema fields.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Load JSON Schemas from evaluation/contracts/ (read-only)
- [ ] Implement validate(payload, schema_name) with additionalProperties false
- [ ] Add tests for reject-unknown-field samples

## 5. Acceptance checks

Proves: **NFR-04/05; BR-061 prep** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
