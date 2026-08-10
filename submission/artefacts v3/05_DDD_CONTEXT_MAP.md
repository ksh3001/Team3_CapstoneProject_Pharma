# DDD Context Map

> Phase 2. Domain language and boundaries only — no services/APIs/RAG/agents as domain concepts. Operational exceptions preserved, not resolved.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Domain–evidence lead (named TBD) |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP lead; Product–value lead |
| Status | Draft |
| Related requirements / ADRs | RUB-04, RUB-05; DEC-010; inject register |

## Purpose

Define ubiquitous language and bounded contexts for evidence-reconciliation assist so later architecture cannot absorb regulated decision authority or “clean away” challenge contradictions.

**Completion:** Contexts include Evidence & Provenance and Decision Authority; context relationships defended; exceptions listed as gaps/invariants.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `submission/evidence/inject_evidence_register.csv` | Team register from package coverage | 84 injects mapped | Derived |
| E-002 | `data/decision_rights.csv` | Decision rights | Human accountability | Binding |
| E-003 | `data/ai_use_boundaries.csv` | AI boundaries | Advisory limits | Binding |
| E-004 | `data/RELATIONSHIP_MODEL.csv` | Declared FK/exceptions | Required links + deliberate gaps | Includes declared_exception |
| E-005 | `submission/evidence/anchor_conflict_register.md` | Anchor analysis | Unit/duplicate/cold-chain/state conflicts | Interpretive on facts |
| E-006 | `case/INTEGRATED_CASE.md` | Case | Domain narrative D01–D13 | Narrative |

## 1. Ubiquitous language

| term | definition_in_this_case | bounded_context | owner_role | ambiguity_risk | must_not_be_used_loosely |
|---|---|---|---|---|---|
| evidence-complete package | Structured cited facts + conflicts + gaps + abstentions ready for human review | Evidence & Provenance | Domain + GxP | Confused with “batch released” | Yes — not a disposition |
| readiness_state | insufficient_evidence / conflicted_evidence / ready_for_authorized_review | Batch Review Readiness | EU QP (consumer) | Treated as release | Yes |
| batch disposition | Release/reject/reprocess/relabel/recall decision | Decision Authority | EU QP | AI “recommends release” | Yes — AI prohibited |
| ICSR / case | Safety case identity under investigation; may have duplicates | PV Case Intake Support | Safety Physician | Merge ≠ same case | Yes |
| reportability | Final regulatory reporting decision | Decision Authority | Safety Physician | AI auto-reportable | Yes — AI prohibited |
| draft option | Non-executing supply alternative | Supply Option Planning | Supply Governance Board | Treated as reservation | Yes |
| as-of time | Temporal applicability for authority/doc/result | Evidence & Provenance | Domain | Source vs receipt time collapse | Yes |
| authority | Governing source for a fact at as-of | Evidence & Provenance | Domain + GxP | Newest file wins | Yes |
| unit conflict | Incompatible or unapproved unit/spec pairing | Master Data / Identity | Domain | Silent convert | Yes |
| untrusted document | Catalog trust≠approved; not executable instruction | Evidence & Provenance | Security | Equal-trust RAG | Yes |

## 2. Bounded contexts

| Context | Purpose | Decisions owned | Decisions NOT owned | Safety risk if misunderstood |
|---|---|---|---|---|
| **Evidence & Provenance** | Cite, hash, authority, as-of, lineage | Whether a fact is citable | Regulated disposition | Fabricated completeness |
| **Decision Authority & Accountability** | Name human owners; deny AI authority | Who may decide | How AI “helps decide” regulated acts | Authority laundering |
| **Batch Review Readiness** | Package batch evidence for QP | Readiness packaging states | Batch certification/disposition | False ready_for_review |
| **PV Case Intake Support** | Intake/cluster/clock/listedness context | Support artefacts + required_reviews | Final seriousness/causality/reportability/signal | Irreversible merge / wrong clock |
| **Supply Option Planning** | Draft shortage/cold-chain options | Draft options + constraints | Reserve/allocate/ship/recall | Side effects |
| **Master Data / Identity** | Product/substance/batch/case identifiers & units | Conflict surfacing | Silent golden-record merge | Double-count / wrong product |
| **Clinical Trial Integrity** | Protocol/eligibility/consent context | Abstention on ambiguity | Eligibility determination by AI | Unblinding / wrong protocol |
| **Quality Systems / DI** | Deviations, CAPA, audit trail, validation state | Flag DI breaks | Closing CAPA / changing validation label | Hidden DI failure |
| **Regulatory Information** | IDMP/labels/commitments/eCTD completeness | Completeness gaps | Variation classification alone | Missing sequence treated as OK |
| **Security & Entitlements** | AuthZ freshness, tool trust | Deny/allow assist | Business disposition | Stale allow |
| **Privacy & Cross-border** | Purpose, residency, DSR vs hold | Flag conflicts | Delete GxP-required records | Unlawful delete/export |

