# task-019 — Implement evaluation gate runner (FR-007)

| Field | Entry |
|---|---|
| Task ID | task-019 |
| Status | ready |
| Depends on | 011,015,016,017 |
| FR / area | FR-007 |
| Maps AC / NFR | AC-060, AC-061, AC-062, AC-063 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Implement /v1/evaluate/run (or CLI) that hard-fails prohibited/side-effect/authz violations and emits machine-readable results.

## 2. Specs to load

- submission/specs/features/FR-007-evaluation-gates-measure.md
- submission/specs/api/api_contracts.md (§ evaluate/run)
- submission/specs/testing/nfrs.md
- submission/specs/architecture/ADR-010-decision-audit-snapshot.md
- submission/specs/api/module_rules.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Mutating packs to pass gates; soft-fail only for hard controls.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Implement evaluate runner suites for hard controls
- [ ] Emit machine-readable results under submission/
- [ ] Make task-011 tests pass; do not mutate packs to pass

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
