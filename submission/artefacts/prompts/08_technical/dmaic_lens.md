# Prompt 08 — DMAIC Lens (thin)

**DMAIC focus:** Improve contracts; Measure/Control NFRs.

1. **Token / Retrieval / Context caps**
   - NFR-01 LLM calls = 0 assessed; NFR-13 ≤32 knowledge docs scanned; Applicable-only return; Narrator off (ADR-002).

2. **Error/retry vs Model waste**
   - No blind model retries; mode_violation 503; deterministic path does not retry LLM.
   - Idempotency prevents duplicate side-effect attempts (none allowed anyway).

3. **Measurable Control metrics for Prompt 12**
   - NFR-02 side effects 0; NFR-03 authz deny 100%; NFR-04/05 schema/prohibited 100%; NFR-11 audit 100%; latency p95 ≤30s (NFR-06–08).

4. **Open ambiguities that would cause Extra processing at build**
   - AMB-PV-01 fuzzy **open-blocked** (prevents thrash).  
   - Assumed items documented so agents do not invent thresholds.
