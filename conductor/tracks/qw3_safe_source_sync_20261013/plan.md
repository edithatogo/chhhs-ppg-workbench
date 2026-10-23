# QW3 implementation plan — Refresh without losing local work

Execute this pre-authorised bounded scope under [the project workflow](../../workflow.md).
Read [the specification](./spec.md). Each task produces a useful result; no phase
approval ceremony or blanket coverage threshold.

## Deliver the quick win

- [x] 1. **Prove a bounded acquisition/extraction path.** Read source metadata/content, preserve raw snapshot and create working copy. Test only the necessary XLSB action. After two identical failures, use a supported existing fallback or record the blocker; do not start a new infrastructure project.

- [x] 2. **Implement persistent identity and protected updates.** Reuse DocumentUIDs/qualified aliases; retain all original fields and ordinal duplicate headings. Resolve unknown identity separately; source-only writes must not touch cases, local owners, decisions, drafts or deadlines.

- [x] 3. **Make completion and failure explicit.** Use one serial worker, complete counts and durable run receipts. Check source consistency around acquisition. Partial failure does not advance the last-successful checkpoint; missing rows remain exceptions.

- [x] 4. **Exercise the small critical scenarios.** Import twice; reorder/alter a test source; preserve a local case edit; simulate or safely reproduce one failed/partial run. Read back records and source unchanged status. No percentage coverage target.

- [x] 5. **Enable cadence and hand over only the proven scope.** After the preceding checks, enable hourly metadata polling and daily full reconciliation in Power Automate. Record exact live evidence privately, visible as-of/error state and support owner. No whole-document refetch on every poll.

## Completion record
15 October 2026: source-only local adapter prepared in `scripts/ppg_source_sync.py`.
Seventeen fictional regression checks pass: frozen hash/header/raw-value preservation, replay/reorder, changed source field, local
edit survival, duplicate/unknown/version-changed identity, namespace isolation,
partial failure/retry, missing rows, readback mismatch and serial worker lock.
Per-run plans/receipts are durable; last-successful checkpoint advances only after
all readbacks with no identity or missing-row exceptions. Missing rows never
cause delete/retirement. Cadence decisions are now tested: hourly unchanged metadata does not trigger
content acquisition; source version changes trigger reconciliation; daily
reconciliation is due from last success; failed runs remain due and missing
metadata prevents content work. Naive/future checkpoint times are rejected.
Native summary projection now follows QW1's loader types: raw date JSON text, qualified review month, source provenance and row reference, retaining typed raw values separately. Sidecar raw/date precision mismatch fails closed. No native binding, writes or schedule are claimed.

QW1 contract proposal: supply frozen main-records/raw snapshot pointers and hashes,
row count, ordinal header/date-sidecar receipt, persistent DocumentUID map with
source-qualified exact aliases, exact catalogue resource/field IDs and last
write/readback, plus assigned flow ID and support owner. Unknown/version-changed
aliases require QW1 reconciliation; never match title/row/ID# automatically.
All 25 raw values remain in the frozen source; date sidecars stay separate.
Conditional source-only patches require complete readback; target adapter has
no create/delete/case-write methods. Metadata polling must read metadata only;
daily reconciliation and on-change imports remain disabled until native proof.

Frozen local handoff consumed on 15 October: QW1's baseline contract declares
`snapshotFrozen` and explicitly withholds sync-writer transfer. Verified raw XLSB,
main-records, date-sidecar and identity-exception hashes against the owner's
receipt; all 25 ordinal fields and 985 rows validate. QW1 ledger resolves all
985 rows to persistent DocumentUIDs through exact qualified aliases, with no
unresolved/missing identity mappings. The source-only six-field candidate retains
all 25 raw fields plus source/ledger/handoff/date provenance privately in
`.local/source-sync/frozen-baseline-candidate.json`; validation receipt is alongside.
No baseline regeneration, macros, central-source changes or native writes occurred.
This is accounted local preparation, not native catalogue readback or a sync run.

