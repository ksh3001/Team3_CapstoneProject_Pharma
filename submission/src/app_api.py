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
