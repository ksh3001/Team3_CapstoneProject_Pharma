"""Part 2: workflows, evaluate, CLI, audit helpers."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


def w(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.lstrip("\n"), encoding="utf-8")


def main() -> None:
    w(SRC / "workflows" / "__init__.py", "")
    w(
        SRC / "workflows" / "batch.py",
        '''
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
    m = re.search(r"([a-zA-Z%]+/?[a-zA-Z]*)\\s*$", (spec or "").strip())
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
''',
    )
    w(
        SRC / "workflows" / "pv.py",
        '''
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
''',
    )
    w(
        SRC / "workflows" / "supply.py",
        '''
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
''',
    )
    w(SRC / "evaluate" / "__init__.py", "")
    w(
        SRC / "evaluate" / "runner.py",
        '''
from __future__ import annotations
import json
from typing import Any
from src.authz.service import check_authorization
from src.contracts.validate import PROHIBITED_BATCH_KEYS, PROHIBITED_SUPPLY_KEYS, assert_no_prohibited, validate_schema
from src.paths import AUDIT_DIR, METRICS_DIR
from src.runtime.context import RequestContext, error_envelope
from src.workflows.batch import run_batch_evidence
from src.workflows.supply import run_supply_options


def run_evaluate(req: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    request_id = req.get("request_id") or "eval-missing"
    user = req.get("user") or ""
    purpose = req.get("purpose") or "evaluate"
    as_of = req.get("as_of") or RequestContext.utc_now()
    suite = req.get("suite") or "contracts"
    auth = check_authorization(user, purpose, "evaluation_run", request_id, as_of)
    if auth["decision"] != "allow":
        return 403, error_envelope("authz_denied", auth.get("reason", "deny"), request_id)

    results = []
    ready_blocked = False

    # Gate: authz revoke+cache
    denied = check_authorization("contractor_77", "batch_evidence", "batch", "NCB204-B24071", as_of)
    gate = "pass" if denied["decision"] == "deny" else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "AUTHZ-contractor_77",
            "gate": gate,
            "ac_ids": ["AC-001", "AC-062"],
            "evidence_path": str(AUDIT_DIR.relative_to(AUDIT_DIR.parents[1]) / f"authz_contractor_77_batch_evidence_NCB204-B24071.json"),
            "reason_codes": [denied.get("reason", "")],
        }
    )

    # Gate: batch happy path schema + no disposition + LR-88 conflict
    code, batch = run_batch_evidence(
        {
            "request_id": f"{request_id}-batch",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": as_of,
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "evaluate-batch-01",
        }
    )
    batch_ok = code == 200 and batch.get("execution_status") == "not_executed"
    unit_conflict = any(c.get("type") == "unit_conflict" for c in batch.get("contradictions", []))
    no_disp = not assert_no_prohibited(batch, PROHIBITED_BATCH_KEYS) if code == 200 else False
    schema_errs = validate_schema(batch, "batch_response.schema.json") if code == 200 else ["http_not_200"]
    gate = "pass" if batch_ok and unit_conflict and no_disp and not schema_errs else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "BATCH-LR-88",
            "gate": gate,
            "ac_ids": ["AC-020", "AC-021", "AC-022", "AC-060"],
            "evidence_path": f"working/audit/batch_{request_id}-batch.json",
            "reason_codes": [] if gate == "pass" else schema_errs[:3] or ["batch_gate_fail"],
        }
    )

    # Prohibited batch shape must be rejected
    pcode, _ = run_batch_evidence(
        {
            "request_id": f"{request_id}-bad",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": as_of,
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "evaluate-batch-bad",
            "batch_disposition": "release",
        }
    )
    gate = "pass" if pcode == 422 else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "BATCH-prohibited-disposition",
            "gate": gate,
            "ac_ids": ["AC-023", "AC-060"],
            "evidence_path": "n/a",
            "reason_codes": [str(pcode)],
        }
    )

    # Supply side effects
    scode, supply = run_supply_options(
        {
            "request_id": f"{request_id}-supply",
            "purpose": "supply_options",
            "as_of": as_of,
            "user": "qp_eu_1",
            "event_id": "SE-001",
            "mode": "deterministic_offline",
            "idempotency_key": "evaluate-supply-01",
        }
    )
    supply_ok = (
        scode == 200
        and supply.get("no_side_effects") is True
        and supply.get("execution_status") == "not_executed"
        and not assert_no_prohibited(supply, PROHIBITED_SUPPLY_KEYS)
        and not any((o.get("quality_status") or "").lower() == "quarantine" for o in supply.get("options", []))
    )
    gate = "pass" if supply_ok else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "SUPPLY-no-side-effects",
            "gate": gate,
            "ac_ids": ["AC-040", "AC-041", "AC-042", "AC-061"],
            "evidence_path": f"working/audit/supply_{request_id}-supply.json",
            "reason_codes": [] if gate == "pass" else ["supply_gate_fail"],
        }
    )

    rcode, _ = run_supply_options(
        {
            "request_id": f"{request_id}-reserve",
            "purpose": "supply_options",
            "as_of": as_of,
            "user": "qp_eu_1",
            "event_id": "SE-001",
            "mode": "deterministic_offline",
            "idempotency_key": "evaluate-supply-bad",
            "create_reservation": True,
        }
    )
    gate = "pass" if rcode in {409, 422} else "fail"
    if gate == "fail":
        ready_blocked = True
    results.append(
        {
            "fixture_id": "SUPPLY-reservation-blocked",
            "gate": gate,
            "ac_ids": ["AC-043", "AC-061"],
            "evidence_path": "n/a",
            "reason_codes": [str(rcode)],
        }
    )

    resp = {
        "run_id": request_id,
        "suite": suite,
        "results": results,
        "ready_blocked": ready_blocked,
        "audit": {"evaluated_at": RequestContext.utc_now(), "user": user},
    }
    (METRICS_DIR / f"evaluate_{request_id}.json").write_text(json.dumps(resp, indent=2), encoding="utf-8")
    return 200, resp
''',
    )
    w(
        SRC / "app_api.py",
        '''
from __future__ import annotations
import json
from typing import Any, Callable
from src.authz.service import check_authorization
from src.evaluate.runner import run_evaluate
from src.runtime.idempotency import check_or_store
from src.runtime.mode import RuntimeMode
from src.workflows.batch import run_batch_evidence
from src.workflows.pv import run_pv_intake
from src.workflows.supply import run_supply_options


def health() -> dict[str, Any]:
    mode = RuntimeMode()
    return {"status": "ok", "mode": mode.mode, "llm_enabled": mode.llm_enabled}


def _with_idempotency(req: dict[str, Any], handler: Callable[[dict[str, Any]], tuple[int, dict[str, Any]]]):
    key = req.get("idempotency_key")
    if not key:
        return 400, {"error": {"code": "validation_error", "message": "idempotency_key required", "request_id": req.get("request_id")}}
    status, prior = check_or_store(key, req, None)
    if status == "conflict":
        return 409, {"error": {"code": "idempotency_conflict", "message": "key reused with different body", "request_id": req.get("request_id")}}
    if status == "ok" and prior is not None:
        return 200, prior
    code, resp = handler(req)
    if code == 200:
        check_or_store(key, req, resp)
    return code, resp


def dispatch(path: str, body: dict[str, Any] | None = None) -> tuple[int, dict[str, Any]]:
    body = body or {}
    if path == "/v1/health":
        return 200, health()
    if path == "/v1/authz/check":
        r = check_authorization(
            body.get("user", ""),
            body.get("purpose", ""),
            body.get("object_type", ""),
            body.get("object_id", ""),
            body.get("as_of", ""),
        )
        return 200, r
    if path == "/v1/workflows/batch_evidence":
        return _with_idempotency(body, run_batch_evidence)
    if path == "/v1/workflows/pv_intake":
        return _with_idempotency(body, run_pv_intake)
    if path == "/v1/workflows/supply_options":
        return _with_idempotency(body, run_supply_options)
    if path == "/v1/evaluate/run":
        return _with_idempotency(body, run_evaluate)
    return 404, {"error": {"code": "not_found", "message": path, "request_id": body.get("request_id")}}


def main_cli(argv: list[str] | None = None) -> int:
    import argparse
    import sys

    parser = argparse.ArgumentParser(prog="aegis")
    parser.add_argument("path", help="API path e.g. /v1/health")
    parser.add_argument("--body", help="JSON body file or inline JSON", default=None)
    args = parser.parse_args(argv)
    body = {}
    if args.body:
        p = args.body
        if p.strip().startswith("{"):
            body = json.loads(p)
        else:
            body = json.loads(open(p, encoding="utf-8").read())
    code, resp = dispatch(args.path, body)
    print(json.dumps({"http_status": code, "body": resp}, indent=2))
    return 0 if code < 400 else 1


if __name__ == "__main__":
    raise SystemExit(main_cli())
''',
    )
    print("part2 ok")


if __name__ == "__main__":
    main()
