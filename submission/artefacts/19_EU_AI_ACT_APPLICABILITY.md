# EU AI Act Applicability

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Security / privacy lead + GxP lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | Architecture lead; Product lead |
| Status | Draft — Stage 4; **not legal advice** |
| Related requirements / ADRs | `sources/LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md` applicability method; artefact 13; REG_BOUNDARY_PACK |

## Purpose

Apply the local guide’s 11-field applicability method to AEGIS’s intended use and state provisional EU AI Act posture with assumptions and residual uncertainty. External links remain optional research anchors.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `sources/LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md` | Local training guide | Applicability method § | Not legal advice |
| E-002 | `case/REGULATORY_BOUNDARY_PACK.md` | Boundary pack | Boundary questions | Research anchors |
| E-003 | `submission/artefacts/13_GXP_LIFECYCLE_VALIDATION.md` | Stage 3 | Advisory intended use | Draft |
| E-004 | `data/ai_use_boundaries.csv` | Boundaries | Prohibited autonomous decisions | Binding |
| E-005 | `sources/REFERENCE_SOURCES.md` | Optional links | EU AI Act listed as research | Verify current law |

## Applicability method (11 fields) — AEGIS v1 assessment mode

| Field | Entry |
|---|---|
| 1. Jurisdiction | EU (NTG DE sponsor/MAH context) + multi-region ops; EU AI Act analysis scoped to EU placing/use assumptions |
| 2. Product / process | Advisory evidence reconciliation for batch readiness, PV intake support, supply draft options |
| 3. Intended purpose | Decision support with human accountability retained; offline deterministic assessment |
| 4. Advisory vs determinative | **Advisory / workflow-supporting** — not determinative for release, PV final, allocation |
| 5. Human accountability | EU QP; Safety Physician; Supply Governance Board (artefact 03) |
| 6. Regulated-record boundary | Assessment packs + audit logs; certification/reportability remain outside AEGIS |
| 7. Affected decision | Influences what humans review; must not execute prohibited decisions |
| 8. Applicable date/version | Analysis as-of 2026-08-10; law/guidance must be re-verified before production |
| 9. Evidence source | E-001–E-004; case packs |
| 10. Assumption | If used only as documented advisory tool with effective human oversight, high-risk “safety component of medical device” style paths are out of scope for v1; **reassess if role becomes determinative** |
| 11. Residual uncertainty | Classification under EU AI Act can change with deployment context, sectoral rules, and amendments — **legal review required** |

## Provisional classification stance

| Stance | Statement |
|---|---|
| Working hypothesis | AEGIS v1 is an AI-enabled (or AI-optional) **decision-support** system with prohibited uses documented; not authorized for autonomous high-risk regulated conclusions |
| Prohibited AI practices | Do not deploy manipulative or social-scoring uses; not in scope of AEGIS |
| Transparency / oversight | Cite evidence; show uncertainty; human review required fields |
| If model assist enabled (ADR-011) | Re-run this artefact; document GPAI/provider obligations if applicable |
| Stop condition | Any design change that makes AEGIS outputs automatically execute release/PV/allocation → **reclassify + stop** |

## Obligations mapped to controls (provisional)

| Theme | AEGIS control |
|---|---|
| Human oversight | Artefact 18; contract human_review |
| Data governance | Artefacts 06–07 |
| Robustness / accuracy | CSA artefact 14; evaluation Stage 6 |
| Cybersecurity | Artefact 16 |
| Logging | Audit on responses |
| Risk management | Artefact 15 + 21 |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Assumption | Advisory classification holds | Wrong if product uses AEGIS as auto-disposition | CQO/Legal | Before production | Open |
| R-002 | Gap | Formal legal opinion not obtained | Expected for workshop | Legal | Pre-production | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| 11-field method applied | Table above | Review | E-001 | Draft |
| Determinative use blocked | Schemas + ADRs | Prohibited-action tests | E-004 | PASS Stage 4 |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| GxP lead | Reviewer | Uncertainty and legal review explicit | § Residual uncertainty | 2026-08-10 |
