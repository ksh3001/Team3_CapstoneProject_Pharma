# Conflict Resolution Policy

| Field | Entry |
|---|---|
| Phase | 2 |
| Status | Binding for AEGIS POC |
| Related | POL-NO-SILENT-UNIT; ADR-007/008/009; inject register |

## Rules

1. **Never silently merge** conflicting identity, unit, time, authority, or material facts.  
2. **Dual-cite** both (or all) sides with source, authority, and timestamps/units preserved.  
3. **Abstain / block readiness** when a material conflict remains open (batch → not `ready_for_authorized_review`).  
4. **Escalate to HITL** with explicit `required_reviews` / human_review reasons.  
5. **No irreversible case merge**; duplicate = candidates only (fuzzy disabled).  
6. **No silent unit conversion**; unapproved interface mappings are conflicts.  
7. **Untrusted/draft/superseded documents** are not instructional authorities.  
8. **IAM revoke overrides cache** — treat stale allow as security conflict.

## Example triggers (package)

| Trigger | Example | Action |
|---|---|---|
| Unit ≠ spec | LR-88 | Conflict + dual-cite |
| Unapproved mapping | interface_mappings approved=no | Conflict |
| Clock disagreement | PV-1001 receipts vs awareness | Dual-cite + clock_resolution review |
| Genealogy / sterility / QP packet gaps | inject themes | Gap/conflict per extract |
| AuthZ revoke+cache | contractor_77 | Deny |
| Quarantine as available | inventory | Exclude; quality_hold |

## Non-goals

Software does **not** “resolve” regulated disagreements into a single truth for certification, reportability, or allocation.
