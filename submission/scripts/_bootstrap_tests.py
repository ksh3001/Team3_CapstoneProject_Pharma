"""Generate AC-linked tests for Prompt 11."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST = ROOT / "tests"


def w(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.lstrip("\n"), encoding="utf-8")


def main() -> None:
    w(
        TEST / "conftest.py",
        '''
import sys
from pathlib import Path

SUBMISSION = Path(__file__).resolve().parents[1]
if str(SUBMISSION) not in sys.path:
    sys.path.insert(0, str(SUBMISSION))
''',
    )
    w(
        TEST / "test_ac_authz.py",
        '''
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
''',
    )
    w(
        TEST / "test_ac_documents.py",
        '''
from src.docs.applicability import applicable_documents


def test_ac010_k998_k999_quarantined():
    docs = {d["doc_id"]: d for d in applicable_documents()}
    for doc_id in ("K-998", "K-999"):
        assert docs[doc_id]["instruction_applicable"] is False
        assert docs[doc_id]["quarantined"] is True


def test_ac011_k006_yes_k007_no():
    docs = {d["doc_id"]: d for d in applicable_documents()}
    assert docs["K-006"]["instruction_applicable"] is True
    assert docs["K-007"]["instruction_applicable"] is False


def test_ac012_k026_draft_not_instruction():
    docs = {d["doc_id"]: d for d in applicable_documents()}
    assert docs["K-026"]["instruction_applicable"] is False
    assert docs["K-026"]["status"] == "draft"
''',
    )
    w(
        TEST / "test_ac_batch.py",
        '''
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
''',
    )
    w(
        TEST / "test_ac_pv.py",
        '''
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
''',
    )
    w(
        TEST / "test_ac_supply.py",
        '''
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
''',
    )
    w(
        TEST / "test_ac_continuity.py",
        '''
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
''',
    )
    w(
        TEST / "test_ac_evaluate.py",
        '''
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
''',
    )
    w(
        TEST / "test_foundation.py",
        '''
from src.contracts.validate import validate_schema
from src.evidence.csv_acl import ChallengeWriteError, forbid_write
from src.paths import DATA
from src.runtime.context import error_envelope
from src.runtime.metrics import MetricsCollector
import pytest


def test_error_envelope_no_stack():
    env = error_envelope("x", "y", "rid")
    assert "traceback" not in str(env).lower()
    assert env["error"]["request_id"] == "rid"


def test_metrics_emit(tmp_path=None):
    m = MetricsCollector()
    ev = m.start("t", "req-m1", "batch_evidence")
    path = m.emit(ev)
    assert path.exists()


def test_forbid_challenge_write():
    with pytest.raises(ChallengeWriteError):
        forbid_write(DATA / "inventory.csv")
''',
    )
    # continuity stub + review hours
    w(
        ROOT / "artefacts" / "11_build" / "continuity_drill_checklist_stub.md",
        """# Continuity Drill Checklist Stub (AC-052)

Status: **scaffolded** — full drill evidence deferred to Phase 7 runbooks (AMB-CONT-01).

| Requirement (from package continuity CSV) | POC stub | Drill evidence |
|---|---|---|
| Batch/supply manual path operable without AI | Deterministic workflows + `ai_disabled` mode | Pending |
| PV without inference (`max_ai_outage_hours=0`) | LLM port no-op; narrator refused | Pending |
| 14-day batch/supply continuity | Not executed in Prompt 11 | Pending Phase 7 |

Risk if claimed complete now: false assurance on AC-052.
""",
    )
    w(
        ROOT / "evidence" / "review_hours_log_template.csv",
        "date,role,hours,rate_usd_ref,workflow,assumption_label,notes\n"
        "2026-08-06,Quality,0,92,batch_evidence,estimated_not_measured,template only\n",
    )
    print("tests ok")


if __name__ == "__main__":
    main()
