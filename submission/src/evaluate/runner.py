from __future__ import annotations
import json
from typing import Any
from src.authz.service import check_authorization
from src.contracts.validate import PROHIBITED_BATCH_KEYS, PROHIBITED_SUPPLY_KEYS, assert_no_prohibited, validate_schema
from src.paths import AUDIT_DIR, METRICS_DIR
from src.runtime.context import RequestContext, error_envelope
from src.workflows.batch import run_batch_evidence
from src.workflows.supply import run_supply_options


def run_evaluate(req: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    request_id = req.get("request_id") or "eval-missing"
    user = req.get("user") or ""
    purpose = req.get("purpose") or "evaluate"
    as_of = req.get("as_of") or RequestContext.utc_now()
    suite = req.get("suite") or "contracts"
    auth = check_authorization(user, purpose, "evaluation_run", request_id, as_of)
    if auth["decision"] != "allow":
        return 403, error_envelope("authz_denied", auth.get("reason", "deny"), request_id)

    results = []
    ready_blocked = False

    # Gate: authz revoke+cache
    denied = check_authorization("contractor_77", "batch_evidence", "batch", "NCB204-B24071", as_of)
    gate = "pass" if denied["decision"] == "deny" else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "AUTHZ-contractor_77",
            "gate": gate,
            "ac_ids": ["AC-001", "AC-062"],
            "evidence_path": str(AUDIT_DIR.relative_to(AUDIT_DIR.parents[1]) / f"authz_contractor_77_batch_evidence_NCB204-B24071.json"),
            "reason_codes": [denied.get("reason", "")],
        }
    )

    # Gate: batch happy path schema + no disposition + LR-88 conflict
    code, batch = run_batch_evidence(
        {
            "request_id": f"{request_id}-batch",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": as_of,
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "evaluate-batch-01",
        }
    )
    batch_ok = code == 200 and batch.get("execution_status") == "not_executed"
    unit_conflict = any(c.get("type") == "unit_conflict" for c in batch.get("contradictions", []))
    no_disp = not assert_no_prohibited(batch, PROHIBITED_BATCH_KEYS) if code == 200 else False
    schema_errs = validate_schema(batch, "batch_response.schema.json") if code == 200 else ["http_not_200"]
    gate = "pass" if batch_ok and unit_conflict and no_disp and not schema_errs else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "BATCH-LR-88",
            "gate": gate,
            "ac_ids": ["AC-020", "AC-021", "AC-022", "AC-060"],
            "evidence_path": f"working/audit/batch_{request_id}-batch.json",
            "reason_codes": [] if gate == "pass" else schema_errs[:3] or ["batch_gate_fail"],
        }
    )

    # Prohibited batch shape must be rejected
    pcode, _ = run_batch_evidence(
        {
            "request_id": f"{request_id}-bad",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": as_of,
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "evaluate-batch-bad",
            "batch_disposition": "release",
        }
    )
    gate = "pass" if pcode == 422 else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "BATCH-prohibited-disposition",
            "gate": gate,
            "ac_ids": ["AC-023", "AC-060"],
            "evidence_path": "n/a",
            "reason_codes": [str(pcode)],
        }
    )

    # Supply side effects
    scode, supply = run_supply_options(
        {
            "request_id": f"{request_id}-supply",
            "purpose": "supply_options",
            "as_of": as_of,
            "user": "qp_eu_1",
            "event_id": "SE-001",
            "mode": "deterministic_offline",
            "idempotency_key": "evaluate-supply-01",
        }
    )
    supply_ok = (
        scode == 200
        and supply.get("no_side_effects") is True
        and supply.get("execution_status") == "not_executed"
        and not assert_no_prohibited(supply, PROHIBITED_SUPPLY_KEYS)
        and not any((o.get("quality_status") or "").lower() == "quarantine" for o in supply.get("options", []))
    )
    gate = "pass" if supply_ok else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "SUPPLY-no-side-effects",
            "gate": gate,
            "ac_ids": ["AC-040", "AC-041", "AC-042", "AC-061"],
            "evidence_path": f"working/audit/supply_{request_id}-supply.json",
            "reason_codes": [] if gate == "pass" else ["supply_gate_fail"],
        }
    )

    rcode, _ = run_supply_options(
        {
            "request_id": f"{request_id}-reserve",
            "purpose": "supply_options",
            "as_of": as_of,
            "user": "qp_eu_1",
            "event_id": "SE-001",
            "mode": "deterministic_offline",
            "idempotency_key": "evaluate-supply-bad",
            "create_reservation": True,
        }
    )
    gate = "pass" if rcode in {409, 422} else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "SUPPLY-reservation-blocked",
            "gate": gate,
            "ac_ids": ["AC-043", "AC-061"],
            "evidence_path": "n/a",
            "reason_codes": [str(rcode)],
        }
    )

    resp = {
        "run_id": request_id,
        "suite": suite,
        "results": results,
        "ready_blocked": ready_blocked,
        "audit": {"evaluated_at": RequestContext.utc_now(), "user": user},
    }
    (METRICS_DIR / f"evaluate_{request_id}.json").write_text(json.dumps(resp, indent=2), encoding="utf-8")
    return 200, resp
