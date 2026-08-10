# Knowledge Graph Decision

> Team3 Phase 2 artefact (template 08). Formalizes **D-004**.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Architecture / Domain |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Product; Evaluation; GxP |
| Status | **Decision: Do not implement a knowledge graph for POC** |
| Related | D-004; PRD out-of-scope (mandatory KG); template 07 semantic layer; inject register |

## Purpose

Decide whether a graph database / RDF knowledge graph is required for AEGIS Evidence Assist, versus a relational/register + ACL approach. Completion: criteria scored; alternatives compared; exit criteria for revisit.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-KG-01 | `00_ASSUMPTIONS_DECISION_LOG` D-004 | KG not assumed |
| E-KG-02 | `artefacts/prompts/03_prd/scope_in_out.md` | Mandatory KG out of scope |
| E-KG-03 | `inject_evidence_register.csv` | 84 injects manageable as register rows |
| E-KG-04 | Working POC (`submission/src`) | CSV ACL + cite/flag meets AC hard controls |
| E-KG-05 | `no_ai_baselines.csv` | MDM/rules claim value without graph |

## 1. Decision criteria

| Criterion | Weight | Score (1–5) | Notes |
|---|---|---|---|
| Multi-hop graph queries required for hard gates? | High | **2** | Gates need AuthZ, unit conflict, quarantine, doc trust — not graph traversal |
| Measured conflict volume needs graph analytics? | High | **1** | Ops volume Unknown (`hypothesis`) |
| Offline deterministic / AI-disabled fit | High | **5** for register | Graph stack adds moving parts |
| Provenance + dual-cite support | High | **4** for Evidence Items | Achieved without KG |
| Time-to-demo / Lean waste | Med | **5** for register | Avoid Overproduction |
| Future master-data MDM programme | Med | **3** | Org MDM ≠ product KG |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| KG mandatory now? | **No** | Architecture | This artefact |

## 2. Graph-required use cases

| Candidate use case | Graph needed? | POC alternative |
|---|---|---|
| Batch↔lab↔deviation multi-hop | Nice-to-have | SQL/CSV joins via ACL by batch_id |
| PV duplicate cluster networks | Maybe later | Exact/strong_key; fuzzy blocked |
| Knowledge concept graph | No for authority filter | Catalog status/trust columns |
| Enterprise ontology publishing | Out of scope | Template 07 glossary |

No hard-gate use case **requires** a graph today.

## 3. Simpler alternative benchmark

| Alternative | Pros | Cons |
|---|---|---|
| **Evidence register + CSV ACL (chosen)** | Deterministic, auditable, offline, matches contracts | Manual joins; not enterprise MDM |
| Relational warehouse | Stronger joins | Out of POC scope |
| Vector RAG over knowledge | Fast search | Equal-trust risk; token waste; out of assessed default |
| Property graph / RDF | Flexible relations | Unjustified complexity; residency/ops burden |

**Benchmark:** POC already passes AuthZ/unit/doc/supply ACs without a graph.

## 4. Graph model and provenance

If revisited later, any graph **must** carry: source, authority, effective_at, integrity hash, as_of edge filters, and **no** write-back to SoRs. Not designed now.

## 5. Query patterns and performance

Current patterns: point lookup by batch_id/case_id/user/doc_id; scan ≤32 knowledge docs; evaluate fixture suite. No path-query SLO justifying Neo4j/RDF.

## 6. Security and temporal filtering

Register/ACL approach enforces IAM>cache and document quarantine at read time. A graph would need equivalent edge-level authz — extra attack surface without benefit under scarcity.

## 7. Decision and exit criteria

**Decision (D-004 confirmed / D-016):** **Do not build a knowledge graph** for the assessed POC. Use `inject_evidence_register` + CSV ACL + semantic glossary (template 07).

**Revisit KG only if all true:**
1. Measured multi-hop query/conflict needs documented (exit `hypothesis` on this point);  
2. Register/ACL proven insufficient on named scenarios;  
3. Offline/AI-disabled continuity preserved;  
4. Security review of graph authz completed;  
5. PRD scope change approved (remove “mandatory KG” exclusion or add optional KG).

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Exit | No KG in POC; register is SoT for inject assessment | Architecture | E-KG-04; this §7 |

## Risks, assumptions and unresolved gaps

| ID | Description | Status |
|---|---|---|
| R-KG-01 | Future MDM may still need graph — separate programme | Deferred |
| R-KG-02 | Register enrichment incomplete (many UNASSESSED) | Open — stewardship |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| KG not required for hard gates | AC suite green without KG | Pass |
| Aligns PRD out-of-scope | scope_in_out | Pass |

## Review record

| Reviewer | Role | Finding | Date |
|---|---|---|---|
| Team3 Architecture | Owner | Accept no-KG decision | 2026-08-07 |
