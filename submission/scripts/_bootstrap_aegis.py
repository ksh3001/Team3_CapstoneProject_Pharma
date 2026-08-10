"""One-shot bootstrap for Prompt 11 AEGIS POC sources. Run from repo root."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
TEST = ROOT / "tests"


def w(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.lstrip("\n"), encoding="utf-8")


def main() -> None:
    for p in [
        SRC / "authz",
        SRC / "evidence",
        SRC / "workflows",
        SRC / "contracts",
        SRC / "runtime",
        SRC / "ports",
        SRC / "evaluate",
        SRC / "docs",
        ROOT / "app",
        ROOT / "working" / "audit",
        ROOT / "working" / "metrics",
        ROOT / "working" / "idempotency",
        TEST,
        ROOT / "artefacts" / "11_build",
    ]:
        p.mkdir(parents=True, exist_ok=True)

    w(
        SRC / "__init__.py",
        '"""AEGIS Evidence Assist POC (deterministic offline)."""\n__version__ = "0.1.0"\n',
    )
    w(
        SRC / "paths.py",
        '''
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
''',
    )
    w(SRC / "runtime" / "__init__.py", "")
    w(
        SRC / "runtime" / "mode.py",
        '''
from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

Mode = Literal["deterministic_offline", "ai_disabled"]


@dataclass(frozen=True)
class RuntimeMode:
    mode: Mode = "deterministic_offline"
    llm_enabled: bool = False

    @classmethod
    def from_request(cls, mode: str | None) -> "RuntimeMode":
        m: Mode = "ai_disabled" if mode == "ai_disabled" else "deterministic_offline"
        return cls(mode=m, llm_enabled=False)

    def refuse_narrator(self) -> bool:
        return True

    def allow_llm_call(self) -> bool:
        return False
''',
    )
    w(
        SRC / "runtime" / "context.py",
        '''
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
''',
    )
    w(
        SRC / "runtime" / "idempotency.py",
        '''
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
''',
    )
    w(
        SRC / "runtime" / "metrics.py",
        '''
from __future__ import annotations
import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any
from src.paths import METRICS_DIR


@dataclass
class MetricsEvent:
    name: str
    request_id: str
    workflow: str
    started_ms: float
    ended_ms: float = 0.0
    side_effect_count: int = 0
    conflict_count: int = 0
    authz_decision: str = ""
    readiness_state: str = ""
    extra: dict[str, Any] = field(default_factory=dict)


class MetricsCollector:
    def start(self, name: str, request_id: str, workflow: str) -> MetricsEvent:
        return MetricsEvent(
            name=name, request_id=request_id, workflow=workflow, started_ms=time.time() * 1000
        )

    def emit(self, event: MetricsEvent) -> Path:
        event.ended_ms = time.time() * 1000
        path = METRICS_DIR / f"{event.request_id}_{event.workflow}.json"
        path.write_text(json.dumps(asdict(event), indent=2), encoding="utf-8")
        return path
''',
    )
    w(SRC / "ports" / "__init__.py", "")
    w(
        SRC / "ports" / "llm.py",
        '''
from __future__ import annotations

CALL_COUNT = 0


class NoOpLLM:
    def complete(self, *args, **kwargs):
        global CALL_COUNT
        CALL_COUNT += 1
        raise RuntimeError("LLM disabled in assessed deterministic path")


def reset_call_count() -> None:
    global CALL_COUNT
    CALL_COUNT = 0


def call_count() -> int:
    return CALL_COUNT
''',
    )
    w(SRC / "contracts" / "__init__.py", "")
    w(
        SRC / "contracts" / "validate.py",
        '''
from __future__ import annotations
import json
from typing import Any
from jsonschema import Draft202012Validator, RefResolver
from src.paths import CONTRACTS

PROHIBITED_BATCH_KEYS = {
    "batch_disposition",
    "release",
    "reject",
    "recall",
    "reprocess",
    "relabel",
    "disposition",
}
PROHIBITED_PV_KEYS = {
    "seriousness",
    "causality",
    "expectedness",
    "reportability",
    "signal_confirmation",
    "final_seriousness",
    "final_causality",
    "final_expectedness",
    "final_reportability",
}
PROHIBITED_SUPPLY_KEYS = {
    "reservation_id",
    "allocation_id",
    "shipment_id",
    "quality_status_change",
    "recall_initiated",
    "reserved_units",
    "allocated_units",
}


def _load(name: str) -> dict[str, Any]:
    return json.loads((CONTRACTS / name).read_text(encoding="utf-8"))


def validate_schema(instance: dict[str, Any], schema_name: str) -> list[str]:
    schema = _load(schema_name)
    store: dict[str, Any] = {}
    for p in CONTRACTS.glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        store[doc.get("$id", p.name)] = doc
        store[p.name] = doc
    resolver = RefResolver.from_schema(schema, store=store)
    validator = Draft202012Validator(schema, resolver=resolver)
    return [e.message for e in sorted(validator.iter_errors(instance), key=lambda e: list(e.path))]


def assert_no_prohibited(payload: dict[str, Any], keys: set[str]) -> list[str]:
    found = sorted(k for k in keys if k in payload)
    for opt in payload.get("options") or []:
        if isinstance(opt, dict):
            found.extend(sorted(k for k in keys if k in opt))
    return found
''',
    )
    w(SRC / "evidence" / "__init__.py", "")
    w(
        SRC / "evidence" / "csv_acl.py",
        '''
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
''',
    )
    w(SRC / "docs" / "__init__.py", "")
    w(
        SRC / "docs" / "applicability.py",
        '''
from __future__ import annotations
from typing import Any
from src.evidence.csv_acl import read_csv

INSTRUCTION_BLOCK = {"untrusted", "draft", "superseded"}


def catalog_rows() -> list[dict[str, str]]:
    return read_csv("knowledge_catalog.csv")


def classify_document(row: dict[str, str]) -> dict[str, Any]:
    status = (row.get("status") or "").lower()
    trust = (row.get("trust") or "").lower()
    instruction_applicable = status == "approved" and trust == "approved"
    quarantined = (status in INSTRUCTION_BLOCK or trust in INSTRUCTION_BLOCK) and not instruction_applicable
    return {
        "doc_id": row.get("doc_id"),
        "file": row.get("file"),
        "status": row.get("status"),
        "trust": row.get("trust"),
        "authority": row.get("authority"),
        "jurisdiction": row.get("jurisdiction"),
        "instruction_applicable": instruction_applicable,
        "quarantined": quarantined,
    }


def applicable_documents(as_of: str | None = None) -> list[dict[str, Any]]:
    return [classify_document(r) for r in catalog_rows()]


def assert_not_instruction_authority(doc_id: str) -> bool:
    for d in applicable_documents():
        if d["doc_id"] == doc_id:
            return not d["instruction_applicable"]
    return True
''',
    )
    w(SRC / "authz" / "__init__.py", "")
    w(
        SRC / "authz" / "service.py",
        '''
from __future__ import annotations
import json
from typing import Any
from src.evidence.csv_acl import read_csv
from src.paths import AUDIT_DIR
from src.runtime.context import RequestContext

ALLOWED_PURPOSES = {"batch_evidence", "pv_intake", "supply_options", "evaluate"}


def _iam_row(user: str) -> dict[str, str] | None:
    for row in read_csv("users_entitlements.csv"):
        if row.get("user") == user:
            return row
    return None


def _cache_active(user: str) -> bool:
    for row in read_csv("access_cache.csv"):
        if row.get("user") == user:
            return True
    return False


def check_authorization(
    user: str,
    purpose: str,
    object_type: str,
    object_id: str,
    as_of: str,
) -> dict[str, Any]:
    checked_at = RequestContext.utc_now()
    reason = ""
    decision = "deny"

    if not user:
        reason = "missing_user"
    elif purpose not in ALLOWED_PURPOSES:
        reason = "invalid_purpose"
    else:
        row = _iam_row(user)
        if row is None:
            reason = "unknown_user"
        else:
            iam_state = (row.get("iam_state") or "").lower()
            role = row.get("role") or ""
            cache_hit = _cache_active(user)
            if iam_state == "revoked":
                decision = "deny"
                reason = "iam_revoked_overrides_cache" if cache_hit else "iam_revoked"
            elif iam_state != "active":
                decision = "deny"
                reason = f"iam_state_{iam_state}"
            elif role == "qualified_person":
                decision = "allow"
                reason = "iam_active_entitled"
            else:
                decision = "deny"
                reason = "role_not_permitted_for_purpose"

    result = {
        "decision": decision,
        "user": user,
        "purpose": purpose,
        "object_type": object_type,
        "object_id": object_id,
        "checked_at": checked_at,
        "reason": reason,
    }
    path = AUDIT_DIR / f"authz_{result['user']}_{result['purpose']}_{result['object_id']}.json"
    path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def authorization_block(
    user: str, purpose: str, object_id: str, as_of: str, object_type: str
) -> dict[str, Any]:
    r = check_authorization(user, purpose, object_type, object_id, as_of)
    return {
        "user": r["user"],
        "purpose": r["purpose"],
        "checked_at": r["checked_at"],
        "decision": r["decision"],
        "reason": r.get("reason", ""),
    }
''',
    )

    # Workflows + evaluate + app written in part 2
    print("part1 ok", SRC)


if __name__ == "__main__":
    main()