## 3. Aggregates and invariants

| ID | Statement | Context | Human owner | Failure risk |
|---|---|---|---|---|
| INV-01 | Material facts in outputs MUST cite source, authority, as-of/retrieved, integrity | Evidence & Provenance | Domain | Unauditable assist |
| INV-02 | Unapproved unit mappings MUST NOT be applied silently | Master Data / Identity | GxP | Wrong OOS/pass |
| INV-03 | AI MUST NOT emit batch disposition or execute disposition tools | Decision Authority | EU QP | Illegal release assist |
| INV-04 | Duplicate candidates MUST remain reversible proposals | PV Case Intake Support | Safety Physician | Wrong case merge |
| INV-05 | Supply options MUST remain draft with no_side_effects | Supply Option Planning | Supply Board | Ghost reservations |
| INV-06 | Untrusted/superseded/draft knowledge MUST NOT be instruction-eligible | Evidence & Provenance | Security | Prompt injection |
| INV-07 | Declared relationship exceptions remain gaps, not defects to delete | Evidence & Provenance | Domain | False completeness |
| INV-08 | Stale/revoked entitlements deny assist | Security & Entitlements | Security | Unauthorized access |

## 4. Context relationships

| Upstream → Downstream | Type | Defence (why this boundary) |
|---|---|---|
| Master Data → Batch / PV / Supply | published language + ACL | Prevent source identifiers distorting domain meaning |
| Evidence & Provenance → all workflow contexts | shared kernel (citation model) | One provenance grammar |
| Workflow contexts → Decision Authority | upstream/downstream | Workflows recommend packages; humans decide |
| Security & Entitlements → all | partnership | Cross-cutting deny-by-default |
| Privacy → PV / Clinical | ACL | Purpose limitation vs GxP retention tension preserved |
| Quality Systems / DI → Batch | upstream | DI breaks block “ready” packaging |

## 5. Domain events (selected)

| Domain event | Command/activity | Actor | Context | Exception |
|---|---|---|---|---|
| LabResultReceived | Ingest LIMS result | Lab interface | Batch Review Readiness | Unit mismatch (LR-88) |
| DuplicateClusterProposed | Cluster ICSRs | PV assist | PV Case Intake Support | Must not auto-merge |
| ColdChainExcursionFlagged | Assess shipment | Supply assist | Supply Option Planning | Logger association dispute |
| EntitlementRevoked | IAM revoke | IAM | Security | Cache still active |
| KnowledgeDocumentRetrieved | Retrieve SOP | Assist | Evidence & Provenance | Untrusted content |

## 6. Anti-corruption needs

| Source smell | Translation need |
|---|---|
| LIMS v1/v2 unit semantics | Explicit mapping approval status; never 1:1 assume |
| Equal-trust markdown knowledge | Filter by knowledge_catalog trust/effective |
| Agent checkpoint resume | Ignore draft reservation side effects in assessed mode |
| KPI language (throughput vs RFT) | Semantic layer / not domain merge (see artefact 07) |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-001 | Gap | Full event storm for all 84 injects not expanded here | Incomplete domain model | Domain | Open — register covers injects |
| R-002 | Assumption | Eleven contexts sufficient for v1 | Over/under partition | Domain | Accepted for Phase 2 |
| R-003 | Risk | Teams use table names as domain language | Brittle design | Architecture | Mitigate via language table |

## Traceability and acceptance

| Claim | Evidence path | Result |
|---|---|---|
| 84 injects registered | `inject_evidence_register.csv` | Done |
| Exceptions preserved | `anchor_conflict_register.md` + RELATIONSHIP_MODEL | Done |
| Decision authority separated | §2 Decision Authority context | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | GxP lead | — | — | — |
