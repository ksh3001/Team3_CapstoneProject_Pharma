# Team Charter — Team-3 / Project AEGIS-PHARMA

**Phase:** 0 Orientation  
**Status:** Active  
**Package:** Workshop-Ready v2 (challenge-only)

## Mission

Deliver a defensible, offline-capable AI Forward Deployed Engineering intervention for NovaCura Therapeutics Group that reduces evidence-reconciliation burden across batch readiness, PV intake support, and supply option planning — without automating regulated accountability.

## Scope boundaries

**In scope**

- Three fail-closed workflows under `submission/`
- Deterministic offline mode, tests, evaluation evidence, 30 artefacts, defence
- Evidence reconciliation, conflict surfacing, human-review handoff

**Out of scope / prohibited**

- Autonomous batch disposition (release/reject/reprocess/relabel/recall)
- Final PV seriousness, causality, expectedness, reportability, or signal decisions
- Inventory reservation, allocation, shipment, quality-status change, or recall initiation
- Editing hashed challenge evidence outside `submission/`
- Real GxP / clinical / patient / regulatory use of this synthetic package

## Roles (assign names in Decision Log DEC-000)

| Role | Accountability |
|---|---|
| Product / value lead | Problem, no-AI case, elevator pitch (01–04, 30) |
| Domain / evidence lead | Inject register, authority/time/unit map (05–09) |
| Architecture / build lead | C4, POC, scripts, `src/`, `app/` |
| GxP / quality lead | Intended use, CSA, QRM, assurance (13–15, 21) |
| Security / privacy lead | Threats, Zero Trust, privacy/RAI (16–18) |
| Evaluation / reliability lead | Suites, gates, FinOps, continuity (22–25, 27) |
| Ops / handover lead | Runbooks, readiness, roadmap (26, 28–29) |

One person may hold multiple roles; independent review for GxP and security remains visible.

## Working rhythm

- Follow `submission/runbooks/EXECUTION_PLAN.md` (~40h, Stages 0–8)
- Hard checkpoints at Hours 7, 12, 18, 26, 34, 38
- Contracts and prohibited-action tests before model inference
- Daily: update assumptions + decision logs; append token utilization via workspace hooks

## Definition of done (team view)

Another qualified person can extract `submission/`, run documented scripts, reproduce tests/evaluation, inspect evidence, operate AI-disabled mode, and understand residual risk without oral knowledge from builders.

## Sign-off (Phase 0)

| Item | Status |
|---|---|
| Boundaries understood | Yes |
| Scoring / hard gates understood | Yes (180 pts; hard gates unconditional) |
| Writable area = `submission/` only | Yes |
| Preflight report filed | Yes (`evidence/phase0_preflight_report.md`) |
