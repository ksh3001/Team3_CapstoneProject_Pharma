from __future__ import annotations
import hashlib
import json
from typing import Any
from src.paths import IDEM_DIR


def _key_path(key: str):
    safe = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return IDEM_DIR / f"{safe}.json"


def body_hash(body: dict[str, Any]) -> str:
    raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def check_or_store(
    key: str, body: dict[str, Any], response: dict[str, Any] | None = None
) -> tuple[str, dict[str, Any] | None]:
    if not key or not (8 <= len(key) <= 128):
        raise ValueError("idempotency_key must be 8-128 chars")
    path = _key_path(key)
    h = body_hash(body)
    if path.exists():
        prior = json.loads(path.read_text(encoding="utf-8"))
        if prior.get("body_hash") != h:
            return "conflict", None
        return "ok", prior.get("response")
    if response is not None:
        path.write_text(
            json.dumps({"body_hash": h, "response": response}, indent=2), encoding="utf-8"
        )
        return "ok", response
    return "miss", None
