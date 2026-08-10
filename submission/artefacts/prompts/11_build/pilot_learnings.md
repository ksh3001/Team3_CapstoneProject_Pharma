# Pilot Learnings (DDD stage 15)

What this pilot would change in domain model / features / contracts:

1. **Safety receipts as first-class Clock Evidence** — `safety_receipts.csv` (channel/receipt) is the practical dual-clock source for PV-1001; domain model should name ReceiptClock alongside awareness_date (ADR-009 already fits).
2. **Interface mapping as standing Conflict producer** — unapproved `interface_mappings` rows should be a named Contradiction type in BC-BATCH (already emitted; promote to ubiquitious language).
3. **Fuzzy duplicate CSV is poison if trusted** — package `duplicate_candidates.csv` scores must never drive auto-merge; keep as optional HITL hint only until AMB-PV-01 closes.
4. **Role vocabulary thin in package** — only `qualified_person` and `supplier_quality_viewer` appear; production needs purpose↔role matrix in BC-AUTHZ, not hard-coded POC allow for QP alone.
5. **Readiness vs disposition language held** — implementing `readiness_state` without disposition fields reduced ambiguity; keep glossary enforcement in contracts.
6. **Measure hooks cheap; baselines still Missing** — instrumentation shipped; framing stays hypothesis until cycle-time/review-hour acquisition.
7. **No domain pressure yet for write plane** — SideEffectGuard + schema bans sufficient for slice; do not reopen C4 for WMS writes.
