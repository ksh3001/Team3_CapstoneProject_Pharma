# ADR-004 — IAM authoritative over gateway cache for AuthZ

| Field | Entry |
|---|---|
| Status | **accepted** (POC assessed mode) |
| Date | 2026-08-06 |
| Owners | Security / CISO; Architecture |
| Related BC | BC-AUTHZ |
| C4 | AuthZ Gateway |
| FR | FR-001 |

## Evidence basis

- **Fact:** `contractor_77` iam_state=revoked while ai_gateway_state=active_cached; cache until after revoke (`users_entitlements.csv`, `access_cache.csv`).
- **Fact:** BR-001 / POL-AUTHZ-IAM.

## Context

Forces: gateway latency cache vs Zero Trust stale entitlement (INJ-067).

## Decision

AuthorizationDecision uses **IAM state as source of truth**. Cache may accelerate allow-path only when IAM is active; **never** allow when IAM is revoked.

## Alternatives considered

1. Cache-first gateway — rejected (fails AC-001).  
2. Cache with short TTL only — insufficient alone without IAM check.  
3. IAM-authoritative — **chosen**.

## Drivers

Stale auth inject; hard gate on revoked entitlements.

## Consequences

- Easier: deterministic deny tests.  
- Harder: extra IAM read per request (POC local CSV ok).  
- Risk: IAM outage → fail closed (deny), may increase Waiting — acceptable.

## Guardrails

- BR-001–003; deny on IAM unavailable (fail closed).

## NFRs

- AuthZ check p95 **Unknown** (local file OK); availability: prefer deny over allow on IAM read failure = **100%** fail-closed.

## Security / privacy

Addresses stale authorization; least privilege.

## Operational impact

Alert on deny bursts; runbook: IAM restore. No cache-only hotfix without ADR revisit.

## Validation

- AC-001–003; PUB-09-class security fixtures.

## Revisit triggers

- When production IAM SLA p95 > **2 s** forcing design change AND compensating control approved; or any allow observed for revoked IAM (>**0**).
