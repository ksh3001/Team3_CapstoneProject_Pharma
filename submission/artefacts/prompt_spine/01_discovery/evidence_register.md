# Prompt 01 — Evidence Register (Discovery)

| Field | Entry |
|---|---|
| Team | Team3 |
| As-of | 2026-08-06 |
| Prompt | `prompts/01_discovery.md` |
| Output root | `submission/artefacts/prompt_spine/01_discovery/` |
| Framing mode | **hypothesis** |

## Engagement scope (in bounds)

- Challenge package: `case/`, `data/`, `knowledge/`, `source_documents/`, `evaluation/`, `starter/`, `requirements/`, `templates/`, `app/`, `tools/`
- Writable work: `submission/` only
- Out of bounds: live NTG production systems, real patient/GxP decisions, inventing unlabeled facts

## Known access gaps

- No live SME interviews; stakeholder needs inferred from packs/CSVs
- No measured operational lead-time distribution (board target exists; baseline Unknown)
- Package integrity verify FAIL on Windows CRLF checkout (A-001); LF-normalized spot-check matches

---

## 1. Repository and source-system map

| Area | Path | Role | Trust note |
|---|---|---|---|
| Case narrative | `case/INTEGRATED_CASE.md` | Scenario + 84 injects | Challenge authority for story |
| Stakeholder pack | `case/STAKEHOLDER_PACK.md` | Mandates / incentives | Broader than CSV |
| Regulatory boundary | `case/REGULATORY_BOUNDARY_PACK.md` | Jurisdiction caution | Not legal advice |
| System facts | `case/SOURCE_SYSTEM_FACT_PACK.md` | Brownfield systems | Challenge fact pack |
| Operational data | `data/*.csv` (~143) | Synthetic operational extracts | Deliberate conflicts |
| Inject index | `data/injects.json` | INJ-001…084 | Count verified 84 |
| Knowledge | `knowledge/*.md` (32) | Mixed authority incl. malicious/fake/old | Must filter |
| Source docs | `source_documents/` | Protocols, LIMS contracts, EMA letter, etc. | Versioned extracts |
| Contracts | `evaluation/contracts/` | Fail-closed schemas | Executable |
| Fixtures | `evaluation/public_fixtures/` | PUB-01…15 inputs | No answer keys |
| Starter | `starter/legacy_pharma.py`, `legacy_portal.js` | Anti-pattern current-state sketch | Not a solution |
| Explorer | `app/` | Offline browse | Challenge UI |

**Connection sketch (observed):** LIMS/MES/EBR/QMS/safety/serialization/inventory CSVs are separate extracts with overlapping identifiers; knowledge docs assert policies at mixed authority; starter concatenates/trusts indiscriminately.

---

## 2. Entities, identifiers, timestamp semantics

| Entity class | Example IDs / sources | Timestamp meaning (observable) | Ambiguity |
|---|---|---|---|
| Product | NCX-101, NCB-204, NCS-310, NCR-415 (`portfolio_products.csv`) | Stage/patent months as static attributes | Label/IDMP conflicts later (INJ-045/046) |
| Batch | `batches.csv`, genealogy | Event vs back-entry time (INJ-025) | Genealogy breaks (INJ-021) |
| Lab result | `lab_results.csv` | Result time vs interface receipt | Unit systems conflict (INJ-024) |
| ICSR / AE | `icsr_cases.csv`, receipts | Awareness vs receipt vs DB entry (INJ-038) | Duplicate clusters (INJ-037) |
| Shipment / logger | `shipments.csv`, temperature loggers | Logger clock vs lane time (INJ-051) | Association disputed |
| User entitlement | `users_entitlements.csv` vs `access_cache.csv` | Revocation time vs cache (INJ-067) | Stale auth |
| Protocol | `protocol_versions.csv` | Approval effective dates by country (INJ-013) | Site divergence |

**Derivation:** Time is not a single enterprise clock; each workflow must carry `as_of` and cite which clock was used.

---

## 3. Evidence ownership and authority (preliminary)

| Data class | Provisional SoT (challenge) | Who may assert | Do not treat as SoT |
|---|---|---|---|
| Batch disposition | Human QP / Quality systems of record | EU QP (AI none) | Assist “readiness”, starter lexical ready |
| Lab result value+unit | LIMS as transmitted + contract version | QC / LIMS owner | Silent interface conversion |
| Safety case final calls | Safety Physician / PV system | Safety Physician (AI none) | Fake expedited rules; untrusted MD |
| Allocation execution | Supply Governance Board | Board (AI draft only) | Planner tools that mutate inventory |
| Policy text | Approved effective knowledge only | Document control / Quality | `MALICIOUS_*`, `FAKE_*`, `*_OLD`, `RESEARCH_NOTE_UNAPPROVED` |
| Model/tool allowlist | Approved signed manifest | CISO / system owner | `tool_manifest_poisoned.json` |

Full authority map deferred to Phase 2 / Prompt library §2 (artefacts 05–08).

---

## 4. Material inconsistencies, gaps, conflicts (sample)

| ID | Conflict / gap | Evidence | Impact on framing |
|---|---|---|---|
| C-01 | KPI conflict speed vs quality vs safety vs clinical lock | `kpi_conflicts.csv` | Complication multi-party |
| C-02 | Unit mapping unapproved | diagnostics; INJ-024 | Measure Unknown for lab trust |
| C-03 | Entitlement cache stale | diagnostics; INJ-067 | Authz must not trust cache |
| C-04 | Untrusted / malicious knowledge present | knowledge set; INJ-065 | Retrieval not equal-trust |
| C-05 | cost_model zeros human review | `cost_model.csv` | Financial baseline Incomplete |
| C-06 | True release lead-time distribution Missing | only BR-01 target | Framing mode → hypothesis |
| C-07 | Starter mutates supply reservation | `legacy_pharma.py` | Current-state unsafe pattern |

