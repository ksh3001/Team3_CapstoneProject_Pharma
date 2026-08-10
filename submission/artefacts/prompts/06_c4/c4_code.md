# C4 Level 4 — Code (riskiest paths only)

| Field | Entry |
|---|---|
| Artifact status | **provisional** |
| Depth | Interfaces only — no full module tree |

## Why Level 4 here

Highest hard-gate risk: authZ bypass, silent unit conversion, supply side effects, disposition leakage.

```plantuml
@startuml
rectangle "AuthorizationPort\ncheck(user, purpose, object, as_of) -> Allow|Deny" as AuthPort
rectangle "EvidencePackBuilder\nbuild_batch(...) -> BatchEvidencePack" as BatchB
rectangle "UnitConflictDetector\ndetect(value, unit, spec) -> Conflict?" as Units
rectangle "SupplyOptionsBuilder\nbuild(...) -> SupplyOptionSet" as SupB
rectangle "SideEffectGuard\nassert_no_writes()" as Guard
rectangle "SchemaValidator\nvalidate(pack, schema) -> OK|Fail" as Schema

AuthPort --> BatchB : require Allow
AuthPort --> SupB : require Allow
BatchB --> Units
BatchB --> Schema
SupB --> Guard
SupB --> Schema
Guard -[#red,dashed]-> SupB : PROHIBITED: reservation/allocation writes
@enduml
```

## Proposed module names (submission layout intent — not implementing here)

| Module | Role |
|---|---|
| `submission/src/authz/` | AuthorizationPort |
| `submission/src/evidence/` | ACL loaders, Evidence Items |
| `submission/src/workflows/batch.py` | BatchEvidencePack |
| `submission/src/workflows/pv.py` | PvIntakePacket |
| `submission/src/workflows/supply.py` | SupplyOptionSet + SideEffectGuard |
| `submission/src/contracts/` | SchemaValidator |
| `submission/src/runtime/mode.py` | Mode Controller |
| `submission/src/ports/llm.py` | Narrator Port (no-op default) |

Exact APIs deferred to Prompt 08.
