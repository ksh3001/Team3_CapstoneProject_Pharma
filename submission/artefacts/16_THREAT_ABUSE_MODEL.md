# Threat and Abuse Model

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Security / privacy lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP lead; Architecture lead (`.cursor/agents/security-reviewer.md`) |
| Status | Draft — Workshop Stage 4 |
| Related requirements / ADRs | Package control **#4**; ADR-005–007, 010–012; QRM-05–06; INJ-065–070, 076 |

## Purpose

Threat-model AEGIS using package control prompt #4: map injection, poisoning, tool abuse, stale authorization, replay, exfiltration, excessive agency, supply-chain compromise and denial-of-wallet to controls, negative tests, logs, response and residual risk.

**Method source:** `prompts/PROMPT_LIBRARY.md` §4 (immutable). No separate team threat prompt file.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `prompts/PROMPT_LIBRARY.md` §4 | Package control | Required threat classes | Immutable |
| E-002 | `data/knowledge_catalog.csv` K-999 | Catalog | FAKE_PV / untrusted docs | Challenge |
| E-003 | `knowledge/MALICIOUS_SUPPLIER_DEVIATION.md` | Untrusted upload pattern | Hidden ignore-hold instructions (INJ-065) | Adversarial |
| E-004 | `data/tool_manifest_poisoned.json` / starter sample | Poisoned manifest | batch:disposition:write (INJ-066) | Adversarial |
| E-005 | `data/users_entitlements.csv` | IAM vs gateway | contractor_77 revoked + active_cached (INJ-067) | Challenge |
| E-006 | `data/model_artifacts.csv` | Registry | Hash mismatch; signature missing (INJ-070) | Challenge |
| E-007 | `data/model_usage.csv` / `security_events.csv` | Usage/security | Denial-of-wallet / exfil patterns (INJ-076/068) | Challenge |
| E-008 | `submission/artefacts/10_C4_ARCHITECTURE.md`–`15` | Stage 3 | Trust boundaries + QRM | Draft |
| E-009 | `submission/tests/test_prohibited_actions.py` | Stage 4 | Negative tests | Executable |

## 1. Assets and trust boundaries

| Asset | Trust zone | Boundary control |
|---|---|---|
| Challenge evidence CSVs/docs | Untrusted-as-mutable; immutable for participants | Read-only adapters; no silent clean |
| Knowledge corpus | Mixed trust (approved/superseded/untrusted) | Instruction channel only if approved+applicable |
| IAM entitlements | Authoritative for allow/deny | Re-check at execution; ignore cache alone |
| Tool manifests | Untrusted until signed/allow-listed | Reject disposition:write tools |
| Model artifacts | Untrusted until hash/signature match | Block mismatched deploy |
| AEGIS outputs | Advisory packs | Schema fail-closed; audit |

## 2. Threat actors and abuse cases

| Actor | Abuse goal | Example |
|---|---|---|
| Malicious supplier / document author | Bypass quality hold via AI | INJ-065 |
| Compromised tool publisher | Silent disposition write | INJ-066 |
| Former contractor / insider | Use revoked access via cache | INJ-067 |
| Curious/malicious querier | Exfiltrate identifiable narratives | INJ-068 |
| Cost attacker | Denial-of-wallet via oversized docs | INJ-076 |
| Supply-chain attacker | Swap model package | INJ-070 |
| Over-eager automation | Excessive agency (allocate/release) | Hard gates |

## 3. Prompt/retrieval poisoning

| Threat | Control | Negative test | Log / response | Residual |
|---|---|---|---|---|
| Indirect prompt injection in SOP/PDF | Treat untrusted/non-approved as data only (ADR-006) | `test_untrusted_knowledge_not_instruction` | security_event + gap/flag | Med until PUB-03 e2e |
| Superseded policy retrieved as current | Effective-date + supersession filter | Applicability unit test (Stage 5 deepen) | audit applicable_documents | Low–Med |
| Poisoned embeddings corpus (if later) | Deterministic mode default; corpus version pin | N/A while model off | model_usage deny | Low in v1 |

## 4. Tool and identity abuse

| Threat | Control | Negative test | Log / response | Residual |
|---|---|---|---|---|
| Poisoned tool manifest write disposition | Signed allow-list; deny `*:write` disposition (ADR-007) | `test_poisoned_tool_manifest_rejected` | tool_denied | Low if enforced in code |
| Stale entitlement cache | IAM authoritative at execution (ADR-005) | `test_stale_entitlement_denied` | authorization.deny | Low if enforced |
| Replay of prior allow decision | checked_at + request_id idempotency; re-authz each run | Replay test Stage 5 | audit | Med until coded |
| Segregation bypass | AI cannot self-approve regulated decision | Schema negatives | human_review required | Low |

## 5. Excessive agency / side effects

| Threat | Control | Negative test | Residual |
|---|---|---|---|
| Batch disposition in output | Schema additionalProperties false; no disposition field | Package `negative_batch_prohibited` + local suite | Low |
| Final PV fields | PV schema | `negative_pv_prohibited` | Low |
| Supply reservation/allocate | no_side_effects const; options draft | `negative_supply_side_effect` | Low |
| Agent loops / unbounded tools | No mutating tools in v1; budgets (Stage 6) | Tool allow-list empty for writes | Low in deterministic v1 |

## 6. Exfiltration, supply chain, denial-of-wallet

| Threat | Control | Negative test / monitor | Residual |
|---|---|---|---|
| Cross-affiliate narrative dump | Purpose limitation; minimise fields; deny broad export | Purpose mismatch deny (Stage 5) | Med |
| Model hash mismatch | Block load if deployed≠registry or signature missing | `test_model_hash_mismatch_blocked` | Low if enforced |
| Denial-of-wallet | Size/token budgets; reject oversized; cost alerts | Budget guard unit test (Stage 5–6) | Med |
| OT ransomware degraded mode | AI-disabled continuity (ADR-012) | Offline path AC-010 | Med until runbooks Stage 7 |

## 7. Residual risk and Stage 4 gate

| Item | Status |
|---|---|
| Schema-level prohibited actions | **PASS** (package + local suite) |
| Entitlement / poisoned tool / untrusted instruction / model hash | **PASS** in `test_prohibited_actions.py` (control logic) |
| Full PUB-03/09 red-team e2e against running POC | Deferred Stage 5–6 (POC not yet built — workshop order) |
| Stage 4 exit | Artefacts 16–21 + prohibited-action tests recorded |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | POC engines not yet wired; tests assert control predicates + schemas | Integration residual | Build | Stage 5 | Open |
| R-002 | Assumption | Deterministic-first reduces agentic attack surface | If ADR-011 enabled early, re-threat | Security | Before model on | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Package #4 classes covered | §§3–6 | test_prohibited_actions + test_contracts | E-009 | PASS Stage 4 scope |
| Hard-gate overreach blocked | Schema | negatives | contract_tests_stage3 | PASS |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| GxP lead | Reviewer | Excessive agency tied to schemas | Confirmed §5 | 2026-08-10 |
| Architecture lead | Reviewer | Aligns ADR-005–007 | Confirmed | 2026-08-10 |
