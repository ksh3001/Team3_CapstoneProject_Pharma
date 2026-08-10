# Computer Software Assurance

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `13_GXP_LIFECYCLE_VALIDATION.md`; `10_C4_ARCHITECTURE.md` §5; `12_INTEGRATION_CONTRACTS.md` §6/§7; `sources/LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md` |

## Purpose

Applies a risk-based, critical-thinking test strategy — assurance effort commensurate with risk, per the research anchor in `sources/LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md` ("Risk-based assurance does not remove accountability for intended use, requirements, testing, data integrity or controlled operation") — to the specific failures already found in artefacts 10–13, rather than proposing a generic test plan. Accountable owner: capstone team. Completion criteria: every high-risk function named here traces to an already-observed failure or near-failure, not a hypothetical category.

## Evidence register

This artefact indexes evidence already registered in `10_C4_ARCHITECTURE.md`, `12_INTEGRATION_CONTRACTS.md` and `13_GXP_LIFECYCLE_VALIDATION.md`; see each item's "Acceptance evidence" column for the specific ID.

## 1. Critical thinking and risk basis

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What determines "high risk" here, concretely, rather than by category label? | A function is treated as high-risk if a real failure or near-failure has already been recorded against it in this evidence set (not merely because it "sounds GxP-critical"). By this test: model artifact integrity (`10_C4_ARCHITECTURE.md` E-1005, currently failing), citation supersession detection (`13_GXP_LIFECYCLE_VALIDATION.md` E-1301 `VT-1`, currently failing), role-revocation/stale-authorization handling (E-1301 `VT-2` and `12_INTEGRATION_CONTRACTS.md` E-1203/E-1204, currently failing), and cross-affiliate/token-cap security gates (`12_INTEGRATION_CONTRACTS.md` E-1205, both currently unblocked) are all high-risk by evidence, not by assumption. | Capstone team | E-1005, E-1301, E-1203, E-1204, E-1205 |
| Has this team identified any confirmed low-risk function eligible for unscripted-only testing? | Not yet, honestly — every function examined so far in artefacts 10–13 has turned out to be high-risk-adjacent once traced to real evidence. This is disclosed as a current gap in the assurance strategy (no low-risk category populated yet) rather than inventing filler low-risk items to satisfy the template's structure. | Capstone team | Gap R-1401 |

## 2. High-risk functions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| HR-1: Model artifact integrity check | Currently failing in evidence — `GXP-SUM-1` deployed hash ≠ registry hash, signature missing (`10_C4_ARCHITECTURE.md` E-1005). | Capstone team | E-1005 |
| HR-2: Citation supersession detection | Currently failing — `VT-1` result `fail_on_superseded_doc` (`13_GXP_LIFECYCLE_VALIDATION.md` E-1301). | Capstone team | E-1301 |
| HR-3: Role revocation / live authorization check | Currently failing — `VT-2` result `fail_cached_access` (E-1301), independently corroborated by `contractor_77`'s 2-day stale-access window (`12_INTEGRATION_CONTRACTS.md` E-1203/E-1204). | Capstone team | E-1301, E-1203, E-1204 |
| HR-4: Cross-affiliate purpose-limitation gate | Currently absent — `SEC-1` (cross-affiliate narrative query) recorded as not blocked (`12_INTEGRATION_CONTRACTS.md` E-1205). | Capstone team | E-1205 |
| HR-5: Token/size denial-of-wallet cap | Currently absent — `SEC-2` (980K-token oversized-document loop) recorded as not blocked (E-1205). | Capstone team | E-1205 |
| HR-6: Checkpoint-age / idempotent resume | Currently failing — `AR-77` resumed a 380-minute-old checkpoint and created duplicate draft reservations (`12_INTEGRATION_CONTRACTS.md` E-1202). | Capstone team | E-1202 |
| HR-7: Prohibited-action schema rejection | Currently **passing** — the one high-risk function with confirmed positive evidence (`tools/test_contracts.py`, 6/6). Included here to show the register is not selectively negative. | Capstone team | `tools/test_contracts.py` |

