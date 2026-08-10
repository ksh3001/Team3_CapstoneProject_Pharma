# Threat and Abuse Model

> Team3 Phase 4 artefact (template 16). Awareness analysis for assessed POC — not a penetration-test certificate.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Security |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Architecture; GxP; Evaluation |
| Status | Phase 4 — provisional (hypothesis) |
| Related | ADR-002/003/004; INJ-065…070; `error_and_security.md`; QRM-01…07 |

## Purpose

Enumerate assets, trust boundaries, abuse cases, and controls for AEGIS-PHARMA assist POC so prohibited agency and trust failures stay fail-closed. Completion: threat coverage for injection, poisoning, exfiltration, tool abuse, excessive agency, replay, supply chain, denial-of-wallet — with tests or explicit residual acceptance.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-TM-01 | `case/INTEGRATED_CASE.md` D10 | Case narrative | INJ-065…070 | Synthetic |
| E-TM-02 | `data/users_entitlements.csv`; `access_cache.csv` | Package | contractor_77 revoked / cache active | Fixture |
| E-TM-03 | `data/tool_manifest_poisoned.json` | Package | Write-seeking tool | Must not load |
| E-TM-04 | `knowledge/` MALICIOUS + catalog | Package | Prompt-injection SOP | Quarantine |
| E-TM-05 | `submission/tests/test_phase3_prohibited.py`; `test_ac_authz.py` | Submission | Negative gates | POC scope |
| E-TM-06 | `artefacts/prompts/08_technical/error_and_security.md` | Submission | Control table | POC authn |

## 1. Assets and trust boundaries

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Critical assets | Evidence packs, AuthZ decisions, audit snapshots, entitlement SoT, approved knowledge corpus, schema contracts | Protect integrity + confidentiality of packs; deny write-plane | C4 + ADR-003/004 |
| Trust boundary IAM vs cache | IAM authoritative (INJ-067) | D-005 / ADR-004 | AC-001; authz_matrix |
| Trust boundary docs | Approved/applicable only; retrieved text = data not instructions | FR-002 | AC-010; phase3 malicious doc |
| Trust boundary tools | No poisoned manifest; no MES/WMS/Safety writes | ADR-003 | phase3 POISON-TOOL |
| System boundary | Assist inside; QP/Safety/Supply Board decisions outside | D-007 | DoD; contracts |

## 2. Threat actors and abuse cases

| Actor / abuse | Scenario (inject) | Control | Residual |
|---|---|---|---|
| Insider / contractor after revoke | INJ-067 cache lag | IAM>cache deny | Low (POC fixture) |
| Malicious supplier content | INJ-065 ignore holds | Quarantine; never execute doc text | Low–Med |
| Compromised tool registry | INJ-066 disposition write | Manifest not loaded; SideEffectGuard; schema reject | Low |
| Curious affiliate scraper | INJ-068 exfil narratives | Purpose-bound AuthZ; minimisation | Med (no full privacy suite) |
| Ransomware / OT cut | INJ-069 | Deterministic offline / AI-disabled | Med (AC-052 drill deferred) |
| Model supply chain | INJ-070 hash mismatch | LLM off assessed; registry check if enabled later | Low (LLM off) |
| Automation-biased reviewer | INJ-071 | Dual-cite; no disposition from AI; HITL | Med (human) |
| Replay / checkpoint abuse | INJ-080 stale resume | Idempotency; no reservation | Low–Med |

## 3. Prompt/retrieval poisoning

| Item | Response | Owner | Acceptance |
|---|---|---|---|
| Hidden SOP instructions | Treated as untrusted data; quarantine path | Security + Quality | AC-010; phase3 |
| RAG instruction override | Forbidden — retrieval never becomes tool call | Architecture | BR-013; error_and_security |
| Fuzzy/dup CSV as authority | Blocked (AMB-PV-01) | PV / Architecture | ADR-007; AC-031 |

## 4. Tool and identity abuse

| Item | Response | Owner | Acceptance |
|---|---|---|---|
| Poisoned tool write | Not on load path | Security | test_phase3_prohibited |
| Excessive agency | No write adapters assessed | Architecture | ADR-003; AC-041–043 |
| Purpose spoof | Purpose allow-list; missing → deny | AuthZ | FR-001; matrix |
| Role inflation | Non-QP roles denied in POC matrix | AuthZ | authz_matrix.csv |

## 5. Data exfiltration and privacy attacks

| Item | Response | Owner | Acceptance |
|---|---|---|---|
| Cross-affiliate PV dump | Purpose + object scope; no bulk export API in POC | Privacy / Security | Template 17; INJ-068 |
| Log leakage | Error envelope strips stacks/secrets | Build | error_and_security |
| Path traversal | Outputs under `submission/` | Build | module_rules |

## 6. Supply chain and denial-of-wallet

| Item | Response | Owner | Acceptance |
|---|---|---|---|
| Model package hash drift | Assessed path LLM=0; enable only with registry match | Architecture | INJ-070; ADR-002 |
| Token / DoW | LLM off; budgets if narrator enabled later | FinOps | NFR-01; cost_model gap |
| Dependency / schema weaken | additionalProperties false; Evaluation approval for bumps | Evaluation | contracts VERSION |

## 7. Controls, tests and residual risk

| Control | Test / evidence | Residual |
|---|---|---|
| IAM>cache | AC-001; phase3; authz_matrix | Accepted Low |
| No disposition / finals / reservation | AC-023/030/043; phase3 | Accepted Low |
| Doc quarantine / poison | AC-010; phase3 | Accepted Low–Med |
| LLM off | AC-051 | Accepted Low |
| Full adversarial privacy red-team | **Not run** (Prompt 12 partial) | **Open Med** → Phase 6/7 |
| Production authn (SSO) | Not in POC | **Open** → prod no-go |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-TM-01 | Gap | Full red-team / privacy suite beyond slice | Med | Security / Evaluation | Phase 6 TEVV | Open |
| R-TM-02 | Assumption | Trusted local CLI user field = POC only | High if exposed | Security | Production deploy | Open |
| R-TM-03 | Risk | Human automation bias (INJ-071) remains | Med | GxP / Product | Training + UX | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Injection / poisoning covered | Quarantine + no manifest | phase3 + AC-010 | TESTS_FIRST_LOG; this file | Pass (POC) |
| Tool abuse / excessive agency | No writes; SideEffectGuard | AC-041–043 | ADR-003 | Pass |
| AuthZ Zero Trust lens | IAM>cache; purpose | AC-001–003 | authz_matrix.csv | Pass |
| Exfil / DoW residual documented | Purpose + LLM off | Partial | §5–6 | Partial |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Security | Owner | Full red-team deferred | Residual R-TM-01 accepted for Phase 4 exit | 2026-08-07 |
