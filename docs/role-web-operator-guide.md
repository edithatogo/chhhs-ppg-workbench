# Role responsibility refresh — web operator guide

Use the published SharePoint role-refresh page to open the flow and the existing
Dated responsibilities and Responsibility exceptions views. Current qualification
uses labelled fictional records. No real appointment or clinical authority is
established by the demonstration.

1. Open the on-demand role projection flow in Power Automate. Select Run and enter
   the intended as-of date as YYYY-MM-DD. Run once; a started message is not a
   completed snapshot. No desktop Office or local CLI is required.
2. Open that exact run in run history. Wait for its terminal result; do not launch
   another run because the browser still shows Loading or Running.
3. On success, open `Report_projection` outputs. Confirm
   `state = completed_dated_snapshot`, and retain its `runKey`, `snapshotCount`
   and as-of date. A green run alone is insufficient without that report.
4. Open Dated responsibilities. Filter RunKey to the report's exact key. Check the
   row count matches snapshotCount and inspect the intended date, document, role,
   holder and resolution. Earlier snapshots remain history, not simultaneous
   appointments. Use Responsibility exceptions for unresolved/ambiguous rows.
5. If the run fails, preserve the run link and existing records. Resolve the
   following holds through the authorised operator; do not repair old snapshots
   or choose a holder just to make a run pass.

| Hold | Meaning and next action |
|---|---|
| RoleSnapshotConflict | An existing snapshot differs. No snapshot is created by this run; preserve wording and investigate the exact key and evidence. |
| RoleSnapshotChangedDuringSave | Saved-row readback differs or is missing. Retain any partial rows; inspect this run before retrying. |
| RoleSourceChanged | Input rereads differ before saving. Reconcile the input versions, then request a fresh dated run. |
| RoleSourceChangedAfterSave | Inputs differ after saving. Partial rows are not a completed snapshot; retain them and reconcile the run. |

For a transport timeout, inspect the exact run and native rows before retrying.
An identical request reuses exact rows. It does not overwrite an edited row.
Only the final completed report identifies an accepted technical snapshot set;
this is not approval of appointments, a portfolio transfer or a clinical decision.

Edit appointments, responsibilities and handovers only through their separately
maintained process. A role refresh does not grant access, infer a vacancy, choose
between overlapping appointments, change an upstream register or send an owner
notification. There is no schedule. Platform failure-alert settings are separate.

Current limits: role data is a bounded qualification fixture; ordinary-user access
and actual organisational appointments remain unverified. Controlled pre-save
mismatch and conflict refusal are qualified. Timed concurrent edits and the final
post-save mismatch path are not yet qualified. The historical procedure/template
inputs remain provisional and do not block this technical development.
