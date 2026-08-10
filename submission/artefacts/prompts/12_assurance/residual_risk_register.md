# Residual Risk Register (updated)

| ID | Risk | Likelihood × impact (qual) | Disposition | Owner | Link |
|---|---|---|---|---|---|
| RR-01 | Ops cycle-time / review-hour Unknown → wrong ROI / board −14% claim | H×H | **Accepted for demo**; block production claims | Product | Evidence backlog P0 |
| RR-02 | AC-052 continuity drill not executed | M×H | **Deferred** Phase 7 | Ops / Team3 | AMB-CONT-01 |
| RR-03 | Thin AuthZ role model (QP-only) | M×M | **Accepted POC**; fix before multi-role demo | Security | D-A01 |
| RR-04 | AMB-PV-01 fuzzy disabled → duplicate FN | M×M | **Accepted** fail-closed | PV BC | ADR-007 |
| RR-05 | AI-EVIDENCE validation triple-state | M×H | **Accepted** — no validated DSS claim | GxP | Architecture review |
| RR-06 | CRLF package hash verify FAIL | L×M | **Accepted** residual A-001 | Build | AMB-DOC-02 |
| RR-07 | Write-plane pressure smuggled later | L×H | **Blocked** without ADR reopen | Architecture | ADR-003 |
| RR-08 | Premature LLM/narrator enable | M×H | **Blocked** until ADR-002 revisit | Mode Controller | ADR-002 |
| RR-09 | Incomplete TEVV / adversarial suites vs DoD §5 | H×H | **Deferred** Phase 6 | Evaluation | poc_vs_production |
| RR-10 | P1 clock dictionary incomplete | M×M | **Assumed** dual-cite interim | Data stewardship | ADR-009 |
| RR-11 | Object-scope entitlement ambiguity | M×M | Fail-closed assumed | Security | AMB-AUTHZ-01 |
| RR-12 | Performance NFR p95 unproven under load | M×L | `inconclusive (data scarcity)` | Architecture | NFR-06–08 |

**Sponsor decisions required (Prompt 13):** accept RR-01/05 for any path beyond demo; approve data access for P0 baselines; never production-go while RR-01/02/05/09 remain unmitigated without explicit acceptance.
