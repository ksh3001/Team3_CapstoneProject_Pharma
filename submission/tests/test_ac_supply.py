from src.app_api import dispatch
from src.workflows.supply import run_supply_options


def _req(**extra):
    base = {
        "request_id": "t-sup-1",
        "purpose": "supply_options",
        "as_of": "2026-08-06T00:00:00Z",
        "user": "qp_eu_1",
        "event_id": "SE-001",
        "mode": "deterministic_offline",
        "idempotency_key": "sup-key-0001",
    }
    base.update(extra)
    return base


def test_ac040_quarantine_not_available():
    code, resp = run_supply_options(_req())
    assert code == 200
    assert all((o.get("quality_status") or "").lower() != "quarantine" for o in resp["options"])
    assert resp["quality_holds"]


def test_ac041_042_no_side_effects_no_reservation():
    code, resp = run_supply_options(_req(request_id="t-sup-2", idempotency_key="sup-key-0002"))
    assert code == 200
    assert resp["no_side_effects"] is True
    assert resp["execution_status"] == "not_executed"
    assert "reservation_id" not in resp


def test_ac043_reservation_blocked():
    code, body = dispatch(
        "/v1/workflows/supply_options",
        _req(request_id="t-sup-bad", idempotency_key="sup-key-bad", create_reservation=True),
    )
    assert code in {409, 422}
