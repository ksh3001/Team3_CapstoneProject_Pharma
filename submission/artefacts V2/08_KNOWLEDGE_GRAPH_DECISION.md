# Knowledge Graph Decision

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `05_DDD_CONTEXT_MAP.md`; `07_ONTOLOGY_SEMANTIC_LAYER.md`; INJ-021, INJ-037, INJ-052, INJ-053, INJ-058 |

## Purpose

Decides, with a genuine simpler-alternative benchmark, whether and where a knowledge-graph capability is justified — per `case/INTEGRATED_CASE.md` §3, the team "may conclude that a... knowledge graph... is unjustified, but must prove the decision." Accountable owner: capstone team. Completion criteria: at least one real use case is shown to need graph traversal, and at least one superficially graph-like use case is shown NOT to need it, both evidenced.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-701 | `data/batches.csv` + `data/material_genealogy.csv` | Batch/genealogy registers, undated | Batch `NCB204-B24071` (CMO-IE, quality_hold): genealogy shows `RESIN-R44` consumed, and `SUA-88` marked `missing_branch` (source MES) | Matches INJ-021's first half |
| E-702 | `data/warehouse_movements.csv` | Warehouse movement log, undated | `WM-90`: material lot `SUA-88`, batch `NCB204-B24071`, quantity 1, unit "assembly", status "issued" | Confirms `SUA-88` **was** issued to this batch per warehouse records, directly contradicting MES's `missing_branch` genealogy entry (E-701) — this is INJ-021's contradiction, resolvable via a single two-table join |
| E-703 | `data/recall_candidates.csv` | Recall-candidate register, undated | `NCS310-S26033` shares component `VIAL-V19` and equipment `FF-02` with `NCS310-S26031`; `NCS310-S26033` distribution = "not shipped"; `NCS310-S26031` distribution = "AE hospitals" | Matches INJ-058; two lots connected via **two different edge types** (shared component, shared equipment), one already shipped to hospitals — this is the artefact's strongest graph-justified case |
| E-704 | `data/icsr_cases.csv` + `data/duplicate_candidates.csv` | ICSR case register + duplicate-candidate register, undated | `PV-1001` (patient_program, product NCB-204, anaphylaxis, DE, 2026-07-20, German, patient_key `P-7X`) and `PV-1014` (call_centre, product "NCB204" [alias], breathing difficulty, DE, 2026-07-19, Arabic, patient_key `P-7X`) — **same patient_key**, similarity 0.93. `PV-1001`/`PV-1009` similarity 0.71, patient_key "unknown" for PV-1009 | Matches INJ-037; product-name variation (`NCB204` vs `NCB-204`) is already resolvable via `product_master_aliases.csv` (`05_DDD_CONTEXT_MAP.md` E-406), so identity aliasing is not, by itself, evidence a graph database is required |
| E-705 | `data/serialisation_events.csv` + `data/packaging_events.csv` | Serialization event log + packaging event log, undated | Serial `SN-10001`: `commission` event → case `CS-77`, pallet `P-88`; same serial has a later `return_scan` event with case = "unknown", pallet = "unknown". `SN-10002`: `commission` → case `CS-77`, no pallet recorded. Packaging line `PKG-3` had a `restart` event at 2026-07-28T13:22:00Z with `aggregation_rebuild = "partial"` | Matches INJ-052; the serial→case→pallet containment chain is broken for some serials, and the root cause (line restart, partial rebuild) is independently confirmed | 
| E-706 | `case/INTEGRATED_CASE.md` §3 | Case narrative | "Participants may conclude that a workflow, knowledge graph or AI component is unjustified, but must prove the decision" | The explicit mandate this artefact must satisfy in both directions (justify and reject) |

