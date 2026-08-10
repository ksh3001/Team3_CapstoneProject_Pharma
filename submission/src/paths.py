"""Resolve repo and challenge data paths (read-only challenge trees)."""
from __future__ import annotations
from pathlib import Path

SUBMISSION = Path(__file__).resolve().parents[1]
REPO_ROOT = SUBMISSION.parent
DATA = REPO_ROOT / "data"
KNOWLEDGE = REPO_ROOT / "knowledge"
CONTRACTS = REPO_ROOT / "evaluation" / "contracts"
WORKING = SUBMISSION / "working"
AUDIT_DIR = WORKING / "audit"
METRICS_DIR = WORKING / "metrics"
IDEM_DIR = WORKING / "idempotency"

for d in (WORKING, AUDIT_DIR, METRICS_DIR, IDEM_DIR):
    d.mkdir(parents=True, exist_ok=True)
