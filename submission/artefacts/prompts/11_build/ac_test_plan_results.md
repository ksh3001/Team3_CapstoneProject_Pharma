# AC Test Plan Results (Prompt 11)

Updated from Prompt 10 `ac_test_plan.md`. Suite: `submission/tests` — **25 passed** (2026-08-06).

| AC ID | Test module | Implement path | Status | Risk / notes |
|---|---|---|---|---|
| AC-001 | `test_ac_authz.py` | `authz/service.py` | **pass** | |
| AC-002 | `test_ac_authz.py` | `authz/service.py` | **pass** | |
| AC-003 | `test_ac_authz.py` | authz + `working/audit/` | **pass** | |
| AC-010 | `test_ac_documents.py` | `docs/applicability.py` | **pass** | |
| AC-011 | `test_ac_documents.py` | `docs/applicability.py` | **pass** | |
| AC-012 | `test_ac_documents.py` | `docs/applicability.py` | **pass** | |
| AC-020 | `test_ac_batch.py` | `workflows/batch.py` | **pass** | |
| AC-021 | `test_ac_batch.py` | `workflows/batch.py` | **pass** | |
| AC-022 | `test_ac_batch.py` | `workflows/batch.py` | **pass** | |
| AC-023 | `test_ac_batch.py` | `workflows/batch.py` | **pass** | |
| AC-030 | `test_ac_pv.py` | `workflows/pv.py` | **pass** | |
| AC-031 | `test_ac_pv.py` | `workflows/pv.py` | **pass** | fuzzy disabled |
| AC-032 | `test_ac_pv.py` | `workflows/pv.py` | **pass** | |
| AC-033 | `test_ac_pv.py` | `workflows/pv.py` | **pass** | |
| AC-040 | `test_ac_supply.py` | `workflows/supply.py` | **pass** | |
| AC-041 | `test_ac_supply.py` | `workflows/supply.py` | **pass** | |
| AC-042 | `test_ac_supply.py` | `workflows/supply.py` | **pass** | |
| AC-043 | `test_ac_supply.py` | `workflows/supply.py` | **pass** | |
| AC-050 | `test_ac_continuity.py` | mode + llm port | **pass** | |
| AC-051 | `test_ac_continuity.py` | mode + workflows | **pass** | |
| AC-052 | checklist stub | Phase 7 drill | **deferred** | Scaffold only; full continuity drill not executed |
| AC-060 | `test_ac_evaluate.py` | `evaluate/runner.py` | **pass** | |
| AC-061 | `test_ac_evaluate.py` | `evaluate/runner.py` | **pass** | |
| AC-062 | `test_ac_evaluate.py` | authz + evaluate | **pass** | |
| AC-063 | `test_ac_evaluate.py` | evaluate results shape | **pass** | |

**Blocked (not tested as enabled):** fuzzy threshold (task-025).
