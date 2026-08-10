# task-024 — Continuity drill checklist stub (AC-052)

| Field | Entry |
|---|---|
| Task ID | task-024 |
| Status | ready |
| Depends on | 018 |
| FR / area | FR-006 |
| Maps AC / NFR | AC-052 (scaffold); defer full drill evidence |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Add continuity drill checklist stub aligned to continuity_requirements.csv; full pass evidence deferred to Phase 7 runbooks.

## 2. Specs to load

- submission/specs/features/FR-006-offline-ai-disabled-continuity.md
- submission/specs/testing/ambiguity_closure.md (AMB-CONT-01)
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md (fix-in-pilot)

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Claiming AC-052 fully satisfied without drill execution.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Add checklist stub mapping continuity_requirements rows
- [ ] Mark AC-052 evidence status: scaffolded / drill pending Phase 7
- [ ] Link from FR-006 / runbooks placeholder

## 5. Acceptance checks

Proves: **AC-052 (scaffold); defer full drill evidence** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
