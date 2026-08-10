# Architecture Decision Register

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | Formalizes decisions already made in `01_BUSINESS_CASE.md` through `10_C4_ARCHITECTURE.md` |

## Purpose

Formalizes twelve architecture-significant decisions already reasoned through in artefacts 01–10 into a single, revisitable register, so no decision exists only implicitly inside a narrative artefact. Accountable owner: capstone team. Completion criteria: at least ten ADRs, each with a real alternative considered and rejected, not a single option presented as inevitable.

## Evidence register

This artefact indexes evidence already registered in prior artefacts by ADR; see the "Acceptance evidence" column of each ADR row for the specific evidence ID and source artefact.

## 1. ADR index

| ADR | Title | Status | Source artefact |
|---|---|---|---|
| ADR-001 | Sequence non-AI fixes before any generative-AI component | Accepted | `01_BUSINESS_CASE.md` §3, `02_DMAIC_WORKBOOK.md` §4 |
| ADR-002 | AI scope is strictly reconcile/cite/flag/abstain — no regulated decision authority | Accepted | `01_BUSINESS_CASE.md` E-004, `03_STAKEHOLDER_DECISION_RIGHTS.md` §2 |
| ADR-003 | AI Evidence-Reconciliation is a new, read-only downstream bounded context | Accepted | `05_DDD_CONTEXT_MAP.md` §2 |
| ADR-004 | Identity conflicts require explicit stewardship before merge; no auto-merge | Accepted | `05_DDD_CONTEXT_MAP.md` §3, §5 |
| ADR-005 | No dedicated graph database; in-process graph-shaped queries for three named use cases only | Accepted | `08_KNOWLEDGE_GRAPH_DECISION.md` §3, §7 |
| ADR-006 | Model Gateway verifies artifact hash + signature before inference; abstain on failure | Accepted | `10_C4_ARCHITECTURE.md` §3, §4 |
| ADR-007 | Models are routed by validated scope, not by confidence score alone | Accepted | `10_C4_ARCHITECTURE.md` §3, §5 |
| ADR-008 | Output is structured and evidence-item-linked; no single free-text summary | Accepted | `04_PRODUCT_SERVICE_BLUEPRINT.md` §3, §4 |
| ADR-009 | Degraded/offline mode is designed as the current operating state, not a contingency | Accepted | `04_PRODUCT_SERVICE_BLUEPRINT.md` §5, `10_C4_ARCHITECTURE.md` §7 |
| ADR-010 | Active legal hold takes precedence over a conflicting deletion request, pending identity confirmation | Accepted (conditional) | `06_DATA_GOVERNANCE_INTEGRITY.md` §2, §6 |
| ADR-011 | Per-API-version adapters required; no shared parser assumes stable field names | Accepted | `10_C4_ARCHITECTURE.md` §6 |
| ADR-012 | Tool authorization is a structural gate on an approval flag, not a documented convention | Accepted | `10_C4_ARCHITECTURE.md` §3 |