QW1 initial-load receipt accounting independently checked locally: 20 contiguous
receipts cover all 985 rows, each reports exact readback; native IDs and persistent
DocumentUIDs are unique and the complete row/UID mapping matches the frozen ledger.
Hashed receipt-accounting evidence is in `.local/source-sync/initial-load-accounting.json`.
This verifies the received load receipts, not a fresh QW3 native read or writer transfer.
The private owner contract still explicitly withholds sync writes and has no flow ID.

Native writer gate superseded on 15 October: QW1 transferred flow creation/selection
and catalogue importer ownership after recording the sole flow ID. The new
contract's initial-load receipt hash and all twelve field/type guards validate.
Exact bindings are in ignored `.local/source-sync/native-binding.json`.
FlowAgent read the intended default environment and existing connected SharePoint
connection; no competing authentication or new connection was used. No existing
PPG flow was found. Created the sole QW3 flow stopped with a manual, serial,
read-only qualification definition. Controlled native run succeeded; recorded
catalogue ID/count and all field/type outputs match the handoff. Flow was stopped
again and its stopped state read back. Detailed native definition/run evidence:
`.local/source-sync/native-qualification-definition.json` and
`.local/source-sync/native-qualification-run.json`. No catalogue writes or
recurrence trigger exists. Native importer and scheduled extraction remain open.

Native frozen-baseline replay is now saved in the same assigned flow. The new
private candidate's uploaded bytes match its local SHA256; UniqueId/ETag are
pinned before/after acquisition. Native serial comparison checks all approved
source summary fields with blank/null and raw-decimal codecs, unique persistent
identities, complete counts and pagination guard. It has GET-only actions and
no catalogue writes or recurrence. The first native replay succeeded: 985 field comparisons, zero writes, unchanged
source candidate ETag; the flow was stopped and state read back. Retain its exact
handle in `.local/source-sync/native-replay-receipt.json`, do not restart it.
Definition is retained at `.local/source-sync/native-replay-definition.json`.
A first save failed due to a solution-style connection-reference logical name;
standalone Embedded refs fixed it, native save/readback then succeeded.

Excel GetTables operation details are available, but no Excel Online Business
connection exists in this environment. No new connection/authentication was
created; scheduled XLSB extraction remains unqualified.

Native source-only writer saved/read back in the same assigned flow: eleven
approved source/provenance fields only, conditional item ETag, post-write readback,
durable attempted-write/run receipts and a success-only checkpoint action.
One bounded same-facts source write succeeded and verified all intended fields.
The intentional partial-failure action is recorded; subsequent row writes are
skipped. Its run remains live while native Foreach drains skipped iterations;
no successful checkpoint exists or has been advanced. Flow is stopped to prevent
new manual runs. Detailed handle/definition are in
`.local/source-sync/native-write-failure-receipt.json` and
`.local/source-sync/native-write-failure-definition.json`.

Central source metadata read through Neo still matches the original frozen pin.
Prepared a validated serial Until variant that exits immediately on abort and
checks central source metadata before/after reconciliation; it is not deployed
while the current run remains live. Private candidate:
`.local/source-sync/native-writer-until-candidate.json`.

The native partial-failure run is terminal Failed: one attempted write, one
completed source-only write, one verified readback. Durable failure receipt read
back from SharePoint; successful-checkpoint action Skipped and checkpoint file
remains absent (404). The Until variant was then saved/read back in the same flow
with qualification flags off, central master metadata guards before/after and
success-only receipt/checkpoint writes. Its full native reconciliation is live;
central metadata read through the actual flow connection succeeded and matches
the frozen pin. Preserve the run at
`.local/source-sync/native-until-run-receipt.json`; do not restart it.

Full Until reconciliation succeeded: 985 readbacks, zero writes; complete native
receipt and checkpoint bytes independently read back and identical. A subsequent
nine-second abort test verified one conditional source-only write/readback and
durable failure, with the previous checkpoint byte-for-byte unchanged.

