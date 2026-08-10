# Architecture Decision Register

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Architecture / integration lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Domain; GxP; Security; Product (challenger) |
| Status | Draft — Stage 3; architecture review **conditional** |
| Related requirements / ADRs | Artefacts 08–10; ≥10 ADRs for rubric |

## Purpose

Record material architecture decisions (structure + rationale) and the Stage 3 architecture review / prohibited-action contract gate (Checkpoint C3).

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `submission/artefacts/08_KNOWLEDGE_GRAPH_DECISION.md` | Stage 2 | KG deferred | Draft |
| E-002 | `submission/artefacts/10_C4_ARCHITECTURE.md` | Stage 3 | Containers | Draft |
| E-003 | `evaluation/contracts/*` + `tools/test_contracts.py` | Package | Fail-closed schemas | PASS 6/6 |
| E-004 | `submission/artefacts/01_BUSINESS_CASE.md` | Stage 1 | Deterministic-first | Draft |
| E-005 | `data/ai_use_boundaries.csv` | Boundaries | Prohibitions | Binding |

## 1. ADR index

| ADR | Title | Status | C4 element | Evidence basis |
|---|---|---|---|---|
| ADR-001 | Deterministic core before GenAI | accepted | All engines | Fact (boundaries) + Stage 1 decision |
| ADR-002 | Defer knowledge graph for v1 | accepted | Evidence Store Adapter | Artefact 08 |
| ADR-003 | Fail-closed JSON contracts as API boundary | accepted | Contract Validator | E-003 |
| ADR-004 | Read-only brownfield adapters | accepted | Evidence Store Adapter | E-005 |
| ADR-005 | Authorization at execution (deny stale cache) | accepted | Authorization Gateway | INJ-067 |
| ADR-006 | Untrusted documents are data not instructions | accepted | Semantic/knowledge path | INJ-065 |
| ADR-007 | Signed tool allow-list only | accepted | ToolManifestVerifier | INJ-066 |
| ADR-008 | Units require approved mapping else abstain | accepted | Batch Reconciler | INJ-024 |
| ADR-009 | PV duplicates are candidates only | accepted | PV Assembler | INJ-037 |
| ADR-010 | Supply options never side-effect | accepted | SideEffectGuard | supply schema |
| ADR-011 | Optional model behind replaceable adapter (off by default) | proposed | Model Adapter | Hypothesis framing |
| ADR-012 | Offline / AI-disabled continuity path mandatory | accepted | CLI offline mode | continuity_requirements |

## 2–3. Context, decisions, consequences (summary forms)

### ADR-001 Deterministic core before GenAI
- **Context:** No-AI baselines estimate large value; hard gates forbid autonomous regulated decisions.
- **Decision:** Implement deterministic reconciler/assemblers first; GenAI optional later.
- **Alternatives:** GenAI-first agents — rejected (INJ-003, hard gates).
- **Consequences:** Faster offline validation; less NLP coverage until Measure.
- **Guardrails:** Model cannot add disposition/PV-final/allocate fields.
- **Validation:** PUB-01–08 without model; AC-011.
- **Revisit:** After Measure baselines if human burden remains high.

### ADR-002 Defer knowledge graph
- See artefact 08. **Validation:** joins satisfy CQs for PUB-01–08. **Revisit:** genealogy/recall Measure failure.

### ADR-003 Fail-closed JSON contracts
- **Decision:** Use package schemas (`additionalProperties: false`, const execution_status/no_side_effects).
- **Validation:** `python tools/test_contracts.py` PASS.
- **Revisit:** Only via versioned schema + compatibility tests.

### ADR-004 Read-only brownfield adapters
- **Decision:** No write APIs to MES/QMS/inventory disposition.
- **Consequences:** Human executes outside AEGIS.
- **Validation:** Code review + absence of mutating adapters; supply negative tests.

### ADR-005 Authorization at execution
- **Decision:** IAM state authoritative; cached gateway alone insufficient.
- **Validation:** AC-008; deny contractor_77 pattern.

### ADR-006 Untrusted documents ≠ instructions
- **Decision:** trust=untrusted/superseded/draft cannot drive actions.
- **Validation:** PUB-03 / INJ-065 tests (Stage 4–5).

### ADR-007 Signed tool allow-list
- **Decision:** Reject poisoned manifests; no write disposition tools.
- **Validation:** Tool manifest negative tests (Stage 4–5).

### ADR-008 Approved units only
- **Decision:** interface_mappings.approved must be yes to convert; else abstain/contradiction.
- **Validation:** AC-003.

### ADR-009 PV duplicate candidates only
- **Decision:** Never irreversible merge in system.
- **Validation:** AC-004/005; schema.

### ADR-010 Supply no side effects
- **Decision:** `no_side_effects=true`; options `status=draft` only.
- **Validation:** AC-006/007; contract negatives PASS.

### ADR-011 Optional model adapter (proposed)
- **Context:** Hypothesis framing; cost model incomplete.
- **Decision:** Keep adapter interface; default off in assessment.
- **Status:** proposed until Measure + FinOps include human review.
- **Revisit:** Stage 6 FinOps gate.

### ADR-012 AI-disabled continuity
- **Decision:** Manual/deterministic path required for batch/PV/supply.
- **Validation:** AC-010; Stage 7 runbooks.

## 4. Architecture review / defence (Checkpoint C3)

| Check | Result |
|---|---|
| C4 maps to DDD contexts and FR-001–005 | pass |
| Material trade-offs have ADRs (≥10) | pass (12 ADRs) |
| Trust/authz/degraded/prohibited writes visible | pass (artefact 10 §6) |
| GenAI/HITL/rules boundaries placed | pass (ADR-001/011/012) |
| PRD out-of-scope not in containers | pass |
| Prohibited-action contract tests | **pass** (`tools/test_contracts.py` 6/6) |
| **Review status** | **conditional** |
| Conditions | (1) Stage 4 threat tests for INJ-065/066/067 still required; (2) ADR-011 remains proposed; (3) No Stage 4 artefacts created yet |

**Go-forward:** Proceed to Stage 4 (artefacts 16–21 + prohibited-action security tests). Do **not** start Stage 5 coding until Stage 4 threat/privacy artefacts exist per workshop plan.

## 5. Structural reopen gate

| Field | Value |
|---|---|
| Reopen required? | no |
| Gate decision | **cleared** for Stage 3 scope (contracts already pass) |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Security negative tests beyond schema samples | Residual until Stage 4–5 | Security | Stage 4 | Open |
| R-002 | Assumption | ADR-011 stays off through Stage 5 POC | Scope creep | Product | Stage 5 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| ≥10 ADRs | §1 | Rubric RUB-07 | This artefact | Met (12) |
| Contract negatives | ADR-003/010 | test_contracts.py | evidence/contract_tests_stage3.md | PASS |
| Conditional review | §4 | Checkpoint C3 | This artefact | conditional |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Product lead | Challenger | No GenAI lock-in | ADR-001/011 | 2026-08-07 |
| Security lead | Reviewer | Authz/tool ADRs required | ADR-005–007 | 2026-08-07 |
| Evaluation lead | Reviewer | Contract gate | PASS recorded | 2026-08-07 |
