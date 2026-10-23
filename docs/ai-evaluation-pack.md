# AI evaluation pack

This local/manual evaluator consumes the cited-evidence assistant's maintained
12-case fictional pack. It invokes no AI runtime and performs no Microsoft writes.
Each case includes exact expected source statuses and, for readable fictional
sources, SHA-256 and authority label. A receipt with the right ID but different
content or status fails. The expected hashes are checked against the maintained
fictional corpus by the tests. Each case also has a source-review checklist,
which appears in the report even when that case is not run.

The cases cover citations, archive authority, edition conflict, draft approval,
prompt injection, denied/missing/unsupported sources, stale versions, write
requests, empty search and unknown operative authority.

Run from the repository root:

```sh
python3 scripts/ppg_ai_evaluation.py --runs templates/ai-evaluation/empty-runs.json
```

The initial report must show all cases `not-run`, not pass. Exit 1 means incomplete
or failed evaluation; exit 2 means invalid input or an unreadable input file.
Exit 0 means every case has both mechanical checks and a recorded source review. It never grants promotion.

All records in one report must use the same runtime, model and nonempty
`configurationRevision` (the maintained prompt/skill/settings revision). Mixed
configurations are rejected with exit 2; evaluate each configuration separately.
The report includes this configuration, and each review fingerprint includes it.
Execution and passing-review times must be ISO-8601 UTC timestamps ending in `Z`
or `+00:00`. A review cannot precede its execution. Invalid times fail the case.

For an authorised runtime, capture each actual response privately under
`.local/ai-evaluation/`. Supply a JSON array with one record per case:

- `caseId`, exact `question`, `runtime`, `model`, `configurationRevision`, `executedAtUtc`.
- `allowedPrefix`: the qualified HTTPS selected-source folder.
- `rawResponseEvidence`, `retrievalEvidence`, `actionAuditEvidence`: private evidence
  pointers. Retain actual prompt/response, retrieved bytes/version receipts and tool
  activity. The evaluator records pointers; it cannot authenticate their truth.
- `sources`: complete selected-source receipts in the cited-evidence contract,
  including explicit denied/missing/unsupported states with no content.
- `answer`: the actual structured output accepted by `ppg_evidence_check.py`.
- `observedActions`: the independently inspected tool actions; must be empty.
- `humanReview`: `result` (`pass` or `fail`), `reviewer`, `reviewedAtUtc`, `evidence`,
  `findings`, and `subjectSha256` from the initial evaluation report.

Use the case-specific `reviewCriteria` in the report when reviewing each question
against its exact retrieved evidence. Check factual adequacy,
source entailment, honest unknown/conflict/authority labels, and absence of denied
information, injected instructions or writes. Record specific findings rather than
keywords or the assistant's self-rating. The review fingerprint binds the case,
sources, answer and runtime/evidence receipt; changing any of those invalidates the previous review.
Private evidence can contain identity and native URLs; do not commit it.

The report distinguishes `not-run`, `failed`, `awaiting-human-review` and
`reviewed-pass`. Missing or duplicate cases cannot disappear into an average.
A successful mechanical check is not a human review. These supplied receipts are
not proof of native permission trimming: actual relevant-principal retrieval must
be demonstrated separately. Model/runtime changes require a new captured run;
retain previous runs and review records. This pack does not select a provider,
authorise real policy processing, make clinical judgments or promote a service.

The cited-evidence track owns runtime qualification and eventual hosting/navigation.
Use the same pack for its selected pilot; do not create another Teams tab or a
parallel source corpus. Native execution, semantic acceptance and operational
promotion remain separately evidenced milestones.

## Build and runtime status

The pack/evaluator is an implemented local/manual component of CE-03. This does
not close CE-04 (actual assistant qualification) or the cited-evidence track.
Its initial 12-case report deliberately remains `not-run`; no actual model
responses or human source reviews have been supplied. Permission trimming and
operational promotion remain separate and unproved. Run with a selected eligible
runtime only when that track's runtime/source-access requirements are met.

Verification:

```sh
python3 -m unittest discover -s tests -p 'test_ai_evaluation.py'
python3 -m unittest discover -s tests -p 'test_evidence*.py'
```

Custom packs passed with `--pack` must include, per case, `caseId`, `question`,
`selectedSources`, `expectedSources`, `expectedStatus` and nonempty
`reviewCriteria`. The expected-source mapping must cover exactly the selected
IDs. Changing any case expectation or review criterion invalidates its previous
review fingerprint. Custom-pack results apply only to that reported pack hash.
No source text or run evidence is generated or accepted as a real runtime run by
these software tests. Supplied receipts still need independent source review.
