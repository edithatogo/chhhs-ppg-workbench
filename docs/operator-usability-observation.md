# Baseline measurement and operator observation

> Current native recovery/reporting increment: [21 October qualification and restart procedure](recovery-qualification-20261021.md). Earlier sections retain their dated scope.

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Reuse [process measures](process-reporting.md) and `config/process-measures.json`
for case counts, missing follow-up evidence and linked calendar intervals. Those
measures do not measure active working time. This small manual observation sheet
adds task-level observations without changing existing measures or introducing a
List, service, dashboard, schedule or respondent record.

Download `operator-observation.csv` and save a new dated copy in approved storage.
Use one walkthrough ID and one row per attempted task. `asOf` is the observation's
actual timestamp with timezone; never substitute this guide's publication date.
Set datasetKind to operational or fictional and keep cohorts separate. The supplied
`fictional-observation.csv` is illustrative accounting, not a timed native test.

| Field/measure | Meaning and denominator |
| --- | --- |
| outcome | completed, held, failed or not-observed; counts describe all attempted tasks, excluding not-observed |
| durationSeconds | Nonnegative observed hands-on duration; blank is unknown. Timing sample includes only completed tasks with valid observed duration. Report sample count and total/median for those tasks; do not call their sum a complete-workflow duration when tasks are held or excluded. |
| missingInputCount | Count of distinct missing required inputs encountered within the task; blank unknown. Sum counts over tasks with a known count and report that task denominator; repeated missing inputs across tasks may be counted again. |
| helpRequired | yes, no or blank unknown. Help rate is yes rows divided by attempted rows with known yes/no; report both counts. No helper identity or message content. |
| correctionCount | Number of actual corrective/rework actions within that task; blank unknown. Sum with the number of tasks having a known count. It is not a count of distinct cases. |
| exclusionReason | Explain held/failed/not-observed or omitted timing without personal or content details. |

Fictional example:5attempted tasks,4completed and1held. Timing has4samples totalling
200seconds, median45seconds; this is not total workflow time. Help is2/5tasks,
missing inputs2across5known-count tasks, corrections1across5known-count tasks.
These are arithmetic examples only. Real-use measures and time savings are
**Not measured** until actual comparable observations exist. Do not substitute
case age or event calendar days for hands-on duration.

For new maintained Word output, the preferred structured-document route remains
subject to its recorded production prerequisites. This deliverable is an editable
CSV observation format and short guide, so it reuses the existing supported format
without a Word generator or dependency on that unavailable route.

## Baseline and matched observations — OA-01/OA-03, 18 October 2026

The maintained kit extends this CSV and the existing process-reporting command.
[Observation dictionary](../config/observation-measures.json) freezes five task
keys, completion criteria, baseline method and denominator rules. The existing
[process dictionary](../config/process-measures.json) continues to define case
counts and linked event calendar intervals; those definitions are unchanged.

1. Save a new copy of `templates/operator-usability/operator-observation.csv` in
   approved private storage. Use fictional data for practice; actual observations
   require an authorised participant later. Do not invent participant identities,
   policy decisions or observations to complete instrumentation.
2. Choose a small fixed task/input set and the same completion standard for both
   methods. Observe the old/manual route as `baseline` and the workbench route as
   `workbench`. Time actual hands-on work, pausing for interruptions/waits; do not
   estimate it from recall, Created timestamps or case age. Preserve held/failed
   attempts and missing timing rather than recording only successes.
3. Use a different opaque `walkthroughId` for each run and one row per task/run.
   Give the matched old/new task a shared `pairId`. Record identical `inputRef`,
   `sourcePeriod`, `sourceVersion` and `taskVariant` for a comparable frozen task.
   A later retry needs a new run/pair identity; duplicates are refused.
4. Record actual timezone-bearing `asOf`, outcome, assistance, corrections and
   missing-input counts. Blank is unknown; zero means actually observed zero.
   Give an exclusion reason for held/failed attempts or missing completed-task
   timing. `not-observed` rows cannot contain measured values.
5. Inspect denominators/exclusions and retain original inputs with the generated
   snapshot. Do not pool different tasks or interpret learning/order effects,
   changed inputs or small samples as causal benefit.

| Added field | Meaning |
|---|---|
| method | baseline, workbench, or blank/unclassified for legacy observations |
| pairId | Opaque matched-task comparison reference; absent means unpaired |
| inputRef | Stable reference to the exact frozen task inputs; no document narrative |
| sourcePeriod | The source/report period represented by those inputs, not observation date |
| sourceVersion | Exact baseline/snapshot/template version relevant to the task |
| taskVariant | Fixed task shape/complexity, such as one-reference or one-case |
| stageWaitSeconds | Optional directly observed inactive wait within the task. Completed-task samples only; separate from hands-on time and existing linked-event calendar days. Blank remains unknown. |

A pair is eligible only with exactly one baseline and one workbench attempt for
that task, equal nonblank input/period/version/variant, completed outcomes and known
hands-on times. Missing counterparts, unknown/mismatched identity and held/failed
or untimed attempts are listed as comparison exclusions. Separate task timing and
count summaries still describe their qualified observations. No cross-task
aggregate saving or full-workflow elapsed time is computed.

## Run the existing CLI

The CSV route uses Python's standard library and no tenant connection, Forms,
Power BI, premium connector or new service. Use the existing project environment:

