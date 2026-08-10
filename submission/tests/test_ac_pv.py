from src.workflows.pv import run_pv_intake


def _req(**extra):
    base = {
        "request_id": "t-pv-1",
        "purpose": "pv_intake",
        "as_of": "2026-08-06T00:00:00Z",
        "user": "qp_eu_1",
        "case_ids": ["PV-1001"],
        "mode": "deterministic_offline",
        "idempotency_key": "pv-key-0001",
    }
    base.update(extra)
    return base


def test_ac030_no_final_pv_fields():
    code, resp = run_pv_intake(_req())
    assert code == 200
    for k in ("seriousness", "causality", "expectedness", "reportability", "signal_confirmation"):
        assert k not in resp


def test_ac031_no_fuzzy_auto_merge():
    code, resp = run_pv_intake(
        _req(request_id="t-pv-dup", case_ids=["PV-1001", "PV-1014"], idempotency_key="pv-key-dup")
    )
    assert code == 200
    for c in resp["duplicate_candidates"]:
        assert c.get("auto_merged") is False
    assert "duplicate_manual_assessment" in resp["required_reviews"]


def test_ac032_dual_clocks_review():
    code, resp = run_pv_intake(_req(request_id="t-pv-clock", idempotency_key="pv-key-clock"))
    assert code == 200
    assert len(resp["clock_evidence"]) >= 2
    assert any(c.get("type") == "clock_disagreement" for c in resp["contradictions"])
    assert "clock_resolution" in resp["required_reviews"]


def test_ac033_k999_not_reportability_authority():
    code, resp = run_pv_intake(_req(request_id="t-pv-k999", idempotency_key="pv-key-k999"))
    assert code == 200
    k999 = [x for x in resp["listedness_context"] if x.get("doc_id") == "K-999"]
    assert k999 and k999[0].get("reportability_authority") is False
