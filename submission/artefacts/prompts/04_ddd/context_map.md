# Context Map — AEGIS Evidence Assist

| Field | Entry |
|---|---|
| Prompt | `prompts/04_ddd.md` |
| Skills | `domain-and-architecture` |
| Artifact status | **provisional** |
| Cites | `domain_model.md`, `03_prd/scope_in_out.md` |

## Bounded contexts (summary)

```text
[Upstream SoRs: LIMS/MES/EBR/QMS/Safety/Inventory/IAM/DocMgmt]
        | ACL (anti-corruption)
        v
   +-----------+     +-----------+     +------------+
   | BC-BATCH  |     |  BC-PV    |     | BC-SUPPLY  |
   +-----------+     +-----------+     +------------+
        ^                 ^                  ^
        |    shared kernel: Evidence Item, as_of, Citation, Conflict, Abstention
        +--------+--------+--------+---------+
                 |                 |
           +-----------+    +------------+
           | BC-AUTHZ  |    | BC-DOCAPPLY|
           +-----------+    +------------+
                 \                 /
                  \               /
                   v             v
                 +---------------+
                 |  BC-MEASURE   |
                 +---------------+
                        |
                        v
        [External decision contexts: QP certification | Safety final | Supply allocation]
```

## Relationships

| From | To | Pattern | Rationale |
|---|---|---|---|
| Upstream SoRs | BC-BATCH / BC-PV / BC-SUPPLY | **Anti-corruption layer** | Protect ubiquitous language from LIMS/MES/Safety field slang; map units/IDs explicitly |
| BC-AUTHZ | Core three | **Upstream / conformist** | Cores conform to deny/allow; no work without authz |
| BC-DOCAPPLY | Core three | **Upstream / published language** | Publishes Applicable Document vs quarantined instruction |
| BC-BATCH ↔ BC-PV | Occasional | **Partnership** (loose) | Product-quality complaint ↔ AE linkage — cite both; no shared write model |
| BC-SUPPLY → BC-BATCH | Downstream customer | **Customer/Supplier** | Options may consume batch quality_status facts; supply must not write batch disposition |
| Core three → BC-MEASURE | Downstream | **Customer/Supplier** | Measure consumes packs/options for gates; does not own domain decisions |
| Core three → External decision contexts | Downstream OHSynchronous | **Separate contexts** | Certification / final PV / allocation **never** inside AEGIS |
| Shared kernel | Evidence Item, Conflict, Abstention, as_of, Citation | **Shared kernel** (minimal) | Keep kernel small; avoid fat shared model |

## Defended choices

- **Not** one “Pharma AI” context — would smash accountability boundaries.  
- **Not** contexts named after CSV files.  
- **ACL required** given LR-88 unit mismatch and dual LIMS contract versions.  
- External decision contexts stay outside even if UI is adjacent — PRD out-of-scope.

## Open boundary risks (Prompt 05/06)

| Risk | Impact | Mitigation intent |
|---|---|---|
| Global process owner pressures uniform automation (INJ-074) | Context ownership erosion | Keep local A on RACI; POL-BR01 |
| Product-quality ↔ PV linkage invites merged aggregate | Irreversible coupling | Partnership + citations only |
| AuthZ cache treated as shared kernel | Stale auth | IAM authoritative (P0) |
| Measure context starts “fixing” packs | Gate gaming | Measure read-only on domain outputs |
