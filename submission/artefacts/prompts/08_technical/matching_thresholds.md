# Matching Thresholds

| Feature | Strategy order | Threshold | Rejection | Dedup |
|---|---|---|---|---|
| FR-003 batch_id | 1) exact equality | N/A (exact) | unknown batch → 404/gap | N/A |
| FR-004 duplicates | 1) exact case/worldwide id 2) strong_key equality (product + patient_key + event_date + AE_PT) | equality only | no candidate; optional manual review | multiple candidates OK; merge forbidden |
| FR-004 fuzzy | **disabled** | **open-blocked** (Unknown) | N/A | N/A |
| FR-004 multilingual | no auto score | **assumed** HITL always for non-English | do not drop narrative | N/A |

**Rule:** No guessed fuzzy number (e.g. 0.8) permitted in code until ADR updates this file with an evaluated threshold.
