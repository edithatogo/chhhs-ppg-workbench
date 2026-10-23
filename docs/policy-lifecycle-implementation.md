# Full policy lifecycle — implementation and acceptance map

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

## Current reconciled result — 23 October 2026

[Reviewed technical archive and remaining requirements](lifecycle-closeout-20261023.md)
supersedes pending wording in the dated sections below. Both configured fictional
r6 cycles are2/2 and the commissioned WB queue is closed. General edition graph
controls, broader native adverse windows and real publication/authority remain
unqualified. Third-party review is user-deferred to the final adoption track.
The scenario ledger retains old pending text as history alongside dated current
proof; full original acceptance remains false. Do not repeat completed cycles.

## Commission and baseline

On 17 October 2026 the user commissioned the full policy-management cycle within
M365 and Power Platform. This extends the previously completed recording workbench;
it does not reopen its delivered components or perform substantive policy review.
This map records scoped technical qualification; it is not an approved clinical
procedure. Policy-derived routing/delegation requirements must be attached by the
source-review lane before their dependent native transitions are enabled.

## Reuse and remaining behaviour

| Stage | Existing authoritative system component | Remaining behaviour and acceptance proof |
|---|---|---|
| Identify and initiate | Catalogue, Review Queue, guarded source sync, monthly reporting | Native case initiation tied to stable DocumentUID and exact baseline; repeated initiation does not duplicate the same review occurrence |
| Establish ownership | Case role fields and Consultation/Handoff Events | Explicit offer/accept/decline handling with next action and agreed due date; a proposal never becomes accepted responsibility implicitly |
| Prepare and revise | Evidence library, maintained templates, package completeness | Essential preparation usable inside M365; editable versioned output and native validations; retries preserve human edits and issued history |
| Consult | Consultation/Handoff Events | Version-scoped requests/responses and coverage/conditions checks; explicit recipients/routes before any sending; changed content invalidates reliance on earlier-version responses |
| Assess readiness | Readiness Events | Native gate compares case/document/version/hash and required findings/conditions; no inferred pass from file presence or an empty view |
| Seek and record decision | Assurance Decision events | Source-supported route/delegation and exact-version submission; rejection/defer/return-for-change branches; endorsement alone never becomes approval |
| Publish and make effective | Assurance Publication events and library history | Connect to actual controlled publication destination; retain exact approved and issued revisions, effective date and verified link; no automatic issue from a recorded assertion |
| Implement and verify | Assurance Implementation/Verification events | Link actual actions and evidence, failed/inconclusive outcomes and unresolved conditions; only evidence-backed completion advances the case |
| Maintain, supersede, withdraw | Policy edition fields/views and current edition-management work | Explicit replacement/withdrawal/retirement evidence and retained issued versions; source absence never retires a policy |
| Re-enter review | Existing due/overdue reporting | Establish the next review occurrence from recorded rules/dates without overwriting the completed occurrence or inventing a review period |

## Transition contract to implement

These are semantic gates, not new CaseStatus choice strings. The native owner must
read the existing live case schema and map these gates before making additive
changes; do not install a parallel status system.

- Each transition has a unique request identity, CaseUID, document identity, review
  occurrence, expected current stage/ETag, exact document revision/hash, actor,
  requested target, evidence references and outcome. No executable names/recipients
  are inferred from free text or historical proposals.
- Read the current case and relevant event records before validation. Compare exact
  scope and referenced parent/supersession chains; native required-field validation
  alone does not prove cross-record consistency or actor authority.
- A changed document revision creates new pending assessment/consultation work.
  Preserve older decisions and responses without applying them to the new bytes.
- Rejection, deferral, open conditions, missing evidence and failed verification
  remain explicit incomplete outcomes with a next action. An absent record is not
  a completed stage. Withdrawal needs its own authorised evidence.
- Write only the owned case/local lifecycle fields using conditional concurrency;
  never write importer-owned source facts. Retain before/after and failure receipts.
  A failed or stale transition cannot advance case state.
- Separate local record mutation from external effects. Notifications, approval
  requests, publication and distribution require the identified authorised route;
  retries must not duplicate effects. Test using isolated fictional destinations.
- A replay with the same request and unchanged inputs returns the retained result;
  changed inputs under the same request identity are refused. Recovery resumes the
  same occurrence and preserves completed side effects and human edits.

## End-to-end acceptance

Prove one isolated fictional cycle through initiation, accepted ownership, editable
preparation, consultation, readiness, decision, publication representation,
implementation, verification, supersession/withdrawal and next-review creation.
The publication representation must be labelled fictional and isolated from the
real clinical publication route. Also prove rejection/defer/return-for-change,
changed-version refusal, stale concurrent update, retry after partial failure,
duplicate prevention and preserved history. Do not mark real policy outcomes.

Run through the intended M365 operator entry and relevant ordinary-user roles;
record any untested access separately. Required calculations, selections and
validation must execute within M365/Power Platform, with native readback of actual
records, files, links and run effects. Local tests and downloaded utilities do not
satisfy that runtime requirement. AI, Autofill, external adapters and Dataverse
migration are not prerequisites for this core lifecycle.

