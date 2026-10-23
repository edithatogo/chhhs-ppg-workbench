# CLI assurance and status report

The report is a read-only summary of explicit local JSON/JSONL receipts. It
classifies recorded operations as successful, incomplete or refused, lists any
explicit `*Qualified` Boolean flags, and keeps human acceptance separate. It does
not scan `.local`, inspect source content, contact Microsoft 365, or turn an exit
code into native qualification.

From the repository root, provide each receipt or journal explicitly and choose a
new private report path:

```sh
.venv/bin/python scripts/ppg_workbench.py assurance-report \
  --input .local/my-run/run.jsonl \
  --input .local/my-run/native-journal.jsonl \
  --input .local/my-run/evaluation.json \
  --output .local/my-run/assurance-status.md
```

The command accepts up to 100 `.json`/`.jsonl` inputs, 5 MiB per file and 25 MiB
combined. It rejects symlinks, malformed files and an existing report path. The
report is created exclusively with mode `0600`. It records each input path, size,
SHA-256, JSONL record or JSON object count, final event, operation outcome and explicit technical
qualification flags. It does not copy receipt bodies or error messages into the
report.

“Successful” means a supplied artifact records a recognized terminal success.
“Incomplete” includes started-only, failed-without-a-refusal-code, partial and
unrecognized receipts. “Refused” requires an explicit refusal, denial or conflict
signal. A report may therefore show a successful operation with partial or
not-stated technical qualification. Human acceptance is always reported as
“not assessed”; reviewers, content approval, publication authority and operational
acceptance require separate evidence.

Supply the relevant child and parent receipts together when a run has multiple
stages. This report summarizes only those paths; an omitted journal may contain a
later event. Preserve original receipts and create a new report after each new
operation rather than replacing evidence.
