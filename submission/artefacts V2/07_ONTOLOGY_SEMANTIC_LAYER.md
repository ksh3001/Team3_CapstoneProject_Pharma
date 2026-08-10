# Ontology and Semantic Layer

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team 3 — AEGIS-PHARMA capstone (individual names/roles pending; see A-001 in `01_BUSINESS_CASE.md`) |
| Version / date | v0.1 draft — 2026-08-07 |
| Reviewers | Pending team review |
| Status | Draft |
| Related requirements / ADRs | `05_DDD_CONTEXT_MAP.md`; `06_DATA_GOVERNANCE_INTEGRITY.md`; INJ-013, INJ-018, INJ-039, INJ-040, INJ-046 |

## Purpose

Defines the temporal- and jurisdiction-aware semantic model needed so that "current," "approved" and "authoritative" are never treated as global, timeless properties. Accountable owner: capstone team. Completion criteria: every temporal/jurisdictional conflict below is modeled as a first-class property (scope + effective date + source), not resolved by picking one value and discarding the others.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-601 | `data/protocol_versions.csv` | Protocol version register, undated | Trial `NCB204-301` has three simultaneously-recorded versions: v5.0 (effective 2026-06-01, status `global_current`), v4.1 (effective 2026-02-01, status `current_IN_pending_amendment`), v3.2 (effective 2025-10-01, status `obsolete_but_site_cached`) | Matches INJ-013; critically, `current_IN_pending_amendment` is a *legitimate* regulatory state (India's ethics-committee approval of the v5.0 amendment is still pending), whereas `obsolete_but_site_cached` describes a stale local copy — these are not the same kind of "non-latest version" and must not be modeled identically |
| E-602 | `data/site_approvals.csv` | Site approval register, undated | Site `IN-014` (trial `NCB204-301`): approved_protocol = 4.1, ec_status = active. Site `DE-008`: approved_protocol = 5.0, ec_status = active | Confirms E-601's India state is a genuine, currently-active local approval, not an error — both sites are correctly "active" under two different protocol versions at the same moment |
| E-603 | `data/timezone_rules.csv` | Site timezone register, undated | `DE-008`: Europe/Berlin, DST transition 2026-03-29. `IN-014`: Asia/Kolkata, no DST | Any cross-site temporal comparison (e.g., "was this event before or after the v5.0 effective date at each site") must resolve local time correctly per site, including DST for DE-008 |
| E-604 | `data/terminology_versions.csv` | MedDRA version register, undated | MedDRA 27.1 = `legacy_cases`; MedDRA 28.0 = `current_global` | Matches INJ-039; a term coded under 27.1 is not automatically re-mappable to its 28.0 preferred term without an explicit version-aware mapping step |
| E-605 | `data/listedness_sources.csv` | Listedness register, undated | Product `NCB-204`, risk "anaphylaxis": `IB v12` = listed (yes); `CCDS v4` = listed (yes); `IN local label` = listed (no) | Matches INJ-040 exactly — three sources of the *same* product/risk pair genuinely disagree, not through error but because IB/CCDS are global reference safety documents and the IN local label reflects a distinct, locally-approved regulatory text |
| E-606 | `data/product_labels.csv` | Label register, undated, all rows status = approved | `NCB-204` EU label v6: "severe infusion reactions including anaphylaxis"; US label v5: "serious infusion reactions" (no explicit anaphylaxis term); IN label v3: "infusion reactions" (generic) | All three are currently approved — the divergence here is in textual specificity, not approval status; this is evidence-precise and should not be forced to match the higher-level case narrative's "pending/absent" framing without re-verification (see Gap R-601) |
| E-607 | `data/market_authorisations.csv` | Market authorisation register, undated | `NCB-204`: EU authorised/label v6; US authorised/label v5; IN authorised/label v3 | Label-version references are internally consistent with E-606 — no additional conflict found here |
| E-608 | `data/regional_rules.csv` | Regional decision-rights register, undated | EU: "Qualified Person" holds "batch certification human-only"; US: "Quality Unit" holds "disposition human-only"; IN: "Authorized Quality" holds "release human-only" | The underlying invariant (human-only regulated release decision) is universal across all three jurisdictions, but the accountable-role *name* and legal basis differs per jurisdiction — this must be modeled as a jurisdiction-parameterized role, not a single global term like "the QP" |

## 1. Competency questions

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| CQ1 | "What protocol version and approval status applies to trial X at site Y as of date D?" — answerable from E-601+E-602 jointly; not answerable from either alone, since E-601 gives global version states and E-602 gives per-site approval. | Capstone team | E-601, E-602 |
| CQ2 | "Which listedness source is authoritative for expectedness determination for adverse event risk R on product P, for a case arising in jurisdiction J?" — this requires an explicit authority-by-jurisdiction rule (not present in the data itself, see Gap R-602), since E-605 shows three legitimate sources disagreeing. | Capstone team | E-605; Gap R-602 |
| CQ3 | "What is the currently approved label risk text for product P in market M as of date D?" — answerable from E-606/E-607 directly, with version and effective status attached. | Capstone team | E-606, E-607 |
| CQ4 | "Who is the accountable human role for a batch-release decision in jurisdiction J, and does any role anywhere carry AI release authority?" — answerable from E-608; answer to the second half is uniformly "no" across all three jurisdictions sampled. | Capstone team | E-608 |
| CQ5 | "Was a given timestamped event before or after protocol version v5.0's effective date, evaluated in local site time?" — requires E-601's effective_date plus E-603's per-site timezone/DST rule; a naive UTC-only comparison would be wrong for DE-008 across the March DST transition. | Capstone team | E-601, E-603 |

## 2. Core concepts and relations

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Protocol (trial_id, version, effective_date, status) —[approved_for]→ Site (site_id, jurisdiction, ec_status) | Models E-601/E-602: a single trial has multiple Protocol version nodes, each independently linked to zero or more Sites via an `approved_for` edge carrying its own `ec_status`. | Capstone team | E-601, E-602 |
| Product —[has_label]→ Label (market, version, risk_text, status, effective) | Models E-606/E-607; multiple Label nodes per Product, one per market, each independently versioned. | Capstone team | E-606, E-607 |
| Product —[has_listedness_statement]→ ListednessSource (document, version) —[states]→ RiskListedness (risk, listed: boolean) | Models E-605 as a 3-hop relation, preserving all three sources rather than collapsing to one listedness value per product/risk pair. | Capstone team | E-605 |
| Jurisdiction —[assigns_accountable_role]→ AccountableRole (name, legal_basis) —[holds]→ DecisionType (human_only: boolean) | Models E-608; the "human-only" invariant is a property of `DecisionType`, constant across jurisdictions, while `AccountableRole.name` varies. | Capstone team | E-608 |
| AdverseEventTerm (raw_text) —[coded_under]→ TerminologyVersion (system, version) —[maps_to]→ PreferredTerm | Models E-604; a coded term is never stored without its coding-system version attached. | Capstone team | E-604 |

## 3. Identifiers and aliases

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| New identifier classes introduced by this artefact (beyond `05_DDD_CONTEXT_MAP.md`'s compound/substance/product identifiers) | `trial_id` (e.g., `NCB204-301`), `site_id` (e.g., `IN-014`, `DE-008`), `terminology_version` (e.g., MedDRA 27.1 vs 28.0) — each requires its own identity + versioning rule, not reuse of the product/substance identity pattern from `05_DDD_CONTEXT_MAP.md`. | Capstone team | E-601–E-604 |
| Does any identifier collide across contexts? | Not observed in this evidence pull; `trial_id` and `site_id` namespaces do not appear to overlap with the compound/substance/product identifiers already documented. This is stated as a negative finding, not proof of absence — full identifier-collision review remains open at the whole-estate level. | Capstone team | N/A — negative finding |

## 4. Temporal and jurisdictional semantics

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Is "current" a global or scoped property? | Scoped, not global — E-601 proves this directly: v5.0 is `global_current` while v4.1 is simultaneously `current_IN_pending_amendment` for India specifically. The ontology must never expose a single "current version" field for a trial without a jurisdiction/site parameter. | Capstone team | E-601, E-602 |
| Is a non-latest version automatically a defect? | No — E-601's v4.1 state is a legitimate, active regulatory condition (pending local EC amendment approval), while v3.2 (`obsolete_but_site_cached`) is a genuine risk (a stale cached copy with no active approval basis). The ontology must distinguish "legitimately still-current-locally" from "obsolete-but-not-yet-refreshed" as two different semantic categories, not one "old version" bucket. | Capstone team | E-601 |
| How does this artefact treat "later timestamp = more authoritative"? | It does not assume this — consistent with `case/SOURCE_SYSTEM_FACT_PACK.md`'s explicit warning ("A later timestamp is not automatically more authoritative than an approved signed record"). E-605's three listedness sources are not resolved by picking the most recently dated one; jurisdiction and document type (reference safety document vs. local label) determine authority for a given purpose. | Capstone team | E-605, `case/SOURCE_SYSTEM_FACT_PACK.md` |
| How are cross-site timestamps compared? | Via site-local time with each site's own DST rule (E-603) applied before comparison to a protocol's `effective_date` — a UTC-naive comparison is explicitly rejected as a design pattern given DE-008's DST transition. | Capstone team | E-603 |

## 5. Controlled vocabularies and units

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Are controlled vocabularies version-pinned? | Must be — E-604 shows MedDRA 27.1 vs. 28.0 producing different preferred-term mappings for the same underlying event; `05_DDD_CONTEXT_MAP.md` E-407 similarly showed `controlled_vocabularies.csv` carrying an explicit version (`2026-1`) for dose_form/route terms. Both cases require the ontology to store (term, vocabulary, version) as a single unit, never term alone. | Capstone team | E-604; `05_DDD_CONTEXT_MAP.md` E-407 |
| Does version pinning apply to units as well as terms? | Yes, by extension — `05_DDD_CONTEXT_MAP.md` E-405 (unapproved mg/L→µg/mL interface mapping) is the units-domain instance of the same general rule: a unit conversion is a versioned, approvable artifact, not an implicit assumption. | Capstone team | `05_DDD_CONTEXT_MAP.md` E-405 |

## 6. Entitlements and policy context

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Is the "human-only release decision" rule jurisdiction-specific or universal? | The invariant (no AI release/disposition authority) is universal across all three sampled jurisdictions (E-608); only the accountable role's *name* and legal basis is jurisdiction-specific ("Qualified Person" in EU, "Quality Unit" in US, "Authorized Quality" in IN). The ontology's `DecisionType.human_only` flag must be hard-coded true for release/disposition regardless of jurisdiction; only the `AccountableRole.name` lookup varies. | Capstone team | E-608 |
| Risk of getting this backwards | If an implementation hard-codes "EU Qualified Person" as *the* accountable-role concept globally, it would be structurally wrong for US and IN deployments — this is a concrete design bug this section exists to prevent, not a hypothetical. | Capstone team | E-608 |

## 7. Versioning and validation

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| What must every fact node in this ontology carry, at minimum? | (value, source document + version, effective_date, jurisdiction/scope) as a single unit — directly demonstrated as necessary by E-601 (protocol version + status + effective_date), E-605 (source + version + listed value), and E-606 (market + version + risk_text + status). A model that stores only the latest value per entity cannot represent any of these three real cases correctly. | Capstone team | E-601, E-605, E-606 |
| How is this validated? | Each competency question (§1) should have at least one corresponding query test against the loaded ontology, confirming both that valid multi-version states are retrievable (not collapsed) and that no query silently returns a single "current" answer when the underlying data has jurisdiction-scoped divergence (as in E-601/E-602). Not yet implemented — logged as Gap R-603. | Capstone team | Gap R-603 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-601 | Gap | `product_labels.csv` (E-606) shows all three NCB-204 labels as "approved" with differing text specificity, which does not exactly match the case narrative's INJ-046 framing ("approved in EU, pending in US, absent in two distributor leaflets") | Low-Medium — the CSV evidence is treated as authoritative for this artefact; the narrative may describe a different or broader instance of label divergence not captured in this specific dataset | Capstone team | Phase 2, cross-check against full `data/` set for a second labeling-divergence dataset | Open |
| R-602 | Gap | No supplied rule states which listedness source (IB, CCDS, local label) is authoritative for which purpose/jurisdiction (E-605) | High — CQ2 cannot be fully answered without this; a wrong default (e.g., "always use CCDS") could mis-state local reportability, and a wrong default the other way could miss a genuine global signal | Capstone team / Safety Physician (role-played) | Phase 3 (Specify), before Workflow B listedness logic is built | Open |
| R-603 | Gap | No competency-question validation queries implemented yet against a real ontology/graph store | Medium | Capstone team | Phase 4 (Build) | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| "Current" protocol version is always jurisdiction-scoped in output, never a bare global value | Ontology query design (§4) | Not yet implemented | — | Pending |
| Listedness output surfaces all disagreeing sources, never a single collapsed answer | `evaluation/contracts/pv_response.schema.json` / `evidence_item.schema.json` | Partially covered by existing schema structure; specific multi-source listedness test not yet written | `evaluation/contract_samples/positive_pv.json` (existing) | Partial |
| Accountable-role lookup is jurisdiction-parameterized, not hard-coded to one region | Entitlement/role-resolution design (§6) | Not yet implemented | — | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| — | — | Not yet reviewed | — | — |
