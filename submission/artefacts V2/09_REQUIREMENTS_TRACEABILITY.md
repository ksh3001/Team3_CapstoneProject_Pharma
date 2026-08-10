# Requirements and Traceability

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | Synthesizes `01_BUSINESS_CASE.md` through `08_KNOWLEDGE_GRAPH_DECISION.md` |

## Purpose

Consolidates every functional, non-functional, GxP/safety/security/privacy requirement established across artefacts 01–08 into one traceable register, linking each to its source evidence, its architecture/control, and its test result (existing pass, pending, or current-state fail). Accountable owner: capstone team. Completion criteria: every requirement traces to at least one prior artefact's evidence ID; no requirement is invented without a source.

## Evidence register

This artefact does not introduce new evidence rows; it indexes evidence already registered in prior artefacts. See `01_BUSINESS_CASE.md` (E-0xx), `03_STAKEHOLDER_DECISION_RIGHTS.md` (E-1xx), `02_DMAIC_WORKBOOK.md` (E-2xx), `04_PRODUCT_SERVICE_BLUEPRINT.md` (E-3xx), `05_DDD_CONTEXT_MAP.md` (E-4xx), `06_DATA_GOVERNANCE_INTEGRITY.md` (E-5xx), `07_ONTOLOGY_SEMANTIC_LAYER.md` (E-6xx), `08_KNOWLEDGE_GRAPH_DECISION.md` (E-7xx).

## 1. Stakeholder and business requirements

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| BR-001: Reduce end-to-end release lead time 14% without weakening Quality authority or changing specifications | Board target, `01_BUSINESS_CASE.md` E-001 | Board (role-played) | `01_BUSINESS_CASE.md` §1 |
| BR-002: Resolve conflicting functional KPIs without letting any one function's incentive silently drive AI scope | `01_BUSINESS_CASE.md` E-002; `03_STAKEHOLDER_DECISION_RIGHTS.md` §3 | Capstone team | `03_STAKEHOLDER_DECISION_RIGHTS.md` §3 |
| BR-003: Prefer non-AI fixes (rules/workflow, master-data repair) where they close the same root causes as a proposed AI capability | `01_BUSINESS_CASE.md` §3; `02_DMAIC_WORKBOOK.md` §3/§4 | Capstone team | `02_DMAIC_WORKBOOK.md` |

## 2. Functional requirements

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| FR-001: Workflow A reconciles genealogy, lab results, environmental monitoring, deviations, CAPA, change control, validation state and supplier evidence, and flags gaps/contradictions | `case/INTEGRATED_CASE.md` §4; concrete contradiction case: `02_DMAIC_WORKBOOK.md` E-201/E-202/E-203; `08_KNOWLEDGE_GRAPH_DECISION.md` E-701/E-702 (MES vs. warehouse contradiction) | Capstone team | `evaluation/contracts/batch_response.schema.json` |
| FR-002: Workflow A never releases, rejects, reprocesses, relabels or recalls | `01_BUSINESS_CASE.md` E-004 | Capstone team | `evaluation/contract_samples/negative_batch_prohibited.json` — PASS |
| FR-003: Workflow B supports intake, duplicate detection, terminology normalization, source authority, reporting-clock reconstruction, listedness evidence, multilingual review | `case/INTEGRATED_CASE.md` §4; duplicate case: `08_KNOWLEDGE_GRAPH_DECISION.md` E-704; terminology: `07_ONTOLOGY_SEMANTIC_LAYER.md` E-604; listedness: `07_ONTOLOGY_SEMANTIC_LAYER.md` E-605; language quality: `04_PRODUCT_SERVICE_BLUEPRINT.md` E-303 | Capstone team | `evaluation/contracts/pv_response.schema.json` |
| FR-004: Workflow B never makes final seriousness/causality/expectedness/reportability/signal-confirmation decisions | `01_BUSINESS_CASE.md` E-004 | Capstone team | `evaluation/contract_samples/negative_pv_prohibited.json` — PASS |
| FR-005: Workflow C generates traceable, non-executing supply/cold-chain options using only quality-released stock | `case/INTEGRATED_CASE.md` §4; `04_PRODUCT_SERVICE_BLUEPRINT.md` E-306; recall-scope tracing: `08_KNOWLEDGE_GRAPH_DECISION.md` E-703 | Capstone team | `evaluation/contracts/supply_response.schema.json` |
| FR-006: Workflow C never reserves, allocates, ships, changes quality status or initiates recall without explicit authorized human approval | `01_BUSINESS_CASE.md` E-004; `04_PRODUCT_SERVICE_BLUEPRINT.md` E-306 | Capstone team | `evaluation/contract_samples/negative_supply_side_effect.json` — PASS |
| FR-007: All AI output vocabulary must avoid disposition/progression language (e.g., "recommend progression") even when technically only citing evidence | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-301, §2 | Capstone team | Gap — no automated check yet (`04_PRODUCT_SERVICE_BLUEPRINT.md` Traceability table) |

