# Stage 3 — Contract Test Results

| Field | Entry |
|---|---|
| Date | 2026-08-07 |
| Command | `python tools/test_contracts.py` |
| Workshop stage | 3 — Architecture and controls |
| Related artefacts | 11_ADR_REGISTER (§4), 12_INTEGRATION_CONTRACTS (§7) |

## Results

| Sample | Schema | Expected | Result |
|---|---|---|---|
| positive_batch.json | batch_response.schema.json | valid | **PASS** |
| positive_pv.json | pv_response.schema.json | valid | **PASS** |
| positive_supply.json | supply_response.schema.json | valid | **PASS** |
| negative_batch_prohibited.json | batch_response.schema.json | invalid | **PASS** |
| negative_pv_prohibited.json | pv_response.schema.json | invalid | **PASS** |
| negative_supply_side_effect.json | supply_response.schema.json | invalid | **PASS** |

**Suite result: 6/6 PASS**

## Interpretation

Fail-closed workflow contracts are executable and prohibit disposition / final PV / supply side-effect shapes at the schema boundary. This satisfies Stage 3 exit “contract tests” and Checkpoint C3 prohibited-action contract review for package samples.

Remaining (later stages): inject-level tests (AC-003, AC-008–011), PUB fixtures end-to-end, and PUB-09–15 participant-defined contracts.
