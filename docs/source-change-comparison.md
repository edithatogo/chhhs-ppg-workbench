# Source-change comparison and affected cases

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

This read-only local/manual tool compares preserved source-register values and
shows cases linked to changed DocumentUIDs. It does not compare the policy text,
establish current authority, perform review or update case decisions. The tool and operator guide are hosted in the existing evidence library, with
a frozen comparison linked from Start Here. Refresh remains local/manual.

Use repo-local Python 3.15.1 from this repository:

```sh
.venv/bin/python scripts/ppg_source_comparison.py \
  --baseline templates/source-comparison/baseline.json \
  --candidate templates/source-comparison/candidate.json \
  --cases templates/source-comparison/cases.json \
  --output .local/source-comparison/example-1
```

Open `comparison.html` in the new output directory. The accompanying JSON retains
machine-readable before/after values and input hashes. Output directories must
be new: repeat with another name; existing reports are never overwritten.
Keep operational inputs and reports in ignored `.local/`, under existing access.
These reports can contain clinical-governance source details.

For operational use, obtain the exact complete prepared plan associated with the
last successful reconciliation and verify its hash against that checkpoint's
receipt. A successful metadata poll is not a baseline. Supply the latest extracted
candidate plan separately, including unresolved identity exceptions. Never reuse
an old candidate as evidence of a newly observed source version. Use the existing
`ppg_source_sync.prepare` contract; do not regenerate the baseline or change the
identity ledger to make comparison succeed. Snapshot references and source hashes
are retained, but this tool cannot independently authenticate supplied extracts.

Cases are a JSON array containing `CaseUID` and `linkedDocumentUIDs`, either a UUID
array or its JSON-encoded string. Export all relevant cases with existing access;
do not omit closed cases silently. Other fields, including next actions, are
ignored and preserved in the input. Malformed/empty links and linked identities
absent from both plans are reported as unresolved, not unaffected. SharePoint
export wrappers must be unwrapped to their item array before use.

Every raw source field is compared exactly, including fields outside the summary
projection. Absent and null are distinct. Row order/projection timestamps alone
are not content changes. Unknown aliases remain exceptions; the report can still
show changes for known identities, labelled partial and reconciliation held.
Missing records are exceptions, never retirement. Cases are affected candidates
for human attention, not automatically reopened, reassigned or marked ready.

The tool makes no tenant calls, writes no input files, advances no checkpoints,
and sends no notifications. It does not alter the importer. The four Teams tabs
remain unchanged. A browser-readable local report is not a deployed Teams view.

## Retained native acquisition qualification

Use `scripts/ppg_source_comparison_inputs.py` with the existing qualified extraction
runtime (pyxlsb 1.0.10, already used for the baseline). The ordinary comparison
command needs only Python's standard library. The acquisition adapter does not
install dependencies, call Microsoft APIs or run workbook macros. Supply native
exports of `--baseline`, `--baseline-raw`, `--observed-raw`, `--checkpoint`,
`--state`, `--ledger`, `--cases`, the canonical acquisition URL as `--observed-ref`,
and a new `--output` directory. Keep exports private. The bundled CSV mapping is
checked by exact ordinal headers, including both distinct Audit Approach fields.

The adapter verifies baseline bytes/hash, source identity and ETag, committed
record accounting and identity contract. It must reproduce every baseline raw
cell before extracting the observed acquisition. It rejects parser/header drift,
stale acquisition bindings or changed identity contracts. Cached formula results
are compared as captured values; this is not a live Excel recalculation or policy
text comparison. An operator must re-read source metadata before calling the
result current; the acquisition's timestamp/version remains visible permanently.

On 16 October, native baseline parity passed for 985 × 25 data cells. The captured
observed version contained 984 records: 88 changed known records, two missing
identities and one unknown alias. The one existing case had no links to the known
differences. This is partial coverage, not assurance that no case is affected.
The report retains the last successful baseline and shows the reconciliation hold.
It performs no identity resolution or business assessment.

## Teams use and refresh

In the existing **Start Here** tab, use **Source-change comparison and affected
cases**. Download the frozen HTML report and open it locally, or download JSON
for detailed evidence. This is a dated snapshot, not a live dashboard. The tool
ZIP contains maintained scripts, mapping, instructions and fictional inputs;
extract it and run the command above. Tool download does not execute code in Teams.

For refresh, obtain fresh native exports and the retained raw acquisition with
matching source metadata. Re-run qualification into a new directory. Inspect
hold/partial states, then upload the new report with a unique versioned filename
and update the existing managed hub block. Retain earlier reports; do not replace
human work. `tools/source-comparison/deploy.js` supports guarded, repeat-safe
hosting/navigation: same bytes are adopted; conflicting bytes stop. Preserve
all unrelated hub controls and manifest entries. No new tab, post, access grant,
flow schedule or case update is required. Uploaded reports inherit existing
library access; private-channel membership does not redefine resource access.

## Committed retained absences — 17 October 2026

The authorised reconciliation has 985 active source records and 987 catalogue
identities. Two evidenced absences are retained unchanged. A comparison using this
baseline must supply its exact successful `--checkpoint` and complete
`--catalogue` item array. The acquisition adapter accepts these same inputs and
uses the checkpoint's committed identity ledger, including its acknowledgement
history; an older bootstrap ledger is not the active contract.

The validator accounts for every catalogue identity and rejects unknown,
duplicate, unacknowledged or stale absences, wrong contracts and incomplete native
retention readback. Current absence authority is bound to the exact source hash;
a later source version cannot inherit it silently. Returned known identities keep
their historical acknowledgement without treating it as new absence authority.
Boolean, fractional, textual and negative accounting counts are invalid.

The report lists retained identities separately with their original recorded
source fields and acknowledgement evidence. Absence does not establish clinical
retirement or current approval. Cases linked to retained identities remain
explicitly unresolved for human attention. Unknown or unqualified case links also
remain unresolved; zero changed active records does not resolve those cases.

The 17 October comparison reproduces all 24,625 active baseline cells: 985 active
records, two retained absences and 987 catalogue identities; no active source
field differences. The existing case has two qualified active links; no changed active records or
unresolved links were found in this metadata comparison. Coverage is complete
for the supplied catalogue and case inputs; clinical content remains unassessed. Fresh source metadata matched the preserved acquisition's
ETag, identity and byte length. This reuses exact retained bytes; it is not a new
byte acquisition or content review. The earlier 16 October report remains history.
