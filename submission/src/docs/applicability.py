from __future__ import annotations
from typing import Any
from src.evidence.csv_acl import read_csv

INSTRUCTION_BLOCK = {"untrusted", "draft", "superseded"}


def catalog_rows() -> list[dict[str, str]]:
    return read_csv("knowledge_catalog.csv")


def classify_document(row: dict[str, str]) -> dict[str, Any]:
    status = (row.get("status") or "").lower()
    trust = (row.get("trust") or "").lower()
    instruction_applicable = status == "approved" and trust == "approved"
    quarantined = (status in INSTRUCTION_BLOCK or trust in INSTRUCTION_BLOCK) and not instruction_applicable
    return {
        "doc_id": row.get("doc_id"),
        "file": row.get("file"),
        "status": row.get("status"),
        "trust": row.get("trust"),
        "authority": row.get("authority"),
        "jurisdiction": row.get("jurisdiction"),
        "instruction_applicable": instruction_applicable,
        "quarantined": quarantined,
    }


def applicable_documents(as_of: str | None = None) -> list[dict[str, Any]]:
    return [classify_document(r) for r in catalog_rows()]


def assert_not_instruction_authority(doc_id: str) -> bool:
    for d in applicable_documents():
        if d["doc_id"] == doc_id:
            return not d["instruction_applicable"]
    return True
