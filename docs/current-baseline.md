# Current source baseline — 15 October 2026

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

## Result and evidence

The current downloaded XLSB has been extracted from an isolated, byte-identical
working copy. The retained raw snapshot is unchanged. All 15 sheets have private
JSON exports of populated scalar/cached values, with original row/column positions.
Original formulas, styles, links and macros remain preserved in the XLSB; they
were not executed or recalculated. This is local baseline extraction, not a native
scheduled Excel/Power Automate extraction or deployed catalogue.

The main-sheet header and 19,403 populated cell values were cross-checked using
pyxlsb 1.0.10 and python-calamine 0.8.3: zero discrepancies. Binary workbook
properties and cell number formats were also checked. Parsers ran in an isolated
uv environment; no global plugin or hosted runtime was introduced.

## Sheets and counting boundary

| Sheet | Populated rows, including any headers |
|---|---:|
| STANDARDS TRACKING (hidden) | 111 |
| OVERDUE BY STANDARD (hidden) | 83 |
| REPORT INSTRUCTIONS | 15 |
| DUE & OVERDUE REPORT | 276 |
| Master Document Register | 986 |
| Links (hidden) | 68 |
| Rescinded links | 12 |
| Rescinded master | 1,037 |
| STATS (trailing space in source name) | 14 |
| Activity Report | 22 |
| Policy Registration | 95 |
| Procedure Registration | 1,589 |
| Drug Infusion Registration | 118 |
| Sheet2 | 170 |
| Sheet1 | 366 |

Only **Master Document Register** is the initial catalogue source: **985 populated
data rows plus one header, 25 columns, A1:Y986**. Every data row has a title and
Document ID. Registration, rescinded, reporting and ancillary sheets are retained
but not added to the active catalogue count. Populated-row counts are not counts
of unique documents or current policies. Formatting extends beyond populated
cells on several ancillary sheets; used-range dimensions must not drive imports.

## Headers

All 25 headers match `config/source-field-map.csv` exactly, including whitespace,
line breaks and both Audit Approach columns. The existing ordinal mappings remain
valid. Preserve each Audit Approach column separately. Do not collapse headings
or silently infer a new schema from cleaned display labels.

## Identity findings

| Candidate | Missing rows | Duplicate groups | Rows in duplicate groups |
|---|---:|---:|---:|
| Document ID | 0 | 0 | 0 |
| ID# | 2 | 40 | 86 |
| Title | 0 | 4 | 8 |
| Asset # | 972 | 0 | 0 |
| Document Type + ID# | 2 | 21 | 44 |

Document IDs remain unique after trimming and case-folding. Title duplicate counts
also persist after those transformations. No two complete 25-field rows are exact
duplicates. Repeated IDs/titles are reconciliation candidates, not evidence that
records may be deleted or merged. Document ID is a current snapshot alias; its
version-bearing nature still prevents assuming it is permanent identity. Use a
persistent DocumentUID with source-qualified aliases for future updates; do not
use row position, ID# or title alone as an upsert key.

## Date handling

Workbook properties specify the **1900 date system**. Raw numeric serials and
text are retained. Applicable cell formats, not numeric appearance alone, drive
date qualification. Stored calendar dates are separate from their display precision;
source calendar dates are not converted to UTC timestamps.

| Field | Findings |
|---|---|
| First Ever Date | 963 month-formatted dates, 16 text values, 6 blanks |
| Last Reviewed | 143 month dates, 4 day dates, 7 day/month displays without a displayed year, 657 text values, 1 unqualified numeric year candidate, 173 blanks |
| Next Review Date | All 985 values are month-formatted dates |
| Published | 101 month-formatted dates, 884 blanks |

Month-formatted dates have `YYYY-MM` sidecars; the underlying stored day does not
become an exact clinical deadline. The seven year-omitting date displays and text/
review-history entries retain their ambiguity. The numeric year candidate is not
converted into an Excel serial date. No blank, partial date or mixed history is
coerced into a guessed day/month/year.

Two First Ever Date entries and one Published entry contain stored dates after the
assessment date. These are visible source-quality exceptions for later review,
not automatic corrections. Future next-review months are expected candidates,
not evidence of an anomaly by themselves. No overdue-day calculation is asserted.

Date decoding references: Microsoft [BrtWbProp](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-xlsb/4d7ffab6-6ba7-4825-94f8-a5eb3fedbd22)
and [BrtXF](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-xlsb/879a823e-0a0e-42c3-a977-dc64cbb3d909).

## Preservation and next action

The workbook contains VBA and two external-workbook link parts, with no native
Table parts. No macros ran, no links refreshed, no source writes occurred.

Private artifacts are in `.local/baseline/2026-10-15/`: working copy, all-sheet
exports, main-records, date sidecars, identity exception rows, summary and hashed
receipt. The raw download and its metadata receipt remain in
`.local/snapshots/2026-10-15/`. Neither folder is tracked in Git.

The baseline remains the dated extraction finding. Destination qualification and
initial catalogue/case provisioning have since completed; see
[the current delivery record](workbench-delivery.md) and
[active handoff](../conductor/handoff.md). Current review/source-sync conditions
belong to those records, rather than this earlier extraction checkpoint.
