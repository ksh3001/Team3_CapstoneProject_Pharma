# Phase 0 — Preflight Report

| Field | Entry |
|---|---|
| Team | Team 3 |
| Date | 2026-08-07 |
| Runtime | Python 3.12.10 (Windows) |
| Repo root | `Team3_CapstoneProject_Pharma` |
| Package mode | Offline / challenge-only (Workshop-Ready v2) |
| Status | Phase 0 complete — ready for Phase 1 Discovery |

## 1. Commands executed

From repository root:

```text
python --version
python run_capstone.py --check
python tools/check_submission_structure.py --scaffold
python tools/test_contracts.py
python starter/baseline_diagnostics.py
python tools/verify_package.py
python tools/check_submission_structure.py --final
```

## 2. Results summary

| Check | Result | Interpretation |
|---|---|---|
| Python runtime | PASS (3.12.10 ≥ 3.10) | Meets package assumption |
| `check_submission_structure.py --scaffold` | **PASS** | Writable `submission/` scaffold present |
| `tools/test_contracts.py` | **PASS** (6/6) | Fail-closed workflow contracts executable |
| `starter/baseline_diagnostics.py` | 4 findings (intentional) | Brownfield clues only — not a full assessment |
| `run_capstone.py --check` / `verify_package.py` | FAIL (see §3) | Documented; not a blocker to start discovery |
| `check_submission_structure.py --final` | FAIL (expected) | Empty submission content until later phases |

### Contract test detail (all PASS)

- `positive_batch.json` expected valid — PASS
- `positive_pv.json` expected valid — PASS
- `positive_supply.json` expected valid — PASS
- `negative_batch_prohibited.json` expected invalid — PASS
- `negative_pv_prohibited.json` expected invalid — PASS
- `negative_supply_side_effect.json` expected invalid — PASS

### Baseline diagnostics (starter clue only)

1. stale entitlement cache
2. model hash mismatch
3. unapproved unit mapping
4. untrusted knowledge present

These align with disclosed injects (e.g. INJ-067, INJ-070, INJ-024, INJ-065) and must not be “cleaned” from challenge evidence.

## 3. `verify_package.py` failure classification

Failures observed fall into three buckets. **None are treated as packaging defects to repair in immutable challenge areas.**

### A. Git object scan noise (clone artefact)

Many `NUL byte in .git/objects/...` and pack-file findings. Caused by scanning the local `.git` directory; not challenge CSV/knowledge corruption. **Do not modify `.git` or challenge evidence to chase these.**

### B. Manifest / hash coverage drift

- `manifest total packaged-file count mismatch`
- `manifest file listing does not exactly match packaged files`
- `immutable hash coverage mismatch`

Expected once participant-writable content exists under `submission/` (and any local `.cursor` extensions). `FILE_HASHES.csv` intentionally excludes `submission/`. Original package `VALIDATION_REPORT.json` recorded PASS at 311 files; current verifier recount includes participant and local tooling paths.

### C. Unresolved prose references

Verifier flags paths mentioned in `submission/prompts/*.md` that point to artefacts not yet created (e.g. `submission/artefacts/01_BUSINESS_CASE.md`). **Expected until Phase 1+** copies templates into `submission/artefacts/`.

## 4. Orientation confirmation (boundaries understood)

| Topic | Source | Team stance |
|---|---|---|
| Writable zone | `PACKAGE_SCOPE_AND_ASSUMPTIONS.md` | All work under `submission/` only |
| Immutable evidence | `FILE_HASHES.csv` | Do not edit `case/`, `data/`, `knowledge/`, `templates/`, etc. |
| Mandatory workflows | `case/INTEGRATED_CASE.md` | Batch evidence, PV intake, supply options — all non-executing |
| Hard gates | `requirements/SCORING_MODEL.md` | No autonomous disposition / final PV / allocate / recall |
| Scoring | 180 points, 17 areas | Content quality separate from structural `--final` gate |
| Method prompts | `submission/prompts/` | Team prompts + `PROMPT_MAPPING.md`; package library untouched |
| Threat modeling | Package control #4 | Repo approach → artefact `16_THREAT_ABUSE_MODEL.md` |
| Offline | Scope pack | Deterministic / AI-disabled path required later |

## 5. Team method readiness

| Item | Status |
|---|---|
| Team prompts `01`–`13` under `submission/prompts/` | Present |
| `PROMPT_MAPPING.md` → artefacts | Present |
| Package `prompts/PROMPT_LIBRARY.md` | Unmodified (hashed) |
| Next prompt | `01_discovery.md` |

## 6. Phase 0 exit decision

| Criterion | Met? |
|---|---|
| Offline checks runnable | Yes (stdlib Python) |
| Scaffold valid | Yes |
| Workflow contracts proven fail-closed | Yes |
| Boundaries / scoring understood | Yes (this report + charter) |
| Assumptions log opened | Yes — see `team_charter_and_working_agreements.md` |
| Proceed to Phase 1 | **Yes** |

## 7. Residual Phase 0 risks

| Risk | Handling |
|---|---|
| `verify_package.py` remains FAIL in this clone | Accept for participant work; re-run on clean extract before defence; do not alter immutable hashes |
| `--final` FAIL | Expected until artefacts/code/evidence populated |
| Baseline diagnostics incomplete | Full inject mapping in Phase 1–2 |
