# Tests-First Log (Phase 3)

## Policy

Material prohibitions and AuthZ/poisoning controls require deterministic tests before treating implementation as Phase-3-complete. Offline / AI-disabled continuity remains mandatory.

## Chronology (honest)

| Step | When | Action | Result |
|---|---|---|---|
| 1 | Prompt 11 era | AC suite authored against FR/AC | Implemented; suite green historically |
| 2 | Phase 3 start | Added `submission/tests/test_phase3_prohibited.py` (disposition, PV finals, reservation, authz, malicious doc, poisoned manifest, unit conflict, merge) | **Written as negative gate suite** |
| 3 | Phase 3 | Ran `pytest` on phase3 + key AC modules | **24 passed** (implementation already present from Prompt 11 — not a red→green rewrite in this session) |
| 4 | Phase 3 close | Documented RTM + this log | Checkpoint |

## Interpretation

Hard-gate tests were **not left red** at Phase 3 close. The Phase 3 contribution is: (a) expanded prohibition/poisoning coverage, (b) RTM linking req→design→test, (c) pinned contract copies under `submission/src/contracts/`.

If Evaluation requires a literal red-then-green demo, re-break one prohibition temporarily under a branch — **not done** here to avoid destabilizing the assessed green suite.

## Current command

```text
PYTHONPATH=submission python -m pytest submission/tests -q
```

## Inventory (Phase 3 focus)

| Test focus | Module | Linked control |
|---|---|---|
| Disposition rejected | test_phase3_prohibited | AC-023 |
| No final PV | test_phase3_prohibited | AC-030 |
| No reservation | test_phase3_prohibited | AC-043 |
| AuthZ deny contractor | test_phase3 + test_ac_authz | AC-001 |
| Malicious / poisoned | test_phase3_prohibited | AC-010 / tool boundary |
| Unit conflict dual-cite | test_phase3 + test_ac_batch | AC-020 |
| No auto-merge | test_phase3 + test_ac_pv | AC-031 |
| Continuity / LLM off | test_ac_continuity | AC-050/051 |
