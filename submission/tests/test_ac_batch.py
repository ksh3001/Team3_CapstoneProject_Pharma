from src.app_api import dispatch
from src.workflows.batch import run_batch_evidence


def _req(**extra):
    base = {
        "request_id": "t-batch-1",
        "batch_id": "NCB204-B24071",
        "purpose": "batch_evidence",
        "as_of": "2026-08-06T00:00:00Z",
        "user": "qp_eu_1",
        "mode": "deterministic_offline",
        "idempotency_key": "batch-key-0001",
    }
    base.update(extra)
    return base


def test_ac020_unit_conflict_lr88():
    code, resp = run_batch_evidence(_req(request_id="t-batch-lr88", idempotency_key="batch-key-lr88"))
    assert code == 200
    assert any(c.get("type") == "unit_conflict" for c in resp["contradictions"])
    assert all(c.get("silent_conversion") is False for c in resp["contradictions"] if c.get("type") == "unit_conflict")


def test_ac021_not_executed_no_disposition():
    code, resp = run_batch_evidence(_req(request_id="t-batch-exec", idempotency_key="batch-key-exec"))
    assert code == 200
    assert resp["execution_status"] == "not_executed"
    for k in ("batch_disposition", "release", "reject", "recall"):
        assert k not in resp


def test_ac022_conflicted_not_ready():
    code, resp = run_batch_evidence(_req(request_id="t-batch-ready", idempotency_key="batch-key-ready"))
    assert code == 200
    assert resp["readiness_state"] == "conflicted_evidence"


def test_ac023_prohibited_disposition_rejected():
    code, body = dispatch(
        "/v1/workflows/batch_evidence",
        _req(request_id="t-batch-bad", idempotency_key="batch-key-bad", batch_disposition="release"),
    )
    assert code == 422
