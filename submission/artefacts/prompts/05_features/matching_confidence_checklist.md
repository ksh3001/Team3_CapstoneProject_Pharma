# Matching / Confidence Checklist

## FR-001, FR-002, FR-005, FR-006, FR-007

**N/A — no confidence-gated matching** (exact entitlement, catalog trust rules, exact product/batch identity, continuity, gates).

## FR-003 — Batch identity

| Item | Specification |
|---|---|
| Strategy order | 1) Exact `batch_id` match only |
| Fuzzy / alias | **Not permitted** in v1 (Unknown alias registry → do not fuzzy) |
| Threshold | N/A (exact) |
| Rejection | Unknown batch_id → Gap + insufficient_evidence; no guessed batch |
| Dedup | N/A |

## FR-004 — Duplicate candidates (confidence-gated)

| Item | Specification |
|---|---|
| Strategy order (fixed) | 1) Exact case_id / worldwide unique ID if present → 2) Strong deterministic key bundle (product + patient initials/hash + event date + verbatim AE term) if all present → 3) Fuzzy narrative/similarity **only if threshold defined** |
| Stage 1–2 acceptance | Exact or full strong-key equality ⇒ emit duplicate_candidate with strategy=exact\|strong_key |
| Stage 3 threshold | **Unknown** (AMB-PV-01) ⇒ **do not run fuzzy auto-link**; queue for human review instead |
| Rejection below threshold | No candidate merge; optional `required_reviews` entry `duplicate_manual_assessment`; business error intent: `duplicate_confidence_insufficient` (HTTP later in Prompt 08) |
| Dedup / quantity | Multiple candidates allowed; never irreversible merge; never collapse to single case automatically |
| Multilingual extraction confidence | **Unknown** metric (AMB-PV-02) ⇒ treat non-English source narratives as requiring human review; do not auto-drop |

**Rule:** No “best effort” fuzzy matching without a number.