## 2. Context and forces

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| ADR-001 context | Board demands -14% lead time (E-001) without weakening Quality authority; non-AI options (rules_workflow 27%/6wk, master_data_repair 38%/10wk) are faster and lower-risk than genai_assist (51%/14wk) (`01_BUSINESS_CASE.md` E-003). Root-cause analysis (`02_DMAIC_WORKBOOK.md` §3) found rules/master-data gaps are largely distinct from the residual cross-org evidence-reconciliation gap. | Capstone team | `01_BUSINESS_CASE.md` E-003; `02_DMAIC_WORKBOOK.md` §3 |
| ADR-002 context | `ai_use_boundaries.csv` and `decision_rights.csv` independently cap AI authority at "none"/"draft only" for all three regulated decisions (`01_BUSINESS_CASE.md` E-004, E-007). | Capstone team | `01_BUSINESS_CASE.md` E-004, E-007 |
| ADR-003 context | Multiple bounded contexts (Discovery, Regulatory, Manufacturing, Laboratory, Quality, Safety, Supply) each own their own identity; an AI layer that became a new system of record for any of them would violate `knowledge/IDMP_MASTER_DATA_GOVERNANCE.md`'s stewardship principle. | Capstone team | `05_DDD_CONTEXT_MAP.md` §2, E-408 |
| ADR-004 context | `BX-17` compound-code collision (E-401) and `NCB204-DE`→`NCB-204` ambiguous mapping (E-404) show real identity conflicts already exist; auto-merging either would silently fabricate a resolved identity that isn't actually resolved. | Capstone team | `05_DDD_CONTEXT_MAP.md` E-401, E-404 |
| ADR-005 context | Recall-scope tracing (E-703), PV duplicate clustering (E-704) and serialization reconstruction (E-705) are genuinely graph-shaped, but the flagship genealogy contradiction (E-701/E-702) resolves with a plain two-table join — a full graph database is a heavier tool than the evidenced need justifies at current data volume. | Capstone team | `08_KNOWLEDGE_GRAPH_DECISION.md` §2, §3 |
| ADR-006 context | `GXP-SUM-1`'s deployed artifact hash does not match its registry hash and has no signature (E-1005) — a real, present integrity failure on the exact model intended for Workflow A. | Capstone team | `10_C4_ARCHITECTURE.md` E-1005 |
| ADR-007 context | `PV-NER-4` is registered `validated_scope_en_de` (E-1001); its English F1 (0.91) vs. Hindi/Arabic F1 (0.67/0.63) gap is not just an accuracy question but a validated-scope boundary. | Capstone team | `10_C4_ARCHITECTURE.md` E-1001; `04_PRODUCT_SERVICE_BLUEPRINT.md` E-303 |
| ADR-008 context | Reviewer `QR-11` accepted an `unsafe_candidate` output in 19 seconds based on a one-line summary that omitted an open sterility excursion (E-301) — a real recorded automation-bias failure. | Capstone team | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-301 |
| ADR-009 context | The AI primary-region outage (`DT-2`, E-304/E-1002) has no recorded end time in the evidence — it is not a drill scenario. | Capstone team | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-304; `10_C4_ARCHITECTURE.md` E-1002 |
| ADR-010 context | `LH-44` (active legal hold on `NCB204-301`/`NCB204-B24071`) and `DSR-17` (open deletion request for subject `S-301-044`) may name overlapping data, but the link is not confirmed by a join field (`06_DATA_GOVERNANCE_INTEGRITY.md` R-501). | Capstone team | `06_DATA_GOVERNANCE_INTEGRITY.md` E-505–E-507 |
| ADR-011 context | LIMS result API v1 (`unit`/`status`) and v2 (`ucum_code`/`lifecycleState`) rename fields entirely rather than adding to them (E-1006). | Capstone team | `10_C4_ARCHITECTURE.md` E-1006 |
| ADR-012 context | `batch_status_plus` is an unapproved tool with a poisoned manifest already present in the tool catalog (E-1003) — the attack surface is not hypothetical. | Capstone team | `10_C4_ARCHITECTURE.md` E-1003 |

