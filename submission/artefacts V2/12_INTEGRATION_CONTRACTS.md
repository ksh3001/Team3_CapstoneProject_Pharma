# Integration Contracts

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `10_C4_ARCHITECTURE.md` §6, ADR-011; `11_ADR_REGISTER.md`; INJ-025, INJ-067, INJ-068, INJ-076, INJ-080 |

## Purpose

Defines versioned input/output contracts, unit/terminology handling, and — critically — idempotency, replay and stale-authorization behaviour against two already-observed failures (a checkpoint-replay duplication and an entitlement-revocation lag) and two already-observed, currently-unblocked security events. Accountable owner: capstone team. Completion criteria: every interface has an explicit idempotency and authorization-freshness rule; the two unblocked security events are converted into named, testable requirements, not left as narrative color.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-1201 | `data/interface_events.csv` | Interface event log, undated | `MES-QMS`: event `timeout`, retry_count = 7, idempotency_key = "missing". `PV-vendor`: event `duplicate_delivery`, retry_count = 3, idempotency_key = `case_vendor_ref` | The `MES-QMS` row is the negative example (7 retries with no idempotency key — every retry is a potential duplicate side effect); `PV-vendor` is the positive contrast (a real idempotency key exists and could dedupe) |
| E-1202 | `data/agent_runs.csv` | Agent run log, undated | Run `AR-77`, workflow `supply_recovery`, checkpoint `cp-4`, state_age_minutes = 380 (6.3 hours), draft_reservations = `DR-1;DR-2`, resume_result = `duplicates_created` | Matches INJ-080 exactly — resuming from a 6.3-hour-old checkpoint produced duplicate draft reservations; this occurred even though Workflow C's reservations are draft-only (no real stock impact), confirming the failure mode is real, not merely theoretical |
| E-1203 | `data/users_entitlements.csv` | Entitlement register, undated | `contractor_77` (role `supplier_quality_viewer`): iam_state = `revoked`, ai_gateway_state = `active_cached`. `qp_eu_1` (role `qualified_person`): iam_state = `active`, ai_gateway_state = `active` | Matches INJ-067 — the AI gateway's cached entitlement for `contractor_77` is stale relative to the authoritative IAM state; `qp_eu_1` is shown as a correctly-synchronized positive control |
| E-1204 | `data/access_cache.csv` | Access cache record, undated | `contractor_77`: cached_until = 2026-08-03T10:00:00Z; revoked_at = 2026-08-01T05:00:00Z | The cache TTL (valid until Aug 3) outlives the actual revocation event (Aug 1) by just over 2 days — a concrete, dated stale-authorization exposure window, not an abstract risk |
| E-1205 | `data/security_events.csv` | Security event log, undated | `SEC-1`: `cross_affiliate_narrative_query`, 48,900 tokens, blocked = **no**. `SEC-2`: `oversized_document_loop`, 980,000 tokens, blocked = **no** | Matches INJ-068 (exfiltration attempt) and INJ-076 (denial-of-wallet) respectively — both attempts are recorded as **not blocked**, i.e., currently-unmitigated, not hypothetical |
| E-1206 | `10_C4_ARCHITECTURE.md` E-1006 | Prior artefact, this team | LIMS result v1 (`unit`/`status`) vs. v2 (`ucum_code`/`lifecycleState`) field rename; ICSR `E2B_R3` variable date precision | Carried forward, not re-derived |

## 1. System/interface inventory

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Which interfaces does this artefact cover? | `MES-QMS` (internal, timeout-prone, E-1201); `PV-vendor` (external, duplicate-delivery-prone, E-1201); `LIMS` result API v1/v2 (E-1206); Safety `E2B_R3` ICSR feed (E-1206); AI Gateway ↔ IAM entitlement sync (E-1203/E-1204). | Capstone team | E-1201, E-1203, E-1206 |

## 2. Versioned input contracts

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| LIMS result input contract | Must declare `api_version` explicitly and route to a version-specific adapter — v1 fields (`unit`, `status`) and v2 fields (`ucum_code`, `lifecycleState`) are not compatible field renames that can share one parser (E-1206, ADR-011). | Capstone team | E-1206 |
| ICSR E2B_R3 input contract | Must accept and preserve a variable date-precision field per record (E-1206) rather than coercing every date to a fixed precision at ingestion. | Capstone team | E-1206 |

## 3. Versioned output contracts

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Are output contracts already defined and tested? | Yes — `evaluation/contracts/{batch_response,pv_response,supply_response}.schema.json`, validated against 6 sample fixtures via `tools/test_contracts.py` (6/6 PASS, re-confirmed this session). | Capstone team | `tools/test_contracts.py` |
| Do these contracts need a version field for future change? | Yes — not currently modeled in the existing schemas (a gap, logged below) — any future schema change (e.g., adding a new evidence-item field) needs a `contract_version` so old and new consumers can be distinguished, consistent with the LIMS v1/v2 lesson (§2). | Capstone team | Gap R-1201 |

## 4. Units and terminology

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| How are unit and terminology conflicts handled at the integration layer? | Cross-referenced, not re-derived: unit conversions must be explicitly approved before use (`05_DDD_CONTEXT_MAP.md` E-405, ADR-004-adjacent); terminology (e.g., MedDRA) must carry its version alongside every coded term (`07_ONTOLOGY_SEMANTIC_LAYER.md` E-604). | Capstone team | `05_DDD_CONTEXT_MAP.md` E-405; `07_ONTOLOGY_SEMANTIC_LAYER.md` E-604 |