## 1. Decision criteria

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What makes a use case graph-shaped rather than join-shaped? | Fixed-depth, small-fan-out lookups across a known, small number of tables (e.g., E-701/E-702's single genealogy-to-warehouse join) do not require a graph engine. Variable-depth traversal across an unknown number of intermediate hops, multiple edge types, or transitive-closure clustering (E-703, E-704, E-705) is where a graph model earns its complexity cost. | Capstone team | E-701–E-705 |

## 2. Graph-required use cases

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Recall-scope tracing (Workflow C-adjacent, informs but does not execute) | E-703 requires following **two distinct edge types** (`shared_component`, `shared_equipment`) potentially across many lots to answer "which lots could plausibly be affected," and this fan-out could deepen transitively (lot A shares a component with B, B shares equipment with C, etc.) as more lots are added — a genuine variable-hop connected-components problem, not a fixed join. | Capstone team | E-703 |
| PV duplicate clustering beyond pairwise scores | E-704's `duplicate_candidates.csv` already contains pre-computed pairwise similarity scores (0.93, 0.71) — the *pairwise* scoring itself does not require a graph. What does: if `PV-1001~PV-1014` and `PV-1001~PV-1009` both hold, determining whether all three form one cluster (transitive closure) versus two separate pairs is a connected-components graph problem, especially once case volume grows beyond a handful of hand-checkable pairs. | Capstone team | E-704 |
| Serialization path reconstruction under partial data | E-705's serial→case→pallet containment chain is broken for at least one serial (`SN-10001`'s return_scan) and incompletely rebuilt for a whole line (`PKG-3`, "partial"). Reconstructing the most probable pallet association for an orphaned serial requires path search over the containment graph as it existed before/after the restart, not a single lookup. | Capstone team | E-705 |

## 3. Simpler alternative benchmark

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Does the flagship batch-genealogy contradiction (INJ-021) need a graph database? | No — E-701/E-702 is resolved by a single two-table join (`material_genealogy.csv` × `warehouse_movements.csv` on `material_lot` + `batch_id`). A relational query or even a pandas merge finds the contradiction (`missing_branch` in MES vs. `issued` in warehouse) without any graph traversal. This is the artefact's clearest "graph is unjustified here" finding, directly answering `case/INTEGRATED_CASE.md`'s challenge (E-706) in the negative for this specific use case. | Capstone team | E-701, E-702 |
| Does pairwise PV duplicate detection (the 0.93/0.71 scores themselves) need a graph database? | No — `duplicate_candidates.csv` shows this is already produced as a scored-pairs table; a similarity/deduplication pipeline outputting such a table needs no graph engine. Only the *transitive clustering across more than two candidates* (§2) benefits from graph algorithms, and even that can be implemented as an in-memory connected-components pass (e.g., `networkx`, or a recursive SQL CTE) over the existing pairs table — not necessarily a dedicated graph database product. | Capstone team | E-704 |
| What is the actual simpler-alternative benchmark proposed? | For all three graph-shaped use cases in §2: implement variable-hop/connected-components logic as an explicit algorithm (recursive CTE or a lightweight in-process graph library) operating directly over the existing relational/CSV sources, rather than standing up a separate graph database product. A dedicated graph database is justified only if/when data volume or query latency at production scale is shown to make this approach insufficient — not evidenced by the current (2–3 row per table) sample. | Capstone team | E-701–E-705; Gap R-701 |

## 4. Graph model and provenance

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Node types (for the three justified use cases only) | `Lot/Batch`, `Component`, `Equipment` (recall scope); `ICSRCase`, `PatientKey` (pseudonymous), `Product` (with alias resolution per `05_DDD_CONTEXT_MAP.md` E-406) (PV clustering); `Serial`, `ShippingCase`, `Pallet` (serialization). | Capstone team | E-703, E-704, E-705 |
| Edge types | `SHARED_COMPONENT`, `SHARED_EQUIPMENT` (recall); `SIMILAR_TO(score, reason)`, `SAME_PATIENT_KEY` (PV); `COMMISSIONED_INTO(case)`, `AGGREGATED_INTO(pallet)` (serialization). | Capstone team | E-703, E-704, E-705 |
| Provenance requirement | Every edge must carry source system and retrieval time — e.g., a `SHARED_EQUIPMENT` edge derived from `recall_candidates.csv` must record that this file, not a live MES query, was the source, consistent with `knowledge/AI_GXP_BOUNDARY.md` evidence expectations (`04_PRODUCT_SERVICE_BLUEPRINT.md` E-307). | Capstone team | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-307 |

