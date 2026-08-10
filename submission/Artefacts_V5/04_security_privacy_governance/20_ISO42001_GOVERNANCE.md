# ISO/IEC 42001-Aligned Governance

> Team3 Phase 4 artefact (template 20). **Aligned mapping** for delivery — **not** ISO/IEC 42001 certification or AIMS audit pass.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Governance / Architecture |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Product; Security; Evaluation |
| Status | Phase 4 — provisional |
| Related | Templates 15–19; ADR register; Prompt 12/13 assurance & proposal |

## Purpose

Map AEGIS POC controls to an AI Management System lens (policy, inventory, risk, lifecycle, suppliers, monitoring, evidence) so governance is design-time, not retrofit.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-42-01 | REGULATORY_BOUNDARY_PACK | 42001-aligned AI management expected where applicable |
| E-42-02 | Decision log D-001…D-019 | Governance decisions |
| E-42-03 | Phase 3 QRM / CSA / GxP lenses | Risk + assurance |
| E-42-04 | Prompt 12 production_readiness / evaluation_report | Demo conditional-go; prod no-go |
| E-42-05 | `working/audit/` AuthZ snapshots | Operational evidence (POC) |

## 1. AI policy and objectives

| Policy element | Team3 stance |
|---|---|
| Objective | Fail-closed evidence assist; humans retain regulated decisions |
| AI default | Off / optional port (ADR-002); deterministic continuity required |
| Prohibited | Disposition, final PV, allocate/ship/recall, cache-over-IAM, poisoned tools |
| Framing | `hypothesis` until P0 baselines acquired |
| Non-claim | Not 42001 certified; not validated GxP DSS |

## 2. Use-case inventory and ownership

| Use-case ID | Description | AI used? | Owner | Status |
|---|---|---|---|---|
| UC-BATCH | Batch evidence pack | No (assessed) | Quality context | In POC |
| UC-PV | PV intake packet | No (assessed) | PV context | In POC |
| UC-SUPPLY | Supply options draft | No (assessed) | Supply context | In POC |
| UC-AUTHZ | Purpose-bound AuthZ | Rules only | Security | In POC |
| UC-EVAL | Hard-gate evaluate | Rules only | Evaluation | In POC |
| UC-NARR | Optional narrator | Disabled assessed | Architecture | Inventory only |

## 3. Risk and impact assessment

| Hook | Artefact |
|---|---|
| Quality risk | `15_QUALITY_RISK_MANAGEMENT.md` |
| Threat/abuse | `16_THREAT_ABUSE_MODEL.md` |
| Privacy/ethics | `17_PRIVACY_ETHICS.md` |
| Human factors | `18_RESPONSIBLE_AI_HUMAN_FACTORS.md` |
| Act applicability | `19_EU_AI_ACT_APPLICABILITY.md` (abstain class) |

Impact: patient/process risk controlled by **blocking** high-impact actions, not by monitoring alone.

## 4. Lifecycle controls

| Stage | Control in POC |
|---|---|
| Design | ADRs; C4; contracts additionalProperties false |
| Build | Tests-first hard gates; module_rules |
| Verify | pytest 32; evaluate runner |
| Operate | Local audit; modes offline/ai_disabled |
| Change | Contract version bump + Evaluation approval; ADR reopen triggers |
| Retire | Vendor exit deferred Phase 7+ template 27 |

## 5. Supplier and data governance

| Topic | Stance |
|---|---|
| Model supplier | None on assessed path; hash mismatch (INJ-070) blocks enablement |
| Challenge data | Immutable read; D-001 |
| Knowledge authority | Catalog + applicability; quarantine untrusted |
| Privacy suppliers / processors | N/A in local POC |

## 6. Monitoring, incidents and improvement

| Topic | POC | Production gap |
|---|---|---|
| AuthZ / quarantine / side-effect metrics | Local files + evaluate | Central SIEM/SOC |
| Incidents (exfil, poison, ransomware) | Documented in threat model | IR runbook Phase 7 (tmpl 25) |
| Continual improvement | Decision log; residual risks | Formal AIMS cadence |

## 7. Evidence mapping

| 42001-style evidence | Path |
|---|---|
| AI inventory | §2 this file |
| Risk assessments | Templates 15–19 |
| Approvals / decisions | `00_ASSUMPTIONS_DECISION_LOG.md` |
| Evaluation results | `artefacts/prompts/12_assurance/*`; pytest |
| Audit logs | `submission/working/audit/` (runtime) |
| Missing-control flags | R-* in Phase 4; prod no-go D-012 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-42-01 | Gap | No organisational AIMS / certification program | Accepted (training) |
| R-42-02 | Gap | Post-market monitoring not applicable to POC | Open for prod |
| R-42-03 | Assumption | Inventory complete for assessed scope | Revisit if UC-NARR enabled |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Use-cases inventoried | §2 | Pass |
| Risk hooks linked | §3 | Pass |
| No certification claim | Document control | Pass |
| Prod governance incomplete | §6 gaps; D-012 | Documented |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Governance | Owner | Aligned map sufficient for Phase 4 | Cert program out of scope | 2026-08-07 |
