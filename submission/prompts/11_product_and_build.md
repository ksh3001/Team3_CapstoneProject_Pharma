> **V3 adaptation:** Team method prompt. Do not edit hashed prompts/PROMPT_LIBRARY.md. Write all outputs under submission/ only. Obey package control prompts, GxP fail-closed contracts, and prohibited-action boundaries. See submission/prompts/PROMPT_MAPPING.md.
# Prompt 11 — Deliver (Execute Tasks / AI Coding + Tests)

**Lifecycle stage:** Deliver / Spec-Driven Development — AI Coding **and** Tests (intentionally merged)  
**Framework applied:** Executes Prompt 10 tasks against PRD, features, C4, ADRs, technical contracts, and Lean constraints  
**Core question:** How do we ship the governed slice by executing one task at a time — with AC-linked tests?  
**Prerequisites:** Prompt 10 sequencing in artefacts `09`/`28`; Prompts 03–09 artefacts; Prompt 09 structural reopen `cleared`.  
**Primary output type:** Working implementation + test evidence + updated traceability.

---

## Intent

**Implement** the minimum governed workflow by executing **Prompt 10 tasks in order** — one task (or small batch) per agent run. Load only the specs each task lists. Do not invent contracts, ACs, or architecture during coding.

**SDD note:** Spec-Driven Development lists **Tests** as its own stage. This library **intentionally merges** Coding + Tests into Prompt 11 (AC verification continues in Prompt 12), same style as Architecture-before-Technical. Do not skip the AC test plan.

**DDD stage 15 (pilot, learn & refine):** treat this build as the pilot slice — capture learnings that would change the domain model.

**Scarce-data rule:** if narrative class is `hypothesis` or artifacts are `provisional`, finish assumption-test / Measure tasks before feature enrichment.

---

## Entry criteria

- Implementation sequence and AC mapping exist in artefact `09`; blocked items are labeled.  
- Technical traceability matrix exists.  
- Prompt 09 structural reopen gate is `cleared`.  
- Lean build constraints and (if needed) assumption-test priorities are ranked.  
- Out-of-scope from PRD remains visible.

---

## Produce / do

1. **Execute work in order** from the sequence in artefacts `09`/`28` — for each unit, load only the listed artefact sections.  
2. **Assumption-test / Measure tasks first** when required by hypothesis/provisional/Lean.  
3. **Implement** per module rules (Prompt 08) inside the C4 shape.  
4. **Add/update tests** under `submission/tests/` that prove ACs/BRs/NFRs **before** moving on; update artefact `09` with pass/fail/deferred.  
5. **Prohibit operational write-back** unless ADR/technical design explicitly authorizes it.  
6. **Keep specialist authority visible** — HITL for domain-critical decisions remains obvious in UX and logs.  
7. **Update traceability** — FR → contract → AC → task → code/test paths.  
8. **PoC vs production label** — mark what is demonstrated vs still required.  
9. **Explanation & uncertainty behavior** — implement as specified in features/technical design (do not invent silently).  
10. **Pilot learnings (DDD stage 15)** — record pilot learnings in artefact `28_PRODUCTION_READINESS.md` / `09_REQUIREMENTS_TRACEABILITY.md`: what would change in domain model, features, or contracts after this pilot.
### Lean / DMAIC lens (spine — thin)

**DMAIC focus this stage:** **Improve** execution — remove waste while building; do not introduce new AI wastes.

In artefact `02_DMAIC_WORKBOOK.md` (short notes only), record:

1. Which Prompt 09 must-fix items were actually implemented?  
2. New wastes introduced during build (token bloat, extra agent loops, duplicate validation)?  
3. Measure instrumentation shipped (or still missing)?  
4. Deferrals that should return to DMAIC Analyze/Improve?

---

## Exit criteria (handoff to Prompt 12)

- [ ] All non-blocked tasks for the governed slice are done or explicitly deferred with risk.  
- [ ] Artefact `09` updated: in-scope ACs are pass, fail, or deferred with risk (none silently skipped).  
- [ ] AC-linked tests exist for completed features.  
- [ ] ADR guardrails and prohibited write paths are respected (or deviations logged).  
- [ ] Traceability matrix is updated with code/test links.  
- [ ] Pilot learnings recorded in artefact `28_PRODUCTION_READINESS.md` (DDD stage 15).  
- [ ] PoC vs production gaps are listed for Assurance and Proposal.  
- [ ] artefact `02_DMAIC_WORKBOOK.md` is complete.

---

## Constraints

- Do not invent API shapes, thresholds, or error codes — fix Prompt 08 (or 05) instead.  
- Do not hard-code conclusions for specific entities from source data.  
- Do not silently override ADRs, domain invariants, or PRD out-of-scope.  
- Do not scale features Lean marked as overproduction/token/model waste.  
- Do not expand beyond the minimum governed slice while critical assumptions remain untested (unless throwaway spike).

---

## Output

Do **not** create build log trees outside the scaffold. Implement only in package-expected dirs:

- `submission/src/`
- `submission/app/`
- `submission/tests/`
- Update traceability rows in `submission/artefacts/09_REQUIREMENTS_TRACEABILITY.md` as features land

See `submission/prompts/PROMPT_MAPPING.md`.
