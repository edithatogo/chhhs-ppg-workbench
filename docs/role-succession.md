# Role responsibilities and succession

Current route: operators use the [web role-refresh guide](role-web-operator-guide.md)
and native responsibility/exception views. No desktop Office or operator terminal
is required. Versioned inputs, accepted manual handovers, dated web refresh,
duplicate-free retry and copied-record recovery are technically qualified. Real
appointments, authority confirmation and ordinary-user adoption remain unperformed.

The dated sections below retain their original evidence and earlier limitations.
Local CLI commands are developer diagnostics/recovery preparation, superseded as
the operator refresh route by the web guide. Native cross-record form enforcement,
automatic transfer service and full runtime restore/cutover remain unqualified;
the manual/web pilot does not promise them.

New integration-owned Lists separate stable organisational roles, responsibility
assignments, effective-dated appointments and responsibility handovers. All have
version history and unique record keys. The schema is
[role-registers.json](../config/role-registers.json). These are local records;
upstream custodian, executive and authorising-officer assertions stay unchanged.

A role can be held by a person, group or committee. Responsibilities include all14
categories in the versioned role contract. A new holder requires a new appointment
with an effective start. Record the previous appointment's exclusive end date;
never replace its holder identity. Acting holders receive no implicit precedence.
Overlapping appointments produce an ambiguity. Role records grant no permissions
or clinical authority.

A succession handover keeps the same role and identifies old/new appointments.
A portfolio transfer identifies different roles and its document scope. Record
acceptance actor, time and evidence. The handover list is an evidence register;
it does not automatically change assignments or apply transfers. The local projection validates role/appointment references, succession dates,
explicit scope and acceptance evidence; native form enforcement and transactional
application of accepted portfolio transfers remain open work.

## Dated responsibility output

Export the three native role/assignment/appointment lists completely into a private
JSON object with `roles`, `assignments`, `appointments` and `handovers` REST response envelopes.
Retain available historical decisions separately under `historicalDecisions`.
Continuation links are refused so a partial export cannot resolve ownership.

```sh
.venv/bin/python -m scripts.ppg_role_projection \
  --input .local/review-intelligence/roles-export.json \
  --as-of 2026-10-18 \
  --output .local/review-intelligence/responsibilities-20261018.json
```

Use a new output filename for every run. This local read-only projection resolves
accepted appointments/assignments with evidence, retains historical decisions
unchanged, and shows vacancies, unconfirmed assignments and overlaps. Multiple
responsibility assignments are shown with concurrent IDs; they are not silently
reduced to one owner. Delegation must identify authority evidence and structured
scope (`documentUIDs` and `responsibilityTypes` arrays); unmatched/unstructured
scope cannot resolve a holder for that responsibility.

Native forms enforce calendar format/validity on five date columns; they do not
enforce all cross-record, interval-ordering or authority rules. The Lists' Responsibility records views show the input
records; the dated joined output is currently a manual export/projection. Do not
call these views a live automatic responsibility dashboard. No real people or
policy responsibilities are assigned by the fictional qualification fixture.

## Recovery and pending acceptance

Exact list/field/view bindings and native receipts stay private. Before retrying
an interrupted write, inspect the original job and query the stable key. The
create-only seed helper compares existing values and refuses differences rather
than overwriting edits. Provisioning refuses schema drift; no permission edits
or repairs are implicit. Export records and available version history before a
correction; retain earlier appointments and decision actors. A full copied native
recovery, real-role reconciliation, handover enforcement, joined native view and
ordinary-user acceptance remain to be qualified. SharePoint Lists are separate
ALM artefacts and are not automatically packaged in a Power Platform solution.

## Qualification observed on 18 October 2026

Four versioned lists/33 fields/four views and five fictional records were read
back. After a timed-out create, enumeration proved the first appointment existed;
retry preserved three existing keys and created the two missing records. Complete
native export contains one role, one assignment, two appointments and one handover.
Dated projection resolves fictional-one on31May and fictional-two on1June while
retaining the role identity. The native appointment view renders both rows.
Historical decision preservation is tested locally; no native clinical decision
was invented. Detailed receipts remain in `.local/review-intelligence/20261018/`.

## Stored dated responsibility output — 19 October 2026

**PPG Responsibility Snapshots** now stores derived joins, with **Dated
responsibilities** and **Responsibility exceptions** views. This is an on-demand
snapshot fallback, not a live automatic owner service. Select one run and inspect
its as-of date/source hash; multiple snapshots are not simultaneous assignments.
The run's manifest records source-export, implementation and role-contract hashes.
Original assignments, appointments and accepted handovers remain authoritative.

```sh
.venv/bin/python -m scripts.ppg_responsibility_snapshots \
  --input .local/review-intelligence/roles-export.json \
  --as-of 2026-10-19 \
  --output .local/review-intelligence/responsibility-snapshot-run.json
```

