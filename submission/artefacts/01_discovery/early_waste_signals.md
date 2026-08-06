# Prompt 01 — Early Waste Signals

Lean preview only. **Not** measured baselines. **Not** full Prompt 09 workshop.

| # | Signal | DOWNTIME / AI-specific waste | Observed vs hypothesized | Evidence |
|---|---|---|---|---|
| 1 | Hunting evidence across many brownfield systems | Waiting; Motion; Extra processing | Hypothesized | `case/SOURCE_SYSTEM_FACT_PACK.md`; case §2 |
| 2 | Lexical batch “ready” including invalid_sample_prep | Defects; Overprocessing | **Observed** | `starter/legacy_pharma.py` `batch_ready` |
| 3 | Reconciling unit mismatches / unapproved conversions | Defects; Extra processing | **Observed** conflict + hypothesized rework | `lab_results.csv` LR-88; `interface_mappings.csv` approved=no |
| 4 | Equal-trust knowledge retrieval | AI retrieval waste; Defects | **Observed** pattern | `search_knowledge`; K-998 malicious instruction |
| 5 | Using superseded / draft / untrusted docs without filter | Defects | **Observed** corpus composition | `knowledge_catalog.csv` K-007, K-026, K-998, K-999 |
| 6 | Treating quarantine inventory as available; creating reservation in “plan” | Overproduction; Defects | **Observed** | `inventory.csv` quarantine row; `plan_supply` return |
| 7 | Stale cached entitlements after IAM revoke | Defects; Security failure waste | **Observed** | `access_cache.csv` vs `users_entitlements.csv` |
| 8 | Disputed system validation state slows/misleads use | Waiting; Defects | **Observed** conflict | `validation_inventory.csv` triple state |
| 9 | KPI pressure to skip completeness for speed | Defects | Hypothesized | `kpi_conflicts.csv` vs BR-01 |
| 10 | Inference spend without counted human review | Token/cost waste; hidden rework | **Observed** cost model gap / hypothesized ops | `cost_model.csv` zeros; `staff_rates.csv` |
| 11 | Duplicate / clock PV rework | Extra processing; Defects | Hypothesized | INJ-037/038 evidence sources |
| 12 | Automation bias accepting incomplete summaries | Defects | Hypothesized | INJ-071 |

Revisit full DOWNTIME + AI-waste registers in `prompts/09_lean_dmaic.md` after thin lenses from Prompts 01–08.
