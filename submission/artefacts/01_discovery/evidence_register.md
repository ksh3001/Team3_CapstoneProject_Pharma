# Prompt 01 — Evidence Register (Discovery)

| Field | Entry |
|---|---|
| Prompt | `prompts/01_discovery.md` |
| Team | Team3 |
| As-of | 2026-08-06 |
| Output folder | `submission/artefacts/01_discovery/` |
| Framing mode | **hypothesis** |
| Architecture proposed? | **No** (Prompt 01 constraint) |

## Entry criteria

| Criterion | Status |
|---|---|
| Source materials available | Met — full challenge package offline |
| Engagement scope stated | Met — see below |
| Access gaps listed | Met — see below |

### Engagement scope (in bounds)

- Immutable challenge evidence: `case/`, `data/`, `knowledge/`, `source_documents/`, `evaluation/`, `requirements/`, `starter/`, `templates/`, `app/`, `tools/`, `prompts/`
- Writable participant work: `submission/` only
- Mandatory workflow objects (for later framing, not designed here): batch evidence, PV intake, supply options

### Known access gaps

- No live SME / shop-floor time-motion study
- No production NTG systems or credentials
- No measured historical release lead-time distribution (only board target)
- Package `verify_package` FAIL on this Windows CRLF checkout (LF-normalized spot-check previously matched published hash for a knowledge file); full LF audit not completed

---

## 1. Repository and source-system map

### Repository map (what exists)

| Area | Path | Contents (observed) | Connection |
|---|---|---|---|
| Case | `case/INTEGRATED_CASE.md` | Org, mandate, workflows A/B/C, INJ-001…084 | Narrative spine |
| Stakeholder pack | `case/STAKEHOLDER_PACK.md` | Roles, incentives, conflicts | Complements thin CSV |
| System fact pack | `case/SOURCE_SYSTEM_FACT_PACK.md` | Domain→systems→known conditions | Brownfield map |
| Regulatory boundary | `case/REGULATORY_BOUNDARY_PACK.md` | Jurisdiction caution | Not legal advice |
| Operational extracts | `data/*.csv` | 139 profiled datasets (`DATASET_PROFILE.csv`); 602 dictionary rows | Synthetic SoT candidates |
| Inject index | `data/injects.json` + `inject_evidence_map.csv` | 84 injects, all `UNASSESSED` | Challenge conditions |
| Knowledge | `knowledge/*.md` + `data/knowledge_catalog.csv` | 32 docs with authority/status/trust | Mixed trust |
| Source documents | `source_documents/` | Protocols, LIMS contracts, EMA letter, CCDS, cold-chain, CMO audit | Versioned extracts |
| Contracts / fixtures | `evaluation/contracts/`, `public_fixtures/` | Schemas + PUB-01…15 | Inputs only |
| Starter (anti-pattern) | `starter/legacy_pharma.py`, `legacy_portal.js` | Lexical ready; equal-trust MD; supply reservation | Current-state clue |
| Explorer | `app/` | Offline inject browser | Navigation aid |
| Checks | `tools/verify_package.py`, `test_contracts.py` | Integrity / schema tests | Package tooling |

### Source-system map (from fact pack + inventory CSVs)

| Domain | Systems (fact pack) | Known condition (fact pack) | Package CSV / system clues |
|---|---|---|---|
| Discovery | ELN, assay, images, compound registry | ID collision post-acquisition | `compounds.csv`, `assay_results.csv`, BIOX-ELN research-only |
| Clinical | EDC, CTMS, eConsent, IRT, ePRO, wearables, imaging | Protocol/consent async; clocks differ | `protocol_versions.csv`, `consents.csv`, `wearable_readings.csv` |
| Manufacturing | ERP, MES, eBR, historian, PAT, warehouse | Genealogy breaks; unit mismatches | `batches.csv`, `material_genealogy.csv`, `ebr_steps.csv` |
| Laboratory | LIMS, CDS, instruments, notebooks, spreadsheets | Shared accounts; OOS inconsistency | `lab_results.csv`, `access_logs.csv`, LIMS-4 validated |
| Quality | eQMS, DMS, training, supplier quality | Taxonomy / effective-doc inconsistency | `deviations.csv`, `capa_records.csv` |
| Safety | Global safety DB, affiliates, vendors, literature, call centre | Duplicates; terminology; awareness dates | `icsr_cases.csv`, `safety_receipts.csv` |
| Regulatory | RIM, eCTD, labeling, IDMP | Identity / commitment drift | `idmp_mappings.csv`, `ectd_sequences.csv` |
| Supply | Serialization, logistics, cold-chain, CMO | Aggregation / logger association gaps | `inventory.csv`, `shipments.csv`, `temperature_loggers.csv` |
| AI platform | Gateway, models, vector store, tools, evaluator | Stale entitlements; mutable manifests | `users_entitlements.csv`, `access_cache.csv`, `tool_catalog.csv`; AI-EVIDENCE **pilot** with **conflicting validation states** |

