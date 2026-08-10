# Prompt 13 — DMAIC Lens (executive Control story)

**DMAIC focus:** What improved, what remains, what to fund next.

1. **Top wastes removed vs still open** (09 + control_lens_rollup / 12)
   - **Removed/prevented in PoC:** Defects (stale auth, unit silent-convert, untrusted instructions); Overproduction (quarantine-as-available, reservations); Model/token waste (LLM off); false fuzzy merges (blocked).  
   - **Still open:** Ops Waiting (multi-system hunt magnitude Unknown); Human-review cost Unknown; HITL queue depth unmeasured; Continuity drill; full TEVV/adversarial depth.

2. **Measure baselines sponsors must unlock**
   - P0 pack cycle-time (median/p90).  
   - P1 human review hours for TCO.  
   - AC-052 continuity drill evidence.  
   - (Optional later) fuzzy golden set; load p95.

3. **Control owners after handover**
   - Evaluation hard gates → Evaluation / Quality Systems.  
   - Side-effect / no-write → Architecture / Supply.  
   - AuthZ IAM>cache → Security / CISO.  
   - Mode/LLM-off → Architecture.  
   - Continuity → Ops.  
   - Claims/framing → Product / CQO.  
   (Detail: `12_assurance/control_lens_rollup.md` §5.)

4. **Next DMAIC loop**
   - **Measure loop first** (not continuous feature expansion): acquire P0/P1 baselines + continuity drill → re-Frame hypothesis→decision-ready → only then consider M2 harden / optional ADR-002.  
   - Owners must be staffed; do not imply autonomous CI without them.

5. **Pilot learnings (Prompt 11) that imply changes**
   - Treat safety receipts as first-class Clock Evidence.  
   - Name unapproved interface mapping as standing Contradiction type.  
   - Never trust package fuzzy scores for auto-merge.  
   - Expand AuthZ purpose↔role matrix beyond QP-only before multi-persona demo.
