"""Live failure demonstrations for Phase 8 defence.

Run: PYTHONPATH=submission python submission/scripts/run_defence_failure_demos.py

Writes machine-readable results under phases/08_defence/failure_demo_results.csv
and prints a panel-friendly summary. Does not mutate challenge evidence.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBMISSION = ROOT / "submission"
sys.path.insert(0, str(SUBMISSION))

from src.app_api import dispatch  # noqa: E402
from src.ports.llm import call_count, reset_call_count  # noqa: E402
from src.workflows.batch import run_batch_evidence  # noqa: E402
from src.workflows.pv import run_pv_intake  # noqa: E402
from src.workflows.supply import run_supply_options  # noqa: E402

OUT = (
    SUBMISSION
    / "artefacts"
    / "phases"
    / "08_defence"
    / "failure_demo_results.csv"
)
AS_OF = "2026-08-07T00:00:00Z"


def _row(demo_id: str, title: str, expected: str, ok: bool, detail: str) -> dict[str, str]:
    return {
        "demo_id": demo_id,
        "title": title,
        "expected_fail_closed": expected,
        "observed_pass": "yes" if ok else "no",
        "detail": detail,
    }


def main() -> int:
    rows: list[dict[str, str]] = []

    # D1 — revoked contractor with cache lag
    code, body = dispatch(
        "/v1/workflows/batch_evidence",
        {
            "request_id": "def-d1",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": AS_OF,
            "user": "contractor_77",
            "mode": "deterministic_offline",
            "idempotency_key": "def-d1-key",
        },
    )
    ok = code == 403
    rows.append(
        _row(
            "D1",
            "AuthZ revoke beats cache (INJ-067)",
            "HTTP 403 deny; no pack",
            ok,
            f"http={code}; keys={list(body.keys())}",
        )
    )

    # D2 — prohibited disposition
    code, body = dispatch(
        "/v1/workflows/batch_evidence",
        {
            "request_id": "def-d2",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": AS_OF,
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "batch_disposition": "release",
            "idempotency_key": "def-d2-key",
        },
    )
    ok = code in {409, 422}
    rows.append(
        _row(
            "D2",
            "Batch disposition rejected",
            "422/409 contract_violation",
            ok,
            f"http={code}; error={body.get('error', {}).get('code')}",
        )
    )

    # D3 — reservation / side effect
    code, body = dispatch(
        "/v1/workflows/supply_options",
        {
            "request_id": "def-d3",
            "event_id": "SE-001",
            "purpose": "supply_options",
            "as_of": AS_OF,
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "create_reservation": True,
            "idempotency_key": "def-d3-key",
        },
    )
    ok = code in {409, 422}
    rows.append(
        _row(
            "D3",
            "Supply reservation blocked",
            "409/422 side_effect_blocked",
            ok,
            f"http={code}; error={body.get('error', {}).get('code')}",
        )
    )

    # D4 — AI-disabled narrator kill switch
    code, body = dispatch(
        "/v1/workflows/batch_evidence",
        {
            "request_id": "def-d4",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": AS_OF,
            "user": "qp_eu_1",
            "mode": "ai_disabled",
            "narrator": True,
            "idempotency_key": "def-d4-key",
        },
    )
    ok = code == 503
    rows.append(
        _row(
            "D4",
            "AI-disabled refuses narrator",
            "HTTP 503 mode_violation",
            ok,
            f"http={code}; error={body.get('error', {}).get('code')}",
        )
    )

    # D5 — happy path still works (contrast)
    reset_call_count()
    code, resp = run_batch_evidence(
        {
            "request_id": "def-d5",
            "batch_id": "NCB204-B24071",
            "purpose": "batch_evidence",
            "as_of": AS_OF,
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "def-d5-key",
        }
    )
    ok = (
        code == 200
        and resp.get("execution_status") == "not_executed"
        and call_count() == 0
        and "batch_disposition" not in resp
    )
    rows.append(
        _row(
            "D5",
            "Entitled assist pack (contrast)",
            "200; not_executed; LLM=0; no disposition",
            ok,
            f"http={code}; readiness={resp.get('readiness_state')}; llm={call_count()}",
        )
    )

    # D6 — PV no finals / no auto-merge
    code, resp = run_pv_intake(
        {
            "request_id": "def-d6",
            "case_ids": ["PV-1001", "PV-1014"],
            "purpose": "pv_intake",
            "as_of": AS_OF,
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "def-d6-key",
        }
    )
    finals = {"seriousness", "causality", "reportability"} & set(resp.keys())
    auto = any(c.get("auto_merged") for c in resp.get("duplicate_candidates", []))
    ok = code == 200 and not finals and not auto
    rows.append(
        _row(
            "D6",
            "PV intake no finals / no auto-merge",
            "200; no final fields; auto_merged=false",
            ok,
            f"http={code}; finals={sorted(finals)}; auto={auto}",
        )
    )

    # D7 — evaluate hard gates
    code, resp = dispatch(
        "/v1/evaluate/run",
        {
            "request_id": "def-d7",
            "suite": "contracts",
            "fixture_ids": ["PUB-01"],
            "user": "qp_eu_1",
            "purpose": "evaluate",
            "as_of": AS_OF,
            "idempotency_key": "def-d7-key",
        },
    )
    ok = code == 200 and resp.get("ready_blocked") is False
    rows.append(
        _row(
            "D7",
            "Evaluate hard gates green",
            "ready_blocked=false",
            ok,
            f"http={code}; ready_blocked={resp.get('ready_blocked')}",
        )
    )

    # D8 — supply happy path no side effects
    code, resp = run_supply_options(
        {
            "request_id": "def-d8",
            "event_id": "SE-001",
            "purpose": "supply_options",
            "as_of": AS_OF,
            "user": "qp_eu_1",
            "mode": "deterministic_offline",
            "idempotency_key": "def-d8-key",
        }
    )
    ok = code == 200 and resp.get("no_side_effects") is True
    rows.append(
        _row(
            "D8",
            "Supply options no_side_effects",
            "200; no_side_effects=true",
            ok,
            f"http={code}; no_side_effects={resp.get('no_side_effects')}",
        )
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "demo_id",
                "title",
                "expected_fail_closed",
                "observed_pass",
                "detail",
            ],
        )
        w.writeheader()
        w.writerows(rows)

    print("=== AEGIS Phase 8 — Live failure / control demonstrations ===\n")
    all_ok = True
    for r in rows:
        mark = "PASS" if r["observed_pass"] == "yes" else "FAIL"
        if r["observed_pass"] != "yes":
            all_ok = False
        print(f"[{mark}] {r['demo_id']} {r['title']}")
        print(f"       expected: {r['expected_fail_closed']}")
        print(f"       detail:   {r['detail']}\n")
    print(f"Results CSV: {OUT}")
    print(json.dumps({"all_demos_pass": all_ok, "count": len(rows)}, indent=2))
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
