# Domain Model — AEGIS Evidence Assist

| Field | Entry |
|---|---|
| Prompt | `prompts/04_ddd.md` |
| Skills | `domain-and-architecture` (DDD); thin lens via `process-and-lean-discovery`; routed via `fde-operating-model` |
| Prerequisites | `01_discovery/`, `02_scqa/`, `03_prd/` |
| Team | Team3 |
| As-of | 2026-08-06 |
| **Artifact status** | **provisional** |
| Narrative class | `hypothesis` (unchanged) |

**Rule:** Prefer **rules + HITL** over autonomous AI. Do not treat this model as production domain truth until P0 SoT questions close (`01_discovery/evidence_acquisition_backlog.md`).

---

## 1. Frame business problem (domain terms)

Within PRD scope, the domain problem is: **Evidence Reconciliation for Regulated Human Decisions** — assembling cited, temporally applicable, authority-ranked evidence so accountable humans can decide batch certification readiness inputs, PV case handling, and supply allocation options — without the assist system owning those decisions.

Governing experiment (Prompt 02): Measure-first hybrid — MDM/rules + narrow fail-closed evidence-assist; generative AI optional/off by default.

---

## 2. Domain and subdomains

| Subdomain | Type | Why |
|---|---|---|
| **GxP Batch Evidence Reconciliation** | **Core** | Primary value + highest GxP defect risk if wrong |
| **Pharmacovigilance Case Intake Support** | **Core** | Clock/duplicate/listedness integrity; patient safety adjacent |
| **Bounded Supply Option Planning** | **Core** | Shortage ethics + no side effects; allocation accountability external |
| Document / Policy Applicability | Supporting | Authority, effective date, supersession, jurisdiction |
| Identity & Authorization (purpose-bound access) | Supporting | Entitlement at execution time |
| Master Data & Unit Semantics | Supporting | Product/batch/case identity; unit conflict detection |
| Measure / Evaluation of Assist Quality | Supporting | Experiment KPIs; gates |
| Brownfield Systems of Record (LIMS, MES, Safety DB, Inventory, …) | Generic / external | Upstream facts; not owned by AEGIS |
| Model Hosting / Token Metering | Generic / external | Optional; out of core domain meaning |

---

## 3. Ubiquitous language

### Resolved terms (provisional glossary)

| Term | Meaning in AEGIS | Must not mean |
|---|---|---|
| **Evidence Item** | A cited fact with source, authority, effective_at, integrity, and verbatim value where applicable | An instruction to the model/tool |
| **Applicable Document** | Knowledge/policy with trust/status allowing use at as_of and jurisdiction | Any markdown in the corpus |
| **Conflict** | Two or more Evidence Items that disagree on identity, unit, time, authority, or material fact | A bug to silently “fix” |
| **Abstention** | Explicit non-resolution when conflict/gap cannot be governed | Empty output or invented consensus |
| **Review Readiness** | Structured assessment of evidence completeness/conflicts for **human** review | Batch release / disposition / certification |
| **Batch Disposition** | Release / reject / reprocess / relabel / recall decision | Anything the assist may emit |
| **ICSR Intake Packet** | Preserved source facts + candidates + clocks + required human reviews | Final seriousness/causality/reportability |
| **Duplicate Candidate** | Suggested possible same-case linkage | Irreversible merge |
| **Supply Option** | Ranked draft plan with constraints and approval needs | Reservation, allocation, shipment |
| **no_side_effects** | Assessed mode makes no inventory/quality/recall state change | “Planning” that writes reservations |
| **Available for options** | Inventory considered only when quality_status permits per policy | Sum of all units including quarantine |
| **Current Entitlement** | IAM authoritative active grant for user×purpose×object | Gateway cache alone (`active_cached`) |
| **as_of** | Instant for temporal applicability of evidence/documents | “Latest file wins” without authority |

### Unresolved / overloaded (remain provisional)

