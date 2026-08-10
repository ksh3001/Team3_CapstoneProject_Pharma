# Assurance Case

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | Artefacts 09–20; CSA 14; QRM 15; evaluation evidence |

## Purpose

States what we can and cannot claim about AI-EVIDENCE today, with arguments, supporting evidence, defeaters and invalidation conditions. Accountable owner: CQO / Validation. Completion criteria: top claim is either supported or explicitly **not claimed**; no silent overclaim of pilot readiness.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-2101 | `14_COMPUTER_SOFTWARE_ASSURANCE.md` | Prior artefact | Six high-risk functions failing/absent; no AI-assisted pilot recommended | Team conclusion |
| E-2102 | `13_GXP_LIFECYCLE_VALIDATION.md` | Prior artefact | VT-1/VT-2 failed; AF-1/AF-2 corroborate | Challenge + team |
| E-2103 | `submission/evidence/test_results.json` | Generated 2026-08-07 | 51/51 unit tests + 6/6 contract samples PASS | POC deterministic layer only |
| E-2104 | `submission/evidence/evaluation_results.json` | Generated 2026-08-07 | 11/15 public fixtures pass; 4 honestly `not_implemented` | Partial coverage |
| E-2105 | `data/model_artifacts.csv` + model gateway tests | Challenge + code | GXP-SUM-1 hash mismatch / missing signature → abstain | Blocks AI summarisation |
| E-2106 | `data/candidate_outputs.csv` / reviewer_feedback | Challenge | Automation bias: 19s unsafe accept | Human-factor defeater |

## 1. Top claim

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Top claim we **do** make | The deterministic support layer (reconcile/cite/flag/abstain; PV cluster/cite; draft supply options; security/privacy/checkpoint gates) fails closed on evidenced abuse patterns and never executes regulated side effects. | Capstone team / CQO | E-2103, E-2104 |
| Top claim we **do not** make | That AI-EVIDENCE is validated, production-ready, or safe for supervised AI inference pilot. | CQO | E-2101, E-2102, E-2105 |

## 2. Context and assumptions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Context | Brownfield NTG estate; three bounded workflows; offline deterministic mode is the assessed operating mode today. | Capstone team | Artefacts 01, 10, 19 |
| Assumptions | Challenge evidence immutable; schemas authoritative for assessed mode; humans retain all regulated decisions. | Capstone team | Workspace rules |

## 3. Subclaims and arguments

| Subclaim | Argument | Status |
|---|---|---|
| SC1: No disposition/side effects in assessed outputs | Schema + forbidden-language scanner + workflow design | Supported (E-2103) |
| SC2: Stale auth / purpose / token / checkpoint abuses gated | Unit tests + PUB-09/13 | Supported (E-2103/E-2104) |
| SC3: Compromised/unverified models not selected | Gateway abstains | Supported (E-2105) |
| SC4: DSR vs hold does not auto-delete on unconfirmed link | privacy_gates + PUB-11 | Supported (E-2104) |
| SC5: AI summarisation/NER ready for use | Would require integrity + validation pass | **Unsupported** (E-2101/E-2105) |
| SC6: Humans will not over-trust drafts | Countermeasure partially coded; UI missing; E-2106 shows failure | **Not yet supported** |

## 4. Evidence references

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Machine evidence | test_results.json, evaluation_results.json, run_output.json | Capstone team | E-2103, E-2104 |
| Documentary evidence | Artefacts 01–20, especially 14/15/16/18 | Capstone team | E-2101, E-2102 |
| Challenge injects | INJ-066–084 mapped across threat/privacy/reliability/finops | Capstone team | inject_evidence_map.csv |

## 5. Defeaters and counterevidence

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Defeater D1 | VT-1/VT-2 already failed on the platform under assessment (E-2102). | Validation | E-2102 |
| Defeater D2 | Model artifact integrity broken for flagship summariser (E-2105). | Capstone team | E-2105 |
| Defeater D3 | Automation bias already observed (E-2106). | CQO | E-2106 |
| Defeater D4 | 4/15 public fixtures not implemented — coverage incomplete. | Capstone team | E-2104 |
| Defeater D5 | Historical SEC-1/SEC-2 were unblocked in the estate — code gates close the pattern in POC, not proven in production estate. | CISO | Artefact 16 |

## 6. Residual risk

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Highest residual | Human over-trust + incomplete UI; OT ransomware path; residency violation still open in estate; tool allow-list not coded. | CQO / CISO / DPO | Artefacts 16–18 |
| Acceptable for defence demo? | Yes for **deterministic fail-closed POC demonstration**. No for **operational AI pilot**. | CQO | E-2101 |

## 7. Invalidation and reapproval conditions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Invalidates SC1–SC4 | Any side-effecting tool enabled; schema weakened; live-IAM bypass; fabricated eval passes. | Capstone team | This artefact |
| Required before claiming SC5 | Registry hash/signature match; re-run VT; CSA high-risk functions green; language-slice gates; UI automation-bias controls. | Validation / CQO | E-2101 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-2101 | Risk | Stakeholders may hear "tests pass" as "AI ready" | High | Capstone team | Defence messaging | Open |
| R-2102 | Gap | Assurance case not yet independently reviewed | Medium | CQO | Before defence | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Deterministic fail-closed support | src gates + workflows | 51 tests; 11 fixture passes | E-2103, E-2104 | Supported |
| AI inference pilot ready | — | CSA / VT | E-2101, E-2102 | Not supported |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | CQO / Validation | — | — | — |