## Ownership and next integration

Workbench retains shared registry/hub/manifest and sole case/source integration
ownership; it owns native actionable routing after schema/guard agreement. Review
and templates owns source-grounded decision/publication/edition requirements and
its existing archive work. This lane owns the lifecycle contract and acceptance
mapping. Register one additive lifecycle track through Workbench after the mapping
is reconciled; do not create duplicate stage tracks or independent writers.

The first native initiation/ownership slice has now executed. Remaining integration
centres on usable case/version selection, editable M365 preparation, connected
operator stage gates, native closure/recovery, next occurrence and ordinary-user
access. Specific unavailable production document/publication routes remain open;
they must not silently be replaced by local scripts or recorded-only assertions.

## Existing implementation references

- [Consultation and ownership](consultation-handoff.md), maintained config `config/consultation-handoff.json`.
- [Readiness](human-readiness-recording.md), maintained config `config/readiness-recording.json`.
- [Decision through verification](decision-implementation-assurance.md), maintained config `config/assurance-recording.json`.
- [Edition history](policy-editions.md), maintained config `config/policy-edition-fields.json`.
- [Native document qualification](native-document-generation.md) and [package generation](unattended-package-generation.md).
- [Current handoff](../conductor/handoff.md) and [source precedence](../conductor/decisions.md).

## Implemented evidence gate and native binding handoff

`tools/lifecycle/validate.js` implements a pure consistency check with no I/O or
mutations. It accepts explicit scope, expected/observed case ETag, complete event
history and selected event IDs. It returns `consistent`, reasons and zero writes;
there is no approval, route-authority or policy-current result. The caller must
supply the required selection for its requested transition; checking one finding
does not establish that every lifecycle stage is complete.

| Evidence kind | Existing native field mapping |
|---|---|
| All events | EventUID, CaseUID, DocumentReference, ReviewedVersionRef, DocumentSHA256, EvidenceReference, ConditionsState, SupersedesEventUID |
| Ownership | EventKind=Ownership handoff; RecordState=Accepted; FromRole, SubjectRole, ParentEventUID; ActorName/OccurredOn; exact matching Proposed parent |
| Readiness | Finding=Ready for decision; AssessorName/AssessedOn; does not rename these to ActorName/OccurredOn |
| Decision | Stage=Decision; RecordState=Recorded; DecisionOutcome=Approved (recorded); DecisionReference, ReadinessEventUID; ActorName/OccurredOn |
| Publication | Stage=Publication; RecordState=Recorded; PublicationURL, PublishedVersionRef, ParentEventUID to selected decision |
| Implementation | Stage=Implementation; RecordState=Recorded; ImplementationActions; ParentEventUID to selected decision or publication |
| Verification | Stage=Verification; RecordState=Recorded; VerificationResult=Verified (recorded); VerificationMethod, ParentEventUID to selected implementation |

Fresh Workbench schema read reports the existing `caseStatus` as optional Text,
not a Choice. Existing role/date/action fields remain optional and do not include
native occurrence/revision/hash fields. Consequently no allowed state list or
missing lifecycle identity is inferred from that schema.

Additive storage candidate for the native owner: retain a versioned transition
request/receipt in the existing evidence library, keyed by unique request identity
and linked CaseUID, containing occurrence, semantic operation, expected ETag,
exact evidence pins, actor, before/after, effect identities and outcome. Bind it
explicitly to the case and validate uniqueness/recovery before updating local
fields. This is a proposal awaiting native schema/placement qualification, not an
existing store or permission to write one. Preserve existing case/source values.

Seven focused checks cover consistent chains, stale case/document pins,
endorsement/rejection/defer/open conditions, duplicate/superseded/cross-case
records, missing selected parents and exact ownership proposals. These are local
component checks only; native invocation, caller stage requirements, ordinary-user
access, effective actor authority, document-byte correspondence and complete
lifecycle acceptance remain to be implemented and verified.

The companion `validateLifecycleTransition` now requires explicit evidence sets
for accept-ownership, submit-for-decision, record-decision, record-publication,
record-implementation, record-verification and close-review. These operation names
are technical contract keys, not native case statuses or clinical routes. Unknown
operations and omitted stages fail. `observedAtUtc` must be a valid UTC observation;
future/invalid event dates and missing rationale are rejected. Ten focused checks
pass. Rejection/defer/withdrawal routing, occurrence initiation, actor authority,
source-byte verification and effect execution remain native implementation work;
these operations must not be approximated by the successful-evidence path.

## Source-grounded holds and native qualification scenarios

The review lane freshly verified and extracted six retained policy, guideline,
approval-matrix, publication-form, local-approval and specialist-pathway sources.
Exact hashes/page/cell/paragraph references and conflicts are retained privately in
`.local/policy-lifecycle/approval-publication-editions/requirements-discovery.md`
and its source-reference/audit files. Captured copies are not confirmed operative.

The resulting implementation requirements are:

