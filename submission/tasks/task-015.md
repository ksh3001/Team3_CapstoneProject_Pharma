# task-015 — Implement batch evidence workflow (FR-003)

| Field | Entry |
|---|---|
| Task ID | task-015 |
| Status | ready |
| Depends on | 007,012,013,014 |
| FR / area | FR-003 |
| Maps AC / NFR | AC-020, AC-021, AC-022, AC-023 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Implement batch_evidence pack: cite/flag/abstain, readiness enum, dual-cite conflicts, reject disposition shapes.

## 2. Specs to load

- submission/specs/features/FR-003-batch-evidence-pack.md
- submission/specs/api/api_contracts.md (§ batch_evidence)
- submission/specs/data/state_transitions.md
- submission/specs/data/data_model.md
- submission/specs/architecture/ADR-003-no-write-adapters-assessed.md
- submission/specs/architecture/ADR-008-per-source-acl-adapters.md
- submission/specs/api/module_rules.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Batch disposition; release certification.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Implement workflows/batch.py per api_contracts
- [ ] AuthZ first; docs filter; ACL fetch; validate response
- [ ] Make task-007 tests pass

## 5. Acceptance checks

Proves: **AC-020, AC-021, AC-022, AC-023** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
