# Other Moonshot Ideas (excluding PIPG)

| Field | Entry |
|---|---|
| Branch | `Moon-shot-research` |
| Companion doc | `submission/artefacts/moonshot/PIPG_MOONSHOT.md` (Prompt-Injection Protection Gateway — detailed separately) |
| Basis | Challenge package only (`case/`, `data/`, `knowledge/`, `evaluation/`, `templates/`, DoD/scoring) |
| Note | `submission/` implementation for these ideas is not started; this file is a concept catalogue with repo fit |

---

## How to read this catalogue

Each idea includes:

- **What it is** — short product definition  
- **Repo fit** — native hooks on this branch  
- **Fit tier** — A (strong), B (clear hooks), C (possible / thinner)  
- **Implementation sketch** — what would land under `submission/` if chosen  

**Tier A** ideas sit most naturally on challenge contracts, injects, and hard gates.  
**PIPG** is omitted here; see the companion doc.

---

## Tier A — Strongest fit on this branch

### 1. AI-SBOM and agent inventory

**What it is:** A living bill of materials for every model, agent run, tool, prompt template, dataset, and dependency used in Batch / PV / Supply paths.

**Repo fit:** `data/model_registry.csv`, `data/tool_catalog.csv`, `data/agent_runs.csv`, INJ-011 (unqualified model), INJ-070 (model hash mismatch), INJ-080 (checkpoint / agent resume).

**Implementation sketch:** Inventory service that hashes and versions artefacts; blocks runtime use of unregistered or hash-mismatched models/tools; exports SBOM for inspection (INJ-050 / INJ-084).

---

### 2. Responsible AI control tower

**What it is:** Single ops console for AI risk, AuthZ status, security events, approvals, kill-switch, and release-gate health across the three workflows.

**Repo fit:** Required operating properties in `case/INTEGRATED_CASE.md`; eval release gates; incident / continuity / retirement injects; empty `submission/runbooks/` expectation.

**Implementation sketch:** Read-only dashboard over audit logs, gateway decisions, evaluate results, and mode (`deterministic_offline` / `ai_disabled`); no autonomous regulated actions.

---

### 3. Consent-and-purpose-as-code engine

**What it is:** Machine-checkable rules for “who may use which data for which purpose,” enforced before any workflow or model call.

**Repo fit:** Contract `authorization.purpose`; INJ-060/061/063; `data/consents.csv`; `knowledge/ECONSENT_AND_SECONDARY_USE.md`; DoD purpose-limitation obligations.

**Implementation sketch:** Purpose ontology + consent/license adapters; deny secondary use / commercial targeting when not covered; emit abstentions and human_review.

---

### 4. Human-authority decision matrix

**What it is:** Explicit map of AI-propose vs human-decide actions by role (QP, safety, clinical, supply), enforced at runtime.

**Repo fit:** `human_review`, `execution_status: not_executed`; INJ-006, INJ-074; `data/decision_rights.csv`; `templates/03_STAKEHOLDER_DECISION_RIGHTS.md`; `AI_GXP_BOUNDARY.md`.

**Implementation sketch:** Matrix config (object × action × role); workflows may only draft; prohibited conclusions rejected by contract validation.

---

### 5. Evidence provenance ledger

**What it is:** Immutable trail of source, authority, effective/retrieved time, integrity hash, and transformations for every fact used.

**Repo fit:** `evaluation/contracts/evidence_item.schema.json` (source, authority, effective_at, retrieved_at, sha256, `source_preserved: true`); INJ-036 ALCOA+ break; scoring hard gate on provenance.

**Implementation sketch:** Ledger store appending evidence items and lineage edges; refuse silent unit conversion / uncited material facts; export for inspection.

---

### 6. Evidence contradiction detector

**What it is:** Systematic detection and surfacing of conflicting claims across sources instead of silent merge.

**Repo fit:** Required `contradictions[]` on workflow contracts; case built on conflicting IDs, clocks, authorities, listedness; DoD conflict preservation.

**Implementation sketch:** Deterministic comparators (unit, time, identity, authority); populate `contradictions` / `gaps`; never present conflict as resolved.

---

### 7. Uncertainty and confidence engine

**What it is:** Quantifies and propagates uncertainty; forces abstention when identity, unit, time, authority, or evidence is incomplete.

**Repo fit:** Required `abstentions` / `gaps`; DoD uncertainty + abstention; many injects with unknown/missing referenced sources.

**Implementation sketch:** Confidence / completeness scores per claim; thresholds → abstain + `human_review`; no fabricated certainty.

---

