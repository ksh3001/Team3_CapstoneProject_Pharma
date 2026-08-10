# Decision Index — Prompt 07

| ADR | Title | Status | C4 elements | DDD BC | Blocked on backlog? |
|---|---|---|---|---|---|
| ADR-001 | Deterministic offline default | accepted (POC) | Runtime; Mode Controller | Shared continuity | No |
| ADR-002 | LLM optional off by default | proposed | Model Adapter; Narrator Port | Gen AI boundary | Partially — review-hour/cycle baselines (P0/P1) before enable |
| ADR-003 | No write adapters assessed | accepted (POC) | PROHIBITED exec edges; SideEffectGuard | BC-SUPPLY/BATCH/PV | No |
| ADR-004 | IAM over cache | accepted (POC) | AuthZ Gateway | BC-AUTHZ | Related P0 entitlement SoT policy doc — decision stands on CSV facts |
| ADR-005 | Single Workflow Runtime POC | proposed | Workflow Runtime | All | No |
| ADR-006 | Local evidence/audit store | proposed | Evidence & Audit Store | Shared audit; MEASURE | No |
| ADR-007 | Duplicate matching fail-closed | accepted (POC) | PV Intake Service | BC-PV | AMB-PV-01 / golden set before fuzzy |
| ADR-008 | Per-source ACL adapters | proposed | Read Connectors + ACL | ACL supporting | P1 unit mapping authority strengthens adapters |
| ADR-009 | Multi-clock evidence | proposed | PV Intake; Evidence Items | BC-PV | **Yes — P1 clock dictionary** |
| ADR-010 | Decision audit snapshot | proposed | Store; all services | Shared audit | No |

## Candidate coverage (from `06_c4/adr_candidates.md`)

| Candidate | ADR |
|---|---|
| ADR-C01 | ADR-001 |
| ADR-C02 | ADR-002 |
| ADR-C03 | ADR-003 |
| ADR-C04 | ADR-004 |
| ADR-C05 | ADR-005 |
| ADR-C06 | ADR-006 |
| ADR-C07 | ADR-007 |
| ADR-C08 | ADR-008 |
| ADR-C09 Demo UI tech | Deferred — non-blocking; decide in Prompt 08/11 |
| ADR-C10 Gate in-process | Folded into ADR-005 (in-process Gates) |

## Sponsor / data-access flags (Prompt 13)

- Enable LLM in any assessed path (ADR-002)  
- Production write/execution plane (supersede ADR-003)  
- P0 cycle-time and review-hour access to upgrade hypothesis  
- P1 clock dictionary owners for ADR-009
