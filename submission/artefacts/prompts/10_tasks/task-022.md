# task-022 — Emit measure metrics on workflow completion

| Field | Entry |
|---|---|
| Task ID | task-022 |
| Status | ready |
| Depends on | 004,015,016,017,019 |
| FR / area | FR-007 |
| Maps AC / NFR | M-01–M-05, M-08; AC-063 support |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Wire metrics collector to emit latency, conflict counts, side-effect=0, authz completeness, and evaluate artifacts per run.

## 2. Specs to load

- submission/artefacts/prompts/09_lean_dmaic/dmaic_plan.md (§2–4)
- submission/specs/features/FR-007-evaluation-gates-measure.md
- submission/specs/testing/nfrs.md
- submission/specs/testing/ac_test_plan.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Inventing board -14% baseline numbers.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] On each workflow/evaluate completion, emit metrics JSON
- [ ] Include side_effect_count=0 assertion hook for supply
- [ ] Document how to read median/p95 from fixture runs

## 5. Acceptance checks

Proves: **M-01–M-05, M-08; AC-063 support** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
