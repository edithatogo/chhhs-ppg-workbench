# Coexisting selected-case event routes — saved, runtime qualification pending

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The two existing event flows can retain ownership actions alongside consultation
entry. Operators choose an explicit action rather than requiring an administrator
to replace a flow definition for each step. Both candidates were saved to their existing native flows on 18 October 2026.
Independent GET readback matched their executable definitions, excluding only
injected authentication, and both remain Stopped. No operator run of these
composed profiles has occurred. Existing qualified profiles and evidence remain retained.

| Flow purpose | Action field | Choices | Other inputs |
|---|---|---|---|
| Offers and consultation requests | `text`, labelled Action | Ownership offer; Consultation request | Ownership role and scope come from the verified request |
| Selected responses | `text_5`, labelled Action | Ownership response; Consultation response | Existing `text` through `text_4`: reference, response, reason, evidence, next action |

Only Action is required by the native form schema. Ownership response retains its
mode-specific runtime validation before context reads. Missing or non-text fields
are refused explicitly. An unbound consultation check requires no invented response
content. Unsupported actions stop with an explicit zero-effect result.

Both routes reuse one authenticated selected-case context graph. The operator
supplies no document pins, case identity or parent override. Ownership payloads,
parent/scope checks, full-payload retry checks and long-action handling remain in
place. A matching existing proposal can be returned historically after case
progression, with no creator or progression permission.

After-write case/source/request/parent checks still determine qualification. A
verified retained event followed by context drift has `qualified=false` and an
explicit retained-event/context-changed result. Successful execution alone is not
qualification. Readback uncertainty remains unknown and requires reconciliation.

The final after-check is flat to keep the composed native action depth within
eight levels. Sibling-scope dependencies are checked during construction; response
payload evaluation still waits for its native parent and response-history reads.

## Prepared-document boundary

Consultation currently returns an explicit missing-prepared-revision hold with
zero event/case/source/request writes. The original source is not substituted for
the prepared draft. A supplied prepared binding is rejected by this initial
composition until its actual native consumer is implemented and qualified.

The configured role is the existing fictional content-review role. It establishes
neither an independent reviewer nor real actor authority. The actual prepared-file
identity/version/hash, original-source provenance and qualification receipt must
come from the document and integration owners before consultation is invoked.

## Coverage preparation

The separate read-only coverage action builder requires explicit same-case,
separate prepared scope and a nonempty, unique required-role plan. It cannot
validate a draft or grant content readiness, policy approval or progression.
The caller must first qualify the physical prepared artifact and its provenance.

For this initial contract, each required role needs exactly one request and one
matching responded record with closed conditions, evidence, rationale, next action
and valid native chronology. Pending, declined, conditional, duplicate, unknown-role
or correction histories hold. No latest-date choice resolves conflicting records.

Readers must retain the qualified SharePoint provider, connection and dataset and
use the reviewed literal collection URI. Only a complete collection or the exact
current-CaseUID filter is accepted; state/condition/role filters, selected-column
projections, explicit truncation and dynamic URIs are refused. Native next links
also prevent complete coverage. Calculations use built-in
[Filter array and Select actions](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-perform-data-operations).
Actual prepared-scope recording and native coverage qualification remain pending.

Maintained sources: [event routing](../tools/lifecycle/build_selected_event_routes.py)
and [coverage actions](../tools/lifecycle/build_consultation_coverage.py).
Private router candidates remain under `.local/policy-lifecycle/coexisting-event-routes/`.

## Native operator-form observation

The new request flow appeared in the actual selected-row Lists menu. Its embedded
run panel remained blank with a progress indicator on a fresh owned filtered tab;
one reopen after the direct Power Automate details page loaded produced the same
result. No inputs or Run button were reached and no run was submitted. Native
history confirmed the latest run unchanged, and the request flow was stopped
again. This is a form-loading blocker, not runtime replay qualification. The
response flow remains stopped and unrun. Existing authentication was preserved.

A separate bounded schema probe removed only the Action enum and adjusted its
description while preserving the executable runtime allowlist. The plain-string
form still remained blank, so the enum hypothesis did not resolve the blocker.
No run was submitted. Both original composed candidates were restored, independently
read back as matching, and remain Stopped. No authentication changes were made.

## Prepared-context composition increment

