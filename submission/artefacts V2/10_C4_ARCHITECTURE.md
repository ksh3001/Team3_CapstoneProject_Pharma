# C4 Architecture

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `09_REQUIREMENTS_TRACEABILITY.md`; INJ-011, INJ-066, INJ-070, INJ-072, INJ-078, INJ-079, INJ-081 |

## Purpose

Defines the system context, containers, components and trust boundaries of the AI Evidence-Reconciliation capability against the platform's **actual current degraded state** — not an idealized fully-available deployment. Accountable owner: capstone team. Completion criteria: every architectural control traces to a concrete platform-state finding below, including at least one currently-blocking finding (model artifact integrity) that the architecture must handle, not assume away.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-1001 | `data/model_registry.csv` | Model registry, undated | `TRN-OMICS-2` (portfolio ranking) status = `research_unqualified`; `GXP-SUM-1` (batch evidence summarisation) status = `pilot`; `PV-NER-4` (case entity extraction) status = `validated_scope_en_de` | `PV-NER-4`'s validated scope is explicitly limited to English/German — this is a stronger, more precise finding than a mere accuracy gap (compare `04_PRODUCT_SERVICE_BLUEPRINT.md` E-303) |
| E-1002 | `data/model_endpoints.csv` | Endpoint status, undated | `primary_large` (EU-West, model `large-1`) status = `down`; `fallback_small` (OnPrem-DE, model `small-7b`) status = `available` | Corroborates `04_PRODUCT_SERVICE_BLUEPRINT.md` E-304 (`DT-2`, AI primary region outage) at the architecture/endpoint level |
| E-1003 | `data/tool_catalog.csv` | Tool catalog, undated | `batch_status_read`: read-only, approved = yes. `batch_status_plus`: read/write disposition, approved = **no**, manifest = `tool_manifest_poisoned.json`. `draft_supply_option`: create draft only, approved = yes | Matches INJ-066; the poisoned tool is already correctly marked unapproved in the catalog — the architecture's job is to make that rejection structurally enforced, not just documented |
| E-1004 | `data/network_zones.csv` | Network zone status, undated | `OT_FILL_FINISH`: restricted trust, "isolated during incident". `GXP_APP`: controlled trust, "degraded". `AI_CLOUD`: external trust, "unavailable primary" | Confirms the whole estate is currently in a degraded, multi-zone incident state (consistent with `04_PRODUCT_SERVICE_BLUEPRINT.md` `DT-1`/`DT-2`) — architecture must be designed for this state as the present reality |
| E-1005 | `data/model_artifacts.csv` | Model artifact integrity check, undated | `GXP-SUM-1`: deployed_hash = `sha256:222BAD`; registry_hash = `sha256:222bbb`; signature = **missing** | Matches INJ-070 exactly, and critically, `GXP-SUM-1` is the model registered for *batch evidence summarisation* (E-1001) — the deployed artifact does not match its registry-approved hash and carries no signature. This is a present-tense, blocking finding, not a hypothetical |
| E-1006 | `data/api_contract_versions.csv` | API contract register, undated | LIMS result v1 uses fields `unit`/`status`; v2 uses `ucum_code`/`lifecycleState` (different field names, not additive); Safety ICSR `E2B_R3` has `precision variable` date semantics | A v1→v2 consumer cannot assume field-name stability; date precision in ICSR must be carried through, not normalized to a false precision |
| E-1007 | `data/vendor_dependencies.csv` | Vendor dependency register, undated | Model hosting, vector store, evaluation, and observability all map to a single vendor, `AIVENDOR-X` | Matches INJ-078 — total vendor concentration across the entire AI stack, a direct architectural and continuity risk |

## 1. System context

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Who/what are the external actors and systems? | Human actors: EU Qualified Person, Safety Physician, Supply Governance Board (`03_STAKEHOLDER_DECISION_RIGHTS.md` §2). External systems: LIMS, MES, RIM/ERP, safety database, warehouse/serialization systems (`case/SOURCE_SYSTEM_FACT_PACK.md`), external CRO labs (E-1006). The AI Evidence-Reconciliation system is one box, strictly downstream of all of these per `05_DDD_CONTEXT_MAP.md` §2. | Capstone team | `03_STAKEHOLDER_DECISION_RIGHTS.md`, `05_DDD_CONTEXT_MAP.md` |
| What is the trust boundary at the system-context level? | `AI_CLOUD` is explicitly an "external" trust zone (E-1004) — the system context diagram must show a trust-boundary line between `GXP_APP` (controlled) and `AI_CLOUD` (external), with only validated, schema-checked traffic crossing it. | Capstone team | E-1004 |