## 3. Assurance methods

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Which method applies to HR-1–HR-6 (all currently failing/absent)? | Scripted, evidence-based testing with a specific pass/fail assertion tied to the exact evidence row that exposed the failure (e.g., a test asserting `deployed_hash == registry_hash` for HR-1, reproducing E-1005's exact condition) — not exploratory/unscripted testing, which is reserved for genuinely low-risk functions this team has not yet identified (§1). | Capstone team | E-1005, E-1301, E-1202, E-1205 |
| Which method applies to HR-7 (already passing)? | Scripted regression testing to ensure it remains passing as new requirements are added — already implemented via `tools/test_contracts.py`, re-run and confirmed passing multiple times this session. | Capstone team | `tools/test_contracts.py` |

## 4. Unscripted and scripted evidence

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Is any unscripted (exploratory) testing evidence available today? | No — all evidence in this pull (`validation_tests.csv`, `security_events.csv`, `agent_runs.csv`) is itself the output of what appears to be scripted or logged monitoring, not exploratory testing notes. This team has not yet performed its own exploratory testing pass. | Capstone team | Gap R-1402 |
| What should exploratory testing target first, if performed? | The same six high-risk functions (§2), specifically probing variations the existing scripted evidence does not cover — e.g., HR-4's gate should be exploratory-tested against *within-affiliate* queries that are unusually broad, not just the exact `cross_affiliate_narrative_query` pattern already logged. | Capstone team | E-1205 |

## 5. Defect handling

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Are HR-1 through HR-6 tracked as defects with owners? | Partially — each has a risk/gap entry in its source artefact (`10_C4_ARCHITECTURE.md` R-1001; `13_GXP_LIFECYCLE_VALIDATION.md` R-1302; `12_INTEGRATION_CONTRACTS.md` R-1203/R-1204/R-1205), but none yet has a confirmed accountable remediation owner by name/role — only "capstone team" pending role assignment. | Capstone team | Cross-referenced R-IDs above |
| What defect-severity ranking follows from §1's evidence-based method? | Critical: HR-4, HR-5 (live, unblocked security exposure). High: HR-1, HR-2, HR-3 (block any "validated"/"production-ready" claim for the AI-EVIDENCE capability). Medium: HR-6 (draft-only impact, but corrupts audit trail per `12_INTEGRATION_CONTRACTS.md` §6). | Capstone team | E-1005, E-1205, E-1301, E-1202 |

## 6. Release decision evidence

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Can any AI-assisted capability in this capstone currently be recommended for even a supervised pilot? | No, on the current evidence — HR-1 through HR-6 collectively mean the summarisation model is unverified, citation freshness cannot be trusted, revoked users may still be served, two real attack patterns are unblocked, and checkpoint resume duplicates state. A release/pilot recommendation before remediating at least HR-1, HR-2, HR-4 and HR-5 would contradict this artefact's own evidence. | Capstone team | HR-1–HR-6 |
| Does this block the capstone's own submission? | No — these are pre-existing platform conditions this team is required to surface and design around, per `case/INTEGRATED_CASE.md`'s embedded-inject rule (§6: "no later instructor injects... discover connections... from the supplied evidence"). The capstone's deliverable is the design and test evidence that would need to pass before real deployment, not a claim that deployment is currently safe. | Capstone team | `case/INTEGRATED_CASE.md` §6 |

## 7. Continuous assurance

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| How should HR-1–HR-7 be monitored after initial remediation? | Each should become a standing regression check re-run on every model/config/tool-catalog change (consistent with `knowledge/AI_MODEL_CHANGE_CONTROL.md`, not detailed here) — HR-1's hash check in particular must re-run on every model deployment event, not just at initial validation. | Capstone team | Cross-reference only |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1401 | Gap | No confirmed low-risk function has been identified yet, so the risk-based effort split (scripted-heavy vs. unscripted-light) is currently all-scripted by necessity, not by design choice | Low-Medium — may indicate incomplete exploration, not an actual absence of any low-risk function | Capstone team | Phase 4/5 (Build / Break and recover) | Open |
| R-1402 | Gap | No exploratory/unscripted testing has been performed by this team yet | Medium | Capstone team | Phase 5 (Break and recover) | Open |
| R-1403 | Risk | HR-1 through HR-6 have no named accountable remediation owner by role, only "capstone team" | Medium | Capstone team | Phase 3 (Specify) | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| HR-7 (prohibited-action rejection) passes and stays regression-tested | `evaluation/contracts/*.schema.json` | `tools/test_contracts.py` | `evaluation/contract_samples/*` | PASS (6/6) |
| HR-1–HR-6 each have a scripted test reproducing their known-failing condition | New tests, not yet written | Not yet implemented | E-1005, E-1301, E-1202, E-1205 | Pending — all currently FAIL if evidence is representative |
| Release/pilot recommendation withheld until HR-1, HR-2, HR-4, HR-5 pass | This artefact §6 | Team governance decision | This document | Self-verified — recommendation explicitly withheld above |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
