# Native recovery and technical reporting qualification — 21 October 2026

The reusable lifecycle is complete at `3f72e6b`: two fictional end-to-end cycles,
72 distinct cycle runs and 18,600 action records. Earlier dated progress entries
that leave RR-04/05 open are historical checkpoints, superseded by the terminal
[handoff](../conductor/tracks/ppg_reusable_lifecycle_routes_20261020/handoff.md).
The wider production lifecycle and deferred ordinary-user testing keep their own
scope; do not rebuild the qualified cycles.

## Published technical result

The secondary PPG Technical Usability page (exact URL in the private publication receipt)
was published at version 1.0, read back and rendered in the current signed-in
browser. All metrics and qualification limits match the generated source.
Start Here was preserved; the page is not promoted as news. Six safe refusals
contribute a separate 1,503 action records. All nine original profiles were
unchanged and Started at the lifecycle checkpoint, with no runs in flight.
The 50 local tests belong to that checkpoint; the reporting increment separately
passes 15 reporting/observation tests.

Real-user sample is zero. Time saved, reviewer effort and clinical benefit remain
**not measured**. Ordinary-user testing is user-deferred. A technical pass does
not confer clinical approval, operational adoption or publication authority.

## Native copied-record and artifact recovery

Two new explicitly fictional cases demonstrate export-to-new-record recovery.
The original's later human edit remains intact. The restored case has a distinct
CaseUID and native identity; every declared recoverable field and evidence link
matches the exported snapshot. All 23 prior cases were preserved; the resulting
25-case count is a new checkpoint, not a correction of the earlier lifecycle count.
Read-only resumed adoption found the existing recovered identity and added no
records. Server-enforced unique CaseUIDs remain in place.

Record metadata MERGE with an outdated HTTP ETag returned **412**. Captured
conditional request headers and independent readback confirm no stale mutation,
version advance or lost human edit.

On an isolated fictional file copy, native RestoreByLabel recovered version 1.0
as current version 3.0; historical edited version 2.0 remained readable. The
independently downloaded edited export was also recovered into a separate new
file using `overwrite=false`; its bytes and hash match. Original files remain
unchanged.

**Excluded route:** a deliberately stale binary-content PUT was accepted (204)
and advanced only the disposable copy to version 4.0. Its effects were reconciled;
versions 1–3, the original and the separate recovered export remain intact.
This adapter/endpoint is not qualified for conditional content updates. Do not
use it to overwrite an edited or issued file. Use create-only recovery into a
new identity, verify bytes and links, then let the existing owner decide whether
to adopt it. Record metadata concurrency proof does not qualify file-content CAS.

## Continuity and visible controls

Existing `caseStatus`, `accountableRole`, `proposedOutcome`, `nextAction`,
`sourceBaselineRef`, `linkedDocumentUIDs` and `evidenceDraftLink` are sufficient.
The fictional cases explicitly record local completion/upstream publication
pending and an **unaccepted** responsible role. Preserve the edited original and
issued history. A custodian handoff must retain source and output versions,
evidence hashes, completed local work, outstanding upstream action, responsible
role acceptance and next action. An unsent handoff is preparation, not acceptance
or permission to update the authoritative register.

Native inspection confirms versioning on the queue and evidence library, with
major-version limits 50 and 500 respectively. Both inherit permissions; the
fictional file also inherits. Minor versions, moderation, forced checkout and IRM
are false on the inspected objects. Selected compliance fields were omitted from
the fixture response: this does **not** establish absence of tenant retention.
No labels, locks, grants or configuration were changed. Full Purview policy,
ordinary-user effective access, backup service and RPO/RTO remain unqualified.

## Restart procedure and dependency handoff

1. Identify the existing writer, exact object, environment and current principal.
   Refresh the affected definition/state, record identity/version/HTTP ETag and
   file metadata/bytes. Preserve raw exports privately; never export credentials.
2. Classify the last attempt from its saved intent, transport and outcome. An
   absent dispatch receipt is distinct from an unknown post-dispatch result.
   Reconcile native state before any retry; never blindly rerun a creation.
3. Match the full existing CaseUID and declared field mapping. Adopt an exact
   recovered copy read-only. A changed original is retained, not reset.
4. Recover files create-only into a fresh identity from verified bytes. For a
   native version restore, operate only on the authorised disposable copy and
   inspect current and historical versions afterwards. Exclude binary PUT CAS.
5. Read back identity, fields, links, output hash/version and preserved originals.
   An annotation-only difference may exclude only the observed per-response
   `odata.id`; do not normalize business fields, versions or ETags.
6. Retain local-complete/upstream-pending until the existing custodian actually
   accepts and performs the authorised upstream step. Keep the handoff unsent
   unless sending is separately authorised. Record operational support ownership
   as unaccepted where it has not been demonstrated.

