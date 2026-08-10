# DMAIC Workbook

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `01_BUSINESS_CASE.md` §3/§6 (R-002, R-003); INJ-021, INJ-028, INJ-029, INJ-031, INJ-033, INJ-034, INJ-036, INJ-005 |

## Purpose

This workbook root-causes the release-lead-time problem stated in `01_BUSINESS_CASE.md` §1, to (a) close Gap R-002 (no absolute baseline figure) as far as available evidence allows, and (b) test Assumption A-002/Gap R-003 — whether `master_data_repair` and `rules_workflow` (E-003) target overlapping or distinct root causes, which determines whether their estimated values can be treated as even partly additive. Accountable owner: capstone team. Completion criteria: every named root cause traces to a concrete evidence row, not a generic category.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-201 | `data/release_packets.csv` | Release-packet line items, undated | Batch `NCB204-B24071`: "CMO audit commitment 2025-14" = missing; "CoA" = present | Two-row sample; matches INJ-028 (Qualified Person evidence gap) exactly |
| E-202 | `data/change_controls.csv` | Change-control register, undated | `CC-77`: MES vendor hotfix 11.2.4 installed as "emergency" change; retrospective_approval = missing | Matches INJ-034 (change-control bypass) exactly |
| E-203 | `data/certificates_analysis.csv` | Certificate/CoA analysis, undated | `COA-RG78`, material lot `RG-78`: source = "manual transcription"; signature = "not available"; value = 99.1% | Matches INJ-036 (ALCOA+ provenance break); the original signed source is stated elsewhere in the case as unlocatable |
| E-204 | `data/system_inventory.csv` + `data/validation_inventory.csv` | Two independent inventories, undated | System `AI-EVIDENCE` is classified "business support / pilot" in `system_inventory.csv`, but appears as "conditionally_released" (Quality inventory), "research_only" (Architecture catalog) and "validated" (Vendor portal) across three sources in `validation_inventory.csv` | Matches INJ-031 (validation-state ambiguity) exactly — critically, this is the AI-assist system category itself, not an unrelated system |
| E-205 | `data/deviations.csv` + `data/capa_records.csv` | Deviation/CAPA registers, undated | `DEV-201` (taxonomy: mixing_time) closed under `CAPA-31` ("operator retraining"), effectiveness check = "no recurrence under code mixing_time" = effective. `DEV-244` (taxonomy: process_duration) is open and marked `similarity_to: DEV-201` | Matches INJ-033 (CAPA effectiveness failure) — the CAPA's own effectiveness check is scoped to its original taxonomy code, so a recurrence filed under a different code would not be caught by it |
| E-206 | `data/organisations.csv` | Organisation register, undated | `NTG` (sponsor/MAH, DE), `BIOX` (acquired biotech, US), `CMO-IE` (Emerald Fill Finish, contract manufacturer, IE) | Matches INJ-005 (acquisition integration) — confirms a real acquired entity and a real external CMO exist in scope, not a hypothetical |
| E-207 | `01_BUSINESS_CASE.md` §3, §6 (R-002, R-003, A-002) | Prior artefact, this team, 2026-08-07 | No absolute lead-time baseline supplied; no-AI option values (38%/27%/51%) not proven additive | Carried forward as the two open questions this workbook attempts to narrow |

## 1. Define

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What is the process under study? | The evidence-assembly sub-process that precedes EU Qualified Person batch certification for Workflow A's scope — i.e., the work of gathering genealogy, lab results, environmental monitoring, deviations, CAPA, change control, validation state and supplier evidence into a complete release packet (`case/INTEGRATED_CASE.md` §4, Workflow A). | Capstone team | `case/INTEGRATED_CASE.md` §4 |
| What is the defect definition? | A "defect" in this DMAIC sense is any release-packet item that is missing, contradictory, unsigned/untraceable to source, or ambiguous in validation/authority state at the point the QP would review it — i.e., exactly the four concrete instances in E-201–E-204, not a generic "slowness" claim. | Capstone team | E-201, E-202, E-203, E-204 |
| Is this in scope of Workflow A (reconcile/cite/flag/abstain only)? | Yes — every defect example below is something the workflow may *surface*, not resolve. None requires or implies a release/reject/reprocess/recall action, consistent with `data/ai_use_boundaries.csv` (`01_BUSINESS_CASE.md` E-004). | Capstone team | `01_BUSINESS_CASE.md` E-004 |

