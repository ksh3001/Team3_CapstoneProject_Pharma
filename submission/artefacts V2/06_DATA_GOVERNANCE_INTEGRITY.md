# Data Governance and Integrity

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `05_DDD_CONTEXT_MAP.md`; `knowledge/GXP_DATA_INTEGRITY_STANDARD.md` (K-014); INJ-029, INJ-030, INJ-032, INJ-036, INJ-061, INJ-064 |

## Purpose

Assesses ALCOA+ integrity of the underlying data estate, resolves (or explicitly leaves open) authority conflicts between retention, legal hold and deletion obligations, and identifies where privileged access and audit-trail controls have already failed. Accountable owner: capstone team. Completion criteria: every ALCOA+ attribute failure traces to a specific record; retention/hold/deletion conflicts are surfaced, not silently resolved in either direction.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-501 | `data/audit_trails.csv` | Audit log, 2026-07-26 | System `LIMS-4`, event `audit_capture_disabled`, user `svc_admin`, start 00:11:00Z, end 00:58:00Z (47 minutes) | Matches INJ-029 exactly; this is a GxP-critical system (`LIMS-4` classified "GxP critical, validated" per `05_DDD_CONTEXT_MAP.md` context E-401-adjacent system inventory) |
| E-502 | `data/privileged_sessions.csv` | Session log, 2026-07-26 | Session `PS-901`, user `svc_admin`, purpose "master data repair", approved_window 00:00–00:30Z, actual_end 00:58Z | The session ran 28 minutes past its *approved* window (00:30→00:58), and audit capture (E-501) was disabled for the entire 00:11–00:58 span — meaning at least part of the unauthorized overrun period occurred with no audit trail at all |
| E-503 | `data/document_lineage.csv` | Lineage record, undated | `COA-RG78`: derived_from = `vendor_pdf_missing`; transcribed_by `AN-12`; verified_by `AN-13` | A two-person transcribe/verify control exists, but the stated `derived_from` value is literally "vendor_pdf_missing" — the two-person check cannot restore the ALCOA+ "Original" attribute once the source is gone |
| E-504 | `data/spreadsheet_inventory.csv` | Spreadsheet register, undated | `Dissolution_Acceptance_v7.xlsm`, owner `QC-IN`, intended_use "batch acceptance calculation", version_control = "email", verified = "no" | Matches INJ-032; used for a GxP-critical calculation (batch acceptance) with no validated version control and no confirmed verification |
| E-505 | `data/retention_rules.csv` | Retention policy, undated | `clinical_trial_source`: 25 years EU minimum, retain; `ICSR`: PV lifecycle retention, retain; `AI prompt logs`: privacy minimisation, delete after 90 days **unless evidence hold** | The AI-prompt-log rule already anticipates a hold exception — this is the mechanism this artefact must connect to E-506/E-507 |
| E-506 | `data/legal_holds.csv` | Legal hold register, undated, status active | `LH-44`: scope "NCB204-301 and NCB204-B24071", status = active | An active hold on both a trial (NCB204-301) and a specific batch (NCB204-B24071, the same batch already flagged incomplete in `02_DMAIC_WORKBOOK.md` E-201) |
| E-507 | `data/deletion_requests.csv` | Data-subject request register, undated, status open | `DSR-17`: subject_id `S-301-044`, scope "all biomarker and AI data", status = open | Subject ID prefix `S-301-` plausibly associates with trial `NCB204-301` (per E-506's scope naming), but this is **not explicitly confirmed** by a join field in the supplied data — treated as a hypothesis (Gap R-501), not asserted as fact |
| E-508 | `data/data_residency.csv` | Residency compliance check, undated | `EU trial personal data`: approved_regions = EU; observed_region = SG; source = "backup_replica" | Matches INJ-064 — a confirmed observed violation, not a theoretical risk |
| E-509 | `data/backup_inventory.csv` | Backup configuration, undated | System `ClinicalLake`: primary region DE, backup region SG, encryption = yes, approval = "missing" | Plausible root cause of E-508 — the SG backup replica exists and is encrypted, but was never formally approved, which is consistent with EU personal data ending up outside its approved region |
| E-510 | `knowledge/GXP_DATA_INTEGRITY_STANDARD.md` (K-014, approved 2026-02-15) | Synthetic NovaCura Global Policy | "Preserve attributable, legible, contemporaneous, original, accurate, complete, consistent, enduring and available records"; "Do not overwrite original values or audit evidence" | Governs the interpretation of E-501–E-504 below |

## 1. Dataset inventory and classification

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Which datasets in this evidence pull are GxP-critical vs. business-support? | GxP-critical: `LIMS-4` (audit trail subject, E-501), the batch-acceptance spreadsheet (E-504, despite being an unmanaged tool), clinical trial source and ICSR records (E-505). Business-support: AI prompt logs (E-505) — explicitly a shorter-retention, privacy-minimised category, not GxP source data. | Capstone team | E-501, E-504, E-505 |
| Is every GxP-critical dataset under formal version control? | No — E-504 shows a GxP-critical calculation (batch acceptance) running on a spreadsheet with `version_control = "email"` and `verified = "no"`. This is a control gap, not a data-quality nuance. | Capstone team | E-504 |

## 2. Source authority by object/context/time

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| When retention, legal hold and deletion obligations name the same object, which governs? | No single rule is universally authoritative — per `case/SOURCE_SYSTEM_FACT_PACK.md`, authority must be resolved by object, jurisdiction, effective time and process state. Here: if E-507's subject `S-301-044` is confirmed part of trial `NCB204-301` (E-506's active hold scope), the active legal hold (E-506) must take precedence over the deletion request (E-507) for any data within the hold's scope, and the AI-prompt-log retention rule (E-505) already encodes exactly this precedence ("delete after 90 days **unless evidence hold**"). | Capstone team | E-505, E-506, E-507 |
| Can this conflict be resolved right now? | No — the subject-to-trial link (Gap R-501) is not confirmed by a join field in the supplied data. This artefact does not resolve DSR-17's disposition; it documents the conflict and the precedence rule that would apply once identity is confirmed, per the abstain-on-unresolved-identity principle. | Capstone team | Gap R-501 |