Use an explicit YYYY-MM-DD date, a complete four-register export and a new output
path. The CLI prepares payloads; it does not assign people or write to SharePoint.
A new source/date/implementation produces another run; exact replay uses the same
keys. Qualified native insertion compares every existing value and refuses drift
rather than replacing human edits. The projection retains unresolved appointments,
concurrent assignments, authority/scope exceptions and historical decisions.
Role resolution grants neither SharePoint access nor clinical authority.

Three labelled fictional native snapshots demonstrate the holder changing across
a succession date while retaining the same role and assignment. Exact readback and
zero-create replay pass. Both views' filters/fields read back. Complete source
exports before/after compare unchanged, including previous appointments, handover
actors and evidence. This verifies technical succession projection, not real
appointments or operational acceptance. Native rows all resolve; overlap and
unconfirmed cases are additionally tested locally.

Retain the raw source export, run manifests/full output, source-code revisions,
keys, field bindings and native receipts privately. A companion stores the source
export and demonstrations; verify downloaded file hashes separately. Recover into
a separate target and compare source/history and exact snapshot keys before any
binding change. Copied restoration, automatic refresh, real-role reconciliation,
portfolio-transfer application and ordinary-user adoption remain open. This new
List is a separate SharePoint ALM artefact, not a Power Platform solution component.

## Existing library-property adoption

The stored multi-date snapshot bundle reuses three existing evidence-library
properties: Title identifies its dated-bundle purpose, Description retains each
as-of date/source-export hash/projection identity, and Capture SHA-256 identifies
the actual stored artifact bytes. `scripts/ppg_projection_library_metadata.py`
builds these values from the existing run manifests; no selection or ownership
calculation moves into document metadata. No field or register is added for this
adoption, and policy review-date fields are not repurposed as projection dates.

Actual field types/internal names and REST entity-property names were read back.
The Description field requires explicit selection and returns HTML entities;
read/compare its decoded JSON once, keeping other property comparisons exact.
An omitted description is an incomplete read, not evidence that it needs another
write. The first save was reconciled through explicit read and native versions
before retrying. Original property values are retained from the preimage and
version1.0; no history or human content was replaced.

All three properties match. Exact replay performs zero writes, with the file's
identity, body hash and version unchanged on replay. Updates use only changed
values and the exact item ETag, preventing repeat-trigger loops; no flow or
notification is added. Preserve raw encoded and decoded evidence plus preimage
before correction. This is JSON artifact metadata qualification, not Word-body
refresh, live ownership, publication authority or copied-restoration proof.
As-of filtering remains available through the dated native snapshot List; the
library Description is a multi-run provenance note, not a new typed date column.

## Canonical date enforcement

The local role resolver/projection now enforces the documented Gregorian
`YYYY-MM-DD` convention for as-of, assignment, appointment and handover dates.
Compact dates, week dates, timestamps, impossible calendar dates and non-string
values are refused. Only a null/missing or empty end date represents an open
interval; false/zero cannot silently become an open appointment. Acceptance
timestamps remain a separate timezone-bearing field.

The earlier parser accepted compact/week-date representations. Eighteen focused
checks now cover malformed dates, valid leap days, exclusive end boundaries and
history preservation. Fresh CLI exports of all four native registers match the
previous five-record fixture; projections at three valid dates are unchanged.
The malformed-date CLI check refuses before creating output. These checks make
no native edits and do not add native form validation or qualify transfer
application. Existing snapshots retain their original keys, code hashes and
versions. Future runs bind the revised implementation; recover an older run
using its recorded code revision rather than repinning it to current code.

## Manual portfolio transfer and read-only audit

A portfolio move creates a separate destination assignment; it does not change
an organisational role's holder or rewrite the source assignment/actor. Use an
exclusive source end date equal to the destination start date, with an explicit
accepted handover recording documents, roles, actor/time and evidence. Preserve
the source assignment's acceptance evidence and earlier versions. Proposed or
partially recorded transfers are not completed transfers.

Export all four registers completely and provide explicit assignment pairs:

```json
[{"fromAssignmentId":"fictional-source","toAssignmentId":"fictional-destination"}]
```

```sh
.venv/bin/python -m scripts.ppg_portfolio_transfer \
  --input .local/review-intelligence/roles-export.json \
  --handover FICTIONAL_HANDOVER_KEY \
  --pairs .local/review-intelligence/transfer-pairs.json \
  --output .local/review-intelligence/new-transfer-audit.json
```

This CLI audits already recorded manual changes; it never applies assignments,
grants access or verifies clinical authority. It requires accepted/evidenced
source and destination assignments, matching documents/responsibilities, exact
date boundaries, complete scoped source accounting and no overlapping destination
or conflicting accepted transfer. It binds source/pair/code hashes, preserves
historical decisions and refuses an existing output file.

