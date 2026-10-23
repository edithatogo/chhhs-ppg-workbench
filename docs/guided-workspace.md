# Guided workspace and case navigation

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

This increment uses existing SharePoint forms, Lists and managed Start Here
navigation. It adds no application, licence requirement, tab or notification.
See [delivery scope](usability-delivery-plan.md). Exact native evidence and bindings
are retained privately under `.local/usability/uw/`; current delivery is recorded
in the [track plan](../conductor/tracks/ppg_guided_workspace_20261017/plan.md).

## Five tasks

| Task | Input and supported route | Result |
|---|---|---|
| Find a policy | Policy identity and source view: search by source title, then confirm DocumentUID. Use the captured-policy/edition views for reference copies. | Source identity and provenance; currency may remain unconfirmed. |
| Open a case | Case workspace: open an existing case by CaseUID and check its linked DocumentUIDs. Use native New only when starting authorised work; supply a genuine unique CaseUID. | Source context, proposed work, review status, draft and event links. |
| Prepare a package | Download the existing assembler HTML and open locally; supply recorded metadata and actual files. | A new DRAFT ZIP and missing-items report. Download/manual preparation, not a Teams execution button or submission. |
| Record a review | Open the case and its CaseUID-filtered readiness, assurance or consultation history. Record only actual findings against the exact document version/hash. | Human findings and implementation evidence; blank history means not recorded. |
| Resolve an exception | Follow the existing identity guide for holds; use missing-input, target-check and ownership-handoff views for follow-up. | Evidence-backed resolution or visible pending/held state. No automatic identity, ownership or date decision. |

## Case form and landing

The form groups all existing human-editable fields into case/source context,
proposed work, review recording, and evidence/implementation records. Native
readiness, assurance and consultation links are filtered by CaseUID. These are
case histories, not automatic new-record defaults: verify CaseUID/document/version
and hash when recording a new event. No field is hidden, made read-only or required
by the presentation. Form grouping is not a security boundary.

Case workspace and target-check views show the recorded next action, role, target,
source and draft. A missing value is explicit. Only source/draft URLs within the
bound workspace become clickable; other references remain visible for verification.
The source catalogue remains the importer-owned source of facts. A CaseUID must
not be confused with a linked DocumentUID. No case is resolved from a title alone.

The retained example's separately hosted dated navigation guide links its exact
source snapshot, working draft, frozen comparison, case histories and verified
existing-artifact archive/receipt pair. A verified archive is an integrity result,
not approval or proof of historical authorship; generation receipt remains unknown
where absent. No other case inherits that example's package or receipt. Future
cases with no recorded package must show that absence, never a guessed latest file.

## Follow-up and dates

- Case workspace: all recorded cases with action/context and case-specific links.
- Missing action or evidence: records lacking an action, source snapshot or draft
  reference. Presence alone does not establish evidence adequacy or valid content.
- Targets and follow-up checks: all recorded targets with strict calendar checks.
  Only real `YYYY-MM-DD` dates receive past/current classification, using Brisbane
  day boundaries. Past ISO text says **confirm agreement**, never proves an agreed
  deadline. Pending conditions, month-only values and invalid dates are not overdue.
- Ownership offered/not accepted and outstanding conditions reuse the existing
  consultation views. Proposed case roles do not establish accepted ownership.
- Identity holds retain the existing source-status and identity-resolution paths.

No background update is introduced. Date labels evaluate when the view renders;
reload to refresh. Existing default views and unrelated views remain available.

## Maintenance and evidence

`config/guided-workspace.json` defines the five tasks and view queries;
`config/guided-workspace-form.json` holds the form layout with a private workspace-path placeholder; resolve it with `bind_form` before native application.
`scripts/ppg_guided_workspace.py` builds only presentation JSON and classifies dates;
it has no tenant writes. Native deployment uses the existing qualified M365 route.
Native custom-format serialization must escape XML-sensitive characters within
JSON before submission using `formatter_json`; decode/read back and check rendered expressions afterward.
Keep previous formatter/page preimages, exact bindings and native receipts privately.

Native verification must include rendering, actual routes, keyboard navigation,
repeat adoption and preserved originals. Local date checks do not prove native
rendering. Teams desktop acceptance remains closed by the user's confirmation;
this increment uses supported Teams web/SharePoint verification. It does not prove
another user's access from the operator session.

## Completed fictional PPG walkthrough — 18 October 2026

