# AI-Specific Waste Register

| # | Waste | Assessment (current / proposed) | Obs vs Hyp | Action |
|---|---|---|---|---|
| 1 | **Token waste** | cost_model inference 184k/mo line; assessed path must not call LLM | Observed cost signal; hyp if enabled | NFR-01 LLM calls = 0 assessed; narrator off; no blind retries |
| 2 | **Retrieval waste** | Equal-trust search over mixed catalog incl. malicious | Observed pattern | Applicable Documents filter; quarantine K-998/K-999; scan cap ≤32 (NFR-13) |
| 3 | **Model waste** | Premature genAI; starter unsafe paths; blind model retry | Observed starter; hyp scale | Deterministic-first (ADR-001); mode_violation 503; no LLM retry loop |
| 4 | **Human-review waste** | Review hours = 0 in cost_model; risk of reviewing every trivial pass OR missing high-severity | Observed gap + hyp ops | Log hours (M-06); risk-route HITL; multilingual always review (assumed AMB-PV-02) |
| 5 | **Evaluation waste** | Ad-hoc demos without machine-readable gates | Hypothesized if skipped | FR-007 `/v1/evaluate/run`; AC-060–063; binary hard gates first (AMB-MEAS-01) |
| 6 | **Integration waste** | Per-feature microservice soup; unclear SoT; write adapters | Hyp prevented by C4 | Single Workflow Runtime + ACL; IAM/docs/SoR SoTs; no WMS write |
| 7 | **Context waste** | Reconstructing as_of/citation per UI; large undifferentiated prompts | Hypothesized | Shared kernel fields in pack; Applicable-only return; no full-corpus dumps |
| 8 | **Observability waste** | Logs nobody owns; missing correlation; stack leaks to client | Hyp if unmanaged | Evidence Store audit owner; X-Request-Id; error envelope only (Prompt 08) |

**Scale rule:** Do not add retrieval/model capacity to “burn down” Waiting until M-01/M-06 baselines exist or are explicitly assumed.
