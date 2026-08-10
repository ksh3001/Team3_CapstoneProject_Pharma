# Computer Software Assurance

> Participant working template. Prompts define expected evidence but do not provide an answer. Replace bracketed guidance with your own analysis and cite challenge or submission evidence.

## Document control

| Field | Entry |
|---|---|
| Team / owner | GxP & quality lead |
| Version / date | 0.1 / 2026-08-07 |
| Reviewers | Evaluation lead; Architecture lead |
| Status | Draft — Stage 3 |
| Related requirements / ADRs | Artefact 13; ADR-003; artefact 09 ACs; FDA CSA guidance as research anchor only |

## Purpose

Apply a risk-based Computer Software Assurance approach proportionate to AEGIS’s advisory role: assure critical fail-closed behaviors heavily; avoid theatre documentation for low-risk UI chrome.

## Evidence register

| Evidence ID | Source path / record | Authority and effective time | Fact used | Integrity / limitation |
|---|---|---|---|---|
| E-001 | `submission/artefacts/13_GXP_LIFECYCLE_VALIDATION.md` | Stage 3 | Intended use advisory | Draft |
| E-002 | `submission/artefacts/09_REQUIREMENTS_TRACEABILITY.md` | Stage 2 | AC-001–011 | Draft |
| E-003 | `tools/test_contracts.py` | Package | Schema positive/negative | PASS |
| E-004 | `sources/LOCAL_REGULATORY_AND_STANDARDS_GUIDE.md` | Local guide | Risk-based assurance does not remove accountability | Training summary |
| E-005 | `data/validation_inventory.csv` / `validation_tests.csv` | Estate evidence | Brownfield validation inconsistency exists | Challenge condition |

## 1. Risk-based assurance strategy

| Feature / function | Process risk if wrong | Assurance level | Assurance activity |
|---|---|---|---|
| Schema fail-closed / prohibited fields | High — regulated overreach | High | Contract negatives; static review of models |
| Authz deny stale entitlement | High — unauthorized access | High | Negative entitlement tests |
| Unit conversion / abstention | High — wrong lab conclusion support | High | INJ-024 style tests |
| Duplicate candidate only | High — silent case merge | High | PV negatives + unit tests |
| Supply no_side_effects | High — unintended allocation | High | Supply negatives |
| Evidence citation presence | High — fabricated facts | High | Graders + fixture tests |
| Readiness enum only | Medium–High | High | Schema enum tests |
| Optional model summarization | Medium (if enabled) | Medium | Golden/adversarial; off by default |
| UI presentation | Lower if contracts hold | Medium/Low | Exploratory + a11y checks |

## 2. Unscripted / exploratory testing

| Area | Approach |
|---|---|
| Conflict-rich batches | Exploratory on PUB-01/02 style packs |
| Malicious document | PUB-03 / INJ-065 |
| Offline mode | Operate with model adapter disabled |

## 3. Scripted / automated testing

| Suite | Maps to |
|---|---|
| `tools/test_contracts.py` | AC-001/002/004–007 foundation |
| Stage 5 `submission/tests/` | AC-003, AC-008–011 + inject fixtures |
| Stage 6 evaluation | Subgroup, outage, FinOps gates |

## 4. Supplier / brownfield software

| System | Assurance note |
|---|---|
| LIMS/MES/QMS | Remain under their owners’ validation; AEGIS consumes exports/CSV snapshots |
| AI-EVIDENCE pilot | Not treated as validated SoR; AEGIS assessment mode must not depend on it |
| Model vendor (if used) | Supplier assessment + hash/signature (INJ-070); ADR-011 proposed |

## 5. CSA evidence package (planned)

| Evidence | Location |
|---|---|
| Intended use | Artefact 13 |
| Requirements/AC | Artefact 09 |
| Architecture/ADRs | Artefacts 10–11 |
| Test results | submission/evidence + evaluation |
| Residual risk | Artefact 15 + Stage 4 assurance case |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Due / trigger | Status |
|---|---|---|---|---|---|---|
| R-001 | Gap | Full CSA protocol document not yet formalized | Needed before production claim | GxP | Stage 7 | Open |
| R-002 | Risk | Estate validation_inventory inconsistency confuses boundary | Mis-tiering | GxP | Clarify per component | Open |

## Traceability and acceptance

| Claim / requirement | Architecture or control | Test / evaluation | Evidence path | Result |
|---|---|---|---|---|
| High-risk functions identified | §1 | Contract tests PASS | E-003 | Partial |
| Assurance proportionate | §1–3 | Review C3 | This artefact | Draft |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Evaluation lead | Reviewer | Contract suite accepted as Stage 3 gate | Logged | 2026-08-07 |