| Term | Issue | De-provisionalizer |
|---|---|---|
| `review readiness` enums | Exact enum set not locked to schema yet | Align to `evaluation/contracts/batch_response.schema.json` in Prompt 05/08 |
| `OOS_LIMS` vs investigation states | Lab vs OOS process language collision | QC ubiquitous language workshop (P1 unit/SoT) |
| `conditionally_released` / `validated` / `research_only` | Conflicting inventories for AI-EVIDENCE | P1 validation SoT |
| `active_cached` | Technical status leaking into domain | Entitlement SoT policy (P0) |
| Event time vs report time | Clock semantics per object | P1 clock dictionary |

**Anti-corruption:** Do not import LIMS/MES/Safety DB field names as domain nouns without mapping through an ACL; do not treat dataset filenames as bounded contexts.

---

## 4. Bounded contexts (with owners)

| Context ID | Bounded context | Business owner (accountable) | Decisions owned in context | Assist may |
|---|---|---|---|---|
| BC-BATCH | Batch Evidence Reconciliation | EU QP / Quality (certification outside); Quality reviewer operates assist | What evidence is cited; what conflicts/gaps/abstentions exist; readiness **input** | Recommend/cite/flag/abstain |
| BC-PV | PV Intake Support | Global Safety Head / Safety Physician (final calls outside) | Packet completeness; duplicate **candidates**; clock provenance; review queues | Extract/normalize/cluster/cite |
| BC-SUPPLY | Supply Option Planning | Supply Governance Board (allocation outside); planner operates assist | Option ranking; violated constraints; required approvals | Draft options only |
| BC-AUTHZ | Purpose-Bound Authorization | CISO / IAM + process owner for purpose | Allow/deny execution | Enforce deny-by-default |
| BC-DOCAPPLY | Document Applicability | Document control / Quality | Which docs are applicable at as_of | Filter/quarantine; never execute untrusted instructions |
| BC-MEASURE | Assist Evaluation & Gates | Evaluation / Quality risk owner | Gate pass/fail for “ready” claims | Score; block |

Owners marked from `decision_rights.csv` + stakeholder pack; TBD refinements flagged where CSV thin.

---

## 5. Entities, value objects, aggregates & invariants

### Aggregates (core)

| Aggregate | Root | Key invariants (always hold) |
|---|---|---|
| **BatchEvidencePack** | BatchId + as_of + purpose | No disposition fields; every material claim cited or abstained; unit conflicts not silently converted; `execution_status` remains non-executing |
| **PvIntakePacket** | Case/SourcePackageId + as_of + purpose | Source facts preserved verbatim; duplicates are candidates only; no final safety conclusions; clocks cited with provenance |
| **SupplyOptionSet** | ShortageEventId + as_of + purpose | `no_side_effects = true`; quarantine not treated as available without explicit rule+flag; no reserve/allocate/ship/status/recall properties |
| **AuthorizationDecision** | User + purpose + object + as_of | IAM state authoritative over cache when revoked; deny on purpose mismatch |
| **ApplicableDocumentSet** | Query + as_of + jurisdiction | Untrusted/draft/superseded not used as instructions; supersession visible |

### Value objects (examples)

`EvidenceCitation`, `AuthorityTag`, `EffectiveInterval`, `QuantityWithUnit`, `QualityStatus`, `MedDRACodingRef`, `ReportingClockSpan`, `ConstraintViolation`, `GateResult`.

### Policies (POL-*)

| ID | Policy |
|---|---|
| POL-NO-DISPOSITION | When producing BatchEvidencePack then disposition/certification fields must be absent |
| POL-NO-FINAL-PV | When producing PvIntakePacket then final seriousness/causality/expectedness/reportability/signal confirmation must be absent |
| POL-NO-SIDE-EFFECTS | When producing SupplyOptionSet then no inventory/quality/recall mutation and no_side_effects true |
| POL-NO-SILENT-UNIT | When units disagree or mapping unapproved then Conflict + Abstention — never silent convert |
| POL-NO-IRREVERSIBLE-MERGE | When duplicate candidates exist then no auto-merge |
| POL-AUTHZ-IAM | When IAM revoked then deny even if cache active |
| POL-DOC-TRUST | When document trust≠approved (or superseded/untrusted/draft) then not instruction-capable |
| POL-BR01 | Assist must not weaken Quality independent authority |