## 3. Options considered

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| ADR-001 options | (a) Build `genai_assist` first as the primary lever; (b) sequence `master_data_repair` → `rules_workflow` → narrow AI on residual gap only; (c) do only non-AI fixes and stop. Rejected (a): highest estimated value but slowest and highest-risk, and root-cause analysis showed a real residual gap only AI addresses well. Rejected (c): would leave the cross-org evidence-reconciliation gap (E-201/E-206) unaddressed. Chosen: (b). | Capstone team | `01_BUSINESS_CASE.md` §3; `02_DMAIC_WORKBOOK.md` §4 |
| ADR-002 options | (a) Grant AI "recommend" authority with a fast-track human rubber-stamp; (b) grant AI zero authority beyond evidence citation, with mandatory full-evidence human review. Rejected (a): directly enables the automation-bias failure pattern already observed (E-301). Chosen: (b). | Capstone team | E-301, `01_BUSINESS_CASE.md` E-004 |
| ADR-003 options | (a) Let the AI layer write back corrected/reconciled values to source systems for efficiency; (b) strictly read-only, publish-only-its-own-citations. Rejected (a): would make the AI layer an unmanaged, unaudited master-data writer, violating K-015's stewardship requirement. Chosen: (b). | Capstone team | `05_DDD_CONTEXT_MAP.md` E-408 |
| ADR-004 options | (a) Auto-merge identical-looking codes across sources with a confidence threshold; (b) never auto-merge, always surface as a flagged conflict pending stewardship. Rejected (a): `BX-17` (E-401) proves identical codes can be genuinely different substances — a confidence-threshold merge would have silently fabricated a false identity. Chosen: (b). | Capstone team | E-401 |
| ADR-005 options | (a) Adopt a dedicated graph database for all evidence relationships; (b) adopt one only for the three genuinely graph-shaped use cases, using recursive queries/in-process traversal elsewhere. Rejected (a): unjustified by evidenced use cases and current data volume (E-701/E-702 resolve via plain join); adds vendor/architecture surface area. Chosen: (b), with an explicit reconsideration trigger (§7). | Capstone team | `08_KNOWLEDGE_GRAPH_DECISION.md` §3, §7 |
| ADR-006 options | (a) Trust the model registry status field alone; (b) independently verify deployed artifact hash and signature at call time. Rejected (a): would have missed the real `GXP-SUM-1` mismatch (E-1005) entirely, since the registry's hash is correct — only the *deployed* artifact is wrong. Chosen: (b). | Capstone team | E-1005 |
| ADR-007 options | (a) Route by live confidence/F1 score per request; (b) route by the model's registered validated-scope field, hard-blocking out-of-scope languages. Rejected (a): confidence scores can look reasonable even outside validated scope and don't carry the same governance weight as a formal validation record. Chosen: (b). | Capstone team | E-1001 |
| ADR-008 options | (a) Single confidence-weighted natural-language summary per output; (b) structured, evidence-item-linked output requiring per-item expansion before an accept action is enabled. Rejected (a): is exactly the pattern that produced the `CO-1`/`QR-11` failure (E-301). Chosen: (b). | Capstone team | E-301 |
| ADR-009 options | (a) Treat AI unavailability as an edge case tested occasionally; (b) design the primary demo/build path to work with AI unavailable by default, treating availability as the enhancement. Rejected (a): `DT-2`'s outage is open-ended in the evidence, not a drill. Chosen: (b). | Capstone team | E-304, E-1002 |
| ADR-010 options | (a) Honor the deletion request immediately since it is patient-initiated; (b) honor the legal hold immediately since it is a compliance obligation; (c) confirm the subject-to-trial link first, then apply whichever rule the confirmed link dictates. Rejected (a) and (b) as unconditional defaults: both risk acting on an unconfirmed identity link. Chosen: (c). | Capstone team / DPO (role-played) | `06_DATA_GOVERNANCE_INTEGRITY.md` §2 |
| ADR-011 options | (a) One shared parser assuming stable LIMS field names across versions; (b) a versioned adapter per API version. Rejected (a): directly contradicted by E-1006's evidence of a full field rename between v1 and v2. Chosen: (b). | Capstone team | E-1006 |
| ADR-012 options | (a) Document tool approval status as guidance for prompt design; (b) enforce tool approval as a structural gate in the Tool Execution Service, independent of prompt content. Rejected (a): a compromised or hallucinating agent could still reference `batch_status_plus` by ID regardless of prompt-level guidance. Chosen: (b). | Capstone team | E-1003 |

## 4. Decision and rationale

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Common rationale thread across all twelve ADRs | Every decision favors an option that (i) is falsifiable against a specific evidence row rather than a general principle, and (ii) fails closed (abstain/escalate/reject) rather than fails open (assume/merge/proceed) when evidence is incomplete or contradictory — directly implementing the `.cursor/rules/pharma-fde.mdc` instruction to "deny by default on stale or ambiguous state." | Capstone team | `.cursor/rules/pharma-fde.mdc` |

