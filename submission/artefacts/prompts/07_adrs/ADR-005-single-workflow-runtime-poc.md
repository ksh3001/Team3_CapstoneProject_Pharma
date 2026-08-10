# ADR-005 — Single Workflow Runtime container for POC

| Field | Entry |
|---|---|
| Status | **proposed** |
| Date | 2026-08-06 |
| Owners | Architecture / Build |
| Related BC | All |
| C4 | Workflow Runtime hosts services FR-001–007 |
| FR | all |

## Evidence basis

- **Assumption:** Minimal provisional map reduces integration waste for capstone.
- **Derivation:** C4 provisional forbids elaborate microservice/agent fabric.

## Context

Forces: clean separation vs delivery speed under hypothesis.

## Decision

Implement POC as **one Workflow Runtime** (API+CLI) hosting AuthZ, DocApp, Batch, PV, Supply, Mode, Gates components in-process (modules), plus Rules engine library. Not a mesh of independently deployed microservices.

## Alternatives considered

1. Microservice per BC — rejected for POC complexity/Overproduction.  
2. Serverless per feature — rejected offline.  
3. Single runtime — **chosen** for POC.

## Drivers

ADR-C05; dmaic transportation waste; offline.

## Consequences

- Easier: one setup/test/evaluate script.  
- Harder: later split needs modular boundaries now (package by component).  
- Risk: modularity erosion — mitigate with module_rules in Prompt 08.

## Guardrails

- Component package boundaries match C4 Level 3; no Supply module importing write SDKs.

## NFRs

- Single-process assessed run; deploy units for POC = **1** runtime (+ optional static UI).

## Security / privacy

Smaller attack surface; still enforce AuthZ before each workflow.

## Operational impact

Rollback = prior submission version. Monitor process health only at POC scale.

## Validation

- Import/architecture check: no execution SDK; scripts setup/run/test/evaluate/reset work.

## Revisit triggers

- When independent scaling needed (e.g. gate runner CPU > **70%** of runtime for >1 week in pilot) or team ownership split requires separate deployables.
