# Prompt 06 — DMAIC Lens (thin)

**DMAIC focus:** Improve by architecture; avoid new wastes.

1. **Transportation / Integration waste**
   - Single Workflow Runtime + ACL read path reduces hop soup vs per-feature microservices (provisional).
   - Clear SoT: IAM for auth; approved docs for policy; SoR extracts for facts — fewer ambiguous “which system wins” hops at runtime (conflicts still cited, not silently merged).

2. **Waiting risks**
   - Sync human-review queues on Conflicts/Abstentions/duplicates — necessary for safety; Mode Controller must not block deterministic path on LLM latency.
   - AuthZ deny fails fast (good) vs waiting on cache refresh — IAM-first removes stale-wait loops.

3. **Observability / Context waste**
   - Audit owned in Evidence Store with named owners (boundary doc) — avoid logs nobody owns.
   - Shared kernel keeps citation/as_of in pack — avoid reconstructing meaning in every UI ad hoc.

4. **Overproduction vs minimum governed workflow**
   - No agent swarm, no write-execution container, no always-on model — matches provisional DDD minimum flow.
   - Adding WMS write adapters or multi-agent planners now would be Overproduction relative to PRD out-of-scope.
