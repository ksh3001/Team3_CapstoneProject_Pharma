# Privacy and Ethics

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `06_DATA_GOVERNANCE_INTEGRITY.md`; ADR-010; INJ-017, INJ-035, INJ-060, INJ-061, INJ-064, INJ-068; K-011, K-020, K-029 |

## Purpose

Maps purpose, consent, minimisation, residency, rights and ethical trade-offs for the three workflows against already-observed privacy failures (withdrawn biomarker consent still processed, unapproved cross-border export, EU→SG residency breach, open DSR vs active legal hold). Accountable owner: DPO (role-played). Completion criteria: every D09 inject has a control decision; DSR-17 is not silently executed or silently refused without documenting the hold-link gap.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-1701 | `data/consents.csv` | Consent register; C-044 effective 2026-07-20T10:15:00+05:30 | `C-044` subject `S-301-044`, purpose `trial_and_biomarker`, status = **`withdrawn_biomarker`** | Matches INJ-017 pattern when paired with processing event |
| E-1702 | `data/processing_events.csv` | Processing log | `PE-9` specimen `SP-044-A`, purpose `biomarker_model`, status `completed`, consent_check = **`cached_active`** | Downstream processing completed after biomarker withdrawal using a stale cached consent check — fact of failure, not interpretation |
| E-1703 | `data/data_exports.csv` | Export register | `EX-77`: NCB204 trial biomarker, EU→US, purpose `global model training`, approved = **no** | Matches INJ-060 — unapproved cross-border secondary use |
| E-1704 | `data/data_residency.csv` + `data/backup_inventory.csv` | Residency / backup | EU trial personal data approved EU, observed **SG** via `backup_replica`; ClinicalLake backup SG with approval = missing | Matches INJ-064; carried from `06_DATA_GOVERNANCE_INTEGRITY.md` E-508/E-509 |
| E-1705 | `data/deletion_requests.csv` + `data/legal_holds.csv` + `data/retention_rules.csv` | Rights / hold / retention | `DSR-17` open for `S-301-044` "all biomarker and AI data"; `LH-44` active on `NCB204-301` and `NCB204-B24071`; AI prompt logs delete@90d unless evidence hold | Matches INJ-035/INJ-061; subject↔trial link still unconfirmed (R-501) |
| E-1706 | `data/security_events.csv` SEC-1 | Security log | Cross-affiliate narrative query unblocked | Privacy-relevant exfiltration of safety narratives (INJ-068) |
| E-1707 | `knowledge/ECONSENT_AND_SECONDARY_USE.md` (K-011, 2026-02-28) | Synthetic NovaCura Global Policy | Propagate withdrawal; map each use to purpose; stop incompatible secondary use while preserving required records | Scenario-internal authority |
| E-1708 | `knowledge/PRIVACY_AND_PSEUDONYMISATION.md` (K-020, 2026-03-20) | Synthetic NovaCura Global Policy | Minimise; separate identifiers; assess re-identification; control access/purpose/retention/transfer | Scenario-internal authority |
| E-1709 | `knowledge/SUPPLY_ALLOCATION_ETHICS.md` (K-029, 2026-05-28) | Synthetic NovaCura Global Policy | Visible patient/trial/compassionate constraints; accountable governance for allocation | Ethics for Workflow C |

## 1. Purpose and data map

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Workflow A data | Batch evidence objects (genealogy, LIMS, deviations, COA lineage) — primarily GxP quality data; may reference identifiers that join to trial/batch holds (E-1705). Purpose: reconcile/cite/flag/abstain only. | Capstone team / DPO | `ai_use_boundaries.csv`; E-1705 |
| Workflow B data | ICSR narratives, MedDRA codes, listedness sources — special-category health data. Purpose: extract/normalize/cluster/cite. | Capstone team / DPO | E-1706; prior PV artefacts |
| Workflow C data | Inventory, allocation constraints, recall genealogy — may encode patient-impact ethics constraints (E-1709). Purpose: draft options only. | Capstone team | E-1709 |
| Biomarker / omics secondary use | Explicitly out of intended purpose for this POC unless separately approved — E-1703 shows an unapproved EU→US training export already occurred. | DPO | E-1703, E-1707 |

## 2. Permission/consent assumptions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Can cached consent be trusted? | No — E-1701+E-1702: biomarker withdrawal recorded, yet `PE-9` completed with `consent_check=cached_active`. Live consent state must be re-checked at processing time (same pattern as live IAM in artefact 16). | Capstone team / DPO | E-1701, E-1702, E-1707 |
| Assumption we refuse | That "trial" consent implies "biomarker_model" / "global model training" secondary use. E-1703 is unapproved; E-1707 requires purpose mapping. | DPO | E-1703, E-1707 |
| Decision | Any AI path that would ingest biomarker or trial personal data for model training is out of scope for this submission and must abort on withdrawn or unapproved purpose. | Capstone team | E-1701–E-1703 |

