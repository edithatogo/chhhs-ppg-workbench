# Consultation and ownership handoff

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Use the **PPG Consultation and Handoff Events** List to record human responses and
ownership assertions against an existing Review Queue **CaseUID**. This recording
path does not send requests, notify anyone, assign a role or transfer responsibility.
Use the case's existing route and evidence; do not change the case merely because
an event was entered. Actual authority, role acceptance and capacity remain human.

## Establish the version and role

Copy the CaseUID, stable DocumentReference, exact ReviewedVersionRef and SHA-256
of those exact document bytes. A latest-document link alone is not version proof.
SubjectRole identifies the respondent or proposed receiving role. FromRole is the
offering role for ownership handoffs. Use role labels and actual actor evidence;
Created By identifies the record entrant, not necessarily the respondent.

Give every event a unique EventUID. Generate a new event identifier for a new
assertion; retain the same identifier when reopening/correcting that record. Keep
supporting material in the existing evidence library with its native version/link.
There is no new document-generation requirement: this workflow records structured
events and references existing evidence. If producing a maintained consultation
report later, assess the preferred SharePoint structured Word route first.

## Consultation

1. Add EventKind **Consultation**, RecordState **Pending response** (or **Unknown**
   when even request status is unknown). Record the role, version, next action and
   evidence of any request already made outside this system. Entry sends nothing.
2. When an actual response arrives, add a new event for the same exact scope and
   role. Link the pending event's EventUID in ParentEventUID. Set **Responded**,
   **Declined** or **Not required** as actually evidenced. Responded requires
   ResponseSummary; terminal states require ActorName, OccurredOn, Summary and
   EvidenceReference. Not required needs a reason and evidence, never silent omission.
3. Set ConditionsState **Open** and ConditionsNotes for unresolved matters.
   Keep notes short (255 characters); place full text in linked evidence.
   Resolution requires an explicit evidence reference. Preserve responses that
   disagree; recording one response never resolves another respondent's conditions.

An absent response, empty view or elapsed date never means consent or agreement.

## Ownership handoff

1. Record EventKind **Ownership handoff**, **Proposed**, FromRole and SubjectRole,
   exact scope, the offered work/constraints in Summary, evidence and NextAction.
   Proposed does not assign the receiving role or establish capacity.
2. Record actual **Accepted**, **Declined** or **Withdrawn** as a separate event,
   linking the original proposal in ParentEventUID. Accepted requires that link;
   confirm same case/document/version/hash and offering/receiving roles manually
   or with the validator. Include actual actor/date/rationale/evidence, capacity
   or conditions and next action. Native validation cannot verify cross-row links.
3. Check the applicable authority/delegation and evidence before relying on an
   acceptance. Recording acceptance neither changes Review Queue nor performs a
   legal/governance transfer. Existing mandated operational routes still apply.

## History, corrections and changed documents

Save and reopen every event to check the entered identity, kind, state, actor/date,
links and conditions. Native version history retains edits. For another assertion
or correction, prefer a new EventUID with SupersedesEventUID pointing at the prior
same-scope event; retain both. The views include history and do not automatically
select a final/current assertion or close superseded conditions.

Changed document bytes/version need new pending/proposed events. Do not retarget
an old response or acceptance to a new version. Prior consultation can be linked
as background evidence but does not become current acceptance. Check conflicting
responses and unresolved conditions explicitly.

## Focused views

- **Awaiting consultation response** shows entered Unknown/Pending response
  consultation records, including historical pending entries retained for traceability.
- **Ownership offered - not accepted** shows entered Unknown/Proposed handoffs.
- **Outstanding consultation conditions** shows Open conditions on either kind.
- **Response and ownership history** retains all assertions and version references.

These are literal entered-record views. A later response does not hide its pending
predecessor. Inspect linked response/supersession records before counting outstanding
work. An empty view does not prove consultation coverage or completed handoff.

## Native controls and optional stronger check

Native required fields, unique EventUID, versioning and List validation reject
missing identity, invalid kind/state combinations and incomplete terminal records.
Hash validation checks length only. The platform cannot authenticate an actor's
assertion, inspect evidence, prove authority, enforce cross-row version/role links
or determine the operative/current policy.

The optional read-only validator checks hexadecimal hash, document bytes, exact
scope, parent proposal/response and supersession references, and duplicate event
identity. Supply private event/history JSON; history must omit the event being
validated while including its parents and later superseding assertions:

```sh
python3 scripts/ppg_consultation.py --event PRIVATE-EVENT.json --history PRIVATE-HISTORY.json --case-uid EXISTING_CASE_UID --document-ref STABLE_DOCUMENT_REFERENCE --version-ref EXACT_VERSION_REFERENCE --document PRIVATE-EXACT-DOCUMENT
```

A recordedOwnershipAcceptance result is an evidenced record state for that exact
version, never an assignment, notification, policy approval or completed transfer.
Invalid/stale/superseded assertions return Unknown for operational reliance.

## Technical delivery evidence

Maintained schema/views/validation: `config/consultation-handoff.json`.
Repeat-safe same-site provisioning: `tools/consultation/provision.js`.
Native qualification and lifecycle are recorded in the selected Conductor track;
local checks alone are not native deployment proof. Real data, actor identities,
resource IDs and detailed receipts stay outside Git under `.local/consultation-handoff/`.
