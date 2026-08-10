# Control Plan (operating standards)

Aligned to Prompt 09 §5 Control. Status: **documented for POC**; not live-operated in NTG production.

| Control | Standard | Monitor (POC) | Owner | Revisit trigger | Operating? |
|---|---|---|---|---|---|
| Hard evaluation gates | Fail ⇒ ready blocked | `/v1/evaluate/run` + pytest | Evaluation | Any prohibited allow | **Yes** in POC CI/local |
| Side effects | Count = 0 | Supply audit `side_effect_count`; AC-041–043 | Architecture / Supply | Count >0 | **Yes** in tests |
| AuthZ revoke+cache | Deny | AC-001; evaluate AUTHZ fixture | Security | Allow on contractor_77 | **Yes** in tests |
| Audit completeness | 100% checks logged | `working/audit/authz_*.json` | Evidence Store (Team3) | Missing fields | **Partial** (local files) |
| LLM default off | Calls = 0 assessed | `ports/llm.py` call_count; health | Mode Controller | Any assessed LLM call | **Yes** in tests |
| Fuzzy | Disabled | matching_thresholds; no task-025 | PV BC | Threshold + golden set | **Yes** (blocked) |
| HITL queues | Depth/age tracked | *not implemented* | Quality / PV | Sustained growth | **No** — Improve backlog |
| Continuity drill | Pass recorded | checklist stub only | Ops / Team3 | Drill fail | **No** — deferred |
| Framing class | hypothesis until baselines | Product review | Product | Measured cycle-time | **Yes** (policy) |
