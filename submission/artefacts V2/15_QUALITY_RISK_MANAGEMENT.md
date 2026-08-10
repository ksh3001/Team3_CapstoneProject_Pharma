# Quality Risk Management

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | ICH Q9(R1) research anchor (`case/REGULATORY_BOUNDARY_PACK.md`); synthesizes `02`, `06`, `08`, `10`, `12`, `13`, `14` |

## Purpose

Traces **multi-inject failure chains** — combinations of independently-true facts already evidenced across prior artefacts that compound into a hazard neither fact alone would reveal — directly answering `case/INTEGRATED_CASE.md` §6's expectation that participants "discover connections, contradictions and failure chains from the supplied evidence rather than receive staged surprises." Accountable owner: capstone team. Completion criteria: every failure chain below links at least two independently-sourced evidence items, not a single restated finding.

## Evidence register

This artefact combines evidence already registered in `02_DMAIC_WORKBOOK.md`, `04_PRODUCT_SERVICE_BLUEPRINT.md`, `06_DATA_GOVERNANCE_INTEGRITY.md`, `08_KNOWLEDGE_GRAPH_DECISION.md`, `10_C4_ARCHITECTURE.md`, `12_INTEGRATION_CONTRACTS.md` and `13_GXP_LIFECYCLE_VALIDATION.md`. Each chain below cites its component evidence IDs.

## 1. Risk question and scope

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Risk question | Where do two or more independently-recorded, individually-manageable facts combine into a hazard that no single-artefact review would surface? | Capstone team | N/A — framing |
| Scope | Five failure chains, each spanning at least two source artefacts, covering batch release, AI-platform trust, data-integrity accountability, recall scope and privacy/legal-hold conflict. | Capstone team | §3 below |

## 2. Hazard analysis

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What method is used? | Qualitative severity/likelihood framing per ICH Q9(R1) research anchor, without fabricating false numeric precision the underlying evidence does not support (no invented probability percentages) — consistent with `case/REGULATORY_BOUNDARY_PACK.md`'s caution that these are research anchors, not legal conclusions. | Capstone team | `case/REGULATORY_BOUNDARY_PACK.md` |

