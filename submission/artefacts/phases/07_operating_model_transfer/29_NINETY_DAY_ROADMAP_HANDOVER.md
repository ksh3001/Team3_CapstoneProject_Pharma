# 90-Day Roadmap and Handover

> Team3 Phase 7 artefact (template 29). Measure-first roadmap — no agent/RAG scale in days 0–30.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Product / Sponsors liaison |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Evaluation; Security; Ops; GxP |
| Status | Phase 7 — provisional (hypothesis) |
| Related | Prompt 13 §13/16/19; Phase 5–6 residuals; D-013 |

## Purpose

Prioritize backlog, time-box 0–30 / 31–60 / 61–90 actions, name dependencies, publish handover inventory, and define success/stop criteria for post-capstone transfer.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-RD-01 | Prompt 13 evidence acquisition plan | P0/P1/P2 |
| E-RD-02 | Prompt 13 phased roadmap M1–M3 | Gates |
| E-RD-03 | RR register; Phase 6 open items | Blockers |
| E-RD-04 | `roadmap_90day.csv`; `handover_inventory.csv` | Companions |

## 1. Prioritized backlog

| Priority | Item | Unblocks |
|---|---|---|
| P0 | Median/p90 pack cycle-time sampling | Exit pure hypothesis / ROI honesty |
| P0 | Entitlement SoT policy beyond CSV | Multi-role AuthZ |
| P0 | Knowledge SoT usage rules at as_of | Retrieval confidence |
| P1 | Review-hour sampling × staff rates | Honest TCO |
| P1 | AC-052 continuity drill | RR-02 |
| P1 | Clock field dictionary | ADR-009 |
| P2 | Fuzzy golden set + threshold ADR | AMB-PV-01 |
| P2 | TEVV expansion (privacy/load/subgroup graders) | RR-09 |
| P2 | Real IAM/OIDC + DocMgmt ACL | Prod pattern |

**Explicitly deferred 90 days:** LLM-on-assessed, write-plane, KG product, agent swarm.

## 2. 0–30 day actions

| Action | Owner | Exit |
|---|---|---|
| Sponsor decisions S1–S7 recorded | Product | Written yes/no |
| Start P0 cycle-time data access | Ops / Quality | Sample plan approved |
| Freeze demo narrative = hypothesis | Product / CQO | No −14% proof claims |
| Keep pytest/evaluate green on any change | Build | CI or manual gate |
| IR playbook socialized | Ops / Security | Read confirmation |
| Defence rehearsal prep (Phase 8) | Whole team | Failure demos listed |

## 3. 31–60 day actions

| Action | Owner | Exit |
|---|---|---|
| Deliver first cycle-time / review-hour samples | Ops / FinOps | Dataset + Unknown→measured or assumed |
| Execute AC-052 continuity drill (scoped) | Ops | Drill report |
| Expand AuthZ role matrix beyond QP-only | Security | Matrix + tests |
| Privacy leakage suite slice | Privacy / Eval | Results or residual accept |
| HITL queue metrics stub in ops | Evaluation | Depth/age fields |

## 4. 61–90 day actions

| Action | Owner | Exit |
|---|---|---|
| Security/GxP review of hardened pattern | CISO / GxP | Review minutes |
| TEVV bar agreed with Evaluation | Evaluation | Written suite list |
| ADR-002 revisit **only if** Measure pass | Architecture | Keep off default unless triggers met |
| Production go reassessment | Sponsors | Still expect **no-go** unless §7 of tmpl 28 met |
| Clean-room handover pack refresh | Build / Docs | Inventory signed |

## 5. Dependencies and owners

| Dependency | Provider | Blocks |
|---|---|---|
| Ops data access | Manufacturing / Quality | P0 baselines |
| IAM policy owners | CISO | Prod AuthZ |
| SME review time | Quality / PV / Supply | TCO + rubric |
| Legal Act class | Legal/Compliance | Q-EU-01 |
| Facilitator package LF hashes | Facilitator | A-001 residual |

## 6. Handover inventory

See [`handover_inventory.csv`](handover_inventory.csv). Summary:

| Bundle | Path |
|---|---|
| Phase artefacts 0–7 | `submission/artefacts/phases/` |
| Prompt spine 01–13 | `submission/artefacts/prompts/` |
| Code + tests | `submission/src/`, `submission/tests/` |
| Evidence JSON | `submission/evidence/` |
| Decision log | `phases/00_preflight/00_ASSUMPTIONS_DECISION_LOG.md` |
| Residual risks | `prompts/12_assurance/residual_risk_register.md` |
| Run command | `PYTHONPATH=submission python -m pytest submission/tests -q` |

**Handover stance:** pilot demo package with residuals disclosed; **production authority not transferred**.

## 7. Success and stop criteria

| Success (90d) | Stop / pivot |
|---|---|
| P0 samples in hand or explicit assume | Board demands prohibited automation → stop / escalate charter |
| AC-052 drill done or formally waived | Write-plane funded without ADR reopen → **stop** |
| Demo narrative stays honest | ROI claimed from Missing data → **stop messaging** |
| Hard gates remain green | Gate regression → block demo |
| LLM still off assessed unless ADR-002 | Silent LLM enable → **stop** |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-RD-01 | Assumption | Sponsors grant P0 access | Open |
| R-RD-02 | Gap | Calendar assumes post-workshop capacity | Open |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| 90-day Measure-first plan | §§1–4 + CSV | Pass |
| Production not handed over | §6 stance | Pass |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Product | Owner | No scale-first M1 | Aligns D-013 | 2026-08-07 |
