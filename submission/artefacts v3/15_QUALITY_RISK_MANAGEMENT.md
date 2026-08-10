# Quality Risk Management

> Phase 3. ICH Q9-style thinking for the advisory assist: hazards, failure chains, controls, residual risk.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / GxP–quality lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Architecture; Security; Product |
| Status | Draft |
| Related requirements / ADRs | Artefacts 13–14; INV-01…08; DEC-011 stop criteria |

## Purpose

Answer: **What could go wrong if the assist misleads or overreaches, and are controls sufficient for a go / conditional-go?**

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | inject register / anchor conflicts | Unit, duplicate, cold-chain, DI themes |
| E-002 | ai_use_boundaries / decision_rights | Authority hazards |
| E-003 | knowledge_trust_catalogue | Untrusted instruction hazard |
| E-004 | baseline_diagnostics clues | Starter failure modes |
| E-005 | artefacts 10–14 | Controls already designed |

## 1. Risk question and scope

| Item | Entry |
|---|---|
| Risk question | Does the proposed assist unacceptably increase risk of wrong batch release narrative, wrong PV clock/reportability path, or unsafe supply action — relative to status quo reconciliation? |
| In scope | Three workflows; offline POC; optional LLM behind port |
| Out of scope | Validating source LIMS/MES themselves; legal certification claims |

## 2. Hazard analysis

| ID | Hazard | Harm |
|---|---|---|
| H-01 | Assist emits or implies batch disposition | Inappropriate release/reject path |
| H-02 | Conflicts hidden or “resolved” by model | QP decides on false completeness |
| H-03 | Silent unit conversion | Wrong OOS interpretation |
| H-04 | Final reportability / case merge | Regulatory / patient safety decision error |
| H-05 | Reservation / allocate side effect | Wrong stock movement |
| H-06 | Stale/revoked entitlement allow | Unauthorized GxP data access |
| H-07 | Untrusted SOP as instruction | Malicious or obsolete procedure followed |
| H-08 | Automation bias | Human skips contradictory evidence |
| H-09 | AI outage → unsafe workaround | Shadow spreadsheets without controls |
| H-10 | Fabricated citations | DI failure / inspection risk |

## 3. Failure chains

| Chain | Sequence | Worst outcome |
|---|---|---|
| C-01 | Unapproved mapping applied → false pass → readiness ready → QP trusts | Wrong release narrative |
| C-02 | Untrusted doc retrieved as policy → agent “follows” → prohibited tool call | Side effect / bad advice |
| C-03 | Cached IAM allow after revoke → sensitive batch opened | Confidentiality / integrity |
| C-04 | Model summarizes away gap → human misses sterility excursion | Patient risk via release |
| C-05 | Supply option treated as reservation in downstream manual step | Allocation error |

## 4. Risk controls

| Hazard | Preventive | Detective | Corrective |
|---|---|---|---|
| H-01/H-04/H-05 | Schema forbid + no write tools | Contract negatives | Block release; incident |
| H-02/H-03 | Detectors; unapproved→contradiction | Inject tests | Human resolve; no auto-fix |
| H-06 | AuthZ at execution; max cache age | Stale IAM tests | Deny + audit |
| H-07 | Instruction eligibility (DEC-022) | Untrusted SOP tests | Abstain |
| H-08 | UX: show gaps/conflicts first (Phase 4) | HF eval | Training / checklist |
| H-09 | AI-disabled deterministic path | Continuity drill | Runbook |
| H-10 | Mandatory evidence_item hash | Citation TEVV | Fail closed |

## 5. Residual risk and uncertainty

| Residual | Level | Why acceptable for POC go? |
|---|---|---|
| Human still errs under time pressure | Medium | Assist cannot remove human residual; must not amplify via hidden conflicts |
| Runtime gates not yet coded | High until Phase 5 | **Conditional** — schema controls exist; runtime RED acknowledged |
| Absolute lead-time baseline unknown (A-011) | Medium | Value claim relative until measured |
| Optional LLM prompt bypass | Medium | Port disabled in assessed deterministic scoring path |

## 6. Risk acceptance

| Decision | Condition |
|---|---|
| **Accept to proceed into Phase 4–5 build** | Schema fail-closed green; QRM/CSA/C4/ADRs drafted; runtime tests exist (red) |
| **Conditional-go to defence** | Runtime gates green; no prohibited execution in evaluate; HF bias controls documented |
| **Stop** (DEC-011) | Design requires AI authority for disposition/reportability/allocate |
| **Pivot** | Non-AI waves alone meet board-acceptable progress with lower residual |

**Phase 3 acceptance statement (draft):** Residual risk from unimplemented runtime gates is **acknowledged and not accepted for final release**, but is **accepted for continued design/build** because failing tests are in place and schemas already deny prohibited fields.

## 7. Review triggers

| Trigger | Action |
|---|---|
| Any prohibited field accepted by builder | Critical defect; stop demo claims |
| New interface version | Update ACL + this QRM |
| Automation-bias finding severity ↑ | Strengthen UX / training controls |
| KG revisit (DEC-020) | Re-run hazard H-02/H-10 for graph complexity |
| Hour-18 / Hour-34 reviews | Formal re-acceptance |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-351 | Risk | Residual H-08 until Phase 4 UX | Wrong trust | GxP + HF | Open |
| R-352 | Gap | Named GxP owner TBD | Acceptance lag | Team | Open |

## Traceability and acceptance

| Claim | Control | Test / review | Result |
|---|---|---|---|
| Hazards cover three workflows | §2–3 | Peer review | Draft |
| Controls map to ADRs/tests | §4 | Trace table | Draft |
| Residual explicitly accepted/rejected | §6 | Hour-18 | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | GxP | Pending formal acceptance | | |
