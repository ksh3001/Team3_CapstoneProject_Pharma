from src.authz.service import check_authorization
from src.app_api import dispatch


def test_ac001_revoked_cached_denied():
    r = check_authorization(
        "contractor_77", "batch_evidence", "batch", "NCB204-B24071", "2026-08-06T00:00:00Z"
    )
    assert r["decision"] == "deny"
    assert "revoked" in r["reason"]
    assert r["user"] == "contractor_77"
    assert r["purpose"] == "batch_evidence"
    assert r["checked_at"]


def test_ac002_entitled_qp_allowed():
    r = check_authorization(
        "qp_eu_1", "batch_evidence", "batch", "NCB204-B24071", "2026-08-06T00:00:00Z"
    )
    assert r["decision"] == "allow"


def test_ac003_audit_fields_and_workflow_403():
    r = check_authorization(
        "contractor_77", "supply_options", "shortage_event", "SE-001", "2026-08-06T00:00:00Z"
    )
    for k in ("user", "purpose", "checked_at", "decision"):
        assert k in r
    code, body = dispatch(
        "/v1/workflows/batch_evidence",
        {
            "request_id": "t-authz-deny",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": "2026-08-06T00:00:00Z",
            "user": "contractor_77",
            "mode": "deterministic_offline",
            "idempotency_key": "authz-deny-key1",
        },
    )
    assert code == 403