### 8. AI-disabled continuity simulator

**What it is:** Exercisable simulation that the three workflows remain safe for a defined outage (e.g. 14 days) with inference off, then reconcile on restore.

**Repo fit:** INJ-082; `data/continuity_requirements.csv`; `knowledge/AI_DISABLED_CONTINUITY.md`; DoD manual mode; `submission/runbooks/` AI-disabled continuity.

**Implementation sketch:** Mode switch + drill scripts; golden outage fixtures; prove no degradation into higher-authority automation; reconciliation checklist.

---

### 9. Responsible AI release gate

**What it is:** Hard CI/evaluate gate that blocks ship when security, provenance, subgroup, or GxP boundary tests fail.

**Repo fit:** `evaluation/EVALUATION_PLAN.md` release gates; public fixtures; `requirements/SCORING_MODEL.md` hard gates; DoD “failed gates block release.”

**Implementation sketch:** Evaluate runner over contract + adversarial suites; machine-readable scorecard; fail-closed on untrusted instructions, prohibited actions, missing manual mode.

---

### 10. Continuous assurance-case generator

**What it is:** Living claims–arguments–evidence tree kept current from tests, audits, and residual risks (demo vs production claims).

**Repo fit:** `templates/21_ASSURANCE_CASE.md`; CSA / GxP lifecycle templates; INJ-050 inspection surge; defence expectation to link claims to evidence.

**Implementation sketch:** Generate/update assurance markdown/JSON from test results and control inventories; separate C0 (demo) vs C0′ (production) claims.

---

### 11. AI accountability ledger

**What it is:** End-to-end record of who approved what, on which evidence, under which purpose and authority.

**Repo fit:** Required `audit` on contracts; INJ-084 retirement/evidence preservation; `data/retention_rules.csv`.

**Implementation sketch:** Append-only audit events (AuthZ, PIPG/security, workflow, reviewer); retention-aware export; inspectable after retirement.

---

### 12. Zero-trust AI tool marketplace

**What it is:** Registry where every tool is authenticated, least-privilege, continuously authorized, and human-approved for side effects.

**Repo fit:** `knowledge/ZERO_TRUST_AI_TOOLS.md`; INJ-066/067/070; `tool_catalog.csv`; approved vs poisoned manifests in `starter/api_samples/` and `data/`.

**Implementation sketch:** Signed manifest store; execution-time AuthZ for user×purpose×tool; deny over-privileged tools; pairs naturally with PIPG tool verifier.

---

### 13. Responsible AI red-team factory

**What it is:** Continuous generation and execution of adversarial cases (injection, poison, stale AuthZ, exfil, DoW, excessive agency).

**Repo fit:** DoD adversarial suite; D10–D12 injects; `templates/16_THREAT_ABUSE_MODEL.md`; eval suites #5, #8, #11.

**Implementation sketch:** Fixture factory from inject catalogue; scheduled negative tests; residual-risk register updates; feeds release gate.

---

## Tier B — Clear hooks, thinner native product shape

### 14. Policy-as-code compiler

**What it is:** Compiles written policies into enforceable runtime rules.

**Repo fit:** 32 `knowledge/` docs with status/authority/effective date; retrieval conflict handling on every policy extract.

**Implementation sketch:** Parse document-control blocks + mandatory controls into rule packs; applicability engine before instruction use.

---

### 15. Ethics-as-code engine

**What it is:** Executable ethical constraints (harm, fairness of allocation, secondary use) that can block or flag actions.

**Repo fit:** `SUPPLY_ALLOCATION_ETHICS.md`; privacy/ethics template; INJ-056, INJ-059–063.

**Implementation sketch:** Constraint library for supply options and data-use paths; violations → abstain / approvals_required.

---

### 16. Fairness-as-code framework

**What it is:** Codified fairness metrics and thresholds evaluated continuously.

**Repo fit:** INJ-009 omics cohort bias; INJ-072 language inequity; `model_performance.csv`; DoD subgroup suites.

**Implementation sketch:** Metric definitions + graders; block release when subgroup evidence missing or thresholds fail.

---

### 17. Explainable AI evidence studio

**What it is:** Workspace to assemble citations, reason codes, and review packs for auditors and accountable humans.

**Repo fit:** Citation/provenance obligations; INJ-071 automation bias; RAI template `18_RESPONSIBLE_AI_HUMAN_FACTORS.md`.

**Implementation sketch:** UI/CLI over evidence items + contradictions; dual-cite views; never hide omitted deviations.

---

### 18. Algorithmic impact assessment autopilot

