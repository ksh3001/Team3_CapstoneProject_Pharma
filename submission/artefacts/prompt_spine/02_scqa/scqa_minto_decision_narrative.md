# Prompt 02 — SCQA & Minto Decision Narrative

| Field | Entry |
|---|---|
| Team | Team3 |
| As-of | 2026-08-06 |
| Prompt | `prompts/02_scqa_minto.md` + `prompts/PROMPT_LIBRARY.md` §1 |
| Prerequisite | `submission/artefacts/prompt_spine/01_discovery/evidence_register.md` |

## 0. Narrative class

| Field | Value |
|---|---|
| **Narrative class** | `hypothesis` (matches Prompt 01; not upgraded) |
| **Evidence boundary** | Synthetic challenge package only; cite paths; no live NTG metrics |
| **Top blocking acquisition items** | Measured release-pack cycle time; knowledge authority catalog; entitlement SoT vs cache; human review hours (see Prompt 01 backlog) |
| **Audience** | NTG Quality / PV / Supply sponsors + Team3 defence panel |
| **Decision horizon** | Capstone POC window; board target due 2026-11-30 is context not POC SLA |
| **Authority boundary** | AI none on batch certification & ICSR reportability; draft only on allocation (`decision_rights.csv`) |

---

## A. SCQA narrative

### Situation

NovaCura Therapeutics Group (NTG) runs discovery, clinical, manufacturing, quality, PV and supply across multiple regions with a fragmented brownfield estate (LIMS, MES, EBR, QMS, RIM, safety, serialization, spreadsheets, vendor portals). Portfolio pressure includes NCX-101 exclusivity countdown and high-risk biologics/sterile products (`portfolio_products.csv`; `case/INTEGRATED_CASE.md`). The board requested a **−14% release lead time** improvement by 2026-11-30 **without** changing registered specifications or weakening independent Quality authority (`board_requests.csv` BR-01).

### Complication

Evidence needed for batch readiness, PV intake, and shortage response is slow and conflict-prone: functional KPIs pull Manufacturing, Quality, Safety and Clinical in different directions (`kpi_conflicts.csv`); starter tooling shows lexical “ready,” equal-trust knowledge retrieval, and supply reservation side effects (`starter/legacy_pharma.py`); process-excellence estimates claim material value from master-data repair and rules **without** generative AI, while genAI assist claims higher value but longer duration and sits atop an incomplete cost model that zeroes human review (`no_ai_baselines.csv`, `cost_model.csv`). Hard boundaries forbid autonomous release, final PV decisions, and stock execution (`ai_use_boundaries.csv`). **Measured current lead-time baseline is Unknown** → any genAI-first ROI claim would invent facts.

### Question

**For the three mandatory workflows, what capability should Team3 qualify and test first—such that cycle-time and rework can improve without transferring regulated accountability to AI—and what evidence must be acquired before locking a build-vs-no-AI decision?**

### Answer (`hypothesis` mode — governing experiment)

Run a **Measure-first hybrid experiment**: (1) quantify conflict and rework proxies while executing master-data and rules/checklist repairs; (2) pilot a **narrow deterministic evidence-assist** that only reconciles/cites/flags/abstains (batch), extracts/clusters/cites (PV), and drafts non-executing options (supply); (3) keep any generative model **optional, off by default**, and falsifiable. **Do not** lock genAI as the sole intervention.

**Falsifiers:** prohibited action becomes executable; provenance/authority/time/units not preserved; AI-disabled path missing; MDM+rules alone meet agreed cycle-time proxies without assist; human+inference TCO worse than no-AI path after honest review costing.

**Desired outcomes (“good”):** cited conflict packs; 100% block of prohibited outputs in negatives; manual continuity drills pass; no Quality-authority weakening.

**Exclusions:** architecture/vendor/model lock-in; autonomous disposition/PV-final/allocate; changing specifications.

---

## B. Minto pyramid

**Governing answer:** Qualify a fail-closed, Measure-first evidence-assist experiment—not a genAI autonomous decision engine.

1. **Respect hard accountability boundaries**  
   - Fact: AI authority none / draft only (`decision_rights.csv`).  
   - Fact: Allowed/prohibited strings in `ai_use_boundaries.csv`.

2. **Attack root evidence waste before generative scale**  
   - Fact: MDM 38%/10w and rules 27%/6w in `no_ai_baselines.csv`.  
   - Derivation: starter defects are rules/data problems, not model-absence problems.

3. **Keep the assist narrower than the board problem**  
   - Fact: BR-01 forbids Quality-authority change.  
   - Assumption (labeled): board −14% is an enterprise outcome metric, not a license to auto-certify.

4. **Measure what is Unknown before claiming decision-ready value**  
   - Fact: package lacks lead-time distribution.  
   - Backlog: instrument proxies and human review hours.

5. **Prove continuity and deny paths as first-class**  
   - Fact: continuity_requirements require manual runbooks; PV max_ai_outage_hours=0.  
   - Fact: diagnostics already flag stale auth, untrusted knowledge, unit mapping.

6. **Price full operating cost**  
   - Fact: inference 184000 USD/mo; human review lines at 0.  
   - Derivation: ROI using zeros is invalid (INJ-077 theme).

7. **Preserve local human A under global process pressure**  
   - Fact: INJ-074 / stakeholder pack — QP and Safety retain legal accountability.

---

## C. Framing handoff pack

| Item | Content |
|---|---|
| Decision question for PRD/DDD | What fail-closed evidence-assist capabilities are in scope for batch readiness support, PV intake support, and supply option drafts—and what is explicitly out of scope? |
| Success metrics (baseline known/unknown) | Prohibited-action block rate (known target 100%); conflict dual-cite rate (Unknown baseline); evidence-pack cycle-time proxy (Unknown); AI-disabled drill pass (binary); review hours × rates (Unknown, rates known) |
| Open questions blocking design | Knowledge SoT catalog; unit mapping authority; entitlement SoT; measured cycle time |
| Later artifacts provisional? | **Yes** — PRD/vision and artefacts 01–04 marked provisional under `hypothesis` until Measure upgrades framing mode |

---

## Prompt library §1 checklist (Qualify)

| Required element | Where addressed |
|---|---|
| Measurable workflow problem | Complication + metrics (proxies; baselines Unknown labeled) |
| Affected decisions | Certification, reportability, allocation — human A |
| Baseline | Partial: starter + CSVs; lead-time Unknown |
| No-AI alternative | MDM + rules sequenced before genAI |
| Constraints | BR-01, AI boundaries, continuity, offline |
| Uncertainty | Narrative class hypothesis; acquisition backlog |
| Stop criteria | Falsifiers above; hard gates |
| Cite every factual claim | Evidence paths in Situation/Complication/pyramid |