## 5. Time and identity semantics

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Can the AI gateway trust its own cached entitlement state? | No — E-1203/E-1204 prove a real, dated case where the cache (`cached_until` 2026-08-03) remained valid for over 2 days after the authoritative IAM revocation (2026-08-01). Every AI gateway call for a non-trivial-risk action must re-check live IAM state, not rely solely on cache TTL, consistent with the workspace rule "check current user, purpose, object, role and tool authorization at execution time." | Capstone team | E-1203, E-1204 |
| What is the maximum acceptable cache staleness? | Not specified in supplied evidence — this artefact does not invent a number; it requires that whatever number is chosen, it must be independently justified and shorter than any observed real-world revocation-to-cache-expiry gap (here, >2 days is already too long). | Capstone team | Gap R-1202 |

## 6. Error/idempotency/replay

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Is every retryable interface idempotent today? | No — `MES-QMS` (E-1201) retries 7 times on timeout with **no** idempotency key, meaning each retry is a potential duplicate write with no way to detect it as a repeat. `PV-vendor` (E-1201) is the correct pattern: an idempotency key (`case_vendor_ref`) exists specifically to catch `duplicate_delivery`. | Capstone team | E-1201 |
| Does checkpoint/resume logic need an age check? | Yes — E-1202 shows a 380-minute-old (6.3 hour) checkpoint resume produced duplicate draft reservations for the exact workflow (`supply_recovery`) this capstone must implement. Resume logic must reject or force re-validation of any checkpoint beyond a defined maximum age, rather than blindly resuming and generating new draft reservations alongside old ones. | Capstone team | E-1202 |
| Does "draft only" (no real stock impact) make E-1202 a non-issue? | No — duplicated draft reservations still corrupt the audit trail and could mislead a human reviewer (e.g., the Supply Governance Board, `03_STAKEHOLDER_DECISION_RIGHTS.md` §2) into believing two independent recommendations exist when they are actually one duplicated state. | Capstone team | E-1202 |
| What idempotency rule follows for this capstone's own build? | Every state-mutating agent action (including draft-only ones) must carry an idempotency key derived from (workflow, checkpoint, logical-action), and every retryable external call must carry one derived from the request's natural key (e.g., `case_vendor_ref`-style), following the E-1201 positive example rather than the E-1201 negative one. | Capstone team | E-1201, E-1202 |

## 7. Compatibility and contract tests

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Are the two unblocked security events (E-1205) covered by any existing test? | No — `tools/test_contracts.py`'s 6 fixtures cover schema compliance and prohibited-action rejection only; neither `cross_affiliate_narrative_query` (SEC-1) nor `oversized_document_loop` (SEC-2) has a corresponding contract-level test today. Both must become named negative-fixture requirements: a purpose-limitation check that rejects cross-affiliate narrative queries outside a case's own affiliate scope, and a per-request token/size cap that rejects oversized-document submission loops before they reach 980K tokens. | Capstone team | E-1205; Gap R-1203 |
| What must a stale-authorization contract test verify? | That a request from a user whose IAM state is `revoked` (E-1203) is rejected by the AI gateway even if the gateway's own cache still shows `active_cached` — i.e., testing the gateway's *behavior*, not just its cache table. Not yet implemented. | Capstone team | E-1203, E-1204; Gap R-1204 |
| What must an idempotency contract test verify? | That resuming `AR-77`-style state beyond a defined max age either refuses to resume or de-duplicates against existing draft reservations, rather than reproducing E-1202's `duplicates_created` outcome. Not yet implemented. | Capstone team | E-1202; Gap R-1205 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1201 | Gap | Existing output contracts (`evaluation/contracts/*.schema.json`) have no `contract_version` field | Medium — future schema changes could break consumers silently | Capstone team | Before any schema change is made | Open |
| R-1202 | Gap | No maximum cache-staleness threshold is defined for AI gateway entitlement checks | High — currently only bounded by "must be less than the observed >2-day gap," not a designed number | Capstone team / CISO (role-played) | Phase 3 (Specify) | Open |
| R-1203 | Risk | Two real security events (cross-affiliate query, oversized-document loop) are recorded as currently unblocked and have no corresponding test | Critical — these map directly to INJ-068 and INJ-076 and must be closed before any security claim is made in the final defence | Capstone team / CISO (role-played) | Before `16_THREAT_ABUSE_MODEL.md` sign-off | Open |
| R-1204 | Gap | No test verifies live (non-cached) IAM state is actually checked at execution time | High | Capstone team | Phase 4 (Build) | Open |
| R-1205 | Gap | No test verifies checkpoint-age-based resume rejection/de-duplication | Medium-High | Capstone team | Phase 4 (Build) | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Output schemas remain valid and version-stable | `evaluation/contracts/*.schema.json` | `tools/test_contracts.py` | `evaluation/contract_samples/*` | PASS (6/6) |
| Cross-affiliate exfiltration query is blocked | Purpose-limitation gate (new) | Not yet implemented | E-1205 (`SEC-1`) | **Currently FAILS if replayed as-is** — no block exists |
| Oversized-document denial-of-wallet loop is blocked | Token/size cap gate (new) | Not yet implemented | E-1205 (`SEC-2`) | **Currently FAILS if replayed as-is** — no block exists |
| Stale cached entitlement is rejected at execution time | Live IAM check (new) | Not yet implemented | E-1203, E-1204 | Pending |
| Checkpoint resume beyond max age is rejected or de-duplicated | Checkpoint-age gate (new) | Not yet implemented | E-1202 | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
