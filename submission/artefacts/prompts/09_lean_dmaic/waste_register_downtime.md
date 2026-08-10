# DOWNTIME Waste Register (AI FDE)

Labels: **Observed** = package/fixture evidence; **Hypothesized** = case/ops inference without measured baseline.

| Code | Waste | Where (current / proposed) | Obs vs Hyp | Impact | Eliminate / simplify action |
|---|---|---|---|---|---|
| D | Defects — lexical batch ready / invalid_sample_prep | Current starter; proposed Rules + readiness enum | Observed | False ready → Quality risk | Replace lexical ready; BR-022 / AC-022; never map ready→disposition |
| D | Defects — unit mismatch silent convert | LR-88; interface mapping approved=no | Observed | Wrong potency narrative | Dual-cite conflict; no silent convert (ADR-008, AC-020) |
| D | Defects — untrusted/malicious docs as instructions | K-998/K-999; equal-trust search | Observed | Injection / wrong authority | Applicable Documents only; quarantine (FR-002, AC-010) |
| D | Defects — stale AuthZ cache | contractor_77 | Observed | Unauthorized pack/options | IAM > cache every call (ADR-004, AC-001) |
| D | Defects — automation bias incomplete summaries | If genAI on before Measure | Hypothesized | Hidden omissions | LLM off default (ADR-001/002); cite/flag only |
| D | Defects — KPI pressure skip completeness | Ops under BR-01 pressure | Hypothesized | Incomplete packs shipped as “done” | Gates block ready on hard fails; −14% not sole CTQ |
| O | Overproduction — quarantine as available | inventory + starter plan | Observed | Fake supply options | released-only available (AC-040) |
| O | Overproduction — reservation in “plan” | plan_supply side effect | Observed | Inventory corruption risk | no_side_effects; no reservation (AC-041–042) |
| O | Overproduction — unused reports / agent swarms / write plane | If built vs PRD | Hypothesized (prevented) | Scope creep | C4 minimum; no write container (Prompt 06/07) |
| O | Overproduction — genAI features before Measure | Cost model inference line | Hypothesized scale | Token spend without CTQ proof | Measure-first; ADR-002 gated |
| W | Waiting — multi-system evidence hunt | Brownfield ops | Hypothesized | Long pack cycle | Single cited pack (FR-003–005); instrument M-01 |
| W | Waiting — HITL on conflicts/duplicates/clocks | Proposed runtime queues | Observed need + hyp volume | Safety vs delay | Risk-route; measure queue depth; accept residual |
| W | Waiting — AI-EVIDENCE validation triple-state | validation_inventory | Observed conflict | Blocks “validated DSS” claims | No validated-decision claim; manual policy |
| W | Waiting — model latency on critical path | If LLM sync | Hypothesized | Hang | Mode controller; deterministic path never waits on LLM (AC-050) |
| N | Non-utilized talent — SMEs on repetitive checks | Ops | Hypothesized | Costly talent on rote work | Deterministic checks first; SME on exceptions only |
| T | Transportation — spreadsheet/ETL hops | Brownfield | Hypothesized | Lost provenance | ACL read + citation in pack; no write-back |
| I | Inventory — exception / duplicate / unreviewed queues | Proposed HITL | Hypothesized volume | Backlog aging | Exact/strong_key only; fuzzy blocked; queue metrics |
| I | Inventory — stale embeddings / unreviewed AI drafts | If RAG/narrator early | Hypothesized | Drift + review debt | No embeddings in assessed path |
| M | Motion — UI/system switching; prompt copying | Ops / agent workflows | Hypothesized | Context rebuild errors | Shared kernel as_of/citation; single runtime |
| E | Extra processing — repeated retrieval / agent loops | Unbounded RAG/agents | Hypothesized | Token + time | NFR-13 ≤32 docs; Applicable-only; budgets (ADR) |
| E | Extra processing — duplicate validation / silent unit rework | Lab/mapping conflicts | Observed | Rework loops | Typed conflicts; ADR-008 |
| E | Extra processing — inspection rework from missing audit | If audit absent | Hypothesized | Finding debt | ADR-010; NFR-11 100% |
| E | Extra processing — inventing fuzzy thresholds at build | AMB-PV-01 | Observed ambiguity | Thrash / false accepts | open-blocked; no guessed 0.8 |
