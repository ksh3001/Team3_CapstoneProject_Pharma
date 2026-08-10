# Stakeholder and Decision Rights

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending team entry; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | INJ-002, INJ-006, INJ-016, INJ-071, INJ-074; `01_BUSINESS_CASE.md` §1, §5 |

## Purpose

This artefact establishes who is accountable for each regulated decision touched by Workflows A/B/C, where incentives conflict, and how AI output can be overridden or escalated — required before any workflow, prompt or agent design begins (`runbooks/PARTICIPANT_RUNBOOK.md` Phase 1). Accountable owner: capstone team, informed by role-played sponsors. Completion criteria: every AI-touched decision maps to exactly one accountable human role with a stated review/override path, per `case/REGULATORY_BOUNDARY_PACK.md` boundary question 4 ("Which human role remains accountable and what evidence must that role inspect?").

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-101 | `case/STAKEHOLDER_PACK.md` (full 15-row table) | Narrative stakeholder register, undated | Full mandate/incentive/concern/decision-authority for 15 named roles (CMO, CQO, EU QP, Global Head of PV, Head of Clinical Ops, Regulatory Affairs VP, Manufacturing VP, Supply Chain VP, DPO, CISO, Head of Biostatistics, Patient Safety Representative, Site Investigator Council, Works Council, Procurement) | This is the authoritative narrative source; the structured `stakeholders.csv` (E-102) is a partial 3-row extract, not a superset — both are cited and neither is discarded |
| E-102 | `data/stakeholders.csv` | Structured register, undated | ST-01 EU Qualified Person (EU, priority: evidence completeness); ST-02 Manufacturing VP (Global, priority: supply continuity); ST-03 Global Safety Head (Global, priority: reporting timeliness) | Only 3 of the 15 roles in E-101 appear here — treated as a machine-readable sample, not the complete stakeholder set |
| E-103 | `data/decision_rights.csv` | Decision-rights register, undated | batch certification → EU Qualified Person, ai_authority = none; ICSR reportability → Safety Physician, ai_authority = none; stock allocation → Supply Governance Board, ai_authority = draft only | "Safety Physician" (E-103) and "Global Head of Pharmacovigilance" / "Global Safety Head" (E-101/E-102) are not confirmed to be the same role — flagged as Gap R-101, not silently merged |
| E-104 | `data/ai_use_boundaries.csv` | Executive prohibition (INJ-006), undated | Allowed vs. prohibited AI actions per workflow (batch evidence, PV intake, supply planning) | Matches `01_BUSINESS_CASE.md` E-004 exactly; cited again here for the RACI matrix |
| E-105 | `case/INTEGRATED_CASE.md` line 50 (INJ-002) | Case narrative | Manufacturing rewards throughput, Quality rewards deviation containment, Supply rewards service level, Clinical rewards database-lock speed | Confirms structural incentive conflict independent of any AI intervention |
| E-106 | `case/INTEGRATED_CASE.md` line 133 (INJ-074) | Case narrative | "A global process owner wants uniform automation while local Qualified Persons and safety officers retain legal accountability." Evidence distributed across `stakeholders.csv; decision_rights.csv` | Direct statement of the global-standardization vs. local-accountability conflict this artefact must resolve |
| E-107 | `case/INTEGRATED_CASE.md` line 128 (INJ-071) | Case narrative | "Reviewers accept an AI summary despite an omitted critical deviation." Evidence: `candidate_outputs.csv; reviewer_feedback.csv` | Automation-bias risk directly informs §4 (independent review) design, not just a UX note |
| E-108 | `case/REGULATORY_BOUNDARY_PACK.md` boundary questions 1–6 | Research anchor, not legal conclusion | Six boundary questions the team must answer per AI-touched component (regulated-record status, influence on quality/safety, advisory vs. determinative, accountable role, proportionate validation, absolute prohibitions) | Explicitly "research anchors, not legal conclusions" — applicability is the team's determination, not asserted here |

## 1. Stakeholder map

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Who are the accountable decision-makers the three workflows must not bypass? | EU Qualified Person (batch certification, "final certification remains human-only" per E-101); Global Head of Pharmacovigilance / Safety Physician (final safety decisions "remain human-only" per E-101/E-103); Supply Governance Board / Supply Chain VP ("Planning; regulated execution needs approvals" per E-101, ai_authority "draft only" per E-103). | EU QP / Safety Physician / Supply Governance Board (role-played) | E-101, E-102, E-103 |
| Who are the advisory/veto stakeholders with no execution authority but standing to block? | Patient Safety Representative — "Advisory veto through safety governance" (E-101). Data Protection Officer — "Privacy risk acceptance and escalation" (E-101). Works Council / Employee Forum — "Consultation rights in applicable regions" (E-101), relevant to any AI telemetry used on reviewers. | Capstone team to route these into escalation design (§5) | E-101 |
| Who owns segregation-of-duties tension between global standardization and local accountability (INJ-074)? | Unresolved by design — E-101 and E-106 confirm the conflict exists but do not resolve it. This artefact's position (§4): the AI layer must be configurable per local Qualified Person / safety officer without requiring a global process-owner override, so uniform automation cannot silently supersede local legal accountability. | Capstone team | E-106 |
| Which stakeholders are structurally incentivized against full evidence completeness? | Manufacturing VP (throughput-rewarded, E-105) and Supply Chain VP (service-level-rewarded, E-105) both have an incentive to accept faster-but-thinner evidence packets; the EU QP's stated concern is explicitly "Missing CMO and audit commitments" (E-101). This is a designed check, not a flaw to engineer away. | Capstone team | E-101, E-105 |

