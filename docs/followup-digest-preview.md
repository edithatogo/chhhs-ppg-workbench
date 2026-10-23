# Follow-up recording and manual digest preview

23 October correction: accepted ownership requires a usable UTC occurrence time at or before the preview as-of time. Future, invalid, missing and non-UTC acceptance stays unresolved. Existing snapshots remain historical; use a new explicit preview key when the guard refuses an old output instead of overwriting it.

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

This is the supported local/manual fallback for RF-02/RF-04. It needs the existing
Python interpreter, no additional Microsoft licence, connector, consent or tenant
write permission. Existing Lists views remain the in-workspace entry point. This
command does not deploy a native form, cloud digest or notification service.

For the qualified normal web route, use
[native follow-up/history and workspace previews](followup-native-web.md).
The local command remains a recovery/preparation option; operators do not need
Python or desktop Office for the native route.

Use the existing consultation/handoff ledger for proposed and accepted roles.
Export its records through the qualified CLI when needed; do not infer acceptance
from the case's free-text role. Follow-up events supplement that ledger without
changing it, the lifecycle writer's objects, cases or the upstream register.
Store real inputs and all outputs under ignored `.local/`, in approved storage;
outputs include private recipient details. Only the fictional fixture belongs in Git.

Run a fictional preview from the repository root:

```sh
.venv/bin/python scripts/ppg_followup_digest.py \
  --input templates/followup/fictional-preview.json \
  --as-of 2026-10-18T00:00:00Z --output .local/followup-preview.json
```

Repeat to a new output path with `--previous .local/followup-preview.json` to
identify unchanged candidates. Outputs are exclusive: existing files are refused.
Inspect the JSON in the workspace; no email-ready body or sending action exists.
Delivery eligibility is always false, independently of preview inclusion.

The input has `events`, `currentScopes` and existing `ownershipEvents` arrays.
The fictional fixture shows the full shape. Record UTC event time, actor, stage,
state and human rationale. `Priority` is human text, never an automatic clinical
score. `SourceDueDate` remains separate from `AgreedTargetDate`; an agreed target
requires `TargetAgreementEvidence`. Blank dates remain null. Use `WaitingReason`
and `NextAction` for the specific blocker and next work. Do not put patient data
in these fields. `stageEnteredOn` is derived from consecutive same-stage,
same-document-scope history, preserving subsequent priority/action changes.

To record a transition, prepare one event JSON with a new persistent `EventUID`
and `PreviousEventUID` equal to the current case head. Run the same command with
`--append-event .local/new-followup-event.json` and a new output filename. It
produces a new input payload copy; retain the original. An exact retry returns
unchanged; conflicting reuse or a stale head/version is refused. This is a serial
local preparation workflow, not a transactional multi-user native store. Refresh
and reconcile inputs before any future native application. Old-version history
stays intact; only current exact case/document/version/hash can enter a preview.

Only Open records with a next action, one valid current-version accepted handoff
(with no unresolved conditions), an explicitly verified role-matched recipient
and confirmed source freshness enter the candidate array. Completed, Declined
and Superseded records are suppressed. Unknowns, stale scope, ambiguous acceptance
and missing recipients are exception rows. A recipient assertion records a manual
directory/authority check, not access or consent proof. Freshness is the operator's
explicit `Current` assertion with source-as-of and check timestamps; it is not
inferred from file modification time. Its evidence must be checked operationally.

The18 October local slice did not attempt native mutation. Its former native
deployment gap is superseded by the21 October dedicated-register/manual-flow
qualification; existing case and lifecycle writers retain their objects. Native
schema/effects, append/readback, retry and scoped source preservation now have
fictional current-account proof. This does not establish ordinary-user adoption.
Planner, Approvals and a custom Power Apps form are deferred: the existing ledger,
Lists views and manual preview meet the selected preparation need without creating
a second task authority, messages, premium dependency or additional environment.
Native preview placement is delivered; ordinary-user acceptance remains separate.
