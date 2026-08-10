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
