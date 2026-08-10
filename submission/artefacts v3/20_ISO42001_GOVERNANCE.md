# ISO/IEC 42001-Aligned Governance

> Phase 4. AIMS-oriented delivery controls for the assist. **Not** a claim of ISO/IEC 42001 certification.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / GxP + Security–privacy |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Product; Architecture; Evaluation |
| Status | Draft |
| Related requirements / ADRs | Artefacts 13–19, 21; DEC-010; trust-risk-security skill |

## Purpose

Map the POC to an AI Management System–style control set (inventory, risk, lifecycle, roles, improvement) so governance evidence exists even though NovaCura is “not certifying yet.”

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | artefacts 01–19 | Existing governance spine |
| E-002 | decision / assumptions logs | Decisions & open items |
| E-003 | system_inventory.csv | AI-EVIDENCE pilot classification |
| E-004 | evaluation suites plan | Monitoring hooks |

## 1. AI policy and objectives

| Policy statement (POC) | Objective |
|---|---|
| AI remains advisory; humans decide regulated acts | Zero prohibited autonomous executions |
| Fail closed on trust/authZ/schema | Deny by default |
| Offline deterministic continuity required | AI-disabled path always available |
| No silent evidence mutation | Preserve provenance |

## 2. Use-case inventory and ownership

| Use-case ID | Description | Owner role | Risk posture |
|---|---|---|---|
| UC-BATCH | Batch evidence packaging | Domain + GxP; QP consumer | GxP-relevant support |
| UC-PV | PV intake support | Domain + Safety | GxP-relevant support |
| UC-SUPPLY | Draft supply options | Domain + Supply board | Business/GxP-adjacent |
| UC-LLM-OPTIONAL | Constrained GenAI assist port | Architecture | Optional; disableable |

## 3. Risk and impact assessment

| Assessment | Artefact |
|---|---|
| Quality risk (QRM) | 15 |
| Threat/abuse | 16 |
| Privacy/ethics | 17 |
| Human factors | 18 |
| EU AI Act awareness | 19 |
| CSA high-risk functions | 14 |

## 4. Lifecycle controls

| AIMS theme | POC control |
|---|---|
| Design | ADRs 031–041; contracts v1 |
| Development | Tests before inference; gates stubs→impl |
| Verification | Contract + inject + trust suites |
| Deployment | Single-package offline (ADR-041) |
| Operation | Runbooks Phase 7; AI-disabled |
| Retirement | Retain audit; disable adapters |

## 5. Supplier and data governance

| Topic | Control |
|---|---|
| Model/vendor | Ports & adapters; pin versions; eval on change |
| Tools | Signed allowlist (`tool_allowlist.json`) |
| Data | Challenge hashes immutable; submission-only writes |
| Knowledge | Instruction eligibility DEC-022 |

## 6. Monitoring, incidents and improvement

| Event | Response |
|---|---|
| Prohibited attempt | Block + audit + Security note |
| Gate defect escape | Critical — stop release claims |
| Bias / a11y defect | Product+GxP; fix before defence if critical |
| Continual improvement | Decision log + ADR revisit triggers |

## 7. Evidence mapping

| 42001-oriented artefact | Path |
|---|---|
| AI inventory | §2 this doc |
| Risk/impact | 15–19 |
| Approvals / decisions | DECISION_LOG |
| Evaluation results | Phase 6 `evaluation_results.json` (later) |
| Audit logs | Response `audit` field + evidence/ |
| Incident path | INCIDENT runbook (Phase 7) |
| System/model card | Assurance case 21 + blueprint 04 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-441 | Gap | No formal AIMS certification attempt | External audit unreadiness | GxP | Accepted for POC |
| A-025 | Assumption | Mapping above is sufficient governance evidence for capstone defence | Scorer expects more | Team | Open |

## Traceability and acceptance

| Claim | Control | Evidence | Result |
|---|---|---|---|
| Inventory exists | §2 | This artefact | Draft |
| Risk assessments linked | §3 | 14–19 | Draft |
| No certification claim | Purpose banner | Defence | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | GxP | Pending | | |