The local [composition builder](../tools/lifecycle/build_selected_prepared_context.py)
can embed the integration lane's reviewed preparation branch at top level after
the same selected-case context. It requires the exact reviewed definition digest,
identical context and connection references, and a GET-only SharePoint reader.
Case projection branches are not copied. Ownership actions remain unchanged;
consultation mode selects the reader using the existing form key. Unsupported
executable actions, writes and method-override headers are refused. Three focused
checks pass; both current private candidates assemble within the action-depth limit.
This is local preparation only: the approved reader still needs its native positive
qualification handoff, and consultation recording/coverage and operator UI remain
unqualified. The composed prepared-reader candidates were subsequently saved and read back
Stopped; their runtime qualification remains pending.

## Prepared-scope event recording — local implementation

The [consultation builder](../tools/lifecycle/build_prepared_consultation_events.py)
adds mutually exclusive consultation branches to the two existing event flows.
Each flow retains its ownership creator and has a separate consultation creator
for the same existing list; no invocation can choose both modes. No extra native
flow, connection, role assignment, notification or case writer is introduced.

Requests use the verified prepared file UID/version and existing fictional role.
Responses retain the existing five input wires, derive the exact request parent,
and accept Responded, Unanswered, Declined or Conditional assertions. Only Responded
records closed conditions; all other outcomes retain Open conditions. This is
recording only, with no consultation coverage or content-readiness grant.

The response verifies the complete request payload except its original date,
requires complete response history, and refuses a competing response identity.
Both modes use absent-only creates, exact immutable-payload retries excluding the
creation date, complete native readback, and before/after checks on case, source,
baseline, draft, template and qualification receipt. Response parent/history are
rechecked after recording. Long next actions retain their full Note value and use
a bounded finding in the Text255 conditions field. Uncertain writes/readback hold
for reconciliation; context drift cannot become qualified success.

Four focused event checks and three prerequisite checks pass. Current private
compositions have action depth eight and no unresolved action references. These
candidates are now saved and read back Stopped; they have not been run natively. The prepared-reader positive
qualification, operator entry, recording/replay/adverse output proof, and later
coverage integration remain open.

## Runtime coverage integration — local only

Coverage now derives its scope from the same execution's verified prepared-reader
output, rather than requiring per-document flow configuration. It reads the full
literal event collection; a fixture CaseUID filter is rejected for this runtime
route. The history result remains provisional until fresh case, source, baseline,
draft, receipt and template metadata checks complete. Only the final
`Native_consultation_coverage_receipt` combines complete history with that native
context bracket. A verified event with drifted context cannot open this check.

Five event checks, two runtime-coverage checks and four existing coverage checks
pass. The response composition has 166 actions, maximum depth eight. This remains
local implementation; no native recording or coverage acceptance is claimed.

## Review fixes before native qualification

Both ownership and consultation append actions in newly assembled candidates now
set `inputs.retryPolicy.type=none` explicitly. A response reads its parent item
again, requires a nonempty/nonwildcard native token and unchanged immutable
payload, then refreshes the complete response history immediately before the
write guard. A newly visible competing or changed history holds without creation.
After recording, parent token/payload and exact response history are checked again.
These are observable native brackets, not an atomic transaction; changes after
the last pre-write read can still require reconciliation. Existing qualified
native profiles/evidence remain preserved. These fixes are now saved and read back
Stopped, with native runtime proof still pending.
Six event checks and three prerequisite checks pass.

## Upstream native reader evidence

Independent reads verified the current prepared-output positive receipt and three
terminal negative runs: missing template token, invalid template hash and stale
generated version. Every negative receipt kept preparation and consultation closed
with zero writes. A subsequent exact flow read still showed the integration
owner's negative profile Started, rather than the final good definition restored.
Event deployment/invocation therefore remain held pending that owner's restoration
and handoff. No event-flow deployment or upstream flow mutation was performed by
this lane. The direct event-flow details page also exposed no Run/Test control or
selected-case form; it is not a qualified fallback for the stalled Lists widget.

## Native consultation save and response guard correction

The reviewed request definition saved successfully. The first response save
returned HTTP400; independent GET confirmed that the previous response definition
remained Stopped. Its final pre-write expression contained 9,089 characters.
Splitting those same conditions into bounded, side-effect-free Compose checks
allowed the revised response definition to save. The final guard requires every
check to be true; no native read or write occurs between the final history read
and these evaluations. Six focused event checks passed after the correction.

Both current executable definitions now match independent native GET readback,
excluding only injected authentication, and both remain Stopped. Request has133
and response170 actions, maximum depth eight. Mutation retry policies are
explicitly none, and ownership/consultation creators remain mutually exclusive.
No consultation event run or write has occurred. The integration owner's good
prepared-reader definition was also independently verified restored and Stopped
before these saves. Prior negative-profile observation remains retained privately.

