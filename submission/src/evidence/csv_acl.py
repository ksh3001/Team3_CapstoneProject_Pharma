from __future__ import annotations
import csv
import hashlib
import json
from pathlib import Path
from typing import Any
from src.paths import DATA


class ChallengeWriteError(RuntimeError):
    pass


def _ensure_under_data(path: Path) -> Path:
    resolved = path.resolve()
    data_root = DATA.resolve()
    if data_root not in resolved.parents and resolved != data_root:
        raise ChallengeWriteError(f"ACL path escape: {path}")
    return resolved


def read_csv(name: str) -> list[dict[str, str]]:
    path = _ensure_under_data(DATA / name)
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def forbid_write(path: Path) -> None:
    raise ChallengeWriteError(f"Write to challenge path forbidden: {path}")


def evidence_item(
    source: str,
    record_id: str,
    authority: str,
    effective_at: str | None,
    facts: dict[str, Any],
    retrieved_at: str,
) -> dict[str, Any]:
    raw = json.dumps(facts, sort_keys=True, separators=(",", ":")).encode("utf-8")
    digest = hashlib.sha256(raw).hexdigest()
    return {
        "source": source,
        "record_id": record_id,
        "authority": authority,
        "effective_at": effective_at,
        "retrieved_at": retrieved_at,
        "facts": facts,
        "integrity": {"sha256": digest, "source_preserved": True},
    }
