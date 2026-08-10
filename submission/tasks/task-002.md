# task-002 — Shared error envelope and request context

| Field | Entry |
|---|---|
| Task ID | task-002 |
| Status | ready |
| Depends on | 001 |
| FR / area | foundation |
| Maps AC / NFR | NFR error envelope (Prompt 08) |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Implement standard error JSON helpers and shared request context (user, purpose, as_of, request_id, idempotency_key).

## 2. Specs to load

- submission/specs/api/error_and_security.md
- submission/specs/api/api_contracts.md (common headers / errors)
- submission/specs/api/module_rules.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Workflow business rules; AuthZ policy.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Define error envelope schema helper (code, message, request_id; no stack traces)
- [ ] Define RequestContext dataclass/fields per api_contracts common headers
- [ ] Unit-test envelope shape (no secrets/stacks)

## 5. Acceptance checks

Proves: **NFR error envelope (Prompt 08)** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
