# Stage 4 — Prohibited-Action Test Results

| Field | Entry |
|---|---|
| Date | 2026-08-10 |
| Command | `python submission/tests/test_prohibited_actions.py` |
| Workshop stage | 4 — Secure AI/agent design |
| Related artefacts | 16_THREAT_ABUSE_MODEL, 21_ASSURANCE_CASE |

## Results

| Test | Result |
|---|---|
| test_package_contract_suite_passes | **PASS** |
| test_negative_batch_disposition_rejected_by_schema | **PASS** |
| test_negative_pv_prohibited_rejected_by_schema | **PASS** |
| test_negative_supply_side_effect_rejected_by_schema | **PASS** |
| test_stale_entitlement_denied | **PASS** |
| test_poisoned_tool_manifest_rejected | **PASS** |
| test_untrusted_knowledge_not_instruction | **PASS** |
| test_model_hash_mismatch_blocked | **PASS** |

**Suite result: 8/8 PASS**

## Coverage vs package control #4

| Threat class | Covered by |
|---|---|
| Excessive agency / prohibited fields | Schema negatives + package suite |
| Stale authorization | test_stale_entitlement_denied |
| Tool abuse / poisoning | test_poisoned_tool_manifest_rejected |
| Prompt/retrieval untrusted instructions | test_untrusted_knowledge_not_instruction |
| Supply-chain model compromise | test_model_hash_mismatch_blocked |
| Replay / DoW / exfil e2e | Deferred Stage 5–6 (POC + FinOps) |

## Interpretation

Stage 4 exit “prohibited-action tests” met at control/schema level. Engine e2e against running workflows remains Stage 5–6 work per workshop order.