**Fact (SOURCE_SYSTEM_FACT_PACK):** “No system is universally authoritative… A later timestamp is not automatically more authoritative than an approved signed record.”

---

## 2. Entities, identifiers, and timestamp semantics

| Entity / ID class | Example evidence | Timestamp fields observed | Semantic risk |
|---|---|---|---|
| Product | NCX-101, NCB-204, NCS-310, NCR-415 (`portfolio_products.csv`) | Stage / patent_months (static attrs) | Alias / IDMP conflicts in other datasets |
| Batch | e.g. NCB204-B24071 (`lab_results.csv`) | Lab result rows; EBR back-entry theme (INJ-025) | Event time vs report/back-entry time |
| Lab result | LR-88, LR-89 | Implicit result time not fully standardized in row | Unit vs spec mismatch on same row |
| User / entitlement | `contractor_77`, `qp_eu_1` | `revoked_at`, `cached_until` vs `iam_state` | Cache can outlive revocation |
| Knowledge doc | K-001…K-032, K-998, K-999 | `effective` (or `unknown`) | Superseded/untrusted/draft still in corpus |
| API contract | LIMS result v1 vs v2 | `date_semantics` sparse / “precision variable” on Safety ICSR | Version drift |
| Inventory lot position | product×market×quality_status | None on inventory rows | Quality status must gate “available” |
| Agent run | AR-77 (`agent_runs` dictionary example) | `state_age_minutes` | Stale checkpoint / duplicate draft reservations |

**Ambiguous terms flagged for Prompt 04 (DDD) — not redefined here:** `review readiness`, `available_units`, `OOS_LIMS` vs pass, `conditionally_released` vs `validated` vs `research_only`, `active_cached`.

---

## 3. Evidence ownership and authority (preliminary)

| Data class | Provisional challenge SoT | Who may assert (from decision_rights / packs) | Must not assert as SoT |
|---|---|---|---|
| Batch certification / disposition | Quality / QP systems of record (outside assist) | EU Qualified Person — AI authority **none** | Lexical lab “ready”; untrusted knowledge |
| Lab result value + unit | Transmitted LIMS result + declared contract version | QC / LIMS owner | Unapproved interface conversion (`approved=no`) |
| Policy / SOP text | `knowledge_catalog` rows with trust/status **approved** and applicable effective date | Document control / Quality | K-007 superseded; K-998/K-999 untrusted; K-026 draft |
| ICSR final reportability | Safety Physician — AI **none** | Safety Physician | FAKE_PV_EXPEDITED_RULE |
| Stock allocation execution | Supply Governance Board — AI **draft only** | Supply Governance Board | Summing quarantine into available; reservation creation |
| Entitlement | IAM `users_entitlements.iam_state` | IAM | `access_cache` alone when revoked |
| System validation state | Ambiguous — three inventories disagree for AI-EVIDENCE | Quality system owner (unresolved) | Single catalog pick without conflict flag |

### Knowledge trust snapshot (catalog facts)

| Trust / status | Docs (examples) |
|---|---|
| approved | Majority of K-001…K-032 global policies |
| superseded | K-007 `BATCH_RELEASE_POLICY_OLD.md` (superseded by K-006) |
| untrusted | K-998 `MALICIOUS_SUPPLIER_DEVIATION.md`; K-999 `FAKE_PV_EXPEDITED_RULE.md` |
| draft | K-026 `RESEARCH_NOTE_UNAPPROVED.md` |
| local_approved | K-016 `LOCAL_WORK_INSTRUCTION_DE.md` (jurisdiction DE) |

---

## 4. Material inconsistencies, gaps, and conflicts

