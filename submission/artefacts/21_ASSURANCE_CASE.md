# Assurance Case

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | GxP lead + Security lead + Evaluation lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Architecture lead; Product lead |
| Status | Draft — Stage 4 claims; POC evidence pending Stage 5–6 |
| Related requirements / ADRs | Artefacts 09–20; hard gates; DEFINITION_OF_DONE |

## Purpose

Claims–arguments–evidence that AEGIS can be operated as a bounded advisory system without autonomous regulated decisions, with identifiable invalidation conditions and residual risk.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `requirements/SCORING_MODEL.md` hard gates | Scoring | Unconditional fail conditions | Binding |
| E-002 | `tools/test_contracts.py` + Stage 3 evidence | Tests | Schema positives/negatives PASS | Package samples |
| E-003 | `submission/tests/test_prohibited_actions.py` | Stage 4 | Control negatives PASS | Control-level |
| E-004 | Artefacts 01–20 | Submission | Design/control claims | Draft |
| E-005 | `DEFINITION_OF_DONE.md` | Package | Completion standard | Binding |

## Top-level claim (C0)

**C0:** For the documented intended use, AEGIS assessment mode does not autonomously release/reject batches, make final PV decisions, or allocate/ship/recall stock, and fails closed on stale auth, untrusted instructions, poisoned write tools, and schema-prohibited fields.

## Argument structure

### C1 — Prohibited regulated actions cannot execute
- **Argument:** Output contracts forbid disposition/final PV/side effects; architecture has no write adapters.
- **Evidence:** E-002; ADR-004/009/010; artefact 10 §6; `test_contracts` negatives.
- **Status:** Supported at schema/design level; full engine e2e Stage 5.

### C2 — Authorization and tool trust are enforced at execution
- **Argument:** IAM re-check; poisoned manifests rejected; model hash mismatch blocked.
- **Evidence:** E-003; ADR-005–007; artefact 16.
- **Status:** Supported by Stage 4 control tests.

### C3 — Untrusted content cannot become instructions
- **Argument:** knowledge trust filter; untrusted docs excluded from instruction channel.
- **Evidence:** E-003 `test_untrusted_knowledge_not_instruction`; ADR-006; INJ-065.
- **Status:** Control predicate PASS; PUB-03 e2e Stage 5–6.

### C4 — Human accountability preserved
- **Argument:** Decision rights + HITL + readiness/draft-only outputs.
- **Evidence:** Artefacts 03, 18; contract human_review fields.
- **Status:** Design-supported; UX demo Stage 5–9.

### C5 — Privacy and governance applicability considered
- **Argument:** Purpose limitation, hold/DSR method, EU AI Act 11-field analysis, 42001 theme map.
- **Evidence:** Artefacts 17, 19, 20.
- **Status:** Analysis draft; legal review residual.

### C6 — Continuity when AI unavailable
- **Argument:** Deterministic core + AI-disabled requirement.
- **Evidence:** ADR-001/012; continuity_requirements; offline default.
- **Status:** Design-supported; runbooks Stage 7.

## Invalidation conditions (claim fails if…)

| ID | Condition | Response |
|---|---|---|
| INV-01 | Any path sets batch disposition / final PV / allocation side effect | Stop release; hard-gate fail |
| INV-02 | Revoked user can obtain allow via cache alone | Stop; fix authz |
| INV-03 | Untrusted doc text changes system action | Stop; retrieval fix |
| INV-04 | Deployed model hash ≠ registry without block | Stop model path |
| INV-05 | AEGIS reclassified as determinative without re-validation | Pause; redo artefacts 13/19/21 |
| INV-06 | Offline/manual path unavailable for required workflows | Pause go-live |

## Residual risk (accepted for Stage 4 → Stage 5)

| Residual | Acceptance |
|---|---|
| POC not yet implemented | Accepted to proceed to Stage 5 build |
| Measure baselines Unknown | Accepted; no −14% claim yet |
| Legal EU AI Act opinion pending | Accepted for workshop; not for real deployment |
| Full red-team/PUB e2e pending | Must close in Stages 5–6 before defence |

## Stage 4 assurance verdict

**Conditional support for C0 at design/control-test level.** Proceed to Stage 5 POC under existing ADRs; do not claim production readiness.

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Engine-level proof pending | Defence incomplete until Stage 5–6 | Build/Eval | Stage 5–6 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| C0 Stage 4 | C1–C3 | prohibited-action suite | E-002, E-003 | Conditional PASS |
| Invalidation conditions listed | Table | Review | This artefact | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Evaluation lead | Reviewer | Verdict conditional — not production | Explicit | 2026-08-10 |
| Product lead | Reviewer | Aligns no-AI / deterministic-first | Confirmed | 2026-08-10 |
