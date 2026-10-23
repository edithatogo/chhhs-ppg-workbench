# Web role refresh qualification — in progress

The operator route is a manually launched Power Automate cloud flow. It must not
require an operator CLI, local Python or desktop Office. Existing manual register
maintenance and stored snapshots remain the supported fallback while this route
is qualified. This does not change appointments, clinical authority or access.

## Current evidence

The integration-owned candidate reads all four role registers, projects an explicit
as-of date through a separate SharePoint-hosted Office Script/runtime workbook,
and rechecks source stability before reporting. It contains no register writers,
schedule, notification action or snapshot writers. Existing Embedded Standard
SharePoint and Excel connections were reused without new consent.

The TypeScript projection matches the Python reference across positive/negative
fixtures and three dated exports of the twelve native input records. Fifteen
focused tests pass. Native script/workbook bytes, inherited access and replay
were verified separately. These are preparation and storage evidence, not proof
of successful native execution.

The first browser-launched run reached all four successful register reads and
request composition. It then failed at `RunScriptProdV2` with
`ResponseSwaggerSchemaValidationFailure`: connector response `body` expected a
String but received an Object. No successful projection, source recheck or report
is claimed. Management-trigger launch previously returned a schema mismatch and
created no run; the web form successfully launched exactly one reconciled run.
Detailed bindings and run/action evidence remain private under the dated
`role-web-refresh-v1` qualification directory.

## Next actions and recovery

1. Qualify the actual hosted-script return schema and connector output shape;
   preserve this failed run and first script revision. Do not weaken date input or
   infer successful Office Script execution from a saved definition.
2. Verify output against the same dated source export and Python projection.
3. Add guarded derived snapshot persistence only after core parity succeeds.
   Exact replay must create zero snapshots; changed sources or edited outputs must
   hold rather than overwrite. Preserve original registers and previous runs.
4. Publish operator navigation and a successor workflow release only when the
   usable route and recovery are qualified. Frozen workflow releases remain intact.

The created flow is manual-only and currently On for qualification; it has no
scheduled trigger. To suspend this candidate, stop only this owned flow after
checking its run state. Preserve its runtime assets and evidence; do not delete
existing snapshots or modify shared connections. Native default failure-alert
subscription was observed and was not changed; absence of a notification action
is not a claim that platform failure alerts are disabled.

Current procedure/template verification and ordinary-user adoption remain open,
separate from this technical qualification. No desktop Word check is required.

## Response and runtime correction

The second immutable script revision corrects the connector envelope to an object
with a string `result` and log array. Native run two succeeded, including source
rechecks, but actual output comparison found zero responsibilities where the
Python reference produced two. It is explicitly rejected as qualification proof.
The complete returned source JSON matched the actual input; no source was lost.

The projection used `Map.values()` loops. Native execution silently skipped those
loops despite local Node parity. Direct iteration over the already validated
source arrays replaces iterator loops, retaining duplicate/reference checks and
all original records. This is packaged as a third immutable script revision;
earlier revisions and both run records remain preserved. No derived persistence
is enabled until actual output equality passes.

Third native run completed successfully with the corrected array loops. Actual
report output contains two responsibilities and equals the Python projection of
its twelve native input records at the same as-of date. The complete source JSON
and its SHA-256 match; all four source rechecks succeeded. This qualifies the
read-only projection for that retained fixture, not saved snapshots, all possible
inputs or ordinary-user access. Fifteen focused tests pass. Private evidence:
`native-v3-parity.json`, the third run pointer/actions and three downloaded action
outputs. No persistence or business-state change occurred.

## Guarded persistence candidate

The existing derived List has native versioning plus a unique indexed SnapshotKey.
The candidate first checks all projected keys: absent rows are eligible and
existing rows must match every owned field exactly. It then creates missing rows
only, with automatic connector retries disabled on creates, and reads each saved
row back. It has no update/delete action. Serial loop and trigger concurrency,
together with the native unique constraint, limit duplicate creation; native
failures must be reconciled rather than relaunched blindly.

All four sources are checked before and after persistence. Completion is reported
only after exact saved-row and final source checks. The report supplies RunKey and
expected count. Failed or interrupted runs may leave partial rows: these are
retained and must not be treated as a completed snapshot. Source and human edits
are never repaired automatically. Replay can reuse only exact rows; a conflict
requires operator investigation and preservation of the original evidence.

First native persistence run succeeds: two rows match all thirteen owned fields;
five earlier snapshots remain byte-for-byte equal in the complete item export.
Actual report still matches Python. An identical browser-launched replay succeeds,
skips creation and returns the identical completed report. CLI exports show all
seven items, including native versions, unchanged. Sixteen focused tests and flow
validation pass. Private receipts: persistence-first-proof, persistence-replay-proof,
full before/after exports and both exact native run pointers/action outputs.

This proves first/repeat behaviour for the retained fixture. Deliberately edited
snapshot and mid-run changed-source refusal remain unverified natively. Operator
navigation, completed-run selection, a workflow-guide successor and ordinary-user
access are not promoted by this evidence. Preserve partial rows after failure;
reconcile the exact run before retry, and do not overwrite a conflicting row.

## Native refusal qualification

