# Source ingestion — bounded constraints for QW1/QW3

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The attached XLSB snapshot was inspected in earlier work, not live in this setup.
It had 985 main-sheet rows, 25 columns, 15 worksheets, no native Tables, a VBA
project and two external-workbook link parts. Counts/ranges are snapshot facts,
not permanent validation constants. The main sheet is `Master Document Register`.
Preserve both `Audit Approach` columns by ordinal; preserve ambiguous dates and
review-history text before any normalization. `config/source-field-map.csv`
retains all 25 original headings and mappings from v0.4.

1. Acquire original bytes using permitted SharePoint metadata/content reads.
2. Retain the snapshot and process a separate working copy; do not execute VBA or
   refresh external links. Qualify XLSB actions against that copy only. Run script
   availability/support is an open operation check, not an implemented feature.
3. Use the existing permitted fallback if needed. Renaming XLSB to XLSX is not
   conversion. Do not create a new service to solve an unproven connector problem.
4. Preserve persistent IDs and qualified aliases. Source row order, shared `ID#`
   and a title similarity score are not identity. Changed version-bearing aliases
   are reconciliation candidates, not automatic merges.
5. Update imported facts only. Local case owners, deadlines, drafts, feedback,
   decisions and notes remain team-owned. Material upstream changes create a
   reconciliation task against the case's pinned baseline.
6. Missing rows are exceptions, not retirement. Keep histories/numbering/report
   sheets out of active counts; preserve their raw source for later work.
7. Use one serial worker; account for every row, read back intended results, and
   commit a successful checkpoint only after completion. Partial writes remain
   visibly partial and do not claim to be an unchanged last-good live List.

Initial manual import and repeat/local-edit tests precede scheduling. The requested
cadence is hourly metadata checks, imports on change, and daily full reconciliation.
Do not create an unrelated reminder in ChatGPT; this cadence belongs to the future
Power Automate flow. QW2 remains independent of this schedule.

Detailed action-level designs are in the user's v0.4 source package. Reuse those
only for this track; they do not make the earlier 5-List layout mandatory for QW1.
