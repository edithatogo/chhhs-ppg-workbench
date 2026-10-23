# Full Dataverse migration proposal

> 23 October current [reviewed partial closeout](dataverse-closeout-20261023.md): discovery works; four environments are visible, including separately owned ALM/Word test targets. Earlier expired-session and no-PPG-container statements below are dated history, not current target-selection evidence. No migration driver or target is established.

16 October 2026 proposal, refreshed 22 October 2026 Brisbane. Status: reviewable proposal; a bounded current
Developer candidate inventory is available. No target is selected and no native
migration is authorised by this document. SharePoint remains operational.

The user selected a full migration proposal. The recommendation is to migrate the
workbench's structured records and workflow state in stages while retaining
SharePoint as the document/version-history service. This is a proposed hybrid
architecture, not a completed migration or a plan to move only the easy records.
The full operational scope below includes events, history, identity, sync,
permissions, document references, forms, reporting and recovery.

## Current discovery refresh — 22 October 2026

Supported PAC enumeration now succeeds under the existing Queensland Health profile and returns the organisation and existing Developer candidates. The default environment solution inventory is accessible. No profile, permission or environment was changed. This supersedes the earlier enumeration-expiry observation below; those earlier details remain dated evidence. No PPG target/solution is selected, and no demonstrated Lists limitation currently justifies migration or cutover. Retain the functioning SharePoint system and this proposal. Exact region/capacity/licensing/security and isolated solution qualification remain necessary if an actual migration driver is established. Discovery is not production entitlement or migration acceptance. Private current receipts are in `.local/artefact-recovery/20261021-native/pac-*`.

## Decision and expected value

Qualify an existing non-production Dataverse environment before designing a
production cutover. Preserve the current workbench until equivalent behavior,
source fidelity, access and recovery are demonstrated. Do not choose the default
environment merely because PAC currently points to it or use another project's
solution because it is visible.

The candidate benefit is enforceable relationships across cases, document identities
and event records, with explicit ownership and access behavior. This is a hypothesis
to test against the existing Lists workflow, not evidence that Lists is failing.
Record the actual relational/security/operating limitation, a reproducible example
and the desired outcome before recommending that production migration is worthwhile.
If no demonstrated benefit outweighs the operating cost, retain SharePoint and keep
the prepared migration path without cutover.

## Destination discovery and solution decision

The local PAC auth inventory has two cached Queensland Health profiles: an
organisation environment and a separately named Power Pages developer environment.
These are discovery candidates only. The authenticated environment enumeration
failed with AADSTS70043 (Conditional Access sign-in-frequency expiry), and device
sign-in renewal was opened in @Browser. Cached profile names/URLs are not a current
list of accessible environments or proof of suitability. Other-organisation
profiles are excluded from this proposal. Exact bindings and raw receipts stay in
`.local/dataverse-migration/`.

Conductor's supported alternative is the existing PPG native owner's qualified
same-origin Dataverse read session. Its private receipt
`developer-candidate-inventory-20261016.json` records successful current solution,
publisher and own-role reads. No PPG-named solution matched the scoped query;
other naming conventions were not exhaustively excluded. Returned publishers
included defaults, Microsoft and a different clinical workload. None is selected
as the PPG migration container. The account's System Administrator and Basic User
roles establish those assigned roles, not least-privilege parity or licensing.
Region, capacity and production entitlement remain unqualified.

The reviewable candidate for a **fictional development pilot only** is the existing
PPG Developer environment, `PRIVATE-DEVELOPER-ENVIRONMENT-URL`, environment ID
`PRIVATE-NATIVE-BINDING-01`. This is not a production destination
recommendation. Exact target confirmation is required before writes. After that,
qualify actual environment type/region/capacity and an isolated PPG solution and
publisher; collision-check proposed names/prefixes before selecting them. Do not
reuse another workload's publisher or modify the existing Word flow. No purchase,
role grant, environment creation or production cutover is implied.

Conductor recommends one distinct container proposal: solution unique name
`CHHHSPPGWorkbenchPilot`, display name `CHHHS PPG Workbench — fictional migration pilot`,
and dedicated publisher proposal `CHHHSPPGWorkbench` with proposed prefix `chppg`.
These are proposed names, not existing IDs or qualified physical names. Check exact
solution/publisher unique-name and prefix collisions, then verify actual publisher
creation/readback before deriving table names. Use solution-first SDK/PAC operations
and retain solution export/unpack and reversal proof. A display name containing
Developer is not independent proof of environment type, capacity, expiry or eligibility.
Complete supported read-only classification before metadata creation; preserve all
unrelated native objects and the operating SharePoint source.

