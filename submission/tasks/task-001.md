# task-001 — Scaffold submission/src layout and mode defaults

| Field | Entry |
|---|---|
| Task ID | task-001 |
| Status | ready |
| Depends on | — |
| FR / area | foundation |
| Maps AC / NFR | NFR-01, NFR-09 (prep) |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Create package layout under submission/src matching module_rules with LLM off and deterministic_offline default.

## 2. Specs to load

- submission/specs/api/module_rules.md
- submission/specs/architecture/c4_code.md
- submission/specs/architecture/ADR-001-deterministic-offline-default.md
- submission/specs/architecture/ADR-002-llm-optional-off-default.md
- submission/specs/api/deployment_notes.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Business logic; HTTP handlers; reading challenge data for decisions.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Create submission/src/{authz,evidence,workflows,contracts,runtime,ports,evaluate}/ and submission/tests/, submission/scripts/
- [ ] Add mode config defaults: deterministic_offline, llm_enabled=false
- [ ] Add package __init__.py files / pyproject or path bootstrap as needed
- [ ] Document entrypoint stub only (no feature logic)

## 5. Acceptance checks

Proves: **NFR-01, NFR-09 (prep)** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
