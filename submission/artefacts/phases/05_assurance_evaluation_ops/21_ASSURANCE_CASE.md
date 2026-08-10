# Assurance Case

> Team3 Phase 5 artefact (template 21). Claims–arguments–evidence for assessed POC — **not** a validated GxP DSS assurance case.

## Document control

| Field | Entry |
|---|---|
| Team / owner | Team3 — Evaluation / GxP |
| Version / date | 1.0 / 2026-08-07 |
| Reviewers | Architecture; Security; Product |
| Status | Phase 5 — provisional (hypothesis) |
| Related | Prompt 12; Phase 3–4; D-012; RR-01…12 |

## Purpose

Support the decision: **demo conditional-go / production no-go** by structuring top claim, subclaims, evidence, defeaters, residual risk, and invalidation conditions.

## Evidence register

| Evidence ID | Source | Fact used | Limitation |
|---|---|---|---|
| E-AC-01 | `artefacts/prompts/12_assurance/*` | Eval report; residual risks; AC results | Prompt-era 25 tests; now 34 |
| E-AC-02 | `submission/tests/` pytest | Hard gates green | Fixture scope |
| E-AC-03 | Phase 3 RTM + contracts | Req→test map | AC-052 deferred |
| E-AC-04 | Phase 4 threat/privacy/Act | Security residuals; Q-EU-01 | No compliance claim |
| E-AC-05 | `tevv_suite_status.csv` | 12-suite honesty map | Most partial/inconclusive |
| E-AC-06 | DEFINITION_OF_DONE / SCORING | Hard fail-closed properties | Package |

## 1. Top claim

| Item | Response | Owner | Acceptance |
|---|---|---|---|
| **C0 (demo)** | AEGIS POC can assist batch/PV/supply evidence assembly under fail-closed AuthZ **without** performing prohibited regulated actions on package fixtures | Evaluation | Hard-gate pytest + evaluate pass |
| **C0′ (production)** | System is **not** assured as production GxP decision support or EU AI Act–classified product | Product / GxP | Explicit **no-go** until RR-01/02/05/09 cleared or sponsor-accepted |

## 2. Context and assumptions

| Item | Response |
|---|---|
| Framing | `hypothesis` — P0 cycle-time / review-hour baselines Missing |
| Data | Synthetic challenge fixtures (A-003) |
| AI | LLM off on assessed path (ADR-002) |
| Authority | Humans retain certification / final PV / allocation (D-007) |
| Scope | Local CLI/runtime under `submission/`; no enterprise IAM/MES |

## 3. Subclaims and arguments

| ID | Subclaim | Argument |
|---|---|---|
| C1 | Purpose-bound AuthZ fail-closed | IAM>cache; contractor_77 deny; audit fields |
| C2 | No autonomous disposition / final PV / side effects | Schema + SideEffectGuard + no write adapters |
| C3 | Untrusted docs/tools do not instruct or write | Quarantine; poisoned manifest not loaded |
| C4 | Deterministic continuity path exists | Mode controller; AI-disabled refuses narrator |
| C5 | Material ACs traced to tests | RTM + AC suite (excl. AC-052) |
| C6 | Residual risks disclosed; ROI not overclaimed | RR register; hypothesis; cost_model gap |

## 4. Evidence references

| Subclaim | Primary evidence |
|---|---|
| C1 | AC-001–003; authz_matrix; Phase 4 |
| C2 | AC-023/030/041–043; test_phase3_prohibited; ADR-003 |
| C3 | AC-010; RED_TEAM_RESIDUAL; INJ-065/066 |
| C4 | AC-050/051; ADR-001/002 |
| C5 | `09_REQUIREMENTS_TRACEABILITY.md`; pytest |
| C6 | residual_risk_register; scorecard; cost_model.csv |

## 5. Defeaters and counterevidence

| Defeater | Status | Handling |
|---|---|---|
| Board −14% proven by POC | **Undefeated for production** — baselines Missing | Block ROI claims (RR-01) |
| Continuity under 14-day outage | **Undefeated** — AC-052 deferred | RR-02 |
| Full 12 TEVV suites pass | **False** — see tevv_suite_status | RR-09; Phase 6 |
| Validated DSS / Act class clear | **False / abstain** | RR-05; Q-EU-01 |
| Fuzzy duplicates complete | Blocked by design | ADR-007 accepted FN risk |
| CRLF hash verify FAIL | Residual A-001 | Cite LF-normalize |

## 6. Residual risk

See Prompt 12 `residual_risk_register.md` (RR-01…12) and Phase 4 red-team residual. Phase 5 does **not** clear RR-01/02/05/09.

## 7. Invalidation and reapproval conditions

Reapprove / reopen C0 if any:

1. Write-plane or side-effect > 0 on assessed path  
2. AuthZ allow for revoked IAM user  
3. LLM call on assessed path without ADR-002 revisit  
4. Fuzzy auto-merge enabled without threshold ADR  
5. Production ROI claim without P0 baselines  
6. Challenge evidence mutated  

## Risks, assumptions and unresolved gaps

| ID | Type | Description | Status |
|---|---|---|---|
| R-AS-01 | Gap | Full CAE for production validation | Open — out of POC |
| R-AS-02 | Assumption | Fixture outcomes generalize to site data | Open |
| R-AS-03 | Risk | Sponsor pressure to treat C0 as C0′ | Open (R-002) |

## Traceability and acceptance

| Claim | Control | Test | Result |
|---|---|---|---|
| C0 demo assist fail-closed | Architecture + gates | pytest / evaluate | **Supported** |
| C0′ production assured | — | TEVV incomplete | **Not supported** |

## Review record

| Reviewer | Role | Finding | Resolution | Date |
|---|---|---|---|---|
| Team3 Evaluation | Owner | Split claim C0/C0′ | Aligns D-012 | 2026-08-07 |
