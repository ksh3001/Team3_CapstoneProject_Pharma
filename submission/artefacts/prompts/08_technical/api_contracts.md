# API / Interface Contracts — AEGIS Evidence Assist (POC)

| Field | Entry |
|---|---|
| Prompt | `prompts/08_technical_design.md` |
| Skills | `spec-driven-delivery` |
| Entry | Architecture review **conditional** (`07_adrs/architecture_review.md`) |
| Status | provisional POC contracts |
| Base URL (local) | `http://127.0.0.1:8080` (or CLI equivalent) |
| Auth model | Purpose-bound check every call (ADR-004); no public internet OAuth required for offline POC |

**Schema authority:** Response bodies for workflows MUST validate against package schemas under `evaluation/contracts/` (participant copy may version under `submission/src/contracts/` later). `additionalProperties: false`.

**Idempotency:** Header `Idempotency-Key` (string, 8–128 chars) required on POST workflow endpoints. Replay with same key + same body hash returns prior response; different body → `409`.

**Common headers:** `X-Request-Id` (client or server UUID); `X-As-Of` ISO-8601 UTC; `X-User-Id`; `X-Purpose`.

---

## 1. POST /v1/authz/check — FR-001

**Purpose:** Explicit AuthorizationDecision (also invoked internally by workflow endpoints).

### Request

```json
{
  "user": "string minLength 1",
  "purpose": "batch_evidence | pv_intake | supply_options | evaluate",
  "object_type": "batch | case_package | shortage_event | evaluation_run",
  "object_id": "string minLength 1",
  "as_of": "ISO-8601 datetime UTC"
}
```

### Validation

- `purpose` enum as above only.  
- `as_of` must parse as UTC datetime.  
- IAM revoked ⇒ deny even if cache active.

### Success `200`

```json
{
  "decision": "allow | deny",
  "user": "...",
  "purpose": "...",
  "object_id": "...",
  "checked_at": "ISO-8601",
  "reason": "string"
}
```

### Errors

| Code | When |
|---|---|
| 400 | schema/validation fail |
| 401 | user missing |
| 403 | decision deny (also returned as 200 with deny for explicit check — **POC rule:** use **200** with `decision=deny` for check endpoint; workflow endpoints use **403**) |

---

## 2. POST /v1/workflows/batch_evidence — FR-003 (+ FR-002)

### Request

```json
{
  "request_id": "string minLength 1",
  "batch_id": "string minLength 1",
  "purpose": "batch_evidence",
  "as_of": "ISO-8601 UTC",
  "user": "string minLength 1",
  "mode": "deterministic_offline | ai_disabled",
  "idempotency_key": "string 8-128"
}
```

### Success `200`

Body MUST satisfy `evaluation/contracts/batch_response.schema.json` including:

- `workflow`: `"batch_evidence"`
- `execution_status`: `"not_executed"`
- `readiness_state`: `insufficient_evidence | conflicted_evidence | ready_for_authorized_review`
- `authorization.decision`: `allow`
- evidence/contradictions/gaps/abstentions/human_review/audit/applicable_documents present

**PROHIBITED properties (reject 422):** any of `batch_disposition`, `release`, `reject`, `recall`, `reprocess`, `relabel`, or disposition synonyms.

### Errors

| Code | When |
|---|---|
| 400 | invalid JSON / missing fields / bad as_of |
| 403 | authz deny |
| 409 | idempotency conflict |
| 422 | schema fail or prohibited fields / silent-conversion attempt |
| 503 | mode requires model but AI disabled (should not occur if mode deterministic) |

---

## 3. POST /v1/workflows/pv_intake — FR-004

### Request

```json
{
  "request_id": "string",
  "purpose": "pv_intake",
  "as_of": "ISO-8601 UTC",
  "user": "string",
  "case_ids": ["string", "..."],
  "source_package_ref": "string",
  "mode": "deterministic_offline | ai_disabled",
  "idempotency_key": "string 8-128"
}
```

### Success `200`

MUST satisfy `pv_response.schema.json`:

- `workflow`: `"pv_intake"`
- `execution_status`: `"not_executed"`
- includes `source_facts`, `duplicate_candidates`, `clock_evidence`, `terminology`, `listedness_context`, `required_reviews`

**PROHIBITED:** final seriousness/causality/expectedness/reportability/signal_confirmation fields.

### Duplicate emission rules

Per `matching_thresholds.md`: exact → strong_key only; fuzzy disabled (threshold open-blocked).

### Errors

Same family as batch: 400 / 403 / 409 / 422.

---

## 4. POST /v1/workflows/supply_options — FR-005

### Request

```json
{
  "request_id": "string",
  "purpose": "supply_options",
  "as_of": "ISO-8601 UTC",
  "user": "string",
  "event_id": "string",
  "mode": "deterministic_offline | ai_disabled",
  "idempotency_key": "string 8-128"
}
```

### Success `200`

MUST satisfy `supply_response.schema.json` with `no_side_effects: true`, `workflow: supply_options`, `execution_status: not_executed`.

**PROHIBITED:** reservation/allocation/shipment/quality_status_change/recall execution properties; any filesystem/DB write that creates reservations.

### Errors

400 / 403 / 409 / 422; plus **409** if SideEffectGuard detects attempted write.

---

## 5. POST /v1/evaluate/run — FR-007

### Request

```json
{
  "request_id": "string",
  "suite": "contracts | public_fixtures | adversarial | continuity",
  "fixture_ids": ["PUB-01", "..."],
  "user": "string",
  "purpose": "evaluate",
  "as_of": "ISO-8601 UTC",
  "idempotency_key": "string 8-128"
}
```

### Success `200`

```json
{
  "run_id": "string",
  "suite": "string",
  "results": [
    {
      "fixture_id": "string",
      "gate": "pass | fail",
      "ac_ids": ["AC-020"],
      "evidence_path": "relative/path",
      "reason_codes": ["string"]
    }
  ],
  "ready_blocked": true,
  "audit": {}
}
```

Hard gate fail ⇒ `ready_blocked: true` (boolean required).

---

## 6. GET /v1/health

### Success `200`

```json
{ "status": "ok", "mode": "deterministic_offline", "llm_enabled": false }
```

---

## 7. CLI parity (same contracts)

| Command | Maps to |
|---|---|
| `python -m aegis authz check ...` | POST /v1/authz/check |
| `python -m aegis run batch ...` | POST /v1/workflows/batch_evidence |
| `python -m aegis run pv ...` | POST /v1/workflows/pv_intake |
| `python -m aegis run supply ...` | POST /v1/workflows/supply_options |
| `python -m aegis evaluate ...` | POST /v1/evaluate/run |

CLI must emit the same JSON bodies to stdout or `--out` path.

---

## 8. Explicit non-endpoints (out of scope)

No APIs for: batch release, PV finalization, allocate/reserve/ship, model admin beyond mode flag, mutating challenge `data/`.
