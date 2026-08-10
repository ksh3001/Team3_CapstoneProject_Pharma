# Threat and Abuse Model

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `12_INTEGRATION_CONTRACTS.md`; `10_C4_ARCHITECTURE.md` R-1001/R-1004; ADR-006/007; INJ-066–INJ-070, INJ-076, INJ-080 |

## Purpose

Names the assets, trust boundaries and abuse cases that already have concrete challenge evidence (poisoned tool manifests, unblocked exfiltration, denial-of-wallet, stale entitlements, model-hash mismatch), and binds each to a control already implemented in `submission/src` or explicitly still open. Accountable owner: CISO (role-played) with capstone team as author. Completion criteria: every D10 inject (INJ-066–070) and the related wallet/replay injects map to a control, test, or residual-risk row — none left as narrative colour.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-1601 | `data/security_events.csv` | Security event log, undated | `SEC-1` `cross_affiliate_narrative_query` 48,900 tokens, blocked = **no**; `SEC-2` `oversized_document_loop` 980,000 tokens, blocked = **no** | Matches INJ-068 and INJ-076 — observed, unmitigated at time of capture |
| E-1602 | `data/tool_catalog.csv` + `data/tool_manifest_poisoned.json` | Tool catalogue + poisoned manifest | `batch_status_plus`: permissions `read/write disposition`, approved = **no**, manifest points to poisoned JSON with `batch:disposition:write` and `postAction: set disposition=READY` | Matches INJ-066 — an unapproved tool that would execute regulated disposition if loaded |
| E-1603 | `data/users_entitlements.csv` + `data/access_cache.csv` | IAM + cache, 2026-08-01…03 | `contractor_77` revoked in IAM while gateway cache still `active_cached` until 2026-08-03T10:00Z | Matches INJ-067; >2-day stale-authorization window (`12_INTEGRATION_CONTRACTS.md` E-1203/E-1204) |
| E-1604 | `data/model_artifacts.csv` | Model artifact register | `GXP-SUM-1`: deployed_hash `sha256:222BAD` ≠ registry_hash `sha256:222bbb`; signature = `missing` | Matches INJ-070; integrity failure already enforced by `model_gateway.py` |
| E-1605 | `data/agent_runs.csv` | Agent run log | `AR-77` resume from 380-minute checkpoint → `duplicates_created` | Matches INJ-080; closed by `checkpoint.py` age + idempotency rules |
| E-1606 | `data/network_zones.csv` + `data/downtime_events.csv` | Network / downtime | OT/IT segmentation and ransomware containment downtime `DT-1` (16 h) | Matches INJ-069 — availability/segmentation threat, not yet an executable gate in `submission/src` |
| E-1607 | `starter/legacy_portal.js` | Brownfield starter (unsafe by design) | Client-side logic treats tool descriptions and retrieved text as trusted instructions | Challenge evidence of unsafe retrieval/tool trust patterns; not a production system |

## 1. Assets and trust boundaries

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What assets does this threat model cover? | (1) Regulated decision rights (batch disposition, PV final determinations, stock actions) — must never be tool-executable; (2) safety/PV narratives and trial personal data; (3) model artifacts and registry integrity; (4) IAM/entitlement truth; (5) audit/evidence completeness; (6) token/cost budget (wallet). | Capstone team / CISO | E-1601–E-1605 |
| Where are the trust boundaries? | Untrusted: retrieved documents, tool manifests, user text, vendor feeds, cached gateway state. Trusted only after verification: IAM live state, signed model registry hashes, approved tool catalogue rows (`approved=yes`), schema-validated workflow outputs. Human-approved side effects remain outside the AI boundary entirely. | Capstone team | E-1602, E-1603, E-1604, E-1607 |
| What is explicitly *not* an AI-trusted asset? | Any tool with disposition write (`batch_status_plus`, E-1602) and any model failing integrity (E-1604). | Capstone team | E-1602, E-1604 |

## 2. Threat actors and abuse cases

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| External / insider probing for safety data | Cross-affiliate narrative query consuming 48.9K tokens without being blocked (E-1601 SEC-1) — purpose-limitation failure, not hypothetical. | Capstone team | E-1601; `security_gates.check_purpose_limitation` |
| Malicious or compromised tool publisher | Unapproved `batch_status_plus` with poisoned post-action that would set disposition READY (E-1602). | Capstone team | E-1602 |
| Stale-identity abuse | Revoked contractor still served as active via cache (E-1603). | Capstone team | E-1603; `security_gates.check_live_authorization` |
| Supply-chain / model substitution | Deployed hash mismatch + missing signature on GxP summarizer (E-1604). | Capstone team | E-1604; `model_gateway.verify_artifact_integrity` |
| Agent/replay abuse | Checkpoint resume creating duplicate draft reservations (E-1605). | Capstone team | E-1605; `checkpoint.resume_checkpoint` |
| Wallet attacker / noisy neighbour | 980K-token document loop unblocked (E-1601 SEC-2). | Capstone team | E-1601; `security_gates.check_token_budget` |
| OT ransomware / segmentation failure | Documented containment outage (E-1606) — availability and continuity threat for MES/QMS/historian. | Capstone team | E-1606; Gap R-1602 |