## 2. Container view

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What containers make up the AI Evidence-Reconciliation system? | (1) API/Orchestrator; (2) Model Gateway — routes to `primary_large` or `fallback_small` per E-1002, never assumes primary is up; (3) Tool Execution Service — enforces the `approved` flag in E-1003 as a hard gate, not a UI hint; (4) Retrieval/Evidence layer — consumes domain contexts via the ACLs defined in `05_DDD_CONTEXT_MAP.md` §5; (5) Contract Validation layer — enforces `evaluation/contracts/*.schema.json` on every output; (6) Audit/Evidence Store — append-only, per `knowledge/GXP_DATA_INTEGRITY_STANDARD.md`. | Capstone team | E-1002, E-1003, `05_DDD_CONTEXT_MAP.md` |
| Does the container view show the current degraded state or only the happy path? | It must show both — the Model Gateway container's routing logic is only correctly specified if the diagram/narrative explicitly includes the `primary_large: down` → `fallback_small: available` path (E-1002) as a normal, currently-active branch, not an appendix. | Capstone team | E-1002 |

## 3. Component view

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Model Gateway — Artifact Integrity component | Must verify `deployed_hash == registry_hash` and a valid signature before permitting any inference call to a given model. Applied to current evidence (E-1005), this component would **currently reject `GXP-SUM-1`** — deployed hash `sha256:222BAD` does not match registry hash `sha256:222bbb`, and no signature is present. This is not a future control to design for a hypothetical attack; it is a check that would fire against present data. | Capstone team | E-1005 |
| Model Gateway — Validated-Scope Router component | Must check a model's registered validated scope (E-1001) before routing a request to it — `PV-NER-4` is validated for English/German only; a Hindi or Arabic PV narrative must not be silently routed to it as if in-scope. This is stricter than a confidence-based flag (as drafted in `04_PRODUCT_SERVICE_BLUEPRINT.md` §6): it is an out-of-validated-scope block, not a lower-confidence warning. | Capstone team | E-1001 |
| Model Gateway — Research/Production Separation component | Must block any model registered `research_unqualified` (E-1001, `TRN-OMICS-2`) from being callable by any production decision-support path, directly preventing a recurrence of INJ-011. | Capstone team | E-1001 |
| Tool Execution Service — Manifest Approval Gate | Must check `tool_catalog.csv`'s `approved` field (or its production equivalent) before any tool is registered as callable — `batch_status_plus` (E-1003, unapproved, poisoned manifest) must be structurally unreachable, not merely absent from a default list that a compromised or hallucinating agent could still reference by ID. | Capstone team | E-1003 |
| Contract Validation layer | Already exists and passes for the three workflow schemas (`tools/test_contracts.py`, 6/6) — this component view formalizes where that check sits: after the Model Gateway, before any output reaches a human reviewer. | Capstone team | `tools/test_contracts.py` |

## 4. Critical code/sequence view

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Sequence: batch-evidence reconciliation request, given current platform state | (1) API receives request → (2) Retrieval layer pulls evidence via ACLs (`05_DDD_CONTEXT_MAP.md` §5) → (3) Model Gateway attempts `GXP-SUM-1` (registered for this use case, E-1001) → (4) **Artifact Integrity component rejects it** (E-1005, hash mismatch + missing signature) → (5) Gateway must not silently fall back to an unverified path; it must either use a verified alternative model with equivalent validated scope, or **abstain and escalate** per `knowledge/AI_GXP_BOUNDARY.md` ("abstain or escalate when applicability cannot be established") → (6) Contract Validation → (7) Human review (EU QP) → (8) Audit log. | Capstone team | E-1001, E-1005 |
| What must the sequence never do at step (5)? | Silently substitute an unverified `GXP-SUM-1` artifact "because it mostly matches," or present output to the EU QP without disclosing that the primary summarisation model failed integrity verification. | Capstone team | `knowledge/AI_GXP_BOUNDARY.md` |

