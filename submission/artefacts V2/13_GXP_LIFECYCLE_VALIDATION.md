# GxP Lifecycle and Validation

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `05_DDD_CONTEXT_MAP.md` E-204; `10_C4_ARCHITECTURE.md` §5; `12_INTEGRATION_CONTRACTS.md` §5; `knowledge/COMPUTERISED_SYSTEM_LIFECYCLE.md` (K-010); INJ-021, INJ-022, INJ-029, INJ-030, INJ-031, INJ-034, INJ-058, INJ-067 |

## Purpose

Establishes the risk-based lifecycle and validation status of the `AI-EVIDENCE` system category using **already-executed validation test results and already-open audit findings**, not a theoretical validation plan. Accountable owner: capstone team. Completion criteria: this artefact does not claim `AI-EVIDENCE` (or any successor built by this team) is production-ready while a directly-relevant validation test is recorded as failed.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-1301 | `data/validation_tests.csv` | Executed validation test log, undated | `VT-1`: system `AI-EVIDENCE`, requirement "citation provenance", result = `fail_on_superseded_doc`. `VT-2`: system `AI-EVIDENCE`, requirement "role revocation", result = `fail_cached_access` | These are **already-run, already-failed** tests on the exact system category this capstone extends — not a hypothetical future test plan. `VT-1` directly falsifies K-003's "detect supersession" mandatory control; `VT-2` is the same failure mode already found independently in `12_INTEGRATION_CONTRACTS.md` E-1203/E-1204 (`contractor_77`), now confirmed as a formal validation failure |
| E-1302 | `data/quality_events.csv` | Quality event register, undated, both open | `QE-100`: deviation, object `NCB204-B24071`, severity `major`, status open. `QE-101`: complaint, object `NCS310-S26033`, severity `critical_potential`, status open | Both objects are already in this team's evidence set for other reasons: `NCB204-B24071` was already flagged for a missing CMO audit commitment (`02_DMAIC_WORKBOOK.md` E-201); `NCS310-S26033` was already used as the recall-scope example sharing `VIAL-V19`/`FF-02` with a lot shipped to AE hospitals (`08_KNOWLEDGE_GRAPH_DECISION.md` E-703). These open events materially raise the stakes of both prior examples |
| E-1303 | `data/audit_findings.csv` | Audit findings register, both open | `AF-1`: data integrity, "shared accounts and missing original records", open. `AF-2`: AI governance, "unclear validated state and vendor change controls", open | These are **independent, official audit findings** that converge with this team's own independently-derived findings (AF-1 ≈ INJ-030 + `06_DATA_GOVERNANCE_INTEGRITY.md` E-503; AF-2 ≈ `05_DDD_CONTEXT_MAP.md` E-204 + `02_DMAIC_WORKBOOK.md` E-202) — this convergence is treated as corroboration, not coincidence |
| E-1304 | `knowledge/COMPUTERISED_SYSTEM_LIFECYCLE.md` (K-010, approved 2026-03-10) | Synthetic NovaCura Global Policy | "Control configuration, access, audit trail, backup, continuity, change and periodic review"; "Preserve records and verification through retirement" | Governs the interpretation of E-1301–E-1303 |

## 1. Intended use and boundary

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Intended use of `AI-EVIDENCE` (and any successor this team builds) | Reconcile/cite/flag/abstain only, per `01_BUSINESS_CASE.md` E-004 — never a system of record, never a decision-maker. Not re-derived here. | Capstone team | `01_BUSINESS_CASE.md` E-004 |

## 2. Risk classification

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Is `AI-EVIDENCE` GxP-relevant despite being advisory-only? | Yes — it directly informs the evidence an EU QP reviews before batch certification (`03_STAKEHOLDER_DECISION_RIGHTS.md` §2); an incorrect or unverifiable citation could materially mislead that review even though the AI makes no decision itself. This places it as GxP-relevant, configured/custom software requiring proportionate validation — consistent with K-010's risk-based approach, though this team does not assert a specific formal GAMP category without further evidence (Gap R-1301). | Capstone team | `03_STAKEHOLDER_DECISION_RIGHTS.md` §2; K-010 |

## 3. Lifecycle deliverables

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Does `AI-EVIDENCE` currently pass its own validation tests? | No — both recorded tests fail (E-1301). `VT-1` (citation provenance / supersession detection) failing means the system can currently cite a superseded document as if current — directly contradicting `knowledge/AI_GXP_BOUNDARY.md`'s "detect supersession" requirement (`04_PRODUCT_SERVICE_BLUEPRINT.md` E-307). `VT-2` (role revocation) failing means a revoked user's access may still be honored — the same failure independently found in `12_INTEGRATION_CONTRACTS.md` §5. | Capstone team | E-1301 |
| What does this mean for any claim this capstone makes about Workflow A readiness? | It cannot be claimed production-ready or even pilot-safe until both `VT-1` and `VT-2` pass — this is now the second independent blocking finding for Workflow A's AI layer, alongside `10_C4_ARCHITECTURE.md` R-1001 (`GXP-SUM-1` artifact integrity failure). Both must be disclosed together in the final defence. | Capstone team | E-1301; `10_C4_ARCHITECTURE.md` R-1001 |

