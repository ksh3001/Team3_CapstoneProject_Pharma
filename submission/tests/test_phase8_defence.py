"""Phase 8: defence artefacts exist and live failure demos all pass."""
from __future__ import annotations

import csv
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBMISSION = ROOT / "submission"
PHASE8 = SUBMISSION / "artefacts" / "phases" / "08_defence"
SCRIPT = SUBMISSION / "scripts" / "run_defence_failure_demos.py"
RESULTS = PHASE8 / "failure_demo_results.csv"


def test_phase8_artefacts_exist():
    for name in (
        "30_ELEVATOR_PITCH.md",
        "FINAL_RECOMMENDATION.md",
        "FAILURE_DEMOS.md",
        "PHASE8_CHECKPOINT.md",
    ):
        assert (PHASE8 / name).is_file(), name


def test_run_defence_failure_demos_all_pass():
    env = os.environ.copy()
    env["PYTHONPATH"] = str(SUBMISSION)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=str(ROOT),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert RESULTS.is_file()
    with RESULTS.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == 8
    assert all(r["observed_pass"] == "yes" for r in rows), rows


def test_final_recommendation_states_no_go():
    text = (PHASE8 / "FINAL_RECOMMENDATION.md").read_text(encoding="utf-8").lower()
    assert "no-go" in text or "no_go" in text
    assert "conditional-go" in text or "conditional_go" in text
    assert "hypothesis" in text
