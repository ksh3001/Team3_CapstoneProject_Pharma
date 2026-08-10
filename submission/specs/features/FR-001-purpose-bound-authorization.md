# FR-001 — Purpose-bound authorization

| Field | Entry |
|---|---|
| Feature ID | FR-001 |
| Name | Purpose-bound authorization |
| Owning context | BC-AUTHZ |
| Status | provisional |
| Matching/confidence | N/A (exact entitlement check) |

## Actors

- Requesting user (Quality reviewer, PV intake scientist, Supply planner, or other entitled role)
- IAM / entitlement source of truth
- System AuthorizationDecision emitter

## Preconditions

- Request names user, purpose, object (batch_id / case package / shortage event), and as_of.
- Entitlement records exist for evaluation (package: `users_entitlements`; cache must not override revoke).

## Happy path

1. Actor submits authorized workflow request with purpose and object.
2. System evaluates **Current Entitlement** using IAM authoritative state at check time.
3. System records AuthorizationDecision allow with checked_at.
4. Downstream feature may proceed.

## Exceptions / alternate paths

- IAM revoked (even if gateway cache active) → deny; stop workflow; emit audit reason.
- Purpose mismatch or missing purpose → deny.
- Object out of grant scope → deny.
- Entitlement SoT ambiguous → abstain/deny (fail closed); flag ambiguity AMB-AUTHZ-01.

## Business rules

- BR-001: When IAM state is revoked, AuthorizationDecision must be deny regardless of cache.
- BR-002: When purpose is missing or not allowed for the workflow, AuthorizationDecision must be deny.
- BR-003: Every allow or deny must record user, purpose, object, checked_at, and decision.

## Acceptance criteria

- AC-001: Given contractor_77 revoked in IAM with active cache, when any workflow is requested, then decision is deny and no pack/options are produced.
- AC-002: Given qp_eu_1 active with purpose batch_evidence and batch object in scope, when requested, then decision is allow.
- AC-003: Given allow/deny outcome, when audit is inspected, then user, purpose, checked_at, and decision are present.

## HITL / AI boundaries

- Rules only. AI must not grant entitlement. Human IAM admin clears denials.

## Out of scope

- Identity provider implementation; OAuth protocols; UI login screens; C4 components.

## Ambiguities

- AMB-AUTHZ-01: Exact field mapping of “object in scope” grants — Unknown until entitlement schema detailed (Prompt 08); fail closed if unclear.
- AMB-AUTHZ-02: Entitlement SoT policy IAM vs cache — Prompt 01 P0; until resolved BR-001 stands.
