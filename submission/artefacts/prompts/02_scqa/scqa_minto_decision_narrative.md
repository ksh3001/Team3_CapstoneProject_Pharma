# Prompt 02 — SCQA & Minto Decision Narrative

| Field | Entry |
|---|---|
| Prompt | `prompts/02_scqa_minto.md` |
| Skills applied | `exec-communication` (Frame); `process-and-lean-discovery` (thin Define lens); routed via `fde-operating-model` |
| Prerequisite | `submission/artefacts/prompts/01_discovery/evidence_register.md` |
| Team | Team3 |
| As-of | 2026-08-06 |
| Output folder | `submission/artefacts/prompts/02_scqa/` |
| Architecture / vendor / model locked? | **No** |

---

## 0. Narrative class

| Field | Value |
|---|---|
| **Narrative class** | `hypothesis` — **matches Prompt 01; not upgraded** (no new measured baselines acquired) |
| **Evidence boundary** | Synthetic challenge package + Prompt 01 register only. Claims limited to cited facts/derivations; assumptions labeled and tied to acquisition backlog. No live NTG operational metrics. |
| **Top blocking acquisition items (keep hypothesis)** | P0: measured release-pack cycle time (median/p90); P0: knowledge SoT usage rules at as-of for approved vs superseded/untrusted/draft; P0: entitlement SoT policy (IAM vs gateway cache) — from `01_discovery/evidence_acquisition_backlog.md` |
| **Audience** | Board / CQO / Global PV Head / Supply Governance sponsors; Team3 defence panel (COO/CIO/CFO lenses as needed) |
| **Decision horizon** | Capstone qualification window; board BR-01 due 2026-11-30 is **context**, not a claimed POC SLA |
| **Authority boundary** | AI authority **none** on batch certification and ICSR reportability; **draft only** on stock allocation (`decision_rights.csv`). BR-01 forbids weakening Quality authority. |

---

## Governing answer (Minto — lead)

**Run a Measure-first hybrid experiment:** instrument conflict and cycle-time proxies while advancing master-data repair and rules/checklists; pilot a **narrow, fail-closed evidence-assist capability** that only cites/reconciles/flags/abstains (batch), extracts/clusters/cites (PV), and drafts **non-executing** supply options — with any generative model **optional and off by default**. **Do not** lock a genAI-first build or transfer regulated accountability to software.

---

## A. SCQA narrative

### Situation

NovaCura Therapeutics Group (NTG) operates a multi-region pharmaceutical estate spanning discovery, clinical, manufacturing, quality, PV, regulatory and supply (`case/INTEGRATED_CASE.md`; `case/SOURCE_SYSTEM_FACT_PACK.md`). The package exposes **139** profiled operational CSV datasets, **84** injects (all still `UNASSESSED`), and **32** knowledge documents with mixed trust (`DATASET_PROFILE.csv`, `inject_evidence_map.csv`, `knowledge_catalog.csv`). The board requested a **−14%** reduction in release lead time by **2026-11-30** without changing registered specifications or weakening independent Quality authority (`board_requests.csv` BR-01). Accountable humans retain final authority: EU QP (certification), Safety Physician (reportability), Supply Governance Board (allocation — AI draft only) (`decision_rights.csv`).

### Complication

Evidence needed for batch-review readiness, PV intake, and shortage/cold-chain response is slow, conflict-prone, and unsafe if automated naively:

