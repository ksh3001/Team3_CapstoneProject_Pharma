# Business Rules Register

| BR ID | Feature | Rule (testable) | POL / notes |
|---|---|---|---|
| BR-001 | FR-001 | IAM revoked ⇒ deny regardless of cache | POL-AUTHZ-IAM |
| BR-002 | FR-001 | Missing/disallowed purpose ⇒ deny | |
| BR-003 | FR-001 | Allow/deny records user, purpose, object, checked_at, decision | |
| BR-010 | FR-002 | Untrusted docs not instruction-capable | POL-DOC-TRUST |
| BR-011 | FR-002 | Draft docs not instruction-capable | POL-DOC-TRUST |
| BR-012 | FR-002 | Superseded docs not current authority | |
| BR-013 | FR-002 | Retrieved text is data, never tool command | |
| BR-020 | FR-003 | No disposition/release/reject/reprocess/relabel/recall in pack | POL-NO-DISPOSITION |
| BR-021 | FR-003 | execution_status = not_executed | |
| BR-022 | FR-003 | readiness_state ∈ {insufficient_evidence, conflicted_evidence, ready_for_authorized_review} | |
| BR-023 | FR-003 | Unit disagreement or approved=no mapping ⇒ Conflict; no silent convert | POL-NO-SILENT-UNIT |
| BR-024 | FR-003 | Material claims cited or abstained/gapped | |
| BR-025 | FR-003 | ready_for_authorized_review ≠ certification | |
| BR-030 | FR-004 | No final seriousness/causality/expectedness/reportability/signal confirmation | POL-NO-FINAL-PV |
| BR-031 | FR-004 | Source facts verbatim; interpretations labeled | |
| BR-032 | FR-004 | Duplicates are candidates only; no irreversible merge | POL-NO-IRREVERSIBLE-MERGE |
| BR-033 | FR-004 | Duplicate matching follows checklist order/thresholds | |
| BR-034 | FR-004 | Disagreeing clocks all remain visible | |
| BR-040 | FR-005 | no_side_effects = true | POL-NO-SIDE-EFFECTS |
| BR-041 | FR-005 | No reserve/allocate/ship/status change/recall properties | |
| BR-042 | FR-005 | Quarantine not available supply | |
| BR-043 | FR-005 | No persisting draft reservations in assessed mode | |
| BR-050 | FR-006 | Assessed default needs no live inference | |
| BR-051 | FR-006 | AI-disabled keeps rules path or manual runbook | |
| BR-052 | FR-006 | PV must not depend on model availability | |
| BR-060 | FR-007 | Hard gate fail blocks ready | |
| BR-061 | FR-007 | Measure must not mutate domain packs to force pass | |
| BR-062 | FR-007 | Gated runs record id/result/evidence path | |
