# Prompt 11 — DMAIC Lens (thin)

**DMAIC focus:** Improve execution — remove waste while building; avoid new AI wastes.

1. **Prompt 09 must-fix items implemented**
   - Failing-then-green AC tests for authz/docs/batch/PV/supply/gates  
   - No write-plane / disposition / allocate tasks  
   - LLM off; fuzzy blocked  
   - Measure metrics emit + review-hour template  

2. **New wastes during build?**
   - Minimal: bootstrap generator scripts under `submission/scripts/` (dev-only; not runtime agent loops)  
   - No token/RAG/narrator path introduced  
   - jsonschema `RefResolver` deprecation warning only (tech debt, not Model waste)

3. **Measure instrumentation**
   - Shipped: `working/metrics/*.json` per workflow; evaluate results JSON  
   - Still missing: ops-measured cycle-time / review-hour baselines (Unknown)

4. **Deferrals → Analyze/Improve**
   - AC-052 continuity drill (Phase 7)  
   - AMB-PV-01 fuzzy threshold  
   - Production IAM/DocMgmt/TEVV scale (`poc_vs_production.md`)
