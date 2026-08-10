# Prompt 03 — DMAIC Lens (thin)

**DMAIC focus:** Define (scope of improvement) + Measure targets.  
**Skills:** `process-and-lean-discovery` thin-lens contract.  
**Not** full Prompt 09.

1. **In-scope capabilities that remove waste vs add capability**
   - **Remove waste:** conflict citation/abstention, authZ deny, authority filtering, checklist/rules gates, non-mutating options, Measure instrumentation — cut defects, rework, and unsafe overproduction.
   - **Add capability (bounded):** evidence-assist packing for three workflows — assist only, not new regulated decision rights.

2. **Out-of-scope exclusions that prevent overproduction / extra processing**
   - No auto-release / final PV / allocate-ship — prevents false “complete” work and accountability transfer.
   - No mandatory genAI / vector stack — prevents token/retrieval waste before Measure.
   - No claiming board −14% in POC — prevents optimizing the wrong CTQ.

3. **Success metrics → DMAIC Measure list**

   | Measure | Baseline |
   |---|---|
   | Prohibited-action block rate 100% | N/A |
   | False “resolved” conflicts = 0 | Unknown |
   | Cycle-time proxy | **Unknown** |
   | Supply side effects = 0 | Unknown |
   | AuthZ deny (revoked+cached) | Scenario known |
   | Review hours in TCO | Hours Unknown; rates known |
   | AI-disabled drill pass | Unknown |

4. **Scope that would create token / model / human-review waste if built too early**
   - Generative summarization or broad RAG over mixed-trust knowledge before authority filters, bias controls, and cycle-time/review-hour baselines — keep LLM **off by default** in this provisional PRD.