---

## 6. Domain events (event storming equivalent)

| Domain event | Trigger | Primary actor | Context |
|---|---|---|---|
| EvidenceReconciliationRequested | User starts batch pack | Quality reviewer | BC-BATCH |
| ConflictDetected | Divergent Evidence Items | System rules | BC-BATCH / BC-PV / BC-SUPPLY |
| AbstentionRecorded | Unresolved conflict/gap | System / reviewer | core BCs |
| BatchEvidencePackPrepared | Pack complete for human review | Quality reviewer | BC-BATCH |
| BatchCertificationPerformed | Human certifies/rejects | EU QP | **Outside** AEGIS |
| PvIntakeStarted | Source package received | Intake scientist | BC-PV |
| DuplicateCandidatesProposed | Clustering rules/AI assist | System | BC-PV |
| ReportingClockReconstructed | Receipt/awareness facts cited | System | BC-PV |
| SafetyConclusionRecorded | Final PV decision | Safety Physician | **Outside** AEGIS |
| ShortageOptionsRequested | Shortage/cold-chain event | Supply planner | BC-SUPPLY |
| SupplyOptionsDrafted | Options ranked | System | BC-SUPPLY |
| AllocationApproved | Human governance | Supply Governance Board | **Outside** AEGIS |
| AuthorizationDenied | Stale/missing entitlement | BC-AUTHZ | BC-AUTHZ |
| UntrustedDocumentQuarantined | Poisoned/untrusted content | BC-DOCAPPLY | BC-DOCAPPLY |
| GateFailed | Eval hard fail | BC-MEASURE | BC-MEASURE |
| AiDisabledModeEntered | Outage / kill switch | Ops | All (manual path) |

---

## 7. Minimum governed workflow (domain)

1. Authorize (BC-AUTHZ) for purpose×object×as_of.  
2. Assemble Evidence Items from upstream SoRs via ACL.  
3. Apply Document Applicability (BC-DOCAPPLY).  
4. Run deterministic conflict/invariant checks (rules).  
5. Optionally draft narrative assist (**off by default**) — never override invariants.  
6. Emit pack/options with citations, conflicts, abstentions, required human reviews.  
7. Human decides in external SoR (certify / PV final / allocate).  
8. Record audit + gate results (BC-MEASURE).

---

## 8. Pilot / refine notes (`provisional`)

| Learn in pilot | Would stabilize domain model if… |
|---|---|
| Which conflicts dominate rework | Cycle-time + conflict taxonomy measured (P0) |
| Whether reviewers accept abstentions | HITL overload vs under-catch tuned |
| Whether LLM adds value beyond rules | Falsifiers + TCO after MDM/rules |
| Validation SoT for AI-EVIDENCE | Single authoritative inventory (P1) |

Executed later in Prompt 11 `pilot_learnings.md`.

---

## 9. Production readiness concerns (domain view only)

- Unresolved SoT for entitlement, units, validation state, clocks.  
- Risk of ubiquitous language drifting back to dataset/API names.  
- Context ownership unclear if global process owners override local QP/Safety (INJ-074).  
- Handover: domain policies POL-* must survive vendor/model exit.

Executed later in Prompt 12/13 production readiness — not full C4 here.

---

## 10. Link to Prompt 01 acquisition backlog (de-provisionalizers)

| Backlog | Stabilizes |
|---|---|
| P0 cycle time | Measure language; CTQ |
| P0 knowledge SoT rules | BC-DOCAPPLY; Applicable Document |
| P0 entitlement SoT | BC-AUTHZ; Current Entitlement |
| P1 unit mapping authority | QuantityWithUnit; POL-NO-SILENT-UNIT |
| P1 AI-EVIDENCE validation SoT | Intended-use boundary for assist |
| P1 clock dictionary | as_of semantics |
| P1 review hours | HITL cost in domain economics |