A labelled fictional conflicting row was appended only to the existing isolated
recovery snapshot List. Its key matches the expected projection while its Title
contains deliberately different operator wording. The candidate was temporarily
bound to that copy after exact quiescent-definition checks. Native preflight
refused the row, persistence and completion were skipped, and all six isolated
rows/versions remained unchanged. The intentional failing assertion is visible
under `Snapshot_conflict_Preflight_snapshots`; its current engine error is an
InvalidTemplate/divide-by-zero assertion, not a transport failure. Operator-facing
conflict diagnostics still need improvement before broader adoption.

A second controlled test directed only the role recheck read to the existing
isolated role copy. Native run ended with `RoleSourceChanged`; no persistence or
completion occurred. This tests a deliberately mismatched read, not a timed
concurrent source edit. No role input was modified to produce the condition.

Both temporary definitions are retained privately. The exact working definition,
connections and original snapshot target were restored and read back. All seven
working snapshots and all six isolated rows retain their full values/versions.
The extra isolated row remains labelled test evidence; it is not a real role
assignment or completed run. No working snapshot was edited or deleted.
Private proof: conflict-preservation-proof, refusal-final-proof, per-iteration
refusal receipts, both native run handles and conditional binding receipts.

Operator navigation, clearer conflict reporting, final post-persistence mismatch
qualification, workflow successor and evidence publication remain open. Existing
first/replay evidence is preserved; no wider ordinary-user acceptance is claimed.

## Explicit holds and published operator route

The current candidate replaces deliberate expression failures with monotonic
conflict flags in serial loops and explicit Terminate actions outside them.
Native conflict qualification now returns `RoleSnapshotConflict` with a clear
preserve-and-investigate message, skips persistence/completion and preserves the
isolated fixture. Missing/cardinality checks precede first-row evaluation. Later
exact rows cannot reset an earlier conflict. Saved-row conflicts and post-save
source mismatch have distinct codes; their deliberate native negative paths still
need separate qualification.

The original working target/connections are restored with this revised definition.
A normal native repeat succeeds, skips creates and returns the identical completed
report. All seven working and six isolated rows/versions remain unchanged. Sixteen
focused tests plus flow validation pass. Read order is canonical rather than
inherited from binding dictionary order, keeping variable initialisation before
all source rechecks.

A separate SharePoint operator page1.0.0 links the flow and existing Dated
responsibilities/Responsibility exceptions views. It explains exact-run observation,
report state, RunKey/count filtering, holds, partial rows, retry and fixture limits.
Native published readback verifies all content/three targets; replay makes zero
changes and previous guides/maintained Word remain unchanged. Browser visual
inspection confirms current-account rendering. A draft comparison initially found
space versus percent-encoded view URLs; expected targets were normalised after
read-only inspection, without overwriting the existing draft. Broader access is
unverified. Sanitised instructions: role-web-operator-guide.md; private page proof:
20261021/role-web-guide-v1.

The full frozen workflow-register/diagram successor and archived evidence delivery
remain pending. The new guide is an incremental operator route, not a claim that
those deliverables or ordinary-user adoption are complete.

Runtime recovery evidence delivered21October: five exact native files/replay0 and
a downloaded70-member archive reconstruct archived Python/Node parity, source/hash,
script/contract pins, first/repeat snapshots and refusal preservation in isolation.
264 signed action-link fields removed from summaries; private bindings/records stay
out of Git. A loose-workbook upload changed custom XML/deleted-part metadata, so
that failed attempt is preserved and exact workbook bytes are delivered inside ZIP.
No working runtime or input changed. This closes offline evidence delivery, not
native runtime restoration, cutover or managed solution packaging. See
role-web-runtime-recovery.md; private role-web-recovery-v1/archive-storage-proof.

21 October quiet-preference correction: exact native flow comparison changes only
flowFailureAlertSubscribed true→false; definition/connections/Started/nine runs
unchanged. CLI read checks plus native Repair tips off/confirmation used; installed
CLI has no flow-set command. No run/source/global setting changed. Separate native
receipt/recovery preserves the then-current default and correction; weekly platform
digest/past email suppression is not claimed. See role-flow-alert-preference.md.

## 21 October fresh role runtime revalidation

After a separate standards-host lookup returned404, the role workflow was tested
rather than presumed broken. The installed M365 CLI completed-run resubmit operation
was used once against the last successful fictional qualification. Current native
definition and existing connections matched the qualified version, the flow remained
Started with failure alerts off, and the new run completed successfully. The report
returned two completed dated responsibilities; Create_snapshot was skipped. All12
input records and seven snapshots retained their values and version markers. Only
per-response UUID metadata `odata.id` differed and was excluded after explicit
inspection; no business field, item ID or ETag was excluded.

This verifies the current role runtime at the retained fictional as-of date through
actual script execution, source rechecks and duplicate-free persistence. It does
not prove direct workbook download availability, native restoration, real-holder
acceptance or ordinary-user access. No runtime repair was needed or performed.
Exact run/transport/action outputs and before/after preservation proof are private
under20261021/role-runtime-revalidation-v1. No signed links or tenant bindings enter
Git. The operator route remains the published web guide; developer CLI resubmission
is qualification evidence, not an operator terminal requirement.