## 3. Minimisation and pseudonymisation

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Policy requirement | Minimise; separate direct identifiers from working data; assess linkage risk (E-1708). | DPO | E-1708 |
| Current POC posture | Deterministic workflows operate on already-pseudonymised IDs present in challenge CSVs (`S-301-044`, case IDs). No new direct identifiers are collected. Prompt-log retention already short (90 days) unless hold (E-1705). | Capstone team | E-1705, E-1708 |
| Gap | No formal re-identification assessment artefact for joining PV narratives + genealogy + trial IDs in one analyst session. | Capstone team / DPO | Gap R-1701 |

## 4. Secondary use and re-identification

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Observed secondary-use failure | EX-77 unapproved export for global model training (E-1703). | DPO | E-1703 |
| Control decision | Secondary use requires explicit approval record; absence of approval = deny (fail closed). Not "approve by silence." | DPO | E-1703, E-1707 |
| Re-identification | Subject token `S-301-044` plus trial/batch naming in LH-44 creates a plausible link used by `privacy_gates.py` to abstain — the gate treats plausible link as reason to block automatic deletion, not as proof of identity. | Capstone team | E-1705; `privacy_gates.py` |

## 5. Residency and cross-border controls

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Current-state violation | EU trial personal data observed in SG via backup replica (E-1704). | DPO | E-1704 |
| Cross-border export | EX-77 EU→US unapproved (E-1703). | DPO | E-1703 |
| Decision for AI platform | Do not place EU trial personal data, ICSR free text, or biomarker payloads into regions/services lacking an approved residency record. Offline deterministic mode must remain available without cross-border model calls. | Capstone team / DPO | E-1704; ADR offline continuity |
| Cross-affiliate access | SEC-1 pattern denied by purpose-limitation gate (E-1706). | CISO / DPO | Artefact 16; `security_gates.py` |

## 6. Rights, retention and legal hold

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| DSR-17 vs LH-44 | Open deletion request vs active hold whose scope names trial/batch that *may* include the subject (E-1705). Identity join not proven → abstain from deletion (`privacy_gates.check_deletion_against_hold` → `abstain_unconfirmed_link`). | DPO | E-1705; PUB-11; `test_privacy_gates.py` |
| Precedence if link confirmed | Active legal hold and GxP retention (clinical 25y, ICSR lifecycle) outrank privacy-minimisation deletion for in-scope records; AI prompt logs already encode "unless evidence hold" (E-1705). | DPO | E-1705, E-1707 |
| What we will not do | Auto-delete biomarker/AI data for DSR-17 while LH-44 is active and link unresolved; auto-deny the data subject without documenting the gap. | DPO | R-501 / R-1702 |

## 7. Ethical trade-offs and oversight

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Shortage allocation ethics | Workflow C must surface trial/compassionate/patient constraints and require Supply Governance Board approval — never silent utilitarian optimisation (E-1709). | Supply Governance Board | E-1709 |
| Privacy vs pharmacovigilance | Deleting ICSR/source needed for safety obligations would harm patients; retention rules already retain ICSR (E-1705). Trade-off resolved in favour of safety retention with documented DSR handling. | DPO / PV | E-1705 |
| Oversight | DPO for privacy rights/residency; CISO for exfiltration; CQO/QP for GxP record integrity; board for allocation ethics. | Per `03_STAKEHOLDER_DECISION_RIGHTS.md` | Prior artefact |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1701 | Gap | No formal re-identification assessment for multi-workflow analyst sessions | Medium | DPO | Before production pilot | Open |
| R-1702 | Gap | Subject↔trial join for DSR-17/LH-44 still unconfirmed (same as R-501) | High | DPO | Before DSR-17 actioned | Open |
| R-1703 | Risk | Consent cache pattern (E-1702) may exist in other systems beyond PE-9 | High | DPO / Clinical | Immediate inventory | Open |
| R-1704 | Assumption | Challenge CSV subject IDs are already at acceptable pseudonymisation for training use of this package | Medium if wrong | Capstone team | Defence | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| DSR vs hold abstains when link unconfirmed | `privacy_gates.check_deletion_against_hold` | `test_privacy_gates.py`; PUB-11 | E-1705 | PASS |
| Cross-affiliate narrative denied | `check_purpose_limitation` | `test_security_gates.py` | E-1706 | PASS |
| Unapproved secondary export blocked | Policy decision; no export executor in POC | Manual / future gate | E-1703 | Designed, not coded |
| Live consent check (not cache) | Required by this artefact | Not yet a `submission/src` module | E-1701, E-1702 | Open |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | DPO (role-played) | — | — | — |
