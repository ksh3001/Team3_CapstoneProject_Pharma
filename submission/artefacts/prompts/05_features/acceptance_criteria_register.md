# Acceptance Criteria Register

| AC ID | Feature | Criterion (binary) | Primary BR |
|---|---|---|---|
| AC-001 | FR-001 | Revoked+cached user ⇒ deny; no pack/options | BR-001 |
| AC-002 | FR-001 | Active entitled QP-style user + purpose ⇒ allow | BR-002 |
| AC-003 | FR-001 | Audit has user, purpose, checked_at, decision | BR-003 |
| AC-010 | FR-002 | K-998/K-999 quarantined; not instruction-applicable | BR-010 |
| AC-011 | FR-002 | K-006 may apply; K-007 not instruction-capable when superseded | BR-012 |
| AC-012 | FR-002 | K-026 draft not instruction-capable | BR-011 |
| AC-020 | FR-003 | LR-88-style unit conflict recorded; no silent within-spec convert | BR-023 |
| AC-021 | FR-003 | execution_status not_executed; no disposition fields | BR-020/021 |
| AC-022 | FR-003 | Material conflict ⇒ not ready_for_authorized_review | BR-022 |
| AC-023 | FR-003 | Prohibited disposition shape rejected | BR-020 |
| AC-030 | FR-004 | No final PV conclusion fields | BR-030 |
| AC-031 | FR-004 | Below-threshold duplicates not auto-merged | BR-032/033 |
| AC-032 | FR-004 | Disagreeing clocks both cited + review required | BR-034 |
| AC-033 | FR-004 | K-999 not reportability authority | BR-010/030 |
| AC-040 | FR-005 | Quarantine units not available supply | BR-042 |
| AC-041 | FR-005 | no_side_effects true; no execution fields | BR-040/041 |
| AC-042 | FR-005 | No reservation created | BR-043 |
| AC-043 | FR-005 | Side-effect contract shape rejected | BR-041 |
| AC-050 | FR-006 | Model down ⇒ deterministic/manual path, not hang | BR-050 |
| AC-051 | FR-006 | AI-disabled refuses narrator; rules remain | BR-051 |
| AC-052 | FR-006 | Continuity drill completable per requirements | BR-052 |
| AC-060 | FR-007 | Prohibited batch output ⇒ gate fail; ready blocked | BR-060 |
| AC-061 | FR-007 | Supply side-effect output ⇒ gate fail | BR-060 |
| AC-062 | FR-007 | AuthZ deny case has no downstream allow pack | BR-060 |
| AC-063 | FR-007 | Machine-readable results include suite/id/result | BR-062 |