## 3. Failure chains

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| **Chain A — Pressure-induced acceptance of incomplete batch evidence** | (1) Board mandates -14% lead time (`01_BUSINESS_CASE.md` E-001). (2) Batch `NCB204-B24071` already has a missing CMO audit commitment (`02_DMAIC_WORKBOOK.md` E-201) **and** an open major deviation (`13_GXP_LIFECYCLE_VALIDATION.md` E-1302, `QE-100`). (3) A recorded automation-bias failure already shows a reviewer accepting an AI summary that omitted a critical fact in 19 seconds (`04_PRODUCT_SERVICE_BLUEPRINT.md` E-301). **Compound hazard**: lead-time pressure (1) plus an already-demonstrated tendency to accept incomplete-looking-complete output (3) applied to a batch that is *actually* incomplete in two ways (2) creates a realistic path to a QP certifying on the basis of an AI summary that under-represents real, open quality events — even though the AI itself never decides. Severity: High (patient/product-quality relevant). Likelihood: elevated by (1) and (3) both being independently confirmed, not hypothetical. | Capstone team | E-001, E-201, `QE-100`, E-301 |
| **Chain B — Compromised summarisation trusted more during a crisis, not less** | (1) AI primary region is down; fallback is a smaller on-prem model (`10_C4_ARCHITECTURE.md` E-1002). (2) The intended summarisation model `GXP-SUM-1` fails artifact-integrity verification (E-1005). (3) The same system category fails its own citation-supersession validation test (`13_GXP_LIFECYCLE_VALIDATION.md` E-1301, `VT-1`). (4) All four AI-platform capabilities are single-vendor (`10_C4_ARCHITECTURE.md` E-1007). **Compound hazard**: during exactly the kind of platform incident already underway (ransomware containment, `04_PRODUCT_SERVICE_BLUEPRINT.md` E-304), reviewers under operational pressure may lean on AI output *more*, not less — at the precise moment (1)–(4) mean that output is least verifiable. Severity: Critical. Likelihood: the triggering conditions (region outage, vendor concentration) are already present in the evidence, not speculative. | Capstone team | E-1002, E-1005, E-1301, E-1007, E-304 |
| **Chain C — Unattributable privileged action during degraded audit visibility** | (1) Audit capture was disabled for 47 minutes overlapping a 28-minute unauthorized session overrun (`06_DATA_GOVERNANCE_INTEGRITY.md` E-501/E-502). (2) An independent open audit finding confirms "shared accounts" as a live issue (`13_GXP_LIFECYCLE_VALIDATION.md` E-1303, `AF-1`). (3) Entitlement revocation lag means a revoked user's access can remain honored for days (`12_INTEGRATION_CONTRACTS.md` E-1203/E-1204). **Compound hazard**: if a shared or improperly-still-active account were used during an audit-capture gap, there would be no reliable way to attribute the resulting master-data change to a specific accountable individual — a direct ALCOA+ "Attributable" failure at the intersection of three separately-documented weaknesses. Severity: High. Likelihood: each precondition is independently confirmed already; only their simultaneous occurrence is not directly evidenced (Gap R-1501). | Capstone team | E-501, E-502, `AF-1`, E-1203, E-1204 |
| **Chain D — Incomplete recall-scope traversal silently under-reports exposure** | (1) `NCS310-S26033` and `NCS310-S26031` share a component and equipment; the latter was already distributed to AE hospitals (`08_KNOWLEDGE_GRAPH_DECISION.md` E-703). (2) `NCS310-S26033` now has an open critical-potential complaint (`13_GXP_LIFECYCLE_VALIDATION.md` E-1302, `QE-101`). (3) INJ-058 explicitly states "not all genealogy links are complete" for recall candidates. **Compound hazard**: if the AI's connected-components traversal (designed in `08_KNOWLEDGE_GRAPH_DECISION.md` §2) silently drops a lot because its genealogy link is missing/broken, rather than surfacing it as "connection unknown, requires investigation," a human recall-scope reviewer could be shown an artificially narrow — and falsely confident-looking — set of affected lots, at the exact moment (2) means real patient exposure may already exist. Severity: Critical (patient-safety-adjacent, though the AI itself must never decide the recall). Likelihood: the missing-link condition is explicitly disclosed as a known estate characteristic, not rare. | Capstone team | E-703, `QE-101`, INJ-058 |
| **Chain E — Premature deletion destroying legally-held evidence** | (1) `DSR-17` (deletion request, subject `S-301-044`) and `LH-44` (active legal hold on `NCB204-301`) may name overlapping data, unconfirmed (`06_DATA_GOVERNANCE_INTEGRITY.md` E-505–E-507, R-501). (2) AI prompt logs are retained only 90 days "unless evidence hold" (E-505) — implying the hold-check mechanism must actually run correctly to prevent deletion. (3) The reconciliation AI would generate prompt/evidence logs referencing this subject's data if used in this trial context. **Compound hazard**: if the identity link in (1) is real but the automated hold-check in (2) has the same kind of "checks a cache instead of live state" defect already found elsewhere (`13_GXP_LIFECYCLE_VALIDATION.md` `VT-2`, `12_INTEGRATION_CONTRACTS.md` E-1204), AI-generated evidence relevant to an active legal hold could be deleted on schedule before the hold is honored. Severity: High (legal/regulatory, not patient-safety). Likelihood: depends on the unconfirmed link in (1) — explicitly flagged as conditional, not asserted. | Capstone team | E-505, E-506, E-507, R-501, `VT-2`, E-1204 |

