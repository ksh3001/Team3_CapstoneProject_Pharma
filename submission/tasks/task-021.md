# task-021 — Evidence audit store snapshots

| Field | Entry |
|---|---|
| Task ID | task-021 |
| Status | ready |
| Depends on | 012,015,016,017 |
| FR / area | FR-001/003/004/005 |
| Maps AC / NFR | AC-003; NFR-11; ADR-006/010 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Persist decision/audit snapshots under submission working store for packs and authz checks.

## 2. Specs to load

- submission/specs/architecture/ADR-006-local-evidence-audit-store.md
- submission/specs/architecture/ADR-010-decision-audit-snapshot.md
- submission/specs/testing/nfrs.md (NFR-11)
- submission/specs/data/data_model.md
- submission/specs/api/module_rules.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Writing into challenge data/; omitting purpose/user.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Persist authz + workflow audit snapshots under submission/
- [ ] Include user, purpose, as_of, decision, citations as required
- [ ] Tests for NFR-11 completeness on happy/deny paths

## 5. Acceptance checks

Proves: **AC-003; NFR-11; ADR-006/010** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
