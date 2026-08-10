"""Phase 6: PUB fixture integrity, mapped smoke runs, evaluate + outage gates."""
from __future__ import annotations

import csv
import json
from pathlib import Path

from src.app_api import dispatch
from src.contracts.validate import validate_schema
from src.ports.llm import call_count, reset_call_count
from src.workflows.batch import run_batch_evidence
from src.workflows.pv import run_pv_intake
from src.workflows.supply import run_supply_options


def _assert_schema(schema_file: str, resp: dict) -> None:
    errors = validate_schema(resp, schema_file)
    assert not errors, errors

ROOT = Path(__file__).resolve().parents[2]
PUB_DIR = ROOT / "evaluation" / "public_fixtures"
PHASE6 = (
    Path(__file__).resolve().parents[1]
    / "artefacts"
    / "phases"
    / "06_tevv_reliability_incident"
)

# Fixture authorized_context users are not in IAM CSV — assessed smoke uses entitled QP.
SMOKE_USER = "qp_eu_1"
AS_OF = "2026-08-07T00:00:00Z"


def _load_pub(scenario_id: str) -> dict:
    path = PUB_DIR / f"{scenario_id}.json"
    assert path.is_file(), path
    return json.loads(path.read_text(encoding="utf-8"))


def test_all_fifteen_pub_fixtures_exist_and_have_scenario():
    for i in range(1, 16):
        sid = f"PUB-{i:02d}"
        data = _load_pub(sid)
        assert data["scenario"]["id"] == sid
        assert data["scenario"]["workflow"]
        assert data.get("authorized_context", {}).get("execution") == "disabled"


def test_pub01_02_batch_smoke_schema_valid():
    reset_call_count()
    for sid, key in (("PUB-01", "p6-pub01"), ("PUB-02", "p6-pub02")):
        code, resp = run_batch_evidence(
            {
                "request_id": f"p6-{sid}",
                "batch_id": "NCB204-B24071",
                "purpose": "batch_evidence",
                "as_of": AS_OF,
                "user": SMOKE_USER,
                "mode": "deterministic_offline",
                "idempotency_key": key,
            }
        )
        assert code == 200, resp
        _assert_schema("batch_response.schema.json", resp)
        assert resp.get("execution_status") == "not_executed"
    assert call_count() == 0


def test_pub04_pv_smoke_schema_valid():
    code, resp = run_pv_intake(
        {
            "request_id": "p6-PUB-04",
            "case_ids": ["PV-1001"],
            "purpose": "pv_intake",
            "as_of": AS_OF,
            "user": SMOKE_USER,
            "mode": "deterministic_offline",
            "idempotency_key": "p6-pub04",
        }
    )
    assert code == 200
    _assert_schema("pv_response.schema.json", resp)
    for k in ("seriousness", "causality", "reportability"):
        assert k not in resp


def test_pub07_supply_smoke_no_side_effects():
    code, resp = run_supply_options(
        {
            "request_id": "p6-PUB-07",
            "event_id": "SE-001",
            "purpose": "supply_options",
            "as_of": AS_OF,
            "user": SMOKE_USER,
            "mode": "deterministic_offline",
            "idempotency_key": "p6-pub07",
        }
    )
    assert code == 200
    _assert_schema("supply_response.schema.json", resp)
    assert resp["no_side_effects"] is True


def test_evaluate_hard_gates_ready_not_blocked():
    code, resp = dispatch(
        "/v1/evaluate/run",
        {
            "request_id": "p6-eval-1",
            "suite": "contracts",
            "fixture_ids": ["PUB-01", "PUB-04", "PUB-07"],
            "user": SMOKE_USER,
            "purpose": "evaluate",
            "as_of": AS_OF,
            "idempotency_key": "p6-eval-key",
        },
    )
    assert code == 200
    assert resp["ready_blocked"] is False
    assert all(r["gate"] == "pass" for r in resp["results"])


def test_outage_ai_disabled_kill_switch():
    code, body = dispatch(
        "/v1/workflows/batch_evidence",
        {
            "request_id": "p6-outage-narr",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": AS_OF,
            "user": SMOKE_USER,
            "mode": "ai_disabled",
            "narrator": True,
            "idempotency_key": "p6-outage-narr",
        },
    )
    assert code == 503


def test_phase6_artefact_companions_exist():
    for name in (
        "25_INCIDENT_RECOVERY.md",
        "TEVV_EXECUTION_DEEPEN.md",
        "incident_playbook.csv",
        "subgroup_evidence.csv",
        "pub_smoke_results.csv",
        "tevv_execution_results.csv",
    ):
        assert (PHASE6 / name).is_file(), name


def test_subgroup_csv_forbids_ungrounded_claims():
    path = PHASE6 / "subgroup_evidence.csv"
    with path.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) >= 8
    for r in rows:
        if r["grader_status"] == "not_run":
            assert r["claim_allowed"] == "no"
