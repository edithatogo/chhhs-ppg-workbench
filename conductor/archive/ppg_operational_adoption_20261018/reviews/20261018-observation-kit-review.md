# Review Report: OA-01/OA-03 baseline measurement and observation kit

## Summary

The bounded CSV/CLI instrumentation is implemented and verified; actual participant
access, observations, full-cycle acceptance and real benefits remain unperformed.

## Verification Checks

- [x] **Plan Compliance**: Yes for selected OA-01/OA-03 — maintained task/measure dictionary, matched old/new inputs, effort/waits/counts/outcomes, missingness and exclusions. Source/period/version identity retained. Forms/Power BI/participant prerequisites excluded from instrumentation.
- [x] **Style Compliance**: Pass — existing Python standard library, CSV template and process-reporting command; no new analytics service or tenant component.
- [x] **New Tests**: Yes — ten observation tests and twelve existing process-measure regressions pass.
- [x] **Test Coverage**: Yes for selected local instrumentation; fictional and blank end-to-end commands, legacy format/arithmetic, strict matching, zero/missing values, invalid inputs, formulas, provenance and no-overwrite checked. Real observation is not claimed.
- [x] **Test Results**: Passed — 22 affected tests. Fictional run returns two one-sample task comparisons and excludes the held pair; blank run returns no attempts/comparisons and Not measured. Legacy 200-second/median45 example unchanged.

## Findings

### Medium — fixed: exact input-byte provenance

- **File**: `scripts/ppg_process_measures.py`
- **Context**: Text-mode reading can normalise CRLF and discard a UTF-8 BOM, so a decoded-text hash alone cannot identify the actual input file bytes.
- **Fix applied**: Observation CLI reads bytes and stores their SHA-256; decoding is separate. Regression uses BOM/CRLF input and confirms unchanged source bytes and exact digest.

### Medium — fixed: finite values can overflow during aggregation

- **File**: `scripts/ppg_observation_measures.py`
- **Context**: Individually finite measurements can sum/average to Infinity, which must not be exported as a valid time measure.
- **Fix applied**: Validate numeric inputs and refuse nonfinite report aggregates before output creation. A regression supplies two individually finite extreme values and verifies refusal.

## Review and scope

Reviewed the observation helper, the existing CLI's additive mode, dictionary,
blank/matched fixtures, existing example, maintained guides and tests. Original
portfolio/event calculations and fixtures are unchanged; twelve process tests
pass. Known/missing denominators remain distinct, zero is a valid observed value,
held/failed tasks cannot enter completed timing comparisons and unmatched periods
or versions never compare. Per-task signed differences are descriptive, not pooled
savings or causal effects. Real data are not invented or imported for this proof.

Output CSV contains fixed keys/numeric summaries; free-text references/notes stay
in private JSON/source CSV. Existing output directories and human edits are
preserved. Source CSV is never mutated. Exact input and dictionary hashes retain
provenance. Ten-column legacy observation files remain readable. Dataset cohort
mixing, duplicate run/task or pair/method rows and malformed values fail visibly.

The preferred SharePoint structured-document route is not replaced: this extends
the existing editable CSV and technical CSV/JSON projection. No new Word generator,
Forms collection, BI audience, database, schedule or native writer is introduced.
No licences, permissions, participants, credentials or tenant access are required
for the selected local route. No clinical work, invitation or messaging occurred.

OA-01/OA-03 technical slice is complete; preserve OA-02/OA-04/OA-05 and the broader
track as open. Ordinary-user identity/access needs an actual authorised participant;
no impersonation or admin-to-user inference. Benefit remains Not measured for the
fictional/blank proof. Private receipts: `.local/observation-kit/20261018/`.
