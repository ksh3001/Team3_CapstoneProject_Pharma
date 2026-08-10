# GxP Lifecycle and Validation

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | GxP & quality lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Architecture lead; Security lead |
| Status | Draft — Stage 3 |
| Related requirements / ADRs | Artefacts 10–12; knowledge AI_GXP_BOUNDARY; COMPUTERISED_SYSTEM_LIFECYCLE; CSA artefact 14 |

## Purpose

State intended use, GxP relevance, lifecycle/validation approach, and electronic record/signature boundary for AEGIS as an **advisory evidence-reconciliation system** — not a disposition engine.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `knowledge/AI_GXP_BOUNDARY.md` | Approved policy extract | AI GxP boundary themes | Training extract |
| E-002 | `knowledge/COMPUTERISED_SYSTEM_LIFECYCLE.md` | Approved | Lifecycle expectations | Training extract |
| E-003 | `data/ai_use_boundaries.csv` | Boundary register | Allowed/prohibited | Binding |
| E-004 | `data/system_inventory.csv` | Inventory | AI-EVIDENCE=pilot; LIMS validated | Ambiguity pattern elsewhere |
| E-005 | `case/REGULATORY_BOUNDARY_PACK.md` | Boundary questions | Applicability method | Not legal advice |
| E-006 | `submission/artefacts/10_C4_ARCHITECTURE.md` | Stage 3 | Advisory containers | Draft |

## 1. Intended use

| Item | Statement |
|---|---|
| Intended use | Assist authorized users to reconcile and cite evidence for batch-review readiness, PV intake support, and draft supply options |
| Intended user | QP/QA reviewers, PV intake staff/physicians, supply planners under governance |
| Operating mode | Deterministic offline-capable assessment; optional model assist later behind ADR-011 |
| Out of intended use | Autonomous batch disposition, final PV decisions, stock reservation/allocation/shipment/recall, clinical eligibility determination |

## 2. GxP relevance and category

| Question (REGULATORY_BOUNDARY_PACK) | Answer for AEGIS v1 |
|---|---|
| Creates/modifies regulated records? | Produces **advisory** evidence packs + audit logs; does not write disposition/allocation to SoR |
| Influences quality/safety/supply decisions? | Yes — decision support only |
| Advisory vs determinative? | **Advisory / workflow-supporting**; human remains accountable |
| Validation posture | Risk-based CSA (artefact 14); higher rigor on fail-closed boundaries and audit |

## 3. Lifecycle controls

| Phase | Control |
|---|---|
| Concept / requirements | Artefacts 01–09; inject map |
| Design | Artefacts 10–12; ADRs |
| Build / verify | Stage 5 tests before inference; schema gates |
| Operate | Authz at execution; audit; AI-disabled continuity |
| Change | Model/prompt/tool/config under change control (Stage 4 artefacts) |
| Retire | Retain prompts/versions/decisions/validation evidence (INJ-084) |

## 4. Electronic records / signatures boundary

| Topic | Position |
|---|---|
| AEGIS pack | Electronic record of assessment; not e-signature for batch certification |
| Certification / reportability | Remain in validated SoR + human signature processes outside AEGIS |
| Audit trail | Required for AEGIS assessments (who/what/when/as-of/authz) |
| Part 11 / Annex 11 | Applicability assessed where AEGIS records are relied upon in GxP processes — document assumptions per jurisdiction (Stage 4 regulatory artefacts) |

## 5. Data integrity expectations

| Expectation | Implementation link |
|---|---|
| ALCOA+ on citations | evidence_item.schema; artefact 06 |
| No silent unit conversion | ADR-008 |
| No use of untrusted docs as instructions | ADR-006 |
| Conflicts preserved | readiness_state conflicted_evidence / abstentions |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Assumption | Advisory classification accepted by Quality | May require tighter validation if reclassified | CQO | Validation plan | Open |
| R-002 | Gap | Full IQ/OQ/PQ scripts not yet written | Expected Stage 5–6 | GxP | Build | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Intended/prohibited use explicit | §1 | Hard-gate tests | E-003 | Draft |
| No SoR disposition writes | C4 + ADR-004 | Integration review | E-006 | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Architecture lead | Reviewer | Aligns with read-only adapters | Confirmed | 2026-08-07 |
