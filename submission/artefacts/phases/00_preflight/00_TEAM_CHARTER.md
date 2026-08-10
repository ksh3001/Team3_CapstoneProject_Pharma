# Team3 Charter — Project AEGIS-PHARMA

| Field | Value |
|---|---|
| Team | Team3 |
| Engagement | NovaCura Therapeutics Group — Project AEGIS-PHARMA |
| Mode | Challenge-only, offline-capable FDE capstone |
| Writable area | `submission/` exclusively |
| Charter as-of | 2026-08-06 |

## Mission

Design and demonstrate a **narrow, fail-closed** intervention that reduces evidence-reconciliation burden across batch review readiness, PV intake/signal support, and supply-shortage / cold-chain option planning — without taking over regulated human accountability.

## Mandatory workflows (in scope)

| ID | Workflow | Allowed | Prohibited |
|---|---|---|---|
| A | `batch_evidence` | Cite evidence, conflicts, gaps, abstentions, review readiness | Release, reject, reprocess, relabel, recall, disposition |
| B | `pv_intake` | Preserve source facts, duplicates, clocks, terminology/listedness provenance, human-review queues | Final seriousness, causality, expectedness, reportability, signal confirmation |
| C | `supply_options` | Ranked draft options, violated constraints, approval needs; `no_side_effects: true` | Reserve, allocate, ship, change quality status, initiate recall |

## Role map and decision rights

One person may hold multiple roles; independent review remains visible for hard-gate and security claims.

| Role | Primary accountability | Decision rights | Independent review of |
|---|---|---|---|
| Product / value lead | Problem, KPIs, no-AI comparison, stop/pivot | Scope narrowness vs business ask | Over-automation claims |
| Domain / evidence lead | Inject register, authority, time, units, lineage | Evidence applicability rulings (with abstain) | Silent merges / “cleaned” contradictions |
| Architecture / integration lead | C4, ADRs, contracts, brownfield coexistence | Schema versions and ports | Side-effecting integrations |
| GxP / quality lead | Intended use, CSA/QRM, records/signatures boundary | GxP relevance classification | Any path that looks like disposition |
| Security / privacy lead | Threat model, Zero Trust tools, purpose limitation | Deny-by-default on stale auth / unsigned tools | Tool manifests and retrieval trust |
| Evaluation / reliability lead | TEVV suites, release gates, SLOs, AI-disabled path | Gate thresholds and block/release | Post-hoc threshold fishing |
| Build lead | `submission/src`, scripts, offline deterministic mode | Implementation choices inside contracts | Prohibited fields and mutations |

Accountable human roles in the *enterprise* case (QP, PV head, Quality, etc.) remain outside the system’s authority — see `case/STAKEHOLDER_PACK.md`.

## Working agreements

1. **Qualify before agents.** No model/agent design until artefacts 01–04 and the no-AI baseline are drafted.
2. **Tests before inference.** Prohibited-action, authz, poisoning, and unit/time conflict tests are written before optional LLM ports.
3. **Preserve contradictions.** Records marked draft, superseded, untrusted, referenced_missing, or conflicting are challenge conditions — cite both sides; abstain when unresolved.
4. **Deny by default.** Stale entitlements, unsigned/poisoned tools, purpose mismatch, or ambiguous object identity → refuse or escalate; never invent authority.
5. **Offline first.** Assessed path is deterministic offline mode; AI-disabled continuity is first-class.
6. **Evidence discipline.** Facts, interpretations, assumptions, decisions, and residual risk are labelled separately. Paths are relative; versions and hashes recorded for material outputs.
7. **No challenge mutation.** Do not edit `case/`, `data/`, `knowledge/`, `source_documents/`, `evaluation/`, `requirements/`, `starter/`, or `templates/` to “fix” the case.
8. **Assumption logging.** Any unresolved identity, unit, time precision, terminology, jurisdiction, source authority, or evidence completeness gap is entered in `00_ASSUMPTIONS_DECISION_LOG.md` before proceeding.
9. **Hard-gate ownership.** Security/privacy + GxP leads must sign off (in the decision log) before any demo that could be mistaken for autonomous regulated action.
10. **Clean-room mindset.** Every command a peer needs must live under `submission/scripts/` and runbooks by Phase 7.

## Escalation

| Trigger | Escalate to | Stop rule |
|---|---|---|
| Proposed feature changes batch disposition, final PV, allocation, or recall | GxP + Product leads | Immediate stop; redesign |
| Untrusted or poisoned document treated as instruction | Security lead | Deny; quarantine evidence |
| Unit / identity / clock conflict presented as resolved without dual citation | Domain lead | Reopen; abstain |
| Release gate fail or unreproducible eval | Evaluation lead | Block “ready” claim |
| Package integrity doubt affecting a material claim | Whole team | Cite A-001; do not silently normalize |

## Success definition (Phase 0 lens)

Another team can later extract `submission/`, run documented commands, reproduce tests and evaluation, inspect evidence, operate the manual path, and understand residual risk without oral knowledge from Team3 — per `DEFINITION_OF_DONE.md`.

## Out of scope for the assessed POC

- Live clinical, PV, quality, supply, or recall decisions on real products
- Autonomous inventory mutation or batch certification
- Mandatory knowledge graph, vector DB, or cloud LLM (optional only if justified and offline-replaceable)
- Rewriting challenge evidence or hash corpora
