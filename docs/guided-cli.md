# Guided CLI operation

Use the existing qualified Python and Node installations. No installation, premium
connector, new client, consent, schedule or background process is introduced.
Run from the repository root. To run a complete prepared sequence with one
command, create a private JSON plan containing the existing stage arguments:

```sh
.venv/bin/python scripts/ppg_workbench.py --plan .local/my-run/plan.json --state .local/my-run/run.jsonl
```

Create `.local/my-run` first and keep the plan and receipt in the repository's
ignored private area. Paths in the plan are relative to the current working
directory. The runner invokes existing commands directly, without a shell, and
does not change their validation, identity, publication or approval rules. It
prints each stage, declared output locations and next action. Existing single-step
commands remain available. Nothing selects records, creates a Word body, infers
authority or advances a clinical state for you.

Use `guide` for a compact route map and `STEP --help` for Python-step arguments.
Use the source/package guides below for required input contracts. A plan contains
only the stages needed for one task; do not combine unrelated cases or revisions.

## Plan format

Each stage declares an allowlisted `step`, the exact argument array passed to its
existing command, and one or more expected output paths. For a publisher whose
stdout is itself a required JSON input to a later step, set `stdoutArtifact` and
also list that path under `outputs`:

```json
{
  "schemaVersion": 1,
  "steps": [
    {
      "step": "prepare-sources",
      "arguments": ["--job", "templates/cited-evidence/source-preparation-job.json", "--input", "templates/cited-evidence", "--output", ".local/my-run/preparation"],
      "outputs": [".local/my-run/preparation"]
    },
    {
      "step": "publish-sources",
      "arguments": ["PRIVATE_CONFIG.json", ".local/my-run/preparation", ".local/my-run/native-journal.jsonl", ".local/my-run/selected.json"],
      "stdoutArtifact": ".local/my-run/publication.json",
      "outputs": [".local/my-run/native-journal.jsonl", ".local/my-run/selected.json", ".local/my-run/publication.json"]
    }
  ]
}
```

This sample demonstrates the shape only. Continue the plan with `lookup`, `excerpt`,
`validate` or `evaluate-sources` as required, declaring every new output. For
package work use `select-case`, `prepare-package`, `assemble-package` and optionally
`publish-package`. Keep the same arguments and output paths for one run; the plan's
byte hash is bound into its receipt. Outputs must be new when a stage starts. A
successful stage is complete only when every declared output exists. The runner
records a SHA-256 fingerprint for each output file/tree and verifies it before
skipping that stage on resume. Resume also requires the original working directory,
exact declared output paths and plan bytes.

| Step | Arguments after the step | Existing guide |
|---|---|---|
| `prepare-sources` | `--job JOB --input INPUT --output NEW_PREPARATION` (optional `--pdf-tool PATH`) | [Source preparation](cli-source-preparation.md) |
| `publish-sources` | `CONFIG PREPARATION NEW_JOURNAL NEW_SELECTED` | Source preparation |
| `lookup` | `--config CONFIG --query 'literal phrase' --selected SELECTED --output NEW_BUNDLE` | [Evidence lookup](cli-evidence-lookup.md) |
| `excerpt` | `--bundle BUNDLE --config CONFIG --needle 'literal text' --output NEW_ANSWER` | Evidence lookup |
| `validate` | `--bundle BUNDLE --config CONFIG --answer ANSWER --output NEW_REPORT` | Evidence lookup |
| `evaluate-sources` | `--preparation PREPARATION --bundle BUNDLE --config CONFIG --publication PUBLICATION --output NEW_REPORT` | Source preparation |
| `select-case` | `--deployment DEPLOYMENT --case-id ITEM_ID --case-uid EXPECTED_UUID --output NEW_SELECTION` | [Package preparation](cli-package-preparation.md) |
| `prepare-package` | `SELECTION/selection.json METADATA NEW_JOB JOB_ID` | Package preparation |
| `assemble-package` | `JOB INPUT EXISTING_OUTPUT_DIRECTORY` | Package preparation |
| `publish-package` | `CONFIG PACKAGE_DIRECTORY NEW_JOURNAL` | Package preparation |
| `assurance-report` | repeat `--input RECEIPT`; `--output NEW_REPORT.md` | [CLI assurance report](cli-assurance-report.md) |

The stage allowlist and fixed runtimes live in `scripts/ppg_workbench.py`; plans
cannot choose a shell, executable or additional tool. The runner does not infer
data dependencies between stages, so arguments and declared outputs must follow
the contracts in the existing guides.

## Receipts and progress

For a single-stage invocation, retain stdout as the publication JSON used by later
steps. A shell redirect creates its file before execution: file existence is not
success. Check exit status and the child journal/report. For example:

```sh
.venv/bin/python scripts/ppg_workbench.py \
  --receipt .local/NEW_ATTEMPT.jsonl publish-sources \
  PRIVATE_CONFIG.json PRIVATE_PREPARATION NEW_JOURNAL.jsonl NEW_SELECTED.json \
  > NEW_PUBLICATION.json
```

`--receipt` must precede the step. A single-stage private receipt uses exclusive
creation and mode 0600, records started/exit status, and excludes command arguments
and source content. The multi-stage `--state` receipt is also exclusive and mode
0600, append-only, and fsynced after each event. It excludes argument values and
source content, and records the plan hash, stage names, output paths/hashes and
exit codes. Keep it alongside the plan in private storage. Child native receipts
and validation reports remain authoritative; exit zero alone is not native
qualification or semantic acceptance. `--offline` forwarded to the existing
validator/evaluator retains its weaker documented evidence scope.

## Failure and restart

For a clean interruption between stages, rerun the same plan and receipt with
`--resume`:

```sh
.venv/bin/python scripts/ppg_workbench.py --plan .local/my-run/plan.json --state .local/my-run/run.jsonl --resume
```

Resume verifies the plan hash and each previously completed output before skipping
those stages. It refuses changed/missing outputs, different plans or working
directories, mismatched declared outputs, pre-existing outputs, and failed or
unknown last stages. A receipt ending in `started` means
the child outcome is unknown, never success. A failed stage may have partial effects.
In either case, preserve evidence, inspect the child journal, and reconcile native
state using the existing guide. Then create a fresh plan beginning at the first
incomplete stage and a fresh state receipt; use new output paths where the child
contract requires them. Do not edit a receipt to claim completion. The runner
never deletes outputs, retries authentication or restarts publication automatically.
The assembler/publishers retain their existing immutable revision and replay guards.
Changed inputs or human-edited outputs require an explicitly new revision. Search
misses remain indexing-unconfirmed.

## Qualification — 23 October 2026

Dispatch tests cover literal argument passing without a shell, failure propagation,
one-step execution, exclusive private receipts and argument redaction. Plan-runner
checks cover multi-stage execution, output fingerprinting, safe boundary resume,
and refusal of uncertain/changed state. A real local fictional source preparation
through this command verifies usable dispatch/output. Native route qualification
remains the separately recorded source/evidence/package proof; this increment does
not claim a new cloud run or ordinary-user acceptance.
