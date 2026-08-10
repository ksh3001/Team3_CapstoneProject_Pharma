# Assurance Case

> Phase 4. Structured argument that the assist is **adequately safe for continued POC build / later conditional go**, not that it is production-certified.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / GxP + Architecture + Security |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Product; Evaluation |
| Status | Draft |
| Related requirements / ADRs | DEC-010/011/012/032/041; artefacts 04, 10–20 |

## Purpose

State the top safety/assurance claim, supporting subclaims, evidence, defeaters, and reapproval triggers for Project AEGIS-PHARMA’s three fail-closed workflows.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | evaluation/contracts + test_contracts | Schema fail-closed GREEN |
| E-002 | submission tests (schema + runtime + trust) | Schema GREEN; runtime/trust RED |
| E-003 | artefacts 10–20 | Architecture, GxP, threat, privacy, HF, governance |
| E-004 | tool_allowlist.json | Assessed tool policy |
| E-005 | DEC-032 | Residual acceptance for build only |

## 1. Top claim

**C0:** *For the synthetic offline POC, the AEGIS evidence assist cannot execute prohibited regulated acts (batch disposition, final PV safety/reportability, stock reserve/allocate/ship/recall) and will fail closed on stale authZ, unsigned/poisoned tools, and untrusted instructions — provided runtime gates are implemented and evaluation gates remain green.*

**Claim for Phase 4 exit (weaker):** *C0-design* — the above properties are **specified, contracted, and tested (red where unimplemented)**; schema-level prohibited fields already cannot validate.

## 2. Context and assumptions

| ID | Context / assumption |
|---|---|
| CTX-1 | Assessed mode uses challenge/synthetic data offline |
| CTX-2 | Humans retain disposition/reportability/allocate authority |
| CTX-3 | Optional LLM disabled or port-constrained for scored path |
| A-026 | Schema `additionalProperties: false` remains enforced |
| A-027 | Operators follow AI-disabled runbook when model unavailable |

## 3. Subclaims and arguments

| Subclaim | Argument | Support |
|---|---|---|
| SC-1 No disposition/reportability/reservation in outputs | Schemas forbid fields; builder must reject | E-001; ADR-032/040 |
| SC-2 No source writes | C4 PROHIBITED; read-only integrations | Artefact 10/12; ADR-037 |
| SC-3 AuthZ deny on stale/revoked | Execution-time check | ADR-033; tests RED |
| SC-4 Tools contained | Allowlist; assessed no writes | tool_allowlist; ADR-034; tests RED |
| SC-5 Untrusted docs not instructions | DEC-022 eligibility | Artefact 16; tests RED |
| SC-6 Privacy conflicts fail closed | DSR≠erase; residency deny export | Artefact 17; tests RED |
| SC-7 Humans not misled by design | Conflict-first HF controls | Artefact 18 |
| SC-8 Governance awareness | EU AI Act / 42001 mapped without conformity claims | Artefacts 19–20 |

## 4. Evidence references

| Evidence | Path | Supports |
|---|---|---|
| Package contract suite | `tools/test_contracts.py` | SC-1 |
| Schema mirror tests | `submission/tests/test_schema_contracts.py` | SC-1 |
| Runtime prohibited tests | `test_prohibited_runtime_gates.py` | SC-1,3,4,5 (RED) |
| Trust-boundary tests | `test_trust_boundary_gates.py` | SC-3…6 (RED) |
| Tool policy | `submission/evaluation/tool_allowlist.json` | SC-4 |
| QRM / CSA | artefacts 14–15 | Residual risk |
| Threat model | artefact 16 | SC-3…5 |

## 5. Defeaters and counterevidence

| Defeater | Status | Response |
|---|---|---|
| Runtime gates not implemented | **Active** | DEC-032: accept for build; not for release |
| Automation bias despite UX | Open | Phase 6 HF unscripted |
| Prompt injection bypasses eligibility | Open | Assessed LLM-off; red-team |
| Legal class under EU AI Act higher than assumed | Open | Escalation; conservative controls |
| Operator treats draft option as reservation outside system | Open | Training + no side effects in system |

## 6. Residual risk

| Residual | Acceptance |
|---|---|
| RED runtime/trust tests | Accepted for Phase 5 entry only |
| Human residual error | Accepted — assist must not amplify via hidden conflicts |
| No formal DPIA / legal class | Accepted for synthetic POC; not for production |

## 7. Invalidation and reapproval conditions

| Condition | Effect |
|---|---|
| Any prohibited execution in evaluate | Invalidate C0; stop demo claims |
| Schema loosened to allow disposition fields | Invalidate SC-1; require new ADR + tests |
| Write tools enabled in assessed mode | Invalidate SC-4 |
| Real PHI introduced without privacy review | Invalidate CTX-1; pause |
| Design requires AI authority for regulated acts | Stop (DEC-011) |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-451 | Gap | C0 not yet evidenced by green runtime tests | Release blocked | Architecture | Open Phase 5 |
| A-026/027 | Assumption | See §2 | Defeater if false | Team | Open |

## Traceability and acceptance

| Claim | Status now | Path to green |
|---|---|---|
| C0-design (Phase 4) | **Met** — specs + tests exist | — |
| C0 (release) | **Not met** | Implement gates; Phase 6 suites green |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | GxP + Security | Pending conditional acceptance | | |
