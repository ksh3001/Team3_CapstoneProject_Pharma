"""Phase 5: TEVV suite map and scorecard companions must be complete and honest."""
from __future__ import annotations

import csv
from pathlib import Path

PHASE5 = (
    Path(__file__).resolve().parents[1]
    / "artefacts"
    / "phases"
    / "05_assurance_evaluation_ops"
)

ALLOWED_STATUS = {
    "pass_poc",
    "partial",
    "inconclusive_data_scarcity",
    "deferred",
    "fail",
}


def _rows(name: str) -> list[dict[str, str]]:
    path = PHASE5 / name
    assert path.is_file(), path
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def test_tevv_has_twelve_suites_with_allowed_status():
    rows = _rows("tevv_suite_status.csv")
    assert len(rows) == 12
    ids = [r["suite_id"] for r in rows]
    assert ids == [f"TEVV-{i:02d}" for i in range(1, 13)]
    for r in rows:
        assert r["status"] in ALLOWED_STATUS, r
        assert r["primary_evidence"].strip()
        # Honesty: must not claim blanket production pass
        assert r["status"] != "pass_production"


def test_hard_gate_suite_is_pass_poc():
    by_id = {r["suite_id"]: r for r in _rows("tevv_suite_status.csv")}
    assert by_id["TEVV-03"]["status"] == "pass_poc"


def test_scorecard_production_no_go():
    rows = _rows("scorecard_summary.csv")
    by_dim = {r["dimension"]: r for r in rows}
    assert by_dim["production_go"]["verdict"] == "no_go"
    assert by_dim["demo_go"]["verdict"] == "conditional_go"
    assert by_dim["hard_gates"]["verdict"] == "pass"
    assert by_dim["business_outcome_roi"]["verdict"] == "inconclusive_data_scarcity"
