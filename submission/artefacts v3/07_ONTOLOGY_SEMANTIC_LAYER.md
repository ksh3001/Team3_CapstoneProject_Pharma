# Ontology and Semantic Layer

> Phase 2. Meaning ladder: define concepts/metrics before assuming RAG/KG.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Domain–evidence lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Product–value; Architecture |
| Status | Draft |
| Related requirements / ADRs | RUB-06; artefacts 05–06, 08 |

## Purpose

Answer competency questions with shared concepts, identifier rules, and temporal/jurisdictional semantics so KPI and product language stop colliding silently.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | `data/kpi_conflicts.csv` | Conflicting functional KPIs |
| E-002 | `data/portfolio_products.csv` | Product identities |
| E-003 | `data/controlled_vocabularies.csv` / terminology_versions | Terminology drift risk |
| E-004 | `data/timezone_rules.csv` | Clock semantics |
| E-005 | artefact 05 language table | Ubiquitous language |
| E-006 | `data/listedness_sources.csv` themes (INJ-040) | Multi-authority expectedness |

## 1. Competency questions

| ID | Question | Route bias |
|---|---|---|
| CQ-01 | Is batch NCB204-B24071 evidence-complete for authorized review as-of T? | Rules + structured evidence |
| CQ-02 | Which lab results conflict on units/authority for a batch? | Structured + mapping approval |
| CQ-03 | Which ICSR cases are duplicate *candidates* without merging? | Relationship/cluster |
| CQ-04 | What clocks exist for awareness date on a case? | Multi-record temporal |
| CQ-05 | Which inventory is usable vs quarantined for draft options? | Quality status filter |
| CQ-06 | Which knowledge docs are instruction-eligible at as-of? | Catalog trust/effective |
| CQ-07 | What is “right first time” vs “schedule adherence” in this programme? | Semantic/metrics layer |

## 2. Core concepts and relations

| Concept | Relates to | Notes |
|---|---|---|
| Product | Batch, Label, Authorisation, Shipment | product_id vs local aliases |
| Batch | LabResult, Genealogy, Deviation, ReleasePacket | status ≠ disposition |
| LabResult | Unit, Spec, InterfaceMapping, OOSInvestigation | status enums disagree across tools |
| SafetyCase | AdverseEvent, Receipt, DuplicateCandidate, ListednessSource | clocks plural |
| Shipment | Logger, TradeDocument, InventoryLot | association may be disputed |
| KnowledgeDocument | Authority, EffectiveDate, Trust, Supersedes | instruction eligibility |
| Entitlement | User, Purpose, CacheState | checked_at required |
| Metric | Function, Target | not interchangeable across functions |

## 3. Identifiers and aliases

| Identity class | Rule | Conflict example |
|---|---|---|
| batch_id | Stable in batches.csv; complaints may use lot synonym | product_complaints.lot → batch_id |
| case_id | Do not collapse on similarity score alone | PV-1001 cluster |
| product_id | Portfolio master; IDMP mappings may diverge | INJ-045 |
| logger | May be missing readings | LG-42 |
| model_id | Registry hash vs deployed hash | INJ-070 |

## 4. Temporal and jurisdictional semantics

| Dimension | Rule |
|---|---|
| Source time vs receipt time | Preserve both; do not pick one silently (PV clocks) |
| Document effective | Only approved docs with effective≤as-of are instruction-eligible |
| Timezone | Apply timezone_rules; wearable/local skew is conflict (INJ-018) |
| Jurisdiction | Listedness/labels/market authorisations are market-scoped |
| Local vs global SOP | DE local WI vs global policy — both may apply; record conflict |

## 5. Semantic layer (metrics-as-meaning)

| Metric name | Definition for AEGIS | Owner lens | Must not mean |
|---|---|---|---|
| release_lead_time | Board BR-01 end-to-end release lead time | Board | AI auto-release latency |
| right_first_time | Quality KPI 96% | Quality | Evidence package FPY (related but distinct) |
| schedule_adherence | Manufacturing 98% | Manufacturing | Evidence completeness |
| expedited_on_time | Safety 100% | Safety | Final reportability correctness |
| evidence_package_FPY | % packages needing no return for missing provenance/authority/unit/time | Evaluation (defined Phase 1) | Batch released |
| cost_per_evidence_complete_decision | Human + infra (+tokens if any) per successful package | FinOps | Token cost alone |

**Decision:** Implement a **lightweight semantic glossary + metric definitions** in submission (this artefact + code enums later). Full dbt/MetricFlow platform **out of scope** for capstone POC.

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-001 | Gap | controlled_vocabularies not fully enumerated here | Open |
| R-002 | Assumption | CQ set covers three workflows + trust | Accepted for v1 |

## Traceability and acceptance

| Claim | Result |
|---|---|
| KPI collisions named | Done (E-001) |
| Temporal/jurisdiction rules stated | Done |
| Semantic layer scoped lightly | Done — see artefact 08 for KG |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Pending | Domain lead | — |