The user commission supports a comparative fictional technical experiment:
create parent/child identities and event references from the maintained fixture,
read back exact values/relationships, exercise duplicate/orphan rejection and
interrupted-write recovery, and compare preservation with the source fixture.
Retain separate raw and normalized target exports and a solution export/unpack.
A successful experiment supports only technical feasibility. The actual Lists
limitation and benefit still need evidence before production migration is recommended.

| Decision | Current state | Evidence needed |
|---|---|---|
| Migration driver | Candidate relationship/security benefit; limitation unspecified | Actual failing/awkward task and desired measurable outcome |
| Pilot environment | Current PPG Developer candidate reads succeed; target not selected | Exact target confirmation; actual type/region/capacity qualification |
| Production environment | Not selected | Intended operating boundary, access, capacity and recovery qualification |
| Solution/publisher | Scoped query found no PPG-named solution; none selected | Distinct PPG container, collision-checked names/prefix and component ownership |
| Document storage | Propose retaining existing SharePoint library | Native reference, version/history, editing and access parity |
| Source writers/cutover | Existing SharePoint path retained | Explicit writer handoff, reconciliation and rollback rehearsal |

## Target model and field rules

Use [the maintained mapping](../config/dataverse-migration.json) as the declared-schema
inventory. Refresh it from exact native schema exports before implementation.
Names here are conceptual roles, not permanent prefixed Dataverse logical names.

| Component | Target treatment | Acceptance rule |
|---|---|---|
| Catalogue | SourceDocument with original DocumentUID | All25 source fields, raw values, acquisition and identity provenance preserved |
| Review queue | ReviewCase with original CaseUID | Local status, role proposals, next action and dates preserved verbatim |
| Case/document association | Explicit relationship/link representation | Every supplied existing link accounted for; unknown links remain exceptions |
| Three event histories | Separate readiness, assurance and consultation event tables | EventUID namespaces, original case/version/hash, human assertions and correction history retained |
| Evidence references | File identity/URL/version/hash and existing edition/currency assertions | Blank/unconfirmed remains unresolved; captured Approved never becomes current by migration |
| Raw documents/history | Retain existing SharePoint library and issued/edit history | Actual file links/downloads/editing/access verified from target workflow |
| Identity aliases/decisions | Migrate operational identity state only through an explicit verified mapping | Existing accepted ledger/history retained; no inferred new identity or automatic retirement |
| Import checkpoints | Preserve old checkpoint; create target checkpoint only after verified commit | Interrupted writes/retry cannot advance success falsely |
| Historical list versions/authorship | Preserve original audit evidence separately from new Dataverse execution metadata | No fabricated historical actor, timestamp or native audit event |

Dataverse row GUIDs are separate from preserved business identifiers. Verify actual
alternate-key activation and lookup/navigation names. Imported choice codes require
an explicit label/code crosswalk; unknown values hold the affected import. Preserve
month precision and raw Excel dates independently of date-only/UTC columns. Do not
convert null, absent, unrecorded and Not applicable into one state. Preserve originals
of human-edited text and all source fields, including those omitted from current views.

Deletion/cascade behavior must be explicitly constrained for document/case/event
relationships. Test orphan refusal and recovery on fictional data; never delete
original records to make counts agree.

## Security and history

Translate required behavior from actual existing access; do not copy site membership
into new roles automatically. The following are capability proposals, not user or
role assignments:

| Capability | Proposed minimum boundary | Required proof |
|---|---|---|
| Source ingestion | Write mapped source facts and checkpoint only | Cannot change case decisions or human findings |
| Case preparation | Read source facts; maintain permitted local case fields | Cannot modify source identity or turn a proposal into approval |
| Human event recording | Record authorised event assertions and linked corrections | Exact reviewed version retained; no fabricated sign-off |
| Evidence navigation | Follow only accessible SharePoint file references | Dataverse access does not widen SharePoint document access |
| Schema/operations maintenance | Existing authorised maintainer route | Deployment privilege separate from ordinary data use |

Inventory effective roles/teams/ownership, column protections, sharing, retention,
audit and DLP needs before configuring them. Test actual allowed and denied reads
and writes with existing authorised principals; do not grant access solely to make
a test pass. Access parity is separate from data-count parity. The original system
stays available until each intended workflow meets its required access boundary.

Keep original SharePoint version history/audit and source timestamps as original
evidence. New import execution timestamps/actors must remain distinguishable.
Do not present imported historical rows as recreated native Dataverse audit history.
Record any history that cannot be represented as native metadata as preserved
readable evidence with explicit limitations; an unresolved mandatory history
requirement blocks cutover.