To remove per-row overhead on unchanged data, the same flow now compares complete
canonical source tuples in bulk and writes only differing rows serially. Blank/null
and raw-decimal codecs, UID/count/pagination/source-version guards remain. Native
bulk reconciliation succeeded in about six seconds: 985 readbacks, zero writes,
committed checkpoint. Its bounded partial-failure test failed as intended in about
ten seconds; durable receipt and skipped checkpoint verified. Normal flags restored;
flow stopped. Definition and proof:
`.local/source-sync/native-bulk-writer-qualified.json` and
`.local/source-sync/native-bulk-qualification-receipt.json`.
A native save nesting-limit rejection was corrected by removing the redundant
per-row If wrapper; no failed save was run.

Native cadence decision path saved and manually qualified on unchanged source:
source metadata + successful checkpoint read, state receipt persisted; candidate
content read and catalogue reconciliation skipped. Poll summary proves zero
content fetches, zero catalogue writes and no checkpoint advance. Evidence:
`.local/source-sync/native-cadence-manual-definition.json` and
`.local/source-sync/native-cadence-poll-receipt.json`. Flow remains stopped;
recurrence has not been enabled.

QW1's extraction-route handoff now confirms the existing route is operator-mediated
Neo acquisition and isolated local pyxlsb/calamine extraction. Script/receipt/
contract pointers and raw hash were verified without executing or editing the
owner's extraction. It explicitly records no qualified unattended runtime or
existing Excel Online Business connection. It does not reduce the QW3 objective
or authorise new connections, credentials, activation or runtime. A changed central
workbook must never be reconciled from the old frozen candidate.

**Exact next action / resource gate:** supply an authorised existing unattended
XLSB extraction connection/action/runtime in the assigned scope, then qualify a
new isolated snapshot and daily/on-change acquisition before enabling the full
requested hourly metadata/daily reconciliation cadence. No further independent
extraction qualification is available under the current handoff; do not reopen
writer-transfer/authentication discovery or replace this with frozen-only cadence.


15 October extraction-resource gate superseded by explicit user authorisation:
created a scoped Excel Online Business connection using the existing QH identity
with silent authentication. Native worksheet discovery and Office Script execution
against an isolated XLSB copy succeeded. Synchronous script packaging was required;
the minimal legacy envelope failed without any catalogue writes.

Native extraction matches all 985 baseline rows, 25 ordinal columns (24,650 cells
including headers) and 15-sheet inventory. Explicitly reviewed format normalisations
preserve month-only Next Review Date precision; no raw scalar differences.
Detailed native/comparison evidence is retained privately under .local/source-sync/.

Unattended acquisition also succeeded in the sole assigned flow: central metadata
before/after, raw binary acquisition, stable-version guard, byte-preserving base64
JSON envelope, independent isolated workbook and extraction result persistence.
Native file readback verifies the original byte count/hash and baseline parity.
No catalogue writes or recurrence were involved in these qualification definitions.

Next: integrate the freshly acquired raw provenance and identity-qualified candidate
into the existing source-only reconciler; qualify changed-source/recovery behaviour
before enabling the requested cadence. Baseline extraction and raw acquisition are
now proven; end-to-end scheduled synchronisation remains open.


## Usable QW3 delivery — 15 October 2026

The prior extraction/resource gate is closed. The sole assigned native flow now
runs with an hourly recurrence in Brisbane time and serial concurrency. Normal
qualification flags are off. Daily reconciliation is due 24 hours after the last
successful checkpoint; a changed central source version triggers fresh acquisition
on the next poll. Unchanged hourly polls do not refetch workbook content.

Native daily qualification acquired original bytes, retained a byte-preserving raw
envelope, made an isolated XLSB copy, computed SHA-256, resolved the existing
identity ledger, preserved month-only dates, persisted candidate/records and
verified all 985 catalogue records. It made zero catalogue writes on unchanged
facts and committed the durable checkpoint. Identical raw bytes reuse the pinned
last-successful candidate to avoid provenance-only rewrites. Cached candidate
ETag/UID must match the checkpoint; newly created candidate content must match
the fresh builder output. Raw byte length and source version are guarded.