## 2. Measure

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Can Gap R-002 (no absolute baseline lead-time figure) be closed with current evidence? | No — `data/release_packets.csv`, `data/change_controls.csv` and `data/certificates_analysis.csv` are small, deliberately illustrative samples (2–3 rows each) with no timestamps for "time to detect" or "time to resolve." R-002 remains open; it requires either a synthetic timing model built and disclosed as such, or explicit acceptance that no absolute baseline exists and only relative/defect-count measures are usable. | Capstone team | Gap R-002 carried forward, not closed |
| What can be measured instead? | Defect *density and type* per batch, using the four confirmed defect categories: (1) missing packet item (E-201), (2) unapproved change bypass (E-202), (3) unsigned/transcribed certificate (E-203), (4) validation-state ambiguity (E-204). For batch `NCB204-B24071` alone, at least one instance of category (1) is confirmed. | Capstone team | E-201–E-204 |
| Is the measurement system itself trustworthy? | No, not yet — E-204 shows the very system category this intervention would belong to (`AI-EVIDENCE`) already has an unresolved, three-way conflicting validation status. Any "before/after" cycle-time measurement built on top of an ambiguously-validated system would itself be untrustworthy evidence. This must be resolved (see §6) before any Measure-phase claim is treated as reliable. | Capstone team | E-204 |

## 3. Analyse

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Root cause — missing evidence items (E-201) | Fragmented systems of record with no single evidence-authority model (`case/SOURCE_SYSTEM_FACT_PACK.md`: "No system is universally authoritative... authority [must be defined] by business object, jurisdiction, effective time, process state and accountable role"). A CMO-sourced audit commitment (E-201, E-206 confirms `CMO-IE` exists) is exactly the kind of externally-sourced evidence that falls through when no system owns cross-organisation evidence completeness. | Capstone team | E-201, E-206, `case/SOURCE_SYSTEM_FACT_PACK.md` |
| Root cause — unapproved change bypass (E-202) | Emergency-change process allows deployment before approval, with no confirmed enforced mechanism forcing retrospective closure (E-202: `retrospective_approval = missing`, no due date recorded). This is a **process/rules** gap, not a data-quality or AI gap. | Capstone team | E-202 |
| Root cause — unsigned/transcribed certificate (E-203) | Manual transcription step exists in the CoA pathway with no requirement to retain or link the original signed source at transcription time. This is a **data-integrity/process design** gap (ALCOA+), not something an AI summarization layer can fix after the fact — the original is already unlocatable. | Capstone team | E-203 |
| Root cause — validation-state ambiguity (E-204) | Three inventories (Quality, Architecture, Vendor) independently classify the same system without a reconciliation step or single system-of-record for validation status. This is a **master-data governance** gap. | Capstone team | E-204 |
| Root cause — CAPA effectiveness blind spot (E-205) | The CAPA effectiveness check is scoped to the original deviation's taxonomy code (`mixing_time`); a recurrence coded under a different taxonomy (`process_duration`) is invisible to that check even though `DEV-244` is explicitly flagged `similarity_to: DEV-201`. This is a **taxonomy/rules design** gap, not a volume-of-data problem. | Capstone team | E-205 |
| Does this resolve R-003 (are `master_data_repair` and `rules_workflow` additive)? | Partially informs it. Of the five root causes above, E-202 (change-control bypass) and E-205 (CAPA taxonomy blind spot) are **rules/workflow-design** gaps — enforcement and taxonomy logic, not master-data problems. E-203 (transcription) and E-204 (validation-state ambiguity) are **master-data/governance** gaps — no rule change fixes a already-unlocatable signed source or a three-way inventory conflict. E-201 (missing cross-org evidence item) sits at the boundary of both. This suggests `master_data_repair` and `rules_workflow` target *largely distinct* root-cause classes in this sample, which weakens (but does not prove) the case against pure non-additivity. **This remains an assumption, not a resolved fact** — the sample is 5 defect instances, not a statistically representative population. R-003 status is updated to "partially informed," not "closed." | Capstone team | E-201–E-205; `01_BUSINESS_CASE.md` R-003 |
| Where, if anywhere, is generative AI's marginal contribution once master data and rules are fixed? | On this evidence, the residual gap AI could close is cross-system, cross-organisation *evidence reconciliation* — connecting a CMO's audit commitment record (E-201/E-206) to a batch's release packet across organisational boundaries — which is neither a pure master-data fix (the CMO's record is legitimately external) nor a pure rule (there is no fixed schema mapping every external partner uses). This is consistent with, and narrows, Workflow A's stated scope. | Capstone team | E-201, E-206 |

## 4. Improve

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Recommended sequencing (unchanged from `01_BUSINESS_CASE.md` §3, now root-cause-justified) | 1) Rules/workflow fix: enforce mandatory retrospective-approval due dates for emergency changes (closes E-202-type gaps) and taxonomy-aware CAPA effectiveness checks that also check `similarity_to` links (closes E-205-type gaps) — matches `rules_workflow` (27%/6 weeks, `01_BUSINESS_CASE.md` E-003). 2) Master-data fix: single system-of-record reconciliation for validation state (closes E-204-type gaps) and mandatory signed-source retention at transcription (closes E-203-type gaps) — matches `master_data_repair` (38%/10 weeks). 3) Narrowly-scoped AI: cross-organisation evidence reconciliation and citation only (closes the residual E-201/E-206-type gap), matching Workflow A's exact allowed-action list. | Capstone team | E-201–E-206; `01_BUSINESS_CASE.md` E-003, E-004 |
| Does Improve require any prohibited action? | No — every proposed fix is either a process/rule change, a master-data governance change, or an AI reconcile/cite/flag/abstain action. None releases, reprocesses, reallocates or recalls anything. | Capstone team | `01_BUSINESS_CASE.md` E-004 |
| What must be fixed before AI evidence reconciliation can even be trusted (blocking dependency)? | The `AI-EVIDENCE` system category's own validation-state ambiguity (E-204) must be resolved first — deploying an AI evidence-reconciliation capability on top of a system whose own validation status is disputed across three inventories would compound, not reduce, the reconciliation problem. | Capstone team | E-204 |

