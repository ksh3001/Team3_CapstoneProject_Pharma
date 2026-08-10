# Requirements and Traceability

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Domain & evidence lead + Evaluation lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | GxP lead; Security lead |
| Status | Draft — Stage 2 (Prompt 05 feature/AC content landed here; no separate FR files) |
| Related requirements / ADRs | Artefacts 01–08; evaluation/contracts; INJ clusters in artefact 06 |

## Purpose

Trace Stage 1–2 decisions into uniquely identified requirements and acceptance criteria for the three mandatory workflows, ready for Stage 3 contracts/ADRs and Stage 5 tests — without creating parallel FR document trees.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `submission/artefacts/01_BUSINESS_CASE.md`–`04_*.md` | Stage 1 | Problem, scope, HITL, rights | Draft |
| E-002 | `submission/artefacts/05_DDD_CONTEXT_MAP.md`–`08_*.md` | Stage 2 | Contexts, semantics, KG defer | Draft |
| E-003 | `evaluation/contracts/*.schema.json` | Package | Required response fields / prohibitions | Executable |
| E-004 | `data/ai_use_boundaries.csv`; `decision_rights.csv` | Boundaries | Allowed/prohibited | Binding |
| E-005 | `data/inject_evidence_map.csv` + artefact 06 map | Injects | IN_SCOPE_v1 clusters | Cluster-level |
| E-006 | `evaluation/PUBLIC_FIXTURE_INDEX.csv` | Fixtures | PUB-01–08 map to 3 schemas | No answer keys |

## Feature index (in-scope v1)

| Feature ID | Name | Bounded context | Priority | Status |
|---|---|---|---|---|
| FR-001 | Batch evidence reconciliation | Batch Evidence Reconciliation | P0 | provisional |
| FR-002 | PV case intake support | PV Case Intake Support | P0 | provisional |
| FR-003 | Supply / cold-chain option drafting | Supply Options Planning | P0 | provisional |
| FR-004 | Runtime authorization & trust gates | Cross-cut | P0 | provisional |
| FR-005 | AI-disabled / offline continuity hooks | Cross-cut | P0 | provisional |

## 1. Stakeholder and business requirements

| ID | Requirement | Source | Owner |
|---|---|---|---|
| BR-01 | Contribute to −14% release lead-time goal without changing specs or Quality authority | board_requests; artefact 01 | Product |
| BR-02 | Preserve human accountability for certification, final PV, allocation/recall | decision_rights; artefact 03 | GxP/PV/Supply |
| BR-03 | Prefer Measure + master-data/rules before GenAI scale | no_ai_baselines; artefact 01/08 | Product |
| BR-04 | Inspection-ready cited evidence within surge window | INJ-050; artefact 06 | Quality/RA |

## 2. Functional requirements

| ID | Requirement | Feature |
|---|---|---|
| FRQ-001 | Given batch_id, purpose, as-of, user context → produce batch_response with evidence, contradictions, gaps, abstentions, readiness_state, applicable_documents | FR-001 |
| FRQ-002 | readiness_state ∈ {insufficient_evidence, conflicted_evidence, ready_for_authorized_review} only | FR-001 |
| FRQ-003 | Given PV source package + receipts → pv_response with source_facts, duplicate_candidates, clock_evidence, terminology, listedness_context, required_reviews | FR-002 |
| FRQ-004 | Duplicate handling proposes candidates only; no irreversible merge | FR-002 |
| FRQ-005 | Given shortage/cold-chain event + constraints → supply_response with draft options, constraints, approvals_required, quality_holds, no_side_effects=true | FR-003 |
| FRQ-006 | All workflow responses: execution_status=not_executed; authorization object present | FR-001–003 |
| FRQ-007 | Deny when entitlement stale/ambiguous; deny untrusted docs as instructions; deny unsigned/poisoned tools | FR-004 |
| FRQ-008 | Provide deterministic offline path producing same contract shape without model inference | FR-005 |

## 3. Non-functional requirements

| ID | Requirement | Measure |
|---|---|---|
| NFR-001 | Offline assessment mode (stdlib / locked deps) | Run without cloud keys |
| NFR-002 | Idempotent request handling (same request_id → same logical result; no side effects) | Replay tests |
| NFR-003 | Audit fields present on every response | Schema + logs |
| NFR-004 | Token/cost budgets when model used; denial-of-wallet controls | Stage 6 FinOps |
| NFR-005 | Continuity: manual runbooks within continuity_requirements windows | Stage 7 runbooks |
| NFR-006 | Accessibility: no colour-only warnings; keyboard paths (INJ-073) | Stage 6 UX tests |
| NFR-007 | Subgroup: multilingual PV uncertainty visible (INJ-072) | Stage 6 gates |

