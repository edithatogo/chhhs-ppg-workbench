# Unattended extraction qualification

The source-only reconciliation kernel has passed native replay and failure
recovery. The remaining acquisition step must produce a newly accounted snapshot
when the central workbook changes; an old frozen candidate cannot stand in for
new source content.

## Preferred route

Use an Excel Online Business connection in the assigned environment. Download and
retain the central workbook as raw evidence, then run an Office Script against an
isolated working copy in the pilot library. The script reads the master worksheet
without requiring native Excel Tables and returns scalar values, the worksheet
inventory and formats for the four date columns. It contains no setters, macro
execution or link/data refresh calls. Connector operations may still save workbook
metadata, so the central register is never the Excel action target.

Compare a qualification result with the retained baseline: 15 worksheets, 25
headers, 985 data rows, every cell value, and all four date-column formats. Blank
cells may differ only as empty string versus null. Preserve raw scalar values and
month-only review-date precision. These counts qualify this dated baseline; future
snapshots must be accounted independently rather than forced to the old count.

Before cadence, test newly acquired content, repeat behaviour, source-change
metadata guards, row moves, local-edit survival, and failure without checkpoint
advance. Script execution and extraction parity alone do not close those gates.

## Native outcome — 15 October 2026

The connection and worksheet discovery succeeded on the isolated XLSB copy.
The minimal script envelope failed before cell access; explicit synchronous API
metadata corrected execution. Native extraction succeeded in about 11 seconds.
Direct result comparison matched every one of the 24,650 cells, the 25 headers,
985 data rows and all 15 worksheets. Date-format comparison found 1,925 literal
serialization changes, all covered by three reviewed equivalent pairs: escaped
hyphen/space versus literal separator in month/year formats, and two-digit versus
four-digit year notation in day formats. All scalar values and month-only next
review precision match. Unexpected format differences still fail qualification.

Fresh raw acquisition also passed: metadata before/after remained stable, the
original byte count and SHA-256 matched independent native readback, and a new
isolated copy reproduced the baseline extraction. The native candidate builder
then succeeded in about 24 seconds. Its raw hash, identity contract, all 985
projected facts/months and retained records artifact hash matched independent
readback. The parameter metadata needed indexed names; that packaging correction
resolved a native gateway error. The tracked builder is
[ppg_candidate_builder.ts](../scripts/ppg_candidate_builder.ts); script envelopes,
actual operational inputs and receipts stay private.

The builder reads displayed review months and checks their agreement with numeric
serials and qualified formats on every row. Unknown/version-changed aliases,
duplicate identities, missing identities, header drift and unqualified date
interpretation fail closed; it never mints or retires identities. Local checks
cover hash vectors/original bytes, Unicode, all 985 Python projections, artifact
hashing, row moves and those rejection paths. Native proof additionally covers the
actual displayed-month values and full acquisition/export.

## Integrated and activated outcome

The native forced-daily run acquired fresh bytes, verified all 985 catalogue rows,
made zero writes and committed the success checkpoint. Reusing the pinned last
successful candidate for identical raw bytes avoids provenance-only rewrites.
Cached candidates must match checkpoint ETag/identity; new retained candidates
must match the fresh builder output. Original byte count must match metadata.
Source/candidate versions are checked through final readback.

An intentional integrated failure after one same-facts conditional source write
and readback saved a failure receipt and left the prior checkpoint unchanged.
A genuine altered workbook fixture changed one title on an isolated copy; its raw
hash changed, the new native candidate preserved all 985 identities and month
values, and exact retained-candidate readback passed. The fixture performed no
catalogue write or checkpoint advance and did not alter the central workbook.

The assigned flow is now Started with hourly recurrence in Brisbane time and
single-run concurrency. Daily or changed-source reconciliation uses the qualified
acquisition path. All qualification flags are off. The first automatic hourly
invocation succeeded at 06:12 Brisbane time on 15 October: metadata only, zero
content fetches/writes and no checkpoint advance. Direct final native readback
confirmed state, recurrence, concurrency and flags. The daily route was manually
qualified; a full day of scheduled operation has not yet been observed.

A real central change was observed on 15 October: the 13:12 Brisbane scheduled run
detected the 13:10:53 source update and retained its raw acquisition. Local inspection
of the acquired original confirmed a genuinely populated appended row whose alias
is absent from the frozen ledger. The builder rejected it at the unknown-identity
guard before catalogue writes; the prior checkpoint and 985 imported rows remain
unchanged. This is an intended operational hold, not an extraction/parser defect.
No identity mapping or baseline/count extension has been commissioned. The flow
remains active; later reconciliation of the new identity is separate from system
setup. No new identity or source decision was manufactured to close technical work.

## Fallback inspection

An existing approved Python runtime could reuse the proven XLSB reader. A desktop
route would need an operational Windows/Excel machine, a usable desktop connection,
and unattended capacity. Read-only inspection found a prototype machine pool but
no desktop flows or desktop connections in the assigned environment. The current
Azure CLI account inventory showed tenant-level entries without ARM subscriptions.
Neither finding establishes tenant-wide absence; neither qualifies a fallback.

Detailed scripts, native bindings, snapshots, result comparisons and inventory
receipts remain private under `.local/`. No new runtime, paid capacity, permission
change or external data service has been created.
