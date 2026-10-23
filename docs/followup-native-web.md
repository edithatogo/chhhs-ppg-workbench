# Follow-up history and quiet digest preview — web route

The manual web path is qualified with fictional records under the current
account. Four versioned Lists, seven views and one on-demand flow support dated
follow-up history and saved digest previews. Source case and ownership inputs
remain unchanged. No desktop Office, operator CLI or messaging service is part
of this route. Representative ordinary-user adoption remains separate.

## Record follow-up

1. Open **PPG Follow-up Contexts**. Record the existing CaseUID, exact document
   reference/version/hash and evidence for the observed source. Keep source due
   date separate from an agreed review target. Record source-as-of/check times
   and freshness explicitly; Unknown is valid. Verify any recipient against the
   accepted role and retain evidence. This records an observation, not authority
   to change the central register or assign a role.
2. Reopen the context and note its current native version. Open **PPG Follow-up
   Requests**, choose New and select **Record follow-up**. Use a fresh request
   key/event UID, the CaseUID/context version and latest completed predecessor
   EventUID (blank for the first event). Record stage, state, occurrence/as-of
   UTC time, rationale, human priority, next action and waiting reason. Record
   target-agreement evidence if an agreed date exists. Save and reopen.
3. Open the on-demand follow-up flow, Run, and enter the request's numeric item
   ID. Inspect that exact run's terminal result and **Report_followup** output.
   A started message or green intermediate action is insufficient.
4. Open **PPG Follow-up History** and the exact completion record. Verify the
   event, document scope, recorded actor, dates and predecessor. Earlier events
   remain history. Native version history provides correction evidence; a direct
   edit to a committed event is detected and held by later processing.
5. Record a later transition with a new request/event and current predecessor.
   An exact retry reuses the existing output. A stale predecessor or conflicting
   identity is refused. Preserve uncertainty and inspect actual saved rows before
   retrying a timeout. Never delete partial evidence to make a rerun pass.

## Preview a digest

Create a new request with **Preview digest**, a fresh request key and UTC as-of
instant. Optionally copy the previous completed preview RunKey to identify
unchanged candidates. Run the same flow with this request ID. Use its final
RunKey/digest link and confirm the candidate, exception and suppression counts.
Each preview is a version-bound observation, rather than a live email draft.

A candidate requires an Open follow-up, exact current scope, one valid recorded
accepted handoff with no open conditions, confirmed source freshness and a
verified recipient matching that role. Missing scope, ownership, recipient or
freshness becomes an exception. Completed/declined/superseded follow-ups and
closed cases are suppressed. Stage-entry time is retained across same-stage
updates. New candidate rows expose stage-entry time and the recorded human
priority as columns; neither is a calculated clinical urgency score. Earlier
snapshots retain their original payload and may have blank additive columns.
The accepted handoff ledger remains authoritative for its recorded
assertions; the preview does not create a second assignment authority.

Snapshots are usable only with their exact completed-run marker. A failed or
interrupted run may have partial rows; it is not a completed preview. Later source
changes require a new request/preview. Earlier snapshots remain historical.
Inspect native version history if a row was edited: managed snapshot rows and
their completion marker must still be at version1.0 for the original output
proof to apply. A retained human edit is evidence, not an automatically validated
new preview. Create a fresh preview to observe current state.
No notification or delivery action exists. Per-flow platform failure alerts must
also be verified Off before activation; creating a flow with a requested false
flag alone did not apply that setting in the current tenant.

