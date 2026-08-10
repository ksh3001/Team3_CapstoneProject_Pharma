# Knowledge Graph Decision

> Phase 2. Climb the meaning ladder only with evidence. Citation ≠ provenance.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Domain–evidence + Architecture |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Product–value; GxP |
| Status | Draft |
| Related requirements / ADRs | RUB-06; DEC-020 (this decision) |

## Purpose

Decide whether a knowledge graph is necessary for the fail-closed evidence-reconciliation assist, versus simpler relational/deterministic alternatives — with an explicit revisit trigger.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | `data/RELATIONSHIP_MODEL.csv` | Explicit relationship rules already encoded |
| E-002 | `submission/evidence/anchor_conflict_register.md` | Genealogy, duplicates, recall multi-hop pressure |
| E-003 | `data/material_genealogy.csv` / recall themes | Multi-hop lot/component questions |
| E-004 | `data/duplicate_candidates.csv` | Pairwise similarity already tabular |
| E-005 | `data-and-knowledge` skill | Meaning ladder; GraphRAG only when relationships force it |
| E-006 | Phase 1 DEC-010 | Narrowest viable assist; non-AI first |

## 1. Decision criteria

| Criterion | Weight | Observation |
|---|---|---|
| Multi-hop relationship questions dominate? | High | Partial: genealogy/recall/serialization — yes; many injects are pairwise/tabular |
| Entity resolution required before aggregate? | High | Yes for products/cases/lots — solvable with master-data + mapping tables |
| Provenance path required? | High | Yes — solvable with evidence_item contracts + lineage tables |
| Team/time for graph ops? | High | Capstone 40h — graph platform is heavy |
| Offline deterministic mode? | High | Relational + rules easier to freeze offline |
| Defence burden | Med | Must justify KG if chosen; simpler alternative must be benchmarked |

## 2. Graph-required use cases (candidates)

| Use case | Why graph-shaped | Can simpler approach work for v1? |
|---|---|---|
| Material genealogy / recall scope | Multi-hop lot–component–equipment–shipment | Yes — recursive SQL/CTE or precomputed closure table on vignette scale |
| ICSR duplicate clusters | Graph of candidate edges | Yes — pairwise table already exists; do not need property graph |
| Knowledge supersession chains | Doc–supersedes–doc | Yes — catalog columns supersedes/effective/trust |
| Serialization aggregation breaks | Hierarchy case–pallet | Yes — event tables + gap flags |

## 3. Simpler alternative benchmark (chosen for v1)

**Alternative S1 — Relational evidence mesh + deterministic detectors**

- Use CSVs + `RELATIONSHIP_MODEL` as the contract for joins  
- Emit `evidence_item` provenance for every material fact  
- Detectors for unit/authority/time/trust/duplicate/quarantine conflicts  
- Optional later: materialized “edge list” export for genealogy without a graph DB  

**Benchmark claim:** For vignette-scale data and three workflows, S1 answers CQ-01…CQ-06 without a graph engine, preserves offline determinism, and matches DEC-010 narrowest path.

## 4. Graph model and provenance (only if revisited)

If revisit triggers fire, minimal graph:

- Nodes: Product, Batch, Lot, Material, Shipment, Case, Document, User, Spec  
- Edges: CONTAINS, TESTED_BY, SHIPPED_AS, DUPLICATE_CANDIDATE_OF, SUPERSEDES, CITES (with effective time on edges)  
- Provenance assembler still mandatory — graph is not a substitute for authority/as-of  

## 5. Decision

| Field | Entry |
|---|---|
| **Decision** | **Do not implement a knowledge-graph database for the capstone POC (v1).** Use relational evidence mesh + semantic glossary (artefact 07) + deterministic conflict detectors. |
| **Options considered** | (A) Neo4j/Neptune-style KG (B) Hybrid GraphRAG (C) Relational mesh **← selected** (D) Pure vector RAG over docs |
| **Rationale** | Relationships that matter are already expressible via RELATIONSHIP_MODEL and small vignettes; pure RAG fails provenance/trust; full KG adds ops cost without unlocking mandatory workflow contracts |
| **Rejected** | Pure RAG default (cannot do units/trust/authority); immediate KG platform (over-scope) |
| **Revisit triggers** | (1) Recall/genealogy questions require interactive multi-hop beyond ~2 joins on real volumes (2) Entity resolution across >N source systems unmanageable in tables (3) Inspector demands path queries S1 cannot produce reproducibly |

## 6. Consequences

| Positive | Negative / residual |
|---|---|
| Faster deterministic offline POC | May need migration note if graph added later |
| Clear provenance via schemas | Multi-hop UX less “native” |
| Aligns non-AI-first sequencing | Must still model edges logically in docs/tests |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-001 | Assumption | Vignette join depth ≤2 for demo anchors | Accepted |
| R-002 | Risk | Stakeholders equate “AI” with vector RAG | Mitigate in defence |
| R-003 | Gap | No formal ADR number yet — DEC-020 stands in until Phase 3 ADR register | Open |

## Traceability and acceptance

| Claim | Result |
|---|---|
| KG decision with simpler benchmark | Done |
| Revisit triggers quantified qualitatively | Done |
| Aligns meaning ladder | Done |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Pending | Architecture lead | — |