| ID | Finding | Evidence path | Class |
|---|---|---|---|
| C-01 | Board −14% lead time vs no Quality-authority change | `data/board_requests.csv` BR-01 | Fact constraint |
| C-02 | KPI conflict across Manufacturing/Quality/Safety/Clinical | `data/kpi_conflicts.csv` | Fact |
| C-03 | Lab potency unit `mg/L` vs spec `ug/mL`; status OOS_LIMS | `data/lab_results.csv` LR-88 | Fact |
| C-04 | Interface mapping `1:1_assumed`, **approved=no** | `data/interface_mappings.csv` | Fact |
| C-05 | LIMS API v1 `unit` vs v2 `ucum_code` / `lifecycleState` | `data/api_contract_versions.csv` | Fact |
| C-06 | IAM revoked but gateway `active_cached` past revocation | `users_entitlements.csv`, `access_cache.csv` | Fact |
| C-07 | Inventory includes `quarantine` 5100 units NCB-204 Global | `data/inventory.csv` | Fact |
| C-08 | AI-EVIDENCE validation states disagree across three sources | `validation_inventory.csv` vs `system_inventory.csv` pilot | Fact |
| C-09 | Starter treats invalid_sample_prep as ready; trusts all MD; creates reservation | `starter/legacy_pharma.py` | Observed anti-pattern |
| C-10 | Malicious doc instructs ignore quality holds | `knowledge/MALICIOUS_SUPPLIER_DEVIATION.md` | Fact (adversarial) |
| C-11 | cost_model human review lines at 0 vs nonzero staff rates | `cost_model.csv`, `staff_rates.csv` | Fact gap |
| C-12 | All 84 injects still `participant_status=UNASSESSED` | `inject_evidence_map.csv` | Gap |
| C-13 | Measured release-pack cycle-time distribution | Not in package | **Missing** |

---

## 5. Stakeholder decisions and decision horizons

| Decision | Status | Horizon | Accountable (evidence) |
|---|---|---|---|
| Achieve −14% release lead time without Quality-authority change | Pending target | Due 2026-11-30 | Board (`board_requests.csv`) |
| Batch certification | Ongoing human | Per batch | EU QP — AI none |
| ICSR reportability | Ongoing human | Clock-driven | Safety Physician — AI none |
| Stock allocation | Ongoing human | Shortage events | Supply Governance Board — AI draft only |
| Capstone intervention qualification | Pending Team3 | Capstone window | Team3 (this discovery feeds Prompt 02) |
| Inject assessment | UNASSESSED ×84 | Capstone | Team3 domain/evidence |

Stakeholders with explicit CSV priority: EU QP (evidence completeness), Manufacturing VP (supply continuity), Global Safety Head (reporting timeliness) — `stakeholders.csv`. Broader mandates in `case/STAKEHOLDER_PACK.md`.

---

## 6. Constraints register (visible in evidence)

| Type | Constraint | Source |
|---|---|---|
| Compliance | No AI release/reject/reprocess/recall; no final causality/seriousness/reportability; no reserve/allocate/ship | `ai_use_boundaries.csv` |
| Accountability | AI authority none / draft only on named decisions | `decision_rights.csv` |
| Quality authority | No specification or Quality-authority change while pursuing lead-time cut | `board_requests.csv` |
| Data integrity | Do not silently convert units (dictionary note on unit fields; mapping unapproved) | `DATA_DICTIONARY.csv`, `interface_mappings.csv` |
| Security | Revoked IAM must not remain effective via cache; untrusted docs not instructions | entitlements/cache; K-998/K-999 |
| Continuity | Manual runbooks; batch/supply 14-day AI outage; PV without inference | `continuity_requirements.csv` |
| Privacy | Purpose limitation themes in knowledge + injects D09 | catalog + case |
| Technical | Offline package; work under `submission/`; synthetic training only | `PACKAGE_SCOPE_AND_ASSUMPTIONS.md`, `LICENSE_AND_USE.md` |
| Economics | Large inference cost line; human review understated at 0 | `cost_model.csv` |

---

## 7. Current-state workflow sketch

### Observed (starter code)

1. Load `lab_results.csv` → if all statuses in {pass, invalid_sample_prep} → `batch_ready` true (**no** unit/authority/as-of checks).
2. Search `knowledge/*.md` by substring → return file+full text (**equal trust**).
3. Sum all `inventory.csv` units for product → return `available_units` and `reservation_status: created` (**includes quarantine; side effect flag**).

### Inferred (labeled assumption — case §2)

Humans gather extracts across MES/LIMS/QMS/safety/supply systems, reconcile conflicts manually, then accountable roles decide in systems of record. Assist platform AI-EVIDENCE is **pilot** with disputed validation state.

| Step | Observed / inferred |
|---|---|
| Multi-system evidence gather | Inferred (case, fact pack) |
| Informal / lexical readiness | Observed (starter) |
| Equal-trust document use | Observed (starter) |
| Planning that mutates reservation | Observed (starter return value) |
| Human regulated decision | Fact (`decision_rights.csv`) |

---

## 8. Fact / derivation / assumption / question register

