# Prompt 09 — DMAIC Plan (Measure-first)

| Field | Entry |
|---|---|
| Prompt | `prompts/09_lean_dmaic.md` |
| Narrative class | `hypothesis` |
| Mode | **Measure-first** — instrumentation and evidence acquisition outrank new AI features |
| Aligns | Prompt 02 Question/Answer; Prompt 03 PRD scope & metrics; FR AC register |

---

## 1. Define

**Problem (from Prompt 02):** Evidence reconciliation for batch readiness, PV intake, and supply planning is slow and error-prone across brownfield systems; unsafe starter paths and equal-trust knowledge create defect and overproduction risk. Board wants −14% release lead time without changing Quality authority.

**Improvement scope (this POC):** AEGIS Evidence Assist — cite/flag/abstain/options only for three workflows; purpose-bound AuthZ; authority-aware documents; offline/AI-disabled continuity; evaluation hard gates; Measure scaffolding.

**Out of Define (non-negotiable):** Autonomous disposition, final PV safety decisions, reserve/allocate/ship/status change/recall, mandatory genAI/RAG scale, claiming board −14% as POC pass.

**CTQs (control + experiment):**

| CTQ | Type | Target | AC / metric link |
|---|---|---|---|
| Prohibited actions blocked | Control | 100% on negative fixtures | AC-023, AC-030, AC-043, AC-060–062 |
| False “resolved” conflicts | Control | 0 | AC-020, AC-022, AC-032; PRD §3 |
| Supply side effects | Control | 0 | AC-040–043, NFR-02 |
| AuthZ revoke+cache | Control | Deny | AC-001 |
| Cycle-time proxy | Experiment | Improve vs Team3 instrumented baseline | PRD §3; **baseline Unknown** |
| Human review hours in TCO | Experiment | Tracked × `staff_rates.csv` | PRD §3; **hours Unknown** |
| AI-disabled continuity | Control drill | Pass per continuity CSV | AC-052 |

**Stakeholders / owners:** Quality/QP support, PV intake, Supply planner (users); CQO / CISO / DPO (controls); Team3 Evaluation owns gates; Architecture owns mode/contracts.

---

## 2. Measure

### 2.1 Known / package-local now

| Metric | Current signal | Source |
|---|---|---|
| Contract suite | PASS 6/6 | `tools/test_contracts.py` |
| Inject / dataset / knowledge counts | 84 / 139 / 32 | package inventories |
| Concrete conflict fixtures | LR-88, interface mapping approved=no, contractor_77, quarantine inventory, AI-EVIDENCE triple | data CSVs |
| Inference cost model line | 184000 USD/mo listed | `cost_model.csv` |
| Observability cost line | 31000 | `cost_model.csv` |
| Human review cost lines | 0 (gap) | `cost_model.csv` |
| AuthZ scenario | revoke+cache present | entitlements + access_cache |
| Architecture review | conditional | Prompt 07 |

### 2.2 Unknown baselines (explicit)

| Metric | Status | Blocks |
|---|---|---|
| Median / p90 release-pack or evidence-pack cycle time | **Missing** | ROI / board −14% claims; framing → decision-ready |
| Ops PV intake rework rate / clock-slip frequency | **Missing** | PV Improve prioritization beyond fixtures |
| Actual human review hours per pack | **Missing** | Honest TCO; FinOps |
| Token use of future model path | **N/A until LLM on** | ADR-002 revisit |
| Fuzzy duplicate precision/recall | **Unknown** | AMB-PV-01 open-blocked |
| AI-disabled drill completion | **Unknown until drilled** | AC-052 evidence |
| Full LF-normalized package hash audit | **Partial** (CRLF residual A-001) | production package claims |

### 2.3 Measure targets for pilot (Prompts 10–12)

| ID | Measure action | Target | AC / NFR |
|---|---|---|---|
| M-01 | Instrument pack timestamp: request → cited pack emit | Capture median/p90 for Team3 fixture runs | PRD cycle-time proxy |
| M-02 | Count Conflicts / Abstentions / ready_for_authorized_review per run | 100% material conflicts dual-cited; 0 silent resolve | AC-020, AC-022, AC-032 |
| M-03 | Side-effect counter on supply path | Always 0 | AC-041–043, NFR-02 |
| M-04 | AuthZ decision log completeness | 100% of checks audited | AC-003, NFR-11 |
| M-05 | Evaluate hard-gate pass/fail machine-readable | 100% suite results recorded | AC-060–063 |
| M-06 | Manual review-hour log template (even if estimated) | Non-zero process for TCO | PRD §3 |
| M-07 | Continuity drill checklist execution | Pass/fail recorded | AC-052 |
| M-08 | Latency p95 per workflow | ≤30s offline deterministic (NFR-06–08) | Prompt 08 NFRs |

