# Inject Evidence Register (Phase 2)

| Field | Entry |
|---|---|
| Source | `data/injects.json` + `data/inject_evidence_map.csv` |
| Count | **84** (INJ-001…INJ-084) |
| Machine-readable | [`inject_evidence_register.csv`](inject_evidence_register.csv) |
| Status | Initial assessment — most rows `UNASSESSED`; specials enriched from package facts |

## Column contract

`inject_id, objects, source_path, authority, effective_at, jurisdiction, units, terminology, time_precision, lineage, access_state, validation_state, contradiction_refs, abstention_triggers` (+ dimension/title/status/summary).

## Dimension coverage

| Dimension | Count |
|---|---:|
| D01 | 6 |
| D02 | 6 |
| D03 | 8 |
| D04 | 8 |
| D05 | 8 |
| D06 | 8 |
| D07 | 6 |
| D08 | 8 |
| D09 | 6 |
| D10 | 6 |
| D11 | 4 |
| D12 | 4 |
| D13 | 6 |

## High-signal rows (enriched)

| Inject | Objects | Contradiction / abstention |
|---|---|---|
| INJ-001 | board_request;product | BR-01 vs completeness pressure / if speed forces skip of unresolved conflict |
| INJ-024 | lab_result;interface_mapping | lab_results LR-88 / interface_mappings approved=no / silent_unit_conversion |
| INJ-037 | icsr_case;safety_receipt | multiple receipt clocks / disagreeing clocks without dual-cite |
| INJ-038 | icsr_case | duplicate_candidates fuzzy scores / below-threshold auto-merge |
| INJ-065 | knowledge_doc | — / untrusted doc used as instruction |
| INJ-066 | tool_manifest | — / unsigned/poisoned tool |
| INJ-067 | user_entitlement;access_cache | — / cache-only allow |
| INJ-071 | package_evidence | — / automation bias incomplete summary |
| INJ-072 | icsr_case | — / language subgroup untested |
| INJ-077 | cost_model | cost_model review hours=0 / TCO without review hours |

## Policy

Never silently merge conflicting evidence. Dual-cite; abstain when identity/unit/time/authority unresolved. See `CONFLICT_RESOLUTION_POLICY.md`.
