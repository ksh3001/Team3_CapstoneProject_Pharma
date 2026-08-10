# PoC vs Production Gaps

| Area | Demonstrated in PoC | Still required for production |
|---|---|---|
| AuthZ | IAM CSV > cache; qp_eu_1 / contractor_77 | Real IAM/OIDC; object-scope grants; entitlement schema |
| Documents | Catalog status/trust filter | Controlled DocMgmt API; jurisdiction SoT; signature/hash verify |
| Batch | LR-88 unit conflict; readiness enum; no disposition | Full genealogy/EM/sterility checklist; MES ACL SLA |
| PV | Exact/strong_key; dual clocks; no finals | Fuzzy after golden set; MedDRA coding service; multilingual metrics |
| Supply | Released-only options; SideEffectGuard | Approved write plane ADR + human execution systems |
| Continuity | AI-disabled refuse narrator; deterministic path | Executed 14-day drill evidence (AC-052) |
| Evaluate | Hard gates on package fixtures | Full 12-suite TEVV / graders / public fixtures |
| Measure | Per-request metrics JSON | Ops cycle-time baseline; review-hour measured TCO |
| Runtime | CLI dispatch localhost | Hardened HTTP, authn, rate limits, observability stack |
| Package integrity | Proceed despite CRLF verify FAIL | LF-normalized hash audit (A-001) |
| Claims | Assist-only; hypothesis framing | No “validated GxP DSS” until AI-EVIDENCE state resolved |
