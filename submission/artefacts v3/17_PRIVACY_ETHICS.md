# Privacy and Ethics

> Phase 4. Purpose limitation, DSR vs GxP hold, residency. Awareness design — not legal sign-off.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team-3 / Security–privacy lead |
| Version / date | 0.1 / 2026-08-10 |
| Reviewers | GxP; Product; Architecture |
| Status | Draft |
| Related requirements / ADRs | INJ-061…064; trust-risk-security skill; artefact 05 Privacy context |

## Purpose

Define privacy/ethics constraints for the three workflows so the assist cannot silently delete GxP-required records, export across residency breaks, or reuse data outside declared purpose.

## Evidence register

| Evidence ID | Source | Fact used |
|---|---|---|
| E-001 | INJ-061 / deletion_requests; retention_rules | DSR vs GxP retention conflict |
| E-002 | INJ-062 / patient_support_cases | PSP leakage risk |
| E-003 | INJ-063 / data_licenses; commercial_use_requests | Research–commercial boundary |
| E-004 | INJ-064 / data_residency; backup_inventory | Residency failure |
| E-005 | Package scope | Synthetic offline training data |
| E-006 | decision_rights / ai_use_boundaries | Purpose-bound assist |

## 1. Purpose and data map

| Workflow | Declared purpose examples | Data classes touched |
|---|---|---|
| Batch evidence | Quality release review support | Batch, lab, EBR, deviations (GxP) |
| PV intake | Safety case intake support | ICSR-like, clocks, listedness |
| Supply options | Shortage/cold-chain planning support | Inventory, quality holds, constraints |

**Rule:** Request must carry `purpose`; mismatched purpose → deny/abstain (C-SEC-05).

## 2. Permission/consent assumptions

| Assumption | Status |
|---|---|
| Assessed mode uses synthetic/challenge data only | A-001 Accepted |
| Real patient consent stacks are out of POC scope | Open legal (escalate) |
| Operator entitlements ≠ consent for secondary use | Binding design rule |

## 3. Minimisation and pseudonymisation

| Control | Behaviour |
|---|---|
| Field minimisation | Return only facts needed for the workflow package |
| No training on prod logs | Capstone: no real PII in prompts |
| Pseudonymisation | Prefer case/batch IDs already in vignette; no new free-text dumps to model |
| Verbatim uncertainty | Preserve; do not “clean” identifiers into golden records |

## 4. Secondary use and re-identification

| Risk | Control |
|---|---|
| PSP → commercial reuse (INJ-062/063) | License/purpose check; abstain if commercial flag on research-restricted |
| Rich PV narrative re-ID | Keep in structured fields; discourage free-text model echo |
| Cross-workflow bleed | Separate request contexts; no ambient session memory of other purposes |

## 5. Residency and cross-border controls

| Rule | Behaviour |
|---|---|
| Residency constraint present (INJ-064) | Flag gap; deny cross-region export/backup actions |
| Offline POC | Local package only — no cloud sync in assessed mode |
| Future cloud | Separate ADR; residency matrix required before enable |

## 6. Rights, retention and legal hold

| Conflict | Design (INJ-061) |
|---|---|
| DSR erasure vs GxP retention | **Do not auto-erase**; surface conflict; human Privacy + GxP decide |
| Retention rule active | Preserve evidence; log DSR request as case |
| Assist role | Package the conflict; never silent delete |

## 7. Ethical trade-offs and oversight

| Trade-off | Choice |
|---|---|
| Speed vs privacy review | Privacy conflicts fail closed even if board lead-time pressure |
| Model usefulness vs leakage | Assessed scoring path LLM-off or tightly ported |
| Oversight | Privacy lead + GxP for hold/DSR; Security for residency |

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Impact | Owner | Status |
|---|---|---|---|---|---|
| R-411 | Gap | No formal DPIA (synthetic POC) | Production gap | Privacy | Open |
| A-022 | Assumption | Synthetic data removes live DPDP/GDPR ops burden for scored path | Wrong if real data introduced | Privacy | Accepted for POC |

## Traceability and acceptance

| Claim | Control | Test | Result |
|---|---|---|---|
| DSR ≠ auto-delete | §6 | `test_dsr_vs_gxp_hold_no_auto_erase` | RED |
| Residency break surfaced | §5 | `test_residency_violation_denies_export` | RED |
| Purpose binding | §1 | `test_purpose_mismatch_denied` | RED |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| TBD | Privacy + GxP | Pending | | |