## 3. Identity and master-data conflicts

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Are identity/master-data conflicts covered here or elsewhere? | Covered in detail in `05_DDD_CONTEXT_MAP.md` (compound code collision E-401, product strength ambiguity E-403/E-404, unapproved unit conversion E-405) — not re-derived in this artefact to avoid duplication. This section confirms no additional identity conflict was found in the retention/residency/audit evidence reviewed here. | Capstone team | `05_DDD_CONTEXT_MAP.md` |

## 4. Quality and ALCOA+ assessment

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Attributable / Contemporaneous failure | E-501+E-502 combined: a privileged session exceeded its approved window by 28 minutes (00:30→00:58) while audit capture was simultaneously disabled for 47 minutes (00:11→00:58) on a GxP-critical system (`LIMS-4`). Any change made during the unauthorized, unaudited overlap (00:30–00:58) cannot be attributed or contemporaneously evidenced — this is a compound failure, not two independent minor findings. | Capstone team | E-501, E-502 |
| Original failure | E-503: `COA-RG78`'s source vendor PDF is stated as missing. The two-person transcribe/verify control (`AN-12`/`AN-13`) is a good compensating control for *accuracy of transcription*, but does not and cannot restore the "Original" ALCOA+ attribute — this distinction must not be blurred in any assurance case. | Capstone team | E-503 |
| Accurate / Consistent risk | E-504: a GxP-critical batch-acceptance calculation with no validated version control and no confirmed verification carries an open accuracy risk for every batch that has relied on it, not just a documentation gap. | Capstone team | E-504 |
| Does any of this block the AI evidence-reconciliation workflow from using these records? | No — Workflow A's role is precisely to *surface* these findings (missing original, unapproved spreadsheet, audit gap) as evidence-completeness flags to the EU QP, not to certify around them. This confirms the workflow's value proposition traces to real, not hypothetical, defects. | Capstone team | `01_BUSINESS_CASE.md` E-004 |

