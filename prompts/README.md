# AI FDE Prompts v2 — Framework + Spec-Driven Sequence

Prompt set aligned to `AI_FDE_Frameworks_Guide.md`, Spec-Driven Development (`References/Spec-Driven-Development-Techademy.pdf`), and the VisionScan-style SDD example.

Each prompt **derives one artifact class**, then hands off. Run in order unless a prompt allows a limited parallel pass.

## Sequence

```text
01 Discover (evidence inputs + early waste signals)
    → 02 Frame (SCQA + Minto)
    → 03 PRD / Vision (product intent + scope)
    → 04 Design domain (DDD for Gen AI)
    → 05 Feature Specifications (FRD — one feature per file)
    → 06 Design structure (C4)
    → 07 Decide (ADR) + Architecture review / defense
    → 08 Technical Design (SRS contracts + pre-build traceability)
    → 09 Improve lens (Lean / DMAIC)
    → 10 Implementation Tasks (numbered agent units)
    → 11 Deliver (execute tasks / AI coding + tests)
    → 12 Evaluate (Assurance + Control + AC review)
    → 13 Propose (Solution Proposal)
```

| # | Prompt | Framework / stage | Core question | Primary artifact |
|---|--------|-------------------|---------------|------------------|
| 01 | Discovery | AI FDE inputs | What exists and what is trustworthy? | Evidence register + sufficiency + early waste signals |
| 02 | SCQA & Minto | Frame | Why does this matter, and what is the ask? | Decision / hypothesis narrative |
| 03 | PRD / Vision | SDD — PRD | What problem, for whom, what success? | Vision + PRD + in/out scope |
| 04 | DDD | Design (domain) | What business meaning and rules? | Domain model & Gen AI boundaries |
| 05 | Feature Specs | SDD — FRD | What should the system do per feature? | FR files + BR/AC registers |
| 06 | C4 | SDD — Architecture | What does the system look like? | C4 views |
| 07 | ADR + Arch review | Decide / defense | Why does it look that way — and can we defend it? | ADRs + architecture review record |
| 08 | Technical Design | SDD — SRS | Exactly how should it behave? | APIs, data, NFRs, errors, traceability |
| 09 | Lean & DMAIC | Improve | Where is waste; how do we Measure/Control? | Waste registers + DMAIC plan |
| 10 | Implementation Tasks | SDD — Tasks | What code needs writing? | Numbered `task-00N` files |
| 11 | Deliver | SDD — AI Coding | How do we execute tasks safely? | Code + tests + execution log |
| 12 | Assurance | Evaluate / Review | Does it match design and ACs? | Evaluation report |
| 13 | Solution Proposal | Synthesis | What should sponsors decide next? | Executive & engineering proposal |

## Rules of engagement

1. **One job per prompt / one question per spec file** — do not merge PRD, feature flows, and API schemas into one document.
2. **Evidence before design** — Prompt 01 scores sufficiency and declares `decision-ready` vs `hypothesis`.
3. **Frame → PRD → Domain → Features** before boxes and contracts.
4. **Map before memory before contracts** — C4 (06) → ADR (07) → Technical Design (08).
5. **Architecture review before tasks** — Prompt 07 produces a pass/conditional review (C4+ADR “review / defense”) before Prompt 10.
6. **Structural reopen after Lean** — if Prompt 09 Improve needs C4/ADR/contract changes, `structural_reopen.md` must be `cleared` before Prompt 10.
7. **Tasks before coding** — Prompt 10 before Prompt 11; agents load only the specs each task lists.
8. **Write the value, not the adjective** — thresholds, timeouts, and limits must be numeric or marked Unknown.
9. **Waste before scale (Lean/DMAIC spine)** — every prompt 01–08 and 10–13 writes a thin `dmaic_lens.md`; Prompt **09 consolidates** into full DOWNTIME + AI-waste registers + DMAIC plan. Do **not** re-run full Prompt 09 after every step. Prompt **12** closes the spine with `control_lens_rollup.md` (lenses 10–12).
10. **Tests are intentional merge** — SDD “Tests” stage is merged into Prompt 11 (+ AC review in 12); every AC needs a row in `ac_test_plan.md`.
11. **PoC ≠ production** — Prompts 11–13 must label demo vs production-grade; DDD stages 15–16 map to pilot learnings (11) and production readiness (12–13).
12. **Specs in the repository** — write under `participant-outputs-v2/` **and** mirror into `specs/` or `tasks/` (required).
13. **Use this folder** — run **`prompts_v2/`** only. Legacy `prompts/` is historical comparison, not the current sequence.

### Lean / DMAIC spine (how it runs through all prompts)

Per `References/1784179827483-Lean_-_DMAIC.pdf`, Lean/DMAIC is the **operating improvement spine**, not a single late phase.

| Prompts | Thin lens focus | Full workshop |
|---------|-----------------|---------------|
| 01 | Measure + light Define | — |
| 02–03 | Define (+ Measure targets) | — |
| 04–05 | Analyze | — |
| 06–08 | Improve-by-design + Control triggers | — |
| **09** | — | **Full** registers + DMAIC plan (`lens_rollup` first) + structural reopen gate |
| 10–11 | Improve (prioritize / execute) | — |
| **12** | Control | **`control_lens_rollup`** closes lenses 10–12 |
| 13 | Control (executive) | — |

Each non-09 prompt: short `dmaic_lens.md` only. Prompt 09: synthesize 01–08 lenses, then deepen. Prompt 12: roll up post-build lenses.

### Chosen SDD order (Architecture before Technical Design)

This library follows the Spec-Driven Development **9-stage hierarchy** (Vision → PRD → Feature Spec → **Architecture** → **Technical Design** → Tasks → Coding → Tests → Review):

- **C4 / Architecture (06)** places code so agents do not put business rules in the wrong layer.
- **ADR + review (07)** records why and defends the map.
- **Technical Design (08)** then locks exact contracts.

**Tests stage:** intentionally merged into Prompt 11 (with Review/AC verification in Prompt 12) — same documentation style as Architecture-before-Technical.

Some SDD slides list “Technical Spec before Architecture.” We **intentionally do not** follow that alternate ordering: placement before contracts reduces silent wrong-layer implementations. Document any team override.

### Output conventions (required mirrors)

| Prompt outputs | Also mirror to |
|----------------|----------------|
| 03 PRD / Vision | `specs/product/` |
| 05 Feature Specs | `specs/features/` |
| 06–07 C4 / ADR / review | `specs/architecture/` |
| 08 Technical Design | `specs/api/`, `specs/data/`, `specs/testing/` as applicable |
| 10 Implementation Tasks | `tasks/` |

Primary copies remain under `participant-outputs-v2/` for the engagement trail.

## Scarce-data mode

| Mode | How to proceed |
|------|----------------|
| `decision-ready` | Normal 01→13 |
| `hypothesis` | 01→02→03 (provisional PRD) → acquisition loop → resume; 04–08 provisional/`proposed`; architecture review may be **conditional**; 09 Measure-first; 10–11 assumption tests first; 12 may rate `inconclusive (data scarcity)`; 13 leads with data-access decisions |

Do **not** present hypothesis outputs as committed production decisions.

## Companion reading

- `AI_FDE_Frameworks_Guide.md`
- `References/Spec-Driven-Development-Techademy.pdf`
- `References/visionscan-pos-spec.md` / `VisionScan-POS-SDD-Techademy.pdf` (worked SDD example)
- `References/` SCQA/Minto, DDD, C4 & ADR, Lean–DMAIC
- Root `README.md` — how to use prompts effectively

Original shorter prompts remain in `prompts/` for comparison.
