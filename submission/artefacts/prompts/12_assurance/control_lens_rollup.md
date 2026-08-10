# Control Lens Rollup (Prompts 09–12)

Closes the Lean/DMAIC spine for handover to Prompt 13.

## 1. Lens table

| Stage | Path | Focus | Top Control/Measure outcome |
|---|---|---|---|
| 09 | `09_lean_dmaic/dmaic_plan.md` §5 | Control plan defined | Owners + revisit triggers named; Measure-first |
| 10 | `10_tasks/dmaic_lens.md` | Improve sequencing | Failing AC tests first; fuzzy blocked; Measure stubs tasked |
| 11 | `11_build/dmaic_lens.md` | Improve execution | Must-fix implemented; 25 tests pass; AC-052 deferred |
| 12 | `12_assurance/dmaic_lens.md` | Control verification | Hard gates pass; baselines inconclusive; production no-go |

## 2. Measure targets: met / missed / inconclusive

| Target (Prompt 09) | Status |
|---|---|
| Prohibited-action block 100% on fixtures | **met** |
| Supply side effects = 0 | **met** |
| AuthZ revoke+cache deny | **met** |
| False resolved conflicts = 0 (LR-88 path) | **met** |
| Audit fields on authz decisions | **met** (POC files) |
| Evaluate machine-readable results | **met** |
| Cycle-time proxy vs ops baseline | **inconclusive (data scarcity)** |
| Human review hours in TCO | **inconclusive (data scarcity)** (template only) |
| Continuity drill AC-052 | **inconclusive / deferred** |
| Latency p95 ≤30s under expected load | **inconclusive (data scarcity)** |
| LLM calls = 0 assessed | **met** |

## 3. Wastes still open after build

- Waiting on HITL queues — volume Unknown; depth/age not instrumented.  
- Human-review cost waste — hours Unknown.  
- Token/model waste — prevented by LLM-off; cost_model inference line still a FinOps signal.  
- Extra processing if fuzzy guessed — prevented (blocked).  
- Transportation/integration — brownfield ops hunt still hypothesized outside POC pack.

## 4. Next Discover/Frame loop (if any)

**Recommended:** short Measure loop — acquire P0 cycle-time + review-hour samples; execute continuity drill; then re-Frame from `hypothesis` → decision-ready **before** any genAI scale or production-go narrative.

## 5. Control owners for handover

| Control | Owner |
|---|---|
| Evaluation hard gates | Evaluation (Team3) → NTG Quality Systems (later) |
| Side-effect / no-write | Architecture / Supply BC |
| AuthZ IAM>cache | Security / CISO |
| Audit store | Evidence Store owner (Team3 POC) |
| Mode / LLM-off | Mode Controller / Architecture |
| Fuzzy policy | PV BC |
| Continuity drill | Ops / Team3 |
| Framing / claims | Product / CQO |