The existing manual-button flow's current first-party form rendered successfully
in the integration lane without submitting a run. That lane owns the shared
case-reference adapter; native trigger conversion awaits its concrete review.
The selected-row widget gap is retained separately from this supported fallback.

## Response-form wording prepared for manual entry

The maintained form schema now describes both response actions: ownership
Accepted/Declined and consultation Responded/Unanswered/Declined/Conditional, with
the corresponding reference prefixes and input limits. Input wire keys and
runtime validation are unchanged. This wording fix is local and will accompany
the reviewed manual-entry conversion; it has not changed the saved native
selected-trigger rollback definition. Six routing and six event checks pass.
The separate [draft operator guide](lifecycle-manual-consultation-guide.md) remains
explicitly pending native form/context/event qualification.

## Shared manual case-reference adapter — awaiting review

The canonical [adapter](../tools/lifecycle/build_case_reference_entry.py) now uses
the currently observed manual Button trigger and retains the existing flow,
connection and action contracts. It reserves Case reference, validates its type
and bounded fictional syntax before GET, derives the fixed list from the reviewed
selected trigger, and requires a complete singleton exact-CaseUID match with a
positive native ID. The subsequent case read must still match both the reference
and resolved ID before any baseline or source-file read. All copied case reads
throughout the assembled definition use the server-resolved ID. Unknown residual
caller-entity/row expressions and action-name collisions are refused. The context
explicitly reports `manual_case_reference_lookup`, without selected-row provenance.

Five focused construction checks pass; actual case-work and both event assemblies
remain within depth eight. These manual candidates are not deployed. The existing
manual initiation flow remains unchanged. An independent native pre-test baseline
retains the case, its two existing ownership events, prepared draft2.0, receipt,
template and source; there are no prepared-scope consultation events yet. Native
read-only context/form proof precedes event creation and retry qualification.

## Actual native manual context proof

The first-party manual form rendered Action and Case reference. One actual UI
submission executed the GET-only probe successfully, resolving the reference to
item7 and passing singleton, full-read identity, baseline and source checks.
The resulting context explicitly reported manual lookup provenance and zero
writes. The exact previous stopped definition and connection references were
restored and independently read back.

The first raw preservation comparison failed. Exact difference accounting found
only three request-generated `odata.id` values: one case response and two event
responses. Removing only those fields left every protected value identical;
actual item IDs, GUIDs, opaque ETags and all business fields were retained. Draft,
receipt, template and source metadata matched without exclusions. The raw failure
and corrected audit are preserved privately. No consultation event was created.

This observation exposed a separate local consultation-history defect: raw row
comparison would mistake changing transport identifiers for changed evidence.
The builder now removes only `odata.id` at singleton-history comparison boundaries.
Zero/multiple-row arrays and all actual IDs, GUIDs, ETags and business fields remain
strict, as do count and pagination checks. Six event and five adapter checks pass;
native adverse comparison regression and event recording remain pending.

## Native comparison regression and dotted-property correction

A GET-only in-memory regression exposed that native setProperty/removeProperty
reject dotted property names. The initial regression failed at fixture setup;
its definition, terminal run and exact error remain retained. No list row changed.
The supported correction uses object union with a parsed single-property JSON
object to normalize only `odata.id` to a constant. Every other property remains
part of strict history comparison, including native IDs, GUIDs and opaque ETags.

The corrected native regression passed: response-identifier-only differences
compare equal, while changed opaque ETag, changed payload, duplicate rows and
both pagination-marker forms compare unequal. Native fixture readback confirms
the positive pair actually differs only in its response identifier. These were
explicit in-memory adverse observations based on a native row, not list mutations
or consultation acceptance. Eleven connector actions were GET-only. The exact
previous stopped definition/connection references were restored; six protected
snapshots remained identical after accounting only for response `odata.id`.

The separately rejected initial definition and native expression failure are
preserved, along with the corrected successful run. Production event recording
and whole-cycle acceptance remain separate next steps.

## Permanent manual entry and fresh ownership occurrence

Both permanent manual event definitions are now saved and independently read
back, retaining their existing flow IDs, connections, history and rollback
profiles. The actual first-party request and seven-field response forms rendered
and accepted the intended fictional inputs.

For a separate fresh fictional occurrence, one ownership proposal and one explicit
Accepted assertion were recorded and independently reloaded. Exact retries of
both returned their original records and timestamps with zero creates. The case
remained unchanged, and no responsibility transfer or notification was performed
by these event flows. Both flows were stopped with exact definitions/references
verified before the separate case-update owner received the terminal Accepted
and retry pins. Actual case projection remains that owner's separate operation.
The prepared-draft consultation case remains distinct and unmodified.