```sh
.venv/bin/python scripts/ppg_process_measures.py \
  --observations templates/operator-usability/fictional-matched-observation.csv \
  --output .local/observations/fictional-run-1
```

For real use replace the CSV path with the private observed copy and choose a new
output directory. The command emits `observations.json` and `observations.csv`.
It validates the full input before creating output and never overwrites an existing
report directory. Input CSV is never changed. Legacy ten-column observation files
remain readable; they are unpaired/unclassified unless additional fields exist.

JSON includes exact input-byte SHA-256, observation/process dictionary hashes,
source/period references, observation dates, walkthrough count, method/task
summaries and row-level exclusions. The direct helper hashes supplied text; the
CLI hashes actual bytes, including a UTF-8 BOM and CRLF when present. Walkthroughs
are runs, not participant or case counts. JSON may contain private references and
exclusion notes: retain it with the input in approved private storage.

CSV summaries contain fixed task/measure keys and calculated values, not free-text
input references/notes that could become Excel formulas. Each value retains its
sample/known-task denominator. Hands-on and wait summaries report their respective
sample sizes, missing completed observations and excluded noncompleted tasks.
Help is yes/known responses, never yes/all rows when responses are missing; 0/0 is
unknown. Missing-input/correction totals include only attempted tasks with known
counts; repeated inputs across tasks may recur. Empty cohorts and zero timing
samples return null/blank values, never a fabricated zero duration.

The fictional matched example has six attempted tasks and two eligible pairs:
find-evidence differs by 60 seconds and find-case by 20 seconds (baseline minus
workbench). Each comparison has one sample. The held package pair is excluded.
These deliberately constructed values prove arithmetic, not time saving. The
blank template produces zero attempts, no comparisons and **Not measured**.
The original five-task fictional example still reproduces 200 seconds/median45.
Negative matched differences correctly indicate more observed workbench time.

Fictional and operational observations cannot be mixed in one input. An operational
label does not prove that a measurement occurred or that the participant has
ordinary-user access. Actual participant observation/access belongs to OA-02;
benefit interpretation and full-cycle evidence remain separate. Forms adds no
needed behaviour for this bounded CSV route and is deferred. Power BI workspace,
reader licensing and refresh qualification remain OA-04, not kit prerequisites.
No invitation, notification, source update or native object change occurs.


## Discharge-review outcomes — OA-06

Use the existing matched task CSV for observed hands-on reviewer effort. The
additional [blank outcome template](../templates/operator-usability/review-outcomes.json)
captures explicit usefulness/false-positive judgments and decision intervals. The
[fictional example](../templates/operator-usability/fictional-review-outcomes.json)
is deliberately constructed arithmetic, not observed benefit. Copy a template to
approved private storage before entering operational data; retain exact input bytes.

Each judgment identifies `reviewRunId`, `documentUID`, exact `documentSha256` and
`findingRef`. `usefulAccepted` and `falsePositive` are booleans or null (unknown),
with actual timezone-bearing `judgedAt` and `decisionRef` for known judgments.
Do not infer either judgment from suggestion disposition, generated finding count,
source coverage or a successful technical trial. Not accepted does not mean false
positive; accepted and useful is a combined explicit observation. Both true is a
conflict requiring reconciliation. Duplicate finding/run judgments are rejected;
the denominator is finding judgments within runs, not distinct suggestions overall.

Decision rows use the same run/document binding, actual timezone-bearing `startedAt`
and `decidedAt`, and `decisionRef`. Missing end is unresolved. A zero-second interval
is valid; negative intervals and missing start/evidence for a decision are rejected.
Elapsed calendar time is separate from hands-on effort and supplies no savings or
causal-benefit claim. Multiple decisions for one run or conflicting document hashes
require separate/reconciled run identities rather than double counting.

```sh
.venv/bin/python -m scripts.ppg_review_outcomes \
  --input .local/observations/review-outcomes.json \
  --output .local/observations/review-outcomes-report.json
```

Output is create-only, carries exact input SHA256 and retains known/unknown
judgment denominators and decision interval sample/missing counts. Zero known
judgments means unknown rate, not zero false positives. An empty template yields
Not measured and null timing. Each dataset has one fictional/operational kind;
conflicting row kinds are rejected. A supplied operational label or evidence
reference does not verify an observation, clinical authority or ordinary-user access.

Read unresolved catalogue coverage separately from the dated review-pack receipt;
no comparison coverage is derived from benefit judgments. Current pack10 retains
its frozen snapshot and later source-only companions retain their own scopes.
Current procedure/template, Word fidelity and operational benefits remain unresolved.

The supplied fictional example has1/2 useful-accepted,1/2 false-positive,1 unknown
judgment for each measure and3600 elapsed seconds. Blank/fictional reports reproduce
exactly from the downloaded nine-member recovery archive; CRC/all hashes and three
archived tests pass.25 related local checks pass. Seven native companion files have
byte/identity/version/inherited-access readback and repeat upload creates0. Existing
report retry refuses without overwriting. Native/private companion review-outcomes-v1
retains templates, reports and recovery instructions. No operational observation,
clinical decision, List-record mutation, permission or notification is fabricated.
This extends the existing manual observation stage only; frozen workflow1.6 and
all earlier releases/packs remain unchanged, with no new transition/flow/schedule.
