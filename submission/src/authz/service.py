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