## 3. Non-functional requirements

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| NFR-001: Abstain or escalate when applicability (source authority, jurisdiction, effective date) cannot be established | `knowledge/AI_GXP_BOUNDARY.md` (`04_PRODUCT_SERVICE_BLUEPRINT.md` E-307); concrete unresolved case: `07_ONTOLOGY_SEMANTIC_LAYER.md` R-602 (listedness authority) | Capstone team | Pending implementation |
| NFR-002: Every fact/edge carries source, version, effective date and jurisdiction/scope, never a bare "current" value | `07_ONTOLOGY_SEMANTIC_LAYER.md` §4/§7; `08_KNOWLEDGE_GRAPH_DECISION.md` §4 (edge provenance) | Capstone team | Pending implementation |
| NFR-003: AI-disabled continuity for at least 14 days | INJ-082; current evidence shows the AI primary-region outage (`04_PRODUCT_SERVICE_BLUEPRINT.md` E-304, `DT-2`) has no recorded end — treated as a live requirement, not a future contingency | Capstone team | `04_PRODUCT_SERVICE_BLUEPRINT.md` R-304 |
| NFR-004: Subgroup/language output-quality parity tracked and low-confidence languages flagged for mandatory review | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-303 (PV-NER-4: English 0.91 vs. Hindi 0.67 vs. Arabic 0.63) | Capstone team | Pending — `evaluation/EVALUATION_PLAN.md` suite 10 |
| NFR-005: No colour-only status indicator; full keyboard navigation | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-302 (both rated "high" severity, fail) | Capstone team | Pending remediation |
| NFR-006: Graph-shaped queries (recall scope, duplicate clustering, serialization reconstruction) implemented in-process, not via a dedicated graph database, unless production-scale evidence proves otherwise | `08_KNOWLEDGE_GRAPH_DECISION.md` §3/§7 | Capstone team | Gap R-701 (load-test not yet performed) |

## 4. GxP, safety, security and privacy requirements

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| GXP-001: No AI authority over batch certification, ICSR reportability or stock allocation beyond "none"/"draft only" | `03_STAKEHOLDER_DECISION_RIGHTS.md` E-103 | EU QP / Safety Physician / Supply Governance Board | `tools/test_contracts.py` — PASS (6/6) |
| GXP-002: Reviewer-facing output must not enable acceptance without evidence-item inspection (counters recorded automation-bias failure) | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-301 (`CO-1`/`QR-11`, 19-second accept of an `unsafe_candidate`) | Capstone team | Pending — no UI built yet |
| GXP-003: Identity conflicts (compound, substance, product) are never auto-merged without stewardship evidence | `05_DDD_CONTEXT_MAP.md` E-401/E-404/E-408 | Capstone team | Pending implementation |
| GXP-004: Interface/unit-conversion mappings must be approved before use, regardless of whether the arithmetic is coincidentally correct | `05_DDD_CONTEXT_MAP.md` E-405 | Capstone team | Pending implementation |
| GXP-005: Audit-trail integrity for privileged sessions — current state has a confirmed, unremediated gap | `06_DATA_GOVERNANCE_INTEGRITY.md` E-501/E-502 (47-minute audit-capture disablement overlapping a 28-minute unauthorized session overrun) | CISO (role-played) | **Currently FAILS** — `06_DATA_GOVERNANCE_INTEGRITY.md` R-502, no remediation evidence yet |
| GXP-006: Data residency — EU trial personal data must stay in approved regions; AI platform must not inherit the same violation pattern | `06_DATA_GOVERNANCE_INTEGRITY.md` E-508/E-509 | DPO (role-played) | **Currently FAILS for `ClinicalLake`**; AI platform check pending (`06_DATA_GOVERNANCE_INTEGRITY.md` R-503) |
| GXP-007: Legal hold precedence over data-subject deletion requests, once identity is confirmed | `06_DATA_GOVERNANCE_INTEGRITY.md` E-505/E-506/E-507 | Capstone team / DPO (role-played) | Blocked on identity confirmation — `06_DATA_GOVERNANCE_INTEGRITY.md` R-501 |
| SEC-001: `PatientKey`-linked graph traversal is purpose-limited to PV duplicate detection only | `08_KNOWLEDGE_GRAPH_DECISION.md` §6 | Capstone team | Pending implementation |
| SEC-002: Prohibited-action output rejected at the schema level regardless of prompt wording | `01_BUSINESS_CASE.md` E-004 | Capstone team | `tools/test_contracts.py` — PASS (6/6) |

