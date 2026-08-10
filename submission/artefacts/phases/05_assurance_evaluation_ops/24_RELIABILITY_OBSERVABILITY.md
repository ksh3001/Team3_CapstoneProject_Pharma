# Reliability and Observability

> Team3 Phase 5 artefact (template 24). POC SLI/SLO aspirational where load evidence is scarce.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Architecture / Ops |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Evaluation; Security |
| Status | Phase 5 — provisional |
| Related | NFR-06–12; AC-050–052; MetricsCollector; RR-02/12 |

## Purpose

Define critical journeys, SLIs/SLOs, telemetry, lineage, capacity, fallback, and retention for the assessed runtime — without claiming enterprise SRE maturity.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-RO-01 | `submission/src/runtime/metrics.py` | Per-request metrics JSON |
| E-RO-02 | `submission/working/audit/` | AuthZ + workflow audits |
| E-RO-03 | NFR table Prompt 08 | Latency/idempotency/immutability targets |
| E-RO-04 | Prompt 12 operability section | Load inconclusive; observability partial |
| E-RO-05 | INJ-069 ransomware / OT | Degraded mode context |

## 1. Critical user journeys

| Journey | Path | Failure mode |
|---|---|---|
| J1 AuthZ check | `/v1/authz/check` or CLI | Deny/stop |
| J2 Batch evidence | workflow batch_evidence | Conflict/gap; never disposition |
| J3 PV intake | workflow pv_intake | No finals; manual duplicate |
| J4 Supply options | workflow supply_options | no_side_effects; quarantine excluded |
| J5 Evaluate gates | `/v1/evaluate/run` | ready_blocked on gate fail |
| J6 Continuity | deterministic_offline / ai_disabled | Narrator refused; rules continue |

## 2. SLI/SLO and error budgets

| SLI | POC SLO | Evidence status |
|---|---|---|
| Hard-gate pass rate (assessed suite) | 100% | **Met** (pytest) |
| AuthZ deny on revoked IAM | 100% | **Met** (AC-001) |
| Side effects on assessed path | 0 | **Met** |
| LLM calls assessed | 0 | **Met** |
| Pack latency p95 | ≤30s (NFR-06–08) | **inconclusive** — no load suite (RR-12) |
| Continuity drill success | AC-052 | **Deferred** (RR-02) |
| Error budget for prohibited-field leaks | **0** — not burnable | Policy |

## 3. Logs, metrics and traces

| Signal | Where | Notes |
|---|---|---|
| AuthZ decision | `working/audit/authz_*.json` | user, purpose, decision, checked_at |
| Workflow audit | `working/audit/*` | mode, llm_enabled, conflicts |
| Latency / counters | `working/metrics/*_*.json` | started/ended_ms, side_effect_count |
| Distributed traces | **None** | POC local only |
| Dashboards / paging | **None** | Prod gap |

## 4. Data/model/prompt/tool lineage

| Lineage element | POC record |
|---|---|
| Challenge inputs | Paths via CSV ACL; immutable challenge tree (NFR-12) |
| Evidence items | authority, effective_at, sha256, source_preserved |
| Schema version | `src/contracts/VERSION.md` 1.0.0-poc |
| Model / prompt | N/A assessed (LLM off); registry check if enabled |
| Tools | Poisoned manifest not loaded; no write tools |
| Evaluate result | ac_ids + evidence_path in runner output |

## 5. Capacity and backpressure

| Topic | Stance |
|---|---|
| Concurrent users | Single-operator CLI assumed |
| Backpressure | Fail closed on AuthZ/schema; bounded steps |
| Queue depth HITL | **Not measured** |
| Token DoW | Avoided (LLM=0); mode kill switch |

## 6. Outage, fallback and recovery

| Scenario | Behaviour | Evidence |
|---|---|---|
| LLM / AI outage | Continue rules-only | AC-051 |
| Network isolation | Deterministic offline | AC-050 |
| Ransomware / OT segment (INJ-069) | No MES write dependency (by design) | ADR-003 |
| Stale agent checkpoint (INJ-080) | No reservation duplication — side effects blocked | AC-043 |
| 14-day continuity drill | **Not executed** | AC-052 deferred |
| Rollback | Git + immutable challenge; no prod deploy | N/A |

## 7. Alerting and evidence retention

| Topic | POC | Production |
|---|---|---|
| Alerts | Manual inspection of evaluate/pytest | SIEM on AuthZ deny spikes, side_effect>0, LLM>0 |
| Retention | Working/audit for evaluation window | GxP retention + legal hold process (Phase 4) |
| Evidence export | Paths in evaluate results | Controlled export w/ purpose |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-RO-01 | Gap | No load/perf proof for p95 | Open RR-12 |
| R-RO-02 | Gap | AC-052 drill | Open RR-02 |
| R-RO-03 | Gap | No ops dashboards/paging | Accepted POC |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Journeys instrumented locally | metrics + audit | Pass (POC) |
| Hard reliability SLIs met | pytest | Pass |
| Enterprise SRE readiness | §3/7 gaps | Fail / no-go |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Architecture | Owner | SLO honesty on latency | Mark inconclusive | 2026-08-07 |