Flow dependencies remain the original nine r6 profiles and their existing
connection references. A raw flow export is not a solution export, a connection
reference is not a credential, and a source bundle excludes operational records
and SharePoint files. The newly exposed FlowAgent route reports missing Azure
sign-in; its solution-context warning `no-dataverse-instance` makes returned
`inSolution=false` inconclusive. Do not migrate or mutate originals based on it.
Retain existing manual provisioning until exact solution and restored-flow proof
is available through a qualified route.

### Final readback and export correction

Fresh raw GETs of all nine profiles match the terminal r6 definitions, connection
references, state and modification time exactly; all remain Started. No new run
or flow mutation was required. The current native details page identifies the
existing owner and SharePoint connection, with no run-only sharing. This is
current-account dependency evidence, not delegated-user execution or credential
backup. The bounded record/file recovery walkthrough above supplies the technical
restart exercise; operational support acceptance remains explicitly unaccepted.

The installed CLI uses **POST**, not GET, for `exportToARMTemplate`. The earlier
GET 404 was a method error, not an entitlement denial. One guarded supported POST
returned 200 and 194,237 raw bytes. The retained export parses as an ARM template
with `Microsoft.Logic/workflows` and `Microsoft.Web/connections`, exported Disabled.
Its connector/action representation differs from the original Power Automate
definition. Original definition, references, state and modification time remain
exact after export. This qualifies native export at that format only: it is not
a Power Automate solution package or a qualified round-trip import. Do not deploy
it to Azure as a substitute. Native Save As remained Loading, but subsequent complete native inventory found
one new Stopped copy. The loading UI did not establish failure: independent GET
confirmed a distinct native identity, the exact original definition, existing
connection references and creator, and an empty run history. All nine originals
remain unchanged and Started. Do not repeat Save As. List and detail surfaces
report creation timestamps in the same second with a small difference; retain
both rather than claim timestamp equality. This qualifies supported native
copy recovery while the source exists, not deleted-source recovery, solution or
cross-environment import. No copy invocation or new connection was needed.

The final complete library comparison retained all 3,231 pre-existing rows:
3,229 compare exactly apart from per-response `odata.id`; two changed outside
the recovery fixtures. The source-state file advanced 168.0 to 169.0 with only
`checkedUtc` changed in its JSON. An existing image acquired image tags and an item
ETag change while its native file stayed 1.0. These differences were reconciled
read-only and preserved, with attribution unestablished. Do not claim a globally
unchanged library or roll back concurrent/platform updates. Six additional rows
are the new recovery folder and its five fictional artifacts.

Private raw proof: `.local/artefact-recovery/20261021-native/`, including
`record-recovery-audit.json`, `file-recovery-audit.json`,
`stale-binary-probe-reconciliation-audit.json`, `visible-controls-audit.json`,
`technical-page-published-audit.json` and `tool-readbacks.json`.
Additional final receipts: `continuity-handoff-audit.json`,
`dependency-final-audit.json`, `native-export-audit.json` and
`final-library-preservation-audit.json`.

Native flow-copy reconciliation is retained in `native-flow-copy-audit.json`. The initial Loading-only interpretation is superseded by that native readback.

## Configuration restoration and source release recovery

The new Stopped fictional copy was subsequently used for an actual fault/restore
exercise. A guarded PATCH added only one fictional Compose action. Independent
native readback verified that exact change. A second guarded PATCH restored the
configuration from the separately frozen raw source export, preserving the copy's
identity, creator, display name and existing connection references. The copy stayed
Stopped throughout and both run-history checks were empty. Fresh final reads of
all nine original profiles again match their frozen definition, references, state
and modification time exactly; all remain Started.

Each management PATCH had an exact target/body digest, one-send guard and no
redirects. The management preimage check is **not atomic concurrency protection**;
this exercise used an isolated copy with no competing writer. Do not generalize
it into a production overwrite procedure or the excluded binary-content route.
Restoration used the raw Power Automate snapshot, not the converted ARM template.
It qualifies configuration recovery into this existing stopped target; it does
not qualify recreation after every target is deleted or cross-environment import.

For a repeat, identify and reserve the isolated stopped target, retain its current
raw preimage and an independently verified export, and verify creator/bindings and
empty run history. Reserve restoration time before a fault. Save only to the
reviewed target; after any uncertain result inspect actual native state before
another mutation. Read back definition, references, identity, state, preserved
originals and run history. Activation and operational use require their own proof.

A source release bundle at `2e47327` was independently verified and restored into
a new checkout. Its commit and tree match exactly, and all 31 focused workspace,
inventory, technical-reporting and observation tests pass there. This source
bundle excludes private bindings, native records/files and other uncommitted
work. Raw native evidence remains separate; neither component alone is a complete
operational backup. No remote publication was performed.

