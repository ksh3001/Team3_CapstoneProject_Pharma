# Live Failure Demonstrations (Phase 8)

## How to run

```bash
PYTHONPATH=submission python submission/scripts/run_defence_failure_demos.py
```

Or via tests: `PYTHONPATH=submission python -m pytest submission/tests/test_phase8_defence.py -q`

Results: [`failure_demo_results.csv`](failure_demo_results.csv)

## Demo script for the panel (≈8 minutes)

| # | Say | Show | Expect |
|---|---|---|---|
| D1 | “Revoked contractor still cached — system must deny.” | contractor_77 batch request | **403** |
| D2 | “We never accept disposition from the assist.” | `batch_disposition=release` | **422** |
| D3 | “Supply cannot reserve inventory.” | `create_reservation=true` | **409** |
| D4 | “AI kill switch — narrator off.” | `mode=ai_disabled` + narrator | **503** |
| D5 | “Entitled user still gets an assist pack — not a release.” | qp_eu_1 batch | **200** `not_executed`, conflicts visible |
| D6 | “PV packet has no finals; no auto-merge.” | PV-1001/1014 | **200**; finals absent |
| D7 | “Evaluate hard gates.” | `/v1/evaluate/run` | `ready_blocked=false` |
| D8 | “Supply options attest no side effects.” | SE-001 | `no_side_effects=true` |

## Closing line

“These failures are the product. The assist works *because* it stops. Production remains no-go until Measure closes the Unknowns.”