A native fictional qualification creates seven labelled input records, initially
with a Proposed handover/destination and open source assignment. The proposed
export is refused. Three exact-ETag changes close the source interval and record
destination/handover acceptance; original1.0 and final2.0 versions remain. Fresh
exports pass the audit, and two stored snapshots show the role/holder on either
side of the date. Twenty-three focused tests pass. All five earlier input records,
three previous snapshots and both views are unchanged. Application replay writes
zero; initial-seed and snapshot replays create zero. No real role is assigned.

The native stale update returns412. Its record fields, GUID, URI, ETag and version
remain unchanged. An initial overly strict observation failed because verbose
`__metadata.id` varied; both the original observation and explicit qualification
refinement are preserved. Do not discard native GUID, item IDs or version pins
when comparing responses. The mutation probe was not repeated to fix observation.

This is a manual multi-record sequence, without atomic commit or automatic
rollback. If interrupted, inspect stable keys, actual fields/history and ETags;
resume only missing confirmed steps. Retain preimages and do not re-seed initial
states over completed work or overwrite changed human records. Refresh dated
snapshots after successful reconciliation. Native form enforcement and ordinary-
user execution remain separate from the API/CLI fixture proof.

The versioned evidence supplement retains five files and the source/history
archive. Restore into separate targets and verify member hashes; copied native
restoration remains open. Update the broader workflow-guide successor for this
manual audit step without changing frozen releases. This is not a new Power
Platform solution component, scheduled writer or clinical approval route.

Workflow documentation follow-up: published release1.3.0 now includes a separate
manual portfolio-transfer workflow and diagram, preserving earlier frozen guides.
The pending successor noted at the qualification checkpoint above is delivered.
Automatic transfer service, copied native recovery and real-role/adoption work
remain open; publication of instructions does not apply an assignment.

Copied-recovery follow-up, 20 October: the [recovery runbook](role-register-recovery.md)
now has native fictional proof: five separate Lists/45 fields,17 records/20
business versions and11 views. Record and view/settings replays write zero; five
dated projections and the manual-transfer audit match. Original five-register
exports compare exactly unchanged, including IDs/history/views. Five stored
snapshot manifests are preserved rather than repinned. The downloaded native
backup and19-member evidence archive pass hashes/CRC. New platform audit identities
remain distinct from archived original provenance. This closes copied recovery
for the fixture only; real-role population, native form enforcement, automatic
service, production cutover and later adoption remain separate. Frozen workflow
release1.3.0 stays unchanged.


The retained catalogue role-label inventory is complete for985 records; see
[source assertions](source-role-inventory.md). This does not populate real
appointments or convert source assertions into accepted assignments.


Working calendar-column scope, refusal proof and recovery:
[working role date validation](working-role-date-validation.md).


## Overlap diagnostics —20October correction

An ambiguous appointment set has no selected holder or delegation scope. The local
projection retains all candidate IDs and does not replace the ambiguity diagnostic
with the first candidate's scope exception. Scope is selected only for a single
returned appointment; its applicability still needs checking. This restores the
existing no-arbitrary-selection contract, without changing native role records,
stored snapshots, historical actors or workflow transitions.

Both input orders of a synthetic scoped-delegation overlap now return ambiguous,
no holder and no scope. The ordinary projection of12 freshly exported native
qualification records is unchanged. No synthetic appointment was saved natively.
19 focused tests pass. Six native evidence files/replay0 and downloaded13-member
CRC/all-hash archive reproduce the corrected CLI outputs, unchanged baseline and
previous order-dependent regression using archived code. Prior code is retained for
regression evidence only. Recover into a separate location and use new output paths;
never overwrite or repin earlier dated snapshots. Private role-overlap-scope-v1
contains operational proof; the same-named native companion retains the guide.


## Confirmed vacancy versus missing appointment evidence

No matching appointment means **unconfirmed**, not a vacancy. An accepted substantive
or acting appointment without a named holder also remains unconfirmed. Only an
explicit `vacant` appointment with accepted status and evidence resolves as vacant;
a vacancy cannot name a holder. Proposed or unevidenced vacancy records remain
unconfirmed. No responsibility or access is assigned by these diagnostic states.

The correction preserves the ordinary projection of12 native qualification inputs.
Five synthetic CLI scenarios and21 focused tests pass; synthetic records were not
saved to the native role Lists. Four evidence files read back with inherited access
and replay0. The downloaded20-member archive passes CRC/all hashes; isolated CLI
replay reproduces all five outputs and unchanged baseline. Original source inputs,
handovers and historical actors remain preserved. Native snapshots are not repinned.

Recovery uses the same-named private/native `role-vacancy-evidence-v1` companion:
validate `source-inputs.zip`, extract separately and run the archived CLI against
saved inputs to new output paths. The prior helper is regression evidence only.
Frozen workflow1.5.1 already requires unknowns to remain unresolved and is preserved.
Real-role reconciliation and ordinary-user adoption remain separate open work.
