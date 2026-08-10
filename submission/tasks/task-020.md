# task-020 — Wire thin CLI/HTTP, health, idempotency

| Field | Entry |
|---|---|
| Task ID | task-020 |
| Status | ready |
| Depends on | 012,015,016,017,018,019 |
| FR / area | all FR endpoints |
| Maps AC / NFR | NFR-09; Idempotency; api_contracts |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Expose thin adapters for authz/workflows/evaluate/health with Idempotency-Key behavior and no business logic in routers.

## 2. Specs to load

- submission/specs/api/api_contracts.md
- submission/specs/api/error_and_security.md
- submission/specs/api/deployment_notes.md
- submission/specs/api/module_rules.md
- submission/specs/architecture/c4_containers.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Business invariants in routers; reverse proxy/prod IAM.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Thin CLI and/or local HTTP 127.0.0.1 only
- [ ] Health returns llm_enabled=false
- [ ] Idempotency-Key replay/409 behavior on POSTs
- [ ] Routers call runtime only

## 5. Acceptance checks

Proves: **NFR-09; Idempotency; api_contracts** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
