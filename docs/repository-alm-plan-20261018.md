# Repository protection, runtimes and ALM — 18 October 2026

> Historical planning baseline. Local Gitleaks/publication enforcement and stable project Python 3.15.0 were subsequently delivered. See [current workflow baseline](workflow-documentation.md) and the ALM track reviews; the dated audit table below is not current runtime status.

## Commission and baseline

The user commissioned incorporation and commit of this plan. This increment is
planning only: it does not publish the repository, enable hooks/CI, upgrade shared
runtimes, change authentication, move native components or deploy solutions.
The [Conductor track](../conductor/archive/ppg_repository_alm_20261018/index.md)
contains executable tasks. Preserve active lifecycle files and native writers.

The following observations were collected in the preceding read-only audit on
18 October; recheck affected state at execution rather than repeating a broad audit.

| Area | Observed state | Implication |
|---|---|---|
| GitHub | No Git remote configured; authenticated intended owner could not resolve the expected repository | Local commits are not verified GitHub publication. Missing versus inaccessible remains unresolved; do not overwrite or invent a replacement remote. |
| Gitleaks | 8.30.1 installed; no active pre-commit/pre-push hook, CI workflow or publishing-script scan gate | Installation provides no enforcement. History scan exited 1 with three apparent false positives: two fictional identity hashes and one prose match. Review exact findings before narrowly documenting exceptions. |
| Data separation | .local/private/outputs/receipts ignored and no tracked files under those prefixes | Useful protection, but not evidence that all tracked text/history is confidential-data-free. |
| Python | Default 3.11.6; python3.15 resolves to 3.15.0a8; 948 setup checks pass under that alpha | Stable 3.15 compatibility is unqualified. Passing setup checks is not full application or tenant acceptance. |
| Document utility | net10.0 target, Open XML 3.5.1 pinned with package lock; selected SDK 11.0.100-rc.1 | Pin and qualify a suitable stable SDK; do not change a shared installation during active work. |
| Other tooling | Node 26.12.0 and PAC 2.13.1 observed | These are installed versions, not a claim that every dependency is latest or supported for every operation. |
| Solution coverage | No complete reconciled component inventory; migration solution/publisher unselected | Do not claim all artefacts belong to a verified ALM solution. Existing pilot membership may differ. |
| Dataverse authentication | PAC and M365 CLI reads failed with AADSTS70043 refresh-token expiry/sign-in-frequency checks | Authentication gap, not an established permission denial. Earlier SharePoint/Graph success does not prove current Dataverse access. |

Detailed scan and attempted solution-read receipts remain private in
`.local/alm-audit-20261018/`. Never commit raw scan matches, credentials, tenant
bindings, operational policy content or exported production data.

## Priority and value

| Sequence | Task | Value / complexity | Independence and completion evidence |
|---|---|---|---|
| 1 | ALM-01 Publication protection | High / low–medium | Local first; block publication on scan failure/missing scanner and test with a harmless synthetic secret. No tenant prerequisite. |
| 2 | ALM-02 Runtime reproducibility | High / low–medium | Isolated project runtime qualification; retain working interpreter. No global upgrade or active-flow change. |
| 3 | ALM-03 Artefact inventory | High / low for local, medium for native reconciliation | Inventory existing files/receipts immediately; hold only live membership fields on authentication. |
| 4 | ALM-04 GitHub synchronisation | High / low–medium | Requires ALM-01 and explicit publication scope; verify identity/privacy and compare remote/local commit after push. No force push. |
| 5 | ALM-05 Solution coverage | High / medium | Exact target and existing rights required; no new environment, publisher or capacity assumed. Preserve existing components until migration/recovery is qualified. |
| 6 | ALM-06 Release discipline | High / medium | Version, checksums, deployment settings and recovery evidence; use scripts/manual release where supported. |
| 7 | ALM-07 Pipeline eligibility | Conditional / high | Assess only after repeated releases justify it; absent premium/Managed Environment/admin rights defer pipelines alone. |

This priority is for repository/ALM work, not a stop on the existing low-complexity
queue/navigation/measurement work. ALM-01 precedes any GitHub publication; neither
native solution enumeration nor a full pipeline is a prerequisite for local value.
Keep one automation and one workflow/template increment, and do not interrupt an
in-flight native operation. ALM-04 may proceed independently of native ALM-05.