---

## 3. Analyze

| Root cause / gap | Waste link | Evidence | Assumption? |
|---|---|---|---|
| Multi-system brownfield hunt without single cite pack | Waiting, Motion, Extra processing | Fact pack; case §2 | **Hypothesized** ops magnitude |
| Lexical readiness / silent unit convert in starter | Defects | `legacy_pharma.py`; LR-88 | **Observed** |
| Equal-trust knowledge + malicious SOP | Retrieval waste, Defects | K-998/K-999; search_knowledge | **Observed** pattern |
| Quarantine treated available; plan creates reservation | Overproduction | inventory; plan_supply | **Observed** |
| Stale cache as sole AuthZ | Defects | contractor_77 | **Observed** |
| Uncounted human review in cost model | Human-review / Observability waste | cost_model zeros | **Observed** gap; hours hyp. |
| Ambiguous clocks / readiness language | Extra processing, Defects | INJ clocks; DDD glossary | Partial package + **assumed** interim dual-cite |
| Premature genAI before Measure | Token, Model, bias Defects | cost_model; AI-EVIDENCE triple | **Hypothesized** if scaled; ADR-001/002 prevent |
| Fuzzy threshold Unknown | Waiting (manual queue) vs false-accept Defects | AMB-PV-01 | **Open-blocked** by design |

Analyses resting on assumptions must not drive scale-out of agents/retrieval.

---

## 4. Improve

**Order rule:** Evidence acquisition and instrumentation **before** optional AI features. Cross-link: `01_discovery/evidence_acquisition_backlog.md`.

| Priority | Improve action | Implements / defers | Backlog link |
|---|---|---|---|
| P0 | Build deterministic offline Workflow Runtime for FR-001–007 per Prompt 08 contracts | Prompt 10–11 | — |
| P0 | Instrument M-01–M-05, M-08 in runtime + evaluate | Prompt 11–12 | P0 cycle-time acquisition |
| P0 | Enforce AuthZ IAM>cache; document quarantine; no writes | FR-001/002/005 | P0 entitlement / SoT |
| P0 | Conflict dual-cite; readiness ≠ disposition; unit conflict block | FR-003 | P1 unit mapping |
| P0 | PV exact/strong_key only; fuzzy **deferred** | FR-004 | AMB-PV-01 |
| P0 | AI-disabled / mode controller; refuse narrator | FR-006 | Continuity |
| P1 | Review-hour logging + staff_rates TCO rollup | Measure / FinOps | P1 human hours |
| P1 | Continuity drill runbooks + execute M-07 | Phase 7 / Prompt 12 | AMB-CONT-01 |
| P1 | Risk-routed HITL queue metrics (depth, age) | Control | ADR-007/009 Waiting |
| P2 | Optional narrator / LLM port only after ADR-002 revisit triggers | **Defer** scale | Token baselines |
| P2 | Fuzzy matching after golden set ≥50 + threshold ADR update | **Blocked** | AMB-PV-01 |
| — | MDM programme / master-data repair | Parallel org lever — **not** product FR scale | D-006 |

**Do not schedule:** agent swarms, write-execution adapters, broad RAG, board −14% optimization loop.

---

## 5. Control

| Control | Standard | Owner | Revisit trigger (from ADR lens 07 + NFRs) |
|---|---|---|---|
| Hard evaluation gates | Ready blocked on fail | Evaluation | Any prohibited shape allow → stop ship |
| Side effects | 0 in assessed mode | Architecture / Supply BC | Count >0 → incident + ADR-003 reopen |
| AuthZ | Deny revoke+cache | Security | Allow on contractor_77 fixture → blocker |
| Audit completeness | 100% purpose-bound checks | Evidence Store owner | Missing audit field → gate fail |
| LLM default | Off assessed | Mode Controller | Any assessed path LLM call without ADR-002 accept |
| Fuzzy | Disabled | PV BC | Enable only with numeric threshold + eval |
| HITL queues | Measure depth/age | Quality / PV process | Sustained growth without risk-route → Improve |
| Continuity | Drill pass recorded | Ops / Team3 | Drill fail → FR-006 reopen |
| Framing class | Stay `hypothesis` until P0 cycle-time acquired or assumed labeled | Product | Upgrade only with measured baseline |

**Feeds Prompt 12:** NFR-02/03/04/05/11; AC-060–063; control_lens_rollup later.
