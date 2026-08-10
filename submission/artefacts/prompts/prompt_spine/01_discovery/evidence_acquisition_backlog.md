# Prompt 01 — Evidence Acquisition Backlog

Required because sufficiency scores include Partial/Missing inputs (`hypothesis` mode).

| Priority | Artifact needed | Likely owner / source | Blocks | Why |
|---|---|---|---|---|
| P0 — blocks framing claim of decision-ready | Measured release-pack cycle time distribution (median/p90) | Manufacturing / Quality ops; not in package | Framing → decision-ready; DMAIC Measure | Only BR-01 target exists |
| P0 | Authoritative knowledge catalog with status/effective_at | Document control; start `data/knowledge_catalog.csv` + knowledge MD | Design retrieval; Prompt library §2 | Untrusted/malicious docs present |
| P0 | Entitlement SoT vs cache semantics | IAM; `users_entitlements.csv`, `access_cache.csv` | AuthZ design | INJ-067 |
| P1 — blocks design | Unit/interface mapping authority | QC / integration; LIMS contracts v1/v2, `interface_mappings.csv` | Batch workflow | INJ-024 |
| P1 | Protocol version authority per site/country | Clinical / RA; protocol CSVs | Clinical-linked evidence | INJ-013 |
| P1 | Human review hours actually spent on packs | Quality / PV / Supply leads; staff_rates exist | FinOps / ROI | cost_model zeros review |
| P2 — blocks production claims | Clean LF integrity verification of package | Facilitator or LF checkout | Package trust narrative | A-001 |
| P2 | Subgroup language performance baselines | PV / model eval | Multilingual gates | INJ-072 |
| P2 | Accessibility audit of any UI | HF / QA | Adoption | INJ-073 |

**None of the above may be invented as facts.** Until acquired, keep narrative class `hypothesis`.
