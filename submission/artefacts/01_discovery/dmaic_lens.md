# Prompt 01 — DMAIC Lens (thin)

**DMAIC focus this stage:** Measure (baseline signals) + light Define.  
**Not** Prompt 09 full waste workshop.

1. **What can already be measured (package-local):**
   - Prohibited-output contract pass/fail (`tools/test_contracts.py` / contract samples)
   - Presence and counts: 84 injects; 139 profiled datasets; 32 knowledge docs
   - Concrete conflict rows: LR-88 unit/spec mismatch; unapproved interface mapping; revoked+cached user; quarantine inventory units; AI-EVIDENCE triple validation state
   - Cost signals: inference 184000 USD/mo; observability 31000; human review lines currently 0
   - Continuity flags in `continuity_requirements.csv`

2. **Baselines Unknown:**
   - Median / p90 release-pack cycle time
   - True PV intake rework rate and clock-slip frequency in operations
   - Actual human review hours per pack
   - Token use of any future model path
   - Complete LF-normalized package hash audit on this checkout

3. **Top 3 early waste signals** (see `early_waste_signals.md`):
   - Extra processing / waiting across brownfield systems — **hypothesized**
   - Defects from lexical ready + unit mapping failures — **observed**
   - AI retrieval / equal-trust document waste (incl. malicious SOP) — **observed** pattern

4. **What Prompt 09 must Measure before scaling automation:**
   - Cycle-time proxies and conflict-flag correctness (dual citation, no silent merge)
   - Prohibited-action block rate and side-effect absence (esp. supply)
   - Human review hours × `staff_rates.csv`
   - AI-disabled continuity drill completion
   - AuthZ deny on stale cache / untrusted instructions
