# Boundaries and Degraded Mode

| Field | Entry |
|---|---|
| Artifact status | **provisional** |
| Cites | `c4_context.md`, `c4_containers.md`, `04_ddd/gen_ai_boundaries.md` |

## Trust / authority boundaries

| Boundary | Rule |
|---|---|
| IAM vs cache | IAM authoritative; cache never grants after revoke (FR-001) |
| Document trust | Only approved/applicable docs are instruction-capable (FR-002) |
| Decision authority | Certification / final PV / allocation **outside** AEGIS system boundary |
| Schema wall | additionalProperties false; prohibited fields rejected |

## Data / privacy boundaries

| Boundary | Rule |
|---|---|
| Purpose limitation | AuthZ purpose must match workflow |
| Minimisation | Assessed mode uses package extracts; no bulk unrelated case exfiltration |
| Cross-border | Jurisdiction on Applicable Documents; local_approved not globally instructional by default (AMB-DOC-01) |

## Connectivity boundaries

| Path | Assessed mode |
|---|---|
| Read challenge `data/` / `knowledge/` | Allowed via ACL |
| Optional LLM network | Disabled by default; may be mocked |
| Write to MES/WMS/Safety execution APIs | **PROHIBITED** |
| Mutate package challenge evidence | **PROHIBITED** |

## Prohibited operational write paths

Explicit list (must appear on maps):

1. Batch disposition / release / reject / reprocess / relabel / recall writes  
2. Final PV conclusion writes presented as system decisions  
3. Inventory reservation / allocation / shipment / quality-status change / recall initiation  
4. Elevating untrusted/draft/superseded documents to policy  
5. Overwriting Evidence Items to clear Conflicts for a green gate  

## Degraded / offline mode (FR-006)

| Failure | Behaviour |
|---|---|
| No network / no LLM | Deterministic Runtime + Rules + local Store continue |
| AI-disabled flag / kill switch | Narrator Port refused; workflows rules-only |
| Upstream extract missing | Gap + Abstention; fail closed on material claims |
| AuthZ deny | Stop; no pack |
| Gate fail | Block ready; do not mutate packs |
| PV with model down | Continue without inference (max_ai_outage_hours=0) |
| Batch/supply prolonged AI outage | Manual runbook up to 14 days; assist remains non-executing |

## Observability ownership

| Signal | Owner |
|---|---|
| AuthZ allow/deny | CISO / Runtime |
| Gate pass/fail | Evaluation lead |
| SideEffectGuard trips | Supply context + Security |
| Model token use (if enabled) | FinOps / Runtime |
