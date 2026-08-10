# task-012 — Implement purpose-bound AuthZ (FR-001)

| Field | Entry |
|---|---|
| Task ID | task-012 |
| Status | ready |
| Depends on | 005 |
| FR / area | FR-001 |
| Maps AC / NFR | AC-001, AC-002, AC-003 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Implement AuthorizationPort/check so IAM revoke beats cache and every decision is audited.

## 2. Specs to load

- submission/specs/features/FR-001-purpose-bound-authorization.md
- submission/specs/api/api_contracts.md (§ authz/check)
- submission/specs/architecture/ADR-004-iam-over-cache.md
- submission/specs/architecture/ADR-010-decision-audit-snapshot.md
- submission/specs/api/module_rules.md
- submission/specs/data/data_model.md (AuthorizationDecision)

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Caching allow without IAM; public OAuth.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Implement authz service reading IAM entitlements over cache
- [ ] Expose check function used by workflows
- [ ] Write audit decision record
- [ ] Make task-005 tests pass; no extras

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
