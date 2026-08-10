# task-004 — Measure metrics collector stubs (M-01–M-05, M-08)

| Field | Entry |
|---|---|
| Task ID | task-004 |
| Status | ready |
| Depends on | 001 |
| FR / area | FR-007 |
| Maps AC / NFR | Measure-first M-01–M-05, M-08 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Add metrics collector stubs for pack latency, conflict counts, side-effect counter, authz audit completeness, evaluate results, p95 latency hooks.

## 2. Specs to load

- submission/specs/features/FR-007-evaluation-gates-measure.md
- submission/artefacts/prompts/09_lean_dmaic/dmaic_plan.md (§2 Measure)
- submission/specs/testing/nfrs.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Flipping gate outcomes; mutating packs.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Create metrics module with counters/timers interfaces
- [ ] Stub emit methods for M-01–M-05, M-08
- [ ] Persist metrics under submission/ working path only
- [ ] Smoke test stub writes a JSON line

## 5. Acceptance checks

Proves: **Measure-first M-01–M-05, M-08** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
