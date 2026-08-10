# Prompt 07 — DMAIC Lens (thin)

**DMAIC focus:** Analyze trade-offs; Control via validation + revisit triggers.

1. **ADRs preventing named waste**
   - ADR-001/002 → Model/token waste and Defects from premature genAI.  
   - ADR-003 → Overproduction (fake reservations) and Defects.  
   - ADR-004 → Security/Defects from stale auth.  
   - ADR-007/009 → Defects from false merges / silent clocks (may increase Waiting — accepted).  
   - ADR-008 → Extra processing from untyped lake / silent unit convert.  
   - ADR-010 → Inspection rework (Extra processing) from missing audit.

2. **Decisions risking new Waiting / review / token waste**
   - ADR-007/009 increase HITL queues (Waiting) — Control by measuring queue depth.  
   - ADR-002 if enabled early → token + bias review waste — revisit gated on Measure.

3. **Validation + revisit as Control**
   - Each ADR lists tests and quantified revisit triggers (side-effect=0, fuzzy=0, revoke allow=0, etc.).

4. **Review open issues as waste risks**
   - Missing baselines → risk of Overproduction (building genAI before Measure).  
   - Write-plane pressure → critical Defect/Overproduction if smuggled — treated as blocker.
