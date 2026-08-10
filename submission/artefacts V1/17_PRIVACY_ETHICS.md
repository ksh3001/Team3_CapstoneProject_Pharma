# Privacy and Ethics

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Security / privacy lead (DPO consult) |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP lead; Product lead |
| Status | Draft — Stage 4 |
| Related requirements / ADRs | INJ-059–064, 041, 068; artefact 06 §6; PRI-001/002; knowledge PRIVACY_AND_PSEUDONYMISATION |

## Purpose

Assess privacy-by-design for AEGIS: purpose limitation, minimisation, retention vs legal hold/GxP, re-identification, cross-border, and ethics of secondary use — without treating challenge synthetic data as real personal data for live processing.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `data/privacy_risk.csv` | Risk register | Re-ID / sensitivity signals | Synthetic |
| E-002 | `data/genomic_data.csv` | Genomic set | Rare-disease identifying combinations (INJ-059) | Synthetic |
| E-003 | `data/consents.csv`; `data_exports.csv` | Consent/export | Secondary-use / cross-border proposals (INJ-060) | Synthetic |
| E-004 | `data/retention_rules.csv`; `legal_holds.csv`; `deletion_requests.csv` | Retain/hold/DSR | Conflict LH-44 vs DSR-17 (INJ-061) | Synthetic |
| E-005 | `data/patient_support_cases.csv` | Free text | Excess sensitive content (INJ-062) | Synthetic |
| E-006 | `data/data_residency.csv`; `backup_inventory.csv` | Residency | Unapproved region replica (INJ-064) | Synthetic |
| E-007 | `data/sensitive_segments.csv` | Segments | Pregnancy/paediatric in general queue (INJ-041) | Synthetic |
| E-008 | `knowledge/PRIVACY_AND_PSEUDONYMISATION.md` | Policy extract | Privacy expectations | Training |

## 1. Purpose limitation

| Purpose | Allowed AEGIS use | Prohibited |
|---|---|---|
| Batch review readiness | Cite manufacturing/lab/quality evidence | Secondary commercial targeting |
| PV intake support | Preserve verbatim needed for case handling | Broad affiliate narrative browsing without purpose |
| Supply draft options | Inventory/quality/constraint facts | Using patient-support hardship text for allocation ethics beyond policy |
| Model training (global) | Out of v1 assessment mode | EU trial data for unspecified training (INJ-060) without lawful basis |

## 2. Minimisation and retention

| Control | Design |
|---|---|
| Field minimisation | Return only fields needed for workflow contract; mask identifiers where purpose allows |
| Prompt/log retention | retention_rules: AI prompt logs delete after 90d unless evidence hold |
| GxP / PV retain | Clinical/ICSR retain per rules — do not auto-delete |
| Legal hold LH-44 | Active on NCB204-301 / NCB204-B24071 — restriction over delete |
| DSR-17 | Open delete request — evaluate restrict/segregate; not blind wipe of held GxP records |

## 3. Pseudonymisation and re-identification

| Risk | Handling |
|---|---|
| Genomic rare combinations (INJ-059) | Do not expose genomic payloads in default pack; abstain/escalate to DPO |
| Sensitive PV segments (INJ-041) | Flag pregnancy/paediatric; specialised review path |
| Patient-support free text (INJ-062) | Do not retrieve into model context by default; purpose check |
| “Pseudonymised” ≠ safe | Treat high-cardinality quasi-identifiers as identifying |

## 4. Cross-border and residency

| Issue | Control |
|---|---|
| Unapproved backup region (INJ-064) | Flag residency failure; AEGIS must not export to unapproved region |
| Cross-border secondary use (INJ-060) | Deny training/export purposes not in consent |
| Assessment mode | Offline local processing preferred |

## 5. Ethics and contestability

| Topic | Position |
|---|---|
| Allocation ethics | Draft options only; human Supply Governance + ethics policy (INJ-056) |
| Contestability | Human can override/abstention; audit reasons |
| Transparency | Show evidence citations and uncertainty; no hidden model authority |
| Works council / monitoring | AI telemetry not used for covert workforce performance scoring (stakeholder pack) |

## 6. Privacy tests (Stage 4/6)

| Test intent | Stage |
|---|---|
| Purpose mismatch deny | Stage 5 wiring |
| Sensitive segment flagged | Stage 5–6 |
| No genomic dump in default batch/PV pack | Stage 5 |
| Subgroup privacy leakage red-team | Stage 6 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Assumption | Synthetic data; real DPIA still required before production | Production blocker | DPO | Before go-live | Open |
| R-002 | Gap | Full lawful-basis matrix per jurisdiction not completed | Regulatory artefact deepen | DPO | Stage 4–7 | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Purpose limitation stated | §1 | Authz purpose bind | E-003 | Draft |
| Hold vs DSR method | §2 | Manual decision record | E-004 | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| GxP lead | Reviewer | Retain vs delete conflict explicit | §2 | 2026-08-10 |