## 5. Consequences and risks

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| ADR-001 consequence | Slower initial AI delivery; the team must actually execute the rules/master-data phases and evidence their effect before claiming AI's marginal contribution, not skip ahead. | Capstone team | `01_BUSINESS_CASE.md` R-002, R-003 |
| ADR-005 consequence | If production data volume proves too large for in-process traversal, this ADR must be revisited (R-701, §7 below) — this is an accepted, bounded risk, not treated as permanently closed. | Capstone team | `08_KNOWLEDGE_GRAPH_DECISION.md` R-701 |
| ADR-006 consequence | Workflow A's AI-summarisation capability is currently **non-functional** until `GXP-SUM-1` is re-deployed from a verified artifact or replaced — this is a direct, disclosed consequence of ADR-006, not a side detail. | Capstone team | `10_C4_ARCHITECTURE.md` R-1001 |
| ADR-007 consequence | Non-English/German PV narratives require full manual processing until a validated multilingual model exists — increases near-term human-review cost, which must be reflected in `23_TOKEN_FINOPS.md` (not yet built). | Capstone team | E-1001 |
| ADR-010 consequence | `DSR-17` cannot be actioned either way until the identity link is confirmed — the data subject's request remains open longer than a naive immediate-deletion policy would allow. | Capstone team / DPO (role-played) | `06_DATA_GOVERNANCE_INTEGRITY.md` R-501 |

## 6. Validation evidence

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Which ADRs already have a passing automated test? | ADR-002 (prohibited-action schemas) — `tools/test_contracts.py`, 6/6 PASS. | Capstone team | `tools/test_contracts.py` |
| Which ADRs have no automated test yet? | ADR-004, ADR-005, ADR-006, ADR-007, ADR-008, ADR-009, ADR-011, ADR-012 — all logged as pending in their source artefacts' traceability tables, not silently assumed enforced. | Capstone team | `10_C4_ARCHITECTURE.md` Traceability table; `08_KNOWLEDGE_GRAPH_DECISION.md` Traceability table |

## 7. Revisit triggers

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| ADR-005 revisit trigger | Production data volume or query-latency evidence showing in-process traversal is insufficient (`08_KNOWLEDGE_GRAPH_DECISION.md` R-701). | Capstone team | R-701 |
| ADR-006 revisit trigger | `GXP-SUM-1` is re-deployed from a verified, signed artifact matching the registry hash — at that point the Model Gateway should permit it again automatically via the same integrity check, not a manual override. | Capstone team | E-1005 |
| ADR-007 revisit trigger | `PV-NER-4` (or a successor model) achieves a formally validated scope extension to additional languages, evidenced by an updated `model_registry.csv`-equivalent status, not just an improved F1 score alone. | Capstone team | E-1001 |
| ADR-010 revisit trigger | The `S-301-044`-to-`NCB204-301` identity link is confirmed or refuted (`06_DATA_GOVERNANCE_INTEGRITY.md` R-501). | Capstone team / DPO (role-played) | R-501 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1101 | Gap | 8 of 12 ADRs have no automated enforcement test yet (§6) | High — these are currently design decisions, not verified controls | Capstone team | Phase 4 (Build) | Open |
| R-1102 | Risk | ADR-006's consequence (Workflow A AI-summarisation non-functional) has not yet been reflected back into `01_BUSINESS_CASE.md`'s value hypothesis as a formal amendment | Medium — risk of an inconsistency between artefacts if not updated | Capstone team | Before final defence | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Every ADR traces to at least one prior artefact's evidence ID | This document, §2 "Acceptance evidence" column | Manual cross-check | `01_BUSINESS_CASE.md`–`10_C4_ARCHITECTURE.md` | Self-verified — no orphan ADRs found |
| At least 10 ADRs present | This document, §1 | Count | §1 ADR index | 12 ADRs — PASS |
| ADR-002 enforcement | `evaluation/contracts/*.schema.json` | `tools/test_contracts.py` | `evaluation/contract_samples/*` | PASS (6/6) |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