## 4. GxP, safety, security and privacy requirements

| ID | Requirement | Control link |
|---|---|---|
| GXP-001 | No autonomous disposition/recall/reprocess | Schema additionalProperties false + negatives |
| GXP-002 | No silent unit conversion; unapproved mappings → abstain | interface_mappings |
| GXP-003 | Preserve ALCOA+ provenance on cited facts | EvidenceItem |
| SAF-001 | No final PV decisions in outputs | pv schema + negatives |
| SEC-001 | Current authorization at execution | FR-004 |
| SEC-002 | Prompt-injection / poisoned-tool fail closed | INJ-065/066 tests |
| PRI-001 | Purpose limitation; minimise identifiable narrative exposure | INJ-068 pattern |
| PRI-002 | DSR vs legal hold / GxP retain → restrict not blind delete | artefact 06 §6 |

## 5. Acceptance criteria

| AC ID | Feature | Criterion (binary) | Test idea |
|---|---|---|---|
| AC-001 | FR-001 | Positive batch fixture validates against batch_response.schema.json | PUB-01/02; contract sample |
| AC-002 | FR-001 | Response with disposition/release fields fails schema / is rejected | negative_batch_prohibited |
| AC-003 | FR-001 | Unapproved unit conflict yields abstention or contradiction, not converted “pass” | INJ-024 fixture |
| AC-004 | FR-002 | Positive PV fixture validates; includes duplicate_candidates and clock_evidence | PUB-04–06 |
| AC-005 | FR-002 | Final causality/reportability properties rejected | negative_pv_prohibited |
| AC-006 | FR-003 | Options status must be draft; no_side_effects true | positive_supply; negatives |
| AC-007 | FR-003 | Side-effect / reservation fields rejected | negative_supply_side_effect |
| AC-008 | FR-004 | Revoked IAM + active cache → authorization.decision=deny | INJ-067 |
| AC-009 | FR-004 | Untrusted knowledge content not executed as instruction | PUB-03 / INJ-065 |
| AC-010 | FR-005 | AI-disabled mode returns contract-valid pack or explicit manual handoff | continuity_requirements |
| AC-011 | Cross | No KG dependency required to pass PUB-01–08 | artefact 08 decision |

## 6. Traceability matrix

| Req / AC | Inject / CQ | Artefact | Contract / fixture | Stage for proof |
|---|---|---|---|---|
| BR-01 | INJ-001 | 01, 02 | Measure plan | 6 |
| FRQ-001–002 / AC-001–003 | INJ-021–028, CQ-1/2 | 05–07 | batch schema; PUB-01–03 | 5–6 |
| FRQ-003–004 / AC-004–005 | INJ-037–044, CQ-3/4 | 05–07 | pv schema; PUB-04–06 | 5–6 |
| FRQ-005–006 / AC-006–007 | INJ-051–058, CQ-5 | 05–07 | supply schema; PUB-07–08 | 5–6 |
| FRQ-007 / AC-008–009 | INJ-065–070 | 06 | security tests; PUB-09 later | 4–6 |
| FRQ-008 / AC-010 | INJ-082 | 04, 02 | manual mode | 5–7 |
| AC-011 | INJ-003 | 08 | offline POC | 5 |

## 7. Change and waiver control

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Req changes | Update this artefact; bump version; link ADR in Stage 3 | Domain + Architecture | Review record |
| Waiver | No waiver for hard-gate prohibitions | CQO / Security | Scoring hard gates |
| Ambiguities | Thresholds Unknown → Measure backlog; do not invent numbers | Eval | artefact 02 |

## Spec ambiguities (Prompt 05 hygiene)

| Ambiguity | Status | Handling |
|---|---|---|
| Numeric duplicate-match threshold | Unknown | Label Unknown; human review always |
| Exact lead-time baseline | Unknown | Measure M1 |
| Confidence scores for GenAI extract | N/A for deterministic v1 core | If model added, lock thresholds in Stage 3/4 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | PUB-09–15 participant contracts not yet written | Stage 3/4 work | Architecture | Stage 3 | Open |
| R-002 | Assumption | FR-001–005 cover Stage 2 scope | May split features later | Domain | Stage 5 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Three workflows have AC | §5 | Contract tests already PASS for schema samples | E-003 | Partial |
| Trace matrix exists | §6 | Checkpoint C2 | This artefact | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| GxP lead | Reviewer | Hard-gate ACs present | AC-002/005/007 | 2026-08-07 |
| Security lead | Reviewer | Auth/injection ACs present | AC-008/009 | 2026-08-07 |
