# task-008 — Failing tests: PV intake AC-030–033

| Field | Entry |
|---|---|
| Task ID | task-008 |
| Status | ready |
| Depends on | 001,002,003 |
| FR / area | FR-004 |
| Maps AC / NFR | AC-030, AC-031, AC-032, AC-033 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Write failing tests for no final PV fields, no below-threshold auto-merge, dual-cite clocks, and K-999 not reportability authority.

## 2. Specs to load

- submission/specs/features/FR-004-pv-intake-packet.md
- submission/specs/features/matching_confidence_checklist.md
- submission/specs/testing/matching_thresholds.md
- submission/specs/architecture/ADR-007-duplicate-matching-fail-closed.md
- submission/specs/architecture/ADR-009-multi-clock-evidence.md
- submission/specs/testing/ac_test_plan.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Fuzzy matching implementation; implementing PV workflow here.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Assert response cannot include final PV conclusion fields
- [ ] Assert no auto-merge without exact/strong_key
- [ ] Assert disagreeing clocks both cited + review required
- [ ] Assert K-999 not used as reportability authority
- [ ] Confirm fail before task-016

## 5. Acceptance checks

Proves: **AC-030, AC-031, AC-032, AC-033** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