## Delivery stages and evidence

| Stage | Concrete output | Exit evidence |
|---|---|---|
| 1 Discovery | Environment/solution/driver decision and current source inventory | Successful scoped reads; exact source/table/file/history counts and required behavior |
| 2 Design | Approved physical mapping, keys, relationships, choices, ownership and document-reference plan | Every source field/state and technical artifact mapped or explicitly retained |
| 3 Fictional pilot | Isolated components inside selected solution; representative fictional parents/children/events | Actual create/readback, denied operations, duplicate retry, edit preservation and rollback |
| 4 Migration rehearsal | Consistent source export, target import and independently exported target projection | Exact values/counts/links, history/files/ACLs and flow/application/report parity |
| 5 Cutover readiness | Rehearsed writer transition and restoration plan | Measured runtime, acceptable recovery window, current backup/restore qualification and no unresolved required gaps |
| 6 Scoped cutover | Explicitly authorised switch of one writer and consuming paths | Final delta parity, actual workflow outputs, access verification and rollback availability |
| 7 Observation/retention | Operating evidence and retained source history | Agreed observation outcomes met before any separately authorised retirement |

No stage is complete from a checklist alone. Existing offline checks demonstrate
only supplied normalized values/declared links; [the current checker](../scripts/ppg_dataverse_reconcile.py)
does not implement source exports, target writes, native security or completeness.
Add those adapters only for the selected physical schema, using existing qualified
Dataverse tooling and the assigned native writer. Export/unpack actual solution
metadata back into the repository after changes.

## Import, consistency and repeat safety

Establish a source inventory and snapshot identity including table/file/history
counts, hashes, ETags and export time. A table scan while people edit is not an
atomic cross-List snapshot; use an agreed consistent capture/final-delta boundary
and verify it. Account explicitly for unresolved identities before selecting rows.

Import parents/keys before associations and events, then retain the original event
ordering evidence. Persist a private source-identity to target-row mapping and
per-batch receipts. Verify committed rows with a target export rather than relying
on the import's success response. Advance a target checkpoint only after all
required writes/readback for that operation succeed. Retry with persistent identity;
do not duplicate events, overwrite a concurrent edit or treat a missing source row
as retirement. Use supported [optimistic concurrency](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/optimistic-concurrency)
where needed and prove conflict handling on the actual target tables.

Validate case preparation, human event recording, evidence download/editing,
source refresh, comparison, reporting, template/assembly inputs and Teams navigation
against the new paths. Preserve existing outputs and four-tab navigation until
replacements work. Do not infer a working application from successful table import.

## Cutover and rollback runbook proposal

1. Agree source snapshot/final-delta boundary, roles performing the existing work,
   tolerable interruption and recovery objectives. Record actual values after the
   rehearsal; no downtime/RPO/RTO claim is supplied by this proposal.
2. Preserve source backups/exports, document/version history, flow definitions,
   target solution package and current bindings. Verify the chosen environment's
   [backup/restore support](https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments)
   and rehearse recovery; a saved export alone is not restore proof.
3. Stop the existing source writer at the recorded boundary only under the scoped
   cutover instruction. Capture final deltas and verify target parity before
   enabling its writer. Do not run simultaneous uncontrolled source/target writers.
4. Switch named consuming paths, execute representative native operations and
   inspect records/files/links/access. Keep approval/publication states unchanged.
5. If parity, access, event history, flow execution or recovery fails, stop the target
   writer, preserve post-switch target changes and their receipts, and restore the
   prior bindings. Reconcile those target-only changes before resuming source work;
   otherwise rollback would lose new human work. Do not blindly replay both sides.
6. Retain the source and all history during observation. No deletion, archival,
   notification or broader deployment follows automatically from a successful run.

## Cost, effort and open decisions

The existing roadmap supports2–4hours of scoping; it does not support a credible
full migration total yet. Price and schedule only after environment access, current
volumes/history, existing licences/capacity, schema and recovery constraints are
known. Separate maker/user/service licensing, database/file/log capacity, flow
connectors, retention and ongoing operations. No purchase or capacity assignment
is proposed as an action here.

The next concrete result is selection of the inspected fictional pilot candidate,
followed by qualified PPG container/capacity/security and a native execution plan. The remaining business
input is the Lists limitation/outcome that justifies migration. Once those are
resolved, revise the mapping into exact target components and produce the fictional
pilot execution plan; do not mark the migration delivered from this proposal.