| Dimension | Complication (cited) |
|---|---|
| Operational | Functional KPIs conflict (Manufacturing schedule adherence vs Quality RFT vs Safety expedited on-time vs Clinical DB lock) — `kpi_conflicts.csv` |
| Data | Lab potency unit ≠ spec unit on LR-88; interface mapping `1:1_assumed` with **approved=no** — `lab_results.csv`, `interface_mappings.csv` |
| Security | `contractor_77` IAM **revoked** while gateway cache remains **active_cached** — `users_entitlements.csv`, `access_cache.csv` |
| Knowledge / AI | Equal-trust retrieval pattern in starter; corpus includes untrusted K-998/K-999, superseded K-007, draft K-026 — `starter/legacy_pharma.py`, `knowledge_catalog.csv` |
| Supply / safety | Quarantine stock present; starter `plan_supply` returns `reservation_status: created` — `inventory.csv`, starter |
| GxP / validation | AI-EVIDENCE validation state disagrees across inventories (validated / conditionally_released / research_only) — `system_inventory.csv`, `validation_inventory.csv` |
| Financial | Inference cost line large; human Quality/medical review costed at **0** — `cost_model.csv` vs `staff_rates.csv` |
| Regulatory / human | Board speed pressure vs QP completeness and AI-use prohibitions — BR-01, `ai_use_boundaries.csv`, stakeholder pack |
| Measure gap | **Release-pack cycle-time distribution Missing** — Prompt 01 C-13 / backlog P0 |

Process-excellence estimates claim MDM **38%/10w**, rules **27%/6w**, genAI assist **51%/14w** (`no_ai_baselines.csv`) — directional challenge figures, not measured NTG baselines.

### Question

**For the three mandatory workflows (batch evidence support, PV intake support, supply option drafting), what capability should Team3 qualify and test first so evidence-reconciliation waste can fall without transferring regulated accountability to AI — and what must be measured before locking build-vs-no-AI?**

### Answer (`hypothesis` — recommended experiment)

**Experiment design**

1. **Measure first:** instrument package-local proxies (conflict dual-cite rate, prohibited-action block rate, side-effect absence, authZ deny on stale cache/untrusted docs) and acquire P0 baselines (cycle time, knowledge SoT rules, entitlement SoT).
2. **No-AI levers in parallel:** master-data repair backlog + rules/checklist gates (aligned to `no_ai_baselines.csv` order).
3. **Capability under test:** narrow **evidence-assist** (not decision engine) bounded by `ai_use_boundaries.csv`.
4. **Generative AI:** optional port only; **disabled by default** in assessed/offline mode until falsifiers fail to trigger and Measure upgrades framing mode.

**Falsifiers (stop / pivot)**

- Any path enables release/reject/reprocess/recall, final PV conclusions, or reserve/allocate/ship/quality-status change/recall initiation.
- Provenance, authority, effective date, units, or time precision not preserved; silent unit conversion or irreversible case merge.
- AI-disabled / manual continuity path missing (batch/supply 14-day; PV without inference — `continuity_requirements.csv`).
- MDM + rules alone meet agreed cycle-time proxies without assist → **pivot** to schema/checklist-only.
- Honest TCO (inference + observability + review hours × rates) worse than no-AI path → **stop** generative scale.

**Desired outcomes (“good”)**

- Cited conflicts with dual sides; abstentions when unresolved.
- 100% block of prohibited outputs on negative fixtures.
- Zero inventory/disposition side effects in assessed mode.
- Manual continuity drills documented.
- Quality authority unchanged (BR-01).

**Explicit exclusions (this decision does not cover)**

- Full PRD, feature flows, bounded contexts, C4, ADRs, vendor/model selection (Prompt 03+).
- Claiming board −14% achieved.
- Autonomous regulated decisions.
- Declaring AI-EVIDENCE “validated for GxP release decisions” while validation inventories conflict.

**Measurable outcomes (baseline known vs Unknown)**

| Metric | Target / note | Baseline |
|---|---|---|
| Prohibited-action block rate | 100% on negatives | Control metric (N/A historical) |
| Unresolved conflict presented as resolved | 0 | Unknown |
| Evidence-pack cycle-time proxy | Improve vs instrumented baseline | **Unknown** (P0) |
| Side-effect free supply runs | 0 mutations / reservations | Starter shows unsafe pattern (observed anti-pattern, not ops baseline) |
| AuthZ deny on revoked+cached user | Deny | Scenario present in package |
| Human review hours in TCO | Tracked | **Unknown** (cost_model = 0) |
| AI-disabled drill | Pass | Unknown until drilled |

---

## B. Minto pyramid

**Governing answer:** Qualify a Measure-first, fail-closed evidence-assist **experiment** — not a genAI autonomous decision engine.

### 1. Keep accountability human-owned

