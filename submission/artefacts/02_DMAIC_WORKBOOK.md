# DMAIC Workbook

> Team3 completed artefact for Phase 1 qualification. Complements `01_BUSINESS_CASE.md`.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Product / value lead (with Domain lead) |
| Version / date | 0.2 / 2026-08-06 |
| Reviewers | Architecture lead; GxP lead |
| Status | Provisional — thin lenses 01–03 done; **full Prompt 09 not run** |
| Related requirements / ADRs | RUB-01, RUB-03; INJ-001…006; D-006 |
| Prompt alignment | `prompts/01_discovery.md` lens; `prompts/02_scqa_minto.md` lens; `prompts/03_prd_vision.md` lens; full workshop = `prompts/09_lean_dmaic.md` (deferred) |

## Purpose

Structure the improvement story for evidence-reconciliation lead time and quality using DMAIC, explicitly separating no-AI levers from any later assistive automation. Per prompt README: Prompts 01–03 write **thin** `dmaic_lens.md` only; this workbook remains the Phase 1 Define/Measure sketch and must be **consolidated** in Prompt 09 — not treated as the full Lean workshop.

**Thin lenses cited:** `prompt_spine/01_discovery/dmaic_lens.md`, `…/02_scqa/dmaic_lens.md`, `…/03_prd/dmaic_lens.md`. Early wastes: `…/01_discovery/early_waste_signals.md`.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-DM-01 | `data/board_requests.csv` | Board BR-01 due 2026-11-30 | −14% release lead time; no spec/Quality-authority change | Synthetic |
| E-DM-02 | `data/kpi_conflicts.csv` | Functional KPIs | Conflicting Manufacturing/Quality/Safety/Clinical targets | Intentional conflict |
| E-DM-03 | `data/no_ai_baselines.csv` | Process-excellence estimates | MDM 38%/10w; rules 27%/6w; genAI 51%/14w | Unvalidated estimates |
| E-DM-04 | `data/ai_use_boundaries.csv` | AI use boundary | Allowed vs prohibited per workflow | Aligns contracts |
| E-DM-05 | `starter/legacy_pharma.py` | Anti-pattern starter | Lexical ready; trusts all MD; mutates supply reservation | Not production code |
| E-DM-06 | `data/continuity_requirements.csv` | Continuity extract | batch/supply: 14-day AI outage with manual runbook; PV: manual runbook, max_ai_outage_hours=0 | Binding for Control |
| E-DM-07 | `case/INTEGRATED_CASE.md` D01–D08 | Case inject catalogue | Genealogy, units, clocks, cold-chain, poisoning injects drive waste | Narrative |

## 1. Define

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Framing mode | `hypothesis` — Measure-first; do not scale automation on Unknown baselines | Product | Prompt 01 sufficiency |
| CTQ / Y metric | Release-pack evidence cycle time (proxy until measured); secondary: PV clock-complete intake rate; supply option latency to governance | Product | E-DM-01; Prompt 02 metrics |
| In-scope process | Cross-system evidence gather → conflict detect → human review → (human) regulated decision outside system | Domain | Case §§4–5; PRD in-scope |
| Out of scope | Autonomous disposition, final PV, allocate/ship/recall | GxP | E-DM-04; `scope_in_out.md` |
| Voice of customer | Board wants speed; QP wants completeness; Safety wants timeliness; Manufacturing wants continuity (E-DM-02; stakeholder pack) | Product | Stakeholder artefact 03 |
| Problem statement | Evidence reconciliation waste and conflict mishandling inflate lead time and inspection risk under KPI conflict | Product | SCQA Complication |

## 2. Measure

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What we can measure now | Presence of unit/authority/time conflicts in packaged CSVs; starter failure modes; contract pass/fail on prohibited outputs; continuity requirements | Evaluation | E-DM-05; contract tests PASS |
| What is missing | Empirical distribution of current release lead time at NTG | Evaluation | R-BC-02 |
| Operational definitions | “Conflict correctly flagged” = both sides cited, no silent merge; “side-effect free” = no inventory/disposition field writes | Architecture | Workflow contracts |
| Baseline clue | Diagnostics: stale entitlement, model hash mismatch, unapproved unit mapping, untrusted knowledge | Security | Phase 0 F-001 |

## 3. Analyse

