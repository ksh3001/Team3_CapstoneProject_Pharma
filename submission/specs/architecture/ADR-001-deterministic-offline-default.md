# ADR-001 — Deterministic offline runtime as assessed default

| Field | Entry |
|---|---|
| Status | **accepted** (POC assessed mode) |
| Date | 2026-08-06 |
| Owners | Architecture / Build; Reliability |
| Related BC | Shared continuity; all core |
| C4 | Workflow Runtime; Mode Controller; Model Adapter off-path |
| FR | FR-006 |

## Evidence basis

- **Fact:** Package is offline-capable; continuity requires manual paths (`continuity_requirements.csv`; PACKAGE_SCOPE).
- **Fact:** FR-006 / BR-050 assessed default must not require live inference.
- **Derivation:** Cloud-first agent platform would violate assessed offline gate.

## Context

Forces: board speed pressure vs hard requirement to run fixtures and defence without cloud keys; ransomware/outage injects (INJ-069/079).

## Decision

Assessed POC default is a **deterministic offline Workflow Runtime**. Optional model calls are non-default.

## Alternatives considered

1. Cloud-first multi-agent platform — rejected: fails offline/continuity and provisional minimum map.  
2. Hybrid always-online with offline fallback — deferred: more complexity than POC needs.  
3. Deterministic offline default — **chosen**.

## Drivers

Offline package constraint; FR-006; Measure-first hypothesis; reduce token/Waiting on LLM.

## Consequences

- Easier: reproducible tests, clean-room defence.  
- Harder: narrative quality without LLM.  
- Riskier: under-selling “AI” to sponsors — mitigated by honest PoC vs production labeling.

## Guardrails

- POL / BR-050–052; no assessed path hard-dependency on LLM.  
- PROHIBITED write paths remain absent by construction.

## NFRs (POC)

- Pack build without model: complete on local machine; p95 target **Unknown** (instrument in Phase 6) — must not hang on network.  
- AI-disabled drill: completable per continuity CSV.

## Security / privacy

Reduces exfiltration surface of live prompts; purpose still enforced.

## Operational impact

Rollback = disable Model Adapter (already off). Monitor: mode flag, inference attempt count (=0 in assessed).

## Validation

- AC-050–052; PUB-10-class outage fixtures; kill-switch test.

## Revisit triggers

- When sponsor requires always-on model for production AND offline drill still passes; or when offline pack p95 > **30 min** on reference fixture set (quantified revisit).