- **Fact:** AI authority none / draft only (`decision_rights.csv`).
- **Fact:** Allowed vs prohibited strings in `ai_use_boundaries.csv`.
- **Fact:** BR-01 forbids Quality-authority weakening.

### 2. Attack evidence waste before generative scale

- **Fact:** MDM 38%/10w and rules 27%/6w in `no_ai_baselines.csv`.
- **Derivation (Prompt 01 D-01/D-02):** starter defects and unit/auth conflicts are data/rules/governance failures, not “missing LLM.”
- **Labeled assumption (A-01):** packaged conflicts represent intentional challenge conditions — backlog: treat as design drivers until proven otherwise.

### 3. Bound the capability to the three workflows’ assist roles

- **Fact:** Case mandates batch evidence reconciliation without disposition; PV intake without final safety decisions; supply options without execution (`case/INTEGRATED_CASE.md` §4).
- **Fact:** Executable contract samples already reject prohibited batch/PV/supply shapes (`evaluation/contract_samples/`).

### 4. Measure Unknowns before claiming decision-ready value

- **Fact:** Cycle-time distribution Missing (Prompt 01).
- **Fact:** Human review costed at 0 while rates exist (`cost_model.csv`, `staff_rates.csv`).
- **Backlog P0/P1:** acquire cycle time and review hours before upgrading narrative class.

### 5. Prove deny-paths and continuity as first-class outcomes

- **Fact:** Stale cache after revoke (`access_cache.csv` / `users_entitlements.csv`).
- **Fact:** Untrusted/malicious knowledge in corpus (K-998/K-999).
- **Fact:** Continuity requires manual runbooks; PV `max_ai_outage_hours=0` (`continuity_requirements.csv`).

### 6. Do not pretend validation ambiguity away

- **Fact:** AI-EVIDENCE appears validated / conditionally_released / research_only across inventories.
- **Implication for experiment:** intended-use claims stay provisional until SoT for validation state is resolved (backlog P1) — **Assumption:** Quality inventory owner decides; do not silently pick one.

### 7. Price workflow economics, not licences alone

- **Fact:** Inference 184000 USD/mo; observability 31000 (`cost_model.csv`).
- **Derivation:** ROI that ignores review hours is invalid for sponsor (CFO lens — `exec-communication`).
- **Backlog P1:** measure review hours.

*(MECE check: accountability · waste levers · capability bound · Measure · controls/continuity · validation honesty · economics — no C4/tool point.)*

---

## C. Framing handoff pack

| Item | Content |
|---|---|
| **Decision question for PRD / DDD** (provisional) | What fail-closed **evidence-assist** capabilities are in scope for batch readiness support, PV intake support, and supply option drafts — and what is explicitly out of scope — under Measure-first `hypothesis` mode? |
| **Success metrics for PRD / DMAIC** | See measurable outcomes table above; mark Unknown baselines explicitly in Prompt 03 |
| **Open questions blocking design** | Cycle-time baseline; knowledge SoT rules at as-of; IAM vs cache SoT; unit mapping authority; AI-EVIDENCE validation SoT; as-of/clock field semantics; review hours |
| **Later artifacts provisional?** | **Yes** — PRD through ADR must be marked **provisional** until framing mode upgrades or assumptions are explicitly accepted |

### Executive lenses (same Answer, four readings)

| Lens | Reading |
|---|---|
| Board | Operating-model experiment to cut evidence latency **without** transferring Quality authority |
| COO | Target three named workflows’ reconciliation loops, not “AI seats” |
| CIO/CTO | Orchestrate fail-closed assist + deny paths; no model lock-in yet |
| CFO | Baseline cycle time and review cost **before** funding genAI scale |

---

## Exit criteria self-check

- [x] Narrative class `hypothesis` consistent with Prompt 01
- [x] SCQA complete; no unlabeled invented facts
- [x] Pyramid MECE; supports are fact / derivation / labeled assumption + backlog
- [x] Answer is experiment with falsifiers and acquisition needs
- [x] Capability level only (no C4 / vendor / model)
- [x] One bounded question ready for Prompt 03
- [x] Thin `dmaic_lens.md` Define focus written