## Publication protection

Use installed Gitleaks with a versioned configuration, staged-content pre-commit
check, pre-push/history check, CI and a fail-closed gate in the existing publishing
script. Inspect existing hooks first and compose rather than overwrite them.
Document hook installation for each clone; local hooks are bypassable, so do not
claim a local hook alone is an enforced server policy. Verify available GitHub
branch/ruleset and secret-scanning controls rather than assume private-repository
plan entitlement. CI runs after upload and therefore cannot alone prevent release.

Review the three findings against exact historical content; use narrow rule/path/
fingerprint exceptions with rationale, never whole-directory suppression or an
unreviewed baseline. Test rejection of a synthetic credential-shaped fixture and
acceptance of the documented fictional hashes. Keep real matches private.

Add a separate tracked-file and history review for personal data, confidential
policy text, tenant URLs/IDs, operational receipts and binary documents. Gitleaks
is not a general confidentiality/DLP guarantee; .gitignore does not untrack files
or remove historical content. Never rewrite history or rotate credentials merely
because a detector flags text; confirm the finding and use a scoped recovery plan.

## Runtime policy

Prefer stable supported releases with explicit project selection, lock files and
recorded qualification. Python 3.15.0 stable was released 9 October 2026; the local
3.15 alpha is not that release. Qualify stable 3.15 in isolation, run setup plus
representative offline importer, reporting, template and lifecycle tests, and
retain the existing minimum-supported contract until compatibility is proven.
Do not run tests that can mutate tenant data under the label of a runtime check.

Pin a stable SDK compatible with the net10.0 utility and use locked dependency
restore. Assess updates for compatibility/security and value, not newest-version
count. CLI versions/auth caches and shared Node/.NET/Python installations are
shared operational dependencies; coordinate before changing them. Preserve the
current known-working versions and precise rollback instructions.

## Artefacts and solution boundary

Inventory logical artefact, kind, owner, environment alias, source path, native
identity reference (private), solution membership/evidence date, dependencies,
deployment method, runtime state, version/hash and recovery method. Distinguish
local source, deployed definition, saved output and accepted runtime behaviour.
Reuse the workspace manifest and existing receipts rather than build a second
operational registry. Report unknown membership explicitly.

Eligible Power Platform flows/apps, connection references and environment-variable
definitions belong in a cohesive PPG solution where supported. Reuse an appropriate
existing publisher/solution after exact-target verification; avoid one solution per
flow or a cross-project catch-all. Separate solutions only for real ownership or
independent release boundaries. A solution is not an archive of every project file.

SharePoint lists/libraries/views, Teams navigation, document templates and content
need separately versioned provisioning/configuration and recovery coverage.
Operational records and confidential documents remain in approved Microsoft storage;
Git contains sanitised schemas/scripts/templates, not real policy packages.
Solutions do not contain Dataverse table data. Record references to externally
owned source/publication systems; never migrate or write the upstream register.

## Authentication, release and governance