## Edited-draft consultation and exact retry

The actual manual response form recorded one fictional Responded assertion against
its unique pending request and the selected edited Word revision v2. The native
receipt verified the retained event; the coverage receipt found exactly one request
and one response for the required fictional role and revalidated case, source,
baseline, draft, template and preparation-receipt pins. Exact genuine-input retry
returned the original response with zero creates and unchanged timestamp/content;
coverage passed again. Neither run granted readiness, approval or progression.

Native SharePoint represents the request's absent response summary as null. The
request contract now writes and verifies that canonical absence explicitly;
answered response findings remain required and nonempty. The original held
request receipt and its subsequent zero-create reconciliation are retained,
without rewriting the original record or creating a duplicate. Seven focused
checks cover this contract and the existing consultation guards.

Private prepared-consultation receipts retain the exact runs, actual edited scope,
readbacks and preservation checks. This is bounded fictional technical coverage;
ordinary-user access, real responder authority and the later connected human
readiness/decision/publication cycle remain open.

## Second prepared occurrence and changed-input reconciliation

The same installed request and response definitions subsequently consumed a
different existing fictional occurrence through their generic preparation branch.
Its own final edited Word revision and immutable preparation receipt were first
verified by the case-work owner. One actual-form request and one Responded entry
were recorded against that exact scope; identical repeats created zero records
and preserved original payloads and dates. Both coverage observations found one
request and one response for the configured fictional role with fresh context.

A changed finding under the same response reference held event qualification.
The creator explicitly skipped; the runtime returned unknown/reconcile rather
than a zero-write receipt. Independent complete-history reconciliation then
verified exactly the two intended additions, unchanged originals and all prior
rows. Twelve other case, file, baseline and projection snapshots were preserved.
Both flows returned to Stopped with exact definitions and connection references.
Private evidence remains under `.local/policy-lifecycle/case9-consultation-readiness/`.

The subsequent readiness fixture was held while a Microsoft push subscription
renewed during native list inspection. After the exploratory forms were closed,
the retained subscription expired. Fresh complete snapshots, the intended saved
connection and the exact expired receiver mapping were verified before one guarded
CLI creation of the same approved fictional finding. The guard allowed one mutation
attempt and prevented automatic POST retry or redirect following. Native readback
verified the full payload, original DateOnly calendar representation, true fictional
marker and immutable row identity; the actual saved display was reopened and its
native row remained unchanged. All earlier findings and twelve other snapshots
were preserved. Post-write subscriptions and receivers were complete empty arrays;
no settings were changed, and no universal tenant-effects claim follows.

This completes technical recording for that occurrence, not human content review.
The separate case-work readiness consumer, purpose decisions and publication still
require their own current evidence. Never resave a finding to repeat a read-only
consumer check.

## Second prepared occurrence: readiness consumption and four purpose records

The installed case-work reader subsequently consumed the retained readiness
finding for the exact edited Word revision. Its first check and identical repeat
verified current preparation, consultation coverage and the one recorded finding;
both performed zero writes and skipped all six projection writers. This completes
technical readiness consumption for this occurrence, without a human content
assessment or permission to progress.

A temporarily assigned, unchanged purpose flow then recorded Committee endorsement,
Officer signoff, Coordinator check and Final authorisation, in that order. Each
actual native form used the reviewed fictional actor, rationale, evidence and route
profile. Every first run created one version-scoped event; its immediate identical
repeat created zero and preserved the full original native row and date before
the next purpose was attempted. Runtime and independent readback verified exact
prepared/readiness scope, immutable profile, parent chain and chronology. The last
pair observed all four assertions together. All prior Assurance history, including
the separate Deferred/Open case, and twelve other protected snapshots were preserved.

The preflight distinguished legacy alerts from modern Rules. An initial query's
client option did not send its intended body; that incomplete observation and its
correction are retained. After the observed UI-created push subscription expired,
the corrected exact-list enumeration explicitly included automatic rules and
Quick Steps and returned a complete empty result. The same expired Microsoft
subscription/receiver mapping, fresh protected frame, stopped exact flow and full
terminal history were verified before enabling. No subscription, rule, permission
or connection setting was changed to qualify the test.

Private `.local/policy-lifecycle/case9-purpose-recording/` retains the canonical
plan, eight forms/runs, complete action histories, native receipts, per-stage
independent snapshots and final audit. This qualifies fictional technical purpose
recording and replay only. Controlled publication, independent binary proof,
implementation, verification, closure, next review and ordinary-user/business
acceptance still require their own current evidence; no real policy approval follows.