| Waste / failure mode | Evidence | Root-cause hypothesis | Lever |
|---|---|---|---|
| Searching many systems / re-entry | Case §2 brownfield | No single authoritative evidence register | MDM + register (no-AI) |
| Silent unit conversion | INJ-024; diagnostics | Unapproved interface mapping | Rules + abstain (no-AI) |
| Trusting all documents equally | Starter `search_knowledge`; INJ-065 | Missing authority/effective-date filter | Authority model (no-AI) |
| KPI-driven shortcut to “ready” | E-DM-02; starter `batch_ready` | Lexical status checks | Schema readiness enums only |
| Supply mutation in “planning” | Starter `plan_supply` | Tooling allows side effects | `no_side_effects` hard fail |
| Hidden review cost | cost_model zeros | Incomplete TCO | FinOps correction |
| GenAI as first lever | E-DM-03 51%/14w | Attractive headline value, longer, doesn’t fix MDM | Sequence MDM/rules first (D-006) |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Vital few | Identity/unit/time/authority conflicts; prohibited side effects; missing manual mode | Domain / Security | Analyse table |
| AI vs non-AI attribution | Majority of vital few are data/governance/rules defects addressable without generative AI | Product | E-DM-03; D-006 |

## 4. Improve

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Improve package | (1) Master-data repair backlog from 84-inject register; (2) rules/checklists and versioned contracts; (3) deterministic assist for cite/flag/abstain/options; (4) optional LLM only behind port, off by default | Architecture | D-003, D-006 |
| Pilot slices | NCB-204 batch readiness; PV duplicate/clock fixtures; NCS-310 cold-chain options | Product | Portfolio risks; PUB fixtures |
| Guardrails | Fail closed on prohibited fields; execution-time authz; poisoned-tool deny | Security / GxP | Hard gates |

## 5. Control

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Process controls | Release gates per EVALUATION_PLAN; failed gates block “ready” | Evaluation | Phase 6 |
| Continuity control | Manual runbooks required; batch/supply tolerate 14-day AI outage; PV must run without inference (max_ai_outage_hours=0) | Reliability | E-DM-06 |
| Change control | Model/prompt/tool/schema versions recorded; unsigned tools denied | GxP / Security | Later artefacts 13–16 |
| Audit | Preserve provenance, as-of, abstentions; no irreversible silent merges | Domain | Hard gates |

## 6. Failure modes and verification

| Failure mode | Detection | Verification |
|---|---|---|
| Auto-release / disposition | Schema + negative tests | `negative_batch_prohibited.json` pattern in submission tests |
| Final PV conclusion | Schema + negatives | PV prohibited sample pattern |
| Inventory reservation | `no_side_effects` + filesystem/DB assert | Supply negative sample pattern |
| Stale auth used | Entitlement vs cache check | INJ-067 fixtures |
| Poisoned SOP followed | Authority filter + red-team | INJ-065 / MALICIOUS doc |
| Automation bias | Human-review mandatory on high-severity gaps | INJ-071; artefact 04 |

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Verification before scale | Public fixtures + adversarial suites must pass gates; clean-room reproduce | Evaluation | DoD §5–6 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-DM-01 | Gap | No measured lead-time baseline in package | Proxy metrics only | Evaluation | Phase 6 | Open |
| R-DM-02 | Risk | Parallel genAI build distracts from MDM | Value leakage | Product | Scope review | Open |
| R-DM-03 | Assumption | Rules+MDM estimates roughly additive with caution | Planning error | Product | Measurement | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Thin DMAIC lenses 01–03 | prompt_spine dmaic_lens files | Prompt exit criteria | `prompt_spine/01_discovery|02_scqa|03_prd/dmaic_lens.md` | Complete |
| Full Lean/DMAIC workshop | Prompt 09 consolidation | Later phase | `prompts/09_lean_dmaic.md` | Deferred |
| DMAIC + benefits path | This workbook + business case | Phase 1 checkpoint | `submission/artefacts/02_DMAIC_WORKBOOK.md` | Provisional |
| No-AI first experiment | D-006 | Defence narrative | `no_ai_baselines.csv`; SCQA Answer | Decided (hypothesis) |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Architecture | Architecture | Confirm deterministic-first improve package | Aligned D-003/D-006 | 2026-08-06 |
| Team3 GxP | GxP | Control must include AI-disabled | E-DM-06 cited | 2026-08-06 |