## 5. Lineage and transformation controls

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What lineage control exists today? | A transcribe/verify two-person pattern (E-503: `AN-12` transcribes, `AN-13` verifies) — present but insufficient alone when the upstream original is missing. | Capstone team | E-503 |
| What lineage control is missing? | A requirement to retain or re-derive the original signed source *before* transcription is permitted to close as complete — currently, transcription without a retained original is not blocked by any evidenced control. | Capstone team | E-503 |
| Does the reconciliation workflow perform any transformation itself? | Per `05_DDD_CONTEXT_MAP.md` §2/§6, the AI context must not become a new, unmanaged transformation point — any transformation it performs (e.g., normalization, unit conversion) must itself be logged with source, rule version and responsible role, consistent with K-014's "document transformations, corrections, versions and responsible roles." | Capstone team | E-510, `05_DDD_CONTEXT_MAP.md` |

## 6. Retention, residency and legal hold

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Is the data-residency violation (E-508) still active? | Stated as the observed condition in the evidence with no remediation record — treated as currently unresolved. Root cause plausibly traces to E-509 (`ClinicalLake` backup replica to SG configured with encryption but missing formal approval). | Capstone team | E-508, E-509 |
| Does this affect the AI platform itself? | Directly relevant — if the AI evidence-reconciliation platform's own vector store, logs or model context reference EU trial personal data and inherits the same backup/replication configuration as `ClinicalLake`, it could reproduce the same residency violation. This must be checked explicitly during architecture (`10_C4_ARCHITECTURE.md`), not assumed absent. | Capstone team | E-508, E-509 |
| How should the DSR-17/LH-44 potential conflict (§2) be handled operationally? | Escalate to confirm the subject-to-trial link (Gap R-501) before any action; if confirmed, apply the hold-precedence rule already implied by E-505; if not confirmed, the deletion request proceeds under standard privacy rules subject to `knowledge/ECONSENT_AND_SECONDARY_USE.md` (not reviewed in this artefact). | Capstone team / DPO (role-played) | E-505, E-506, E-507 |

## 7. Stewardship and issue remediation

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Who owns remediation of each finding? | Not named in supplied evidence for any of E-501–E-504, E-508, E-509 — this is itself a governance gap. Provisional assignment pending team decision: audit/privileged-access findings (E-501/E-502) → CISO (`03_STAKEHOLDER_DECISION_RIGHTS.md` E-101); document lineage/spreadsheet findings (E-503/E-504) → CQO; residency findings (E-508/E-509) → DPO. | Capstone team | `03_STAKEHOLDER_DECISION_RIGHTS.md` |
| What must NOT happen during remediation? | Per K-014, original values or audit evidence must not be overwritten while remediating — e.g., fixing the `Dissolution_Acceptance_v7.xlsm` version-control gap (E-504) must preserve the existing (uncontrolled) version history as historical evidence, not silently replace it with a clean v1 of a new controlled version. | Capstone team | E-510 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-501 | Gap | `DSR-17` subject `S-301-044` not explicitly confirmed linked to trial `NCB204-301` (E-506's hold scope) — naming pattern is suggestive, not proven | High — determines whether an active legal hold blocks a data-subject deletion request | Capstone team / DPO | Before DSR-17 is actioned in any way | Open |
| R-502 | Risk | Unaudited privileged-session overrun (E-501/E-502) means any master-data change made 00:30–00:58Z on 2026-07-26 has no contemporaneous audit evidence | High — could affect trust in any master-data record touched during that window | CISO (role-played) | Immediate | Open |
| R-503 | Risk | AI platform's own data residency has not been checked against the `ClinicalLake` pattern (E-508/E-509) | Medium-High — could silently reproduce a known violation | Capstone team | Before architecture sign-off (`10_C4_ARCHITECTURE.md`) | Open |
| R-504 | Gap | No named remediation owner for any of the five findings in this artefact | Medium | Capstone team | Phase 3 (Specify) | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| AI context does not inherit the `ClinicalLake` residency violation | Data-residency check in architecture design | Not yet implemented | — | Pending |
| Legal hold precedence over deletion request is enforced once identity confirmed | Retention/hold policy engine | Not yet implemented | — | Pending, blocked on R-501 |
| AI transformations are logged with source/rule version (§5) | Transformation-logging design | Not yet implemented | — | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