---

## 5. Stakeholder decisions and horizons

| Decision | Status | Horizon | Authority |
|---|---|---|---|
| Board −14% release lead time | Pending target | Due 2026-11-30 | Board; constraint preserves Quality authority |
| Capstone intervention shape | Pending Team3 | Capstone window | Team3 Product; must respect AI boundaries |
| Batch certification | Ongoing human | Per batch | EU QP — AI none |
| ICSR reportability | Ongoing human | Clock-driven | Safety Physician — AI none |
| Stock allocation | Ongoing human | Shortage events | Supply Governance Board — AI draft only |

---

## 6. Constraints register (visible in evidence)

| Type | Constraint | Source |
|---|---|---|
| Compliance / GxP | No AI release/reject/reprocess/recall; no final PV conclusions; no reserve/allocate/ship | `ai_use_boundaries.csv`, hard gates |
| Quality authority | No specification or Quality-authority change while chasing −14% | `board_requests.csv` BR-01 |
| Security | Deny unsigned/poisoned tools; stale auth | INJ-066/067; ZERO_TRUST knowledge |
| Privacy | Purpose limitation; sensitive PV segments | INJ-041/059–064 themes |
| Operational | AI-disabled continuity; batch/supply 14-day outage; PV without inference | `continuity_requirements.csv` |
| Technical | Offline deterministic assessed mode; work only under `submission/` | Package scope |
| Economics | Inference cost high; human review understated at 0 | `cost_model.csv`, `staff_rates.csv` |

---

## 7. Current-state workflow sketch (observed / inferred)

**Observed (starter):** batch “ready” via lexical lab status; knowledge search trusts all MD equally; supply planning sums units including unsafe states and sets `reservation_status: created`.

**Inferred (case — labeled assumption):** Humans hunt across LIMS/MES/QMS/safety/inventory extracts, reconcile conflicts manually, then accountable roles decide outside any assist.

| Step | Status |
|---|---|
| Gather extracts from many systems | Inferred from case §2 |
| Lexical / informal readiness shortcuts | Observed in starter |
| Human regulated decision | Fact from decision_rights |
| Assist with fail-closed contracts | Not present (gap) |

---

## 8. Fact / derivation / assumption / question register

| ID | Class | Statement |
|---|---|---|
| F-P01-01 | Fact | BR-01 targets −14% release_lead_time by 2026-11-30 with Quality-authority constraint |
| F-P01-02 | Fact | no_ai_baselines: MDM 38%/10w; rules 27%/6w; genai 51%/14w |
| F-P01-03 | Fact | AI boundaries and decision_rights forbid autonomous certification/reportability; allocation draft only |
| F-P01-04 | Fact | Contract samples reject prohibited batch/PV/supply outputs |
| D-P01-01 | Derivation | Multi-system conflict + unsafe starter ⇒ evidence-reconciliation waste is central |
| D-P01-02 | Derivation | Missing measured lead-time baseline ⇒ cannot claim decision-ready ROI for genAI |
| A-P01-01 | Assumption | Packaged CSV conflicts represent real NTG-like failure modes for the exercise |
| A-P01-02 | Assumption | Stakeholder pack overrides thin `stakeholders.csv` for role coverage |
| Q-P01-01 | Question | What is current median release-pack cycle time? |
| Q-P01-02 | Question | Which knowledge docs are approved SoT at as-of time? (Phase 2) |

---

## 9. Top ten investigation hypotheses

| Rank | Hypothesis | Why it matters |
|---|---|---|
| 1 | MDM + rules deliver most safe value before generative AI | Falsifies genAI-first |
| 2 | Unit/identity/time conflicts dominate batch rework | Designs Measure suite |
| 3 | Authority-blind retrieval causes safety failures | Blocks naive RAG |
| 4 | Stale auth will be exploited if cache trusted | Zero Trust design |
| 5 | Hidden human review cost flips genAI ROI | FinOps |
| 6 | Supply “planning” tools currently side-effect | Hard gate design |
| 7 | PV clock disagreement drives compliance risk | Workflow B priority |
| 8 | Language inequity creates silent PV misses | Subgroup Measure |
| 9 | Automation bias will close gaps incorrectly | HITL design |
| 10 | 14-day AI outage is credible and must be manual-capable | Continuity |

---

## 10. AI FDE input sufficiency score

| AI FDE input | Score | What exists | What is missing |
|---|---|---|---|
| Business context | Strong | Case, board request, portfolio, KPI conflicts | Live strategy interviews |
| User workflow | Partial | Case narrative; starter anti-pattern; continuity reqs | Observed SME time-motion; true cycle times |
| Constraints | Strong | AI boundaries, decision rights, BR-01, hard gates, continuity | Jurisdictional legal opinions |
| Evidence (data, logs, research) | Partial | Rich synthetic CSVs, injects, fixtures, knowledge | Measured baselines; LF-verified full hash audit |
| Stakeholder needs | Partial | Stakeholder pack + 3 CSV rows + decision rights | Works council / site primary research |

**Overall framing mode: `hypothesis`**

Rule applied: User workflow Partial + Evidence Partial (critical baselines Missing) → do not claim `decision-ready`. Prompt 02 Answer must be a **testable recommendation / experiment**, not a locked genAI build mandate.

---

## Related thin DMAIC lens

See `dmaic_lens.md` in this folder (Measure + light Define only — not Prompt 09).
