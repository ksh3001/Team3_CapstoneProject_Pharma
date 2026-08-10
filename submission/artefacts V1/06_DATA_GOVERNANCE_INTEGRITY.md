# Data Governance and Integrity

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Domain & evidence lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | GxP lead; Security lead |
| Status | Draft — Workshop Stage 2 |
| Related requirements / ADRs | Stage 2 exit (evidence map); Prompt 04; INJ-021–036, 045, 059–064, 067, 070 |

## Purpose

Define source authority, identity/unit/time handling, ALCOA+ risks, lineage, and retention conflicts for AEGIS — and provide the Stage 2 **evidence map** across inject clusters for the three workflows.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `case/SOURCE_SYSTEM_FACT_PACK.md` | Case | Systems + conditions; contextual authority | Synthetic |
| E-002 | `data/inject_evidence_map.csv` | Package (84 injects) | Inject → evidence_sources | participant_status was UNASSESSED |
| E-003 | `data/RELATIONSHIP_MODEL.csv` | Package | Declared relationships | Structural |
| E-004 | `data/interface_mappings.csv` | Interface | mg/L→ug/mL approved=no | Unapproved |
| E-005 | `data/users_entitlements.csv` | IAM/gateway | contractor_77 revoked + active_cached | Stale auth |
| E-006 | `data/model_artifacts.csv` | Registry | Hash mismatch; signature missing | Supply-chain |
| E-007 | `data/knowledge_catalog.csv` | Catalog | Untrusted + superseded docs present | Mixed trust |
| E-008 | `data/retention_rules.csv`; `legal_holds.csv`; `deletion_requests.csv` | Retention/hold/DSR | Retain vs delete vs LH-44 vs DSR-17 | Conflict |
| E-009 | `data/product_master_aliases.csv`; `idmp_mappings.csv` | Identity | Aliases; ambiguous IDMP strength/presentation | Conflict |
| E-010 | `PACKAGE_SCOPE_AND_ASSUMPTIONS.md` | Scope | Do not silently clean deliberate conflicts | Binding |

## Stage 2 evidence map (inject clusters)

Status values for this stage: `IN_SCOPE_v1` (must be handled by three workflows / controls), `DEFER` (acknowledge; not v1 automation), `POLICY` (constraint only).

| Cluster | Inject IDs (representative) | Primary evidence sources | Workflow / control | Status |
|---|---|---|---|---|
| Board / no-AI / KPI | INJ-001–006 | board_requests; no_ai_baselines; kpi_conflicts; ai_use_boundaries | Business constraints | POLICY |
| Batch genealogy / lab / EM | INJ-021–028 | batches; material_genealogy; lab_results; oos; ebr; release_packets; EM/micro | Batch | IN_SCOPE_v1 |
| Data integrity / validation | INJ-029–036 | audit_trails; access_logs; spreadsheets; CAPA; change_controls; certificates | Batch + cross-cut | IN_SCOPE_v1 |
| PV intake / signal support | INJ-037–044 | icsr_cases; duplicates; safety_receipts; MedDRA; listedness; complaints | PV | IN_SCOPE_v1 |
| Supply / cold-chain / shortage | INJ-051–058 | shipments; loggers; serialisation; inventory; CMO; allocation_constraints; recall_candidates | Supply | IN_SCOPE_v1 |
| Identity / IDMP / labels | INJ-045–046, 008 | idmp_mappings; product_labels; aliases; compounds | Cross-cut | IN_SCOPE_v1 |
| Auth / tools / untrusted docs | INJ-065–070 | knowledge_catalog; tool manifests; entitlements; model_artifacts | Security cross-cut | IN_SCOPE_v1 |
| Privacy / residency / DSR | INJ-059–064 | genomic; consents; retention; residency; DSR | Privacy cross-cut | IN_SCOPE_v1 (controls); DEFER deep genomics product |
| Clinical protocol / eligibility | INJ-013–020 | protocols; eligibility; randomization; consents | Linked evidence only | DEFER automation |
| Continuity / FinOps / retirement | INJ-075–084 | cost_model; continuity; vendor_exit; retirement | NFR / Stage 6–7 | POLICY → later stages |
| Inspection surge | INJ-050 | inspection_requests | All workflows evidence export | IN_SCOPE_v1 |

