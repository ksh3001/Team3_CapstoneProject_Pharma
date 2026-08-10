# Spec Ambiguity Closure

Source: `05_features/spec_ambiguities.md` + matching checklist.

| ID | Closure | Value / rule | Revisit |
|---|---|---|---|
| AMB-AUTHZ-01 | **assumed** | Fail closed if object-scope grant unclear | Prompt 10+ if entitlement schema enriched |
| AMB-AUTHZ-02 | **resolved** (POC) | IAM over cache (ADR-004) | production IAM SLA |
| AMB-DOC-01 | **assumed** | local_approved not instructional outside DE unless jurisdiction matches | P0 SoT policy |
| AMB-DOC-02 | **assumed** | Do not fail pack solely on CRLF hash drift; prefer LF-normalize when hashing | A-001 |
| AMB-BATCH-01 | **assumed** | Block `ready_for_authorized_review` if open Conflict on potency unit, sterility/EM material, genealogy break, or QP packet gap signals present in extract | expand checklist when data profiled |
| AMB-BATCH-02 | **assumed** | Dual-cite times when both present (ADR-009) | P1 clock dictionary |
| AMB-PV-01 | **open-blocked** | Fuzzy disabled; no numeric threshold | golden set ≥50 before enable |
| AMB-PV-02 | **assumed** | Non-English narratives ⇒ required_reviews += multilingual_review | define metric later |
| AMB-SUP-01 | **assumed** | Only `quality_status=released` available; quarantine/unknown excluded | if new statuses appear, update data_model |
| AMB-SUP-02 | **assumed** | No hidden weighted optimizer; return constraints + approvals_required | ethics artefact |
| AMB-CONT-01 | **assumed** | Runbook files required by Phase 7; AC-052 evidence then | Phase 7 |
| AMB-MEAS-01 | **assumed** | Binary hard gates first; precision/recall Unknown | Phase 6 |

**Build path:** Tasks for fuzzy matching are **blocked**. All other in-scope FRs may proceed under assumptions above.
