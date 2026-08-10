from pathlib import Path

root = Path("submission/artefacts/phases/01_qualify")
repls = [
    (
        "submission/artefacts/prompts/prompt_spine/01_discovery/",
        "submission/artefacts/prompts/01_discovery/",
    ),
    (
        "submission/artefacts/prompts/prompt_spine/02_scqa/",
        "submission/artefacts/prompts/02_scqa/",
    ),
    (
        "submission/artefacts/prompts/prompt_spine/03_prd/",
        "submission/artefacts/prompts/03_prd/",
    ),
    ("prompt_spine/01_discovery/", "prompts/01_discovery/"),
    ("prompt_spine/02_scqa/", "prompts/02_scqa/"),
    ("prompt_spine/03_prd/", "prompts/03_prd/"),
    ("prompt_spine dmaic_lens files", "canonical prompts/ dmaic_lens files"),
    ("Version / date | 0.2 / 2026-08-06", "Version / date | 0.3 / 2026-08-07"),
]

for p in sorted(root.glob("*.md")):
    text = p.read_text(encoding="utf-8")
    out = text
    for old, new in repls:
        out = out.replace(old, new)
    out = out.replace("prompt_spine/", "prompts/")
    if out != text:
        p.write_text(out, encoding="utf-8")
        print("updated", p.name)
    else:
        print("unchanged", p.name)
