# task-025 — BLOCKED: Fuzzy duplicate matching

| Field | Entry |
|---|---|
| Task ID | task-025 |
| Status | blocked |
| Depends on | AMB-PV-01 open |
| FR / area | FR-004 |
| Maps AC / NFR | BR-033 threshold — open-blocked |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Do not implement fuzzy duplicate matching until a numeric threshold and golden set exist (ADR-007).

## 2. Specs to load

- submission/specs/testing/matching_thresholds.md
- submission/specs/testing/ambiguity_closure.md (AMB-PV-01)
- submission/specs/architecture/ADR-007-duplicate-matching-fail-closed.md
- submission/specs/features/matching_confidence_checklist.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Any fuzzy implementation or guessed threshold (e.g. 0.8).

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Leave status blocked; no code
- [ ] Revisit only when matching_thresholds.md gains numeric fuzzy threshold + golden set ≥50
- [ ] Do not hand this task to a coding agent

## 5. Acceptance checks

Proves: **BR-033 threshold — open-blocked** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains blocked unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
