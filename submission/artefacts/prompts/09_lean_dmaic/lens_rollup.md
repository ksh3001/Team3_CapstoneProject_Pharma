# Prompt 09 — Lens Roll-up (01–08)

| Field | Entry |
|---|---|
| Prompt | `prompts/09_lean_dmaic.md` |
| Skills | `process-and-lean-discovery` |
| Narrative class | `hypothesis` — Measure-first |
| Architecture review | `conditional` (`../07_adrs/architecture_review.md`) |
| Status | provisional consolidation |

**Rule:** Full DOWNTIME / AI registers below deepen this roll-up; they do not restart from a blank page.

---

## 1. Prior thin lenses

| Prompt | Path | DMAIC focus | Top findings |
|---|---|---|---|
| 01 | `../01_discovery/dmaic_lens.md` | Measure + light Define | Package-local measures exist; cycle-time / review-hours / token baselines **Unknown**; top wastes: Extra processing/Waiting (hyp), Defects (obs), retrieval/equal-trust (obs) |
| 02 | `../02_scqa/dmaic_lens.md` | Define | Complication wastes mapped; Answer = MDM/rules + deterministic cite/flag/abstain; must not automate disposition/PV-final/allocate |
| 03 | `../03_prd/dmaic_lens.md` | Define + Measure targets | In-scope removes waste; out-of-scope blocks overproduction; LLM off-default; board −14% not POC CTQ |
| 04 | `../04_ddd/dmaic_lens.md` | Analyze | POL-* invariants remove Defects; HITL risk-route; RAG bound to Applicable Docs; glossary gaps → Extra processing |
| 05 | `../05_features/dmaic_lens.md` | Analyze + Improve-by-spec | AC/BR stop unit/auth/injection/side-effect defects; AMB-PV-01 fail-closed (Waiting trade-off); no FR for autonomous decisions |
| 06 | `../06_c4/dmaic_lens.md` | Improve-by-arch | Single runtime + ACL cuts Transportation; no write plane / agent swarm; audit ownership named |
| 07 | `../07_adrs/dmaic_lens.md` | Analyze + Control triggers | ADR-001–010 prevent named wastes; HITL queues measured; write-plane smuggle = blocker |
| 08 | `../08_technical/dmaic_lens.md` | Improve contracts + Control NFRs | LLM=0 assessed; NFR hard gates; AMB-PV-01 open-blocked to prevent build thrash |

**Also used:** `../01_discovery/early_waste_signals.md`, `../01_discovery/evidence_acquisition_backlog.md`.

---

## 2. Merged waste names (deduped)

**DOWNTIME already named:** Defects (lexical ready, unit mismatch, untrusted docs, stale auth, automation bias); Overproduction (quarantine-as-available, fake reservation, write plane / agent swarm); Waiting (multi-system hunt, HITL queues, validation triple-state); Non-utilized talent (SME on repetitive checks — hypothesized); Transportation (brownfield hops); Inventory (exception/duplicate queues, unreviewed AI outputs); Motion (screen switching / context rebuild); Extra processing (duplicate validation, silent convert rework, untyped lake, missing audit → inspection rework).

**AI-specific already named:** Token/cost (inference line; LLM-off caps); Retrieval (equal-trust / malicious SOP); Model (premature genAI, blind retries); Human-review (uncounted hours; over-review vs risk-route); Evaluation (hard gates); Integration (ACL/SoT clarity); Context (as_of/citation in kernel); Observability (unowned logs avoided by Evidence Store).

---

## 3. Lens gaps / shallow spots

| Gap | Severity | Handling in Prompt 09 |
|---|---|---|
| No ops-measured cycle-time or review-hour numbers in any lens | High | Measure-first Improve #1–#3; Unknown baselines listed in `dmaic_plan.md` |
| Non-utilized talent barely quantified | Medium | Hypothesized in DOWNTIME-N; do not invent SME hours |
| Language / accessibility baselines only P2 backlog | Low | Residual; not gate for POC fail-closed path |
| Duplicate thin copies under `prompt_spine/` | Doc hygiene | Canonical paths above; spine copies ignored for roll-up |
| Prompt 01 sufficiency Partial/Missing | High | Keeps narrative class `hypothesis` until P0 acquisition |

**Missing lens files:** none for Prompts 01–08 under `submission/artefacts/`.
