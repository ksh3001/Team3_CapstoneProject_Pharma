# Traceability Matrix (pre-build)

| Feature / FR | Endpoint(s) / contract | Business rules | Acceptance criteria | ADR(s) | Ambiguity status |
|---|---|---|---|---|---|
| FR-001 AuthZ | POST /v1/authz/check | BR-001–003 | AC-001–003 | ADR-004 | assumed AMB-AUTHZ-01 fail-closed |
| FR-002 Documents | used by batch/pv/supply | BR-010–013 | AC-010–012 | ADR-002/008 | assumed AMB-DOC-01 deny cross-jurisdiction instruction |
| FR-003 Batch | POST /v1/workflows/batch_evidence | BR-020–025 | AC-020–023 | ADR-001,003,008,010 | assumed AMB-BATCH-01 interim block list |
| FR-004 PV | POST /v1/workflows/pv_intake | BR-030–034 | AC-030–033 | ADR-007,009,010 | open-blocked fuzzy (AMB-PV-01); assumed AMB-PV-02 |
| FR-005 Supply | POST /v1/workflows/supply_options | BR-040–043 | AC-040–043 | ADR-003,001,010 | assumed AMB-SUP-01 released-only |
| FR-006 Continuity | mode + health; all workflows | BR-050–052 | AC-050–052 | ADR-001,002 | assumed AMB-CONT-01 runbooks Phase 7 |
| FR-007 Gates | POST /v1/evaluate/run | BR-060–062 | AC-060–063 | ADR-010,003 | assumed AMB-MEAS-01 binary gates first |
| GET /v1/health | health | — | NFR-09 | ADR-001 | resolved |
