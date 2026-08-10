# Phase 0 — Team Charter and Working Agreements

| Field | Entry |
|---|---|
| Team | Team 3 — Project AEGIS-PHARMA |
| Date | 2026-08-07 |
| Phase | 0 Preflight / orientation |
| Related | `WORKSHOP_DEPLOYMENT_PLAN.md`, `submission/prompts/PROMPT_MAPPING.md`, `submission/evidence/preflight_report.md` |

## 1. Mission

Deliver a defensible, offline-capable intervention for the three mandatory workflows (batch evidence reconciliation, PV intake/signal support, bounded supply options) without taking over regulated human accountability — and defend a go / conditional-go / pivot / pause / stop recommendation with inspectable evidence under `submission/`.

## 2. Role assignment

One person may hold multiple roles. **Independent review must remain visible** for GxP/security-critical artefacts.

| Role | Owns (primary) | Independent reviewer |
|---|---|---|
| Product / value lead | Artefacts 01–04, 30; Prompts 01–03, 13 | Domain & evidence lead (no-AI challenge) |
| Domain & evidence lead | Artefacts 05–09; Prompts 01, 04–05 | Architecture lead |
| Architecture / integration lead | Artefacts 10–12; Prompts 06–08 | GxP lead + Evaluation lead |
| GxP & quality lead | Artefacts 13–15 | Security / privacy lead |
| Security / privacy lead | Artefacts 16–21 (threat via **package #4**); hard-gate security tests | GxP lead |
| Evaluation / reliability lead | Artefacts 22–25; public fixtures; release gates | Build lead |
| Build lead | `submission/src`, `app`, `tests`, `scripts`; Prompts 10–11 | Evaluation lead (schema/contract review) |

Joint ownership (Phase 7): artefacts 26–29, runbooks, evidence packaging — Product/value + Build leads, reviewed by Evaluation lead.

## 3. Working agreements

1. **Write only under `submission/`.** Never edit hashed challenge evidence (`case/`, `data/`, `knowledge/`, `templates/`, package `prompts/`, etc.).
2. **Artefacts only via templates, on the workshop schedule.** Copy `templates/NN_*.md` → `submission/artefacts/NN_*.md` only in the stage that owns them (`WORKSHOP_DEPLOYMENT_PLAN.md`). No parallel output trees; team prompts must not create later-stage artefacts early.
3. **Prompt sequence.** Team prompts `01`→`13` per `PROMPT_MAPPING.md`, always applying the mapped package control prompt(s).
4. **Qualify before architecture/AI.** No model, agent, KG, or vendor lock-in before no-AI comparison (INJ-003) is written in artefacts 01/02.
5. **Preserve contradictions.** Identity, unit, time, authority, terminology conflicts are governed — not silently normalized.
6. **Fail closed.** No code path for batch disposition, final PV decisions, allocation/shipment/recall, or quality-status change. Prove with negative tests.
7. **Tests before inference.** Deterministic contracts and prohibited-action tests precede any model use (`02_build_tests_first`).
8. **Threat model uses repo approach.** Package control #4 + artefact `16_THREAT_ABUSE_MODEL.md` (+ `security-reviewer` agent). No new team threat prompt file.
9. **Skills timing.** Workflow skills (GxP / PV / supply) are for Phase 5–6 build/eval, not Discovery writing.
10. **Assumptions log.** Every assumption needed to proceed is logged below (and later traced into artefacts). No oral-only decisions.
11. **Checkpoints.** Stop and review at hours 7 / 12 / 18 / 26 / 34 / 38 per workshop plan before expanding scope.
12. **Completion reports.** Material increments state: what changed, why simplest sufficient, files affected, validation run/result, residual risk.

## 4. Decision rights (regulated boundaries)

| Decision | AI / system may | Human accountable role |
|---|---|---|
| Batch release / reject / reprocess / recall | Identify gaps/conflicts only | EU QP / Quality |
| Final seriousness, causality, expectedness, reportability, signal | Support intake/analysis only | Global PV / medical review |
| Reserve / allocate / ship / change quality status / initiate recall | Draft options only (`no_side_effects`) | Supply + Quality approvals |
| Clinical eligibility | Out of autonomous scope | Investigator / clinical governance |

## 5. Method stack (Phase 0 confirmed)

| Layer | Location | Use |
|---|---|---|
| Package control prompts | `prompts/PROMPT_LIBRARY.md` | Immutable; always apply |
| Team method prompts | `submission/prompts/01`–`13` | Execution method |
| Mapping | `submission/prompts/PROMPT_MAPPING.md` | Prompt → artefact |
| Commands | `.cursor/commands/00`–`02` | Qualify → map → tests-first |
| Agents | evidence-reviewer, security-reviewer, test-engineer | Independent review |
| Skills | gxp / pv / supply | Phase 5–6 workflows |
| Rules | `pharma-fde.mdc`, engineering-principles | Always on |

## 6. Assumptions and decision log (opened Phase 0)

| ID | Type | Statement | Basis | Impact if wrong | Owner | Status |
|---|---|---|---|---|---|---|
| A-001 | Assumption | `verify_package.py` FAIL in this clone is dominated by `.git` NUL scans + participant-path drift, not corrupt challenge CSVs/knowledge | Preflight classification; original `VALIDATION_REPORT.json` PASS at package build | May need clean-room re-verify before defence | Build lead | Open |
| A-002 | Assumption | Team will prefer deterministic / offline-first implementation unless evidence justifies LLM/KG | `PACKAGE_SCOPE_AND_ASSUMPTIONS.md` participant freedom; INJ-003 | Architecture ADRs change | Product + Architecture | Open — decide after Prompt 02/03 |
| A-003 | Decision | Keep team prompts separate under `submission/prompts/`; do not edit package prompt library | Hash integrity + mapping approach | N/A | Team | Accepted |
| A-004 | Decision | Threat/abuse work uses package control #4 + artefact 16 (no team threat prompt) | Mapping + package library | Artefact 16 ownership = Security lead | Security lead | Accepted |
| A-005 | Assumption | Single-machine offline execution with Python stdlib is sufficient for assessment mode | Scope pack “no hidden services” | If cloud services added later, offline mode still required | Build lead | Open |
| A-006 | Assumption | `no_ai_baselines.csv` value_pct figures are estimates, not measured baselines | `data/no_ai_baselines.csv`; artefact 01/02 | Wrong ROI ranking if treated as facts | Product lead | Open — Phase 1 |
| A-007 | Assumption | Current release lead-time numeric baseline is Unknown in package data | Only BR-01 −14% target present | Cannot claim benefits realisation yet | Evaluation lead | Open — Measure |
| A-008 | Decision | Framing mode = `hypothesis`; capability answer = deterministic fail-closed reconciliation + draft options + HITL; GenAI optional behind interface after Measure | Prompts 01–03; artefacts 01–04 | Architecture must not lock LLM/KG in Phase 2 without challenge | Product + Domain | Accepted — Phase 1 |
| A-009 | Decision | Phase 1 exit = artefacts **01–04** only (workshop Stage 1). No early 06/30. | `WORKSHOP_DEPLOYMENT_PLAN.md` | Phase 2 creates 05–09 | Product lead | Accepted — Phase 1 |
| A-010 | Decision | Delete early `30_ELEVATOR_PITCH.md`; recreate only at Stage 8 / Prompt 13 | User direction 2026-08-07 | Avoid premature defence artefact | Product lead | Accepted |
| A-011 | Decision | Delete early `06_DATA_GOVERNANCE_INTEGRITY.md`; recreate in Stage 2 with 05–09 | User direction: stick to workshop plan | Mapping must not override workshop stages | Product lead | Accepted |
| A-012 | Decision | Stage 2 complete: artefacts **05–09** + evidence map inside artefact 06; **KG deferred for v1** (relational/semantic alternative selected) | `WORKSHOP_DEPLOYMENT_PLAN` Stage 2; artefact 08 | Stage 3 = artefacts 10–15 | Domain + Architecture | Accepted — Phase 2 |
| A-013 | Assumption | RELATIONSHIP_MODEL + rules can satisfy PUB-01–08 without a graph DB | artefact 08 benchmark | May revisit on recall/genealogy Measure fail | Architecture | Open |
| A-014 | Decision | Stage 3 complete: artefacts **10–15** only; architecture review **conditional**; contract tests 6/6 PASS; ADR-001–012 recorded (≥10) | `WORKSHOP_DEPLOYMENT_PLAN` Stage 3 | Stage 4 = artefacts 16–21 | Architecture + GxP | Accepted — Phase 3 |
| A-015 | Decision | Do not start Stage 5 POC coding until Stage 4 threat/privacy artefacts exist (per artefact 11 review conditions) | Checkpoint C3 conditional | Prevents skipping security gates | Build lead | Accepted — **cleared by Stage 4** |
| A-016 | Decision | Stage 4 complete: artefacts **16–21** only; threat via package #4; prohibited-action suite 8/8 PASS | `WORKSHOP_DEPLOYMENT_PLAN` Stage 4 | Stage 5 = POC in src/app/tests | Security + GxP | Accepted — Phase 4 |
| A-017 | Assumption | EU AI Act analysis is provisional training assessment, not legal advice | artefact 19 | Must re-verify before real deployment | Legal/DPO | Open |

## 7. Immediate next step (Phase 1)

1. Copy `templates/01_BUSINESS_CASE.md`, `02_DMAIC_WORKBOOK.md`, `03_STAKEHOLDER_DECISION_RIGHTS.md`, `06_DATA_GOVERNANCE_INTEGRITY.md` → `submission/artefacts/`.
2. Run team prompt `01_discovery.md` with package controls #1 and #2.
3. Cite evidence from `data/*.csv` / `case/*`; do not invent unlabeled facts.
4. Target Checkpoint C1 (hour 7): problem + no-AI qualification review.

## 8. Phase 0 sign-off

| Item | Status |
|---|---|
| Preflight report | Complete — `submission/evidence/preflight_report.md` |
| Team charter | Complete — this file |
| Working agreements | Complete — §3 |
| Role assignment | Complete — §2 |
| Assumptions log opened | Complete — §6 |
| Ready for Phase 1 | **Yes** |
