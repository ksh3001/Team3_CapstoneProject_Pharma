# State Transitions — AEGIS Evidence Assist (POC)

## 1. Runtime mode

```
deterministic_offline (default)
        | kill_switch / AI_DISABLED
        v
   ai_disabled
        | (admin clear + audit) 
        v
deterministic_offline
```

Illegal: `llm_enabled=true` in assessed suites without Mode Controller allow + audit (ADR-002). Assessed CI forces `llm_enabled=false`.

## 2. AuthorizationDecision

```
[request] -> check IAM
   |-- active + purpose ok -> allow
   |-- revoked OR purpose bad OR IAM unavailable -> deny (terminal for request)
```

No transition from deny→allow without new check after IAM change.

## 3. BatchEvidencePack readiness_state

| From | Trigger | To | Illegal |
|---|---|---|---|
| (new) | material gaps open, no blocking conflict | insufficient_evidence | — |
| (new) | blocking Conflict (e.g. unit) | conflicted_evidence | — |
| (new) | no blocking conflict/gap per AMB-BATCH-01 interim | ready_for_authorized_review | — |
| any | authz deny | (no pack) | emitting pack |
| any | add disposition field | rejected | storing disposition |
| ready_for_authorized_review | human certifies | **outside system** | system auto-certify |

`execution_status` always `not_executed` (const).

## 4. Duplicate candidate (PV)

```
no_link --exact/strong_key--> candidate_listed
candidate_listed --human merge outside--> (external SoR)
candidate_listed --fuzzy--> FORBIDDEN until threshold ADR
```

## 5. SupplyOptionSet

```
drafting -> issued (no_side_effects=true)
issued -> (external allocation) outside system
issued -> reservation_created  FORBIDDEN
```

## 6. Evaluation gate / ready claim

```
run -> gate_pass | gate_fail
gate_fail -> ready_blocked=true (terminal for ready claim)
gate_pass -> ready_blocked=false only if all hard gates pass
```

Illegal: mutate pack to force gate_pass (BR-061).
