# task-013 — Implement document applicability (FR-002)

| Field | Entry |
|---|---|
| Task ID | task-013 |
| Status | ready |
| Depends on | 006,012 |
| FR / area | FR-002 |
| Maps AC / NFR | AC-010, AC-011, AC-012 |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Implement Applicable Document filtering with quarantine for untrusted/draft/superseded instruction use.

## 2. Specs to load

- submission/specs/features/FR-002-document-applicability.md
- submission/specs/testing/ambiguity_closure.md (AMB-DOC-*)
- submission/specs/architecture/ADR-008-per-source-acl-adapters.md
- submission/specs/api/module_rules.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

RAG embeddings; treating catalog rows as prompts.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Implement applicability filter (approved vs draft/superseded/untrusted)
- [ ] Quarantine malicious/untrusted instruction docs
- [ ] Make task-006 tests pass

## 5. Acceptance checks

Proves: **AC-010, AC-011, AC-012** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
