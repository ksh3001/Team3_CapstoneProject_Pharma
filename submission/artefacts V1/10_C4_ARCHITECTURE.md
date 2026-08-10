# C4 Architecture

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Architecture / integration lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Domain lead; GxP lead; Evaluation lead |
| Status | Draft — Workshop Stage 3; **provisional** (no KG; deterministic core) |
| Related requirements / ADRs | Artefacts 05–09; ADR-001–010; FR-001–005 |

## Purpose

Describe the minimum architecture that hosts the three fail-closed workflows offline, maps to DDD bounded contexts, and makes prohibited write paths structurally impossible.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `submission/artefacts/05_DDD_CONTEXT_MAP.md` | Stage 2 | Core contexts + ACL | Draft |
| E-002 | `submission/artefacts/08_KNOWLEDGE_GRAPH_DECISION.md` | Stage 2 | KG deferred; relational v1 | Draft |
| E-003 | `submission/artefacts/09_REQUIREMENTS_TRACEABILITY.md` | Stage 2 | FR/AC | Draft |
| E-004 | `evaluation/contracts/*.schema.json` | Package | Fail-closed I/O | Executable |
| E-005 | `case/SOURCE_SYSTEM_FACT_PACK.md` | Case | Brownfield systems | Synthetic |
| E-006 | `data/continuity_requirements.csv` | Continuity | Manual mode required | Binding |

## 1. System context

| Person / system | Interaction with AEGIS |
|---|---|
| EU QP / batch reviewer | Requests batch evidence pack; reviews readiness; certifies outside AEGIS |
| Safety intake / physician | Requests PV intake pack; makes final PV decisions outside AEGIS |
| Supply planner / governance | Requests draft options; executes allocation/shipment outside AEGIS |
| LIMS / MES / eBR / QMS / Safety DB / Supply systems | Read-only evidence sources (brownfield) |
| IAM | Entitlement source of truth at execution |
| Knowledge catalog / source docs | Policy/evidence; trust-filtered |
| AEGIS | Produces cited non-executing assessments only |

## 2. Container view

| Container | Responsibility | Tech posture (v1) |
|---|---|---|
| **AEGIS API / CLI** | Accept request (workflow, ids, purpose, as-of, user); return schema-valid JSON | Local Python stdlib-capable |
| **Authorization Gateway** | Check IAM + purpose + object + tool allow-list; deny stale cache | Deterministic rules |
| **Evidence Store Adapter** | Read challenge `data/` (+ optional submission seed); no writes to disposition/inventory | CSV/file adapters |
| **Batch Reconciler** | FR-001 engine | Deterministic |
| **PV Intake Assembler** | FR-002 engine | Deterministic |
| **Supply Options Planner** | FR-003 engine; `no_side_effects` | Deterministic |
| **Contract Validator** | Validate outputs against schemas; reject additionalProperties violations | `tools/test_contracts` pattern |
| **Audit Log** | Persist request/response hashes, authz decision, mode (AI/offline) | Append-only local |
| **Optional Model Adapter** | Behind interface; disabled by default in assessment mode | Replaceable; off in AI-disabled |
| **Explorer (existing)** | Challenge inject browser (`app/`) — not decision engine | Unchanged package app |

**Not in v1:** graph DB, write-back connectors to MES/QMS disposition, autonomous agents with tools that mutate stock.

## 3. Component view (decision path)

| Container | Components |
|---|---|
| Authorization Gateway | EntitlementChecker; PurposeBinder; ToolManifestVerifier |
| Batch Reconciler | GenealogyAssembler; LabResultComparator; DocumentApplicability; ConflictEmitter |
| PV Intake Assembler | VerbatimExtractor; DuplicateCandidateScorer; ClockAssembler; ListednessContextBuilder |
| Supply Options Planner | ConstraintLoader; OptionRanker; HoldSurface; SideEffectGuard (always true) |
| Shared | EvidenceItemFactory; AbstentionService; SemanticRules (artefact 07); SchemaGate |

## 4. Code view (riskiest paths)

| Module (planned under `submission/src/`) | Rule |
|---|---|
| `authz.py` | Deny-by-default; no disposition imports |
| `workflows/batch.py` | Returns readiness_state only |
| `workflows/pv.py` | No final PV fields in models |
| `workflows/supply.py` | `no_side_effects` constant True; options status draft |
| `contracts/validate.py` | Fail closed on schema |
| `adapters/readonly.py` | No update/insert APIs to regulated SoR |

## 5. Mapping to contexts and features

| Context | Containers/components | Features |
|---|---|---|
| Batch Evidence Reconciliation | Batch Reconciler + SchemaGate | FR-001 |
| PV Case Intake Support | PV Intake Assembler + SchemaGate | FR-002 |
| Supply Options Planning | Supply Options Planner + SideEffectGuard | FR-003 |
| Privacy/Security cross-cut | Authorization Gateway; ToolManifestVerifier | FR-004 |
| Continuity | CLI flag `--offline` / AI-disabled path | FR-005 |

## 6. Boundaries, degraded mode, prohibited writes

| Topic | Design |
|---|---|
| Trust boundary | Untrusted docs/tools never cross into instruction channel |
| Data boundary | Read adapters only for MES/LIMS/inventory disposition fields |
| Degraded / offline | Deterministic engines + manual runbook; model adapter skipped (E-006) |
| Prohibited writes | No APIs for release/reject/allocate/ship/recall/quality-status change |
| Authz | Re-check IAM; ignore AI gateway cache alone |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Assumption | Single deployable CLI/API enough for assessment | UX limits | Architecture | Stage 5 | Open |
| R-002 | Gap | Detailed sequence diagrams deferred | Integration clarity | Architecture | Build tasks | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Map matches DDD | §5 | Review C3 | E-001 | Draft |
| No graph required | Containers exclude KG | AC-011 | E-002 | Draft |
| Prohibited writes absent | §6 | Contract negatives PASS | E-004 | PASS (samples) |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| GxP lead | Reviewer | No disposition container | Confirmed §2/§6 | 2026-08-07 |
| Evaluation lead | Reviewer | SchemaGate present | Confirmed | 2026-08-07 |