Integrated partial failure qualification verified one conditional same-facts write
and readback, persisted failure, and did not advance the prior full-success
checkpoint. A genuine changed workbook fixture modified only an isolated copy:
new raw hash, new candidate, all persistent identities retained, exactly one
changed title cell, month precision preserved and exact native candidate readback.
It did not write fictional data to the catalogue or advance the production checkpoint.
The local scenarios retain duplicate/reorder/local-edit/missing-row/retry evidence;
the native writer continues to address only eleven approved source fields.

The first automatic hourly-trigger run succeeded at 06:12 Brisbane time on
15 October: metadata only, zero content fetches, zero writes and no checkpoint
advance. The daily path was manually qualified; this is not a claim of a full day
of observed scheduled operation or an actual central-source version-change event.
The existing flow owner retains support; no new person or responsibility transfer
was created. Exact bindings, run IDs, definitions and receipts remain private in
`.local/source-sync/native-scheduled-qualified-definition.json` and
`.local/source-sync/native-integrated-qualification-receipt.json`. Shared handoff
and registry integration is delivered to the QW1 owner.


## Current-state systems-build audit — 15 October 2026

Reopened the live definition and run history without changing the enabled flow.
Hourly Brisbane recurrence, concurrency one and all qualification flags off are
verified. Seven automatic metadata polls succeeded from 06:12 through 12:12.
The 13:12 poll detected a genuine central source version change, retained its
original bytes and isolated copy, then rejected one populated appended source
row whose document alias is absent from the qualified identity ledger. This is
the specified identity hold, not an extraction or connector fault. Zero catalogue
writes were attempted, durable failure was recorded and checkpoint commit skipped.
The previous complete 985-record checkpoint remains the last successful run.

The bounded systems build is complete; current refresh is held for QW1 identity
reconciliation. No identity was guessed, ledger extended, source modified or
scheduled guard weakened. The real changed-source event is now observed and
safely held before import. A full 24-hour scheduled daily cycle remains unobserved.
Current checks: 17 source-sync tests pass; 178 setup checks pass, zero fail, with
one pre-existing optional upstream checkout materialisation pending. Private audit:
`.local/source-sync/systems-build-audit-20261015.json`. Shared integration receives
this operational exception separately from technical build completion.

## Elapsed 24-hour read-only observation — 17 October 2026

Inspected the exact existing importer through the intended-account M365 CLI.
Window: 15 October 23:00 to 16 October 23:00 Brisbane (24 elapsed hours).
All 24 hourly buckets contain a normal run; longest gap63m09s reflects the
qualified deployment/reanchoring. All24 normal runs failed closed:15 old-extractor
unknown-alias refusals and9 newer guard-level identity holds. No ordinary run
attempted a catalogue write; every checkpoint commit skipped and every durable
failure receipt succeeded. All24 read the same last-good checkpoint, unchanged
in the current native read (14 October20:03:46 UTC,985readbacks).

Eight forced qualification runs are separate:3Succeeded/5Failed, with their
fixture writes accounted for. The18 extractor failures comprise15 ordinary typed
unknown-alias errors plus3 deliberate identity-precondition/new-identity tests;
no unrelated transport/parser fault was found. Native source ETags/raw-input hashes
and both extractor script IDs are correlated per run. Old row987 uses worksheet
ordinal including the header (data position986), never DocumentUID. Source versions
changed; later row912/986 exceptions are not assumed to identify that same row.
The latest candidate contains985rows,983resolved operations,2unknown aliases and
2missing UIDs. No identities were minted and no source/flow/schedule/auth changed.

Current flow is Started/hourly/concurrency1 with qualification flags false.
This closes elapsed-day observation, not successful daily reconciliation: the
identity hold still prevents a new accepted checkpoint. CLI trigger expansion
failed locally (undefined URI); ordinary paginated history and exact native action
reads succeeded. Proof/hash inventory: `.local/source-sync/observation-20261017/`.
