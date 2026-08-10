# False Positive / False Negative Examples (POC)

Concrete fixture-linked examples — not generic quality claims.

## False positives prevented (would have been unsafe “accept”)

| Example | Wrong accept would mean | System behavior | AC |
|---|---|---|---|
| `contractor_77` with active cache | Unauthorized pack/options | AuthZ **deny**; workflow 403 | AC-001 |
| LR-88 mg/L vs ug/mL spec | Silent within-spec / ready | Conflict dual-cite; `conflicted_evidence` | AC-020, AC-022 |
| K-998 / K-999 as instructions | Prompt-injection / fake PV rule | Not `instruction_applicable`; quarantined | AC-010, AC-033 |
| Quarantine inventory as available | Overstated supply | Excluded from options; in `quality_holds` | AC-040 |
| `batch_disposition=release` in request | Disposition automation | **422** prohibited | AC-023 |
| `create_reservation=true` | Side-effect execution | **409** side_effect_blocked | AC-043 |
| Fuzzy score 0.93 (PV-1001/PV-1014) auto-merge | Irreversible case merge | `auto_merged=false`; manual review | AC-031 |

## False negatives / residual miss risk (accepted or deferred)

| Example | Miss risk | Handling | Status |
|---|---|---|---|
| Strong_key-only duplicate detect | True duplicates with date/product drift may not cluster | HITL `duplicate_manual_assessment` when fuzzy CSV overlap requested | Accepted until AMB-PV-01 |
| Non-English narrative quality | Extraction errors not scored | Always `multilingual_review` | Assumed AMB-PV-02; metric Unknown |
| Genealogy / EM / sterility gaps not in LR-88 pack | Incomplete conflict coverage | AMB-BATCH-01 interim list only | Residual |
| Ops cycle-time improvement | Cannot prove waste removal magnitude | Measure emit only | `inconclusive (data scarcity)` |
