# EU AI Act Applicability

> Team3 Phase 4 artefact (template 19). **Awareness analysis only** — not legal advice, not a conformity assessment, not “Act compliant.” Escalate classification to Legal/Compliance for any real deployment.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Governance / Legal awareness |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Product; GxP; Security |
| Status | Phase 4 — provisional; **abstain on definitive risk class** |
| Related | REGULATORY_BOUNDARY_PACK; D-006/D-007; ADR-002; A-003 |

## Purpose

Bound intended purpose, system boundary, and provisional Act lenses for the assessed AEGIS assist POC; list provider/deployer obligation triggers and change conditions that force re-analysis.

## Evidence register

| Evidence ID | Source | Fact used | Limitation |
|---|---|---|---|
| E-EU-01 | `case/REGULATORY_BOUNDARY_PACK.md` | AI-governance analysis where in scope | Research anchor |
| E-EU-02 | Intended use / PRD / decision_rights | Assist only; humans decide | Synthetic case |
| E-EU-03 | ADR-002 / AC-051 | LLM off assessed path | POC |
| E-EU-04 | Contracts / DoD | No disposition / final PV / allocate | Hard gates |
| E-EU-05 | LICENSE_AND_USE / A-003 | Training scenario | Not real market placing |

## 1. Intended purpose and actor role

| Item | Response |
|---|---|
| Intended purpose (POC) | Assemble evidence packs and draft options for Quality / PV / Supply reviewers under purpose-bound AuthZ |
| Not intended | Autonomous certification, final PV conclusions, allocation/shipment/recall, entitlement grant |
| Actor role (training) | Participant team building a fictional deployer-style assist; **no market placement** |
| Framing | `hypothesis` — not decision-ready production DSS |

## 2. System and component boundary

| In boundary | Out of boundary |
|---|---|
| Workflow runtime, AuthZ, rules, evaluate, local audit | QP certification systems |
| Optional LLM narrator port (**disabled** assessed) | MES/WMS/Safety write execution |
| Challenge data read ACL | Production IAM/IdP |

Component with AI techniques: optional narrator only; assessed continuity is deterministic/rules-only.

## 3. Risk classification analysis

| Lens | Provisional finding | Confidence |
|---|---|---|
| Prohibited AI practices | No evidence AEGIS implements prohibited manipulative social scoring etc. in POC | Med — Legal confirm |
| High-risk (Annex III-style medical devices / safety components) | **Abstain** — pharma quality/PV/supply *assist* may attract heightened scrutiny if it substantially influences health/safety decisions; current design keeps humans determinative and LLM off | Low without Legal |
| GPAI | Not used as general-purpose model provider in assessed path | High for POC |
| Transparency / limited risk | If narrator enabled later, disclose AI-assisted summaries to users | Contingent |

**Decision:** Do **not** self-declare high-risk or exempt. Record open legal question **Q-EU-01**. Production remains **no-go** pending compliance owner classification.

## 4. Prohibited / high-risk / transparency considerations

| Topic | POC control |
|---|---|
| Excessive agency toward health/safety outcomes | Schema + no write plane + HITL |
| Biometric / emotion etc. | Out of scope |
| Transparency | CLI modes expose `deterministic_offline` / `ai_disabled`; no silent AI on assessed path |
| Human oversight | Named roles outside system (template 18) |

## 5. Provider/deployer obligations

| If role were… | Obligation posture (awareness) |
|---|---|
| Deployer of high-risk (hypothetical) | Instructions for use, human oversight, monitoring, logging — **not implemented as production program** |
| Provider | Technical docs, risk mgmt, post-market — **not claimed** |
| POC training | Demonstrate governance-by-design artefacts only |

## 6. Evidence and assumptions

| Assumption | Impact if wrong |
|---|---|
| A-003 synthetic / no real patients | Classification exercise invalid for real data |
| LLM remains off on assessed path | Enabling generative assist reopens Act + GxP analysis |
| Outputs remain advisory | Any determinative wiring → reopen §3 |

## 7. Change triggers

Re-run this analysis when any of:

1. LLM/narrator enabled on assessed or production path  
2. Write adapters / side effects introduced  
3. Outputs used as sole basis for release, PV final, or allocation  
4. Real personal data or EU market placement  
5. Vendor model change (INJ-070 class)  

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| Q-EU-01 | Gap | Definitive Act risk class needs Legal/Compliance | Open |
| R-EU-01 | Risk | Board pressure toward automation misread as high-risk productization | Open (R-002) |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Applicability analysed with abstention | §3 | Pass (process) |
| No “Act compliant” claim | Document control + §5 | Pass |
| Change triggers defined | §7 | Pass |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Governance | Owner | Abstain on risk class | Q-EU-01 logged | 2026-08-07 |
