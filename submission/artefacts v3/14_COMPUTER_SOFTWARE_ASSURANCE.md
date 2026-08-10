# Computer Software Assurance

> Phase 3. Risk-based CSA for high-impact functions of the advisory assist. Critical thinking over checklist theatre.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / GxP–quality lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Architecture; Evaluation |
| Status | Draft |
| Related requirements / ADRs | Artefact 13/15; ADR-032…040; FR-B2/P2/S2/T1 |

## Purpose

Apply CSA thinking: identify **what could cause patient/product harm if wrong**, assure those functions hardest, and scale evidence to risk — without pretending the assist is a release MES.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | artefact 13 | Intended use / risk class |
| E-002 | artefact 15 | Hazards / failure chains |
| E-003 | evaluation contracts + tests | Fail-closed proofs |
| E-004 | starter anti-patterns | Lexical pass, trust-all MD, etc. |

## 1. Critical thinking and risk basis

| Question | Answer for this system |
|---|---|
| What process does software support? | Evidence packaging for human regulated decisions |
| Where can software cause harm? | Hiding conflicts; fabricating completeness; enabling prohibited acts; untrusted instructions; stale authZ |
| What is low risk? | Cosmetic UI; non-decision summaries clearly labelled |
| Assurance bias | Prefer automated contract/inject tests for high-risk functions |

## 2. High-risk functions

| ID | Function | Harm if wrong | Assurance intensity |
|---|---|---|---|
| HR-01 | Prohibit disposition / reportability / reservation fields | Authority laundering | Schema + runtime reject |
| HR-02 | AuthZ freshness | Unauthorized access to GxP data | Negative tests; deny-wins |
| HR-03 | Instruction eligibility | Malicious/outdated SOP executed | Catalog filter tests |
| HR-04 | Unit mapping application | Wrong OOS/pass narrative | Unapproved → contradiction |
| HR-05 | Citation integrity | False audit trail | evidence_item + sha256 |
| HR-06 | Supply side-effect flag | Ghost stock moves | const true + no reservation |
| HR-07 | Duplicate merge | Wrong case identity | Candidates only; no merge API |
| HR-08 | AI-disabled continuity | Decision paralysis / unsafe workaround | Continuity drill |

## 3. Assurance methods

| Method | Used for |
|---|---|
| Contract schema tests | HR-01, HR-05, HR-06 |
| Adversarial / prohibited-action tests | HR-01…04 |
| Fixture inject cases | HR-04, HR-07 (Phase 5+) |
| Unscripted exploration | Automation-bias / HF (Phase 4/6) |
| Code review / ADR gate | Architecture drift |
| Supplier / model eval | Optional LLM port only |

## 4. Unscripted and scripted evidence

| Type | Examples | When |
|---|---|---|
| Scripted | `tools/test_contracts.py`; submission schema tests; planned loader cases | Every evaluate |
| Unscripted | Try to coax disposition via prompt; feed untrusted SOP; revoke user mid-session | Red-team Phase 4/6 |
| Record | Keep failing/passing artefacts under `submission/evidence` | Defence pack |

## 5. Defect handling

| Severity | Example | Disposition |
|---|---|---|
| Critical | Prohibited field accepted; stale allow | Block release; fix before demo claim |
| Major | Silent unit convert; missing citation on material fact | Block scored path |
| Minor | Wording / UX | Track; no false ready_for_review |
| Escape | Found in unscripted | Incident note + regression test |

## 6. Release decision evidence (POC)

| Gate | Evidence | Phase 3 status |
|---|---|---|
| Schema positives/negatives | test_contracts + test_schema_contracts | GREEN |
| Runtime prohibited gates | test_prohibited_runtime_gates | **RED (expected)** |
| Architecture review | artefacts 10–12 | Draft |
| QRM accepted residual | artefact 15 | Draft |
| Full POC release | Phase 5–6 greens | Not yet |

## 7. Continuous assurance

| Cadence | Activity |
|---|---|
| Each change to contracts/gates | Re-run schema + prohibited suites |
| Each evaluate script | Persist machine-readable results |
| Before defence | Re-run clean-room path |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-341 | Gap | Runtime gates unimplemented | CSA incomplete | Architecture | Open Phase 5 |
| A-020 | Assumption | Scripted contract suite catches most HR-01/06 defects | Residual prompt bypass | Evaluation | Open |

## Traceability and acceptance

| Claim | Control | Test | Result |
|---|---|---|---|
| High-risk list complete for POC | §2 | GxP review | Draft |
| Assurance scaled to risk | §3–4 | Hour-18 | Pending |
| Defects block release | §5–6 | Gate policy | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | GxP | Pending | | |
