# C4 Level 3 — Components

| Field | Entry |
|---|---|
| Artifact status | **provisional** |
| Focus | Workflow Runtime + Rules engine internals |

## Component diagram (Workflow Runtime)

```plantuml
@startuml
package "Workflow Runtime" {
  rectangle "AuthZ Gateway\n(FR-001)" <<Container>> as AuthZ
  rectangle "Document Applicability\n(FR-002)" <<Container>> as DocApp
  rectangle "Batch Evidence Service\n(FR-003)" <<Container>> as Batch
  rectangle "PV Intake Service\n(FR-004)" <<Container>> as PV
  rectangle "Supply Options Service\n(FR-005)" <<Container>> as Supply
  rectangle "Mode Controller\n(FR-006 offline/AI-disabled)" <<Container>> as Mode
  rectangle "Evaluation / Gate Runner\n(FR-007)" <<Container>> as Gates
  rectangle "ACL Anti-Corruption\nAdapters" <<Container>> as ACL
  rectangle "Optional Narrator Port" <<Container>> as Narr
}

rectangle "Rules & Gate Engine" <<Container>> as Rules
rectangle "Evidence & Audit Store" <<Container>> as Store
rectangle "Challenge extracts" <<External>> as Data
rectangle "HITL Reviewer" <<Person>> as Human

AuthZ --> Rules : entitlement rules
DocApp --> Rules : trust/status rules
Batch --> AuthZ : must allow
PV --> AuthZ : must allow
Supply --> AuthZ : must allow
Batch --> DocApp
PV --> DocApp
Supply --> DocApp
Batch --> ACL
PV --> ACL
Supply --> ACL
ACL --> Data : read
Batch --> Rules : POL-NO-DISPOSITION / units
PV --> Rules : POL-NO-FINAL-PV / duplicates
Supply --> Rules : POL-NO-SIDE-EFFECTS
Batch --> Store : pack + audit
PV --> Store
Supply --> Store
Mode --> Narr : disable/enable
Narr ..> Batch : optional summary only
Gates --> Store : read packs
Gates --> Rules : hard gates
Human --> Batch : review conflicts
Human --> PV : review clocks/duplicates
Human --> Supply : take options to governance

Supply -[#red,dashed]-> Data : PROHIBITED: write reservation/allocation
Batch -[#red,dashed]-> Data : PROHIBITED: write disposition
@enduml
```

## Component ↔ BC ↔ FR

| Component | Bounded context | Features |
|---|---|---|
| AuthZ Gateway | BC-AUTHZ | FR-001 |
| Document Applicability | BC-DOCAPPLY | FR-002 |
| Batch Evidence Service | BC-BATCH | FR-003 |
| PV Intake Service | BC-PV | FR-004 |
| Supply Options Service | BC-SUPPLY | FR-005 |
| Mode Controller | Shared continuity | FR-006 |
| Evaluation / Gate Runner | BC-MEASURE | FR-007 |
| ACL Adapters | Supporting / shared | FR-003/004/005 inputs |
| Optional Narrator Port | Gen AI (non-owning) | optional assist only |

## Gen AI runtime sketch (structure only)

| Concern | Where it sits | Default |
|---|---|---|
| Retrieval | DocApp + ACL over approved docs / cited extracts | On (rules-filtered) |
| Model calls | Narrator Port via Model Adapter | **Off** |
| Tools | None with write side effects in assessed mode | Disabled |
| Human review | UI/CLI presentation of Conflicts, Abstentions, required_reviews | Required on high-risk |

ADR candidates justify off-by-default and no write tools (see `adr_candidates.md`).