**What it is:** Semi-automated AIA / risk assessment when models, purposes, or data flows change.

**Repo fit:** `templates/19_EU_AI_ACT_APPLICABILITY.md`, QRM/CSA templates; intended-use strategic decisions.

**Implementation sketch:** Questionnaire + evidence binder generator from registry diffs; human sign-off required.

---

### 19. Authority-aware knowledge graph

**What it is:** Graph of entities/relations weighted by source authority, jurisdiction, and effective time.

**Repo fit:** Strategic decision “whether KG is necessary”; `templates/08_KNOWLEDGE_GRAPH_DECISION.md`; KG **not mandatory** (`PACKAGE_SCOPE_AND_ASSUMPTIONS.md`).

**Implementation sketch:** Only if decision artefact says yes; provenance on edges; offline-friendly subset (genealogy, signal links); revisit criteria explicit.

---

### 20. Model-change impact simulator

**What it is:** Before model/prompt/tool change ships, simulate impact on fidelity, fairness, security, and workflow outputs.

**Repo fit:** `AI_MODEL_CHANGE_CONTROL.md`; INJ-081 model substitution; change-control strategic decision.

**Implementation sketch:** Replay public + adversarial fixtures on candidate version; diff scorecard; gate promotion.

---

### 21. Regulatory impact radar

**What it is:** Tracks applicable regulatory themes and maps them to controls and gaps.

**Repo fit:** `case/REGULATORY_BOUNDARY_PACK.md`; EU AI Act / ISO42001 templates; local standards guide (anchors, not legal advice).

**Implementation sketch:** Control↔obligation matrix; gap list with owners; no universal compliance claim.

---

### 22. Natural-language audit assistant

**What it is:** Plain-language Q&A over logs, policies, and evidence for inspection-style requests.

**Repo fit:** INJ-050 inspection surge; audit/evidence obligations; LLM optional behind replaceable interface.

**Implementation sketch:** Retrieval over audit ledger + evidence with citation-only answers; refuse uncited claims; works in degraded/manual mode with deterministic search.

---

### 23. Continuous ethical-drift monitor

**What it is:** Detects slow drift from original ethical/policy intent after deployment.

**Repo fit:** Model performance and human-factors injects; evaluation regression history expectation.

**Implementation sketch:** Baseline snapshots of abstention rates, subgroup metrics, quarantine rates; alert on drift.

---

### 24. Responsible AI model-card generator

**What it is:** Auto-generated living model cards from registry, tests, limits, and known failures.

**Repo fit:** `model_registry.csv`; INJ-011 unqualified research model; FinOps/performance CSVs.

**Implementation sketch:** Card generator from SBOM + evaluate results; blocks use when intended-use or locked training set missing.

---

### 25. Cross-domain incident intelligence platform

**What it is:** Correlates AI/security/quality incidents across Batch, PV, Supply, and vendors.

**Repo fit:** `AI_INCIDENT_RESPONSE.md`; INJ-068/069/079; multi-domain inject chains.

**Implementation sketch:** Incident schema + correlator over security_events / downtime / workflow audits; playbooks under `submission/runbooks/`.

---

## Tier C — Possible, weaker scaffolding

### 26. Fairness and bias observatory

**What it is:** Continuous monitoring dashboard for bias signals across cohorts, language, and time.

**Repo fit:** Same as fairness-as-code (INJ-009, INJ-072); productized observability layer.

**Implementation sketch:** Time-series of subgroup graders; links to release gate and control tower.

---

### 27. Intersectional bias digital twin

**What it is:** Synthetic twin of populations to stress-test intersectional bias before promotion.

**Repo fit:** Cohort bias inject; no twin design in package.

**Implementation sketch:** Synthetic cohort generator + evaluation harness; hypothesis-labeled until validated.

---

### 28. Vulnerable-person protection engine

**What it is:** Extra safeguards when subjects may be vulnerable (privacy leakage, over-collection, coercive use).

**Repo fit:** INJ-059 genomic re-ID; INJ-062 patient-support leakage; privacy template.

**Implementation sketch:** Detectors for sensitive free text / re-ID risk; purpose deny + human review.

---

### 29. Counterfactual explanation engine

**What it is:** Structured “what would need to change for a different outcome?” explanations.

**Repo fit:** No explicit counterfactual requirement in contracts; could sit on readiness/duplicate/option outputs.

**Implementation sketch:** Rule-based counterfactuals over gated evidence features; human-review oriented.

---

### 30. Right-to-explanation portal

**What it is:** Portal for affected parties to request understandable explanations of AI-assisted outcomes.

