# task-014 — Implement read-only Evidence ACL adapters

| Field | Entry |
|---|---|
| Task ID | task-014 |
| Status | ready |
| Depends on | 002,003 |
| FR / area | FR-002/003 shared |
| Maps AC / NFR | BR-024; ADR-008; NFR challenge read-only |
| Prompt | prompts/10_implementation_tasks.md |

## 1. Goal

Implement evidence/ ACL adapters that read package CSVs/knowledge without writes and preserve units/times/authority fields.

## 2. Specs to load

- submission/specs/architecture/ADR-008-per-source-acl-adapters.md
- submission/specs/data/data_model.md
- submission/specs/api/module_rules.md
- submission/specs/architecture/boundary_and_degraded_mode.md

- submission/specs/api/module_rules.md
- submission/artefacts/prompts/09_lean_dmaic/build_constraints_from_lean.md
- submission/artefacts/prompts/09_lean_dmaic/structural_reopen.md (gate cleared)

## 3. Out of scope for this task

Silent unit conversion; write-back to data/.

- Any Prompt 11 mega-build beyond this unit
- Changing challenge evidence under data/, knowledge/, case/

## 4. Implementation steps

- [ ] Implement read adapters for required CSVs/knowledge catalog
- [ ] Preserve verbatim units/times/authority; no writes to challenge paths
- [ ] Unit tests: read OK; write attempt guarded/fails

## 5. Acceptance checks

Proves: **BR-024; ADR-008; NFR challenge read-only** (see submission/specs/features/acceptance_criteria_register.md and submission/specs/testing/ac_test_plan.md).

## 6. Test expectations

- If this is a **failing-test** task (005–011): tests must fail on empty/stub impl, then pass after the paired implement task.
- If this is an **implement** task: update/keep tests green for listed ACs only.
- If **blocked** (025): no tests that encode a guessed fuzzy threshold.

## 7. Done when

- [ ] Checklist in §4 complete
- [ ] Status remains ready unless explicitly unblocked by ADR/threshold update
- [ ] No out-of-scope behavior introduced
- [ ] Specs cited above were the only material inputs used
