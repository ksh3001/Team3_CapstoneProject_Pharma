# Architecture Decision Register

> Phase 3. ≥10 ADRs freezing forks before POC. Options ≥3 each; prohibited paths absent by construction where possible.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Architecture–build lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP; Security; Domain |
| Status | Draft |
| Related requirements / ADRs | DEC-010/012/020/022/030–041; artefacts 05–10, 12 |

## Purpose

Record architecture decisions that keep the assist advisory, offline-capable, and fail-closed — with measurable NFRs and revisit triggers.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | artefacts 05–09 | Domain + KG + requirements |
| E-002 | evaluation/contracts | Fail-closed schemas |
| E-003 | data/api_contract_versions.csv | LIMS v1/v2, E2B |
| E-004 | SKILL_AI_Python_scaffolding / ai-engineering-foundations | Typed contracts, ports |
| E-005 | domain-and-architecture skill | ADR quality gate |

## 1. ADR index

| ADR | Title | Status | C4 level | Related INV/POL |
|---|---|---|---|---|
| ADR-031 | Relational evidence mesh (no KG DB v1) | Accepted | Container | FR-K1; DEC-020 |
| ADR-032 | Adopt package JSON Schema contracts v1 | Accepted | Code | NFR-3; DEC-030 |
| ADR-033 | AuthZ at execution time | Accepted | Component | INV-08 |
| ADR-034 | Signed tool allowlist; assessed mode no writes | Accepted | Component | INV-03/05 |
| ADR-035 | Knowledge instruction eligibility filter | Accepted | Component | INV-06; DEC-022 |
| ADR-036 | Deterministic core before optional LLM | Accepted | Container | FR-T2; DEC-010 |
| ADR-037 | Read-only integrations (no source writes) | Accepted | System | INV-03/05 |
| ADR-038 | Dual ACL for LIMS v1/v2 (+ E2B/IDMP maps) | Accepted | Code | INV-02; artefact 12 |
| ADR-039 | Evidence_item provenance mandatory | Accepted | Code | INV-01 |
| ADR-040 | Supply draft-only / no_side_effects by construction | Accepted | Code | INV-05 |
| ADR-041 | Single-package offline deploy for v1 | Accepted | Container | NFR-1 |

## ADR-031 — Relational evidence mesh (no KG DB v1)

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Domain + Architecture |
| Context | Multi-hop genealogy/recall exist, but vignette scale + 40h + offline DoD |
| Options | (A) Property graph DB (B) Hybrid GraphRAG (C) Relational mesh + detectors ← (D) Pure vector RAG |
| Decision | (C) — see artefact 08 / DEC-020 |
| NFRs | Offline join p95 &lt; 2s on vignette; zero graph ops dependency |
| Security / privacy | Smaller attack surface than graph platform |
| Operational | SQL/CSV loaders; closure table spike only if revisit |
| Guardrails | INV-07 preserve declared exceptions |
| Validation | Anchor fixtures; no KG in dependency lockfile |
| Revisit | When multi-hop recall queries exceed 2 hops on production volumes OR join p95 &gt; 5s |

## ADR-032 — Adopt package JSON Schema contracts v1

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Architecture + Evaluation |
| Context | Need fail-closed I/O before implementation |
| Options | (A) Free-form JSON (B) OpenAPI-only (C) Package schemas + additionalProperties false ← |
| Decision | (C); no challenge schema edits; overlays only with compat tests (DEC-030) |
| NFRs | 100% positives valid; 100% prohibited samples invalid |
| Security | Blocks disposition/reportability/reservation fields |
| Operational | `tools/test_contracts.py` in CI/preflight |
| Guardrails | NFR-3 |
| Validation | Package suite green; submission schema tests green |
| Revisit | When a new allowed field is required by scored workflow |

## ADR-033 — AuthZ at execution time

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Security |
| Context | Entitlement lag / revoked roles (INJ-067 themes) |
| Options | (A) Role string in request only (B) Cached allow forever (C) Check at execution + max cache age ← |
| Decision | (C); deny on revoked or cache_age &gt; max |
| NFRs | AuthZ decision latency p95 &lt; 200ms offline fixture; deny must win |
| Security | Prevents stale allow |
| Operational | Audit reason codes |
| Guardrails | INV-08 |
| Validation | `test_stale_iam_denied` (red until Phase 5) |
| Revisit | When federated IAM RTT p95 &gt; 500ms → redesign cache with revalidation |

## ADR-034 — Signed tool allowlist; assessed mode no writes

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Security + Architecture |
| Context | Tool poison / blind exec anti-patterns |
| Options | (A) Any function-calling tool (B) Allowlist unsigned (C) Signed manifest + assessed no side effects ← |
| Decision | (C) |
| NFRs | 0 write-tool executions in assessed runs |
| Security | Contained ACI |
| Operational | Manifest file in submission; signature check stub→real |
| Guardrails | INV-03/05 |
| Validation | `test_unsigned_tool_denied`, `test_write_tool_denied_in_assessed_mode` |
| Revisit | If production needs controlled write tools — separate ADR + HITL gate |

