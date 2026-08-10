# EU AI Act Applicability

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `04_PRODUCT_SERVICE_BLUEPRINT.md`; `14_COMPUTER_SOFTWARE_ASSURANCE.md`; `ai_use_boundaries.csv`; ADR-006/007 |

## Purpose

Records a **scenario-grounded applicability analysis** for the three intended AI uses under the EU AI Act framing used in this training package — without claiming formal legal advice or real-world regulatory determination. Accountable owner: Legal / Compliance (role-played) with capstone team as author. Completion criteria: intended purpose, actor role, classification *hypothesis*, and change triggers are explicit; residual uncertainty is logged.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-1901 | `data/ai_use_boundaries.csv` | Boundary register | Three use cases with explicit allowed/prohibited actions; no autonomous regulated decisions | Fact of intended scope |
| E-1902 | `knowledge/AI_GXP_BOUNDARY.md` (K-003) | Synthetic policy 2026-05-01 | AI may support evidence review; cannot replace accountable GxP decisions | Scenario policy, not statute |
| E-1903 | `04_PRODUCT_SERVICE_BLUEPRINT.md` / `14_COMPUTER_SOFTWARE_ASSURANCE.md` | Prior artefacts | Supervised support only; CSA conclusion: no AI-assisted capability recommended for pilot while integrity/auth gates fail | Engineering posture |
| E-1904 | `data/candidate_outputs.csv` CO-1 | Review evidence | Unsafe "recommend progression" candidate shows how easily support output slides toward decision language | Abuse/misuse risk input |
| E-1905 | Case geography (NTG EU affiliates, EU QP role) | Integrated case | Deployer context includes EU operations and EU Qualified Person accountability | Scenario setting |

**Assumption A-1901:** This artefact applies the AI Act *as a structured checklist for the training scenario*. It is not a conformity assessment and not legal advice.

## 1. Intended purpose and actor role

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Intended purpose | Assist humans with (A) batch evidence reconciliation, (B) PV intake structuring, (C) non-executing supply/recall-scope options — within E-1901 boundaries. | Capstone team | E-1901, E-1902 |
| Actor role (hypothesis) | NovaCura / NTG is primarily a **deployer** of third-party models (e.g., summarisation/NER) and a **provider** of the integration layer (gateway, workflows, gates) that determines residual risk. Exact provider/deployer split for each vendor model is not fully evidenced → Gap R-1901. | Legal (role-played) | E-1905; Gap R-1901 |
| Explicit non-purpose | Autonomous batch release, final PV determination, stock reservation/shipment, recall initiation (E-1901). | Capstone team | E-1901 |

## 2. System and component boundary

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| In scope | AI-EVIDENCE integration: model gateway, three workflows, security/privacy/checkpoint gates, schema contracts. | Capstone team | `10_C4_ARCHITECTURE.md` |
| Out of scope | MES/QMS/LIMS systems of record; human QP/PV/board decisions; OT networks. | Capstone team | E-1902 |
| General-purpose model components | Vendor models behind gateway; integrity and validated-scope checks are deployer controls before use. | Capstone team | ADR-006/007 |

## 3. Risk classification analysis

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Working classification (scenario) | **Not treated as prohibited** (no social scoring / exploitation systems in scope). **High-risk hypothesis if** the system were used to substantially determine access to essential health products or to replace clinical/safety professional judgment — which our boundaries forbid. **Current engineering posture:** limited-risk / transparency-oriented **support tool** with mandatory human oversight, *provided* boundaries hold in practice (E-1904 shows boundary pressure). | Legal (role-played) | E-1901, E-1904 |
| Why not claim "definitely not high-risk" | Misuse path (disposition language, automation bias) and safety/supply context mean classification could escalate if intended purpose drifts. Classification is therefore **conditional on E-1901 remaining true in deployment**. | Legal (role-played) | E-1904; Gap R-1902 |
| Medical-device angle | Not assessed here — no device-claim evidence in package; abstain rather than invent (Gap R-1903). | Legal / RA | Gap R-1903 |

## 4. Prohibited/high-risk/transparency considerations

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Prohibited practices | None intentionally designed; poisoned disposition tool (artefact 16) would be an unacceptable capability if enabled. | Capstone team | Artefact 16 E-1602 |
| Transparency | Outputs must be machine-checkable drafts with citations/gaps; humans must know they are reviewing AI-assisted packets (E-1902). | Capstone team | E-1902 |
| Human oversight | Hard requirement — contracts forbid side effects; gates fail closed (E-1903). | Capstone team | E-1903 |

## 5. Provider/deployer obligations (scenario checklist)

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Deployer-style duties we implement anyway | Intended-use limits, logging of gate outcomes, human oversight, input data governance, post-market monitoring hooks (eval scripts), instructions for use (runbooks — pending). | Capstone team | E-1901; `scripts/evaluate.py` |
| Provider-style duties for our integration code | Risk management (artefacts 15–16), data governance (06/17), technical docs (10–12), record-keeping (evidence JSON), accuracy/robustness via tests. | Capstone team | Prior artefacts |
| Not claimed complete | Formal EU declaration, notified-body path, or full Annex documentation — out of scope for this training submission. | Legal | A-1901 |

## 6. Evidence and assumptions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Material assumptions | A-1901 (training checklist, not legal opinion); provider/deployer split incomplete (R-1901); no MDR/IVDR claim analysis (R-1903). | Capstone team | This section |
| Supporting technical evidence | Fail-closed gateway, contracts, tests, evaluation honesty (`not_implemented` not faked). | Capstone team | `submission/evidence/*` |

## 7. Change triggers

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Re-open classification if… | (1) Any workflow gains side-effecting tools; (2) outputs regain disposition language; (3) AI used for patient-level treatment/eligibility; (4) EU placing-on-market claim beyond internal support tool; (5) medical-device qualification suggested. | Legal / Capstone | E-1901, E-1904 |
| Immediate trigger already active | Model integrity failure and unvalidated pilot recommendation (E-1903) — do not expand intended purpose until CSA gates pass. | Capstone team | E-1903 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1901 | Gap | Vendor contract evidence incomplete for provider vs deployer per model | Medium | Legal / Procurement | Vendor review | Open |
| R-1902 | Assumption | Classification remains support-tool only while boundaries hold | High if violated | Capstone team | Continuous | Open |
| R-1903 | Gap | No MDR/IVDR applicability analysis | Medium | RA | If clinical claims appear | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| No autonomous regulated decisions | Contracts + use boundaries | `tools/test_contracts.py`; workflow tests | E-1901 | PASS |
| Human oversight retained | RACI + abstention gates | Artefacts 03/18; unit tests | E-1902, E-1903 | PASS (design+code) |
| Formal AI Act conformity | — | — | — | Not claimed |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | Legal / Compliance (role-played) | — | — | — |
