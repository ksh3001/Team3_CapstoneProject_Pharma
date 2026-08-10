# Deployment Notes (lightweight POC)

| Item | Spec |
|---|---|
| Runtime | Python 3.10+; stdlib-first assessed path |
| Bind | `127.0.0.1` only for HTTP demo (error_and_security) |
| Health | GET /v1/health → 200, `llm_enabled=false` |
| Containers | Optional single image later; **not required** for assessed offline scripts |
| Reverse proxy | Out of scope for POC |
| Env flags | `AEGIS_MODE=deterministic_offline\|ai_disabled`; `AEGIS_LLM_ENABLED=false` default |
| Challenge data | Read-only mount/path to repo `data/`, `knowledge/` |
| Working store | Under `submission/` only; reset script clears |

Measurable: NFR-09, NFR-12, NFR-15.