## 4. Validation/assurance strategy

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What must be fixed before re-testing `VT-1`? | A supersession-detection check comparing a cited document's status/effective-date against the current knowledge catalog before citing it — directly implementing `knowledge/AI_GXP_BOUNDARY.md`'s "detect supersession" mandate, which currently fails in practice, not just on paper. | Capstone team | E-1301 |
| What must be fixed before re-testing `VT-2`? | The same live-IAM-check design already specified in `12_INTEGRATION_CONTRACTS.md` §5/§7 (Gap R-1204) — this is one fix serving two purposes: closing a failed validation test here and a security-integration gap there. | Capstone team | E-1301; `12_INTEGRATION_CONTRACTS.md` R-1204 |
| Assurance proportionality | Given `AI-EVIDENCE` is advisory-only but GxP-relevant (§2), a full computer-system-validation (CSV) package proportionate to that risk tier is required, not the lightest-touch "business support" tier implied by one of the three conflicting classifications already found in `05_DDD_CONTEXT_MAP.md` E-204. | Capstone team | `05_DDD_CONTEXT_MAP.md` E-204 |

## 5. Supplier and configuration controls

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Are configuration/change controls for this system category adequate today? | No — `AF-2` (E-1303) is an official open audit finding stating "unclear validated state and vendor change controls," which independently corroborates two of this team's own findings: the 3-way validation-state ambiguity (`05_DDD_CONTEXT_MAP.md` E-204) and the unapproved emergency MES change (`02_DMAIC_WORKBOOK.md` E-202). | Capstone team | E-1303 |
| Does vendor concentration (`10_C4_ARCHITECTURE.md` E-1007) compound this? | Yes — a single vendor (`AIVENDOR-X`) across model hosting, vector store, evaluation and observability means a vendor-side change-control failure would simultaneously affect every layer of assurance for this system, not just one component. | Capstone team | `10_C4_ARCHITECTURE.md` E-1007 |

## 6. Change and periodic review

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Do the open quality events (E-1302) change how this team should treat its own example data? | Yes — `NCB204-B24071` (used as the Workflow A example batch) has an open **major** deviation (`QE-100`), and `NCS310-S26033` (used as the Workflow C recall-scope example) has an open **critical-potential** complaint (`QE-101`). Any demonstration using these batches must disclose these open events, not present the batches as generic clean examples. | Capstone team | E-1302 |
| Does this affect the recall-scope decision in `08_KNOWLEDGE_GRAPH_DECISION.md`? | It raises its real-world stakes — `NCS310-S26033`'s shared-component/equipment link to a lot already distributed to AE hospitals (`08_KNOWLEDGE_GRAPH_DECISION.md` E-703) is now paired with an open critical-potential complaint on that same lot, reinforcing (not changing) the earlier decision that this traversal is genuinely graph-shaped and safety-relevant. | Capstone team | E-1302; `08_KNOWLEDGE_GRAPH_DECISION.md` E-703 |
| Periodic review trigger | Any open major/critical quality event on a batch already referenced in this team's evidence set must trigger a review of whether that example remains appropriate to use in a public demo, or should be replaced/annotated. | Capstone team | E-1302 |

## 7. Retention and retirement

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Does this artefact change the retention position from `06_DATA_GOVERNANCE_INTEGRITY.md`? | No — retention/hold/deletion analysis is not re-derived here; cross-referenced only. | Capstone team | `06_DATA_GOVERNANCE_INTEGRITY.md` |
| What must be preserved if `AI-EVIDENCE` (or its successor) is eventually retired? | Per K-010, "preserve records and verification through retirement" — including the `VT-1`/`VT-2` failed-test history itself, so a future auditor can see the system was not silently promoted to production status while these were open. | Capstone team | E-1304 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1301 | Gap | No specific formal risk category (e.g., GAMP-style) is asserted for `AI-EVIDENCE`, pending fuller risk-assessment evidence | Medium | Capstone team | Phase 3 (Specify) | Open |
| R-1302 | Risk | Two validation tests (`VT-1`, `VT-2`) directly relevant to this capstone's core workflow are recorded as failed and have no evidenced remediation yet | Critical — third independent blocking finding for Workflow A readiness, alongside `10_C4_ARCHITECTURE.md` R-1001 and `12_INTEGRATION_CONTRACTS.md` R-1203/R-1204 | Capstone team | Before any "production-ready" claim | Open |
| R-1303 | Risk | Example batches used elsewhere in this submission (`NCB204-B24071`, `NCS310-S26033`) carry open major/critical quality events | Medium-High — any demo must disclose this, not present clean-looking examples | Capstone team | Before any public demo/defence | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Citation supersession detection works | `AI-EVIDENCE` validation suite | `VT-1` | `data/validation_tests.csv` | **FAIL (recorded)** — remediation required |
| Role revocation is honored without delay | `AI-EVIDENCE` validation suite / `12_INTEGRATION_CONTRACTS.md` live-IAM check | `VT-2` | `data/validation_tests.csv` | **FAIL (recorded)** — remediation required, shared fix with `12_INTEGRATION_CONTRACTS.md` R-1204 |
| Example batches' open quality events are disclosed in any demo | Demo/defence script requirement | Not yet implemented | E-1302 | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
