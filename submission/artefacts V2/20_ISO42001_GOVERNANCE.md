# ISO/IEC 42001-Aligned Governance

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `11_ADR_REGISTER.md`; `15_QUALITY_RISK_MANAGEMENT.md`; `16_THREAT_ABUSE_MODEL.md`; K-003 |

## Purpose

Maps this submission’s AI management practices to an ISO/IEC 42001-style control set for the training scenario — policy, inventory, risk, lifecycle, suppliers, monitoring — and shows where NovaCura’s estate currently fails those controls. Accountable owner: AI governance lead (role-played) / CQO. Completion criteria: each clause-area below cites challenge or submission evidence; gaps are explicit.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-2001 | `knowledge/AI_GXP_BOUNDARY.md` (K-003) | Approved 2026-05-01 | Organisational AI/GxP boundary policy exists in scenario | Synthetic policy |
| E-2002 | `data/ai_use_boundaries.csv` | Use-case inventory | Three approved support uses with prohibitions | Operational inventory seed |
| E-2003 | `11_ADR_REGISTER.md` + `15_QUALITY_RISK_MANAGEMENT.md` + `16_THREAT_ABUSE_MODEL.md` | Prior artefacts | Decisions, multi-inject risk chains, threat controls | Team work product |
| E-2004 | `13_GXP_LIFECYCLE_VALIDATION.md` | Prior artefact | VT-1/VT-2 failed on AI-EVIDENCE; audit findings AF-1/AF-2 | Validation governance failure evidence |
| E-2005 | `data/vendor_dependencies.csv` / `data/model_artifacts.csv` | Vendor / artifact registers | Concentration + hash/signature failure | Supply-chain governance input |
| E-2006 | `submission/scripts/{test,evaluate}.py` + evidence JSON | This build | Monitoring/evaluation loop exists for POC | Limited to public fixtures + unit tests |

## 1. AI policy and objectives

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Policy | E-2001 + E-2002: support-only AI; abstain when applicability unclear; no replacement of GxP accountability. | CQO / AI governance | E-2001, E-2002 |
| Objectives (POC) | (1) Fail closed on integrity/auth/privacy conflicts; (2) measurable reduction of evidence-hunt time *without* increasing unsafe accepts; (3) AI-disabled continuity always available. | Capstone team | E-2003; artefact 01 |

## 2. Use-case inventory and ownership

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Inventory | Batch evidence, PV intake, supply options (E-2002). Owners: EU QP context / PV / Supply Governance Board per RACI. | Capstone team | E-2002; artefact 03 |
| Explicit exclusions | Biomarker model training, disposition tools, autonomous allocation. | Capstone team | Artefacts 16–17 |

## 3. Risk and impact assessment

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Performed? | Yes in scenario work products: QRM chains (15), threat model (16), privacy (17), CSA (14). | Capstone team | E-2003 |
| Current impact conclusion | High residual risk while VT failures and model integrity gaps persist (E-2004, E-2005) — no supervised pilot recommended (artefact 14). | CQO | E-2004, E-2005 |

## 4. Lifecycle controls

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Plan/design | ADRs, C4, contracts, boundaries. | Capstone team | E-2003 |
| Build/verify | Deterministic tests-before-inference; 51 unit tests; contract tests. | Capstone team | E-2006 |
| Validate | AI-EVIDENCE validation already failed VT-1/VT-2 (E-2004) — lifecycle gate is red. | Validation | E-2004 |
| Operate/retire | Runbooks and retirement artefacts still pending (25–27, 29). | Capstone team | Gap R-2001 |

## 5. Supplier and data governance

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Suppliers | Model vendors subject to artifact integrity + validated scope; concentration risk logged (E-2005). | Procurement / Capstone | E-2005; artefact 10 |
| Data | ALCOA+, residency, consent, DSR/hold (artefacts 06, 17). | DPO / Data stewards | Artefacts 06/17 |

## 6. Monitoring, incidents and improvement

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Monitoring | `evaluate.py` / `test.py` write machine-readable results; gate deny metrics defined in artefact 18. | Capstone team | E-2006 |
| Incidents | Security events SEC-1/SEC-2 historically unblocked — now gated in code; incident runbook still pending. | CISO | Artefact 16; Gap R-2001 |
| Improvement | Failed VT/AF items and R-IDs across artefacts form the backlog; no claim of closed-loop CAPA effectiveness yet (prior CAPA effectiveness failures in DMAIC). | CQO | Artefact 02 |

## 7. Evidence mapping

| 42001-style area | Our evidence | Status |
|---|---|---|
| Policy | K-003, ai_use_boundaries | Present |
| Inventory & roles | Artefacts 03–04, E-2002 | Present |
| Risk assessment | Artefacts 14–17 | Present |
| Lifecycle | Artefact 13 + src/tests | Partially failing validation |
| Suppliers | model_artifacts, vendor deps | Integrity fail open |
| Monitoring | scripts + evidence JSON | POC-level |
| Continual improvement | Risk registers | Open items dominate |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-2001 | Gap | Operating/incident/retirement runbooks not yet written under `submission/runbooks/` | Medium-High | Capstone team | Artefacts 25–27 | Open |
| R-2002 | Assumption | Mapping to 42001 is alignment evidence for training, not a claim of certified AIMS | Medium if overstated | Capstone team | Defence | Open |
| R-2003 | Risk | Validation failures (E-2004) mean governance exists on paper while system is not releasable | High | Validation / CQO | Before any pilot | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Use cases inventoried with prohibitions | ai_use_boundaries + ADRs | Contract negative tests | E-2002 | PASS |
| Risk assessments documented | Artefacts 14–17 | Review | E-2003 | PASS (doc) |
| Validated operating AI system | Lifecycle validation | VT-1/VT-2 | E-2004 | FAIL (current state) |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | AI governance / CQO | — | — | — |
