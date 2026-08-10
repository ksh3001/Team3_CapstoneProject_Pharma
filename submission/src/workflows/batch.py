from __future__ import annotations
from typing import Any
from src.authz.service import authorization_block
from src.contracts.validate import PROHIBITED_BATCH_KEYS, assert_no_prohibited, validate_schema
from src.docs.applicability import applicable_documents
from src.evidence.csv_acl import evidence_item, read_csv
from src.runtime.context import RequestContext, error_envelope
from src.runtime.metrics import MetricsCollector
from src.runtime.mode import RuntimeMode
from src.paths import AUDIT_DIR
import json
import re


def _unit_token(text: str) -> str:
    t = (text or "").strip().lower().replace(" ", "")
    return t


def _spec_unit(spec: str) -> str:
    # e.g. "0.85-1.05 ug/mL" -> ug/ml
    m = re.search(r"([a-zA-Z%]+/?[a-zA-Z]*)\s*$", (spec or "").strip())
    return _unit_token(m.group(1) if m else "")


def run_batch_evidence(req: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    metrics = MetricsCollector()
    request_id = req.get("request_id") or "missing"
    ev = metrics.start("batch_evidence", request_id, "batch_evidence")
    mode = RuntimeMode.from_request(req.get("mode"))
    if req.get("narrator") or req.get("use_llm"):
        if mode.refuse_narrator() or not mode.allow_llm_call():
            return 503, error_envelope("mode_violation", "LLM/narrator disabled", request_id)

    user = req.get("user") or ""
    purpose = req.get("purpose") or "batch_evidence"
    batch_id = req.get("batch_id") or ""
    as_of = req.get("as_of") or RequestContext.utc_now()
    if purpose != "batch_evidence" or not batch_id or not user:
        return 400, error_envelope("validation_error", "missing required fields", request_id)

    # reject prohibited request shapes early
    bad = assert_no_prohibited(req, PROHIBITED_BATCH_KEYS)
    if bad:
        return 422, error_envelope("prohibited_fields", f"prohibited: {bad}", request_id)

    auth = authorization_block(user, purpose, batch_id, as_of, "batch")
    if auth["decision"] != "allow":
        ev.authz_decision = "deny"
        metrics.emit(ev)
        return 403, error_envelope("authz_denied", auth.get("reason", "deny"), request_id, {"authorization": auth})

    retrieved = RequestContext.utc_now()
    evidence = []
    contradictions = []
    gaps = []
    abstentions = []
    labs = [r for r in read_csv("lab_results.csv") if r.get("batch_id") == batch_id]
    if not labs:
        gaps.append({"gap": "no_lab_results", "batch_id": batch_id})
    for lab in labs:
        facts = dict(lab)
        evidence.append(
            evidence_item("lab_results.csv", lab["result_id"], "LIMS", lab.get("status"), facts, retrieved)
        )
        result_unit = _unit_token(lab.get("unit", ""))
        spec_u = _spec_unit(lab.get("spec", ""))
        if result_unit and spec_u and result_unit != spec_u:
            contradictions.append(
                {
                    "type": "unit_conflict",
                    "result_id": lab.get("result_id"),
                    "result_unit": lab.get("unit"),
                    "spec": lab.get("spec"),
                    "resolution": "none_dual_cite",
                    "silent_conversion": False,
                }
            )

    # interface mapping approval check (package signal)
    for m in read_csv("interface_mappings.csv"):
        if (m.get("approved") or "").lower() in {"no", "false", "0"}:
            contradictions.append(
                {
                    "type": "unapproved_interface_mapping",
                    "mapping": m,
                    "resolution": "none_dual_cite",
                }
            )

    docs = applicable_documents(as_of)
    applicable = [d for d in docs if d["instruction_applicable"]]
    quarantined = [d for d in docs if d["quarantined"]]

    if contradictions:
        readiness = "conflicted_evidence"
    elif gaps:
        readiness = "insufficient_evidence"
    else:
        readiness = "ready_for_authorized_review"

    human_review = {
        "required": bool(contradictions or gaps),
        "reasons": [c.get("type") for c in contradictions] + [g.get("gap") for g in gaps],
        "hitl": "mandatory_on_conflict_or_gap",
    }

    resp = {
        "request_id": request_id,
        "workflow": "batch_evidence",
        "as_of": as_of,
        "authorization": {
            "user": auth["user"],
            "purpose": auth["purpose"],
            "checked_at": auth["checked_at"],
            "decision": auth["decision"],
            "reason": auth.get("reason", ""),
        },
        "evidence": evidence,
        "contradictions": contradictions,
        "gaps": gaps,
        "abstentions": abstentions,
        "human_review": human_review,
        "execution_status": "not_executed",
        "audit": {"mode": mode.mode, "llm_enabled": False, "quarantined_docs": [d["doc_id"] for d in quarantined]},
        "batch_id": batch_id,
        "readiness_state": readiness,
        "applicable_documents": applicable,
    }

    errors = validate_schema(resp, "batch_response.schema.json")
    if errors:
        return 422, error_envelope("contract_violation", "; ".join(errors[:5]), request_id)

    bad = assert_no_prohibited(resp, PROHIBITED_BATCH_KEYS)
    if bad:
        return 422, error_envelope("prohibited_fields", f"prohibited: {bad}", request_id)

    (AUDIT_DIR / f"batch_{request_id}.json").write_text(json.dumps(resp, indent=2), encoding="utf-8")
    ev.authz_decision = "allow"
    ev.conflict_count = len(contradictions)
    ev.readiness_state = readiness
    metrics.emit(ev)
    return 200, resp
