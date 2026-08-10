# Error Envelope and Security Controls

## Standard error JSON

```json
{
  "error": {
    "code": "string_snake_case",
    "message": "safe client message",
    "request_id": "uuid",
    "details": {}
  }
}
```

`details` must not include stack traces, file paths outside submission, secrets, or raw IAM tokens.

## Error codes (business → HTTP)

| error.code | HTTP | Meaning |
|---|---:|---|
| validation_failed | 400 | schema/request invalid |
| unauthorized_user | 401 | user missing |
| authz_denied | 403 | IAM/purpose deny |
| idempotency_conflict | 409 | key reuse different body |
| contract_violation | 422 | response/request breaks contract / prohibited field |
| side_effect_blocked | 409 | SideEffectGuard |
| mode_violation | 503 | attempted LLM in ai_disabled/assessed |
| not_found | 404 | unknown batch/case/event |
| internal_error | 500 | unexpected (logged server-side only) |

## Security controls

| Control | Rule |
|---|---|
| AuthZ | Every workflow entry calls IAM-authoritative check (ADR-004) |
| Injection | Document text never executed as tool/instruction (BR-013) |
| CORS | Localhost demo only; no `*` with credentials |
| Logging | Correlate via request_id; no PII beyond synthetic case ids in POC |
| Writes | No MES/WMS/Safety write clients linked (ADR-003) |
| Path traversal | Out paths confined under `submission/` |
| SSRF | No user-supplied URL fetch in assessed mode |

## Authentication note (POC)

Offline POC uses **trusted local invocation** + explicit `user` field checked against entitlement CSV — not enterprise SSO. Deployment implication: must not expose port unbound to localhost without real auth (NFR deployment).

## Mapping to AC/NFR

| Control | AC / NFR |
|---|---|
| authz_denied | AC-001, NFR-03 |
| contract_violation | AC-023, AC-043, NFR-04/05 |
| side_effect_blocked | AC-042, NFR-02 |
| mode_violation | AC-051, NFR-01 |
| error envelope present | NFR check in evaluate suite |
