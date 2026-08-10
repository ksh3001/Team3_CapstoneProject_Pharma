# Prompt 04 — DMAIC Lens (thin)

**DMAIC focus:** Analyze (domain defect/rework sources) + design to avoid waste.  
**Skills:** `process-and-lean-discovery` thin-lens contract.  
**Artifact status:** provisional domain model.

1. **Invariants/rules that remove Defects vs leaving them to the model**
   - POL-NO-DISPOSITION / POL-NO-FINAL-PV / POL-NO-SIDE-EFFECTS / POL-NO-SILENT-UNIT / POL-NO-IRREVERSIBLE-MERGE / POL-AUTHZ-IAM / POL-DOC-TRUST — deterministic; AI must not override.
   - Leaving conflict “resolution” or readiness-as-release to the model recreates starter defects.

2. **HITL vs human-review waste**
   - Mandatory HITL on Conflicts, Abstentions, quarantine/authz denies, high-severity gaps.
   - Avoid reviewing every trivial cited pass equally — risk-route (pilot-tuned) to prevent Waiting/over-review waste while catching high-risk cases.

3. **RAG/agent unbounded waste risks**
   - Equal-trust retrieval of all knowledge → token waste + injection defects.
   - Multi-agent option swarms with write tools → overproduction (duplicate reservations).
   - Bound RAG to Applicable Documents + cited Evidence Items; agents stop on invariant/authz/budget.

4. **Domain ambiguities → Extra processing / Motion if unresolved**
   - `review readiness` vs disposition language; OOS vs lab status; validation triple-state; event vs report time; `available_units` including quarantine — force dual systems work and re- litigate in every pack until glossaries/SoTs close (P0/P1 backlog).