Open the existing **PPG — Start Here** page in the M365 workspace and choose
**Completed fictional PPG walkthrough** near the top. The first link opens the
closed fictional review. Its draft/evidence link and three filtered evidence
links show the Word draft, consultation/readiness and decision/implementation/
verification records. The second link opens its separate initiated next review.
Closing the previous occurrence does not complete that new occurrence; neither
example establishes clinical issue authority. This is a read-only walkthrough,
not an instruction to run the historical case-specific closure branch.

Qualified M365 CLI saved and read back page version 30.0: all 17 controls retained,
16 unrelated controls unchanged, exact repeat content unchanged. Current native
case reads confirm the linked example is closed and the next review initiated;
both complete case snapshots remained unchanged after the page update. No case,
draft, workflow, authentication, permission or business-status mutation occurred.
Private preimages, target controls and receipts are retained in
`.local/usability/poc-walkthrough-20261018/`. Browser rendering and another user's
access have not been demonstrated by this CLI save/readback.

## Reproduce the PPG example

Use the existing PPG workspace. No meeting, meeting pack, new channel or channel
selection is needed. The user has accepted the fictional proof of concept;
that acceptance does not establish another user's access or real policy authority.

First walk through the retained example from **PPG — Start Here**. Open the
completed fictional review, follow **Open draft and evidence**, then its three
filtered evidence links. Finish by opening the separate next review. Keep these
retained examples intact; use fresh fictional references for another run.

The demonstrated sequence for a new fictional occurrence is:

1. Initiate the PPG review using the existing initiation operation and a unique
   occurrence reference. Confirm the new case and source/document identity.
2. Record an ownership offer and explicit acceptance through the existing
   ownership forms; confirm the accepted record and its case projection.
3. Prepare a separate Word draft, open/edit/save it, and retain its exact revision
   and technical preparation evidence. Select that draft on the new case.
4. Record consultation and readiness for that exact prepared revision. Retain
   responses, conditions and supporting evidence; do not carry them from another
   version or infer acceptance from the presence of a file.
5. Record the purpose/decision evidence, publication representation and independent
   document-byte proof, followed by implementation and positive verification.
   Fictional entries demonstrate recording; they do not issue a clinical policy.
6. Use the connected PPG closure operation once its prerequisites resolve. Confirm
   the closed case and closure receipt. The historical case-specific **Close
   review** branch is not the connected example's entry point.
7. Use the existing initiation operation's next-review route against the completed
   occurrence's closure trace. Confirm a separate initiated case. An identical
   retry must reuse the committed result rather than create another occurrence.

These steps ran on the retained connected fictional example. They are a sequence
to reproduce, not a claim that every operation is already a general one-click
service. Before running a new occurrence, the lifecycle owner must confirm the
current operation bindings, prepared-version/evidence selection and supported
runtime trace inputs for that occurrence. Runtime verification-parent selection
is being qualified separately by that owner; do not reuse a case-specific binding
or replay old example inputs to work around it. Repeatable setup/packaging and
ordinary-user access remain technical follow-up, not a request to choose a meeting.

The lifecycle owner reports that the native walkthrough renders correctly in the
current account. This supplements the CLI page readback; ordinary-user access
remains unverified. This documentation increment performs only a fresh page read
and changes no native page, case, flow, document, permission or authentication.

## Existing-access inventory — 18 October 2026

A later GET-only inventory used the existing qualified CLI connection. It read
the site role assignments, four SharePoint group rosters, case/evidence/
consultation/readiness/assurance permissions, both fictional case items and
edited drafts, the actual preparation folder and the published guide. All five
resources and those specific items/files inherit their containing permissions;
no item-specific restriction was observed on the examples. Read/Edit/Full Control
group bindings exist; five direct site grants were Limited Access only.

One existing membership account is explicitly listed in the Edit group and is
marked non-site-admin. This supplies an existing SharePoint membership route for
a read-only walkthrough, not proof of that person's intended business role,
effective access or execution. Nested directory-group rosters were not expanded,
so this is not an exhaustive list of potential reviewers. Another non-admin flag
belongs to a non-membership principal with Full Control; it is not classified as
an ordinary reviewer. Personal identities and exact native bindings stay private.

For all twelve identified connected-cycle manual Button flows, the complete
native permissions collection returned exactly one Owner grant, matched to the
current account through the qualified Graph self-read. No additional principal
or run-only grant appeared in those collections. No existing non-admin reviewer
is therefore established as able to run the lifecycle forms. This is an ACL
observation, not a tested denial, a claim about every possible tenant-admin route
or proof that a form executes with the intended actor/connection.

The simplest next step using existing access is a read-only walkthrough by the
existing authorised non-admin Edit account in its own normal session: open Start
Here, the guide, a case, its draft and filtered histories. No invitation, sharing
change or alternate-person sign-in was performed. Flow recording remains with
the existing owner until an intended reviewer has an independently confirmed
run-only route; any grant would be a separately scoped permission change. Maker
development does not need to wait for that operational walkthrough.

