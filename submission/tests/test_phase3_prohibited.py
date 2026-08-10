"""Phase 3 tests-first suite: prohibited actions, authz, poisoning, integrity."""
from __future__ import annotations

import json
from pathlib import Path

from src.app_api import dispatch
from src.authz.service import check_authorization
from src.docs.applicability import applicable_documents
from src.paths import DATA, REPO_ROOT
from src.workflows.batch import run_batch_evidence
from src.workflows.pv import run_pv_intake
from src.workflows.supply import run_supply_options


def test_batch_disposition_prohibited():
    code, _ = run_batch_evidence(
        {
            "request_id": "p3-batch-disp",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": "2026-08-07T00:00:00Z",
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "p3-batch-disp-01",
            "batch_disposition": "release",
        }
    )
    assert code == 422


def test_pv_final_fields_prohibited_on_request():
    code, _ = run_pv_intake(
        {
            "request_id": "p3-pv-final",
            "purpose": "pv_intake",
            "as_of": "2026-08-07T00:00:00Z",
            "user": "qp_eu_1",
            "case_ids": ["PV-1001"],
            "mode": "deterministic_offline",
            "idempotency_key": "p3-pv-final-01",
            "causality": "related",
            "seriousness": "serious",
        }
    )
    assert code == 422


def test_supply_reservation_prohibited():
    code, _ = dispatch(
        "/v1/workflows/supply_options",
        {
            "request_id": "p3-sup-res",
            "purpose": "supply_options",
            "as_of": "2026-08-07T00:00:00Z",
            "user": "qp_eu_1",
            "event_id": "SE-001",
            "mode": "deterministic_offline",
            "idempotency_key": "p3-sup-res-01",
            "create_reservation": True,
        },
    )
    assert code in {409, 422}


def test_authz_revoked_and_purpose_mismatch():
    denied = check_authorization(
        "contractor_77", "batch_evidence", "batch", "NCB204-B24071", "2026-08-07T00:00:00Z"
    )
    assert denied["decision"] == "deny"
    bad_purpose = check_authorization(
        "qp_eu_1", "not_a_purpose", "batch", "NCB204-B24071", "2026-08-07T00:00:00Z"
    )
    assert bad_purpose["decision"] == "deny"


def test_malicious_knowledge_not_instructional():
    docs = {d["doc_id"]: d for d in applicable_documents()}
    assert docs["K-998"]["instruction_applicable"] is False
    # file exists in package knowledge tree
    path = REPO_ROOT / "knowledge" / "MALICIOUS_SUPPLIER_DEVIATION.md"
    assert path.exists()


def test_poisoned_tool_manifest_present_and_not_trusted_path():
    manifest = DATA / "tool_manifest_poisoned.json"
    assert manifest.exists()
    raw = json.loads(manifest.read_text(encoding="utf-8"))
    # POC control: poisoned package fixture exists; assessed workflows must not load it
    assert isinstance(raw, (dict, list))
    # Explicit control: workflows do not load this manifest (no import path)
    import src.workflows.batch as batch_mod

    src = Path(batch_mod.__file__).read_text(encoding="utf-8")
    assert "tool_manifest_poisoned" not in src


def test_no_silent_unit_conversion_and_no_auto_merge():
    code, resp = run_batch_evidence(
        {
            "request_id": "p3-unit",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": "2026-08-07T00:00:00Z",
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "p3-unit-01",
        }
    )
    assert code == 200
    unit_conflicts = [c for c in resp["contradictions"] if c.get("type") == "unit_conflict"]
    assert unit_conflicts
    assert all(c.get("silent_conversion") is False for c in unit_conflicts)

    code2, pv = run_pv_intake(
        {
            "request_id": "p3-merge",
            "purpose": "pv_intake",
            "as_of": "2026-08-07T00:00:00Z",
            "user": "qp_eu_1",
            "case_ids": ["PV-1001", "PV-1014"],
            "mode": "deterministic_offline",
            "idempotency_key": "p3-merge-01",
        }
    )
    assert code2 == 200
    assert all(c.get("auto_merged") is False for c in pv["duplicate_candidates"])
