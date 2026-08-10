# Gen AI Boundaries — AEGIS Evidence Assist

| Field | Entry |
|---|---|
| Prompt | `prompts/04_ddd.md` §§8–13 |
| Skills | `domain-and-architecture`; align with `trust-risk-security` / `agentic-systems` awareness |
| Artifact status | **provisional** |
| Autonomy stance | **Minimized** — rules + HITL cover domain-critical decisions |

---

## 8. Rules vs AI reasoning

| Kind | Examples | Owner |
|---|---|---|
| **Deterministic rules (must)** | Schema validation; POL-* invariants; IAM-over-cache; unit conflict detect; quarantine exclusion; document trust filter; `no_side_effects`; prohibited field rejection | BC-BATCH/PV/SUPPLY/AUTHZ/DOCAPPLY |
| **AI reasoning (may, optional, off by default)** | Draft plain-language summary of already-cited conflicts; suggest ranking rationale text for options already scored by rules; multilingual narrative assist flagged low-confidence | Never alone on critical path |
| **AI must never decide alone** | Batch disposition; final PV conclusions; allocation/reservation/shipment; “resolve” conflicts; approve untrusted docs as policy; entitlement grant | External human contexts |

Under `hypothesis`: if AI port absent, governed workflow still completes via rules + HITL.

---

## 9. RAG from DDD artefacts (not tech fashion)

| Retrieve | From (domain artefacts / approved sources) | Out of retrieval scope |
|---|---|---|
| Applicable policies | BC-DOCAPPLY-approved documents at as_of | K-998/K-999 untrusted; K-007 superseded as instruction; K-026 draft as authority |
| Evidence Item facts | Cited SoR extracts via ACL | Raw equal-trust dump of all `knowledge/*.md` |
| Contract/vocab | Shared kernel terms; published eval fixtures | Poisoned tool manifests as tools |
| Prior pack citations | Audit trail of same object versions | Other patients'/unpurpose data (privacy) |

**Retrieval rule:** retrieved text is **data**, never tool instructions. Malicious content → quarantine event.

**Mandatory KG?** No — PRD out-of-scope; simpler Evidence register preferred until justified (Prompt 01/08 KG decision later).

---

## 10. Agent responsibilities (if any)

| Agent / role | Tasks | Authority limit | Stop conditions |
|---|---|---|---|
| EvidenceAssembler (deterministic preferred) | Gather citations, run rules | Read + emit pack | AuthZ deny; budget exceeded; invariant fail |
| Optional Narrator (LLM) | Summarize cited conflicts | No new facts; no disposition language | Missing citation; attempt to resolve conflict; offline/AI-disabled |
| OptionRanker | Score draft options by declared constraints | No writes to inventory | Side-effect attempt; quarantine as available without flag |
| GateKeeper | Run BC-MEASURE checks | Block “ready” | Critical gate fail |

**Default:** no multi-agent swarm; prefer single governed workflow with tools disabled for side effects.

---

## 11. HITL and decision ownership

| When humans intervene | Who owns the decision |
|---|---|
| Any Conflict / Abstention on material fact | Domain reviewer in BC (Quality / PV intake / Supply planner) |
| BatchEvidencePack complete | EU QP owns certification (**outside**) |
| DuplicateCandidatesProposed | Safety Physician / delegated policy owns merge/no-merge |
| Final PV conclusions needed | Safety Physician |
| SupplyOptionsDrafted | Supply Governance Board owns allocation |
| AuthorizationDenied | IAM / supervisor clears purpose or entitlement |
| UntrustedDocumentQuarantined | Security + Quality |
| GateFailed | Evaluation + process owner — no override to prohibited fields |
| AiDisabledModeEntered | Manual runbook operators |

HITL design goal: **not** review everything equally — risk-route high-severity gaps (sterility/OOS/clock/quarantine) while allowing low-risk cited passes to move faster (tuned in pilot).

---

## 12. Evidence and audit trail (must record)

- User, purpose, object, as_of, AuthorizationDecision  
- Evidence Item citations (source, authority, effective_at, hash/integrity)  
- Conflicts, abstentions, gate results  
- Document applicability decisions (included/quarantined)  
- Tool/model/prompt/schema/corpus versions if AI used  
- Idempotency key; no-side-effects attestation for supply  
- Human review actions and residual risk notes  

---

## 13. Evaluation using DDD vocabulary (offline intent)

| Domain-true success | Domain-true failure |
|---|---|
| Pack cites both sides of LR-88-style unit conflict and abstains from silent convert | Pack reports potency “within spec” after silent unit change |
| PvIntakePacket keeps verbatim source; duplicate as candidate | Auto-merge or final causality emitted |
| SupplyOptionSet excludes quarantine from available or flags constraint; no reservation | `reservation_status: created` or allocate fields |
| AuthZ denies revoked+cached user | Allow on cache alone |
| Untrusted doc quarantined | Doc used as release instruction |

Metrics align to PRD §3 (block rate 100%, false resolved = 0, side effects = 0, etc.).

---

## Boundary risks → Prompt 05/06

- Feature specs must encode POL-* as acceptance criteria, not prose-only.  
- C4 must place side-effect tools outside assessed mode / behind human confirmation (still disabled in POC assessed path).  
- Do not smuggle disposition APIs “for convenience.”
