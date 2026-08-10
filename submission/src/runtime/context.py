from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
import uuid


@dataclass
class RequestContext:
    request_id: str
    user: str
    purpose: str
    as_of: str
    idempotency_key: str | None = None
    mode: str = "deterministic_offline"

    @staticmethod
    def utc_now() -> str:
        return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def new_request_id() -> str:
    return str(uuid.uuid4())


def error_envelope(
    code: str,
    message: str,
    request_id: str | None = None,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    env: dict[str, Any] = {
        "error": {
            "code": code,
            "message": message,
            "request_id": request_id or new_request_id(),
        }
    }
    if details:
        env["error"]["details"] = details
    return env