Full 84-row machine list remains in `data/inject_evidence_map.csv` (immutable). Participant assessment progresses via this cluster map + artefacts 05–09; do not edit the challenge CSV.

## 1. Dataset inventory and classification

| Item / question | Evidence-based response | Decision / owner | Acceptance evidence |
|---|---|---|---|
| Inventory | Challenge `data/*.csv` + dictionary/profile/relationships; 32 knowledge docs catalogued | Domain | E-002, E-003, E-007 |
| GxP critical sources | LIMS/MES/eBR/QMS/safety/serialization | GxP | E-001 |
| Pilot / research | AI-EVIDENCE pilot; BIOX-ELN research-only | Digital/Research | system_inventory |
| AEGIS outputs | Advisory packs — not disposition SoR | GxP | ai_use_boundaries |

## 2. Source authority by object/context/time

| Object | Candidate authority | Rule |
|---|---|---|
| Lab result value | LIMS (+ approved interface mapping) | Unapproved mapping → abstain |
| Batch genealogy | MES + warehouse; gaps flagged | Missing branch = gap not invent |
| Effective quality policy | Approved knowledge with effective date; supersession honored | Superseded/untrusted not instructions |
| PV awareness | All receipt events preserved | No auto-pick without documented rule + human |
| Product identity | Canonical product + aliases; IDMP may be ambiguous | Abstain if unresolved for decision |
| Entitlement | IAM current state at execution | Cache not authoritative |

## 3. Identity and master-data conflicts

| Conflict | Evidence | Handling |
|---|---|---|
| Product aliases | product_master_aliases (NCB204, brand_alias_B → NCB-204) | Normalize with provenance |
| IDMP ambiguous | idmp_mappings mapping_status=ambiguous_strength_presentation | Flag; no silent fix |
| Acquisition IDs | organisations BioXen; INJ-005/008 | ACL + alias; no merge |
| MedDRA dual versions | terminology_versions 27.1 legacy vs 28.0 current | Keep version on coded terms |

## 4. Quality and ALCOA+ assessment

| Finding | ALCOA+ break | Evidence |
|---|---|---|
| Unapproved unit conversion | Accurate / Contemporaneous risk | E-004 |
| Shared accounts / audit gap | Attributable | INJ-029/030 |
| Transcribed certificate | Original / Accurate | INJ-036 |
| Model hash mismatch | Integrity | E-006 |
| Untrusted knowledge as SOP | Enduring / attributable policy break | E-007 |

## 5. Lineage and transformation controls

| Control | Requirement |
|---|---|
| Preserve | source, authority, effective date, version, time precision, unit, verbatim, uncertainty |
| Transform | Record; never overwrite challenge evidence |
| Relationships | Honor RELATIONSHIP_MODEL for referential checks; business conflicts remain |

## 6. Retention, residency and legal hold

| Tension | Evidence | Method |
|---|---|---|
| GxP retain vs privacy delete vs hold vs DSR | E-008 | Restriction/segregation over blind delete when LH-44 / GxP applies |
| Cross-border backup | INJ-064 | Flag residency failure; no silent relocate in AEGIS |

## 7. Stewardship and issue remediation

| Domain | Steward | Remediation example |
|---|---|---|
| Lab interfaces | QC + Integration | Approve or block CRO_LAB_TO_LIMS |
| Entitlements | CISO | Deny active_cached when IAM revoked |
| Knowledge | Quality docs owner | Exclude untrusted from instruction path |
| AEGIS defects | Digital + Quality | CAPA in eQMS — AEGIS does not close CAPA |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Not every inject has a per-row assessment status written back (CSV immutable) | Track in submission only | Domain | Ongoing | Open |
| R-002 | Risk | Treating RELATIONSHIP_MODEL as business truth | Miss intentional conflicts | Domain | Every design | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Evidence map for Stage 2 | Cluster table above | Checkpoint C2 | This artefact | Draft |
| Unapproved units blocked | §2–4 | Negative tests (Stage 5) | E-004 | Pending |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Security lead | Reviewer | Stale auth + untrusted docs in map | Included INJ-065–070 cluster | 2026-08-07 |