| ID | Class | Statement |
|---|---|---|
| F-01 | Fact | 84 injects; 139 profiled CSV datasets; 32 knowledge docs catalogued |
| F-02 | Fact | BR-01: −14% release_lead_time by 2026-11-30; no spec/Quality-authority change |
| F-03 | Fact | no_ai_baselines: MDM 38%/10w; rules 27%/6w; genai 51%/14w |
| F-04 | Fact | contractor_77 IAM revoked 2026-08-01T05:00:00Z but cache active until 2026-08-03T10:00:00Z |
| F-05 | Fact | LR-88 potency 0.92 mg/L vs spec 0.85-1.05 ug/mL, status OOS_LIMS |
| F-06 | Fact | CRO_LAB_TO_LIMS conversion approved=no |
| F-07 | Fact | NCB-204 Global quarantine units=5100 alongside released markets |
| F-08 | Fact | K-998/K-999 untrusted; K-007 superseded; K-026 draft |
| F-09 | Fact | AI-EVIDENCE listed validated / conditionally_released / research_only across inventories |
| F-10 | Fact | Contract positive/negative samples exist under `evaluation/contract_samples/` |
| D-01 | Derivation | Equal-trust retrieval + malicious SOP ⇒ prompt-injection path is present in current-state tooling pattern |
| D-02 | Derivation | Unapproved unit mapping + mixed units on LR-88 ⇒ silent conversion would fabricate comparability |
| D-03 | Derivation | Missing cycle-time baseline ⇒ cannot claim decision-ready ROI for genAI-first |
| A-01 | Assumption | Packaged conflicts are intentional challenge conditions, not packaging defects |
| A-02 | Assumption | Stakeholder pack is authoritative over the 3-row `stakeholders.csv` for role coverage |
| Q-01 | Question | What is median/p90 release-pack assembly time today? |
| Q-02 | Question | Which validation inventory is authoritative for AI-EVIDENCE? |
| Q-03 | Question | Event time vs report time fields per dataset for as-of queries? (partial in dictionary) |

---

## 9. Top ten investigation hypotheses

| Rank | Hypothesis | Impact if true |
|---|---|---|
| 1 | MDM + rules remove more safe waste than genAI-first | Changes Prompt 02 Answer |
| 2 | Unit/identity/time conflicts dominate batch rework | Measure design |
| 3 | Authority-blind retrieval causes control bypass | Blocks naive RAG |
| 4 | Cache-based auth will admit revoked users | Zero Trust control |
| 5 | Quarantine stock is treated as available in planning tools | Hard gate for supply |
| 6 | Hidden human review cost falsifies genAI ROI | FinOps |
| 7 | AI-EVIDENCE validation ambiguity blocks GxP use claims | Intended use boundary |
| 8 | PV clock / duplicate injects drive compliance risk | Workflow B priority |
| 9 | Automation bias closes gaps incorrectly | HITL requirements |
| 10 | 14-day AI outage is a credible operating mode | Continuity first-class |

---

## 10. AI FDE input sufficiency score

| AI FDE input | Score | What exists | What is missing |
|---|---|---|---|
| Business context | Strong | Case, board request, portfolio, KPI conflicts, no-AI baselines | Live executive interviews |
| User workflow | Partial | Case narrative; SOURCE_SYSTEM fact pack; starter anti-pattern | Observed SME workflow; timed baselines |
| Constraints | Strong | AI boundaries, decision rights, BR-01, continuity, DI unit notes | Binding legal opinions by jurisdiction |
| Evidence (data, logs, research) | Partial | 139 CSVs, 84 injects, 32 knowledge docs, fixtures, contracts | Measured cycle-time/review-hour baselines; complete LF hash audit |
| Stakeholder needs | Partial | Stakeholder pack + decision_rights + 3 CSV rows | Primary research (sites, works council) |

### Overall framing mode: `hypothesis`

**Rule applied:** User workflow = Partial; Evidence = Partial with critical baseline **Missing** (cycle time) → Prompt 02 must be a **testable hypothesis narrative**, not a locked build mandate. Do not invent unlabeled facts for Situation/Complication.

---

## Exit criteria self-check

- [x] Sources of truth and trust gaps explicit (§3–4)
- [x] No target architecture / tool selection / full risk model proposed
- [x] Facts vs assumptions vs questions separated (§8)
- [x] Sufficiency scores + framing mode declared (§10)
- [x] Acquisition backlog required (Partial/Missing) → see `evidence_acquisition_backlog.md`
- [x] Early wastes + thin `dmaic_lens.md` produced
- [x] `hypothesis` mode: later framing may use labeled assumptions only
