# Prompt 12 — Evaluation Report

| Field | Entry |
|---|---|
| Prompt | `prompts/12_assurance.md` |
| Date | 2026-08-06 |
| Narrative class | `hypothesis` (unchanged) |
| Offline eval | `pytest submission/tests` → **25 passed**; `/v1/evaluate/run` hard gates **all pass**, `ready_blocked=false` |
| Online/ops | CLI health + workflow dispatch only (no hardened HTTP load test) |

**Verdict legend:** `pass` | `fail` | `partial` | `inconclusive (data scarcity)` | `deferred`

---

## 1. Design fidelity

| Area | Verdict | Notes |
|---|---|---|
| C4 / DDD → code | **partial** | Single runtime, AuthZ, ACL reads, three workflows, SideEffectGuard, evaluate, mode/LLM-off match provisional C4; no separate HTTP container, no UI; BC role matrix thin (QP-only allow in POC) |
| ADR implementation | **partial** | ADR-001/003/004/007 followed in code; ADR-002 followed (off); ADR-005/006/008/009/010 proposed and partially implemented locally; no violations logged |
| Technical contracts | **pass** (POC slice) | Responses validated against `evaluation/contracts/*`; prohibited fields → 422/409; idempotency on POST workflows |
| Module rules | **pass** | Routers thin (`app_api.py`); CSV via ACL; no challenge writes; LLM no-op |
| Ubiquitous language | **partial** | `readiness_state`, `execution_status=not_executed`, `no_side_effects`, Conflicts dual-cite present; no UX surface |
| Feature ACs/BRs | see §6 | 24/25 in-scope ACs **pass**; AC-052 **deferred** |

---

## 2. Data & authority

| Area | Verdict | Notes |
|---|---|---|
| Data-contract handling | **partial** | Schema validate on emit; package schemas versioned externally; participant schema copy not separately versioned |
| Identifier / timestamp | **partial** | Dual clocks for PV-1001 via `safety_receipts` + awareness; P1 clock dictionary still open → ADR-009 residual |
| Conflict / freshness | **pass** (fixtures) | LR-88 unit conflict; unapproved mapping cited; readiness not “resolved” silently |
| Authority / SoT | **pass** (catalog filter) | K-998/K-999/K-026/K-007 not instructional; K-006 applicable |
| Privacy / security / remote access | **partial** | Local CLI; no public OAuth; challenge paths read-only; full adversarial/privacy suite **not** run → beyond slice |

---

## 3. AI / decision quality

| Area | Verdict | Notes |
|---|---|---|
| Deterministic where claimed | **pass** | No LLM calls on assessed path; fixture-stable outcomes |
| Explainability | **partial** | Contradictions/gaps/required_reviews/cited evidence present; no narrative layer (by design) |
| FP / FN examples | **pass** (documented) | See `fp_fn_examples.md` |
| HITL paths | **partial** | Flags/required_reviews set; queue depth/age **not** measured in ops |
| Eval uses DDD/AC IDs | **pass** | Evaluate results include `ac_ids`; tests named by AC |
| Lean eval waste | **partial** | Hard gates tied to release block; cycle-time metrics emit but not decision-grade yet |

---

## 4. Operability

| Area | Verdict | Notes |
|---|---|---|
| Degraded mode | **pass** (unit) | AI-disabled refuses narrator; deterministic path continues (AC-050/051) |
| Critical workflows E2E | **pass** (CLI/fixture) | Batch / PV / supply / authz / evaluate exercised |
| Performance vs NFR-06–08 | **inconclusive (data scarcity)** | No load suite; single-run latency only; p95 ≤30s not statistically shown |
| Observability | **partial** | Audit + metrics JSON under `submission/working/`; no owned ops dashboards |

---

## 5. Control & risk

| Area | Verdict | Notes |
|---|---|---|
| Control standards documented | **pass** | Prompt 09 §5 + this report |
| Control operating in production | **fail** (N/A POC) | Owners named on paper; not operating in live NTG systems |
| Residual risk | see `residual_risk_register.md` | |
| Ambiguities | AMB-PV-01 open-blocked; others assumed | |

---

## 6. Material AC results

| AC | Verdict | Evidence |
|---|---|---|
| AC-001–003 | **pass** | `test_ac_authz.py` |
| AC-010–012 | **pass** | `test_ac_documents.py` |
| AC-020–023 | **pass** | `test_ac_batch.py` |
| AC-030–033 | **pass** | `test_ac_pv.py` |
| AC-040–043 | **pass** | `test_ac_supply.py` |
| AC-050–051 | **pass** | `test_ac_continuity.py` |
| AC-052 | **deferred** / **inconclusive (data scarcity)** for ops claim | Checklist stub only; 14-day drill not executed |
| AC-060–063 | **pass** | `test_ac_evaluate.py` + live evaluate run |

---

## 7. Evidence sampling notes

**Tested:** Package fixtures (contractor_77, LR-88, K-998/999/007/026/006, quarantine inventory, PV-1001 clocks, reservation attempt, prohibited disposition, evaluate suite).

**Not tested:** Full 12 TEVV suites; public PUB fixtures end-to-end; adversarial prompt-injection corpus beyond doc quarantine; load/perf; real IAM; MES/WMS integration; org continuity drill; board −14% lead time; fuzzy matching (blocked).

**Could not test (scarcity):** Ops median/p90 pack cycle-time; actual human review hours; multilingual subgroup baselines; LF-normalized full package hash audit on this checkout (A-001 residual).

---

## 8. Defect & waste findings → Analyze/Improve

| ID | Finding | Type | Action |
|---|---|---|---|
| D-A01 | AuthZ allow hardcoded to `qualified_person` only | Defect (thin role model) | Enrich purpose↔role matrix before broader demo users |
| D-A02 | `jsonschema.RefResolver` deprecation | Tech debt | Migrate to `referencing` |
| D-A03 | HITL queue metrics not emitted | Measure gap | Add depth/age counters (Prompt 09 Control) |
| D-A04 | AC-052 drill not run | Control gap | Phase 7 runbooks + execute |
| W-A01 | Inference cost model line unused while LLM off | Residual cost waste signal | Keep LLM off; do not scale tokens |
| W-A02 | Fuzzy CSV scores if trusted would create FP merges | Prevented waste | Keep AMB-PV-01 blocked |

---

## 9. Go / conditional-go / no-go

| Path | Recommendation | Rationale |
|---|---|---|
| **Capstone demo / offline pilot** | **conditional-go** | Hard controls and ACs (except AC-052) pass; hypothesis framing; show fail-closed paths; disclose residuals |
| **Production / validated GxP decision support** | **no-go** | Material `inconclusive (data scarcity)` on cycle-time/review baselines; AC-052 unproven; DoD §4–5 incomplete; AI-EVIDENCE validation triple-state unresolved; no production IAM/write-plane ADR |

Sponsors must explicitly accept residual risks before any production go; this report does **not** authorize that acceptance.
