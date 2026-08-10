# Threat and Abuse Model

> Phase 4. Zero-trust toward retrieved text, tools, and cached entitlements. Advisory system only.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Security–privacy lead (named TBD) |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Architecture; GxP; Evaluation |
| Status | Draft |
| Related requirements / ADRs | INJ-065…067,076; ADR-033/034/035; FR-T1; artefacts 10–15 |

## Purpose

Identify abuse paths that could turn the evidence assist into an authority-laundering or data-leakage engine, and bind each to a control + test **before** Phase 5 build.

**Completion:** Injection, tool poison, entitlement lag, DoW, and exfiltration have named controls; tool policy frozen in `submission/evaluation/tool_allowlist.json`.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | INJ-065 / MALICIOUS_SUPPLIER_DEVIATION.md | Prompt injection in SOP |
| E-002 | INJ-066 / tool_catalog.csv / tool_manifest_poisoned.json | Poisoned disposition write tool |
| E-003 | INJ-067 / users_entitlements.csv; access_cache.csv | Entitlement revocation lag |
| E-004 | INJ-076 / model_usage; security_events | Denial-of-wallet |
| E-005 | artefact 10 C4 | Trust boundaries; PROHIBITED writes |
| E-006 | DEC-022 / knowledge_trust_catalogue | Instruction eligibility |
| E-007 | evaluation/tool_allowlist.json | Assessed-mode tool policy |

## 1. Assets and trust boundaries

| Asset | Sensitivity | Trust boundary |
|---|---|---|
| Batch / lab / EBR evidence | GxP | Read-only ingress; hashed evidence_item |
| ICSR / PV content | Health / GxP | Purpose-bound; no final safety outs |
| Inventory / quality status | Supply + quality | Draft options only |
| Entitlements cache | Security | Stale ⇒ deny |
| Knowledge corpus | Mixed trust | Instruction filter |
| Tool manifests | Security | Signed allowlist only |
| Model prompts/logs | Leakage risk | Synthetic assessed data; no secrets |

## 2. Threat actors and abuse cases

| Actor | Goal | Abuse case |
|---|---|---|
| Malicious supplier doc | Execute unsafe instruction | INJ-065 SOP injection |
| Compromised tool catalog | Gain write/disposition | INJ-066 poisoned manifest |
| Insider with revoked access | Continue via cache | INJ-067 lag |
| Cost attacker / loop bug | Exhaust tokens/budget | INJ-076 DoW |
| Curious operator | Export beyond purpose | Exfiltration via prompt/logs |
| Over-trusting reviewer | Skip conflicts | Automation bias (→ artefact 18) |

## 3. Prompt/retrieval poisoning

| Item | Control | Test |
|---|---|---|
| Untrusted SOP retrieved | Not instruction-eligible (DEC-022) | `test_untrusted_sop_*` |
| Instruction-like text in evidence | Treat as data; never tool policy | Trust-boundary suite |
| Equal-trust RAG | Forbidden | Retrieval policy Phase 5 |
| Model follows “ignore previous” | Deterministic edges win; LLM optional/disabled in assessed scoring | Continuity + red-team |

## 4. Tool and identity abuse (tool policy)

**Policy (DEC-040):** In assessed mode — `write_tools_allowed=false`; `require_signed_manifest=true`; human confirm for any future side effect; `batch_status_plus` and all prohibited_tool_ids denied.

| Threat | Control | Test |
|---|---|---|
| Poisoned write tool | Allowlist deny + unsigned deny | `test_poisoned_tool_manifest_denied` |
| Blind tool exec | Schema-validated args; no dynamic import of manifests | ADR-034 |
| Stale IAM allow | AuthZ at execution; max cache age | `test_stale_*` |
| Role-only ACL | Purpose + object + tool checks | Phase 5 authZ |

## 5. Data exfiltration and privacy attacks

| Path | Control | Artefact |
|---|---|---|
| Prompt stuffing of PV/PII | Purpose limitation; field minimisation | 17 |
| Log/trace leakage | No secrets; redact in telemetry | 17 / ops |
| Cross-purpose query | Deny mismatched purpose | Trust tests |
| Backup residency break | Residency flag → abstain/deny export | 17 / INJ-064 |

## 6. Supply chain and denial-of-wallet

| Threat | Control |
|---|---|
| Vendor/model price shock | Optional LLM; deterministic path default |
| DoW loops | Step budget, token budget, circuit breaker (scaffolding B5/B7) |
| Poisoned dependency | Pin deps; no unsigned tools |
| Emergency MES hotfix trust | Gap/abstention — not auto-trust (artefact 12) |

## 7. Controls, tests and residual risk

| Control ID | Threats | Phase 4 test status |
|---|---|---|
| C-SEC-01 Instruction eligibility | INJ-065 | RED (stub) |
| C-SEC-02 Tool allowlist | INJ-066 | RED (stub) |
| C-SEC-03 AuthZ freshness | INJ-067 | RED (stub) |
| C-SEC-04 Budget / DoW | INJ-076 | RED (stub) |
| C-SEC-05 Purpose bind | Exfil | RED (stub) |
| C-SEC-06 Schema prohibit | Authority abuse | GREEN (schema) |

**Residual:** Runtime stubs until Phase 5; prompt bypass residual mitigated by assessed LLM-off path (DEC-032).

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-401 | Risk | Red-team depth limited in 40h | Escape | Security | Open |
| A-021 | Assumption | Challenge manifests are the only tool sources in assessed mode | Supply-chain | Security | Accepted for POC |

## Traceability and acceptance

| Claim | Control | Test | Result |
|---|---|---|---|
| Injection blocked as instruction | C-SEC-01 | trust + prohibited suites | RED |
| Poisoned tool denied | C-SEC-02 | trust suite | RED |
| Stale IAM denied | C-SEC-03 | prohibited suite | RED |
| DoW bounded | C-SEC-04 | trust suite | RED |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | Security peer | Pending | | |
