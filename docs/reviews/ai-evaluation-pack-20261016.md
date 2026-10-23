# Review Report: AI evaluation pack

## Summary
Commit `4752e27` provides a useful manual evaluation component, but two validation gaps should be corrected before using its completion result to qualify a runtime.

## Verification Checks
- [ ] **Plan Compliance**: Partial — executable CE-03 component delivered; actual runtime execution, human evaluation and native permission evidence remain pending.
- [ ] **Style Compliance**: Fail — required UTC event times are accepted as arbitrary strings.
- [x] **New Tests**: Yes — eight evaluation tests.
- [ ] **Test Coverage**: Partial — no cross-runtime aggregate or invalid event-time regression.
- [x] **Test Results**: Passed — eight evaluation and thirteen dependency tests; two additional defect reproductions succeeded.

## Findings

### Medium — Completion can combine incomplete evaluations of different runtimes
- **File**: `scripts/ppg_ai_evaluation.py` (Lines L66-L70).
- **Context**: Two cases with different runtime/model values, each given a matching recorded review, produce evaluationComplete=true. Neither runtime has completed the pack. The per-case fingerprint invalidates edits to a reviewed record but does not prevent an aggregate assembled from different models, undermining the documented requirement to rerun after a runtime/model change. The report also omits the runtime/model from its result, concealing this mixture from a report consumer.
- **Suggestion**: Require a single evaluation run configuration (runtime/model and relevant configuration revision), or report completeness independently for each configuration. Include that identity in the result and add a mixed-runtime regression.

### Medium — Execution and review times are not validated as UTC timestamps
- **File**: `scripts/ppg_ai_evaluation.py` (Lines L33-L37, L58-L61).
- **Context**: executedAtUtc="not-a-date" and reviewedAtUtc="also-not-a-date" satisfy the nonempty string checks and permit reviewed-pass/evaluationComplete=true. This violates the project UTC event-time convention and prevents reliable ordering or audit of execution versus review.
- **Suggestion**: Parse both fields as ISO-8601 timestamps with UTC offsets; reject invalid or non-UTC values and a review preceding its run. Add focused regressions.

## Decision
Recommend correcting both issues before runtime qualification. No fixes applied in this review. Existing evidence pointers remain operator-supplied assertions, as documented; this review does not authenticate underlying evidence or establish actual assistant execution, semantic acceptance or native permission trimming. The shared cited-evidence track remains in progress and owned by the integration chat.


## Remediation — 16 October 2026

The user authorised both recommendations. The evaluator now requires one runtime,
model and nonempty configurationRevision across the report, includes that identity
in its output and binds it into each review fingerprint. Mixed configurations are
rejected. Execution and passing-review timestamps are parsed as explicit ISO-8601
UTC; invalid/non-UTC values and reviews before execution fail visibly.

Both findings are resolved locally. Fourteen evaluator tests and thirteen existing
evidence tests pass (27 total), including mixed runtime/model/configuration,
missing revision, invalid/calendar/naive/non-UTC times, chronology and accepted
UTC-offset cases. Actual runtime execution, human evaluation and native permission
proof remain pending; promotionReady remains false. No native resources changed.


# Review Report: AI evaluation pack completion

## Summary
Implementation3108caf and its reporting correction complete the local/manual
CE-03 pack component; actual runtime evaluation remains unperformed.

## Verification Checks
- [x] **Plan Compliance**: Yes for CE-03 pack construction, explicit source expectations, review criteria and separate mechanical/human states; CE-04 runtime qualification remains open.
- [x] **Style Compliance**: Pass; standard-library implementation, fictional fixtures, UTC times and no native writes.
- [x] **New Tests**: Yes; seven added tests,21 evaluator tests total.
- [x] **Test Coverage**: Yes for fixed-corpus hashes, denied/missing/unsupported expectations, altered content/labels/time/version, changed review criteria, mixed configurations, chronology, incomplete CLI results and the12-case software-fixture lifecycle.
- [x] **Test Results**: Passed;21 evaluator plus13 dependency tests,34 total; CLI report saved/read back with12not-run and promotionReady=false.

## Findings

### Low — Per-case mechanical flag omitted evaluation-specific validation
- **File**: `scripts/ppg_ai_evaluation.py`, per-case report construction.
- **Context**: Source expectation validation correctly failed the overall case, but mechanicallyValid inherited only the citation checker's result and could remain true.
- **Resolution**: The flag now covers all mechanical run/case checks before human-review processing. Regression assertions verify false for wrong source state/content/label/time/version. A valid mechanical result still never substitutes for source review.

## Completion audit

| Requirement | Current evidence | Result |
|---|---|---|
| Maintained fixed fictional corpus/questions |12cases; fixture SHA-256 values independently recomputed in test | Complete |
| Expected sources and honest source states | Exact selected-source mapping, content hashes, conservative labels and denied/missing/unsupported states | Complete |
| Citations/version/quotation mismatch | Existing citation checker plus expected-source hash checks; focused negative tests | Complete for local checks |
| Archive/current authority and unknowns | Per-case rubric, expected answer status and no current-authority assertion; substantive adequacy remains human | Component complete |
| Injection and no-write requests | Dedicated refusal cases and review criteria; actions must be empty; evaluator performs no network/native writes | Component complete |
| Separate mechanical and human review | Awaiting-review state, exact subject fingerprint, explicit reviewer findings, configuration and UTC checks | Complete |
| Actual output/readback | CLI initial report saved in ignored qualification directory;12not-run, no completion/promotion claim | Complete for evaluator output |
| Actual AI responses and human evaluation | No run receipts supplied; report remains not-run | Unperformed; CE-04 |
| Native relevant-principal permission trimming | Explicitly unproved; simulated failures remain separate | Unperformed; CE-04 |

## Decision
No unresolved findings in the reviewed evaluation-pack component. The original
configuration/time findings and the source-expectation/reporting gaps are resolved
locally. The cited-evidence reader's separately recorded native metadata finding
remains outside this component and still blocks native assistant qualification.
No claim is made that the evaluator authenticates operator-supplied receipts or
performs semantic review. Source changes invalidate review fingerprints.

Retain the existing track and ownership. CE-03 is complete as a pack/tool build;
CE-01/02/04/05, native deployment, actual evaluation and operational promotion stay
open. No unrelated dirty changes were staged.
