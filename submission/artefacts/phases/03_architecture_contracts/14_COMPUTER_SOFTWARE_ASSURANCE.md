# Computer Software Assurance (CSA)

> Team3 Phase 3 artefact (template 14). FDA CSA **lens** for critical thinking on assurance — not a completed CSA package.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Quality / Evaluation |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | GxP; Security |
| Status | Phase 3 — provisional |
| Related | GxP lifecycle (13); QRM (15); ac_test_plan |

## Purpose

Apply assurance effort proportional to patient/process risk for the assessed assist POC.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-CSA-01 | Hard-gate ACs | Highest assurance on prohibitions |
| E-CSA-02 | test_phase3_prohibited.py | Unscripted-style negative cases |
| E-CSA-03 | evaluate/runner.py | Suite gating |

## 1. Critical thinking summary

| Function | Patient/process risk if wrong | Assurance approach |
|---|---|---|
| AuthZ allow/deny | High (wrong data exposure / wrong action path) | Scripted + negative; IAM>cache |
| Batch disposition output | Critical | Design block + schema + tests |
| PV final / auto-merge | Critical | Design block + tests |
| Supply reservation/side effects | Critical | SideEffectGuard + tests |
| Document applicability | High | Quarantine + poison tests |
| Narrative LLM assist | Medium (misinfo) | Off by default; refuse on assessed |
| Metrics / cycle-time display | Low–med (hypothesis) | Limited — baselines Missing |

## 2. Unscripted testing focus

Phase 3 prohibited suite exercises contractor_77, disposition keys, reservation, poisoned manifest, malicious doc — beyond happy-path AC scripts.

## 3. Supplier / COTS

No production LLM/IAM vendor assurance claimed; challenge fixtures only.

## 4. Documentation rigor

Highest rigor on contracts, ADRs for write-plane denial, and hard-gate tests; lighter on demo UI polish.

## Risks, assumptions and unresolved gaps

| ID | Description | Status |
|---|---|---|
| R-CSA-01 | Full CSA protocol not executed | Accepted for POC |
| R-CSA-02 | Load/performance inconclusive | Open |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Assurance proportional to risk | §1 | Pass |
| Critical functions tested | phase3 + AC | Pass |

## Review record

| Reviewer | Role | Date |
|---|---|---|
| Team3 Quality | Owner | 2026-08-07 |
