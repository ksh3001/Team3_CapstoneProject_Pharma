# PRD — AEGIS Evidence Assist (provisional)

**One question this file answers:** What problem are we solving, for whom, and what does success look like?

| Field | Entry |
|---|---|
| Prompt | `prompts/03_prd_vision.md` |
| Skills | `spec-driven-delivery` |
| Narrative class | `hypothesis` — **provisional PRD** |
| Cites Prompt 02 | `submission/artefacts/prompts/02_scqa/scqa_minto_decision_narrative.md` |
| Spec hygiene | No workflows, APIs, DB schemas, UI wireframes, or folder trees |

---

## 1. Users / personas

| Persona | Need | Accountability note |
|---|---|---|
| Quality / QP support reviewer | Faster, cited readiness inputs | Does not certify |
| EU Qualified Person | Complete evidence for human certification | AI authority **none** |
| PV intake scientist | Structured intake with clocks/duplicates flagged | Does not finalize safety calls |
| Safety Physician | Preserve facts for reportability/causality decisions | AI authority **none** |
| Supply planner | Ranked options with constraints visible | Does not execute allocation |
| Supply Governance Board | Draft options only for approval | AI **draft only** |
| CQO / CISO / DPO (affected) | Quality authority, deny paths, purpose limitation | Policy / control owners |

Sources: `decision_rights.csv`, `stakeholders.csv`, `case/STAKEHOLDER_PACK.md`, Prompt 02 authority boundary.

---

## 2. Goals

1. Reduce evidence-reconciliation rework for the three mandatory assist workflows without changing registered specifications or Quality independent authority (BR-01 context).
2. Make conflicts, gaps, and abstentions explicit (dual citation; no silent “resolved”).
3. Preserve source facts, units, authority, and clocks for human decision-makers.
4. Block prohibited regulated actions in the assessed path.
5. Remain operable offline / AI-disabled per continuity requirements.
6. Measure proxies and honest TCO before locking genAI scale (Prompt 02 experiment).

---

## 3. Success metrics (experiment KPIs)

Write values where known; otherwise **Unknown**.

| Metric | Target / definition | Baseline |
|---|---|---|
| Prohibited-action block rate on negative fixtures | **100%** | N/A (control metric) |
| Unresolved identity/unit/time/authority conflict presented as resolved | **0** | Unknown |
| Supply side effects in assessed mode (reserve/allocate/ship/status change/recall) | **0** | Starter unsafe (not ops baseline) |
| AuthZ outcome for revoked user with active cache (`contractor_77` scenario) | **Deny** | Scenario present in package |
| Evidence-pack cycle-time proxy (median hours to cited pack) | Improve vs Team3 instrumented baseline | **Unknown** (P0) |
| Human review hours included in TCO | Tracked; use `staff_rates.csv` (Quality 92, Safety physician 165, Regulatory 148 USD/hr) | Hours **Unknown**; rates known; cost_model review lines = 0 |
| AI-disabled continuity drill | Pass: batch/supply manual path for **14** days; PV without inference (`max_ai_outage_hours=0`) | Unknown until drilled |
| Board −14% release lead time | Enterprise outcome — **not** a POC pass criterion alone | Current lead time **Unknown** |

---

## 4. In scope (this version) — product capabilities

Numbered capabilities only (not endpoints or screens):

1. Batch **evidence reconciliation support** — reconcile, cite, flag, abstain; readiness input only (`ai_use_boundaries.csv`).
2. PV **intake support** — extract, normalize, cluster (candidates), cite; clocks/terminology/listedness provenance.
3. Supply **option drafting** — generate options only; no execution.
4. Execution-time purpose / entitlement checks (deny stale cache as sole authority).
5. Authority-aware treatment of knowledge (approved vs superseded/untrusted/draft as data, not instructions).
6. Offline deterministic assessed mode.
7. AI-disabled / manual continuity as a first-class operating mode.
8. Evaluation gates that block “ready” on hard-control failures.
9. Measure instrumentation for the metrics in §3 (experiment scaffolding).
10. Parallel **no-AI** levers acknowledged in product intent: master-data repair and rules/checklist work (not generative features).

---

## 5. Out of scope (this version)

Load-bearing exclusions — later prompts must not silently pull these in:

1. Autonomous batch release / reject / reprocess / relabel / recall / any disposition.
2. Final seriousness, causality, expectedness, reportability, or signal confirmation.
3. Reserve, allocate, ship, quality-status change, or recall initiation.
4. Changing registered specifications or weakening Quality independent authority.
5. Mandatory cloud LLM, vector DB, or knowledge graph.
6. Claiming AI-EVIDENCE is GxP-validated for regulated decisions while validation inventories conflict.
7. Achieving or certifying the board −14% lead-time target as a POC deliverable.
8. Full brownfield system-of-record replacement or production cutover.
9. Feature flow detail, APIs, data models, UI, C4, ADRs (owned by later prompts).

---

## 6. Constraints and non-goals

| Type | Constraint |
|---|---|
| Compliance | `ai_use_boundaries.csv`; hard gates in scoring model |
| Accountability | `decision_rights.csv` |
| Continuity | `continuity_requirements.csv` — manual runbooks required |
| Platform | Offline-capable package; work under `submission/` only |
| Data | Synthetic training only; deliberate conflicts preserved |
| Economics | Do not treat cost_model human-review zeros as truth |
| Non-goal | Tool adoption / seat metrics as primary success |
| Non-goal | GenAI-first scale before Measure |

**Hard platform constraint (evidence):** assessed path must not require live cloud keys (`PACKAGE_SCOPE_AND_ASSUMPTIONS.md`). Vendor/model choice deferred (ADR later if needed).

---

## 7. Open questions (before Feature Specs harden)

From Prompt 01/02 backlog — must resolve or **explicitly assume** (labeled):

1. Measured release-pack cycle time (median/p90) — P0  
2. Knowledge SoT usage rules at as-of — P0  
3. Entitlement SoT: IAM vs gateway cache — P0  
4. Unit/interface mapping authority — P1  
5. Which validation inventory wins for AI-EVIDENCE — P1  
6. Actual human review hours per pack — P1  
7. as-of / clock field semantics per critical dataset — P1  
8. Whether generative assist survives falsifiers after MDM/rules — experiment outcome  

---

## Exit criteria self-check

- [x] Vision + PRD cite Prompt 02  
- [x] In-scope and out-of-scope explicit  
- [x] Success metrics with known/Unknown baselines  
- [x] No APIs, data models, architecture  
- [x] Labeled provisional under `hypothesis`  
- [x] Thin `dmaic_lens.md` present  
