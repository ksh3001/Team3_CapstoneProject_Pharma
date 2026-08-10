from __future__ import annotations
import json
from typing import Any
from src.authz.service import authorization_block
from src.contracts.validate import PROHIBITED_SUPPLY_KEYS, assert_no_prohibited, validate_schema
from src.evidence.csv_acl import evidence_item, forbid_write, read_csv
from src.paths import AUDIT_DIR, DATA
from src.runtime.context import RequestContext, error_envelope
from src.runtime.metrics import MetricsCollector
from src.runtime.mode import RuntimeMode


class SideEffectGuard:
    def __init__(self) -> None:
        self.side_effect_count = 0
        self.attempts: list[str] = []

    def note_attempt(self, kind: str) -> None:
        self.attempts.append(kind)
        self.side_effect_count += 1

    def assert_clean(self) -> None:
        if self.side_effect_count != 0:
            raise RuntimeError(f"side_effects_detected:{self.attempts}")


def run_supply_options(req: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    metrics = MetricsCollector()
    request_id = req.get("request_id") or "missing"
    ev = metrics.start("supply_options", request_id, "supply_options")
    mode = RuntimeMode.from_request(req.get("mode"))
    guard = SideEffectGuard()

    if req.get("narrator") or req.get("use_llm"):
        return 503, error_envelope("mode_violation", "LLM/narrator disabled", request_id)

    user = req.get("user") or ""
    purpose = req.get("purpose") or "supply_options"
    event_id = req.get("event_id") or ""
    as_of = req.get("as_of") or RequestContext.utc_now()
    if purpose != "supply_options" or not event_id or not user:
        return 400, error_envelope("validation_error", "missing required fields", request_id)

    bad = assert_no_prohibited(req, PROHIBITED_SUPPLY_KEYS)
    if bad:
        return 422, error_envelope("prohibited_fields", f"prohibited: {bad}", request_id)

    # Explicitly refuse reservation creation attempts
    if req.get("create_reservation") or req.get("reserve"):
        guard.note_attempt("reservation")
        return 409, error_envelope("side_effect_blocked", "reservation forbidden", request_id)

    auth = authorization_block(user, purpose, event_id, as_of, "shortage_event")
    if auth["decision"] != "allow":
        metrics.emit(ev)
        return 403, error_envelope("authz_denied", auth.get("reason", "deny"), request_id, {"authorization": auth})

    retrieved = RequestContext.utc_now()
    inv = read_csv("inventory.csv")
    evidence = []
    quality_holds = []
    available = []
    for row in inv:
        evidence.append(
            evidence_item(
                "inventory.csv",
                f"{row.get('product')}:{row.get('market')}",
                "WMS",
                None,
                dict(row),
                retrieved,
            )
        )
        status = (row.get("quality_status") or "").lower()
        if status == "quarantine":
            quality_holds.append({"product": row.get("product"), "market": row.get("market"), "units": row.get("units")})
        elif status == "released":
            available.append(row)

    options = [
        {
            "option_id": f"OPT-{i+1}",
            "status": "draft",
            "product": row.get("product"),
            "market": row.get("market"),
            "available_units": row.get("units"),
            "quality_status": row.get("quality_status"),
        }
        for i, row in enumerate(available)
    ]

    # Never write challenge data
    try:
        forbid_write(DATA / "inventory.csv")
    except Exception:
        pass

    guard.assert_clean()

    resp = {
        "request_id": request_id,
        "workflow": "supply_options",
        "as_of": as_of,
        "authorization": {
            "user": auth["user"],
            "purpose": auth["purpose"],
            "checked_at": auth["checked_at"],
            "decision": auth["decision"],
            "reason": auth.get("reason", ""),
        },
        "evidence": evidence,
        "contradictions": [],
        "gaps": [],
        "abstentions": [],
        "human_review": {"required": True, "reasons": ["supply_governance_approval"]},
        "execution_status": "not_executed",
        "audit": {"mode": mode.mode, "llm_enabled": False, "side_effect_count": guard.side_effect_count},
        "event_id": event_id,
        "options": options,
        "constraints": [{"constraint": "released_only_available"}, {"constraint": "no_side_effects"}],
        "approvals_required": ["Supply Governance Board"],
        "quality_holds": quality_holds,
        "no_side_effects": True,
    }

    errors = validate_schema(resp, "supply_response.schema.json")
    if errors:
        return 422, error_envelope("contract_violation", "; ".join(errors[:5]), request_id)
    bad = assert_no_prohibited(resp, PROHIBITED_SUPPLY_KEYS)
    if bad:
        return 422, error_envelope("prohibited_fields", f"prohibited: {bad}", request_id)

    (AUDIT_DIR / f"supply_{request_id}.json").write_text(json.dumps(resp, indent=2), encoding="utf-8")
    ev.authz_decision = "allow"
    ev.side_effect_count = 0
    metrics.emit(ev)
    return 200, resp
