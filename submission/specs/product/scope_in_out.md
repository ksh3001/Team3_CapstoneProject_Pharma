# Scope In / Out — AEGIS Evidence Assist

| Field | Entry |
|---|---|
| Prompt | `prompts/03_prd_vision.md` |
| Narrative class | `hypothesis` (provisional) |
| Cites | `prd.md`, `02_scqa/scqa_minto_decision_narrative.md` |

## In scope (this version)

| # | Capability |
|---|---|
| 1 | Batch evidence reconciliation support (reconcile, cite, flag, abstain) |
| 2 | PV intake support (extract, normalize, cluster candidates, cite) |
| 3 | Supply option drafting only (`no_side_effects` intent) |
| 4 | Execution-time purpose / entitlement checks |
| 5 | Authority-filtered knowledge handling |
| 6 | Offline deterministic assessed mode |
| 7 | AI-disabled / manual continuity mode |
| 8 | Hard evaluation gates that block “ready” |
| 9 | Measure instrumentation for experiment KPIs |
| 10 | Acknowledgement of parallel MDM + rules levers (non-generative) |

## Out of scope (this version)

| # | Exclusion |
|---|---|
| 1 | Autonomous batch disposition / certification |
| 2 | Final PV safety or reportability decisions |
| 3 | Reserve / allocate / ship / quality-status change / recall |
| 4 | Spec or Quality-authority changes |
| 5 | Mandatory LLM / vector DB / knowledge graph |
| 6 | GxP “validated decision” claim under conflicting AI-EVIDENCE inventories |
| 7 | Board −14% as POC pass criterion |
| 8 | Production cutover / SoR replacement |
| 9 | Feature flows, APIs, schemas, UI, C4, ADRs (later prompts) |

**Rule:** Any later prompt that pulls an Out-of-scope item without change control violates this PRD.
