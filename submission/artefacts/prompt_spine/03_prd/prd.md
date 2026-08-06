# Prompt 03 — PRD (provisional — hypothesis mode)

**One question this file answers:** What problem are we solving, for whom, and what does success look like?  
**Does not include:** APIs, schemas, UI wireframes, folder trees, feature flow detail.

Cites: Prompt 02 narrative; `ai_use_boundaries.csv`; `decision_rights.csv`; `continuity_requirements.csv`.

## 1. Users / personas

- Quality / QP support reviewers; EU Qualified Person (accountable certification)
- PV intake scientists; Safety Physician (accountable reportability/final safety calls)
- Supply planners; Supply Governance Board (accountable allocation)
- Secondary: CISO/validators (deny paths), DPO (purpose limitation)

## 2. Goals

- Assemble cited evidence packs with explicit gaps/contradictions/abstentions
- Preserve source facts and clocks for PV intake; cluster duplicate **candidates** only
- Produce non-executing supply/cold-chain options with constraints and approval needs
- Operate deterministically offline and via AI-disabled manual runbooks
- Never execute prohibited regulated actions

## 3. Success metrics

| Metric | Target / note | Baseline |
|---|---|---|
| Prohibited-action block rate on negative fixtures | 100% | N/A (control metric) |
| Unresolved conflicts presented as resolved | 0 | Unknown historical |
| Evidence-pack cycle-time proxy | Improve vs Team3 instrumented baseline | **Unknown** (acquire) |
| AI-disabled continuity drill | Pass for batch/supply 14-day; PV without inference | Unknown until drilled |
| Human review hours in TCO | Tracked using `staff_rates.csv` | **Unknown** (cost_model shows 0) |
| Board −14% release lead time | Enterprise outcome — **not** POC pass criterion alone | Unknown current |

## 4. In scope (this version) — product capabilities

1. Batch evidence reconciliation support (cite, flag, abstain, readiness input only)
2. PV intake support (extract, normalize, cluster candidates, cite clocks/terminology)
3. Supply option drafting with `no_side_effects`
4. Execution-time authorization and purpose checks
5. Authority-aware evidence treatment (no equal-trust malicious/untrusted instructions)
6. Offline deterministic mode + AI-disabled continuity
7. Evaluation gates that block “ready” on hard failures

## 5. Out of scope (this version)

1. Autonomous batch release/reject/reprocess/relabel/recall
2. Final seriousness/causality/expectedness/reportability/signal confirmation
3. Reserve/allocate/ship/quality-status change/recall initiation
4. Changing registered specifications or Quality independent authority
5. Mandatory cloud LLM, vector DB, or knowledge graph
6. Production cutover of brownfield systems of record

## 6. Constraints and non-goals

- Synthetic training only; offline-capable assessed path
- Work only under `submission/`
- Hypothesis mode: artefacts provisional until Measure upgrades framing
- Non-goal: winning on speed by weakening Quality/Safety accountability

## 7. Open questions (before Feature Specs harden)

- Knowledge SoT catalog at as-of time
- Unit/interface mapping authority
- Entitlement SoT vs cache
- Instrumented cycle-time and review-hour baselines
- Whether generative assist survives falsifiers after MDM/rules
