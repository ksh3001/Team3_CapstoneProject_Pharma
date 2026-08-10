# Traceability Matrix (updated post-build)

| FR | Endpoint / API | ACs | Task(s) | Code | Tests | Status |
|---|---|---|---|---|---|---|
| FR-001 | POST /v1/authz/check | AC-001–003 | 005,012,021 | `src/authz/service.py` | `test_ac_authz.py` | pass |
| FR-002 | applicable_documents | AC-010–012 | 006,013 | `src/docs/applicability.py` | `test_ac_documents.py` | pass |
| FR-003 | POST /v1/workflows/batch_evidence | AC-020–023 | 007,015 | `src/workflows/batch.py` | `test_ac_batch.py` | pass |
| FR-004 | POST /v1/workflows/pv_intake | AC-030–033 | 008,016 | `src/workflows/pv.py` | `test_ac_pv.py` | pass (fuzzy blocked) |
| FR-005 | POST /v1/workflows/supply_options | AC-040–043 | 009,017 | `src/workflows/supply.py` | `test_ac_supply.py` | pass |
| FR-006 | mode + health | AC-050–051; AC-052 deferred | 010,018,024 | `runtime/mode.py`, `ports/llm.py` | `test_ac_continuity.py` | pass / deferred |
| FR-007 | POST /v1/evaluate/run + metrics | AC-060–063 | 004,011,019,022 | `evaluate/runner.py`, `runtime/metrics.py` | `test_ac_evaluate.py` | pass |
| — | GET /v1/health | NFR-09 | 020 | `src/app_api.py` | `test_ac_continuity.py` | pass |

ADR guardrails respected: ADR-001/002 (LLM off), ADR-003 (no writes), ADR-004 (IAM>cache), ADR-007 (fuzzy off), ADR-008 (ACL reads), ADR-009 (dual clocks), ADR-010 (audit snapshots).
