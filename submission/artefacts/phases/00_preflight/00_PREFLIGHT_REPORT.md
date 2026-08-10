# Phase 0 — Preflight Report

| Field | Value |
|---|---|
| Team | Team3 |
| Package | Project AEGIS-PHARMA (NovaCura / NTG) |
| As-of | 2026-08-06 |
| Runtime | Python 3.10+ / Windows 10 |
| Workspace | `submission/` only |

## Commands executed

| Command | Exit | Outcome |
|---|---:|---|
| `python run_capstone.py --check` | 1 | Deep verify FAIL (see integrity notes) |
| `python tools/verify_package.py` | 1 | Same FAIL as above |
| `python tools/test_contracts.py` | 0 | All 6 contract samples behaved as expected |
| `python tools/check_submission_structure.py --scaffold` | 0 | Scaffold directories present |
| `python starter/baseline_diagnostics.py` | 0 | Four starter clues only (not an assessment) |

## Package counts observed

- Injects: 84 (`data/injects.json`)
- CSV datasets: 143
- Knowledge docs: 32
- Templates: 30
- Public scenarios/fixtures: 15
- Packaged files walked by verifier: 370

## Contract test evidence

- `positive_batch.json` valid
- `positive_pv.json` valid
- `positive_supply.json` valid
- `negative_batch_prohibited.json` invalid (prohibited disposition rejected)
- `negative_pv_prohibited.json` invalid (final safety conclusion rejected)
- `negative_supply_side_effect.json` invalid (side effect rejected)

## Baseline diagnostics clues (starter only)

1. Stale entitlement cache
2. Model hash mismatch
3. Unapproved unit mapping
4. Untrusted knowledge present

These map to inject themes INJ-067, INJ-070, INJ-024, and INJ-065 / knowledge authority controls. They are starting clues, not a complete risk assessment.

## Integrity findings (recorded, not “fixed”)

1. **CRLF vs LF hash drift (environment).** Spot-check of `knowledge/AI_GXP_BOUNDARY.md`: SHA-256 of on-disk CRLF bytes mismatches `FILE_HASHES.csv`, but SHA-256 after normalizing CRLF→LF matches the published hash. Same pattern explains bulk “immutable hash mismatch” / “knowledge hash mismatch” / “fixture evidence mismatch” errors on this Windows checkout. Challenge prose was not rewritten; line endings differ from the hash corpus.
2. **Verifier walks `.git`.** Errors of the form `NUL byte in .git/...` are binary Git objects, not challenge evidence. Treated as verifier scope noise when the package is used inside a Git clone.
3. **Manifest / hash coverage mismatch.** Reported alongside the above; treated as consequential only after CRLF normalization is accounted for. Challenge folders remain read-only for Team3 work.
4. **Unresolved prose references under `prompts/` and some `.cursor/skills/`.** WARN-level references to participant-output filenames that do not exist yet; expected for a challenge-only package.

**Decision:** Proceed with Phase 1 using local challenge content as evidence of record, while treating published hashes as LF-normalized authority. Do not rewrite challenge files to “make verify green.” Record residual package-integrity risk in the assumptions log (A-001).

## Boundary confirmation (read)

- `START_HERE.md` — work only under `submission/`; three mandatory workflows; offline-capable.
- `PACKAGE_SCOPE_AND_ASSUMPTIONS.md` — immutable challenge areas; deliberate ambiguity must be preserved; LLM/KG not mandatory.
- `case/INTEGRATED_CASE.md` — NovaCura portfolio; workflows A/B/C; injects INJ-001…084 across D01–D13; hard fail-closed accountability.
- `DEFINITION_OF_DONE.md` — clean-room reproducibility; 30 artefacts; defence.
- Explorer available at `app/index.html` (offline browse of injects/evidence).

## Phase 0 exit status

| Criterion | Status |
|---|---|
| Preflight commands run and recorded | Met |
| Package integrity understood and residual risk logged | Met (verify not green on CRLF checkout) |
| Case / scope / DoD read | Met |
| Baseline diagnostics run as clue | Met |
| Submission scaffold present | Met |
| Team charter + working agreements | See `00_TEAM_CHARTER.md` |
| Assumptions / decision log seeded | See `00_ASSUMPTIONS_DECISION_LOG.md` |

Phase 0 complete for Team3 purposes. Unconditional “verify_package PASS” is deferred pending an LF-normalized integrity check or facilitator guidance; it does not block discovery work under `submission/`.
