"""Phase 4: AuthZ matrix rows must match live authorization decisions."""
from __future__ import annotations

import csv
from pathlib import Path

from src.authz.service import check_authorization

MATRIX = (
    Path(__file__).resolve().parents[1]
    / "artefacts"
    / "phases"
    / "04_security_privacy_governance"
    / "authz_matrix.csv"
)


def _matrix_rows() -> list[dict[str, str]]:
    with MATRIX.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def test_authz_matrix_file_exists_and_has_rows():
    assert MATRIX.is_file()
    rows = _matrix_rows()
    assert len(rows) >= 8


def test_authz_matrix_expected_decisions():
    for row in _matrix_rows():
        user = row["user"]
        purpose = row["purpose"]
        object_type = row["object_type"] or "batch"
        expected = row["expected_decision"]
        # Skip empty-purpose row — service treats as invalid_purpose deny;
        # call with empty string to mirror BR-002.
        result = check_authorization(
            user=user,
            purpose=purpose,
            object_type=object_type,
            object_id="matrix-probe",
            as_of="2026-08-07",
        )
        assert result["decision"] == expected, (
            f"{user}/{purpose}: got {result['decision']} ({result.get('reason')}), "
            f"expected {expected}"
        )
