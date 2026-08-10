# DDD Context Map

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `case/SOURCE_SYSTEM_FACT_PACK.md`; `knowledge/IDMP_MASTER_DATA_GOVERNANCE.md` (K-015); INJ-005, INJ-008, INJ-024, INJ-045 |

## Purpose

Defines the bounded contexts across NTG's brownfield estate, where identity genuinely conflicts (not just looks inconsistent), and where the AI evidence-reconciliation capability sits relative to those contexts — required before any architecture (`10_C4_ARCHITECTURE`) or ontology (`07_ONTOLOGY_SEMANTIC_LAYER`) work. Accountable owner: capstone team. Completion criteria: every named identity conflict traces to a concrete evidence row; the reconciliation context's boundary (read-only, no system-of-record claim) is explicit, not implied.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-401 | `data/compounds.csv` | Compound register, undated | Code `BX-17` appears twice: source `BIOX`, structure_hash `abc91`, salt_form `mesylate`; source `NTG`, structure_hash `f0872`, salt_form `free_base` | Matches INJ-008 exactly — same local code, genuinely different structure/salt form, not a formatting inconsistency |
| E-402 | `data/substance_master.csv` | Substance register, undated | `SUB-0091` "nexoradine mesylate" (source RIM, status approved); `SUB-0092` "nexoradine" (source Research, status candidate) | Plausibly the substance-level counterpart to the E-401 salt-form split, but no explicit link field confirms this — treated as a hypothesis, not a fact (Gap R-401) |
| E-403 | `data/medicinal_products.csv` | Product register, undated | `NCB-204` (source RIM, strength "100 mg/10 mL", dose_form "concentrate_for_infusion", substance `SUB-204`); `NCB204-DE` (source ERP, strength "10 mg/mL", dose_form "solution", substance "NCB antibody" — free text, not a governed substance ID) | Matches INJ-045; the ERP row's substance field is not even a governed identifier, which is itself a data-governance finding, not only a strength mismatch |
| E-404 | `data/idmp_mappings.csv` | Mapping register, undated | `NCB204-DE` → `NCB-204`, mapping_status = `ambiguous_strength_presentation` | The mapping exists and is explicitly flagged unresolved by the source system itself — not something this team is discovering, it is disclosed as already-known-ambiguous |
| E-405 | `data/interface_mappings.csv` | Interface configuration, undated | Interface `CRO_LAB_TO_LIMS`: source_unit `mg/L`, target_unit `ug/mL`, conversion_rule `1:1_assumed`, approved = `no` | Matches INJ-024. Note on the underlying mathematics: 1 mg/L = 1 µg/mL by dimensional definition (mg/L and µg/mL are numerically equal), so a 1:1 rule is not necessarily numerically wrong for this specific unit pair — but `approved = no` means the mapping was never formally validated/signed off. The defect asserted here is the **absence of approval/change control**, not a proven numeric error; this distinction is preserved rather than collapsed into "the lab data is wrong" |
| E-406 | `data/product_master_aliases.csv` | Alias register, undated | Three aliases (`brand_alias_B`, `NCB204`, `NovaBio mAb`) all map to canonical `NCB-204` | This is governance done correctly per K-015 ("record aliases, source system") — presented as a positive counter-example to E-401/E-403/E-404, not another defect |
| E-407 | `data/controlled_vocabularies.csv` | Controlled vocabulary, version 2026-1 | `dose_form` `DF-001` = "concentrate for solution for infusion"; `route` `ROA-IV` = "intravenous use" | Candidate canonical ubiquitous-language terms; note E-403's RIM row uses "concentrate_for_infusion" (close but not identical string to DF-001's term) — treated as a near-match requiring explicit confirmation, not silently normalized |
| E-408 | `knowledge/IDMP_MASTER_DATA_GOVERNANCE.md` (K-015, approved 2026-04-08) | Synthetic NovaCura Global Policy | "Do not merge identity conflicts without stewardship evidence"; "Record aliases, source system and effective version" | Directly governs how this context map must treat E-401/E-403/E-404 — merging is explicitly prohibited without stewardship sign-off |
| E-409 | `data/organisations.csv` (`01_BUSINESS_CASE.md` E-206) | Organisation register | `NTG` (sponsor/MAH, DE), `BIOX` (acquired biotech, US), `CMO-IE` (contract manufacturer, IE) | Confirms BIOX is a distinct organisational source, consistent with E-401's `source_org` field being the actual identity-disambiguating attribute |

