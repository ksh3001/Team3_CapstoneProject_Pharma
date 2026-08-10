# Submission Artefacts Layout

Two parallel tracks are stored separately:

| Folder | Track | Contents |
|---|---|---|
| [`phases/`](phases/) | Capstone execution plan (Phases 0–8) | Template-style artefacts `00`–`30` as completed |
| [`prompts/`](prompts/) | Prompt library spine (01–13) | Outputs from `prompts/01_discovery.md` … `13_solution_proposal.md` |

Shared decision log: [`phases/00_preflight/00_ASSUMPTIONS_DECISION_LOG.md`](phases/00_preflight/00_ASSUMPTIONS_DECISION_LOG.md).

Spec mirrors (`submission/specs/`, `submission/tasks/`) remain outside this folder and still point at the prompt trail where applicable.
