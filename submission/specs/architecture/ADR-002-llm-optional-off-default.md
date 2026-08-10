# ADR-002 — LLM optional behind port, off by default

| Field | Entry |
|---|---|
| Status | **proposed** (interim POC assumption: off) |
| Date | 2026-08-06 |
| Owners | Architecture; Product; GxP |
| Related BC | Gen AI boundary (non-owning) |
| C4 | Model Adapter; Optional Narrator Port |
| FR | optional paths on FR-003/004/005; FR-006 |

## Evidence basis

- **Fact:** Prompt 02 hypothesis Measure-first; genAI not sole lever (`no_ai_baselines.csv`).
- **Fact:** DDD gen_ai_boundaries — AI must never decide alone.
- **Assumption:** Narrator adds limited value until authority filters + bias controls measured.

## Context

Forces: desire for generative summaries vs automation bias (INJ-071), token cost (cost_model), poisoned retrieval (K-998).

## Decision

Any LLM is accessed only via **Narrator Port / Model Adapter**, **disabled by default** in assessed mode. When enabled, may summarize already-cited Conflicts only — no new facts, no disposition language.

## Alternatives considered

1. Always-on RAG agent — rejected for assessed mode.  
2. No LLM port at all — viable; kept port for future substitution (exit).  
3. Optional port off-by-default — **chosen**.

## Drivers

Hypothesis framing; POL-DOC-TRUST; FinOps honesty; substitution/exit.

## Consequences

- Easier: hard gates stay deterministic.  
- Harder: UX less “smart.”  
- Risk: port later abused — guard with Mode Controller.

## Guardrails

- POL-NO-DISPOSITION / POL-NO-FINAL-PV; BR-013 retrieval is data not commands.  
- Enabling LLM requires Mode Controller allow + audit of model/prompt versions.

## NFRs

- Default inference attempts in assessed suite = **0**.  
- If enabled in a non-assessed demo: budget **Unknown** until FinOps artefact — hard stop on denial-of-wallet patterns (INJ-076) TBD numeric in Prompt 08/23.

## Security / privacy

Prompt-injection containment: untrusted docs never tools; purpose limitation on retrieval.

## Operational impact

Kill switch disables port. Monitor: inference count, token use, enablement flag.

## Validation

- AC-051; red-team poisoned doc; schema reject if narrator injects disposition fields.

## Revisit triggers

- When dual-cite accuracy and review-hour baselines exist AND narrator A/B shows ≥**20%** reduction in median review time without increasing false-ready rate; or when token cost / successful task exceeds agreed FinOps cap (cap TBD Prompt 23).