Event lists still report ReadSecurity1/WriteSecurity1 with inherited Edit. Their
append-only recording convention and guarded flow creates do not prove that
ordinary users cannot edit/delete records or change evidence. Actual permission
enforcement and ordinary-user execution remain open acceptance. This inventory
changed no permissions, accounts, source, case, document, flow, status or auth.
Raw role/member/flow receipts and the sanitised summary are retained under
`.local/access-inventory/20261018/`. An initial unsupported bare Graph request
was corrected once using the CLI's explicit Graph resource; an incorrect folder
lookup was corrected from the actual draft link. Neither was an access denial.
The frozen v1.0.0 documentation baseline and its hashes remain unchanged.

The smallest proposed change, if the existing Edit account is confirmed as an
intended reviewer, is run-only access to the specific manual forms needed for
one fictional task, followed by its stored-result/retry check. Keep existing
flow owners unchanged and avoid granting maker/co-owner rights for execution.
The twelve read definitions currently report Embedded connection references.
An owner must deliberately choose whether the trial uses those existing embedded
connections or the reviewer's own connection through Provided by run-only user.
The lowest-change technical trial retains the existing connection only where
its authority and actor-attribution boundary are explicitly acceptable; that run
would not prove least-privilege writes as the reviewer. If the test must prove
the reviewer's own SharePoint write boundary, qualify a user-provided connection
and its existing licence/environment access instead. Neither choice, run-only
grant nor reviewer selection was applied by this inventory. Microsoft documents
these separate controls in [Share a cloud flow](https://learn.microsoft.com/en-us/power-automate/create-team-flows).


## Ordinary-user trial using existing access

Deferred to later adoption by user instruction; no reviewer has been asked.
These steps remain instructions for that later trial, not a current implementation
gate or completed observation. The reviewer must use their own normal session.
Start Here supplies the current workflow guide and completed fictional review;
retain tenant links and respondent identity only in approved private records.

| Check | Evidence to retain privately | Limit |
|---|---|---|
| Open Start Here and workflow guide | Actual page result and observation time | Owner rendering or group membership alone is insufficient. |
| Open completed fictional case and draft | Matching case/document identity and successful read | View only; preserve the completed draft and its edits. |
| Open its three filtered histories | Correct case filter and actual returned records | Do not infer unrestricted access or record immutability. |
| Open an existing lifecycle recording form | Actual available/unavailable/error result | Do not submit during the current native writer's operation. Form visibility is not execution proof. |
| Record a separately allocated fictional task and repeat | Actual reviewer session, permitted connection route, retained result and duplicate-free retry | Only after its exact fixture and native writer are free; no grants or connection changes are part of this trial. |
| Coauthor/comment and recover a draft | Actual edit/save/reopen and preservation of prior edits | Use an allocated unissued trial draft, never the completed review's retained evidence. |

Use the existing operator observation CSV for actual attempted outcomes, with
blank timing/help fields where unobserved and an exclusion reason for held work.
Keep read-only success, write/run acceptance, coauthoring and least-privilege
claims separate. If a form is unavailable, retain the exact operation/error and
existing ACL evidence, then hold that recording task. Do not impersonate the
reviewer, add run-only/co-owner permissions or treat an embedded owner connection
as proof of the reviewer's own write boundary. Any future access change requires
its own explicit authority. Current native development can continue independently.


## Simplified landing page — 18 October 2026

User feedback identified Start Here as too crowded. Its existing URL now retains
only a brief introduction and five task links: Find a policy, Open a review,
Evidence and drafts, Monthly reports, and Guides and tools. Detailed instructions,
examples, status and maintenance information moved to the linked Guides and tools
page, with a return link. All prior controls and links were preserved there before
the landing change; the prior landing version and exact preimage are retained.

Native save/readback and repeat confirmed landing32.0 and secondary1.0. Reloaded
browser rendering showed exactly five task links. The same workspace, list/library
routes and permissions are reused. No case, source, flow or approval was changed.
This fixes navigation density; actual non-admin access, coauthoring and recording
acceptance remain unverified. Private page preimage and receipts:
`.local/usability/landing-simplification-20261018/`.


## Adoption timing — user clarification

The user clarified that no reviewer had been asked and moved all third-party
review to a later adoption step. The trial instructions above remain available
for that later use; they are not a current implementation prerequisite or evidence
that any ordinary-user test occurred. Keep access/execution/coauthoring unverified.
No invitations, participant requests or permission changes are required now.
