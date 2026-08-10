# ADR Candidates (for Prompt 07)

Architecture choices visible on the map; **not decided** here unless already forced by evidence.

| ID | Choice | Options (sketch) | Forced by evidence? |
|---|---|---|---|
| ADR-C01 | Default runtime = deterministic offline | vs cloud-first agent platform | Yes — package offline + FR-006 / continuity |
| ADR-C02 | LLM optional behind port, off by default | vs always-on RAG agent | Yes — hypothesis Measure-first; gen_ai_boundaries |
| ADR-C03 | No write adapters in assessed mode | vs “draft reservation” tool with human confirm | Yes — POL-NO-SIDE-EFFECTS; starter anti-pattern |
| ADR-C04 | IAM over cache for AuthZ | vs cache-first gateway | Yes — contractor_77 scenario |
| ADR-C05 | Single Workflow Runtime vs split microservices | monolith-ish POC vs many services | Open — prefer minimal provisional map |
| ADR-C06 | Local file/SQLite audit store vs external ledger | local vs remote | Open — local fits offline POC |
| ADR-C07 | Duplicate matching without fuzzy until threshold known | vs enable fuzzy at guessed 0.8 | Yes — AMB-PV-01 Unknown |
| ADR-C08 | ACL per SoR vs one mega-ingest | per-adapter vs lake | Open — ACL required; granularity ADR |
| ADR-C09 | Demo UI technology | static HTML vs small Python UI | Open — non-blocking |
| ADR-C10 | Gate runner in-process vs separate service | same container vs split | Open — same Runtime OK for POC |

Prompt 07 must record status, owners, evidence basis, and consequences for each accepted ADR.
