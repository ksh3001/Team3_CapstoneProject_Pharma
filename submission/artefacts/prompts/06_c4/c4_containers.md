# C4 Level 2 — Containers

| Field | Entry |
|---|---|
| Artifact status | **provisional** |
| Deploy shape | Minimum: local/offline runnable units — no multi-region agent fabric |

## Narrative

Assessed POC uses a small set of containers: a **Demo UI**, a **Workflow API / CLI runtime**, a **Rules & Gate engine**, an **Evidence store** (local), optional **Model adapter** (disabled by default), and **read-only connectors** to challenge data. Side-effecting execution adapters are **not deployed** in assessed mode.

## Container diagram

```plantuml
@startuml
rectangle "Reviewer / Planner / Intake\n(browser or CLI user)" <<Person>> as User

rectangle "Demo UI\n(static or thin web)" <<Container>> as UI
rectangle "Workflow Runtime\n(API + CLI)\nPython 3.10+" <<Container>> as Runtime
rectangle "Rules & Gate Engine\n(deterministic)" <<Container>> as Rules
rectangle "Evidence & Audit Store\n(local files/DB)" <<Container>> as Store
rectangle "Model Adapter\n(optional, off)" <<Container>> as ModelAd
rectangle "Read Connectors + ACL\n(challenge data)" <<Container>> as Conn

rectangle "Challenge / SoR extracts\n(data, knowledge)" <<External>> as Data
rectangle "Optional LLM endpoint" <<External>> as LLM
rectangle "Execution systems\n(MES/WMS/Safety write APIs)" <<External>> as Exec

User --> UI : interact
User --> Runtime : CLI scripts
UI --> Runtime : request workflows
Runtime --> Rules : validate / POL-* / gates
Runtime --> Conn : fetch evidence
Runtime --> Store : write audit + packs (local)
Runtime ..> ModelAd : optional summarize
ModelAd ..> LLM : inference (disabled default)
Conn --> Data : read-only

Runtime -[#red,dashed]-> Exec : PROHIBITED: operational write-back (assessed mode)
Rules -[#red,dashed]-> Exec : PROHIBITED: mutate inventory / disposition
@enduml
```

## Container responsibilities

| Container | Responsibility | BC mapping | FR-IDs |
|---|---|---|---|
| Demo UI | Present packs/options; show deny/quarantine; no silent green “released” | HITL surface | FR-003/004/005 UX |
| Workflow Runtime | Orchestrate minimum governed workflow; modes offline/AI-disabled | All core | FR-001–007 |
| Rules & Gate Engine | AuthZ, doc trust, unit conflict, schemas, release gates | BC-AUTHZ, DOCAPPLY, MEASURE + invariants | FR-001,002,007 + POL in 003–005 |
| Evidence & Audit Store | Persist packs, citations, gates, idempotency keys locally | Shared kernel audit | all |
| Read Connectors + ACL | Translate SoR/CSV language → domain Evidence Items | ACL | FR-003/004/005 |
| Model Adapter | Optional narrator only | Gen AI boundary | optional path of FR-003/004/005; FR-006 off |

## Mapping notes

- No separate “agent swarm” container in provisional map.  
- Evaluation runner may be the same Runtime with `evaluate` entrypoint (FR-007).
