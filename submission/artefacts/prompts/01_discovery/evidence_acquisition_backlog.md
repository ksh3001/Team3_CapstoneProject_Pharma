# Prompt 01 — Evidence Acquisition Backlog

Required: sufficiency scores include **Partial** / **Missing** inputs (`hypothesis` mode).

| Priority | Blocks | Artifact needed | Likely owner / source in package or org | Why it blocks | Later prompt |
|---|---|---|---|---|---|
| P0 | Framing → decision-ready | Measured release-pack cycle time (median, p90) | Manufacturing / Quality ops — **not in package** | Only BR-01 target exists; ROI claims would invent facts | 02 Frame, 09 Measure |
| P0 | Framing / design | Confirmation of knowledge SoT usage rules at as-of (approved vs superseded/untrusted/draft) | Document control; start from `data/knowledge_catalog.csv` | Untrusted/malicious/superseded docs present in same corpus | 02, 04, retrieval design later |
| P0 | Design | Entitlement SoT policy: IAM vs gateway cache | IAM / CISO; `users_entitlements.csv`, `access_cache.csv` | contractor_77 revoked but cached active | 05–08, security tests |
| P1 | Design | Authoritative unit / interface mapping approval | QC / integration; `interface_mappings.csv`, LIMS contracts v1/v2 | LR-88 unit≠spec; mapping approved=no | Batch workflow specs |
| P1 | Design | Which validation inventory wins for AI-EVIDENCE | Quality / Architecture; `system_inventory.csv`, `validation_inventory.csv` | Three conflicting states | GxP intended use |
| P1 | Design / FinOps | Actual human review hours for packs | Quality / PV / Supply; rates in `staff_rates.csv` | cost_model review lines = 0 | 03 metrics, 09, FinOps |
| P1 | Design | as-of / clock field dictionary per critical dataset | Data stewardship; extend `DATA_DICTIONARY.csv` semantics | Event vs report time ambiguous | Contracts / as-of queries |
| P2 | Production claims | Full LF-normalized package hash verification | Facilitator or LF checkout | CRLF verify FAIL residual | Assurance |
| P2 | Production / eval | Language subgroup baselines for PV extraction | PV / evaluation; INJ-072 | Performance inequity hypothesized | 09, 12 |
| P2 | Production | Accessibility findings remediation baseline | HF; `usability_findings.csv` | INJ-073 | 03 adoption |

**Rule:** Until P0 items are acquired or explicitly assumed (labeled), framing mode remains `hypothesis`. Do not invent values for Missing baselines.
