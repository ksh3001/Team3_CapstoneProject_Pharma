"""Build Phase 2 inject evidence register + PUB map from package data."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "submission" / "artefacts" / "phases" / "02_domain_evidence"
OUT.mkdir(parents=True, exist_ok=True)

# Known concrete contradiction / abstention cues (package facts)
SPECIAL = {
    "INJ-001": {"contradiction_refs": "BR-01 vs completeness pressure", "abstention_triggers": "if speed forces skip of unresolved conflict"},
    "INJ-037": {"objects": "icsr_case;safety_receipt", "time_precision": "mixed datetime/date", "contradiction_refs": "multiple receipt clocks", "abstention_triggers": "disagreeing clocks without dual-cite"},
    "INJ-038": {"objects": "icsr_case", "contradiction_refs": "duplicate_candidates fuzzy scores", "abstention_triggers": "below-threshold auto-merge"},
    "INJ-065": {"objects": "knowledge_doc", "access_state": "untrusted_present", "abstention_triggers": "untrusted doc used as instruction"},
    "INJ-066": {"objects": "tool_manifest", "access_state": "poisoned_manifest", "abstention_triggers": "unsigned/poisoned tool"},
    "INJ-067": {"objects": "user_entitlement;access_cache", "access_state": "revoked_with_active_cache", "abstention_triggers": "cache-only allow"},
    "INJ-071": {"abstention_triggers": "automation bias incomplete summary"},
    "INJ-072": {"terminology": "multilingual", "abstention_triggers": "language subgroup untested"},
    "INJ-077": {"contradiction_refs": "cost_model review hours=0", "abstention_triggers": "TCO without review hours"},
}

DIM_DEFAULTS = {
    "D01": {"jurisdiction": "Global/enterprise", "validation_state": "n/a_business"},
    "D02": {"jurisdiction": "site/functional", "validation_state": "n/a_process"},
    "D03": {"units": "may_apply", "terminology": "product/batch IDs", "validation_state": "data_quality"},
    "D04": {"time_precision": "as_of_critical", "validation_state": "temporal"},
    "D05": {"access_state": "authz_sensitive", "validation_state": "security"},
    "D06": {"validation_state": "gxp_validation_inventory"},
    "D07": {"validation_state": "model_eval"},
    "D08": {"validation_state": "privacy"},
    "D09": {"validation_state": "privacy_hf"},
    "D10": {"validation_state": "security_adversarial"},
    "D11": {"validation_state": "ops_continuity"},
    "D12": {"validation_state": "finops_vendor"},
}


def infer_objects(evidence: str, title: str) -> str:
    e = (evidence or "").lower()
    objs = []
    mapping = [
        ("board_requests", "board_request"),
        ("lab_results", "lab_result"),
        ("interface_mapping", "interface_mapping"),
        ("inventory", "inventory_lot"),
        ("icsr", "icsr_case"),
        ("safety_receipt", "safety_receipt"),
        ("adverse_event", "adverse_event"),
        ("users_entitlement", "user_entitlement"),
        ("access_cache", "access_cache"),
        ("knowledge", "knowledge_doc"),
        ("validation_inventory", "validation_record"),
        ("system_inventory", "system_record"),
        ("duplicate_candidate", "duplicate_candidate"),
        ("genealogy", "batch_genealogy"),
        ("shipment", "shipment"),
        ("tool_manifest", "tool_manifest"),
        ("cost_model", "cost_model"),
        ("portfolio", "product"),
        ("stakeholder", "stakeholder"),
        ("decision_rights", "decision_right"),
        ("ai_use_boundar", "ai_use_boundary"),
        ("continuity", "continuity_requirement"),
        ("kpi_conflict", "kpi"),
    ]
    for needle, obj in mapping:
        if needle in e:
            objs.append(obj)
    if not objs:
        objs.append("package_evidence")
    return ";".join(dict.fromkeys(objs))


def authority_for(evidence: str, dimension: str) -> str:
    e = (evidence or "").lower()
    if "knowledge" in e or e.endswith(".md"):
        return "document_control_mixed_trust"
    if "users_entitlement" in e or "access_cache" in e:
        return "IAM_vs_gateway_cache"
    if "lab_results" in e or "lims" in e:
        return "LIMS/QC"
    if "inventory" in e or "shipment" in e:
        return "WMS/supply"
    if "icsr" in e or "safety" in e or "adverse" in e:
        return "Safety_DB/PV"
    if "board_requests" in e:
        return "Board"
    if "validation" in e:
        return "Quality_validation"
    if dimension in {"D05", "D10"}:
        return "Security/CISO"
    return "source_system_as_packaged"


def main() -> None:
    injects = json.loads((ROOT / "data" / "injects.json").read_text(encoding="utf-8"))
    emap = {
        r["inject_id"]: r
        for r in csv.DictReader((ROOT / "data" / "inject_evidence_map.csv").open(encoding="utf-8"))
    }

    fields = [
        "inject_id",
        "dimension",
        "title",
        "objects",
        "source_path",
        "authority",
        "effective_at",
        "jurisdiction",
        "units",
        "terminology",
        "time_precision",
        "lineage",
        "access_state",
        "validation_state",
        "contradiction_refs",
        "abstention_triggers",
        "participant_status",
        "scenario_summary",
    ]

    rows = []
    for inj in sorted(injects, key=lambda x: x["id"]):
        iid = inj["id"]
        dim = inj.get("dimension") or ""
        evidence = inj.get("evidence") or emap.get(iid, {}).get("evidence_sources", "")
        ddef = DIM_DEFAULTS.get(dim, {})
        special = SPECIAL.get(iid, {})
        row = {
            "inject_id": iid,
            "dimension": dim,
            "title": inj.get("title", ""),
            "objects": special.get("objects") or infer_objects(evidence, inj.get("title", "")),
            "source_path": evidence,
            "authority": special.get("authority") or authority_for(evidence, dim),
            "effective_at": special.get("effective_at") or "as_packaged_or_unknown",
            "jurisdiction": special.get("jurisdiction") or ddef.get("jurisdiction", "unspecified"),
            "units": special.get("units") or ddef.get("units", "n/a_or_unknown"),
            "terminology": special.get("terminology") or ddef.get("terminology", "source_terms"),
            "time_precision": special.get("time_precision") or ddef.get("time_precision", "unknown"),
            "lineage": f"challenge:{evidence}" if evidence else "challenge:undeclared",
            "access_state": special.get("access_state") or ddef.get("access_state", "package_readable"),
            "validation_state": special.get("validation_state") or ddef.get("validation_state", "UNASSESSED"),
            "contradiction_refs": special.get("contradiction_refs", ""),
            "abstention_triggers": special.get("abstention_triggers", "unresolved_identity_unit_time_authority"),
            "participant_status": emap.get(iid, {}).get("participant_status", "UNASSESSED"),
            "scenario_summary": (inj.get("scenario") or "")[:240],
        }
        # Concrete package facts for unit inject themes
        if "unit" in (inj.get("title") or "").lower() or "LR-88" in (inj.get("scenario") or ""):
            row["units"] = "conflict_possible"
            row["contradiction_refs"] = row["contradiction_refs"] or "lab_results LR-88 / interface_mappings approved=no"
            row["abstention_triggers"] = "silent_unit_conversion"
        if "quarantine" in (inj.get("scenario") or "").lower() or "quarantine" in (inj.get("title") or "").lower():
            row["contradiction_refs"] = row["contradiction_refs"] or "inventory quarantine vs available"
            row["abstention_triggers"] = "quarantine_as_available"
        rows.append(row)

    csv_path = OUT / "inject_evidence_register.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    # Markdown summary (not all 84 rows fully duplicated — index + pointer)
    md = [
        "# Inject Evidence Register (Phase 2)",
        "",
        "| Field | Entry |",
        "|---|---|",
        "| Source | `data/injects.json` + `data/inject_evidence_map.csv` |",
        "| Count | **84** (INJ-001…INJ-084) |",
        "| Machine-readable | [`inject_evidence_register.csv`](inject_evidence_register.csv) |",
        "| Status | Initial assessment — most rows `UNASSESSED`; specials enriched from package facts |",
        "",
        "## Column contract",
        "",
        "`inject_id, objects, source_path, authority, effective_at, jurisdiction, units, terminology, time_precision, lineage, access_state, validation_state, contradiction_refs, abstention_triggers` (+ dimension/title/status/summary).",
        "",
        "## Dimension coverage",
        "",
        "| Dimension | Count |",
        "|---|---:|",
    ]
    from collections import Counter

    c = Counter(r["dimension"] for r in rows)
    for d, n in sorted(c.items()):
        md.append(f"| {d} | {n} |")
    md += [
        "",
        "## High-signal rows (enriched)",
        "",
        "| Inject | Objects | Contradiction / abstention |",
        "|---|---|---|",
    ]
    for r in rows:
        if r["contradiction_refs"] or r["inject_id"] in SPECIAL:
            md.append(
                f"| {r['inject_id']} | {r['objects']} | {r['contradiction_refs'] or '—'} / {r['abstention_triggers']} |"
            )
    md += [
        "",
        "## Policy",
        "",
        "Never silently merge conflicting evidence. Dual-cite; abstain when identity/unit/time/authority unresolved. See `CONFLICT_RESOLUTION_POLICY.md`.",
        "",
    ]
    (OUT / "inject_evidence_register.md").write_text("\n".join(md), encoding="utf-8")

    # PUB map
    pubs = list(csv.DictReader((ROOT / "evaluation" / "PUBLIC_FIXTURE_INDEX.csv").open(encoding="utf-8")))
    pub_fields = [
        "scenario_id",
        "workflow",
        "fixture_path",
        "response_contract",
        "aegis_workflow",
        "related_inject_themes",
        "phase2_notes",
    ]
    pub_rows = []
    theme = {
        "batch": "INJ unit/genealogy/authz/knowledge trust (e.g. D03/D05/D10); LR-88; contractor_77",
        "pv": "INJ clocks/duplicates/multilingual (e.g. INJ-037/038/072); K-999",
        "supply": "INJ quarantine/reservation/shortage ethics; inventory quality_status",
    }
    for p in pubs:
        wf = (p.get("workflow") or "").lower()
        aegis = {"batch": "batch_evidence", "pv": "pv_intake", "supply": "supply_options"}.get(wf, wf)
        pub_rows.append(
            {
                "scenario_id": p.get("scenario_id"),
                "workflow": p.get("workflow"),
                "fixture_path": p.get("fixture_path"),
                "response_contract": p.get("response_contract"),
                "aegis_workflow": aegis,
                "related_inject_themes": theme.get(wf, "see inject register by dimension"),
                "phase2_notes": "Map for Phase 6 TEVV; no expected answers in package",
            }
        )
    with (OUT / "pub_fixture_map.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=pub_fields)
        w.writeheader()
        w.writerows(pub_rows)

    pub_md = [
        "# Public Fixture Map (PUB-01…15)",
        "",
        "Source: `evaluation/PUBLIC_FIXTURE_INDEX.csv`.",
        "",
        "| Scenario | Package workflow | AEGIS workflow | Contract |",
        "|---|---|---|---|",
    ]
    for r in pub_rows:
        pub_md.append(
            f"| {r['scenario_id']} | {r['workflow']} | {r['aegis_workflow']} | `{Path(r['response_contract']).name}` |"
        )
    pub_md.append("")
    pub_md.append("Machine-readable: [`pub_fixture_map.csv`](pub_fixture_map.csv).")
    (OUT / "pub_fixture_map.md").write_text("\n".join(pub_md), encoding="utf-8")

    print("wrote", csv_path)
    print("rows", len(rows), "pubs", len(pub_rows))


if __name__ == "__main__":
    main()
