# GxP Lifecycle and Validation

> Phase 3. Intended use, risk class, and lifecycle controls for an **advisory** evidence assist — not a release/execution system.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / GxP–quality lead (named TBD) |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Architecture; Security; Product |
| Status | Draft |
| Related requirements / ADRs | DEC-010/012; artefacts 04, 10–12, 14–15; INV-01…08 |

## Purpose

Define GxP lifecycle expectations (intended use → retirement) so validation/assurance effort matches **patient/product risk from misuse**, not from aspirational autonomy.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | `ai_use_boundaries.csv` / artefact 04 | Intended vs prohibited |
| E-002 | `decision_rights.csv` | Human accountability |
| E-003 | `system_inventory.csv` | AI-EVIDENCE = business support / pilot |
| E-004 | evaluation contracts | Fail-closed outputs |
| E-005 | Package scope | Synthetic offline training case |

## 1. Intended use and boundary

| Item | Statement |
|---|---|
| Intended use | Assist authorized humans by packaging cited evidence, contradictions, gaps, and abstentions for batch readiness review, PV intake support, and draft supply options |
| Intended users | EU QP (consumer of batch package), Safety Physician / PV staff, Supply planners / governance, trained operators |
| Operating environment | Offline-capable local package; synthetic/challenge data in assessed mode |
| Prohibited use | Autonomous batch disposition; final PV safety/reportability conclusions; stock reserve/allocate/ship/recall; treating untrusted docs as executable SOPs |
| Out of scope | Replacing validated LIMS/MES/QMS; producing regulatory submissions |

## 2. Risk classification

| Dimension | Classification (POC) | Rationale |
|---|---|---|
| Direct control of product release | **None** (by design) | No disposition output field |
| Influence on human decision | **Medium** if automation bias | Mitigate via conflict visibility + HITL |
| Data integrity impact | **High if citations forged** | Mandatory evidence_item + hash |
| Overall GxP criticality for assist | **GxP-relevant support** with high-risk *functions* gated (see CSA) | Not “validated release system” |

## 3. Lifecycle deliverables

| Phase | Deliverable | POC evidence |
|---|---|---|
| Concept | Intended/prohibited use | Artefact 04; DEC-012 |
| Requirements | Traceability | Artefact 09 |
| Design | C4 / ADRs / integration | Artefacts 10–12 |
| Risk | QRM | Artefact 15 |
| Assurance | CSA plan | Artefact 14 |
| Build | Deterministic core + tests | Phase 5 `src/` |
| Test | Contract + inject suites | Phase 3/6 |
| Release | Go / conditional / pivot | Artefact 30 later |
| Operate | Runbooks + AI-disabled | Phase 7 |
| Retire | Decommission + retention | §7 |

## 4. Validation / assurance strategy

| Approach | Application |
|---|---|
| Risk-based CSA (artefact 14) | Focus assurance on high-risk functions (authZ, prohibited fields, units, instruction trust) |
| Spec → test → build | Contracts and negatives before loaders/LLM |
| Supplier assessment | Model/vendor optional; ports & adapters; no sole reliance |
| Continuous | Contract suite in every evaluate run |

**Claim discipline:** This document does **not** assert Part 11 certification or completed PQ — it defines the plan for the capstone POC.

## 5. Supplier and configuration controls

| Item | Control |
|---|---|
| Challenge package | Hash-verified; do not alter evidence |
| Optional LLM | Adapter boundary; version pinned; disable switch |
| Config | Purpose, as-of, feature flags in audited config |
| Tools | Signed allowlist only (ADR-034) |

## 6. Change and periodic review

| Trigger | Action |
|---|---|
| Schema/ADR change | Compatibility tests + decision log |
| New inject class / interface version | Update ACL + QRM |
| Gate defect escape | Incident + CSA defect handling |
| Periodic | Before defence; after any pivot |

## 7. Retention and retirement

| Record | Retention intent (POC) |
|---|---|
| Audit events / responses | Keep under `submission/evidence` for defence |
| Model prompts/logs | No real PHI/secrets; synthetic only |
| Retirement | Disable adapters; archive hashes; do not delete GxP-relevant audit trail |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-331 | Risk | Users over-trust readiness_state | Wrong human decision | GxP + HF | Open → Phase 4 |
| A-019 | Assumption | Pilot/business-support class fits advisory design | Under-assurance if treated as release system | GxP | Open |

## Traceability and acceptance

| Claim | Control | Test | Result |
|---|---|---|---|
| Intended use frozen | §1 / DEC-012 | Review | Draft |
| Prohibited acts blocked | Contracts + gates | Schema PASS; runtime RED | Phase 3 |
| Lifecycle complete enough for POC | §3 | Hour-18 review | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | GxP | Pending | | |