## 3. Prompt/retrieval poisoning

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| How can retrieval poison decisions? | Tool descriptions and retrieved docs are untrusted data (workspace rule + E-1607). A poisoned manifest (E-1602) shows the concrete pattern: a tool description carrying an instruction-like `postAction` that would execute a regulated write if the agent obeyed the manifest as instructions. | Capstone team | E-1602, E-1607 |
| Control decision | Treat tool manifests as data subject to allow-list + approval flag + schema deny-unknown; never execute `postAction` from an unapproved or unverified manifest. Workflow outputs may only reconcile/cite/flag/abstain (Workflow A) or draft options (Workflow C) — never disposition writes. | Capstone team | E-1602; `ai_use_boundaries.csv` via prior artefacts |
| Is prompt-injection from ICSR/batch narrative text modelled? | Partially — fail-closed contracts reject disposition language in outputs (`contracts.find_disposition_language`), but a dedicated adversarial document corpus for intake poisoning is not yet a participant evaluation asset. | Capstone team | Gap R-1601 |

## 4. Tool and identity abuse

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Unapproved disposition tool | `batch_status_plus` is `approved=no` yet present in catalogue with write permissions (E-1602). Any agent runtime must refuse tools where `approved≠yes` or permissions include disposition write. | Capstone team | E-1602 |
| Identity / entitlement abuse | Live IAM check required; cache alone is insufficient (E-1603). Implemented: `check_live_authorization` denies `contractor_77`. | Capstone team | E-1603; `submission/tests/test_security_gates.py` |
| Checkpoint replay as identity/state abuse | Age-bounded, idempotent resume (E-1605). Implemented: 380-minute checkpoint refused. | Capstone team | E-1605; `submission/tests/test_checkpoint.py` |

## 5. Data exfiltration and privacy attacks

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Observed exfiltration pattern | SEC-1 cross-affiliate narrative query not blocked (E-1601). | Capstone team | E-1601; PUB-09 evaluation path |
| Control | Purpose-limitation gate: same-affiliate allowed; cross-affiliate only with named approved purpose. | Capstone team | `security_gates.py`; artefact `17_PRIVACY_ETHICS.md` for privacy-side map |
| Residual | Rate/volume anomaly detection beyond per-request token cap is not yet implemented. | Capstone team | Gap R-1603 |

## 6. Supply chain and denial-of-wallet

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Model supply chain | Hash mismatch + missing signature (E-1604) → select_model abstains for batch summarisation. | Capstone team | E-1604; `test_model_gateway.py` |
| Denial-of-wallet | SEC-2 980K tokens unblocked historically; now denied by `MAX_TOKENS_PER_REQUEST=50000`. | Capstone team | E-1601; `test_security_gates.py` |
| Vendor/OT concentration | Vendor concentration and OT ransomware (E-1606, INJ-078/069) threaten availability; continuity is specified in later artefacts (`24`/`25`), not closed here as a code gate. | Capstone team | E-1606; Gap R-1602 |

## 7. Controls, tests and residual risk

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Controls implemented in code | Purpose limitation, token budget, live IAM, model integrity, checkpoint age/idempotency, disposition-language scanner, schema deny-additional. | Capstone team | `submission/src/*`; 51 unit tests |
| Controls designed but not coded | Allow-list enforcement against poisoned tool catalogue at runtime (logic stated; no `tool_gate.py` yet); OT zone / ransomware continuity drills; adversarial retrieval corpus. | Capstone team | Gaps R-1601, R-1602, R-1604 |
| Residual risk statement | Even with gates, an approved human can still be socially engineered (automation bias INJ-071, covered in artefact 18). Technical gates do not replace human accountability. | Capstone team | `04_PRODUCT_SERVICE_BLUEPRINT.md` E-301 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-1601 | Gap | No participant adversarial document/prompt-injection evaluation set yet | Medium — retrieval poisoning tested only via tool-manifest inject | Capstone team | Before Phase 5 defence | Open |
| R-1602 | Gap | OT ransomware / zone segmentation (INJ-069) has no executable control in `submission/src` | High for MES/QMS availability | Capstone team / CISO | Artefacts 24–25 + runbook | Open |
| R-1603 | Gap | No cumulative/session-level wallet anomaly detector beyond per-request cap | Medium | Capstone team | FinOps artefact 23 | Open |
| R-1604 | Gap | Runtime tool allow-list against `tool_catalog.csv` / poisoned manifest not yet a module | High if agent runtime is expanded | Capstone team | Before any tool-calling agent demo | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Cross-affiliate narrative query denied without approved purpose | `check_purpose_limitation` | `test_security_gates.py`; PUB-09 path | E-1601 | PASS (code) |
| Oversized document loop denied | `check_token_budget` | `test_security_gates.py` | E-1601 | PASS (code) |
| Revoked user denied despite cache | `check_live_authorization` | `test_security_gates.py`; PUB-09 | E-1603 | PASS (code) |
| Compromised model not selected | `verify_artifact_integrity` / `select_model` | `test_model_gateway.py` | E-1604 | PASS (abstain) |
| Stale checkpoint not blindly resumed | `resume_checkpoint` | `test_checkpoint.py`; PUB-13 | E-1605 | PASS (code) |
| Poisoned disposition tool never callable | Tool allow-list | Not yet implemented | E-1602 | FAIL / Open (R-1604) |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Pending | CISO (role-played) | — | — | — |
