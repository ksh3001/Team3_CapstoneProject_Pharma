# ISO/IEC 42001 Governance Alignment

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Security / privacy lead + Product lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Architecture lead; GxP lead |
| Status | Draft — Stage 4; alignment analysis not a certification claim |
| Related requirements / ADRs | LOCAL_REGULATORY guide AI governance; artefacts 13–19; ADR-001/011/012 |

## Purpose

Map AEGIS controls to ISO/IEC 42001-aligned AI management themes (intended use, roles, risk, lifecycle, suppliers, evaluation, incident, retirement) proportionate to this workshop system.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `sources/LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md` | Local guide | AI governance expectations | Training summary |
| E-002 | `knowledge/AI_MODEL_CHANGE_CONTROL.md`; `AI_INCIDENT_RESPONSE.md`; `AI_DISABLED_CONTINUITY.md` | Policy extracts | Change/incident/continuity | Approved extracts |
| E-003 | `submission/artefacts/11_ADR_REGISTER.md` | Stage 3 | Decision memory | Draft |
| E-004 | `submission/artefacts/16_THREAT_ABUSE_MODEL.md` | Stage 4 | Threat controls | Draft |
| E-005 | `data/vendor_dependencies.csv`; `vendor_exit_assets.csv` | Vendor | Concentration / exit (INJ-078/083) | Challenge |

## 1. AI management system themes → AEGIS evidence

| Theme | AEGIS artefact / control | Gap |
|---|---|---|
| AI policy / intended use | Artefacts 04, 13, 19 | Production policy sign-off TBD |
| Roles & accountability | Artefact 03; team charter | Org RACI beyond team |
| Risk assessment | Artefacts 15, 16, 17 | Ongoing review cadence |
| Objectives & performance | Artefacts 01–02 Measure plan | Baselines Unknown |
| System impact assessment | This Stage 4 set | Formal AIA template TBD |
| Lifecycle | Artefact 13 | Full SOPs Stage 7 |
| Data management | Artefacts 06–07 | Master-data program |
| Technical documentation | Artefacts 09–12 | Code/docs Stage 5 |
| Record keeping | Audit fields; evidence/ | Retention ops |
| Supplier / third party | ADR-011 proposed; vendor injects | Exit plan Stage 7 (27) |
| Human oversight | Artefact 18 | UI Stage 5 |
| Transparency | Citations/uncertainty in contracts | UX |
| Evaluation | Planned Stage 6 (22) | Not yet |
| Incident & continuity | Knowledge extracts; ADR-012 | Runbooks Stage 7 |
| Retirement | INJ-084 acknowledged | Artefact 27 later |

## 2. Operating model for AI changes

| Change type | Gate |
|---|---|
| Prompt / model / tool / schema | Change control + re-test hard-gate suite |
| Enable model assist (ADR-011) | FinOps includes human review; threat re-run; Evaluation gate |
| New data source | Authority/trust onboarding (artefact 06) |

## 3. Statement of conformity posture

AEGIS workshop delivery **aligns controls to 42001 themes** but does **not** claim certified ISO/IEC 42001 conformity. Certification would require organizational AIMS scope beyond this repository.

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | No formal internal AI policy document beyond artefacts | Org adoption | Product | Stage 7 TOM | Open |
| R-002 | Risk | Vendor concentration (INJ-078) if cloud stack added | Exit difficulty | Architecture | Before cloud | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| Themes mapped | §1 | Review | This artefact | Draft |
| No false certification claim | §3 | Defence language | This artefact | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Product lead | Reviewer | Explicit non-certification | §3 | 2026-08-10 |
