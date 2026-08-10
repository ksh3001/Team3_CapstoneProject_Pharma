# task-005 — Failing tests: AuthZ AC-001–003

| Field | Entry |
|---|---|
| Task ID | task-005 |
| Status | ready |
| Depends on | 001,002,003 |
| FR / area | FR-001 |
| Maps AC / NFR | AC-001, AC-002, AC-003 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Write failing tests for revoke+cache deny, entitled allow, and audit fields before AuthZ implementation.

## 2. Specs to load

- submission/specs/features/FR-001-purpose-bound-authorization.md
- submission/specs/features/acceptance_criteria_register.md
- submission/specs/architecture/ADR-004-iam-over-cache.md
- submission/specs/api/api_contracts.md (§ authz/check)
- submission/specs/testing/ac_test_plan.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Implementing AuthZ to make tests pass in this task.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Add tests using contractor_77 revoke+cache fixture → expect deny
- [ ] Add tests for entitled user + purpose → allow
- [ ] Assert audit fields user/purpose/checked_at/decision
- [ ] Confirm tests fail before task-012

## 5. Acceptance checks

Proves: **AC-001, AC-002, AC-003** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