## 4. Risk controls

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Control for Chain A | Structured, evidence-item-linked output (already an ADR, `11_ADR_REGISTER.md` ADR-008) plus a hard rule: any batch with an open major/critical quality event must display that event prominently in the AI's evidence packet, never omit it regardless of summarisation logic. | Capstone team | `11_ADR_REGISTER.md` ADR-008; `13_GXP_LIFECYCLE_VALIDATION.md` E-1302 |
| Control for Chain B | Model Gateway Artifact Integrity + Validated-Scope Router components (`10_C4_ARCHITECTURE.md` §3), enforced especially during degraded-mode operation, not relaxed under time pressure — degraded mode must fail toward *more* scrutiny, not less. | Capstone team | `10_C4_ARCHITECTURE.md` §3 |
| Control for Chain C | Live IAM check at execution time (`12_INTEGRATION_CONTRACTS.md` §5, shared fix with `VT-2`) plus a rule that any privileged session overlapping an audit-capture gap is automatically flagged for independent review, not just logged. | Capstone team | `12_INTEGRATION_CONTRACTS.md` §5 |
| Control for Chain D | Recall-scope traversal must explicitly represent "link unknown/incomplete" as a distinct state from "not connected" — never collapse the two — per `08_KNOWLEDGE_GRAPH_DECISION.md` §4's provenance requirement extended to missing-edge cases. | Capstone team | `08_KNOWLEDGE_GRAPH_DECISION.md` §4 |
| Control for Chain E | Hold-check must query live legal-hold state at deletion-execution time, not a cached/scheduled check — same architectural pattern as `VT-2`'s fix, applied to retention/deletion logic specifically. | Capstone team | `06_DATA_GOVERNANCE_INTEGRITY.md` §6 |

## 5. Residual risk and uncertainty

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Which chains have the highest unresolved uncertainty? | Chain C (simultaneous occurrence of its three preconditions is not directly evidenced, only each precondition individually) and Chain E (depends entirely on the unconfirmed `S-301-044`↔`NCB204-301` link, R-501). Both are presented as plausible compound hazards worth controlling for, not as proven incidents. | Capstone team | Gap R-1501 |
| Which chains are most directly evidenced as already-occurring conditions, not just plausible combinations? | Chain B and Chain D — every precondition in both is independently confirmed as a current, recorded fact (not a hypothesis), so the compound hazard is a logical consequence of already-true conditions, not a speculative scenario. | Capstone team | E-1002, E-1005, E-1301, E-703, `QE-101` |

## 6. Risk acceptance

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Can any of these five chains be accepted as residual risk without control, given capstone scope? | No — per `14_COMPUTER_SOFTWARE_ASSURANCE.md` §6, this team has already withheld a pilot-readiness recommendation on narrower grounds; these compound chains reinforce, not relax, that position. Risk acceptance (if any) is a decision for the accountable human roles named in `03_STAKEHOLDER_DECISION_RIGHTS.md` §2 (EU QP, Safety Physician, Supply Governance Board), not this team. | Named accountable roles (role-played) | `14_COMPUTER_SOFTWARE_ASSURANCE.md` §6; `03_STAKEHOLDER_DECISION_RIGHTS.md` §2 |

## 7. Review triggers

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What should trigger re-review of this risk register? | (a) `GXP-SUM-1` is re-deployed with a matching hash (Chain B partially closes); (b) the `S-301-044` identity link is confirmed or refuted (Chain E resolves either way); (c) `VT-1`/`VT-2` are re-tested and pass (Chains B, C, E all partially close). | Capstone team | `11_ADR_REGISTER.md` §7 revisit triggers (same events) |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1501 | Assumption | Chains C and E combine independently-true preconditions into a plausible compound hazard; simultaneous occurrence is not directly evidenced as having happened, only as being possible given confirmed individual facts | Medium — these are risk-management hypotheses to control for, not confirmed incidents; must not be presented as proven in the final defence | Capstone team | Ongoing | Open |
| R-1502 | Gap | No quantitative likelihood estimate is provided for any chain — only qualitative severity/likelihood framing, per the decision in §2 not to fabricate false numeric precision | Low — this is a deliberate methodological choice, not an oversight, but should be stated explicitly to any reviewer expecting numeric risk scores | Capstone team | N/A — documented choice | Closed (documented) |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Every failure chain cites at least two independent evidence sources | This document §3 | Manual review | Cited evidence IDs per chain | Self-verified — all 5 chains cite 2+ sources |
| Chain D's "link unknown ≠ not connected" control is implemented and tested | Graph traversal design (`08_KNOWLEDGE_GRAPH_DECISION.md`) | Not yet implemented | — | Pending |
| Chain B's degraded-mode-tightens-not-relaxes rule is implemented and tested | Model Gateway components (`10_C4_ARCHITECTURE.md` §3) | Not yet implemented | — | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