## 1. Ubiquitous language

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Is there a single canonical vocabulary today? | Partially — `controlled_vocabularies.csv` (E-407) exists and is versioned (2026-1), but source systems do not consistently use its exact terms: RIM's `medicinal_products.csv` uses "concentrate_for_infusion" (E-403) which is a near-match, not an exact match, to the governed term "concentrate for solution for infusion" (E-407). | Capstone team | E-407, E-403 |
| Decision on canonical terms | Adopt `controlled_vocabularies.csv` as the ubiquitous-language source of truth for dose form and route, but require an explicit, logged confirmation step before treating a near-match source string (e.g., E-403's RIM value) as equivalent to the governed term — never silently normalize, per E-408's "do not merge... without stewardship evidence" principle applied to terminology, not just identifiers. | Capstone team | E-407, E-408 |
| What term must NOT be conflated across contexts? | "Compound" (Discovery context, pre-substance, identified by `compound_code` + `source_org` + `structure_hash`, E-401) must not be conflated with "Substance" (Regulatory context, governed identifier, E-402) or "Medicinal Product" (Regulatory/Manufacturing context, E-403) — these are three distinct ubiquitous-language terms with three distinct identity rules, and E-401 shows what happens when a compound-level code is treated as if it were already a stable identifier. | Capstone team | E-401, E-402, E-403 |

## 2. Bounded contexts

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Discovery / Compound Registry context | Owns compound identity pre-substance-registration. Identity key: (`compound_code`, `source_org`, `structure_hash`) — not `compound_code` alone, because E-401 proves code alone is not unique across organisations. | Capstone team | E-401 |
| Regulatory / RIM context | Owns canonical substance and medicinal-product identity (`substance_master.csv`, `medicinal_products.csv` RIM row, `idmp_mappings.csv`, `product_master_aliases.csv`). This is the closest thing to a system-of-record for product identity, consistent with K-015. | Capstone team | E-402, E-403, E-406, E-408 |
| Manufacturing / ERP context | Owns local production-facing product representation (`medicinal_products.csv` ERP row, `recipes.csv`, `production_schedule.csv`) — explicitly a *local* view, not authoritative for global product identity (E-403's ERP row lacks a governed substance ID). | Capstone team | E-403 |
| Laboratory context | Owns lab result generation and instrument/interface configuration (`lab_results.csv`, `interface_mappings.csv`, `instruments.csv`). Includes external CRO labs as a distinct sub-context connected via interface, not merged (E-405). | Capstone team | E-405 |
| Quality context | Owns deviation, CAPA, change-control and validation-state data (per `02_DMAIC_WORKBOOK.md` E-201–E-205) — not re-derived here, cross-referenced. | Capstone team | `02_DMAIC_WORKBOOK.md` |
| Safety / Pharmacovigilance context | Owns ICSR case data, terminology versions, listedness sources — out of this artefact's detailed evidence pull; scope confirmed via `case/INTEGRATED_CASE.md` D06. | Capstone team | `case/INTEGRATED_CASE.md` D06 |
| Supply context | Owns inventory, shipments, cold-chain, serialization — scope confirmed via `case/INTEGRATED_CASE.md` D08. | Capstone team | `case/INTEGRATED_CASE.md` D08 |
| AI Evidence-Reconciliation context (this capstone's deliverable) | A new, narrow, **read-only downstream context** that consumes published evidence from all of the above via anti-corruption layers, and owns only its own citation/evidence-item output — never becomes a system of record for compound, substance, product, batch, case or inventory identity. This is a deliberate architectural constraint, not an oversight. | Capstone team | E-408; `01_BUSINESS_CASE.md` E-004 |

## 3. Aggregates and invariants

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Compound aggregate invariant | Identity = (`compound_code`, `source_org`) minimum, ideally plus `structure_hash`. Invariant: two rows with the same `compound_code` but different `source_org`/`structure_hash` are NEVER automatically the same aggregate instance (directly falsified by E-401 if assumed otherwise). | Capstone team | E-401 |
| Medicinal Product aggregate invariant | Canonical identity lives in the Regulatory/RIM context (`idmp_product`); local representations (ERP, distributor) are linked via `idmp_mappings.csv` with an explicit `mapping_status`. Invariant: a mapping with any non-"resolved"/non-clean status (e.g., E-404's `ambiguous_strength_presentation`) must never be treated as equivalent for release-relevant strength/presentation decisions until a steward closes it. | Capstone team | E-404, E-408 |
| Interface Mapping aggregate invariant | A unit/vocabulary conversion is not valid for downstream use until `approved = yes` (E-405) — this invariant holds regardless of whether the underlying arithmetic happens to be correct, because the governance failure (no approval/change-control record) is itself the defect being modeled. | Capstone team | E-405 |
| Alias aggregate (positive pattern) | `product_master_aliases.csv` (E-406) models a clean one-to-many alias-to-canonical relationship with no ambiguity flag — used as the target pattern that E-404's `idmp_mappings.csv` row should reach once stewarded. | Capstone team | E-406 |

## 4. Context relationships

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Discovery (BIOX) ↔ Discovery (NTG) | **Separate Ways** (DDD pattern) until explicit stewardship resolves the E-401 collision — no shared kernel is assumed, since the two `BX-17` rows are provably different chemical entities. | Capstone team | E-401, E-408 |
| Regulatory (RIM) → Manufacturing (ERP) | **Customer/Supplier**, RIM upstream: ERP's local product view is a downstream consumer of RIM identity, connected through `idmp_mappings.csv` — but the current state (E-404) shows the mapping itself is unresolved, so ERP cannot currently be treated as a Conformist to RIM without carrying that ambiguity forward. | Capstone team | E-403, E-404 |
| Laboratory (external CRO) → Laboratory (internal LIMS) | **Customer/Supplier** with an unapproved interface (E-405) — currently operating without the anti-corruption layer's approval gate actually enforced, which this context map treats as a defect to close (§5), not an acceptable current state. | Capstone team | E-405 |
| AI Evidence-Reconciliation → every domain context | **Downstream Customer only**, read-only, via published evidence contracts (`evaluation/contracts/*.schema.json`) — never Conformist (it must not silently adopt a source's unresolved ambiguity as fact) and never upstream to any domain context (it must never write back). | Capstone team | E-408; `01_BUSINESS_CASE.md` E-004 |

## 5. Anti-corruption layers

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| ACL 1 — Discovery(BIOX) → Discovery(NTG) | Compound identity resolution service that keys on (`compound_code`, `source_org`) and explicitly surfaces a collision (as in E-401) rather than merging; resolution requires human stewardship evidence per K-015. | Capstone team | E-401, E-408 |
| ACL 2 — Regulatory(RIM) → Manufacturing(ERP) | Product-mapping service that consumes `idmp_mappings.csv`; any `mapping_status` other than a clean/resolved value must be surfaced to the reconciliation context as an open conflict, not silently resolved to the RIM value by default. | Capstone team | E-404 |
| ACL 3 — external CRO Lab → LIMS | Unit/vocabulary conversion gateway that rejects (or flags) any `approved = no` interface mapping (E-405) at ingestion time, regardless of whether the specific unit pair is numerically forgiving — the approval-state check must be structural, not dependent on someone re-deriving the dimensional analysis each time. | Capstone team | E-405 |
| ACL 4 — all domain contexts → AI Evidence-Reconciliation context | This is the master ACL for the whole capstone: every fact entering the reconciliation context must carry source identity, authority, effective date and retrieval time (per `knowledge/AI_GXP_BOUNDARY.md`, `04_PRODUCT_SERVICE_BLUEPRINT.md` E-307), and any unresolved upstream conflict (E-401, E-404, E-405-style) must be passed through as a visible conflict, never resolved on the reconciliation context's own authority. | Capstone team | E-307 (via `04_PRODUCT_SERVICE_BLUEPRINT.md`) |

## 6. Ownership and change boundaries

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Who owns compound/substance/product identity changes? | Discovery function owns compound identity pre-registration; Regulatory/RIM owns substance and medicinal-product canonical identity per K-015; Manufacturing/ERP owns only its local representation and may not unilaterally redefine substance identity. | Capstone team | E-408 |
| Who owns interface-mapping approval? | Not named in supplied evidence (E-405 shows the mapping exists and is unapproved, but not who is accountable for approving it) — logged as Gap R-402. | Capstone team | Gap R-402 |
| Does the AI Evidence-Reconciliation context own any identity? | No — by design (§2), it owns only its own output schema (evidence citations, conflict flags), never compound/substance/product/batch/case/inventory identity. Any implementation that lets the reconciliation context "correct" or "canonicalize" an identity conflict on its own authority violates this boundary. | Capstone team | E-408 |

## 7. Event semantics

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What domain events should the reconciliation context consume? | `IdentityMappingFlagged` (from `idmp_mappings.csv`-style ambiguous status, E-404), `InterfaceMappingUnapproved` (from `interface_mappings.csv`-style unapproved config, E-405), `CompoundCodeCollisionDetected` (from cross-organisation `compound_code` collision, E-401) — all read-only signals into the reconciliation context, never commands. | Capstone team | E-401, E-404, E-405 |
| What events must the reconciliation context never emit? | Any event that a downstream system could interpret as a disposition or identity-resolution action — e.g., no `IdentityResolved`, `BatchReleased`, `MappingApproved` event may originate from the AI context; those are exclusively human/system-of-record events per §6 and `01_BUSINESS_CASE.md` E-004. | Capstone team | `01_BUSINESS_CASE.md` E-004 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-401 | Assumption | `SUB-0091`/`SUB-0092` (E-402) are hypothesized as the substance-level counterpart of the E-401 `BX-17` mesylate/free-base split, but no explicit linking field confirms this | Medium — architecture should not hard-code this link until confirmed | Capstone team | Phase 2/3, full evidence register cross-check | Open |
| R-402 | Gap | No named accountable owner for interface-mapping approval (E-405) | Medium — ACL 3 (§5) needs an approval workflow owner | Capstone team | Phase 3 (Specify) | Open |
| R-403 | Risk | If the reconciliation context's ACLs are implemented as simple pass-throughs rather than genuine conflict-preserving gateways, unresolved identity ambiguity (E-401, E-404) could be silently lost by the time it reaches a human reviewer | High — would violate `knowledge/AI_GXP_BOUNDARY.md`'s "do not... hide conflicting evidence" | Capstone team | Phase 4 (Build), architecture review | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Compound identity never merges across `source_org` without stewardship | Discovery bounded-context identity rule (§2/§3) | Not yet implemented as a test | — | Pending |
| Unapproved interface mappings are rejected/flagged at ingestion (ACL 3) | Interface gateway design (§5) | Not yet implemented | — | Pending |
| Reconciliation context never emits a disposition/resolution event (§7) | Event-schema constraint | Related to `evaluation/contracts/batch_response.schema.json` prohibited-action tests | `tools/test_contracts.py` (existing tests cover output schema, not event emission specifically) | Partial |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
