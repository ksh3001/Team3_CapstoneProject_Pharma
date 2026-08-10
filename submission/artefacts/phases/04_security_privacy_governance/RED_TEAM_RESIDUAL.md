# Red-Team Residual Risk (Phase 4)

| Field | Entry |
|---|---|
| Date | 2026-08-07 |
| Scope | Assessed POC hard-gate + phase3 prohibition/poison suite |
| Not in scope | Full Evaluation Plan privacy leakage suite; production SSO/pen-test |

## Exercised (evidence exists)

| Abuse class | How exercised | Result |
|---|---|---|
| Entitlement revoke lag | AC-001; authz_matrix; contractor_77 | Deny |
| Malicious / poisoned doc | phase3 + AC-010 | Quarantine / exclude |
| Poisoned tool manifest | phase3 | Not loaded |
| Disposition / PV final / reservation | phase3 + AC-023/030/043 | Reject / block |
| LLM on assessed path | AC-051 | Refused |

## Not fully exercised — residual acceptance

| Gap | Residual | Acceptance |
|---|---|---|
| Cross-affiliate exfil campaign beyond fixtures | Med | Accepted for Phase 4; Phase 6 TEVV |
| Production remote-access / OAuth abuse | High if exposed | Prod **no-go** (D-012) |
| Continuity under ransomware drill (AC-052) | Med | Phase 7 |
| Automation-bias UX with live narrator | Med | Narrator stays off |

Owner: Security / Evaluation. Invalidation: any write-plane or LLM-on-assessed enablement.
