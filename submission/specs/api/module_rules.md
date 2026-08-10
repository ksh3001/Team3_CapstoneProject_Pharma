# Module / Layering Rules (Agent Constraints)

Aligned to C4 (`06_c4/c4_code.md`, containers). Enforce in review and tests.

## Layout (target under `submission/`)

```text
submission/
  src/
    authz/           # AuthorizationPort only
    evidence/        # EvidenceItem, ACL adapters (read-only)
    workflows/
      batch.py
      pv.py
      supply.py
    contracts/       # schema validators (wrap evaluation/contracts)
    runtime/
      mode.py
      idempotency.py
    ports/
      llm.py         # no-op default
    evaluate/        # gate runner
  app/               # thin UI — calls Runtime only
  tests/
  scripts/
```

## Enforceable rules

1. **Routers/CLI hold no business invariants** — only parse args, call services, print JSON.  
2. **Workflows hold no SQL/raw CSV paths mixed with policy** — CSV access only via `evidence/` ACL adapters.  
3. **UI does not bypass Runtime** — no direct CSV reads for readiness.  
4. **`ports/llm.py` default is no-op**; assessed tests patch/assert zero calls.  
5. **No module under `workflows/` or `evidence/` may import write SDKs** for MES/WMS/Safety.  
6. **`supply.py` must call SideEffectGuard** before return; guard fails closed.  
7. **Validators run before return** on all workflow responses.  
8. **AuthZ before ACL fetch** on every workflow.  
9. **Challenge paths `data/`, `knowledge/` are read-only** — any write attempt is test failure.  
10. **Measure/evaluate must not mutate packs** to flip gates (BR-061).

## Agent coding constraints

- Load only listed specs per task (Prompt 10).  
- Do not invent endpoints not in `api_contracts.md`.  
- Do not expand PRD out-of-scope.