## 2. RACI/RAPID decision matrix

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Batch certification (Workflow A) | Recommend/Reconcile: AI (reconcile, cite, flag, abstain — E-104). Accountable: EU Qualified Person (ai_authority = none, E-103). Consulted: CQO ("Quality-system policy and risk acceptance", E-101), Manufacturing VP (operations input, "never independent batch release", E-101). Informed: Site Investigator Council where source data is implicated. | EU Qualified Person | E-103, E-104, E-101 |
| ICSR reportability (Workflow B) | Recommend: AI (extract, normalize, cluster, cite — E-104). Accountable: Safety Physician / Global Head of Pharmacovigilance (ai_authority = none, E-103). Consulted: CMO ("Clinical governance and escalation", E-101). Informed: Patient Safety Representative (advisory veto path, E-101). | Safety Physician (role identity to be confirmed — see Gap R-101) | E-103, E-104, E-101 |
| Stock allocation (Workflow C) | Recommend: AI (generate options only — E-104). Accountable: Supply Governance Board (ai_authority = draft only, E-103). Consulted: Supply Chain VP, Manufacturing VP (E-101). Informed: Procurement (contracting implications, E-101). | Supply Governance Board | E-103, E-104, E-101 |
| Does any workflow grant the AI "Approve" or "Decide" in this matrix? | No, by design — E-103 caps every row at "none" or "draft only", and E-104 confirms all three prohibited-action lists exclude the regulated decision itself. This is verified structurally (not just documented) by the passing negative contract tests in `evaluation/contract_samples/negative_*_prohibited.json`. | Capstone team | E-103, E-104, `tools/test_contracts.py` (PASS, 6/6) |

## 3. Incentive conflicts

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What are the confirmed structural conflicts? | (a) Manufacturing throughput vs. Quality deviation-containment vs. Supply service-level vs. Clinical database-lock speed (E-105); (b) EU QP wants evidence completeness, Manufacturing VP wants supply continuity, Global Safety Head wants reporting timeliness (E-102) — three different "success" definitions for the same underlying evidence base; (c) Global process owner wants uniform automation, local QP/safety officers retain legal accountability (E-106); (d) Procurement favours a bundled AI vendor, Architecture/CISO seek substitutability (E-101 "Deliberate conflicts"); (e) Clinical Operations seeks automation, Biostatistics/investigators require prespecified, explainable transformations (E-101). | Capstone team — document, do not silently resolve | E-105, E-106, E-101, E-102 |
| How does this artefact prevent the AI from being tuned to favour one incentive over another? | The workflows' allowed-action lists (E-104) are identical regardless of which function requests the output — the AI cannot be configured to "optimize for Manufacturing's throughput KPI" because it has no allocation, release, or scheduling authority in the first place (E-103/E-104). Any request to change this is itself a decision-rights violation requiring escalation (§5), not a configuration change. | Capstone team | E-103, E-104 |
| Residual conflict not resolvable by design alone | (b) above — three legitimate but different definitions of "good evidence" (complete vs. continuous-supply-preserving vs. fast-to-report) cannot be fully reconciled by withholding AI authority; it requires an explicit escalation path when the AI's abstain/flag output is contested. See §5. | Capstone team | E-102 |

## 4. Independent review and segregation of duties

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What review failure mode is already evidenced (INJ-071)? | "Reviewers accept an AI summary despite an omitted critical deviation" (E-107) — automation bias, not a hypothetical risk. | Capstone team | E-107 |
| What segregation-of-duties control follows from this? | The AI output must never present a single confidence-weighted summary that can substitute for reading the underlying evidence; per `case/REGULATORY_BOUNDARY_PACK.md` boundary question 4, the accountable role (EU QP / Safety Physician / Supply Governance Board) must be able to inspect the same evidence items the AI cited, not only its conclusion. This requires structured, evidence-item-linked output (see `evaluation/contracts/evidence_item.schema.json`), not free-text summarization. | Capstone team | E-108, `evaluation/contracts/evidence_item.schema.json` |
| Who independently reviews the AI's abstention/flag decisions themselves (not just its positive outputs)? | Not yet assigned — an omitted-deviation failure (E-107) could equally occur if the AI wrongly abstains on a real gap and no one checks abstentions. Recommend: same accountable role reviews a sample of abstentions, not only affirmative outputs, as part of the eventual TEVV plan (`evaluation/EVALUATION_PLAN.md` suite 6). | Capstone team | Gap R-102 (below) |
| Does any single role both configure the AI and rely on its output unreviewed? | Must not — Architecture/CISO (tool/prompt/model configuration) are distinct from the EU QP/Safety Physician/Supply Governance Board (output consumers), per the differing "Decision authority" column values in E-101. This separation is a design constraint carried into `templates/16_THREAT_ABUSE_MODEL.md` and `templates/20_ISO42001_GOVERNANCE.md`, not repeated in full here. | Capstone team | E-101 |