Private proof: `copy-config-fault-audit.json`, `copy-config-restore-audit.json`,
`dependency-restored-final-audit.json`, `release-20261022/source-recovery-audit.json`
and `release-recovery-qualified-manifest.json`.


## Canonical solution and membership recovery

The user selected the permanent publisher/solution `CHHHSPPGWorkbench`, prefix
`chppg`, version `0.1.0.0`, in the existing QH Default environment. Current native
privilege readback confirmed create/write/import/export capabilities under the
existing account. No permissions, licences, consent or preferred-solution setting
were changed. The solution is unmanaged. Microsoft documents that Microsoft 365
customers can create standard-connector solution-aware flows where Dataverse is
attached; this eligibility does not establish premium document-generation or
Copilot runtime capacity ([licensing FAQ](https://learn.microsoft.com/en-gb/power-platform/admin/power-automate-licensing/faqs#can-microsoft-365-customers-create-solution-aware-flows-and-child-flows)).

The existing VS Code PAC route initialized and packed an empty solution, imported
it successfully and read back its exact publisher, prefix and version. The native
Outside Dataverse picker then included only the previously reserved Stopped copy.
Its ID, definition, creator and state remained unchanged. Conversion replaced its
embedded connection name with a logical reference; independent Dataverse readback
resolved that reference to the same existing SharePoint connection. This is an
explicit representation change, not raw connection-reference equality.

Actual unmanaged export/unpack contained the expected workflow and connection
reference. The workflow definition matched the frozen native source exactly.
Using **Remove from this solution** removed only membership: the native copy and
connection remained intact. Importing that frozen exported package restored the
same workflow membership and preserved the same flow/workflow IDs, definition,
creator, reference and Stopped state. Run history stayed empty. A second native
export retained exactly the same packaged workflow JSON. This proves supported
same-environment membership recovery; it does not prove recreation after deletion,
cross-environment deployment, managed upgrade or operational acceptance.

After that trial, the nine exact r6 lifecycle profiles were included using fresh
native preimages and individual picker selections. Three older prototypes were
excluded. All nine retain their original flow IDs, exact definitions, creators,
Started states and embedded connection names. They now additionally identify the
same logical solution connection reference. Native membership readback and actual
export reconcile each workflow ID; all ten packaged definitions (nine originals
plus recovery copy) are present, and the export declares no missing dependencies.
The completed 2/2 lifecycle cycles were not rerun. Native connection/definition
readback does not replace a new operational or third-party acceptance exercise.

The first package was a **lifecycle technical release**. The subsequent Default
configuration package extends that exact proof as described below; the Developer
Word pilot remains separately located and qualified.
SharePoint Lists, pages, files, Teams and authoritative publication remain under
their existing provisioning and authority routes. Raw exports and native handles
remain private. Private proof:
`.local/ppg-alm/canonical-20261022/`, especially
`stopped-copy-membership-recovery-audit.json`,
`canonical-original-preinclude-audit.json`,
`canonical-original-postinclude-audit.json` and
`canonical-r6-release-audit.json`; detailed native pre/postimages remain under
`.local/artefact-recovery/20261021-native/`.


### Maintained Default flow coverage

Eight additional exact flow identities were reconciled against existing private
deployment/binding receipts: workspace status, monthly reporting, source importer,
existing cover/package generation, role projection, standards checks, web-guide
reconciliation and follow-up/digest preview. Each had an independent fresh native
preimage before inclusion. All eight retain their flow IDs, exact definitions,
creators, Started states, existing connection names and failure-alert subscription
settings. Added logical references resolve independently to the same three
existing Standard SharePoint, Excel Online (Business) and OneDrive for Business
connections. No new service connection was created and no flow was invoked.

The combined unmanaged export/unpack contains **18 workflow definitions**: the
17 maintained Default profiles and the one Stopped recovery copy. Native solution
membership maps every workflow ID; each exported definition matches its native
readback. The ZIP passes CRC, unique-path and safe-relative-path checks; its
manifest has the selected publisher/prefix/version and declares zero missing
dependencies. These are package checks, not proof that external SharePoint/Excel
resources or credentials are portable to another environment.

PAC generated deployment settings from this actual package: three connection
references, zero environment variables, zero Copilot agents. The unbound settings
and a separate private current-target binding are retained. Never reuse those
bindings against another target without exact ownership/access/readback checks.
The native stopped-copy recovery was tested before including original profiles;
the canonical package is **not** imported over the live originals as an extra test.
The supported manual recovery remains: reserve a stopped copy, freeze/export and
verify, remove membership only, reconcile the native object, import the frozen
package without activation/force-overwrite/global publishing, then verify the
same identity/definition/connections/state, membership and empty run history.

Private release proof: `canonical-workbench-release-audit.json`,
`canonical-workbench-default.zip`, unpacked `canonical-workbench-default/`,
`canonical-complete-membership.txt`,
`canonical-complete-connection-references.txt`,
`canonical-deployment-settings-unbound.json`, the separate private bound settings,
and `terminal-native-preservation-audit.json` under the canonical evidence folder.
The immutable first lifecycle and copy exports remain retained separately.

This closes Default configuration solution membership/export and the tested
same-environment membership-recovery route. Developer Word production,
all-targets-deleted recreation, cross-environment/managed deployment, whole-tenant
backup, SharePoint/Teams provisioning and third-party/operational acceptance are
outside the proof. The existing manual provisioning and evidence routes remain
usable for those separate resources and conditional features.

The new canonical private snapshot was copied create-only to the reconnected
PortableSSD: 285 files, 15,647,173 bytes, with every source/destination SHA-256
verified and originals retained. Credential caches are excluded. Its manifest
and `ssd-backup-audit.json` are retained privately. The earlier 491-file recovery
snapshot remains separate and unchanged; neither is a tenant backup guarantee.


## Managed candidate artifact qualification — 22 October 2026

One managed candidate export of the existing CHHHSPPGWorkbench solution succeeded
through the same qualified VS Code PAC route against the exact QH Default target.
The candidate retains publisher CHHHSPPGWorkbench, prefix chppg and version 0.1.0.0.
It was unpacked locally as Managed. The accepted unmanaged artifact remains intact.
No candidate was imported or deployed, and no activation, publish-all, layer change,
pipeline/host provisioning or permission/licence/consent change was performed.

Both archives have the same 21 unique safe member paths, 18 workflow JSON files,
three connection references and identical component IDs/set. CRC checks pass;
all 18 workflow JSON members and every other non-manifest member match byte-for-byte.
Structural XML comparison found exactly one difference: solution.xml Managed 0
becomes 1. Publisher/version, root components and other manifest content match;
ZIP container metadata may differ. The export declares no missing dependencies,
which does not prove a target's external resources or credentials are ready.

Fresh actual flow-service readbacks preserve all 17 Started profiles and the one
Stopped recovery copy. Definitions, references, creator/workflow identity, trigger
URI, created/modification times and isManaged flags match the prior frozen terminal
snapshot. Independent current connection-reference rows resolve to the same three
existing connections; source solution readback remains Unmanaged 0.1.0.0. No flow
was invoked and the completed lifecycle/recovery trials were not repeated.

Private proof: `.local/ppg-alm/managed-candidate-20261022/`, especially
`managed-candidate-audit.json`, `envelope-differences.json`, export/unpack output,
source solution/connection readbacks, candidate ZIP and `unpacked/`. Detailed flow
readbacks retain the managed-candidate-terminal prefix in the existing private
native evidence folder. The synchronous CLI exposed no server job ID; its actual
tool session/terminal exit 0 and resulting artifact/hash are retained, without an
invented async handle or outstanding-job claim.

This closes the managed **candidate artifact/export** gap only. Managed import,
cross-environment deployment, target-layer transitions, upgrade/uninstall/rollback,
permissions, external resource parity and operational acceptance remain unqualified.
The proven unmanaged/manual route remains available. The conditional-feature goal
is unchanged and blocked; this artifact does not supply production generation or
assistant entitlement.


## Developer Word packaging and recovery boundary

A separate Developer-only CHHHSPPGWorkbench/chppg 0.1.0.0 container now packages the
existing Draft Word pilot and its two pre-existing references. Empty-container
import preceded inclusion; no Default 17+1 payload was imported. Exact current
preimage, membership and all connection-reference rows were retained, and exported
workflow definition/reference equality passed after local extraction. Native final
readback preserves Draft, both distinct workflow/runtime identities, owner/creator
and displayed modification time. No execution/activation or cross-target import.

The preimage has eight explicit changes from the original v3 qualification: six
designer metadata additions and two authentication-expression additions. Preserve
that current representation; do not restore the older v3 graph over it or infer
runtime equivalence. Future recovery must identify the correct Developer container
and both component/resource identities, freeze current state, preserve existing
Default/Active memberships and both shared references, and remove only this owned
custom membership if reversal is needed. Do not delete the flow or globally shared
references. The verified export/current preimage support configuration recovery
preparation; no new Developer native restore or whole-workspace recovery trial was
performed. Source Default packages remain separately qualified and unchanged.

See [Developer packaging](native-document-generation.md#developer-only-custom-packaging--22-october-2026)
and its private packaging audit, recovery plan and terminal handoff. Matching names
across environments do not imply matching object IDs or interchangeable packages.
