# Minimum workbench delivery — 15 October 2026

## Usable output

An existing Clinical Leadership workspace now contains PPG Catalogue, PPG Review
Queue and PPG Review Evidence. The two Lists and document library were created
and read back natively. Versioning is enabled. DocumentUID and CaseUID are required,
indexed and uniqueness-enforced. Access inherits the existing site: no permission,
membership, invitation, source-register or clinical publication change was made.
The site identity/account and scoped permissions were checked through the existing
authenticated Neo route; supported same-origin SharePoint REST operations handled
creation, field/schema reads, initial item writes and readback. M365 authentication
remains separate; no competing login or new application was introduced.

The catalogue contains all 985 main-sheet records from the frozen baseline, with
persistent DocumentUIDs and source-qualified current aliases. A separate immutable
raw envelope preserves every original column/value. Source summary fields and
local case decisions live in different Lists. This is logical ownership, not a
claim of field-level security. Visible views expose human-readable source facts
or role/outcome/next-action/status and clickable evidence links.

## Verification and observed normalization

All catalogue batches reconciled to expected values. Full unchanged read-only
replay matched 985 unique native items and persistent UIDs and made zero writes.
SharePoint stores blank Note strings as null: that observed storage normalization
is explicit in the source-summary codec; original raw blank/type values remain in
the retained envelope. No other value normalization was silently accepted.

The uploaded extracted baseline, identity ledger and date sidecars were SHA-256
qualified before import. SharePoint changed the uploaded XLSB copy's bytes during
ingestion. It is a working copy, not an immutable raw snapshot. An additional ZIP
containing the untouched downloaded XLSB was uploaded and its complete stored
bytes/SHA-256 matched locally; the catalogue links that ZIP as its retained source
baseline. The local raw download remains unchanged.

The review library also holds a Word rendering of the QW2 owner's source
qualification draft plus the selected-register evidence. Native draft text and
all table cells matched the local rendering; selected evidence bytes/hash matched.
The source Markdown was not modified by formatting. No redline or approved-text
comparison is asserted by rendering it in Word.

## Example workflow and technical completion

The existing IETP case demonstrates persistent identity, linked source records,
proposed role, outcome, next action, target date/status and draft/evidence navigation.
Fresh bounded native audit confirms catalogue 985 items, queue one retained case,
versioned library, required indexed unique identities, default views and workflow
fields. Earlier full baseline/replay proof is retained; no repeat import was needed.

The user's 15 October correction separates system setup from policy work. All four
QW1 system tasks are complete. Unassigned/proposed roles, unagreed dates and
unreviewed content are valid example states; they are not software blockers.
The existing case, source records, v0.5 package, draft 0.2 instruments, captured
sources and direction endorsement are retained unchanged. Actual source currency,
role/route decisions, business readiness, acceptance and approval remain unperformed.

QW2's reusable DRAFT template/offline population command has demonstrated editable
example output, refused overwrite on replay, input/source preservation and checks
that do not fabricate business acceptance. Local generation is distinct from the
retained native example renderer; generic unattended arbitrary-case deployment is
not claimed. QW2's technical workflow is complete under the corrected scope.

QW3's qualified acquisition/extraction/candidate/reconciliation and hourly metadata /
daily-or-change cadence remain active. See [extraction qualification](extraction-qualification.md)
for proof and observation limits. QW3 is the sole source-field writer; review
queue/draft/decision fields remain outside that ownership. QW4 remains postponed.

## Receipts and next action

Private deployment binding, ledger, creation/schema receipts, batch accounting,
full catalogue replay, case readback and package rendering/native verification
are retained under `.local/workbench/`. Frozen baseline artifacts remain under
`.local/baseline/2026-10-15/`; source data and tenant identities are not in Git.

The system is ready for later authorised use. No actual reviewer, agreed date,
policy judgement or readiness response is needed to finish this build. The native
[operator handoff](operator-reviewer-handoff.md) explains fields, evidence,
ownership and failure visibility; existing business next-action text is retained
as part of the example, not as a new assignment or active build request.

Supported API reference: [SharePoint list and item REST operations](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/working-with-lists-and-list-items-with-rest).


## Panel improvement integration

The user-requested advisory panel found and resolved case/package drift, broken
Word navigation, ambiguous role presentation, table pagination and a source-summary
blank/null codec defect. The same case and canonical draft were updated; source
facts and local decisions remain separate. See [panel synthesis](panel-review.md)
for changes, direct readback evidence and the distinction between technical proof
and unperformed business use.

## Revision direction endorsed; v0.5 integrated

The user endorsed targeted revisions and progression to responsible PMEO/PMEU
review. That exact narrow decision is retained in the evidence library. Candidate
v0.5 restores the existing respondent floor and strengthens contextual privacy,
restricted handling and immediate escalation; uses existing de-identified action
records; distinguishes committee and content-confirming endorsement, coordinator
preparation and executive approval; and exposes source effective-date conflicts.
Both draft 0.2 procedures, the direction decision and a separate change log were
uploaded and read back. Canonical Word version 5.0 matches source text, 24 ordered
hyperlinks and five repeating table headers. Conditional case update/readback
records the endorsed direction and v0.5 next action, preserving identities, role,
source links and the unagreed date. Responsible content readiness and policy
approval remain unconfirmed; no invitation or publication occurred.

## System-build scope correction

Earlier substantive example preparation and direction endorsement are preserved
as historical evidence. The setup now closes on native resources/identity/views,
source fidelity, editable templates/examples, navigation and sync/recovery proof.
Business policy review and approval are not undertaken or required for technical
completion. No case state, policy content, person/date assignment or source
register was changed by this scope correction.