Native List pages may establish Microsoft-managed realtime UI subscriptions.
These were observed with matching SharePoint Core receivers and short-lived
Microsoft service endpoints; they are distinct from owner reminders or workflow
delivery. Unknown rules/subscribers/receivers still hold the affected deployment.
Do not delete platform channels to make an empty-subscription check pass.
Microsoft documents realtime List changes through its
[websocket notification route](https://learn.microsoft.com/en-us/graph/api/subscriptions-socketio?view=graph-rest-1.0);
the classification here is limited to the native channels actually read back.

## Holds and recovery

| Hold | Response |
|---|---|
| Stale context/document scope or predecessor | Refresh the observed scope/head; retain the old request and create a corrected request/event. |
| Conflicting output or edited history | Preserve current wording/history; inspect the exact key and prior run. Do not overwrite it. |
| Incomplete native collection/bounded limit | Stop the affected operation; qualify complete pagination before scaling. No silent truncation. |
| Source/history changed during save | Retain partial rows and run handle; reconcile current inputs and completed markers before retry. |
| Missing completed previous preview | Choose an actual completed preview key or omit it for a first observation. |

### Copied-record recovery

1. Preserve the exact run handle, original files, native field bindings, item
   versions/ETags and complete source/target exports. Stop the affected path;
   distinguish an observation failure from a terminal failed run.
2. Reconcile actual saved rows by EventUID/SnapshotKey and completion marker.
   If sources and outputs are unchanged, an exact retry can complete missing
   writes. Do not issue a new key merely to hide a partial run.
3. If a human edit or source drift prevents that retry, retain the evidence and
   reconcile it explicitly. Restore required logical records into an isolated,
   versioned copy with matching schema and unique constraints. Read back every
   field and retain a source-item/version to copy-item mapping. Native item IDs,
   native authors and native version history are not recreated by copying data.
4. Repeat the copy and prove zero additional rows; verify that original records
   and their actors/versions remain unchanged. Rebinding a live flow or retiring
   the original store requires a separately checked cutover, not an automatic
   recovery side effect.

Qualification copied all three fictional history events into a dedicated
recovery List, preserving payloads and recorded actors; replay created zero rows.
The original history remained at three version1.0 records. This is bounded
copied-record recovery, not a full native disaster-restoration claim.

## Dated qualification — 21 October 2026

Current correction, 23 October: runtime v5 / flow1.4.0.0 requires ownership
acceptance to have a usable UTC time at or before the preview as-of time. Future
or unqualified acceptance remains an ownership exception. Native negative and
positive controls pass; existing connections/state and quiet behavior are verified.
An older preview key that now conflicts remains preserved; create a new explicit
preview rather than overwriting its historical snapshot. Ordinary-user acceptance
and optional integrations remain deferred. See the
[final review](../conductor/archive/ppg_review_followup_20261018/review.md).

Successful native runs demonstrate first/repeated recording, changed-stage
history, first/unchanged previews, future-event/stale-scope/unknown-freshness/
unresolved-recipient exceptions and completed-follow-up suppression with zero
candidates. Stale context/predecessor, duplicate event/predecessor and an edited
snapshot retry were refused. The fictional human note, its version/ETag and
original event history survive. Candidate columns render stage-entry time,
human priority, distinct agreed/source dates and source observation times.
Declined/superseded and additional missing/ambiguous inputs are covered by the
same runtime's local rules tests; no native clinical decision is implied.

Use exact run-filtered results. Unfiltered candidate views contain historical
observations, including the deliberately edited fictional qualification row.
The final fictional preview contains one suppressed completed follow-up and no
candidate; this does not close the separate source review case.

Planner, Approvals and a custom form are deferred: the existing web forms and
manual flow meet this slice, while task/approval projection would add separate
authority, audience and notification effects without a demonstrated need.
Their precise plan/access/subscriber eligibility is not claimed as freshly
qualified. Reassess only for an identified unmet operator requirement.

Source/case/ownership Lists are read-only inputs. Four dedicated follow-up Lists,
a dedicated workbook/script and one manual flow belong to Workbench integration.
Existing lifecycle and ALM owners retain their objects. Native form entry does
not validate clinical authority, current-policy truth or recipient consent.
No new access, licence, retention lock or schedule is introduced. Ordinary-user
execution and real-use benefit measurement are separate acceptance stages.
