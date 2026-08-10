# Build Constraints from Lean (Prompts 10–13)

## Must-fix-before-build

| Item | Why | Owner cue |
|---|---|---|
| Structural reopen gate = `cleared` | Prompt 10 entry | This folder |
| No write-execution / disposition / PV-final / allocate APIs in task list | Overproduction + hard gates | Architecture |
| AMB-PV-01 fuzzy tasks **absent** or explicitly blocked | Prevent Extra processing / false accepts | PV / Specs |
| AuthZ IAM>cache and document quarantine in first vertical slice | Observed Defects | Security / FR-001–002 |
| Failing tests first for prohibited actions / side effects / authz | DoD; Measure controls | Evaluation |
| Instrumentation hooks for M-01–M-05 planned in same slice as features | Measure-first under hypothesis | Build |
| LLM default off; no assessed RAG mandatory | Token/Model waste | ADR-001/002 |
| Contracts `additionalProperties: false` + evaluation schemas | Defects / Integration | Prompt 08 |

## Fix-in-pilot

| Item | Why | When |
|---|---|---|
| Cycle-time proxy capture on fixture runs (M-01) | Unknown baseline | Prompt 11–12 |
| Review-hour logging template (M-06) | TCO honesty | Prompt 11–12 |
| HITL queue depth/age metrics | Waiting Control | Prompt 12 |
| Continuity drill + runbooks (M-07 / AC-052) | Continuity waste/risk | Phase 7 / Prompt 12 |
| Risk-route tuning for review queues | Human-review waste | After first queue data |
| Clock dictionary refinement beyond dual-cite | Extra processing | P1 backlog |
| Demo UI choice (C09) | Residual non-blocking | Prompt 11 |

## Accept-as-residual-risk

| Item | Residual | Why accepted for Prompt 10 |
|---|---|---|
| Narrative class remains `hypothesis` | Framing not decision-ready | P0 cycle-time still Missing |
| Architecture review `conditional` | Not full `pass` | Open issues residual; no write-plane request |
| CRLF verify_package FAIL (A-001) | Hash audit Partial | Do not rewrite challenge evidence |
| AI-EVIDENCE validation triple-state | No validated DSS claim | Explicit out of claims |
| Fuzzy matching disabled | Higher manual duplicate queue | Safer than guessed threshold |
| Board −14% not proven by POC | Enterprise CTQ deferred | Avoid wrong optimization |
| Multilingual always-HITL load | Review hours may rise | Assumed AMB-PV-02 until subgroup baselines |

## Prompt 10 task-order priorities (Lean)

1. Assumption / control tests (prohibited, side-effect, authz, schema).  
2. Waste removal already designed (cite/flag/quarantine/no-write).  
3. Measure instrumentation.  
4. Feature vertical slice FR-001→007.  
5. Defer narrator, fuzzy, agent/RAG scale.
