# Prompt 10 — DMAIC Lens (thin)

**DMAIC focus:** Improve sequencing — Prompt 09 constraints → task order.

1. **Measure-first / must-fix-before-build → tasks**
   - Failing control tests first: task-005–011 (authz, docs, batch, PV, supply, continuity, gates).  
   - Foundation + schema: task-001–003.  
   - Measure stubs + emit: task-004, task-022; review-hour template task-023.  
   - No write-plane / disposition / allocate tasks created.

2. **Deferred as Overproduction / Model waste**
   - No narrator/LLM-on, RAG, agent swarm, WMS write, MDM product build tasks.  
   - task-025 fuzzy matching **blocked** (Model/Extra-processing waste if guessed).  
   - Full AC-052 org drill deferred (Phase 7) — scaffold only task-024.

3. **Assumption-test tasks vs Unknown baselines**
   - Control ACs do not invent cycle-time; they lock Defect/Overproduction gates.  
   - task-004/022 create the instrumentation path so Unknown cycle-time / conflict counts become measurable on fixture runs.  
   - task-023 enables honest TCO labeling without fabricating hours.

4. **Blocked / Waiting on evidence**
   - task-025 Waiting on AMB-PV-01 threshold + golden set (evidence acquisition).  
   - AC-052 full evidence Waiting on continuity drill execution (not structural reopen).
