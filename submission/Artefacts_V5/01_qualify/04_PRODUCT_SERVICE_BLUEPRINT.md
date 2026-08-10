# Product and Service Blueprint

> Team3 completed artefact. Defines intended/prohibited uses and human-in-the-loop service design for workflows A/B/C.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Product / value lead |
| Version / date | 0.3 / 2026-08-07 |
| Reviewers | GxP lead; Security lead; HF / privacy |
| Status | Phase 1 complete (v0.3) — intended/prohibited uses locked; `hypothesis` mode |
| Related requirements / ADRs | RUB-02; E-BC-04; D-005, D-006; continuity_requirements.csv |
| Prompt alignment | `prompts/03_prd_vision.md`; mirrors `prompts/03_prd/{vision,prd,scope_in_out}.md` |

## Purpose

Specify the product as a **fail-closed evidence-assist service** with clear personas, jobs-to-be-done, frontstage/backstage flows, human review points, failure/recovery journeys, and success measures—narrower than the enterprise board problem. Business intent aligns to Prompt 03 Vision/PRD; this blueprint adds service/journey detail allowed for the capstone template (still no API/schema lock-in).

**Working title:** AEGIS Evidence Assist (from `prompts/03_prd/vision.md`).

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-PB-01 | `data/ai_use_boundaries.csv` | AI boundary extract | Allowed/prohibited strings per use case | Primary product law |
| E-PB-02 | `data/decision_rights.csv` | Decision rights | AI none / draft only | Accountability |
| E-PB-03 | `starter/contracts/WORKFLOW_CONTRACTS.md` | Contract prose | Batch/PV/supply I/O minima | Align schemas |
| E-PB-04 | `data/continuity_requirements.csv` | Continuity | Manual runbooks; 14-day batch/supply AI outage; PV without inference | Recovery design |
| E-PB-05 | `data/stakeholders.csv` + stakeholder pack | Users | QP, Manufacturing, Safety priorities | Personas |
| E-PB-06 | Case INJ-071, INJ-072, INJ-073 | HF injects | Automation bias; language inequity; accessibility failure | UX constraints |
| E-PB-07 | `evaluation/contracts/*.schema.json` | Executable schemas | additionalProperties false; no disposition | Engineering boundary |

## 1. Personas and jobs-to-be-done

| Persona | JTBD | Success look like |
|---|---|---|
| Quality / QP support reviewer | Assemble a cited readiness picture for a batch as-of now | Gaps/contradictions visible; nothing “released” by software |
| EU Qualified Person | Decide certification using complete evidence | Assist never substitutes judgment; packet completeness clear |
| PV intake scientist | Intake and cluster cases with clocks/terminology provenance | Source facts preserved; duplicates candidates only |
| Safety Physician | Make final safety/reportability calls | System withholds final conclusions |
| Supply planner | Prepare shortage/cold-chain options for governance | Ranked options, constraints, approvals; no stock moves |
| CISO / validator (secondary) | Prove deny paths and auditability | Stale auth and poisoned tools blocked |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Primary jobs | Cite/reconcile/flag/abstain (batch); extract/normalize/cluster/cite (PV); generate options (supply) | Product | E-PB-01 |

## 2. Intended and prohibited uses

### Intended uses

| Workflow | Intended use | Required inputs | Allowed outputs |
|---|---|---|---|
| A `batch_evidence` | GxP evidence reconciliation for **batch-review readiness support** | batch_id, purpose, as_of, authorized user context | Cited evidence, applicable docs, contradictions, gaps, abstentions, review readiness; `execution_status: not_executed` |
| B `pv_intake` | Pharmacovigilance **intake and analysis support** | source package, receipts, product context, purpose, as_of, authz | Preserved source facts, uncertainty, duplicate candidates, clock evidence, terminology/listedness provenance, required human reviews |
| C `supply_options` | **Non-executing** shortage/cold-chain option planning | event, inventory snapshot, quality status, demand, constraints, purpose, as_of, authz | Ranked draft options, violated constraints, approvals/impacts; `no_side_effects: true` |

### Prohibited uses (hard fail)

| Workflow | Prohibited | Source |
|---|---|---|
| A | release / reject / reprocess / relabel / recall / any batch disposition | E-PB-01; E-PB-02; DoD |
| B | final seriousness, causality, expectedness, reportability, signal confirmation | E-PB-01; E-PB-02 |
| C | reserve / allocate / ship / change quality status / initiate recall; any inventory mutation | E-PB-01; E-PB-02 |
| All | Using revoked entitlements, unsigned/poisoned tools, or untrusted documents as instructions; silent unit conversion; irreversible case merge; operating without manual AI-disabled path | Hard gates; F-001 |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Product one-liner | Evidence-assist and option drafts under human authority—not an autonomous release, PV, or allocation engine | Product | This section; D-005; Prompt 03 vision |
| Scope hygiene | In/out locked in `prompts/03_prd/scope_in_out.md`; later prompts must not silently pull exclusions | Product | Prompt 03 exit criteria |

## 3. Frontstage/backstage workflow

### Frontstage (user-visible)

