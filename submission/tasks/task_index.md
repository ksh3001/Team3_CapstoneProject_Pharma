# Prompt 10 — Task Index / Execution Order

| Field | Entry |
|---|---|
| Prompt | `prompts/10_implementation_tasks.md` |
| Skills | `spec-driven-delivery` |
| Entry gates | Architecture review `conditional`; Prompt 09 `structural_reopen` **cleared** |
| Narrative class | `hypothesis` — Measure-first ordering |
| Code in this prompt | **None** |

**Mirror:** `submission/tasks/` (same files).  
**AC plan:** `ac_test_plan.md` → `submission/specs/testing/ac_test_plan.md`.

---

## Priority legend

1. Assumption / control tests (failing first)  
2. Foundation + Measure stubs  
3. Feature implement (dependency order)  
4. Wire / audit / metrics emit  
5. Fix-in-pilot stubs  
6. Blocked (do not hand to agent)

---

## Ordered tasks

| Order | Task | Title | Status | Depends | FR |
|---:|---|---|---|---|---|
| 1 | task-001 | Scaffold src layout + mode defaults | ready | — | foundation |
| 2 | task-002 | Error envelope + request context | ready | 001 | foundation |
| 3 | task-003 | Contract schema validators | ready | 001 | foundation |
| 4 | task-004 | Measure metrics collector stubs | ready | 001 | FR-007 |
| 5 | task-005 | Failing tests: AuthZ AC-001–003 | ready | 001–003 | FR-001 |
| 6 | task-006 | Failing tests: Documents AC-010–012 | ready | 001–003 | FR-002 |
| 7 | task-007 | Failing tests: Batch AC-020–023 | ready | 001–003 | FR-003 |
| 8 | task-008 | Failing tests: PV AC-030–033 | ready | 001–003 | FR-004 |
| 9 | task-009 | Failing tests: Supply AC-040–043 | ready | 001–003 | FR-005 |
| 10 | task-010 | Failing tests: Continuity AC-050–051 | ready | 001–002 | FR-006 |
| 11 | task-011 | Failing tests: Evaluate AC-060–063 | ready | 001–003 | FR-007 |
| 12 | task-012 | Implement AuthZ FR-001 | ready | 005 | FR-001 |
| 13 | task-013 | Implement document applicability FR-002 | ready | 006, 012 | FR-002 |
| 14 | task-014 | Read-only Evidence ACL adapters | ready | 002, 003 | shared |
| 15 | task-015 | Implement batch evidence FR-003 | ready | 007, 012–014 | FR-003 |
| 16 | task-016 | Implement PV intake (exact/strong_key) FR-004 | ready | 008, 012–014 | FR-004 |
| 17 | task-017 | Implement supply + SideEffectGuard FR-005 | ready | 009, 012–014 | FR-005 |
| 18 | task-018 | Mode controller + AI-disabled FR-006 | ready | 010, 001 | FR-006 |
| 19 | task-019 | Evaluation gate runner FR-007 | ready | 011, 015–017 | FR-007 |
| 20 | task-020 | Thin CLI/HTTP + health + idempotency | ready | 012, 015–019 | endpoints |
| 21 | task-021 | Evidence audit store snapshots | ready | 012, 015–017 | ADR-006/010 |
| 22 | task-022 | Emit measure metrics on completion | ready | 004, 015–019 | FR-007 |
| 23 | task-023 | Review-hour log template (M-06) | ready | 001 | Measure |
| 24 | task-024 | Continuity drill checklist stub | ready | 018 | FR-006 |
| 25 | task-025 | Fuzzy duplicate matching | **blocked** | AMB-PV-01 | FR-004 |

**Parallelism (safe):** 002∥003∥004 after 001; 005–011 after foundation; 014∥012 after foundation; 015∥016∥017 after 012–014 + their tests; 023 anytime after 001.

---

## Traceability (task → FR → AC → contract)

| Task | FR | ACs | Contract / endpoint |
|---|---|---|---|
| 005, 012 | FR-001 | AC-001–003 | POST /v1/authz/check |
| 006, 013 | FR-002 | AC-010–012 | applicable_documents (workflow-internal) |
| 007, 015 | FR-003 | AC-020–023 | POST /v1/workflows/batch_evidence |
| 008, 016 | FR-004 | AC-030–033 | POST /v1/workflows/pv_intake |
| 009, 017 | FR-005 | AC-040–043 | POST /v1/workflows/supply_options |
| 010, 018, 024 | FR-006 | AC-050–052 | mode + health; continuity |
| 004, 011, 019, 022 | FR-007 | AC-060–063 + Measure | POST /v1/evaluate/run |
| 020 | all | NFR-09 + idempotency | health + all POSTs |
| 021 | cross | AC-003, NFR-11 | audit store |
| 025 | FR-004 | BR-033 | **blocked** — no contract enablement |

Source matrix: `submission/specs/testing/traceability_matrix.md`.

---

## Conditional architecture items → tasks / residual

| Open issue (Prompt 07) | Handling |
|---|---|
| Missing cycle-time / review-hour baselines | task-004, 022, 023 (Measure); residual hypothesis |
| AMB-PV-01 fuzzy | task-025 **blocked** |
| AI-EVIDENCE triple-state | residual — no validated-DSS claim in tasks |
| CRLF verify FAIL | residual A-001 — no task rewrites challenge files |
| Write-plane demand | **not tasked**; would reopen 06–08 |
| Demo UI (C09) | residual; task-020 allows CLI-only |

---

## Out of scope (do not create tasks)

- Autonomous disposition / final PV / allocate-ship-recall  
- Mandatory genAI / RAG / narrator assessed default  
- MDM enterprise programme as product code  
- Guessed fuzzy threshold  
- Challenge evidence mutation  

---

## Handoff to Prompt 11

Execute **ready** tasks in order (or safe parallelism). Do not start task-025. Re-check structural reopen if any task needs write plane or LLM-on-assessed.
