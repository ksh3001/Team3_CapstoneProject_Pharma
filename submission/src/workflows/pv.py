from __future__ import annotations
import json
import re
from typing import Any
from src.authz.service import authorization_block
from src.contracts.validate import PROHIBITED_PV_KEYS, assert_no_prohibited, validate_schema
from src.docs.applicability import applicable_documents, assert_not_instruction_authority
from src.evidence.csv_acl import evidence_item, read_csv
from src.runtime.context import RequestContext, error_envelope
from src.runtime.metrics import MetricsCollector
from src.runtime.mode import RuntimeMode
from src.paths import AUDIT_DIR


def _norm_product(p: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (p or "").lower())


def _strong_key(row: dict[str, str]) -> tuple[str, str, str, str]:
    return (
        _norm_product(row.get("product", "")),
        (row.get("patient_key") or "").lower(),
        (row.get("awareness_date") or "").strip(),
        (row.get("event") or "").strip().lower(),
    )


def run_pv_intake(req: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    metrics = MetricsCollector()
    request_id = req.get("request_id") or "missing"
    ev = metrics.start("pv_intake", request_id, "pv_intake")
    mode = RuntimeMode.from_request(req.get("mode"))
    if req.get("narrator") or req.get("use_llm"):
        return 503, error_envelope("mode_violation", "LLM/narrator disabled", request_id)

    user = req.get("user") or ""
    purpose = req.get("purpose") or "pv_intake"
    case_ids = req.get("case_ids") or []
    as_of = req.get("as_of") or RequestContext.utc_now()
    if purpose != "pv_intake" or not case_ids or not user:
        return 400, error_envelope("validation_error", "missing required fields", request_id)

    bad = assert_no_prohibited(req, PROHIBITED_PV_KEYS)
    if bad:
        return 422, error_envelope("prohibited_fields", f"prohibited: {bad}", request_id)

    object_id = case_ids[0]
    auth = authorization_block(user, purpose, object_id, as_of, "case_package")
    if auth["decision"] != "allow":
        metrics.emit(ev)
        return 403, error_envelope("authz_denied", auth.get("reason", "deny"), request_id, {"authorization": auth})

    retrieved = RequestContext.utc_now()
    cases = {r["case_id"]: r for r in read_csv("icsr_cases.csv")}
    selected = []
    gaps = []
    for cid in case_ids:
        if cid not in cases:
            gaps.append({"gap": "unknown_case", "case_id": cid})
        else:
            selected.append(cases[cid])

    evidence = []
    source_facts = []
    for row in selected:
        facts = dict(row)
        evidence.append(
            evidence_item("icsr_cases.csv", row["case_id"], "Safety DB", row.get("awareness_date"), facts, retrieved)
        )
        source_facts.append({"case_id": row["case_id"], "facts": facts})

    # exact + strong_key duplicates only (fuzzy disabled)
    duplicate_candidates = []
    by_exact = {}
    by_strong: dict[tuple, list[str]] = {}
    for row in selected:
        by_exact.setdefault(row["case_id"], []).append(row["case_id"])
        by_strong.setdefault(_strong_key(row), []).append(row["case_id"])
    for key, ids in by_strong.items():
        uniq = sorted(set(ids))
        if len(uniq) > 1:
            duplicate_candidates.append(
                {"strategy": "strong_key", "key": list(key), "case_ids": uniq, "auto_merged": False}
            )

    # Do not auto-link using fuzzy scores from duplicate_candidates.csv
    for fuzzy in read_csv("duplicate_candidates.csv"):
        # record as informational only when both cases requested — never merge
        if fuzzy.get("case_a") in case_ids and fuzzy.get("case_b") in case_ids:
            duplicate_candidates.append(
                {
                    "strategy": "fuzzy_disabled",
                    "case_ids": [fuzzy.get("case_a"), fuzzy.get("case_b")],
                    "score_observed": fuzzy.get("score"),
                    "auto_merged": False,
                    "status": "manual_assessment_required",
                }
            )

    clock_evidence = []
    contradictions = []
    required_reviews = []
    for cid in case_ids:
        receipts = [r for r in read_csv("safety_receipts.csv") if r.get("case_id") == cid]
        for r in receipts:
            clock_evidence.append(
                {"case_id": cid, "clock": "receipt_at", "source": r.get("channel"), "value": r.get("receipt")}
            )
        if cid in cases:
            clock_evidence.append(
                {
                    "case_id": cid,
                    "clock": "awareness_date",
                    "source": "icsr_cases.csv",
                    "value": cases[cid].get("awareness_date"),
                }
            )
        values = {c["value"] for c in clock_evidence if c["case_id"] == cid and c.get("value")}
        if len(values) > 1:
            contradictions.append({"type": "clock_disagreement", "case_id": cid, "values": sorted(values)})
            required_reviews.append("clock_resolution")
        lang = (cases.get(cid) or {}).get("language") or ""
        if lang and lang.lower() not in {"english", "en"}:
            required_reviews.append("multilingual_review")

    # K-999 must not be reportability authority
    listedness_context = []
    for d in applicable_documents():
        if d["doc_id"] == "K-999":
            listedness_context.append(
                {
                    "doc_id": "K-999",
                    "instruction_applicable": False,
                    "reportability_authority": False,
                    "quarantined": True,
                }
            )
        elif d["instruction_applicable"]:
            listedness_context.append(
                {"doc_id": d["doc_id"], "instruction_applicable": True, "reportability_authority": False}
            )

    assert assert_not_instruction_authority("K-999")

    if any(c.get("strategy") == "fuzzy_disabled" for c in duplicate_candidates):
        required_reviews.append("duplicate_manual_assessment")

    required_reviews = sorted(set(required_reviews))
    terminology = [{"case_id": r["case_id"], "event_verbatim": r.get("event")} for r in selected]

    resp = {
        "request_id": request_id,
        "workflow": "pv_intake",
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
        "abstentions": [],
        "human_review": {"required": bool(required_reviews or contradictions), "required_reviews": required_reviews},
        "execution_status": "not_executed",
        "audit": {"mode": mode.mode, "llm_enabled": False, "fuzzy_enabled": False},
        "case_ids": case_ids,
        "source_facts": source_facts,
        "duplicate_candidates": duplicate_candidates,
        "clock_evidence": clock_evidence,
        "terminology": terminology,
        "listedness_context": listedness_context,
        "required_reviews": required_reviews,
    }

    errors = validate_schema(resp, "pv_response.schema.json")
    if errors:
        return 422, error_envelope("contract_violation", "; ".join(errors[:5]), request_id)
    bad = assert_no_prohibited(resp, PROHIBITED_PV_KEYS)
    if bad:
        return 422, error_envelope("prohibited_fields", f"prohibited: {bad}", request_id)

    (AUDIT_DIR / f"pv_{request_id}.json").write_text(json.dumps(resp, indent=2), encoding="utf-8")
    ev.authz_decision = "allow"
    ev.conflict_count = len(contradictions)
    metrics.emit(ev)
    return 200, resp
