# Incident and Recovery

> Team3 Phase 6 artefact (template 25). POC playbook — **not** a validated enterprise IR plan. Continuity drill (AC-052) remains deferred.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Ops / Security / Evaluation |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Architecture; GxP; Product |
| Status | Phase 6 — provisional |
| Related | INJ-066…070, INJ-080; ADR-001–004; AC-050–052; tmpl 24 |

## Purpose

Define incident taxonomy, detection/triage, kill switches, evidence preservation, rollback, communications, and CAPA/resumption for the assessed AEGIS assist POC so outages and abuse do not create prohibited side effects.

## Evidence register

| Evidence ID | Source | Fact used | Limitation |
|---|---|---|---|
| E-IR-01 | `case/INTEGRATED_CASE.md` D10 | INJ-065…070, INJ-080 | Synthetic |
| E-IR-02 | AC-050/051; phase3/4 tests | Offline / AI-disabled / poison controls | Unit scope |
| E-IR-03 | `incident_playbook.csv` | Scenario→action map | This phase |
| E-IR-04 | Prompt 12 RR-02 | AC-052 drill not executed | Open |
| E-IR-05 | `working/audit/`, `working/metrics/` | Local telemetry | No SIEM |

## 1. Incident taxonomy

| Class | Examples | Severity (POC) |
|---|---|---|
| I-AUTHZ | Revoked user allowed; purpose bypass | Critical |
| I-POISON | Prompt-injection SOP; poisoned tool manifest | Critical |
| I-AGENCY | Disposition/final PV/reservation attempt succeeds | Critical |
| I-MODEL | Hash mismatch package enabled; LLM on assessed | High |
| I-EXFIL | Cross-affiliate identifiable dump | High |
| I-AVAIL | Ransomware / OT cut; model down; checkpoint corruption | Med–High |
| I-DATA | Challenge tree mutation; audit loss | Critical |
| I-COST | Denial-of-wallet if narrator enabled | Med (N/A assessed) |

## 2. Detection and triage

| Signal | Detect how (POC) | First responder |
|---|---|---|
| AuthZ allow on revoked | pytest / evaluate / audit reason missing `iam_revoked` | Security |
| side_effect_count > 0 | Metrics JSON; evaluate gate | Supply + Security |
| LLM call on assessed | `call_count` / mode flag | Architecture |
| Quarantine miss | Doc applicability tests; catalog | Security + Quality |
| Schema / prohibited field accept | Contract validate | Evaluation |
| Ops alert paging | **Not deployed** | Gap → prod |

Triage rule: **patient/process-impacting agency first**; then AuthZ/poison; then availability.

## 3. Containment and kill switch

| Switch | Action | Owner |
|---|---|---|
| AI kill | Set mode `ai_disabled`; refuse narrator | Ops / Architecture |
| Tool plane | Keep write adapters disconnected (ADR-003) | Architecture |
| AuthZ fail-closed | Deny on IAM ambiguity/revoke | Security |
| Evaluate block | `ready_blocked=true` on gate fail | Evaluation |
| Network | Local-only CLI; do not expose unbound | Security |
| Stop ship | Demo/production **no-go** remains if Critical class fires | Product |

## 4. Evidence preservation

| Artefact | Preserve |
|---|---|
| AuthZ + workflow audits | `submission/working/audit/` — do not overwrite during IR |
| Metrics events | `working/metrics/` |
| Evaluate results | Export under `submission/evidence/` |
| Challenge tree | Immutable — never “fix” by editing `data/`/`knowledge/` |
| Decision log | Append IR decision IDs; no silent delete |

## 5. Rollback and reconciliation

| Scenario | Rollback | Reconcile |
|---|---|---|
| Bad code deploy (future) | Git revert participant `submission/` | Re-run pytest + evaluate |
| Stale agent checkpoint (INJ-080) | Discard draft; no reservation exists by design | Confirm side_effect_count=0 |
| Wrong pack content | Re-run workflow with new idempotency key; retain prior audit | Human reviews citations |
| MES/WMS writes | **N/A** — not integrated | If ever added, ADR reopen + full IR redesign |

## 6. Communication and regulatory assessment

| Audience | Message constraint |
|---|---|
| Sponsors / board | No ROI claim from incident; hypothesis framing |
| Quality / QP / Safety | Assist outage ≠ authority change; manual packs continue |
| Regulators (prod hypothetical) | Escalate Legal/GxP — POC makes **no** notification claim |
| Affiliates | Purpose limitation; no bulk narrative share during IR |

## 7. CAPA and resumption criteria

| CAPA theme | Resumption requires |
|---|---|
| Critical agency incident | Root cause + regression test + evaluate green + sponsor ack |
| Poison/tool | Manifest allow-list proof; phase3-class tests green |
| AuthZ | IAM>cache re-verified; matrix rows green |
| Continuity | AC-052 drill evidence (still **open**) before ops “resumed” claim |
| Model enable after incident | ADR-002 revisit + registry hash match |

**Resumption for assessed demo:** pytest green + evaluate `ready_blocked=false` + no Critical open IR.  
**Resumption for production:** not applicable — remains **no-go**.

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-IR-01 | Gap | AC-052 14-day drill not executed | Open (RR-02) |
| R-IR-02 | Gap | No on-call / SIEM | Accepted POC |
| R-IR-03 | Assumption | No write plane remains true | ADR-003 |

## Traceability and acceptance

| Claim | Control | Test | Result |
|---|---|---|---|
| Kill switches defined | §3 | AC-051; mode | Pass (POC) |
| Agency incidents fail closed | SideEffectGuard + schema | phase3 | Pass |
| Full IR program | — | Drill missing | Partial |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Ops | Owner | Drill residual explicit | RR-02 unchanged | 2026-08-07 |