## 5. Acceptance criteria

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What must be true before any workflow is demo-ready? | All FR-00x prohibited-action tests pass (already true, 6/6); at least one adversarial fixture per workflow beyond the existing 6 samples exists (not yet built); GXP-005/GXP-006 current-state failures are either remediated or explicitly accepted as residual risk with named ownership, not silently ignored. | Capstone team | `tools/test_contracts.py`; Gaps above |
| What blocks calling any requirement "done" prematurely? | Per `check_submission_structure.py`'s `substantive()` check, no artefact may contain unresolved `TODO`/`TBD`/`PLACEHOLDER` text below the length threshold — this traceability matrix itself is written to that standard. | Capstone team | `tools/check_submission_structure.py` |

## 6. Traceability matrix

| Requirement ID | Source evidence | Architecture / control | Test / evidence path | Result |
|---|---|---|---|---|
| FR-002 / SEC-002 | `01_BUSINESS_CASE.md` E-004 | `evaluation/contracts/batch_response.schema.json` | `tools/test_contracts.py` → `negative_batch_prohibited.json` | PASS |
| FR-004 | `01_BUSINESS_CASE.md` E-004 | `evaluation/contracts/pv_response.schema.json` | `tools/test_contracts.py` → `negative_pv_prohibited.json` | PASS |
| FR-006 | `01_BUSINESS_CASE.md` E-004, `04_PRODUCT_SERVICE_BLUEPRINT.md` E-306 | `evaluation/contracts/supply_response.schema.json` | `tools/test_contracts.py` → `negative_supply_side_effect.json` | PASS |
| GXP-001 | `03_STAKEHOLDER_DECISION_RIGHTS.md` E-103 | RACI matrix (§2 of that artefact) | `tools/test_contracts.py` (6/6) | PASS |
| FR-007 | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-301 | Output-vocabulary constraint | Not yet implemented | Pending |
| GXP-002 | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-301 | Evidence-item expansion UI requirement | Not yet implemented | Pending |
| GXP-005 | `06_DATA_GOVERNANCE_INTEGRITY.md` E-501/E-502 | Privileged-access/audit-trail control | No remediation evidence | **FAIL (current state)** |
| GXP-006 | `06_DATA_GOVERNANCE_INTEGRITY.md` E-508/E-509 | Backup/residency approval control | No remediation evidence | **FAIL (current state)** |
| GXP-007 | `06_DATA_GOVERNANCE_INTEGRITY.md` E-505–E-507 | Retention/hold precedence engine | Blocked on identity confirmation | Pending / blocked |
| NFR-006 | `08_KNOWLEDGE_GRAPH_DECISION.md` §3/§7 | In-process graph traversal design | Not yet load-tested | Pending |

## 7. Change and waiver control

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| How are the two current-state FAIL findings (GXP-005, GXP-006) handled — do they block this capstone's own submission? | They are pre-existing conditions in the challenge evidence, not defects introduced by this team's build; they are documented as residual risks the proposed AI capability must not worsen and, where relevant (GXP-006 for the AI platform itself), must not inherit. They do not block artefact completion but must appear, unresolved, in the final risk register and defence. | Capstone team | `06_DATA_GOVERNANCE_INTEGRITY.md` §7 |
| What requires a formal waiver rather than a fix? | None identified yet — every FAIL/Pending item above has a stated remediation path, not a requested exception. If any requirement is later judged infeasible within capstone scope, it must be logged here with accountable-role sign-off, not silently dropped. | Capstone team | N/A yet |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-901 | Risk | Two GxP requirements (GXP-005, GXP-006) currently fail against real evidence and have no remediation yet | High — must be disclosed in the final defence, not silently carried | Capstone team | Before final defence | Open |
| R-902 | Gap | FR-007 (disposition-language constraint) and GXP-002 (evidence-expansion UI) have no automated test yet | Medium | Capstone team | Phase 4 (Build) | Open |
| R-903 | Gap | NFR-006's in-process graph approach is unvalidated at production scale (carried from `08_KNOWLEDGE_GRAPH_DECISION.md` R-701) | Medium | Capstone team | Phase 4/5 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Every requirement in this register traces to a prior artefact's evidence ID | Cross-reference check (manual, this document) | Team review | §2–§4 above | Self-verified — no orphan requirements found |
| All 6 existing contract tests remain passing as new requirements are added | `tools/test_contracts.py` | Re-run on each change | `evaluation/contract_samples/*` | PASS (6/6, last run this session) |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
