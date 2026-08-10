# Traceability Gap Audit

Every row: **fixed now** | **assumed** (revisit) | **open-blocked**.

## 1. FR without AC

| Item | Status |
|---|---|
| FR-001–007 | **fixed now** — each has ACs in register |

## 2. BR without verifying AC / threshold

| Item | Status |
|---|---|
| BR-001–003 | fixed — AC-001–003 |
| BR-010–013 | fixed — AC-010–012 |
| BR-020–025 | fixed — AC-020–023 |
| BR-030–034 | fixed — AC-030–033; BR-033 threshold → matching_thresholds |
| BR-040–043 | fixed — AC-040–043 |
| BR-050–052 | fixed — AC-050–052 |
| BR-060–062 | fixed — AC-060–063 |

## 3. AC without endpoint/contract

| Item | Status |
|---|---|
| AC-001–003 | fixed — /v1/authz/check + workflow 403 |
| AC-010–012 | fixed — enforced inside workflow contracts via applicable_documents |
| AC-020–023 | fixed — batch_evidence |
| AC-030–033 | fixed — pv_intake |
| AC-040–043 | fixed — supply_options |
| AC-050–052 | fixed — mode + health + continuity evaluate suite |
| AC-060–063 | fixed — /v1/evaluate/run |

## 4. Endpoint without FR

| Item | Status |
|---|---|
| /v1/authz/check | FR-001 |
| /v1/workflows/* | FR-003–005 |
| /v1/evaluate/run | FR-007 |
| /v1/health | supporting NFR-09 (no FR) — **assumed** ops endpoint OK |

## 5. Matching/confidence without number

| Item | Status |
|---|---|
| Exact / strong_key | **fixed now** — equality rules |
| Fuzzy threshold | **open-blocked** — no fuzzy implementation tasks until number (ADR-007) |
| Multilingual confidence | **assumed** — always HITL flag for non-English (AMB-PV-02) |

## 6. Error/security without AC or NFR

| Item | Status |
|---|---|
| authz_denied | AC-001 / NFR-03 |
| contract_violation | AC-023/043 / NFR-04/05 |
| side_effect_blocked | AC-042 / NFR-02 |
| mode_violation | AC-051 / NFR-01 |
| error envelope / no stack leaks | NFR check in evaluate suite — **assumed** AC-SEC-01 = evaluate asserts envelope shape |

**Unmarked orphans:** none.