## 5. Query patterns and performance

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Representative query 1 | "Find all lots within N hops of equipment `FF-02` or component `VIAL-V19`" — variable-length traversal over `SHARED_COMPONENT`/`SHARED_EQUIPMENT` edges (E-703). | Capstone team | E-703 |
| Representative query 2 | "Return the connected component containing case `PV-1001`" — connected-components over `SIMILAR_TO`/`SAME_PATIENT_KEY` edges (E-704). | Capstone team | E-704 |
| Representative query 3 | "Given orphaned serial `SN-10001`'s return_scan with no case/pallet, what is the most probable prior pallet association based on commission-time proximity and line state?" — path/probability reconstruction (E-705). | Capstone team | E-705 |
| Is performance at scale demonstrated? | No — all evidence in this pull is a 2–3 row sample per table. Whether recursive-CTE/in-process graph traversal remains adequate at full production data volume (thousands of batches, cases, serials) is not evidenced here and must not be asserted as proven. | Capstone team | Gap R-701 |

## 6. Security and temporal filtering

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Does any node type carry sensitive data requiring purpose limitation? | Yes — `PatientKey` (E-704, pseudonymous `P-7X`) is personal-data-adjacent; any traversal touching `SAME_PATIENT_KEY` edges must be scoped to the PV duplicate-detection purpose only (`03_STAKEHOLDER_DECISION_RIGHTS.md` §2 RACI), not exposed as a general-purpose graph query API. | Capstone team | E-704, `03_STAKEHOLDER_DECISION_RIGHTS.md` |
| Does temporal scoping apply to these graph queries? | Yes — `batches.csv`'s `manufacture_date` and `packaging_events.csv`'s restart `time` mean recall-scope and serialization queries must be evaluated "as of" a specific date, consistent with `07_ONTOLOGY_SEMANTIC_LAYER.md` §4's rejection of timeless "current" values; a graph traversal that ignores effective-time scoping could include lots or events that were not actually contemporaneous. | Capstone team | `07_ONTOLOGY_SEMANTIC_LAYER.md` §4 |

## 7. Decision and exit criteria

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Decision | A dedicated, separately-hosted graph database product is **not justified** at this stage. A narrow, in-process graph-shaped capability (recursive queries or a lightweight graph library over existing relational/CSV sources) is justified for exactly three use cases: recall-scope connected-components tracing (E-703), PV duplicate transitive clustering (E-704), and serialization path reconstruction (E-705). General evidence reconciliation for batch review (E-701/E-702) and label/listedness comparison (`07_ONTOLOGY_SEMANTIC_LAYER.md`) do **not** require graph modeling. | Capstone team | E-701–E-705 |
| Exit / reconsideration criteria | Reconsider a dedicated graph database only if: (a) production data volume is shown to make in-process traversal too slow for the required SLO (not yet measured, Gap R-701), or (b) additional graph-shaped use cases are identified beyond the three named here with materially different query patterns. | Capstone team | Gap R-701 |
| Does this decision reduce vendor/architecture risk? | Yes — avoiding a dedicated graph database product for use cases that don't need one directly reduces the vendor-concentration and substitutability risk already flagged in `03_STAKEHOLDER_DECISION_RIGHTS.md` §3 (Procurement favours bundled vendor; Architecture/CISO seek substitutability). | Capstone team | `03_STAKEHOLDER_DECISION_RIGHTS.md` §3 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-701 | Assumption | In-process graph traversal (recursive CTE / lightweight library) is assumed adequate at production scale; not measured against real data volume | Medium — could force a later architecture change if wrong | Capstone team | Phase 4 (Build), load-test against realistic synthetic volume | Open |
| R-702 | Gap | No confirmed upper bound on transitive recall-scope fan-out (E-703) — a real recall investigation could span far more than 2 lots | Medium-High | Capstone team | Phase 3/4, before recall-scope logic is finalized | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Batch-genealogy contradiction (E-701/E-702) resolved without a graph engine | Two-table join implementation | Not yet implemented | — | Pending |
| Recall-scope connected-components query returns both `NCS310-S26033` and `NCS310-S26031` for a query rooted at either lot | Graph-shaped query over `recall_candidates.csv` | Not yet implemented | — | Pending |
| PatientKey-scoped traversal is purpose-limited to PV workflow only | Access-control design (§6) | Not yet implemented | — | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