**Repo fit:** Human-review / accountability themes; accessibility inject INJ-073; no portal artefact.

**Implementation sketch:** Request workflow + cited explanation packs; jurisdiction/purpose constrained.

---

### 31. AI contestability and appeals engine

**What it is:** Formal challenge/appeal path for AI-assisted recommendations.

**Repo fit:** Accountability and decision-rights themes; no appeals workflow in package.

**Implementation sketch:** Appeal case object, evidence freeze, escalation roles, audit outcome.

---

### 32. Explanation fidelity verifier

**What it is:** Checks that explanations match actual system behavior (not plausible fiction).

**Repo fit:** Automation bias INJ-071; evidence fidelity eval suite.

**Implementation sketch:** Consistency tests between explanation claims and evidence/contradiction sets.

---

### 33. Ethical AI impact simulator

**What it is:** Pre-go-live simulation of ethical/social/allocation consequences of a change.

**Repo fit:** INJ-056 allocation ethics; INJ-006 prohibited optimization.

**Implementation sketch:** Scenario runner over demand/inventory/constraints; surfaces violated ethics constraints.

---

### 34. Ethical objective-function firewall

**What it is:** Blocks optimization goals that maximize the wrong objective (throughput over quality, etc.).

**Repo fit:** INJ-006; `ai_use_boundaries.csv`; KPI conflict INJ-002; `AI_GXP_BOUNDARY.md`.

**Implementation sketch:** Allowlisted objective functions per workflow; deny prohibited optimization targets.

---

### 35. Synthetic crisis simulator

**What it is:** Generates crisis scenarios (outage, ransomware, injection surge, vendor exit) for rehearsal.

**Repo fit:** Continuity/incident/vendor-exit injects; Phase “break and recover” runbook guidance.

**Implementation sketch:** Scenario packs + drill runner; scores recovery against continuity requirements.

---

### 36. AI failure digital twin

**What it is:** Sandbox twin to replay and explore AI failure modes safely.

**Repo fit:** Threat model + failure/recovery eval suites; no twin product specified.

**Implementation sketch:** Isolated replay of fixtures and agent_runs with PIPG/AuthZ on; no SoR writes.

---

### 37. Dark-pattern and manipulation detector

**What it is:** Detects manipulative UX that nudges unsafe acceptance of AI outputs.

**Repo fit:** Weakest native fit; INJ-071 automation bias, INJ-073 accessibility only.

**Implementation sketch:** UX heuristic checks on demonstrator; warn on colour-only warnings / forced accept.

---

### 38. Multi-agent ethics review board

**What it is:** Multiple agents debate ethics/risk of a proposed action, then escalate to humans.

**Repo fit:** Agents not mandatory; `AGENT_BUDGET_AND_STOP_POLICY.md` is cautionary; risk of excessive agency.

**Implementation sketch:** Only as bounded, budgeted advisory panel with human final authority; default remain single gated path.

---

## Suggested shortlist if picking a second moonshot after PIPG

| Priority | Idea | Why after PIPG |
|---|---|---|
| 1 | Evidence provenance ledger | Complements quarantine with durable evidence integrity |
| 2 | Human-authority decision matrix | Locks “who may decide” once instructions are gated |
| 3 | Zero-trust AI tool marketplace | Extends PIPG tool verifier into a product registry |
| 4 | AI-disabled continuity simulator | Proves controls survive without models |
| 5 | Responsible AI release gate | Industrializes PIPG + workflow tests as ship/no-ship |
| 6 | Continuous assurance-case generator | Turns controls into living defence evidence |
| 7 | Consent-and-purpose-as-code | Next privacy/GxP differentiator beside injection |

---

## Explicit non-goals (all ideas)

- No autonomous batch disposition, final PV decisions, inventory reservation/allocation/shipment, quality-status change, or recall initiation.
- Do not fabricate, overwrite, or silently normalize regulated evidence.
- Do not treat challenge `case/`, `data/`, `knowledge/`, `evaluation/` as mutable product code — build under `submission/` only.
- Abstain when identity, unit, time, terminology, jurisdiction, source authority, or evidence completeness cannot be resolved.

---

## Document control

| Field | Entry |
|---|---|
| Title | Other moonshot ideas catalogue (excluding PIPG) |
| Location | `submission/artefacts/moonshot/OTHER_MOONSHOT_IDEAS.md` |
| PIPG detail | `submission/artefacts/moonshot/PIPG_MOONSHOT.md` |
| Next step | Select one Tier A/B idea to deepen into a full implementation pitch, or proceed with PIPG Phase A |
