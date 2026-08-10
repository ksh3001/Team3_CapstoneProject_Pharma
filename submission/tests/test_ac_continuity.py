from src.app_api import dispatch, health
from src.ports.llm import NoOpLLM, call_count, reset_call_count
from src.runtime.mode import RuntimeMode
from src.workflows.batch import run_batch_evidence


def test_ac050_model_down_deterministic():
    reset_call_count()
    mode = RuntimeMode.from_request("deterministic_offline")
    assert mode.allow_llm_call() is False
    code, resp = run_batch_evidence(
        {
            "request_id": "t-cont-1",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": "2026-08-06T00:00:00Z",
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "cont-key-0001",
        }
    )
    assert code == 200
    assert call_count() == 0


def test_ac051_ai_disabled_refuses_narrator():
    code, body = dispatch(
        "/v1/workflows/batch_evidence",
        {
            "request_id": "t-cont-narr",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": "2026-08-06T00:00:00Z",
            "user": "qp_eu_1",
            "mode": "ai_disabled",
            "narrator": True,
            "idempotency_key": "cont-key-narr",
        },
    )
    assert code == 503
    # rules path still works without narrator
    code2, resp = run_batch_evidence(
        {
            "request_id": "t-cont-rules",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": "2026-08-06T00:00:00Z",
            "user": "qp_eu_1",
            "mode": "ai_disabled",
            "idempotency_key": "cont-key-rules",
        }
    )
    assert code2 == 200


def test_health_llm_false():
    h = health()
    assert h["status"] == "ok"
    assert h["llm_enabled"] is False
