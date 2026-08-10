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