- Select a category/scope/topic/action-specific route. Record permission to develop,
  consultation, mandatory committee/officer endorsement, coordinator check and
  final authorisation as distinct purposes/evidence; no universal approver rule.
- The retained policy identifies an external controlled-publication source of
  truth. SharePoint/Teams can host the workflow, but cannot be relabelled the
  authoritative publisher merely because this build runs in M365. Qualify an
  actual publication handoff and receipt; use only an isolated fictional target
  during software acceptance.
- Document edition and native file version are distinct. Minor document editions
  cannot be categorically rejected simply for not being a major native version.
  Freeze actual issued bytes and preserve replacement/withdrawal evidence.
- Retain conflicting guideline edition labels, approval-role/form routes and
  risk-based review-cycle rules as unresolved. Do not select a new review interval
  or reconcile delegations by guesswork. Existing recorded dates remain evidence.
- Signed evidence or an accepted equivalent is an operational route requirement;
  entered actor text or a native approval response does not alone establish it.
  Ordinary-user retention/edit/delete controls need separate proof.

`templates/lifecycle/native-acceptance-scenarios.json` now defines twelve native
fictional scenarios, including all ten stages plus concurrency/recovery and
operator-role acceptance. Every scenario starts not-run with no receipt. It is an
acceptance plan, not a substitute for execution proof. The single registered track
is `ppg_policy_lifecycle_20261017`; native LC-02 remains owned by Workbench. Event-list
qualification will reuse its isolated case and pinned version after handoff rather
than create a competing case or writer.

Current-source check on 17 October: the original controlled-policy QHEPS asset
returned visible Access Denied Error 403 in the existing browser. The route was
stopped; no alternate identity/client or access change was attempted. Exact URL
and native-page evidence remain private in
`.local/policy-lifecycle/current-source-check-20261017.json`. Current operative
source confirmation therefore remains open; retained captures do not resolve the
recorded approval-route/review-period conflicts. Fictional technical qualification
continues independently. A permitted current source or confirmed authoritative
rule is required before enabling the corresponding real operational route.

## Historical checkpoint — before the connected proof of concept, 18 October 2026

The twelve-scenario plan distinguishes bounded native component evidence from
full scenario acceptance. Eleven scenarios now have partial native evidence;
editable submission in this connected cycle remains not run. The connected
fictional Case9-to-Case10 first attempt created a request, durable intent and case,
then held before receipt. That first attempt remains failed and unqualified.
Receipt-only recovery subsequently qualified against the same retained Case10,
creating only the missing receipt; identical replay qualified with zero writes.
This selected recovery proof does not establish canonical fresh-first success,
permanent generic next-review entry or the remaining adverse/recovery branches.

No scenario has been promoted to full acceptance: every final scenario receipt
remains null and fullCycleAccepted remains false. Original expected/adverse
requirements and earlier recovery evidence are preserved in the existing scenario
ledger, with the actual Case10 recovery audit and explicit limits appended.

Separate stopped qualification flows and administrator-run examples do not yet
constitute one usable complete operator cycle. The current principal is a site
administrator; see [access qualification](lifecycle-access-qualification.md).
The original generic initiation flow was restored Off; temporary next-review
qualification did not permanently install that operator route. The retained
next-date/rule evidence is explicitly fictional and establishes no operative
review interval, real review date, accepted role or policy authority. Fixed
fictional replacement/withdrawal receipts preserve history but do not establish
real clinical publication or retirement.


## Current implementation reconciliation — 18 October 2026

The connected fictional PPG proof of concept is user-accepted. A separate following
occurrence then completed its own editable draft, consultation/readiness, purpose
records, issued-copy proof, implementation/verification and closure. Closure wrote
once and exact replay wrote zero; its next occurrence was created once and replay
created no case or request. Predecessors, edited/issued bytes and source catalogue
were preserved. This proves the recorded fictional positive path, not full-system
or real policy acceptance. Native snapshots describe their execution time; they
are not a fresh claim about current flow states or authentication.

The native offer/Declined response and replay also preserve an unaccepted case.
An actual selected-row projection refused that Declined/Open response before its
journal, case update or commit. Do not repeat this branch merely because an older
scenario entry listed native decline as missing. Other adverse combinations remain
subject to their own evidence.

The current implementation queue remains WB-04 second distinct PPG completion,
WB-05 selected adverse/recovery windows and WB-06 permanent multi-source re-entry.
Two-policy context and producer handoff source composition is prepared and locally
checked, including reproducible create-only outputs; native save/readback and
execution are outstanding. Source preparation never satisfies native acceptance.

The twelve-scenario ledger retains all expected/adverse requirements and null
final scenario receipts. Its remaining work now distinguishes genuine native gaps
from already verified connected behaviour, optional production document-generation
eligibility, real policy decisions and user-deferred ordinary-user adoption.
No ordinary-user, real publication, operative review interval or actor authority
claim is made. `fullCycleAccepted` remains false. The maintained-template manual
fallback remains usable while preferred production generation is unqualified.
