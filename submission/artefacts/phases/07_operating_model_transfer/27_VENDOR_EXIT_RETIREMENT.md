# Vendor Exit and Retirement

> Team3 Phase 7 artefact (template 27). Exit/portability for assessed POC — **no production LLM vendor** on assessed path.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Architecture / FinOps / Ops |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Security; Evaluation; Product |
| Status | Phase 7 — provisional |
| Related | ADR-001/002/003; INJ-070; Phase 5 FinOps; ports/llm.py |

## Purpose

Inventory dependencies, portability gaps, substitution, exit rehearsal, evidence export, retention/destruction, and retirement approval so concentration risk stays low while LLM remains off.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-VX-01 | `submission/src/ports/llm.py` | No-op LLM port |
| E-VX-02 | `data/model_registry.csv` / INJ-070 | Hash mismatch class |
| E-VX-03 | `data/cost_model.csv` | Inference line item exists; unused assessed |
| E-VX-04 | Challenge LICENSE / package scope | Synthetic training |
| E-VX-05 | `dependency_inventory.csv` | This phase |

## 1. Dependency inventory

| Dependency | Type | Assessed criticality | Lock-in risk |
|---|---|---|---|
| Challenge `data/` / `knowledge/` | Input fixtures | High (demo) | N/A — package |
| Python stdlib + jsonschema | Runtime | High | Low–Med |
| Optional LLM provider | Model API | **None assessed** | Would be High if enabled |
| Enterprise IAM/IdP | Future | Not integrated | — |
| MES/WMS/Safety write APIs | Future | **Not integrated (by design)** | — |
| Local `submission/working/` | Audit/metrics | Med | Portable JSON files |

## 2. Contract and portability gaps

| Topic | Gap |
|---|---|
| Model contract | No production MSA — port is replaceable NoOp |
| Data portability | Packs/audits are JSON under submission; challenge tree stays with package |
| Prompt IP | None on assessed path |
| Tool manifests | Must remain allow-listed; poisoned fixture never loaded |
| Schema authority | `evaluation/contracts/` package + participant pin |

## 3. Substitution strategy

| If… | Then… |
|---|---|
| LLM vendor required later | Keep `LLMPort` interface; ADR-002 gates; registry hash; AI-disabled fallback |
| jsonschema unavailable | Fail closed validate or pin vendored copy under submission (change control) |
| Challenge package withdrawn | Export submission artefacts + evidence JSON; stop regulated claims |
| Write-plane vendor proposed | **Deny** unless ADR-003 reopen + Phase 3–6 re-assurance |

## 4. Exit rehearsal

| Rehearsal | POC evidence | Status |
|---|---|---|
| Run with LLM disabled | AC-050/051; default mode | **Done** |
| Swap narrator to NoOp | Already NoOp | **Done** |
| Export audits/metrics | `working/` copy | Manual OK |
| Full vendor cutover under load | N/A — no vendor | Deferred |
| AC-052 continuity drill | Ops | **Open** |

## 5. Evidence and data export

| Asset | Export path |
|---|---|
| Phase evidence JSON | `submission/evidence/phase*.json` |
| Artefacts | `submission/artefacts/phases/` + `prompts/` |
| Runtime audits | `submission/working/audit/` |
| Test command | `PYTHONPATH=submission python -m pytest submission/tests -q` |
| Challenge data | Do **not** rewrite; cite package paths |

## 6. Retention/destruction

| Class | Rule |
|---|---|
| GxP-relevant audit (prod hypothetical) | Escalate Legal/Quality — no auto-delete (INJ-061) |
| POC working files | Retain for defence/evaluation window |
| Secrets | None expected in POC; never commit `.env` |
| Synthetic challenge | Controlled by package LICENSE — not Team3 to destroy upstream |

## 7. Retirement approval and residual risk

| Retirement of… | Approver | Residual |
|---|---|---|
| Optional LLM path | Architecture + Sponsor (keep off) | Low |
| Entire AEGIS POC | Product + Evaluation | Demo value lost; no prod dependency |
| Hard-gate tests | **Forbidden** without Evaluation | High if skipped |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-VX-01 | Gap | No signed vendor exit clause (no vendor) | Accepted |
| R-VX-02 | Risk | Future single-model concentration | Blocked by ADR-002 default off |

## Traceability and acceptance

| Claim | Evidence | Result |
|---|---|---|
| Assessed path vendor-independent | NoOp LLM + local rules | Pass |
| Exit rehearsal for AI-disabled | AC-050/051 | Pass |
| Production vendor exit program | — | N/A / deferred |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Architecture | Owner | No LLM vendor on assessed path | Aligns ADR-002 | 2026-08-07 |
