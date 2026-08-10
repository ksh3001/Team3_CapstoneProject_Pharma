# Prompt 05 — DMAIC Lens (thin)

**DMAIC focus:** Analyze failure/rework paths + Improve by less wasteful specs.

1. **AC/BR preventing Defects or Extra processing**
   - AC-020/BR-023 stop silent unit conversion defects.
   - AC-010/BR-010–013 stop instruction-injection from untrusted docs.
   - AC-040–043/BR-040–043 stop supply overproduction side effects.
   - AC-001/BR-001 stop stale-auth defects.
   - AC-030–032 stop unlawful PV finals and silent clock picks.

2. **Exceptions → Waiting / Inventory (queues)**
   - AuthZ deny, quarantined docs, duplicate_manual_assessment, clock resolution reviews, conflicted_evidence packs — create human queues; risk-route in HITL (DDD) to avoid reviewing everything.

3. **Confidence/matching ambiguities → retries / false accepts / review waste**
   - AMB-PV-01 Unknown fuzzy threshold: fail closed (no auto-link) to avoid false accepts; may increase manual duplicate queue (Waiting) until threshold set.
   - AMB-PV-02 non-English always reviewed: prevents silent miss; adds review load (Measure later).

4. **Overproduction vs PRD scope**
   - No FR for autonomous disposition/allocation/LLM-mandatory RAG — deferred MDM programme is not a product FR.
   - Optional narrator kept out of assessed default (FR-006) to avoid token/process waste.