Follow [the qualified CLI route](operating-context.md#cli-first-route--18-october-2026).
Reuse intended-account sessions and supported app/tenant/flow mappings. Coordinate
shared authentication renewal with active writers. For supported verification
URL/code steps use the internal browser; password/MFA/new consent remain with the
user. Never transfer tokens or cycle app IDs around access-policy denials.
After renewal verify identity and exact target before enumerating solution
components. An unavailable Dataverse route holds native reconciliation only.

Use unmanaged development source and managed releases to nondevelopment targets
where the actual environment/licence arrangement supports that model. Keep unpacked
sanitised source in Git, immutable versioned build artefacts in approved storage,
and private target values outside Git. Connection references are transportable
bindings, not portable credentials; verify target ownership and connections.

Each release records commit, solution/version, component inventory, source/build
hashes, dependency order, configuration, deployment receipt, smoke/readback evidence
and recovery procedure. Reconcile drift before importing. An import success is not
end-to-end acceptance. A previous solution import is not automatically a safe rollback:
check component removals, schema/data consequences and recovery first. Keep issued
history and human edits intact. Technical release is separate from policy approval.

Record accountable solution/connection owners and backup support arrangements
without assigning people or creating service accounts by inference. Use existing
least-privilege roles and DLP settings; document gaps without granting rights.
Revalidate external connectors, licences and ordinary-user access for affected changes.

Native pipelines are conditional: Microsoft documents premium use rights for
Managed Environments and requirements for pipeline target environments. No new
Managed Environment, licence, consent or pipeline-host provisioning is commissioned.
Use qualified export/unpack/pack/import scripts and deliberate release receipts
where available; defer a large ALM Accelerator/CoE deployment until justified.

## CLI coverage for remaining work

| Work | CLI boundary |
|---|---|
| Queue fields/views/filter formatting, metadata and configuration | Implement and read back through qualified CLI; visual usability remains separate |
| Follow-up calculations/previews, measures and observation templates | Fully CLI-capable using existing inputs; no sending implied |
| Provenance/edition-link checks and missing-data analysis | CLI-capable; authoritative currency remains a human judgement |
| File/version inventory, exports and copied-fixture byte recovery | CLI-capable; preserve originals and actual output links |
| Flow definitions/runs/recovery | Qualified CLI operations; inspect native output when required |
| Solution inventory/export/unpack/deploy | CLI-capable after target auth/permission and supported-operation qualification |
| Word rendering/editability and ordinary-user navigation | Native UI/user evidence required alongside CLI |

## Official sources checked 18 October 2026

- [Python 3.15.0 stable release](https://www.python.org/downloads/release/python-3150/)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [Microsoft solution concepts](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)
- [ALM basics](https://learn.microsoft.com/en-us/power-platform/alm/basics-alm)
- [Pipelines, licences and deployment limits](https://learn.microsoft.com/en-us/power-platform/alm/pipelines)


## Initial factual inventory — 22 October 2026

The [read-only inventory qualification](artefact-inventory-recovery.md#read-only-alm-inventory-qualification--22-october-2026) records current component layers, Git/pipeline prerequisites, Developer system-only observed membership and external artifact source/hash/recovery declarations. All 17 Default profiles returned one Active unmanaged layer each; no additional managed layer was returned. The 120-artifact inventory includes 112 external rows and 311 unique source hashes. Receipt presence is bounded sampling, not whole-workspace native restore or fresh verification of every external artifact.

No hosted Git remote is configured. No existing pipeline host/shared pipeline/target is selected or qualified; first-visit host provisioning was avoided. At this initial snapshot, native Git setup rights/binding and Managed Environment prerequisites were unqualified; the later exact-target assessment below resolves the environment and own-role facts. Current GitHub native integration is a preview requiring additional app/Key Vault/admin setup, distinct from ordinary Git. Retain the qualified local Git/bundle and native CLI/manual release. No pipeline/host/connection provision, permissions or native write was made. This assessment does not resume the separately blocked conditional-feature goal.


The subsequent source correction closes the two helper-flow manifest omissions:
122 logical artifacts, 27 capabilities, ten native-flow groups and the same 112
external artifacts. Existing keys/surfaces/status policy and native 17+1 package
are preserved. Exact retained native identity/definition/binding/owner and recovery
pins stay private; 319 source hashes are covered by the updated inventory. Sixteen
existing workspace/inventory checks pass. No hosted manifest redeployment or
conditional-feature resumption follows this local manifest correction.


A managed candidate artifact has now exported and unpacked through the existing
Default route, with exact component/definition parity to the accepted unmanaged
package and only its Managed manifest flag changed. Fresh source state/binding
preservation passed. This supplies a candidate artifact, without qualifying a
managed target, import, upgrade, uninstall, layer transition or rollback. No such
deployment was attempted; retain the working unmanaged/manual route. See the
[managed candidate evidence scope](recovery-qualification-20261021.md#managed-candidate-artifact-qualification--22-october-2026).


## Maximum ALM route under observed rights — 22 October 2026

Two exact non-admin environment metadata GETs through the existing cached QH client
and four explicit-target PAC own direct/team-role queries succeeded. No login,
resource-scope expansion, settings change or profile selection was needed. The
terminal PAC metadata read retains the previously active QH Default profile.
Existing own-account licence observations are reused; they do not establish or
exclude tenant/flow/Process allocations or production entitlement.

| Prerequisite | Default | Developer | Consequence |
| --- | --- | --- | --- |
| Dataverse | Held: existing ready database | Held: existing ready database | Both retain their separate solution/artifact routes. |
| Managed Environment | Not held in observed state: protectionLevel Basic | Held: protectionLevel Standard | Developer's Managed prerequisite is resolved; no enablement needed. |
| Own Dataverse System Administrator | Not present in returned direct or inherited-team assignments | Held as a direct role | Developer's binding-role prerequisite is resolved. Default maker/basic roles do not supply that role. |
| Custom unmanaged PPG solution | Retained qualified 17+1 package | Retained qualified one-pilot/two-reference package | Same namespace does not make the two packages interchangeable. |
| Native provider/repository binding | Unknown; no selected provider/repository | Unknown; no selected provider/repository | No Azure DevOps Basic/contribute rights or existing GitHub app/connection has been qualified for PPG. |
| Applicable Managed/premium use rights | Unknown beyond retained own-account observations | Unknown beyond Developer/testing scope | Managed state and System Administrator are not licence proof. |
| Identifiable existing pipeline host/shared pipeline/run access | Unknown | Unknown | Environment metadata did not identify an association. No host was guessed or provisioned. |
| Personal-pipeline target type | Not eligible: Default | Developer type observed; target/import/host configuration not qualified | Default exclusion is specific to personal targets, not tenant-wide pipelines. |
| Ordinary hosted Git publication | No Git remote configured | Same repository-level fact | Local commits/checks are usable; GitHub publication/CI enforcement needs a verified selected repository and scope. |

Microsoft documents Standard as enabling Managed Environments and Basic as disabling
them ([CLI reference](https://learn.microsoft.com/power-platform/developer/cli/reference/admin#pac-admin-set-governance-config)).
The current Developer environment therefore already meets the **Managed and System
Administrator** prerequisites for native Git. The remaining gates are concrete:
an existing supported provider connection and selected repository with suitable
provider access, applicable licensing and a bounded binding/round-trip qualification.
Use per-solution binding for the owned PPG solution if that route becomes eligible;
environment-wide binding could include other projects' unmanaged customizations.
Azure DevOps requires its own Basic/contribute access ([setup](https://learn.microsoft.com/power-platform/alm/git-integration/connecting-to-azure-devops));
GitHub native integration remains preview and additionally requires the documented
approved app/Key Vault/connection setup ([preview prerequisites](https://learn.microsoft.com/power-platform/alm/git-integration/connecting-to-github)).
No such setup was performed or inferred from ordinary GitHub access.

For pipelines, the retained exact Default PAC query returned unsupported segment
`deploymentpipelines`. It was not repeated or treated as absence of a platform/custom
host anywhere in the tenant. No existing host association was identifiable from
the supported metadata, so no host query or first Pipelines navigation was attempted.
That first visit can provision a platform host ([personal pipelines](https://learn.microsoft.com/power-platform/alm/platform-host-pipelines)).
A real route still needs an identified associated host/shared pipeline, permission
to run it and an exact qualified target/import pair. Developer testing can use the
Developer Plan; other Managed/premium requirements and any host enforcement/grace
settings must be established for that exact route. Current guidance also describes
October 2026 unmanaged-target enforcement and temporary extensions; Basic alone
therefore does not prove every existing custom pipeline is unusable ([pipeline
licensing and enforcement](https://learn.microsoft.com/power-platform/alm/pipelines#frequently-asked-questions)).
No grace policy, other target or tenant-admin entitlement was inferred.

**Maximum currently qualified route:** explicit-target PAC solution export/unpack,
local Git and publication checks, immutable private artifacts and the existing
scoped manual release/recovery route. Native Git and native pipelines are not yet
end-to-end qualified. Ordinary GitHub artifact publication can extend this route
once the exact existing repository, write/privacy scope and CI behavior are verified;
it does not require Dataverse Git binding, but this repository currently has no
remote. Managed candidate import/upgrade/cross-target recovery remain unqualified.
No new environment, host, app, identity, consent, licence or settings change is a
prerequisite to retaining the proven route.

Private proof: `.local/ppg-alm/eligibility-20261022/`, especially
`environment-read-audit.json`, environment metadata, own-role rows,
`preservation-audit.json` and `eligibility-audit.json`. Both Default packages,
Developer package and binding-r2 candidate hashes remain exact. No flow activation,
rerun, native content write, native Git connection or pipeline association occurred.
The binding-r2 invoker hold and conditional-feature goal remain separate.


## Current r2 Developer exports qualified — 22 October 2026

Current published r2 was independently exported through the existing VS Code PAC
route in both unmanaged and managed formats, preserving the earlier package.
Both retain `CHHHSPPGWorkbench / chppg`, version `0.1.0.0`, exactly one fictional
workflow and its two existing invoker references. Actual ZIP definition and
references match fresh native clientdata and the verified r2 graph. The only
export-only workflow field is `templateName: null`, explicitly accounted for;
all remaining workflow JSON is exact. The two packages differ only in the
solution manifest Managed flag. No missing dependencies were declared.

Before/after native membership is the same three components; canonical readback
remains Published / Stopped with unchanged r2 definition/references. The previous
Developer package hash is unchanged. No auth selection change, publish, activation,
run-form retry, import or restore occurred. Templates, generated documents and
paired receipts remain external resources. Export parity qualifies configuration
capture, not native restore, managed upgrade or current-template output.

This closes the independent current-configuration export gap; it supersedes the
earlier plan to wait for runtime output before export. The one fictional DOCX and
paired-receipt trial remains unresolved at the native run form. Private packages,
raw PAC receipts and independent checks: existing
`.local/ppg-alm/developer-r2-native-trial-20261022/r2-export-audit.json`.


Current r2 fictional output qualification subsequently completed through one normal
native Run. Actual DOCX/paired receipt and preservation/readback verify; final flow
Stopped and canonical graph/references unchanged. Earlier current-output holds are
superseded; r2 configuration exports remain exact, without another export/import.
See [current output qualification](native-document-generation.md#current-r2-fictional-output-qualified--22-october-2026).
Production entitlement, native restore and managed deployment remain separate.


## Developer managed-target boundary qualified — 22 October 2026

Fresh existing-profile PAC enumeration exposes only the current QH Default and
Developer candidates. Exact solution/member reads show the same permanent
`CHHHSPPGWorkbench / chppg`, version `0.1.0.0`, but different unmanaged payloads:
Default has18 workflows and3 existing references; Developer has1 workflow and2
references. Their component identities are disjoint. Current r2 managed/unmanaged
package hashes and the r2 definition remain unchanged. No PAC selection changed.
This is current caller-visible inventory, not a tenant-wide absence assertion.

Microsoft's [solution concepts](https://learn.microsoft.com/power-platform/alm/solution-concepts-alm)
require testing a managed export in a separate environment from its originating
unmanaged solution. Therefore Developer cannot qualify its own managed export.
Default already contains a different maintained workload under the same solution
name; it is not an isolated Developer deployment target. No import was attempted
and no platform error is invented. Do not solve this boundary by deleting or
converting either canonical solution, renaming the accepted namespace, merging
payloads, or forcing an overwrite.

The remaining supported next step is an existing isolated target URL/access,
followed by target-native reference/binding, stopped import, readback and bounded
upgrade/rollback qualification. A copied-target/native restore still needs its
own isolated proof; current export parity and earlier Default recovery are not a
Developer restore claim. The question for an existing target is pending; no new
environment, host, permission, consent or licence was provisioned. Retain the
qualified manual release/recovery route meanwhile.

A fresh own-account Graph read returns the same four assigned products: Microsoft
365 E3, Power BI Premium Per User, Power BI Free and Teams Audio Conferencing.
No assigned Copilot/Syntex or standalone Power Automate Premium product is visible.
Enabled Office365 Flow/Power Apps/PVA service plans do not prove production Word
or native Copilot capacity, nor exclude tenant/flow/Process allocation. No unchanged
capacity activation was retried. Current r2 fictional output remains qualified and
Stopped; its older invoker hold is superseded.

Private current enumeration, exact memberships, package-preservation and licence
receipts: `.local/ppg-alm/developer-deployment-target-20261022/qualification-audit.json`.


## Disposable Developer copy binding boundary — 22 October 2026

One native Save As test used the existing source and account. Its dialog explicitly
states that the copy is Off by default; the chosen fictional name had no prior
match. A single Save created a distinct Stopped fixture outside the canonical
solution. Dataverse resourceid was blank, but its logical workflow ID resolved to
the service object. Both views retained the exact r2 definition and **no connection
references**. A definition-only copy is not a valid r2 recovery baseline.

One guarded copy-only PATCH supplied the original two existing invoker references,
without new connections or source changes. It saved a separate Draft with exact
candidate definition/references; the default GET still showed the older Published
Stopped/unbound version. This is not a failed/no-effect save and does not justify
another PATCH. No publish, activation, run or fault injection followed.

The concrete next operation is a supported non-activating binding/publication route
for this disposable copy, then the actual bounded fault/restore and readback. Until
that route is qualified, the fixture stays Stopped with its binding-repair Draft
retained; it is not runtime-ready or a qualified native restore. Managed import/
upgrade/rollback still needs the separately identified isolated downstream target.

Fresh readback proves zero fixture runs and exact source definition, references,
identity, creator, modification/creation times and Stopped state. Canonical solution
membership remains one workflow/two references; both existing r2 package hashes
remain exact. The extra diagnostic fixture is not included in that canonical set.
No publisher, solution, licence, role, consent, sharing or source-record changes.
Private original/copy/draft identities, one-save/one-PATCH intentions, raw responses,
empty history and preservation audit:
`.local/ppg-alm/developer-copy-restore-20261022/qualification-audit.json`.


## Developer copied-flow published configuration recovery — 22 October 2026

The earlier binding preflight hold is superseded by a completed native exercise.
Normal Publish on this disposable manual-flow copy temporarily enabled it; each
of three publications was immediately followed by a successful stop. No Run,
Test or resubmit occurred. The original flow was never changed or activated.

The two existing invoker references were repaired and published, then a single
fictional template-version enum was deliberately faulted and published. Full
configuration restoration was published and read back exactly: definition,
references, name, identity, creator and creation time match the frozen valid copy.
Both source and copy finish Stopped, with zero copy runs. Source configuration,
canonical three-component membership and both current r2 packages are unchanged.
No new connection, permission, consent, licence or namespace was introduced.

This qualifies copied-flow published configuration recovery only. Deleted-target
recreation, package-import recovery and managed import/upgrade/rollback remain
unqualified; managed deployment requires an existing isolated downstream target.
Production Word entitlement and output adoption remain separate. Earlier raw
Draft-versus-Published holds are retained as history, not current blockers.
Evidence: `.local/ppg-alm/developer-copy-restore-20261022/published-restore-audit.json`.


## Isolated managed configuration deployment qualified — 22 October 2026

The user explicitly authorised creating a suitable isolated test environment using
existing permissions/licensing. A single native PAC Developer creation succeeded
with the existing account: a new Australian-region Dataverse environment with
Basic protection. No billing policy, paid add-on, new licence assignment, consent,
role escalation or Managed Environments enablement was requested. Source Default
and originating Developer workloads were not modified. The prior missing-target
hold is superseded for this bounded test. Exact target URL/IDs remain private.

The new target initially contained only its two built-in solutions. Qualification
then completed with actual native operation and full readback:

1. Import unchanged managed r2 package 0.1.0.0: one inactive workflow and two
   unbound managed references; exact complete definition/reference declarations.
2. Stage-and-upgrade to 0.1.0.1 with exactly one additional fictional accepted
   template-version enum. Read back changed graph/version, managed membership and
   no remaining holding solution; no execution or activation.
3. Stage-and-upgrade to 0.1.0.2 restoring the original complete graph/references.
   This is higher-version recovery, not a claimed in-place downgrade.
4. Uninstall only this disposable target solution, verify solution/workflow/two
   references/components absent and built-in solutions retained, then reimport
   the unchanged frozen 0.1.0.0 package. Verify exact recovered configuration.

All four imports and the uninstall succeeded. Final native Flow service state is
Stopped and actual history is empty. Full source definition/references/identity/
creator/times remain exact and Stopped; original packages and shared PAC selection
are unchanged. Dataverse declaration JSON matches the export exactly; service
reference presentation expands connector metadata, so compare explicit logical
reference/API/invoker mappings rather than equating those two representations.

This qualifies isolated managed **configuration** deployment, staged upgrade,
forward recovery and deleted-target reimport. The target has no connections and
two unbound references. It is not connected-runtime/output qualification,
production adoption, policy approval, native Git or pipeline qualification.
Retain the working source runtime and manual production route. If runtime adoption
is later required here, qualify target connections and a separate fictional
output/edit/retry case; do not reuse source connection IDs across environments.

The retained target is temporary. Current Microsoft guidance permits unmanaged
Developer creation until 15 November 2026, with suspension starting 15 December
2026 and deletion starting 15 January 2027. Preserve the packages/evidence and plan
cleanup or an eligible successor before that lifecycle; no paid conversion or
new schedule was made. See [Developer Plan lifecycle](https://learn.microsoft.com/en-us/power-platform/developer/plan).

Restart: use the private target binding and explicit PAC environment URL; reconcile
any pending import ID before retrying. Check current solution version/membership,
full definition, reference bindings and inactive state. Upgrade via a versioned
candidate; recover by a tested higher-version package or, only on a disposable
empty target, verified uninstall/reimport. Never delete a maintained source
solution to make a target eligible. Keep namespace CHHHSPPGWorkbench / chppg.

Private intent, provisioning operation, all four import IDs, uninstall/absence
reads, candidate packages, full native readbacks and qualification audit:
`.local/ppg-alm/isolated-target-20261022/`.


## Isolated target binding and one connected output qualified — 22 October 2026

The two target OAuth connections were created through the existing signed-in
native route and read back Connected for the intended account. No password/MFA,
new consent, role change, paid enablement or licence assignment was observed. The
first OneDrive attempt survived an interrupted observation; its existing native
record was reconciled and reused rather than creating a duplicate. Word used one
native Create and existing account selection. The runtime additionally created
one native Button/logicflows connection; it is separate from the two references.

PAC reimported the unchanged managed0.1.0.0 package with a deployment settings file
using the actual target connection IDs. Both stored bindings, managed three-
component membership and exact complete definition/reference declarations were
read back before activation and after the test. Source connection IDs were not
transplanted. Checker returned zero errors and only the Off warning.

One temporary target-only activation and one ordinary native Run completed all
five actions successfully. The accepted fictional input's27 fields match the
paired immutable JSON receipt. The actual generated DOCX was11,516bytes; CRC,
all intended scalar/array values, Unicode, optional text and one comparison/one
consultation row were verified. The selected template and earlier human-edited
file remain byte-exact; original source configuration/identity/times remain exact
and Stopped. Target stop returned200, full canonical graph/references match the
preimage, and final actual history contains exactly one successful run.

### Word save boundary and version-safe recovery

Opening the library file URL entered Editing despite its viewing hint. Word
saved a new2.0 version before explicit Viewing selection. Generation1.0 was
11,516bytes and the later version is13,716bytes: ETag, length, modification time,
version and package bytes changed. Both are retained. All67 paragraph texts and
36 content controls persist; normalized complete text matches, and the immutable
JSON receipt is unchanged. Native Word Viewing exposed both pages of the later
version. Do not claim byte preservation or exact generation-version layout from
that later display, and do not label the latest file as the receipt's generation.

Native history lists the actual1.0 version. A read-only REST version-content GET
retrieved its bytes exactly matching the frozen generated snapshot. The direct
history URL's earlier401 remains retained; a changed REST resource path succeeded
with the same existing client/resource and no credential/scope change. No native
restore, deletion, new run or overwrite was used to conceal the later version.

For package preparation, pin the retained generation1.0 bytes/receipt explicitly,
or treat the later Word revision as a separately reviewed working artifact with
its own provenance. Refuse a latest-file/generation-receipt pin mismatch. Prefer
the native viewing/preview route and verify actual mode before relying on a URL's
hint; after opening/editing, re-read version/bytes and preserve the issued history.

This closes the selected target connection and one-case runtime gap. It does not
qualify production entitlement, all shapes/layouts, target edit/retry matrix,
SharePoint document-generation forms, native Git/pipelines or operator acceptance.
The isolated target retains two Connected reference bindings and its flow Off;
its temporary Developer lifecycle is unchanged. Private intents, deployment
settings, failed observations, versioned bytes and native terminal readbacks:
`.local/ppg-alm/isolated-target-binding-20261022/qualification-audit.json`.