## 5. Escalation and override

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What escalation path exists when AI output is contested between functions? | Not yet defined in supplied evidence — E-101/E-102 establish who holds decision authority per domain but no cross-functional escalation sequence is given. Provisional design: contested evidence-completeness disputes (e.g., Manufacturing vs. Quality) escalate to the CQO ("Quality-system policy and risk acceptance", E-101) as the named policy owner; contested reportability timing escalates to CMO ("Clinical governance and escalation", E-101). | Capstone team to formalize | Gap R-103 (below) |
| Where does the Patient Safety Representative's "advisory veto" actually attach? | Unresolved by current evidence — E-101 states the mechanism ("Advisory veto through safety governance") but not the trigger condition or workflow touchpoint. Recommend attaching it to Workflow B's signal-support output before any downstream regulatory action, pending Phase 2/3 confirmation. | Capstone team | Gap R-104 (below) |
| What is the emergency-stop / override path if the AI is wrong or compromised? | Not covered by this artefact — deferred to `templates/18_RESPONSIBLE_AI_HUMAN_FACTORS.md` (human oversight, override, contestability, emergency-stop design) and `knowledge/AGENT_BUDGET_AND_STOP_POLICY.md`, both out of this document's scope but cross-referenced here so the two are not designed inconsistently. | Capstone team | Cross-reference only — not duplicated here |
| Works Council consultation trigger | Where AI telemetry captures reviewer behaviour (e.g., who accepted/overrode which output, relevant to INJ-071 remediation), Works Council / Employee Forum consultation rights apply "in applicable regions" (E-101) — this must be checked per jurisdiction before any reviewer-performance telemetry is enabled, not assumed globally permissible. | Capstone team / DPO (role-played) | E-101 |

## 6. Training and adoption

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Which roles need training before go-live? | All roles in the RACI matrix (§2) that consume AI output directly: EU QP, Safety Physician, Supply Governance Board, plus consulted roles (CQO, CMO, Manufacturing VP, Supply Chain VP) — training must specifically cover the automation-bias failure mode already evidenced (E-107), not only tool mechanics. | Capstone team | E-107 |
| What does "adoption" explicitly exclude? | Training must not present the AI's abstain/flag/cite output as a recommendation to trust by default — the explicit purpose of automation-bias training is to counteract that tendency, consistent with `templates/18_RESPONSIBLE_AI_HUMAN_FACTORS.md` scope (deferred, cross-referenced only). | Capstone team | E-107 |
| Are there known accessibility/language constraints affecting adoption? | Out of this artefact's evidence set — INJ-072 (language inequity) and INJ-073 (accessibility failure) are catalogued in `case/INTEGRATED_CASE.md` but their source data (`model_performance.csv`, `usability_findings.csv`) is not reviewed here; cross-referenced to `templates/18_RESPONSIBLE_AI_HUMAN_FACTORS.md` to avoid asserting unreviewed conclusions. | Capstone team | Cross-reference only |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-101 | Gap | "Safety Physician" (E-103) not confirmed identical to "Global Head of Pharmacovigilance" (E-101) / "Global Safety Head" (E-102) | Medium — RACI accountable-role naming could be inconsistent across artefacts | Capstone team | Phase 2 (Investigate) | Open |
| R-102 | Gap | No reviewer is assigned to independently sample-check AI abstention decisions, only affirmative outputs | Medium — mirrors the INJ-071 failure mode but for the negative case | Capstone team | Before evaluation plan finalization | Open |
| R-103 | Gap | No supplied cross-functional escalation sequence for contested AI output | High — without this, §2's RACI matrix has no dispute-resolution path | Capstone team | Phase 3 (Specify) | Open |
| R-104 | Gap | Patient Safety Representative's advisory-veto trigger condition is not specified in source evidence | Medium — veto right is named but not operationalized | Capstone team | Phase 3 (Specify) | Open |
| R-105 | Assumption | `data/stakeholders.csv` (3 rows) is treated as a non-exhaustive sample of `case/STAKEHOLDER_PACK.md` (15 rows), not a contradiction | Low | Capstone team | N/A — documented, not blocking | Closed (documented) |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| No workflow grants AI "Approve"/"Decide" authority | Structured-output contracts (batch/pv/supply schemas) | `tools/test_contracts.py` | `evaluation/contract_samples/negative_*_prohibited.json` | PASS (6/6, already verified) |
| Accountable role can inspect same evidence AI cites (§4) | `evaluation/contracts/evidence_item.schema.json` | Pending — no runner yet exercises this against public fixtures | `evaluation/public_fixtures/*.json` | Pending |
| Escalation path for contested output (§5) | Not yet architected | Pending | `templates/03_STAKEHOLDER_DECISION_RIGHTS.md` §5 (this document) | Pending — logged as R-103 |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
