"""Phase 7: production no-go checklist and handover companions must stay honest."""
from __future__ import annotations

import csv
from pathlib import Path

PHASE7 = (
    Path(__file__).resolve().parents[1]
    / "artefacts"
    / "phases"
    / "07_operating_model_transfer"
)


def _rows(name: str) -> list[dict[str, str]]:
    path = PHASE7 / name
    assert path.is_file(), path
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def test_phase7_templates_exist():
    for name in (
        "26_TARGET_OPERATING_MODEL.md",
        "27_VENDOR_EXIT_RETIREMENT.md",
        "28_PRODUCTION_READINESS.md",
        "29_NINETY_DAY_ROADMAP_HANDOVER.md",
        "PHASE7_CHECKPOINT.md",
    ):
        assert (PHASE7 / name).is_file(), name


def test_production_checklist_no_go():
    rows = _rows("production_readiness_checklist.csv")
    by_id = {r["item_id"]: r for r in rows}
    assert by_id["PR-12"]["production_status"] == "no_go"
    assert by_id["PR-13"]["demo_status"] == "conditional_go"
    assert by_id["PR-06"]["production_status"] == "not_ready_denied"
    assert by_id["PR-11"]["demo_status"] == "absent_correct"


def test_capability_owners_external_decisions():
    rows = _rows("capability_owners.csv")
    assert len(rows) >= 8
    batch = next(r for r in rows if r["capability_id"] == "CAP-BATCH")
    assert "certification" in batch["external_decision"].lower() or "QP" in batch["external_decision"]
    assert batch["aegis_authority"] == "evidence_pack"


def test_roadmap_defers_llm_and_has_windows():
    rows = _rows("roadmap_90day.csv")
    windows = {r["window_days"] for r in rows}
    assert {"0-30", "31-60", "61-90"} <= windows
    # ADR-002 revisit must not be in 0-30 as forced enable
    early = [r for r in rows if r["window_days"] == "0-30"]
    assert not any("ADR-002" in r["action"] and "enable" in r["action"].lower() for r in early)


def test_handover_inventory_marks_challenge_read_only():
    rows = _rows("handover_inventory.csv")
    challenge = next(r for r in rows if r["bundle_id"] == "H-15")
    assert challenge["status"] == "read_only"


def test_dependency_inventory_llm_not_in_use():
    rows = _rows("dependency_inventory.csv")
    llm = next(r for r in rows if r["dependency_id"] == "DEP-04")
    assert llm["assessed_in_use"] == "no"
    write = next(r for r in rows if r["dependency_id"] == "DEP-06")
    assert write["criticality"] == "prohibited"