## 5. Control

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What ongoing control prevents regression? | (a) Emergency-change retrospective approvals tracked with a due-date SLA and blocked from closure without it (addresses E-202 recurrence); (b) CAPA effectiveness checks required to query `similarity_to` links across taxonomy codes, not just same-code recurrence (addresses E-205 recurrence); (c) single validation-state system-of-record with the other two inventories treated as feeds, not independent authorities (addresses E-204 recurrence). | Capstone team | E-202, E-204, E-205 |
| Who owns each control? | Change-control SLA: Quality/Manufacturing change-control board (role-played). CAPA taxonomy logic: CQO's quality-system policy function (`case/STAKEHOLDER_PACK.md`, `03_STAKEHOLDER_DECISION_RIGHTS.md` E-101). Validation-state system-of-record: Architecture/Digital function, with CQO sign-off given GxP relevance. | Capstone team | `03_STAKEHOLDER_DECISION_RIGHTS.md` |
| How is control effectiveness itself measured (avoiding a repeat of the E-205 blind spot)? | Effectiveness checks must be defined *before* the control is deployed and must explicitly state what they do NOT catch (e.g., "this check catches same-taxonomy recurrence only") — directly countering the failure pattern in E-205 where an unstated scope limit let a real recurrence pass undetected. | Capstone team | E-205 |

## 6. Failure modes and verification

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Failure mode 1 | AI evidence-reconciliation tool is deployed while its own validation status remains disputed (E-204) → outputs could be treated as validated by one consumer and research-only by another, with no way to arbitrate. Verification: block deployment until `templates/13_GXP_LIFECYCLE_VALIDATION.md` and `templates/14_COMPUTER_SOFTWARE_ASSURANCE.md` resolve a single validation state. | Capstone team | E-204 |
| Failure mode 2 | A control's stated scope limit (§5) is not actually enforced in the tool logic, silently reproducing the E-205 pattern in a new taxonomy. Verification: require a specific test case per control that proves the "does NOT catch" boundary is real, not just documented. | Capstone team | E-205 |
| Failure mode 3 | Cross-organisation evidence reconciliation (the AI's residual scope, per §3) is asked to also judge whether a missing CMO commitment is *acceptable* to proceed — a release-adjacent judgement, not reconciliation. Verification: contract-schema test analogous to `evaluation/contract_samples/negative_batch_prohibited.json`, extended to cover "packet acceptability" as a prohibited AI conclusion, not only "release decision." | Capstone team | E-201; `evaluation/contracts/batch_response.schema.json` |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-201 | Gap | No absolute baseline lead-time figure exists in supplied data (carries forward `01_BUSINESS_CASE.md` R-002) | High | Capstone team | Phase 2 (Investigate), full evidence register | Open |
| R-202 | Assumption | `master_data_repair` and `rules_workflow` (E-003) are treated as targeting largely distinct root causes based on a 5-instance sample (E-201–E-205); not statistically validated | Medium — downgrades `01_BUSINESS_CASE.md` R-003 from "unresolved" to "partially informed," not closed | Capstone team | Full evidence register review, Phase 2 | Open (partially informed) |
| R-203 | Risk | The `AI-EVIDENCE` system category has a disputed validation state (E-204) that blocks trustworthy before/after measurement of any AI-attributable improvement | High — could invalidate the entire value-hypothesis measurement in `01_BUSINESS_CASE.md` §4 if not resolved first | Capstone team | Before any cycle-time evaluation is run | Open |
| R-204 | Gap | Control-effectiveness verification (§5/§6) is designed but not yet implemented as an executable test | Medium | Capstone team | Phase 4 (Build) / Phase 5 (Break and recover) | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Root causes are evidence-linked, not asserted | This workbook §3 | Team review | E-201–E-206 | Pending team review |
| AI's residual scope excludes packet-acceptability judgement (Failure mode 3) | `evaluation/contracts/batch_response.schema.json` | `tools/test_contracts.py` (existing negative fixture covers release/reject; acceptability judgement not yet covered) | `evaluation/contract_samples/negative_batch_prohibited.json` | Partial — existing test covers release decisions; acceptability-judgement case (R-204) not yet added |
| Validation-state blocker (R-203) is resolved before measurement | `templates/13_GXP_LIFECYCLE_VALIDATION.md`, `templates/14_COMPUTER_SOFTWARE_ASSURANCE.md` | Not yet built | — | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
