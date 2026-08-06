# Prompt 01 — Early Waste Signals

Lean preview only. Not measured baselines. Not full Prompt 09.

| Signal | DOWNTIME / AI waste | Observed vs hypothesized | Evidence |
|---|---|---|---|
| Multi-system hunt for release evidence | Waiting; Extra processing; Motion | Hypothesized (case §2) | `case/INTEGRATED_CASE.md` |
| Lexical “ready” shortcuts | Defects; Overprocessing | Observed | `starter/legacy_pharma.py` `batch_ready` |
| Re-entering / reconciling unit conflicts | Defects; Extra processing | Hypothesized | INJ-024; diagnostics |
| Equal-trust document retrieval | AI retrieval waste; Defects | Observed pattern in starter | `search_knowledge`; INJ-065 |
| Inventory reservation during “planning” | Overproduction; Defects | Observed | `plan_supply` reservation_status |
| KPI-driven pressure to skip completeness | Defects | Hypothesized | `kpi_conflicts.csv`; BR-01 tension |
| Oversized / repeated inference spend | Token/cost waste; Denial-of-wallet | Hypothesized | INJ-075/076; cost_model inference |
| Zeroed human review in cost model | Defects in decision quality (hidden waste) | Observed in data | `cost_model.csv` |
| Multilingual extraction inequity | Defects; Uneven quality | Hypothesized | INJ-072 |
| Automation bias accepting incomplete summaries | Defects | Hypothesized | INJ-071 |

Revisit full DOWNTIME + AI-waste registers in Prompt 09 (`prompts/09_lean_dmaic.md`) after lenses 01–08.