## ADR-035 — Knowledge instruction eligibility filter

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Security + Domain |
| Context | Untrusted/outdated SOP-as-instruction |
| Options | (A) Equal-trust all MD (B) Trust score soft filter (C) Hard eligibility: approved + approved/local_approved ← |
| Decision | (C) = DEC-022 |
| NFRs | 0 instruction uses of untrusted/superseded docs in eval suite |
| Security | Prompt-injection containment at retrieval edge |
| Operational | knowledge_trust_catalogue.csv as SoT |
| Guardrails | INV-06 |
| Validation | `test_untrusted_sop_not_instruction_eligible` |
| Revisit | When catalog adds new statuses — update allowlist explicitly |

## ADR-036 — Deterministic core before optional LLM

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Architecture |
| Context | Model flaky; AI-disabled continuity required |
| Options | (A) LLM-first agent (B) LLM required for conflicts (C) Deterministic core + optional port ← |
| Decision | (C); ports & adapters; Pydantic contracts when model used |
| NFRs | AI-disabled path completes all 3 workflows offline |
| Security | Model never sole authority |
| Operational | Disable adapter via config |
| Guardrails | DEC-010/011 |
| Validation | Continuity drill Phase 6/7 |
| Revisit | If deterministic detectors miss &gt;X% scored injects — expand rules before model |

## ADR-037 — Read-only integrations

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Architecture + GxP |
| Context | Source writes would create regulated side effects |
| Options | (A) Bidirectional sync (B) Compensating write API (C) Read-only adapters ← |
| Decision | (C); PROHIBITED edges in C4 |
| NFRs | Architecture/dependency check: 0 source-write clients in assessed mode |
| Security | Reduces blast radius |
| Operational | Exports/fixtures for offline |
| Guardrails | INV-03/05 |
| Validation | Static import allowlist + contract negatives |
| Revisit | Never for assessed POC; production write-back needs separate validated system |

## ADR-038 — Dual ACL for LIMS v1/v2 (+ E2B / IDMP)

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Domain + Architecture |
| Context | api_contract_versions: v1 unit/status vs v2 ucum_code/lifecycleState |
| Options | (A) Normalize silently to one shape (B) Support only v2 (C) Versioned ACL preserving source fields + mapping approval ← |
| Decision | (C); unapproved mappings → contradiction (INV-02) |
| NFRs | Both versions load without silent unit convert |
| Security / privacy | Preserve source semantics for audit |
| Operational | Mapping table + tests per version |
| Guardrails | INV-02 |
| Validation | Integration contract tests (artefact 12); INJ-024 fixture |
| Revisit | When LIMS v3 appears — new ACL row + tests |

## ADR-039 — Evidence_item provenance mandatory

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Domain + GxP |
| Context | Citation ≠ provenance; DI expectations |
| Options | (A) Free-text citations (B) Optional integrity (C) Mandatory evidence_item schema ← |
| Decision | (C) |
| NFRs | Every material fact in scored outputs cites evidence_item |
| Security | Tamper-evident hash |
| Operational | Hasher in loader |
| Guardrails | INV-01 |
| Validation | Schema + TEVV citation checks |
| Revisit | If hash algorithm changes — migrate with dual-hash period |

## ADR-040 — Supply draft-only / no_side_effects by construction

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Architecture + Supply governance |
| Context | Reservation/allocate anti-pattern |
| Options | (A) Soft warning on reservation_id (B) Allow side effects with confirm (C) Schema const + no reservation property ← |
| Decision | (C) |
| NFRs | 0 reservations created in assessed runs |
| Security | Side-effect free |
| Operational | Options status const draft |
| Guardrails | INV-05 |
| Validation | negative_supply_side_effect.json |
| Revisit | Only if a separately validated execution system is integrated (out of POC) |

## ADR-041 — Single-package offline deploy for v1

| Field | Entry |
|---|---|
| Status / Date / Owners | Accepted / 2026-08-10 / Ops + Architecture |
| Context | Clean-room / offline DoD |
| Options | (A) Multi-service k8s (B) Cloud-only API (C) Single local package ← |
| Decision | (C) |
| NFRs | setup→test→evaluate on disconnected machine |
| Security | No cloud secret dependency |
| Operational | scripts/setup|run|test|evaluate|reset |
| Guardrails | NFR-1 |
| Validation | Clean-room checklist Phase 7 |
| Revisit | When availability SLO requires HA multi-node (RTO &lt; 1h multi-site) |

## 2–7. Cross-cutting (summary)

| Topic | Response |
|---|---|
| Forces | Advisory-only; offline; deliberate contradictions; 40h |
| Consequences (+) | Testable boundaries; simpler ops |
| Consequences (−) | Less autonomy; more human minutes |
| Risks introduced | Stub gates until Phase 5; absolute lead-time still open (A-011) |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-311 | Gap | Runtime gate implementation pending | Tests red | Architecture | Open |
| A-017 | Assumption | Prototype ADR set sufficient; production ADRs deferred | Defence depth | Architecture | Open |

## Traceability and acceptance

| Claim | Control | Test | Result |
|---|---|---|---|
| ≥10 ADRs | This register | Count ADR-031…041 = 11 | Met |
| Prohibited writes absent | ADR-034/037/040 | Schema + runtime tests | Schema PASS; runtime RED |
| Guardrails → INV | Each ADR | Peer review | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | Architecture peer | Hour-18 review pending | | |