## 5. Trust and GxP boundaries

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Which models are currently fit for any production-adjacent use at all? | Only `PV-NER-4`, and only within its validated scope (English/German, E-1001). `GXP-SUM-1` is `pilot` status (not validated) **and** currently fails artifact integrity (E-1005) — it cannot be treated as production-ready by either criterion independently. `TRN-OMICS-2` is `research_unqualified` and must never reach portfolio decisions. | Capstone team | E-1001, E-1005 |
| Does this change the Workflow A value case? | Yes, materially — `01_BUSINESS_CASE.md`'s Workflow A value hypothesis assumed an AI-assisted summarisation capability; this architecture review finds the specific model intended for that role (`GXP-SUM-1`) is neither validated nor currently integrity-verified. This must be disclosed as a blocking dependency in the final defence, not smoothed over. | Capstone team | E-1001, E-1005; `01_BUSINESS_CASE.md` |
| Trust boundary for `AI_CLOUD` | External trust (E-1004) — no unvalidated data may cross into `GXP_APP` without passing the Contract Validation layer (§3) first, regardless of which model produced it. | Capstone team | E-1004 |

## 6. Data and event flows

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Does the architecture assume stable field names across API versions? | No — E-1006 shows LIMS result v1→v2 renames `unit`→`ucum_code` and `status`→`lifecycleState` entirely; every consumer of a versioned API needs an explicit per-version adapter, not a single shared parser. | Capstone team | E-1006 |
| How is ICSR date precision handled? | E-1006's `E2B_R3` has "precision variable" date semantics — the architecture must carry the original precision (day/month/year/unknown) through the pipeline rather than defaulting to a false day-level precision, consistent with `knowledge/GXP_DATA_INTEGRITY_STANDARD.md`'s "do not overwrite original values." | Capstone team | E-1006 |

## 7. Deployment and offline mode

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Is offline/degraded mode a future contingency or the current state? | The current state, per E-1004 (`OT_FILL_FINISH` isolated, `GXP_APP` degraded, `AI_CLOUD` unavailable primary) and E-1002 (`primary_large` down). The architecture's offline/degraded-mode path is not a "nice to have" — it is the mode the system must already support to be usable today. | Capstone team | E-1002, E-1004 |
| What is the single biggest continuity risk in the deployment view? | Total vendor concentration (E-1007): model hosting, vector store, evaluation and observability are all `AIVENDOR-X`. Combined with `primary_large` already being down (E-1002), this is not a diversified failure domain — a single vendor incident could plausibly explain the entire current outage. | Capstone team | E-1007, E-1002 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1001 | Risk | `GXP-SUM-1` (Workflow A's intended summarisation model) currently fails artifact integrity verification (hash mismatch, missing signature) | Critical — blocks the model this workflow's value case assumed; requires either re-deployment from a verified artifact or an alternative model before any Workflow A AI-summarisation demo | Capstone team | Immediate — before any Workflow A build claim | Open |
| R-1002 | Risk | `PV-NER-4`'s validated scope (English/German only) is narrower than the full multilingual ambition implied by Workflow B (`case/INTEGRATED_CASE.md` D06, multilingual review) | High — non-English/German PV narratives cannot rely on this model's validated output | Capstone team | Phase 3 (Specify), before Workflow B scope is finalized | Open |
| R-1003 | Risk | Single-vendor concentration (E-1007) across all four AI-platform capabilities | High — informs `27_VENDOR_EXIT_RETIREMENT.md` (not built yet) | Capstone team | Phase 3, vendor-exit planning | Open |
| R-1004 | Risk | `data/model_artifacts.csv` contains an artifact-integrity record (deployed_hash/registry_hash/signature) **only for `GXP-SUM-1`** — `PV-NER-4` and `TRN-OMICS-2` have no corresponding row at all. Discovered by `submission/tests/test_model_gateway.py` while implementing the Model Gateway's fail-closed "no record = deny" policy, not by manual review | High — means `PV-NER-4` cannot currently be selected for ANY language, including English/German, under a strict fail-closed policy, which is a stricter and more honest conclusion than `04_PRODUCT_SERVICE_BLUEPRINT.md`'s original framing (validated-scope gap only) | Capstone team | Immediate — before any Workflow B build claim | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Model artifact integrity is checked before inference (§3, §4) | Model Gateway Artifact Integrity component | Not yet implemented | E-1005 shows this would currently fail if checked | Pending implementation; current data would FAIL if checked today |
| Poisoned/unapproved tool manifest cannot be invoked (§3) | Tool Execution Service Manifest Approval Gate | Not yet implemented | `starter/api_samples/tool_manifest_poisoned.json` | Pending — matches `16_THREAT_ABUSE_MODEL.md` scope (not built yet) |
| Out-of-validated-scope language routing is blocked, not just flagged (§3) | Validated-Scope Router component | Not yet implemented | E-1001 | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