1. Authenticated user selects workflow + purpose + as_of object (batch / case pack / shortage event).
2. System shows authorization result (allow/deny) before work.
3. User runs reconciliation/intake/options in **deterministic offline mode** by default.
4. UI presents cited facts, conflicts, abstentions, and required human reviews—not a green “approved” disposition.
5. User exports evidence pack / audit trail for inspection or governance.

### Backstage

1. AuthZ gateway checks current entitlement, purpose, object, role (not cache alone).
2. Evidence loaders read challenge data copies / fixtures; never mutate package `data/`.
3. Authority filter ranks knowledge by status/effective date; quarantines untrusted/malicious text as data.
4. Contract validator enforces schemas; strips/rejects prohibited properties.
5. Audit log stores idempotency key, versions, gate outcomes; optional LLM port skipped in offline/AI-disabled.

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Default mode | Deterministic offline; AI-disabled continuity always available | Architecture | E-PB-04; D-003 |

## 4. Human review touchpoints

| Touchpoint | When mandatory | Human role |
|---|---|---|
| AuthZ failure | Any deny | IAM / supervisor clears purpose or entitlement |
| Conflict abstention | Identity/unit/time/authority unresolved | Domain-accountable reviewer documents resolution |
| Batch readiness high-severity gap | Missing QP packet elements, sterility/OOS conflicts | Quality / QP support—never auto-close |
| PV duplicate candidates | Any merge/no-merge | Safety Physician / delegated intake policy |
| PV clock disagreement | Multiple awareness dates | Safety operations with provenance preserved |
| Supply option selection | Before any external execution | Supply Governance Board |
| Suspected poisoning / injection | Untrusted instruction patterns | Security + Quality |
| Automation-bias check | AI/assist summary present | Reviewer must open omitted critical evidence (INJ-071) |

## 5. Failure and recovery journey

| Scenario | User experience | Recovery |
|---|---|---|
| Model/region outage | Banner: AI unavailable; deterministic path remains | Continue offline; batch/supply up to 14 days per E-PB-04 |
| PV must run without AI | No inference controls shown | Manual intake runbook immediately (max_ai_outage_hours=0) |
| Schema / gate fail | Block “complete”; show failing control IDs | Fix inputs or escalate; no override to prohibited fields |
| Poisoned tool manifest | Tool unavailable | Use approved manifest only; security incident path |
| Checkpoint corruption (INJ-080 theme) | Refuse resume from untrusted state | Reset to last good checkpoint; no duplicate reservations (none allowed anyway) |
| Kill switch | All assist sessions halt | Manual runbooks; preserve audit |

## 6. Accessibility and multilingual experience

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Accessibility | Do not use colour-only status; provide text+icon+machine status codes; full keyboard path for primary flows (responds to INJ-073) | HF / Product | UX acceptance tests Phase 6 |
| Multilingual | PV narratives in Arabic/Hindi must not silently drop below English/German quality—flag low-confidence extraction for human review (INJ-072) | PV / HF | Subgroup eval suite |
| Language of record | Preserve source language verbatim; translations labelled as interpretations | Domain | PV contract source facts |

## 7. Success measures

| Measure | Definition | Gate idea |
|---|---|---|
| Prohibited-action block rate | 100% of negative fixtures denied | Hard gate |
| Conflict handling | Unresolved conflicts never presented as resolved | Hard gate |
| Side-effect free supply | Zero inventory/disposition writes in assessed mode | Hard gate |
| Manual continuity drill | Batch/supply 14-day AI-disabled exercise documented; PV manual path documented | Reliability |
| Review burden | Human review hours × rates tracked (not left at cost_model zero) | FinOps |
| Lead-time proxy | Median evidence-pack assembly time vs Phase 1 baseline once instrumented | Benefits |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Product success ≠ board −14% alone | Meeting lead-time by weakening Quality authority is failure even if faster | GxP / Product | BR-01 constraint |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-PB-01 | Risk | Users treat “review readiness” as release permission | Accountability confusion | Product / GxP | UI copy + training | Open |
| R-PB-02 | Risk | Language inequity creates silent PV misses | Patient safety / compliance | PV / Evaluation | Subgroup gates | Open |
| R-PB-03 | Assumption | Personas derived from pack + 3-row CSV suffice for POC | Missing regional roles | Product | Phase 2 evidence map | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Intended/prohibited uses | Product law + schemas | Contract negatives; authz tests | `submission/artefacts/phases/01_qualify/04_PRODUCT_SERVICE_BLUEPRINT.md` | Phase 1 complete |
| Human oversight | Touchpoints §4 | HF / outage drills | continuity_requirements.csv | Specified |
| Offline / AI-disabled | Runtime modes | PUB-10 class fixtures later | E-PB-04 | Specified |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 GxP | GxP | Readiness must not imply disposition | Explicit prohibited table | 2026-08-06 |
| Team3 Security | Security | AuthZ before work required | Frontstage step 2 | 2026-08-06 |
| Team3 Product | Product | Align with D-006 hybrid no-AI-first | Default deterministic mode | 2026-08-06 |
