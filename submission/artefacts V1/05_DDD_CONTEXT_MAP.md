# DDD Context Map

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Domain & evidence lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Architecture lead; GxP lead |
| Status | Draft — Stage 2; **provisional** (Phase 1 framing = hypothesis) |
| Related requirements / ADRs | Workshop Stage 2; Prompt 04; artefacts 01–04; `case/SOURCE_SYSTEM_FACT_PACK.md` |

## Purpose

Model business meaning and bounded contexts for the three mandatory AEGIS workflows so rules, AI (if any), RAG, and HITL have clear authority limits — without locking Stage 3 architecture.

**Artifact status:** `provisional` — prefer rules + HITL over autonomous AI until Measure baselines exist (artefact 01/02).

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `case/SOURCE_SYSTEM_FACT_PACK.md` | Case | Domain systems and known conditions | Synthetic |
| E-002 | `case/INTEGRATED_CASE.md` §4 | Case | Three mandatory workflows + operating properties | Synthetic |
| E-003 | `data/ai_use_boundaries.csv` | Boundary register | Allowed vs prohibited actions | Binding |
| E-004 | `data/decision_rights.csv` | Decision rights | Human accountability | Binding |
| E-005 | `submission/artefacts/01_BUSINESS_CASE.md` | Stage 1 | Deterministic-first capability answer | Draft |
| E-006 | `submission/artefacts/04_PRODUCT_SERVICE_BLUEPRINT.md` | Stage 1 | Intended/prohibited uses | Draft |
| E-007 | `data/RELATIONSHIP_MODEL.csv` | Package relationships | Declared FK-style links across datasets | Structural |

## 1. Ubiquitous language

| Term | Meaning in AEGIS | Ambiguity / unresolved | Owner context |
|---|---|---|---|
| Evidence item | Cited fact with source, authority, effective time, unit, uncertainty | Must not invent | All workflows |
| Readiness state | `insufficient_evidence` / `conflicted_evidence` / `ready_for_authorized_review` | Not a disposition | Batch |
| Disposition | Release/reject/reprocess/relabel/recall decision | **Out of AI authority** | Quality / QP |
| Duplicate candidate | Possible same-case cluster; not a merge | Irreversible merge prohibited | PV |
| Clock evidence | Receipt/awareness timestamps with provenance | Which clock “wins” needs rule + human | PV |
| Listedness context | Label/IB/CCDS evidence for expectedness support | Sources may conflict | PV |
| Draft option | Non-executing supply recovery option (`status=draft`) | Not a reservation | Supply |
| As-of time | Temporal applicability of the assessment | ≠ later-is-better | All |
| Abstention | Explicit non-resolution when identity/unit/time/authority incomplete | Required failure mode | All |

## 2. Bounded contexts

| Context | Type | Business owner | Decisions owned | AEGIS role |
|---|---|---|---|---|
| **Batch Evidence Reconciliation** | Core | EU QP / Quality | Review readiness only; not certification | Reconcile/cite/flag/abstain |
| **PV Case Intake Support** | Core | Global PV / Safety Physician | Final safety decisions human-only | Extract/normalize/cluster/cite |
| **Supply Options Planning** | Core | Supply Governance Board | Allocation/shipment/recall human | Draft options, no side effects |
| Manufacturing Execution | Supporting | Manufacturing VP | Throughput ops | Upstream evidence provider |
| Laboratory / LIMS | Supporting | QC | Result validity investigations | Upstream evidence; unit contracts |
| Quality System (eQMS) | Supporting | CQO | Deviation/CAPA/change | Document authority |
| Clinical Development | Supporting | Clinical Ops | Protocol/eligibility (out of AEGIS automation) | Linked evidence only |
| Regulatory / IDMP | Supporting | RA VP | Registrations/labels | Identity authority inputs |
| Privacy / Security | Generic-supporting | DPO / CISO | Entitlement, residency, tool trust | Cross-cutting controls |
| AI Platform | Generic | Digital (pilot) | Model/tool hosting | Replaceable; not decision owner |

## 3. Aggregates and invariants

| Aggregate (logical) | Invariants | AI must never |
|---|---|---|
| BatchEvidencePack | Every claim cited; conflicts preserved; `execution_status=not_executed` | Set disposition |
| PvIntakePack | Verbatim preserved; duplicate = candidate only; clocks multi-sourced | Final seriousness/causality/expectedness/reportability/signal |
| SupplyOptionsPack | Options `draft`; `no_side_effects=true`; quality holds visible | Reserve/allocate/ship/change quality status/recall |
| AuthorizationCheck | Current user/purpose/object/role/tool checked at execution | Use stale cached entitlement |

## 4. Context relationships

| Upstream → Downstream | Pattern | Notes |
|---|---|---|
| LIMS/MES/eBR/QMS → Batch Evidence | Customer/Supplier + ACL | Unit/genealogy translation via approved mappings only |
| Safety DB/affiliates/vendors → PV Intake | ACL | Product aliases; MedDRA version retained |
| Inventory/shipments/CMO → Supply Options | Customer/Supplier | Quality status from Quality context, not overwritten |
| Batch ↔ PV | Partnership (weak) | Product-quality complaint linkage as cited evidence only |
| Regulatory IDMP → all product contexts | Conformist / shared kernel (aspirational) | Today mapping_status can be ambiguous |
| AI Platform → core contexts | Published language + strict ACL | Tools signed; deny untrusted instructions |

## 5. Anti-corruption layers

| Boundary | Corruption risk | ACL rule |
|---|---|---|
| CRO lab → LIMS | Unapproved mg/L vs µg/mL (`approved=no`) | Block silent 1:1; flag/abstain |
| Supplier PDF / untrusted knowledge | Prompt injection (INJ-065) | Treat as data; never as policy |
| Tool manifest | Poisoned write/disposition fields (INJ-066) | Signed allow-list only |
| BioXen identifiers | Acquisition collision (INJ-005/008) | Alias map; no silent merge |
| AI gateway cache | Revoked user still active (INJ-067) | Re-check IAM at execution |

## 6. Ownership and change boundaries

| Change type | Owner | Gate |
|---|---|---|
| Ubiquitous language / invariants | Domain lead + accountable role | Update artefacts 05/07; tests |
| Interface unit rules | QC + Integration | Approved mapping required |
| Model/prompt/tool | Digital + Quality (if GxP-relevant) | Change control (Stage 4 artefacts) |
| Decision rights | CQO / PV Head / Supply Board | Artefact 03 |

## 7. Event semantics (minimum)

| Event | Meaning | Emitted by |
|---|---|---|
| EvidenceAssessed | Pack produced with readiness/abstentions | Batch context |
| PvIntakeAssembled | Intake pack ready for human reviews | PV context |
| SupplyOptionsDrafted | Draft options listed; no inventory mutation | Supply context |
| AuthorizationDenied | Stale/ambiguous entitlement | Security cross-cut |
| ManualModeEntered | AI-disabled continuity | Reliability |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Assumption | Three core contexts sufficient for v1 | May miss clinical/regulatory deep flows | Domain | Stage 3 ADR | Open |
| R-002 | Gap | Full event storm across 84 injects not completed | Incomplete integration design | Domain | Stage 3 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Rules vs AI vs HITL bounded | §2–3 | Contract negatives | E-003, E-004 | Draft |
| No technical-layer domain | Contexts are business | Review | This artefact | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| GxP lead | Reviewer | Disposition outside Batch context | Confirmed invariant | 2026-08-07 |
