# Knowledge Graph Decision

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Domain & evidence lead + Architecture lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Product / value lead (no-AI challenger) |
| Status | Draft — Stage 2 decision |
| Related requirements / ADRs | Artefacts 01, 05–07; INJ-003; PACKAGE_SCOPE freedom (KG not mandatory) |

## Purpose

Decide whether a knowledge graph is necessary for AEGIS v1, with an explicit simpler alternative benchmark. This is a **capability data-model decision**, not a vendor selection.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `PACKAGE_SCOPE_AND_ASSUMPTIONS.md` | Scope | KG/LLM not mandatory unless justified | Binding |
| E-002 | `data/no_ai_baselines.csv` | Estimates | Large non-AI value from master-data/rules | Estimated % |
| E-003 | `submission/artefacts/01_BUSINESS_CASE.md` | Stage 1 | Deterministic-first answer | Draft |
| E-004 | `data/RELATIONSHIP_MODEL.csv` | Package | 55 declared relational links | Already joinable |
| E-005 | `data/inject_evidence_map.csv` | Package | Multi-hop injects (genealogy, recall) exist | May stress joins |
| E-006 | `submission/artefacts/07_ONTOLOGY_SEMANTIC_LAYER.md` | Stage 2 | Competency questions CQ-1–6 | Draft |
| E-007 | `evaluation/contracts/*.schema.json` | Package | Structured outputs without graph | Executable today |

## 1. Decision criteria

| Criterion | Weighting question | v1 assessment |
|---|---|---|
| C1 Multi-hop necessity | Do required queries need variable-depth graph traversal? | Partial — genealogy/recall (INJ-021/058) are multi-hop but bounded |
| C2 Provenance first-class | Can evidence provenance be tables + citations? | Yes — matches contracts |
| C3 Offline / deterministic | Can assessment mode run without graph infra? | Required — prefer yes |
| C4 Time-to-value vs Measure | Does KG delay Measure-first path? | Yes — risk |
| C5 Justify vs simpler store | Does graph beat documented joins on CQs? | Not yet evidenced |
| C6 Security/temporal filter | Can filters be applied in SQL/rules? | Yes for v1 |

## 2. Graph-required use cases

| Use case | Graph-helpful? | v1 approach |
|---|---|---|
| Batch evidence pack assembly | Low | Relational joins + evidence register |
| PV duplicate candidates | Low–med | Explicit duplicate_candidates + alias rules |
| Supply constraints | Low | Tabular constraints |
| Recall-scope / shared components | Med–high | Bounded recursive CTE / precomputed closure **candidate** — not mandatory graph DB |
| Enterprise semantic search over 32 knowledge docs | Med | Catalog filters by authority/effective/trust first; vector optional later |

## 3. Simpler alternative benchmark (required)

| Alternative | How it answers CQs | Pros | Cons |
|---|---|---|---|
| **A. Relational/CSV joins + semantic rules (SELECTED for v1)** | Use RELATIONSHIP_MODEL + artefact 07 rules + deterministic engines | Offline; testable; aligns contracts; fastest Measure path | Multi-hop recall awkward |
| B. Document store + evidence index | Pack-centric JSON with citations | Simple provenance | Weak cross-object queries |
| C. Property graph DB | Native multi-hop | Flexible traversal | Ops/validation burden; not justified yet |
| D. Vector KG hybrid | Semantic retrieval + graph | Rich | Highest complexity; token/FinOps risk |

**Benchmark statement:** For PUB-01–08 style assessments, Alternative A can produce schema-valid packs without a graph. Graph (C) is justified only if Measure shows Alternative A cannot complete recall/genealogy competency within accuracy/time budgets.

## 4. Graph model and provenance

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| v1 model | No production KG schema | Architecture | This decision |
| If later graph | Nodes = Product/Batch/Case/Lot/Doc; edges typed; every edge carries source/authority/as-of | Domain | Revisit trigger §7 |
| Provenance now | EvidenceItem array on each workflow response | Build | contracts |

## 5. Query patterns and performance

| Pattern | v1 implementation |
|---|---|
| Point lookup by ID | CSV/keyed store |
| 1–2 hop joins | Explicit joins per RELATIONSHIP_MODEL |
| Bounded genealogy expansion | Depth-limited recursive query or precomputed edges table if needed |
| Policy applicability | knowledge_catalog filter — not graph path query |

## 6. Security and temporal filtering

| Control | v1 |
|---|---|
| Entitlement | Pre-query authz check |
| Trust | Exclude untrusted docs from instruction path |
| Temporal | as-of predicates in rules |
| Exfiltration | Purpose limitation on query surface |

## 7. Decision and exit criteria

| Decision | **Defer knowledge graph for AEGIS v1.** Implement semantic layer + relational/deterministic reconciliation. |
|---|---|
| Owner | Architecture + Domain; challenged by Product (no-AI) |
| Exit / revisit triggers | (1) Genealogy/recall CQs fail Measure accuracy with joins; (2) Inspection evidence assembly exceeds time budget due to join complexity; (3) Sponsors accept graph validation cost |
| Non-decision | No Neo4j/vendor lock; no KG implied by using the word “ontology” in artefact 07 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Risk | Underestimating recall multi-hop | Late pivot to graph | Domain | After PUB recall-style fixtures | Open |
| R-002 | Assumption | RELATIONSHIP_MODEL + rules cover PUB-01–08 | May need edge table | Architecture | Stage 5 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Simpler alternative documented | §3 | Review Checkpoint C2 | This artefact | Draft |
| KG not mandatory path | §7 | Offline POC without graph | E-001, E-007 | Pending Stage 5 |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Product lead | No-AI challenger | Must not default to KG | Deferred KG; Alt A selected | 2026-08-07 |
