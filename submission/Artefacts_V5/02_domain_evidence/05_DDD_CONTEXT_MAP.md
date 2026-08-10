# DDD Context Map

> Team3 Phase 2 artefact. Aligns to capstone template 05; reuses provisional Prompt 04 domain model.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Domain / Architecture |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | GxP lead; Product lead |
| Status | Phase 2 complete — **provisional** (`hypothesis`) |
| Related requirements / ADRs | RUB-04…06; D-004, D-005, D-006; Prompt 04 `artefacts/prompts/04_ddd/` |

## Purpose

Define ubiquitous language, bounded contexts, and ownership so Phase 3+ architecture cannot smash Quality / PV / Supply accountability. Completion: contexts mapped for Research→Supply estate; AEGIS assist contexts separated from human decision contexts; ACL required.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-DDD-01 | `case/SOURCE_SYSTEM_FACT_PACK.md` | Challenge case | Brownfield SoRs: LIMS, MES, EBR, QMS, Safety, inventory, IAM, docs | Narrative |
| E-DDD-02 | `artefacts/prompts/04_ddd/domain_model.md` | Team3 provisional | BC-BATCH/PV/SUPPLY/AUTHZ/DOCAPPLY/MEASURE | Prompt-track |
| E-DDD-03 | `data/decision_rights.csv` | Decision rights | AI none / draft only | Binding |
| E-DDD-04 | `data/ai_use_boundaries.csv` | AI boundaries | Allowed/prohibited per workflow | Binding |
| E-DDD-05 | `inject_evidence_register.csv` | Phase 2 | 84 injects spanning D01–D12 | Initial assessment |

## 1. Ubiquitous language

| Term | Meaning | Must not mean |
|---|---|---|
| Evidence Item | Cited fact with source, authority, effective_at, integrity | Model instruction |
| Applicable Document | Approved/trusted policy at as_of + jurisdiction | Any knowledge MD |
| Conflict | Material disagreement (identity/unit/time/authority/fact) | Silent fix |
| Abstention | Explicit non-resolution | Empty/invented consensus |
| Review Readiness | Input to human review | Batch disposition/release |
| Supply Option | Draft plan, `no_side_effects` | Reservation/allocation |
| Current Entitlement | IAM-authoritative grant | Cache alone |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Glossary locked? | Provisional; unresolved clocks/validation terms listed in Prompt 04 | Domain | E-DDD-02 |

## 2. Bounded contexts

### Enterprise domains (case estate)

| Domain | Role vs AEGIS |
|---|---|
| Research / Preclinical | Upstream facts (generic) |
| Clinical | Upstream; eligibility **out of scope** |
| Manufacturing / MES-EBR | Upstream SoR via ACL |
| Quality / QP | Owns certification **outside** assist; operates BC-BATCH assist |
| Safety / PV | Owns finals **outside**; operates BC-PV assist |
| Regulatory | Constraint/consumer |
| Supply | Owns allocation **outside**; operates BC-SUPPLY assist |

### AEGIS assist contexts

| Context | Owner | Owns | Must not own |
|---|---|---|---|
| BC-BATCH | Quality / QP support | Cite/flag/abstain; readiness input | Disposition |
| BC-PV | PV / Safety | Intake packet; duplicate **candidates**; clocks | Final safety calls |
| BC-SUPPLY | Supply planning | Draft options | Reserve/allocate/ship/status/recall |
| BC-AUTHZ | Security | Allow/deny at execution | Business reconciliation |
| BC-DOCAPPLY | Document control | Applicable vs quarantined docs | Treating untrusted as SOP |
| BC-MEASURE | Evaluation | Gates/metrics | Mutating packs to pass |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| One Pharma-AI context? | **No** — would erase decision rights | Architecture | E-DDD-03 |

## 3. Aggregates and invariants

| Aggregate | Invariants |
|---|---|
| Evidence Pack (batch) | No disposition fields; conflicts dual-cited; readiness ≠ release |
| ICSR Intake Packet | No final seriousness/causality/reportability; no irreversible merge |
| Supply Option Set | `no_side_effects=true`; quarantine not available |
| AuthorizationDecision | IAM revoke beats cache |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Invariants source | ai_use_boundaries + contracts + DoD | GxP | E-DDD-04 |

## 4. Context relationships

| From | To | Pattern |
|---|---|---|
| Upstream SoRs | BC-BATCH/PV/SUPPLY | Anti-corruption layer |
| BC-AUTHZ | Core three | Upstream / conformist |
| BC-DOCAPPLY | Core three | Published language |
| Core three | External QP/Safety/Supply Board | Separate contexts (OHS) |
| Core three | BC-MEASURE | Customer/Supplier (read-only consume) |

## 5. Anti-corruption layers

- Map LIMS/MES/Safety field slang → Evidence Item; never silent unit convert (LR-88).  
- Knowledge catalog status/trust → Applicable Document filter.  
- IAM entitlements authoritative over gateway cache.

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| ACL required? | **Yes** — unit/mapping/auth conflicts observed | Architecture | E-DDD-05; lab/interface CSVs |

## 6. Ownership and change boundaries

| Change type | Owner |
|---|---|
| Ubiquitous language / POL-* | Domain + GxP |
| SoR schema | Upstream system owners |
| Assist contracts | Architecture + Evaluation |
| Decision rights | CQO / Safety / Supply Board |

## 7. Event semantics

| Event | Meaning |
|---|---|
| as_of query | Temporal applicability instant |
| Authorization checked | Purpose-bound decision recorded |
| Conflict raised | Dual-cite; HITL |
| Pack emitted | Assist output; not a regulated decision |
| Option drafted | Non-executing proposal |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-P2-01 | Gap | Clock dictionary Incomplete | Dual-cite interim | Data stewardship | Open |
| R-P2-02 | Gap | AI-EVIDENCE validation triple-state | No validated DSS claim | GxP | Open |
| R-P2-03 | Assumption | Enterprise domains collapse to ACL upstream for POC | Narrower than full org map | Domain | Accepted POC |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Contexts separate from certification/PV-final/allocate | BC map + PRD out-of-scope | AC-021/030/041 | This artefact; Prompt 04 | Pass (design) |
| ACL for brownfield | ADR-008 intent | AC-020 unit conflict | lab_results; interface_mappings | Pass (fixture) |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Domain | Owner | Provisional under hypothesis | Accept for Phase 2 checkpoint | 2026-08-07 |
