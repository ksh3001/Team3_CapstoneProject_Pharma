from src.app_api import dispatch


def test_ac060_063_evaluate_gates():
    code, resp = dispatch(
        "/v1/evaluate/run",
        {
            "request_id": "eval-run-1",
            "suite": "contracts",
            "fixture_ids": ["PUB-01"],
            "user": "qp_eu_1",
            "purpose": "evaluate",
            "as_of": "2026-08-06T00:00:00Z",
            "idempotency_key": "eval-key-0001",
        },
    )
    assert code == 200
    assert "results" in resp
    assert all("fixture_id" in r and "gate" in r for r in resp["results"])
    assert isinstance(resp["ready_blocked"], bool)
    # hard controls should pass on this package
    assert all(r["gate"] == "pass" for r in resp["results"])
    assert resp["ready_blocked"] is False


def test_ac062_authz_deny_no_pack():
    code, body = dispatch(
        "/v1/workflows/batch_evidence",
        {
            "request_id": "eval-deny-pack",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": "2026-08-06T00:00:00Z",
            "user": "contractor_77",
            "mode": "deterministic_offline",
            "idempotency_key": "eval-deny-key",
        },
    )
    assert code == 403
    assert "readiness_state" not in body.get("error", {})
