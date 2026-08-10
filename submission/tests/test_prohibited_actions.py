#!/usr/bin/env python3
"""Stage 4 prohibited-action and security control tests (stdlib only)."""
from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
CONTRACTS = ROOT / "evaluation" / "contracts"
SAMPLES = ROOT / "evaluation" / "contract_samples"
KNOWLEDGE = ROOT / "knowledge"


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _validate(value, schema, path="$"):
    """Minimal schema checks aligned with tools/test_contracts.py."""
    errors = []
    if "$ref" in schema:
        target = _load_json(CONTRACTS / schema["$ref"])
        return _validate(value, target, path)
    typ = schema.get("type")
    if isinstance(typ, list):
        ok = any(
            (t == "null" and value is None) or (t == "string" and isinstance(value, str))
            for t in typ
        )
        if not ok:
            return [f"{path}: wrong type"]
    elif typ == "object" and not isinstance(value, dict):
        return [f"{path}: expected object"]
    elif typ == "array" and not isinstance(value, list):
        return [f"{path}: expected array"]
    elif typ == "string" and not isinstance(value, str):
        return [f"{path}: expected string"]
    elif typ == "boolean" and not isinstance(value, bool):
        return [f"{path}: expected boolean"]
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: not in enum")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: too short")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: pattern mismatch")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: too few items")
        for i, v in enumerate(value):
            errors += _validate(v, schema.get("items", {}), f"{path}[{i}]")
    if isinstance(value, dict):
        for req in schema.get("required", []):
            if req not in value:
                errors.append(f"{path}: missing {req}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for k in value:
                if k not in props:
                    errors.append(f"{path}: additional property {k}")
        for k, v in value.items():
            if k in props:
                errors += _validate(v, props[k], f"{path}.{k}")
    return errors


def _csv_rows(name: str):
    with (DATA / name).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def authorize(user: str, entitlements: list[dict]) -> str:
    """IAM is authoritative; cached gateway alone cannot allow."""
    row = next((r for r in entitlements if r.get("user") == user), None)
    if row is None:
        return "deny"
    if row.get("iam_state") != "active":
        return "deny"
    return "allow"


def tool_allowed(manifest: dict) -> bool:
    """Reject unsigned/poisoned tools that request disposition writes."""
    perms = manifest.get("permissions") or []
    if any("disposition" in p and "write" in p for p in perms):
        return False
    if manifest.get("postAction"):
        return False
    if manifest.get("signature") in (None, "", "missing"):
        # Allow-list posture: require signature for any tool in assessed mode
        if perms:
            return False
    return True


def knowledge_may_instruct(trust: str, status: str) -> bool:
    return trust == "approved" and status == "approved"


def model_load_allowed(artifact: dict) -> bool:
    if artifact.get("signature") in (None, "", "missing"):
        return False
    return artifact.get("deployed_hash") == artifact.get("registry_hash")


class ProhibitedActionTests(unittest.TestCase):
    def test_package_contract_suite_passes(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "test_contracts.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_negative_batch_disposition_rejected_by_schema(self):
        data = _load_json(SAMPLES / "negative_batch_prohibited.json")
        schema = _load_json(CONTRACTS / "batch_response.schema.json")
        errors = _validate(data, schema)
        self.assertTrue(any("additional property" in e for e in errors), errors)

    def test_negative_pv_prohibited_rejected_by_schema(self):
        data = _load_json(SAMPLES / "negative_pv_prohibited.json")
        schema = _load_json(CONTRACTS / "pv_response.schema.json")
        errors = _validate(data, schema)
        self.assertTrue(errors, "expected schema errors for prohibited PV fields")

    def test_negative_supply_side_effect_rejected_by_schema(self):
        data = _load_json(SAMPLES / "negative_supply_side_effect.json")
        schema = _load_json(CONTRACTS / "supply_response.schema.json")
        errors = _validate(data, schema)
        self.assertTrue(errors, "expected schema errors for supply side effects")

    def test_stale_entitlement_denied(self):
        rows = _csv_rows("users_entitlements.csv")
        self.assertEqual(authorize("contractor_77", rows), "deny")
        self.assertEqual(authorize("qp_eu_1", rows), "allow")

    def test_poisoned_tool_manifest_rejected(self):
        poisoned = _load_json(DATA / "tool_manifest_poisoned.json")
        self.assertFalse(tool_allowed(poisoned))
        starter = _load_json(ROOT / "starter" / "api_samples" / "tool_manifest_poisoned.json")
        self.assertFalse(tool_allowed(starter))
        approved = _load_json(ROOT / "starter" / "api_samples" / "tool_manifest_approved.json")
        # Approved sample must not request disposition write; signature may still be required
        self.assertFalse(
            any("disposition" in p and "write" in p for p in approved.get("permissions", []))
        )

    def test_untrusted_knowledge_not_instruction(self):
        rows = _csv_rows("knowledge_catalog.csv")
        untrusted = [r for r in rows if r.get("trust") == "untrusted"]
        self.assertTrue(untrusted, "expected untrusted knowledge rows")
        for r in untrusted:
            self.assertFalse(knowledge_may_instruct(r["trust"], r["status"]))
        # Malicious file exists as challenge content but must not be instructable
        self.assertTrue((KNOWLEDGE / "MALICIOUS_SUPPLIER_DEVIATION.md").is_file())
        fake = next(r for r in rows if "FAKE_PV" in r.get("file", ""))
        self.assertFalse(knowledge_may_instruct(fake["trust"], fake["status"]))

    def test_model_hash_mismatch_blocked(self):
        rows = _csv_rows("model_artifacts.csv")
        bad = next(r for r in rows if r.get("model_id") == "GXP-SUM-1")
        self.assertFalse(model_load_allowed(bad))


if __name__ == "__main__":
    raise SystemExit(unittest.main(verbosity=2))
