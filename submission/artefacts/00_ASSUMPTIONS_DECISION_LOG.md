# Assumptions and Decision Log — Team3

Living log. Separate **facts** (challenge evidence), **assumptions**, **decisions**, and **residual risks**. Do not delete closed items; mark status.

| ID | Type | Status | As-of | Statement | Evidence / rationale | Owner | Invalidation condition |
|---|---|---|---|---|---|---|---|
| A-001 | Assumption + residual risk | Open | 2026-08-06 | On this Windows checkout, SHA-256 mismatches vs `FILE_HASHES.csv` are explained by CRLF line endings; LF-normalized content matches published hashes for spot-checked knowledge files. Challenge meaning is unchanged. | Preflight spot-check `knowledge/AI_GXP_BOUNDARY.md`; verify_package FAIL noise; `.git` NUL walk | Domain / evidence | Facilitator supplies LF tree or rehash; or a material file differs after LF normalize |
| A-002 | Assumption | Open | 2026-08-06 | Capstone may be completed with a deterministic non-LLM core; any model is optional behind a replaceable port and disabled in assessed offline mode. | `PACKAGE_SCOPE_AND_ASSUMPTIONS.md` | Architecture | Scoring or case update requires live inference for pass |
| A-003 | Assumption | Open | 2026-08-06 | Synthetic training data only; no real GxP, clinical, or patient decisions. | `LICENSE_AND_USE.md`, `START_HERE.md` | GxP | Package used outside training context |
| A-004 | Assumption | Open | 2026-08-06 | All 84 injects are disclosed; there are no later instructor-only injects. | `PACKAGE_SCOPE_AND_ASSUMPTIONS.md`, `case/INTEGRATED_CASE.md` §6 | Product | Facilitator injects new sealed materials |
| A-005 | Assumption | Open | 2026-08-06 | Public fixtures PUB-01…15 are input bundles without answer keys; Team3 must justify graders and thresholds before seeing results where possible. | `evaluation/EVALUATION_PLAN.md` | Evaluation | Hidden keys appear in package update |
| D-001 | Decision | Accepted | 2026-08-06 | All Team3 work lands under `submission/`. Challenge folders are read-only evidence. | Workspace rule; package scope | Build | N/A |
| D-002 | Decision | Accepted | 2026-08-06 | Proceed to Phase 1 despite `verify_package` FAIL on CRLF checkout; do not rewrite challenge files to force PASS. | A-001; charter working agreement 7 | Whole team | Material post-normalize content drift proven |
| D-003 | Decision | Accepted | 2026-08-06 | Primary assessed runtime: Python 3.10+ deterministic offline mode; optional LLM port later. | Execution plan; package freedom; reinforced by D-006 | Architecture / Build | Scoring requires live inference |
| D-004 | Decision | Accepted | 2026-08-06 | Knowledge graph is not assumed; Phase 2 must justify vs simpler evidence register. | Case strategic decisions; artefact 08 | Domain / Architecture | Measured query/conflict needs require graph |
| D-005 | Decision | Accepted | 2026-08-06 | Hard fail-closed boundaries for workflows A/B/C are non-negotiable design constraints from day one. | `DEFINITION_OF_DONE.md`; `SCORING_MODEL.md` hard gates; contracts | GxP / Security | N/A |
| D-006 | Decision | Accepted | 2026-08-06 | Hybrid qualification: pursue master-data repair and rules/workflow first; add narrow deterministic evidence-assist POC within `ai_use_boundaries.csv`; do not select genAI as sole intervention. Stop if prohibited actions appear; pivot to schema/checklist-only if MDM+rules meet cycle-time proxies. **Narrative class `hypothesis` until P0 acquisition backlog clears.** | `no_ai_baselines.csv`; artefacts 01–02; Prompt 01–02 spine | Product / Architecture | Measured value upgrades framing to decision-ready |
| D-007 | Decision | Accepted | 2026-08-06 | Intended/prohibited uses locked per artefact 04 and `decision_rights.csv` (AI authority none for certification/reportability; draft only for allocation). | artefacts 03–04; INJ-006; Prompt 03 scope_in_out | Product / GxP | Formal change control amends boundaries |
| D-008 | Decision | Accepted | 2026-08-06 | Phase 1 prompt alignment: run Prompt 01–03 under `submission/artefacts/prompt_spine/`; keep full Prompt 09 deferred; mirror outputs to capstone templates 01–04 as provisional. | `prompts/01|02|03_*.md`; README spine rules | Product | Facilitator requires participant-outputs-v2 path names |
| F-003 | Fact | Observed | 2026-08-06 | Board BR-01: −14% release_lead_time by 2026-11-30 with constraint no specification or Quality-authority change. | `data/board_requests.csv` | Product | Board request superseded |
| F-004 | Fact | Observed | 2026-08-06 | cost_model lists human_quality_review and medical_review at 0 USD/mo while inference is 184000—TCO incomplete. | `data/cost_model.csv`; `staff_rates.csv` | FinOps | Cost model corrected in evidence |
| F-001 | Fact (starter clue) | Observed | 2026-08-06 | `starter/baseline_diagnostics.py` reports: stale entitlement cache; model hash mismatch; unapproved unit mapping; untrusted knowledge present. Incomplete assessment. | Command output; maps toward INJ-067, INJ-070, INJ-024, INJ-065 | Security / Domain | Fuller evidence register supersedes |
| F-002 | Fact | Observed | 2026-08-06 | Executable contracts reject prohibited batch disposition, final PV conclusions, and supply side effects (`tools/test_contracts.py` PASS). | Contract samples under `evaluation/contract_samples/` | Architecture | Schema weakened in submission copy |
| R-001 | Residual risk | Open | 2026-08-06 | If CRLF assumption A-001 is wrong for some files, Team3 could cite drifted challenge text. Mitigation: LF-normalize when hashing citations; prefer relative paths + verbatim excerpts recorded in submission evidence. | A-001 | Domain / Evaluation | Per-file LF hash audit complete |
| R-002 | Residual risk | Open | 2026-08-06 | Board 14% release lead-time target (INJ-001) may create pressure toward prohibited automation. Mitigation: product scope stays evidence-assist only. | `case/INTEGRATED_CASE.md` D01; stakeholder conflicts | Product / GxP | Exec demand overrides charter |

## Open questions (abstain until resolved)

| QID | Topic | Why blocked | Next evidence |
|---|---|---|---|
| Q-001 | Authoritative unit system per lab interface | INJ-024 unit conversion defect; silent conversion forbidden | `lab_results.csv`, `interface_mappings.csv`, LIMS contract v1/v2 |
| Q-002 | Authoritative protocol version per site/country | INJ-013 divergence | `protocol_versions.csv`, `site_approvals.csv`, clinical authority knowledge |
| Q-003 | Which knowledge docs are approved vs draft/untrusted/malicious | Authority filter required before retrieval | `knowledge_catalog.csv`, knowledge front-matter, `MALICIOUS_SUPPLIER_DEVIATION.md` |
| Q-004 | Current entitlement source of truth vs cache | INJ-067 stale cache | `users_entitlements.csv`, `access_cache.csv` |
| Q-005 | Jurisdiction for each regulatory conclusion | Package is not legal advice | `case/REGULATORY_BOUNDARY_PACK.md`, market authorisations |

## Change protocol

1. New assumption → new ID, status Open, owner, invalidation condition.
2. Decision that depends on an open assumption → cite assumption IDs; prefer abstain in POC outputs.
3. Closed items keep history; set Status to Closed/Superseded with pointer to replacement ID.
