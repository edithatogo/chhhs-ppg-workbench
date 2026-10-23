# Native structured Word generation

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The preferred route is SharePoint structured document generation with maintained
Word templates and accepted structured inputs. The existing manual DRAFT generator
and submission assembler remain available while native eligibility is qualified.
The user selected retaining the current route pending entitlement, then checking
alternatives and progressing with existing access. The fictional Developer pilot
is delivered and retained Off. Native generation is verified; production
entitlement/adoption remain conditional. The operational manual route stays.
See the [four-step operator guide](./native-document-operator-guide.md).

## Current eligibility — 16 October 2026

The existing evidence library permits the scoped create/read/recycle probe. Its
Forms → Create new form path created an empty responses folder and opened a
file-upload designer with mandatory Upload file. It did not expose Document
generation form, template selection, mapping or generated-file settings. Nothing
was uploaded or submitted; the empty probe was recycled and absence verified.

The exact work account's Microsoft 365 portal reports **Copilot Chat (Basic)**.
Microsoft's [licence guidance](https://support.microsoft.com/en-us/microsoft-365-copilot/what-copilot-license-do-i-have)
describes the displayed plan. The [feature prerequisites](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation)
require a Copilot maker licence, library Edit access and a DOCX template. Library
write access alone does not qualify this feature. Feature rollout/settings may
also affect availability. Copilot maker entitlement was not displayed in the
checked self-service views; applicable production entitlement remains unqualified.
These views do not establish every tenant, flow or Process allocation.

The alternative [Word Online (Business) connector](https://learn.microsoft.com/en-us/connectors/wordonlinebusiness/)
is Premium in Power Automate. The native View My Licenses pane lists Power Automate Free and Power Automate
for Office 365; its Premium connectors capability is explicitly unavailable.
These personal licences do not qualify production Premium use. They do not rule
out an existing Developer-plan entitlement or a separately licensed Process flow.
No purchase, trial, consent, preview enablement, billing or permission change is
implied. Nothing has been switched from the working manual route.

## Availability recheck — 19 October 2026

Fresh intended-account CLI assignment and licence-detail reads succeeded. The
assigned products remain Microsoft 365 E3, Power BI Premium Per User, Fabric/Power
BI Free and Teams Audio Conferencing. No Copilot or Syntex service plan was present
in those assigned products. This is account evidence, not a tenant-wide absence
claim or proof that another maker cannot use the feature.

The existing PPG library loaded through the authenticated browser. Its Forms
inventory listed two existing forms; opening the inventory is not a successful
document-generation test. The creation menu exposed ordinary Office documents
and Add Template, but no modern-template content-assembly option. No new form,
folder, template or generated output was created. The prior file-upload designer
observation remains dated evidence; this recheck did not submit either form.

A current read of global SharePoint tenant settings was refused with
`Attempted to perform an unauthorized operation.` Consequently existing content
assembly billing, service enablement and allowed-site scope remain unverified.
Do not interpret this denial or the missing menu as proof that billing is absent
or the feature is disabled throughout the tenant.

The concrete remaining check belongs to an existing SharePoint administrator:
inspect Content assembly under Microsoft 365 admin centre's pay-as-you-go service
settings and confirm existing billing/legacy entitlement and this site's scope.
Microsoft's [setup instructions](https://learn.microsoft.com/en-us/microsoft-365/documentprocessing/content-assembly-setup?view=o365-worldwide)
require SharePoint or Global Administrator access for service setup. No billing,
licence, consent or permission change was attempted. A template/output pilot can
follow if the existing route is available; generation has not been proved here.
Private current responses and summary are retained in the dated
`.local/native-document-generation/availability-recheck-*` folder.

## Qualified CLI assignment readback — 16 October 2026

A later intended-account, delegated Microsoft 365 CLI self-profile GET returned
HTTP 200 with assigned licences and plans. It lists Microsoft 365 E3, Power BI
Premium Per User, Fabric Free and Teams Audio Conferencing (select geographies).
Microsoft Office, Flow for Office 365 and Power Apps for Office 365 plans are enabled.
No separate user-assigned Power Automate Premium or Microsoft 365 Copilot SKU was
observed. This supplements the earlier self-service UI evidence.

The read did not inspect flow/Process allocations, environment or tenant capacity,
pay-as-you-go configuration, or subscription/trial duration. Package-flow metadata
such as an unspecified plan, a licence-name placeholder or High throttling is not
entitlement proof. The Office assignment does not itself qualify the Premium Word
connector for production automation. Production eligibility remains unresolved;
no licence, consent, billing or native configuration change followed this read.

Private assignment summary and raw-response hash are retained in
`.local/native-document-generation/qualified-assignment-summary-20261016.json`;
product/plan names use the [Microsoft service-plan reference](https://learn.microsoft.com/en-us/entra/identity/users/licensing-service-plan-reference).

## Alternative qualification — refreshed 16 October 2026

| Route | Licence and permission evidence | Current disposition |
| --- | --- | --- |
| SharePoint structured document generation | Microsoft 365 Copilot was not displayed in checked self-service product views; library effective permissions include Add, Edit and Manage Lists. Existing Forms entry still has no qualified document-generation path. | Preferred production route remains conditional on maker entitlement and feature availability. |
| Word Online (Business), production Power Automate | Native licence pane shows Free/Office 365, standard connectors available and Premium unavailable. Power BI Premium Per User is a different product. | Personal production entitlement unqualified. |
| Word Online (Business), existing Developer environment | Retained native receipt from 15 October shows Power Apps Community with displayed expiry 13 April 2027 in an existing Developer environment. Microsoft maps Community to Developer Plan and permits Premium connectors for development/testing. | Fictional native input/Word/output/receipt, editing, shape and recovery qualification completed. Retained Off; no production entitlement inferred. |
| Existing Process-licensed cloud flow | Microsoft permits Premium use through an allocated Process licence. The inspected PPG importer runs on its owner's plan; no suitable allocated Process flow has been established. | Alternative remains unproven; do not change the importer to test it. |
| Logic Apps with Word Online (Business) | Connector is Standard in Logic Apps, but execution requires an appropriate Azure resource and billing context. Cached CLI inventory supplies no usable subscription. | No existing qualified route; no resource provisioning or spending inferred. |

### Distinct SharePoint generation routes — clarified 19 October 2026

Keep the newer Copilot document-generation forms separate from Syntex/content
assembly (now document processing services). The [newer forms prerequisites](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation#prerequisites)
require assigned Copilot for the creator, library Edit and DOCX. The [content
assembly route](https://learn.microsoft.com/en-us/microsoft-365/documentprocessing/content-assembly?view=o365-worldwide)
documents existing pay-as-you-go billing and Manage Lists; [active legacy per-user
licensing](https://learn.microsoft.com/en-us/microsoft-365/documentprocessing/syntex-licensing?view=o365-worldwide)
can also retain content-assembly access. Absence of user-assigned Copilot alone
does not establish that every SharePoint-native generation route is unavailable.

Existing content-assembly service enablement, site scope, billing and legacy
entitlement have not been qualified for this PPG library. Next check is read-only
inspection of existing configuration through a qualified route. This does not
authorise billing setup, activation, licence assignment, consent or chargeable
execution. Preserve the supported manual route and existing owners meanwhile.

Content assembly has separate shape limits: its documentation excludes templates
with comments or Track Changes, and does not support SmartArt/bulleted lists.
The recovered historical discharge draft retains comments/revisions, so it must
remain preserved as evidence rather than be silently cleaned for generation.
Qualify the eventual maintained template's actual output, complex content,
editability, links and recovery for whichever route proves available.

The [Developer Plan](https://learn.microsoft.com/en-us/power-platform/developer/plan)
permits development/testing, not production. Its entitlement is not a Copilot maker
licence. Reuse the PPG-owned template and isolated native work already under way
in the unattended-package lane; do not create a second writer or borrow clinical
flow bindings without a handoff. Local template validation is preparation only.
The [Process licensing guidance](https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/types)
and connector classification do not establish actual allocation or execution.

Browser checks record the displayed personal products and effective library permissions. PAC's
expired challenge and one Microsoft 365 CLI access-policy rejection do not negate
browser access; do not retry that denied route unchanged. Retain exact evidence
privately. Production migration remains separate from a fictional Developer pilot.

## Prepared pilot boundary

Use one fictional review-package document first, deriving structure and placeholders
from `templates/review-package.md`. Reuse existing source/selection/business logic;
document generation consumes accepted inputs and cannot supply policy judgements.
Keep all output DRAFT / HUMAN CHECK REQUIRED. Do not submit real policy content to
AI field detection during qualification.

The complete maintained-placeholder mapping and acceptance cases are prepared in
`config/native-document-pilot.json`; fictional input is in
`templates/native-document/fictional-inputs.json`. Neither is a native DOCX template
or a generated output. A PPG-owned DOCX candidate was uploaded and read back; subsequent native qualification is recorded below.

Record document kind, case/occurrence identity, exact source snapshot/hash, included
record identities, template version/hash and generated revision in a retained input
manifest and output record. Missing mandatory technical identity fails preparation;
missing human review/approval remains explicit, never invented.

Map scalar identity/title/version/baseline fields, multiline comparison/change/role
and consultation text, optional sections and variable-length source/consultation
rows separately. A scalar-only demonstration cannot qualify repeating tables.
Existing native source calculations and monthly selection remain authoritative.

## Output acceptance before adoption

- Inspect actual editable DOCX and links against accepted inputs and template.
- Prove empty/one/many rows, long/multiline text, Unicode and optional sections
  required by the selected document shape. Do not silently truncate records.
- Save a human edit, regenerate separately and prove the earlier edited output
  and issued history survive. Never use a mutable filename as sole output identity.
- Verify template/source/input/output versions and included record counts/IDs.
- Exercise missing input and duplicate retry/failure; retain a visible failure
  receipt, recover the same operation and never claim success from a run alone.
- Open/download/save/reopen the actual output with the intended operator's access.
  Form submission access does not prove generated-file access.

### Future SharePoint qualification criteria — 17 October 2026

Microsoft's [structured-document guidance](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation)
distinguishes conditional form-field visibility from conditional document sections.
Power Automate generation does not apply the form's visibility rules. A required
field hidden in the form may therefore behave differently in automated output.
Before adoption, compare actual form-generated and flow-generated documents for
matching inputs, including hidden/visible fields and empty optional/required values.
Resolve requiredness deliberately; do not silently waive authoritative inputs.

Conditional document sections are evaluated at generation. Word for the web does
not re-evaluate them when field values are edited afterward. Test actual section
inclusion/exclusion and post-edit behavior separately; where re-evaluation is
needed, qualify a separately generated revision or the documented Word for Windows
route while preserving human edits and earlier output. Neither form visibility
nor a successful flow proves section parity.

These are future output-qualification criteria. Existing production entitlement
and feature-availability gates, manual fallback and native ownership remain as
recorded; this documentation does not qualify or enable a generation route.

A template's validity, local fixture or eligibility report does not close native
save/run/readback or operational acceptance. Keep the preferred route selected for
reconsideration after existing entitlement/feature availability is verified.
Detailed account/resource receipts stay private in `.local/native-document-generation/`.

## Native action input handoff

The existing PPG-owned candidate contains all 19 maintained placeholders, two
repeating sections and an optional plain-text control. Independently inspected
DOCX controls match the maintained mapping. Complete fictional action inputs for
empty/single/many-long-Unicode/optional cases and three negative/recovery scenarios
are retained privately in `.local/native-document-generation/native-action-qualification-inputs.json`.
These are prepared inputs, not generated documents or completed runtime checks.
The receipt distinguishes the DOCX hash from the maintained Markdown source hash.

For the isolated pilot, use a generated occurrence key and revision in a new
filename such as `PPG-fictional-<occurrence>-<revision>.docx`; validate each token
as letters, digits or hyphens. Create exclusively, and resolve a duplicate against
the retained occurrence/input/output receipt before retrying. Preserve edited
and prior outputs; never update an existing output merely because its name matches.
Retain source snapshot, included identities, actual template hash and output hash
in the occurrence receipt. Reject missing technical identity before generation.

`OptionalContent` currently supplies empty/nonempty text. It does not implement
conditional section deletion. Native inspection must determine whether the chosen
document shape tolerates an empty labelled section; otherwise the native writer
must implement and verify section inclusion/exclusion before acceptance. No such
acceptance is claimed. Actual connector schema and field names still require
readback against this candidate, followed by generated-byte inspection.

## Uploaded candidate readback

The PPG-owned candidate is retained in a distinct Word qualification folder in
the evidence library. Upload used exclusive creation; no prior template/output
was replaced. The downloaded package passes ZIP CRC and XML well-formedness checks.
SharePoint added content-type/property XML and changed package relationships;
`word/document.xml` remains byte-identical to the authoring candidate. Both exact
hashes and native file identity are retained privately. At upload time, connector acceptance and
editable output were unproven; later native qualification below supplies that evidence.

The private action-input receipt now points to the uploaded template identity/hash,
with the earlier authoring hash retained separately. Workbench owns the separate
Developer Word pilot; the unattended-package writer retains its Default flow.
Clinical owner has released scoped use-only access after its operation ended/Off; connection settings and all clinical objects must remain unchanged.

The separate fictional PPG Developer designer has discovered the uploaded template
and all25 top-level parameters, including both repeating arrays. Scalar input
readback matches23 prepared values (optional content blank). This is unsaved
designer evidence; repeating inputs, exact saved binding, run/output and acceptance
remain incomplete. No authentication change accompanies the handoff.

## First native output — acceptance defects

The distinct fictional PPG Developer flow is published. Its first manual run
succeeded through Word population and OneDrive file creation in a dedicated PPG
folder, with a run-specific filename. Both connection references resolve to the
released existing connection IDs. No clinical flow/file/settings were changed.
The designer Test panel had a validation error; the existing flow details Run
route submitted the single confirmed run. Fresh native history confirms success.

The downloaded 9,718-byte DOCX passes ZIP CRC. Scalar identity, comparison content
and multiline Unicode text are present. Acceptance fails: consultation response
is blank, and optional content retains its placeholder. Inspect actual native
inputs before selecting a repair. No claim of correct empty/one/many behavior,
editable save/reopen, preservation/retry or production adoption follows this run.
Private first-output content proof and exact run/file identity remain retained.

## Repair002 native result

Actual first-run inputs omitted the response and optional parameter. Repair002
made both explicit and changed the output revision. A conditional API update was
refused because an unpublished active draft existed; no bypass was attempted.
The native draft subsequently reopened, retained all three values, and published.
Full executable-definition comparison confirms the repair and one native casing
normalization of the success condition, with references/trigger/output parameters
and owner preserved. This resolved the repair through native Publish.

One repair run succeeded. Actual action inputs include the response, evaluated
empty optional value and revision. Downloaded DOCX passes CRC and content checks:
response present, optional placeholder absent, one source/consultation row and
multiline Unicode retained. The first output is preserved. The manual pilot flow
is restored Off with full definition/reference/owner readback. Edit/save/reopen,
empty/many rows, optional inclusion, missing input/retry recovery and the operator
input route still require qualification. Production entitlement remains separate.

## Rendered-layout repair candidate

Opening the repaired output in Word Online exposes a layout defect: Markdown
heading markers, pipe-table scaffolding and internal repeat-field labels remain
visible. Native population success does not establish usable presentation.
The one-time template authoring tool now creates real Word Title/Heading styles,
readable labels in repeating paragraph groups and an optional field without an
unconditional label. It does not populate documents locally.

A separate v2 candidate was created exclusively and uploaded without replacing
v1 or either output. Open XML validation reports zero errors; all34 named control
names/IDs are unchanged. Downloaded native bytes pass CRC and preserve authored
document XML, with SharePoint package metadata changes recorded privately.
The native file picker recognises the new template and its25 top-level fields;
changing templates clears input values, so remapping is required. Generated v2
output and edit/recovery acceptance were pending at candidate discovery.

The v2 candidate subsequently published with all25 remapped values. Full executable
graph comparison shows only the new template binding/path metadata, version,
revision and nonempty optional note; connections, owner and other actions are
unchanged. One native run succeeded. Downloaded9,937-byte DOCX passes CRC/content
checks, includes the optional note, and removes Markdown/internal-label defects.
Word Online renders two readable pages, including the consultation page break and
provenance. A test edit saved as native version2.0; downloaded12,181-byte bytes and
the reopened document both retain its marker. Original generated bytes and both
prior native output hashes are preserved.

The conditional Off request timed out; no duplicate request was issued. A fresh
full-row read confirms Off with exact published definition/references/owner
preserved. Remaining acceptance: empty/many groups, generation after the saved
edit, invalid/missing input, retry/recovery and an operator input route. Current
button inputs remain frozen fictional values; this is not an operational form.


## Completed Developer pilot — 16 October 2026

The current native button consumes accepted structured JSON, validates it before
Word, creates a distinct DOCX and retains a matching JSON input/output receipt.
The schema, fictional operator example and guide are maintained in the repository;
three hosted handoff files were created exclusively and downloaded hashes match.
The pilot capability and exact private deployment bindings are registered. No hub,
Teams tab, permission, source/case, clinical-flow or connection-setting change was
needed. Earlier preparation/repair notes above describe historical checkpoints.

| Required proof | Observed result |
| --- | --- |
| Exact bound source/template identity | Required fields/types and fixed fictional identity/hash enums; actual v2 template hash pinned. Regex is unsupported in this native Parse JSON schema, so rejected save was reconciled and replaced with supported constraints. |
| Native operator path | Actual Run form accepts JSON and passes it through validation, Word population, DOCX creation and retained receipt. Downloaded receipt input equals submitted fixture. |
| Empty/one/many and optional text | Empty repeats produce no repeat labels/placeholders; one-row output verified; three source/consultation groups and all18 long Unicode lines preserved. Empty/nonempty optional text verified. |
| Complete layout and editing | Four pages of the many-row document inspected in Word; groups can continue across pages. Actual one-row edit saved as native version2.0, downloaded and reopened. |
| Missing input/failure | Removing sourceSHA256 causes native Parse failure naming the field; four downstream actions skip and DOCX/receipt paths404. No false success receipt. |
| Corrected attempt and duplicate retry | Corrected input succeeds; native Resubmit with identical input creates distinct file IDs/receipts. Prior generated hash and human-edited hash unchanged. This preserves attempts, not exactly-once deduplication. |
| Provenance and preservation | Receipt retains occurrence, revision, included identities, source/template versions/hashes, run ID and actual output metadata. Fresh v1/v2 template hashes unchanged; original generated and edited bytes retained. |
| Final native state | Off; complete executable definition, owner and references match the verified candidate. Native history is terminal; Flow Checker0errors and only expected Off warning. |
| Operator access and handoff | Same authenticated operator opened native outputs, edited/reopened Word and downloaded guide/example/schema. Their exact URLs remain in private binding/hosted guide; no wider-user access claim. |

Keep the Developer pilot as a reusable technical qualification, with the operational
manual route retained. Native fictional runs took about3–4seconds; no measured
end-to-end saving follows. Production use still needs an eligible production route
and one selected real output qualified individually. The preferred SharePoint
structured-document route remains selected for reconsideration when its maker
entitlement/feature is available. No purchase or cutover is part of this pilot.

The selected shape uses repeating paragraph groups and plain optional text.
Arbitrary section deletion, repeating tables, embedded hyperlink authoring and
unattended package integration are outside this delivered shape. Existing output
links and same-account access are verified; business review/approval remain
unperformed. The separate unattended-package lane retains its own integration work.

Private current proof: `operator-v3-final-off.json`,
`operator-v3-final-preservation-and-handoff.json`, `operator-v3-invalid-proof.json`,
`operator-v3-repeat-preservation-proof.json` and native output/receipt bytes in
`.local/native-document-generation/`. Detailed native IDs remain outside Git.

### Runtime envelope and cost boundary

Microsoft's [connector reference](https://learn.microsoft.com/en-us/connectors/wordonlinebusiness/)
sets a 10 MB input-file limit and 100 calls per connection per 60 seconds. This pilot
uses a 12,677-byte template and a few serial runs; it is not a load/maximum-size
qualification. Shared connection capacity must remain available to its existing
owners. Rich-text/date-picker/checkbox controls are unsupported by this connector;
the selected shape uses supported plain text and repeating controls.

The [Developer Plan](https://learn.microsoft.com/en-us/power-platform/developer/plan)
provides development/testing access, not production use. No purchase, licence
assignment, trial, billing or Azure-resource change was made. Production cost is
not estimated without an eligible route and operating scope. Native portal savings
figures are explicitly simulated and are not benefit evidence for this work.

## Shared manifest reconciliation — 16 October 2026

Hosted manifest readback confirms the `native-document-generation` pilot capability
and all five `native-word-*` artefacts match the maintained local entries exactly.
The guarded combined integration preserved every pre-existing capability and
artefact. Existing Word hub content and channel tabs were retained. This registers
the completed fictional Developer pilot; it changes neither its flow nor the
conditional production-adoption status. Private before/after readbacks are retained
in `.local/autofill/native-manifest-before.json` and `native-manifest-after.json`.

## Exact-account/library recheck — 22 October 2026 Brisbane

Supported same-client Graph licence-detail readback succeeded. Assigned products remain Microsoft 365 E3, Power BI Premium Per User, Power BI Free and Teams Audio Conferencing; no Copilot or Syntex plan was observed in these products. This is own-account evidence, not tenant-wide billing/capacity or another licensed Process/maker determination. The exact evidence-library creation menu again exposed ordinary Office documents and Add Template, with no structured-generation or agent entry. Its Forms inventory retained the two existing forms; no new form was created. Keep the preferred structured route conditional and the qualified manual/web and fictional Developer pilot routes at their existing scope. No new generation, production entitlement, tenant setting or output parity is inferred from these reads. Current private evidence: `.local/artefact-recovery/20261021-native/assigned-licences-current.json` and `structured-generation-menu-recheck.json`.


## Documented Forms entry qualification — 22 October 2026

The earlier ordinary **New** menu receipt does not establish document-generation
availability. Microsoft's current [structured generation instructions](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation)
use **Forms → Document generation form** and require a Copilot maker licence,
library Edit access and a DOCX source.

The exact existing evidence library's Forms panel listed the two retained forms.
It exposed Create new form; that path prompted for a response folder and then
opened an ordinary editor with a required Upload file field. No document-generation
choice or template-selection step was observed. Folder creation automatically
saved an accepting-responses form; there was no separate publication step. The
selected fictional form was deleted through its own card's native Delete form
command. After cleanup the two original forms are still listed. No form link was
copied or sent and no response was submitted. The dedicated qualification folder
was retained; independent native readback confirms its same identity and zero
items. Do not claim that this inspection made no native changes.

This is a direct route observation, not proof that generation is unavailable
throughout the tenant or that existing forms cannot support other shapes. The
production prerequisite remains an eligible maker and a generation-capable route,
followed by actual output/edit/retry qualification. Existing manual/web preparation
and the fictional Developer Word pilot remain unchanged in scope. No licence,
permission, consent, connection or tenant setting was changed. Private evidence:
`.local/structured-generation-20261022/qualification-audit.json` and
`forms-route-readbacks.json`; native folder pre/postimages remain under the
existing artefact-recovery receipt folder.

Read-only exact-ID reconciliation also found the existing Developer Word pilot's
Dataverse Modern Flow record in Draft, with observed membership in Default and
Active system solutions. This is a positive native membership readback through
the existing VS Code PAC profile, not an inference from an empty join. It is not
member proof for the separate canonical QH Default solution, a current execution
or production eligibility test. The retained Off policy remains. Private proof:
`.local/structured-generation-20261022/developer-word-membership-audit.json`.


## Developer-only custom packaging — 22 October 2026

Fresh exact-target discovery found the selected Draft Modern Flow only in Default
and Active system solutions. The Developer environment had no matching PPG custom
solution/publisher; its other unmanaged options were Microsoft Basic and the Common
Data Services Default solution. An other-project publisher was left untouched.
Exact name/prefix/ID collision checks returned no matches. Reusing the already
selected CHHHSPPGWorkbench/chppg namespace, the existing qualified VS Code route
imported a verified empty 0.1.0.0 unmanaged container: no Default workload, workflow
or connection payload. The native import job completed successfully. Publisher and
solution received their own Developer-local IDs, distinct from the QH Default IDs.

Only the selected existing workflow was added, with required components. Native
membership readback contains exactly **one workflow and its two existing Word/
OneDrive connection references**; prior system memberships remain. No reference
was renamed and no new service connection was created. The unmanaged export and
local unpack contain exactly that workflow and both reference schemas, with the
current definition and logical references matching the frozen preimage exactly.
The source stays Draft and unmanaged. Workflow identity, separate runtime resource
identity, owner/creator, displayed modification time, manual trigger/schema and
all pre-existing connection-reference rows are preserved. No run or activation,
production adoption, new licence/consent, pipeline host or cross-target workload
import was performed.

The current definition differs from the original qualified v3 snapshot by six
designer metadata additions and **two connector authentication-expression additions**.
Those differences were captured before packaging and preserved unchanged, not
normalized away. Connection references match v3, but its prior runtime tests do
not newly qualify the added authentication representation. No runtime test was
requested or performed in this packaging increment. Current Dataverse Draft
readback is stated explicitly; a fresh flow-service Stopped read is not inferred.

The Developer package and QH Default 17+1 package share a semantic namespace and
version but have **different environment-local IDs and component sets**. They are
not interchangeable artifacts and neither was imported into the other environment.
The Default unmanaged/managed artifact hashes remain unchanged. Existing template,
OneDrive output and receipt files stay outside the solution package and retain
separate controls. Recovery materials are the current preimage, native membership/
reference snapshots and exported/re-extracted package. Native Developer restore,
managed/cross-target deployment and production execution remain unqualified.

Private evidence: `.local/ppg-alm/developer-word-packaging-20261022/`, especially
`packaging-audit.json`, `definition-drift-from-v3.json`, `pilot-clientdata.json`,
`DeveloperWordPilot-unmanaged.zip`, `postexport-preservation-audit.json` and
`recovery-plan.json`. Exact identities, connections, creator/owner and profile
selection details remain private. Shared PAC selection was released after the last
native read/export; no selection change was made by this operation. The active
profile at release was the existing QH Default profile. Conditional production
and assistant/surveillance/migration work remains blocked at its separate gates.


## External dependency reconciliation — 22 October 2026

The five existing manifest entries retain their original identities and bindings.
Their management mapping now includes the maintained Markdown source, fictional
input examples, template tooling, operator guide and current packaging receipts.
No artifact/capability rows or hosted manifest were changed; the 112 external rows
are not a claim that every external dependency has fresh native recovery proof.

| Dependency | Retained evidence and boundary |
| --- | --- |
| SharePoint v2 Word template | Current definition selects the recorded v2 item; private native upload/readback identifies its UID, version and bytes. Retained template bytes match the historical native hash. The v1 item in designer metadata is historical, not the selected input. |
| Source and accepted input | Maintained Markdown source hash matches the recorded template-authoring lineage. Local input/schema/hosted-guide copies match their historical native readback hashes. The fixed fictional sourceSHA256 claim is carried by input/schema/receipts; underlying source-snapshot bytes were not independently reconstructed in this check. |
| OneDrive output and receipt location | Separate connector/container from SharePoint; current definition uses run-specific DOCX and JSON names in the recorded folder. Retained recovery receipt has the same run identity, output name and byte length as the frozen output. Current folder identity and access were not refreshed. |
| Edited output and recovery/history | Existing native edit/version/reopen and distinct-attempt preservation evidence remains dated evidence. Retained edited output, recovery output and associated proof hashes match the original completion audit. No generation, edit/history trial or lifecycle artifact-frame check was repeated. |

The first cached-only template metadata read stopped before transport on expiry.
A subsequent explicitly bounded repair inspected the installed client's silent
method, blocked interactive alternatives and renewed the same saved account/app/
SharePoint resource successfully. Identity and audience remained equal. Fresh
metadata and byte reads succeeded for the selected template, guide, input and
schema. Guide/input/schema hashes still match their historical readbacks.

**Current template byte drift is unresolved.** The selected template retains its
recorded UID and displays version 1.0, but is now 22,377 bytes versus 12,677 in the
qualified snapshot, with a different SHA256. Main document XML and all 36 content
control identities are byte/structurally equal; changed custom XML and four added
trash parts account for ZIP differences. These facts do not establish runtime
parity or explain who/what changed the package. The native Versions query returned
no entries; it supplies no earlier-version restore proof. Preserve both snapshots;
do not silently update the accepted schema/hash, overwrite the native file or
restore the old template. Resolve the lineage/hash binding and qualify the selected
representation before a new generation run. Prior runtime proof stays historical.

The exact OneDrive output-folder read was then held before transport because its
separate Graph cache was expired. No additional resource renewal, new login, PAC
selection, native write, generation or output/history trial was attempted. Current
OneDrive container identity/access and native external restore remain unqualified.
The earlier 20-frame lifecycle proof was reused without a repeated audit. Exact
private target/errors, metadata, old/current bytes and comparisons are retained in
`.local/ppg-alm/developer-external-dependencies-20261022/`, especially
`silent-renewal-read-audit.json`, `targeted-dependency-results.json`,
`template-drift-audit.json` and `reconciliation-audit.json`. The conditional-feature
goal remains blocked. This source mapping was not deployed to the hosted manifest.


## Selected OneDrive dependency repair and drift diagnosis — 22 October 2026

This supersedes the preceding OneDrive expiry hold at the selected metadata/history
scope. The installed CLI's silent method was inspected again: it calls MSAL
acquireTokenSilent for the saved account/resource and propagates an error without
interactive fallback. Initial strict restore validation stopped before renewal:
the selected CLI connection lacked identityId. Read-only inspection established
that its cached Graph and SharePoint tokens have the same principal/tenant/app,
and the installed client's MSAL cache contains exactly one matching account.
Using that same CLI-provided public client, supported MSAL silent acquisition for
that exact existing account and Graph/.default succeeded. Returned principal,
tenant, app, audience and scopes match the prior Graph token. Interactive methods
were blocked. No CLI profile field was reconstructed or overwritten; no credential
or cache was copied to another client, and no new login/consent was requested.

Five exact native GETs qualified the recorded OneDrive folder, retained recovery
DOCX and its paired JSON receipt, and both returned version histories. Both files
resolve to the selected folder ID and drive. DOCX item identity, ETag, size, name
and modification time match the retained recovery receipt. JSON run-specific name
matches that same occurrence/run. Each complete returned history contains version
1.0 with matching size/time. Current native quickXorHash values were captured as
metadata; no fresh output-byte download, history restore, generation, editing or
new runtime test was performed. Earlier edited-output/native-reopen and lifecycle
20-frame evidence remains at its existing dated scope.

Independent ZIP/XML diagnosis identifies the template drift as **SharePoint
library/content-type metadata synchronization**: content-type schema version 11 to
31, added capture/cover/source metadata fields, changed datastore itemID and four
trash parts. No existing property value/path changed or disappeared. All other ZIP
members, including document/control parts, are byte-identical; the Word document
has zero dataBinding nodes. This explains the class of changes beyond timestamps,
without establishing who made them, current runtime equivalence or permission to
repin a hash/restore a file. Both snapshots and the original accepted hash remain.

The next executable gate is a bounded resolution of the selected template's
source/template hash binding and lineage, followed by qualification of that exact
representation before any further generation. Do not silently normalize metadata,
repin the input schema, regenerate or restore the old template. Native external
restore and production entitlement remain separate unqualified gates. No native
content write/run/activation or PAC/profile operation occurred; NSW sign-in was
untouched. The existing management row was updated locally without adding artifact
or capability rows, changing resource identities or publishing a hosted manifest.
Private evidence: `.local/ppg-alm/developer-onedrive-20261022/`, including
`silent-read-audit.json`, `reconciliation-audit.json`, selected metadata/history and
`template-drift-support.json`. The conditional-feature goal remains blocked.


## Exact-template download stability — 22 October 2026

Six bounded GETs read file metadata and native content-type SchemaXml before/after
**two consecutive byte downloads** of the exact selected template. All requests
succeeded through the unexpired existing SharePoint cache, with no renewal/login,
new route/scopes, PAC action or native write. Private request GUIDs, timestamps,
selected response headers and raw responses are retained.

Both fresh downloads and the earlier current snapshot are exactly **22,377 bytes**
with the same full SHA256. Every one of their **22 ZIP members** is byte-identical,
not just document.xml or control identities. UID, ETag, UI version 1.0, file length,
recorded file modification time and content-type schema remain equal before/after;
the native content-type schema version is **31**. There is no per-download byte or
datastore-ID variation in these observations. This supports a stable observed
post-synchronization representation; it does not prove that the earlier transition
occurred only once or that future schema changes cannot alter bytes.

The original accepted template hash and all historical inputs/receipts remain
unchanged. The smallest next binding operation is to prepare a **distinct versioned
binding correction** referencing the same native UID, observed whole-file hash and
content-type schema, with the old/current snapshots and reason retained. Qualify
that exact representation in a separately scoped fictional native run before
adoption. Do not normalize away ZIP metadata, overwrite the original binding,
automatically repin a schema or restore/upload a template to make hashes match.
This measurement performed none of those operations and supplies no new runtime,
production or native restore proof. Private receipts and raw snapshots remain in
`.local/ppg-alm/developer-external-dependencies-20261022/` as
`stability-reads-audit.json`, `stability-audit.json`, `stability-read1.docx`,
`stability-read2.docx` and bracketed file/content-type metadata.


## Binding r2 candidate and native invoker hold — 22 October 2026

A distinct **candidate**, `config/native-document-binding-r2.json`, records the
stable current whole-file hash, logical template/flow references, UI version 1.0
and content-type schema 31. Exact native UID/ETag, current preimage, candidate graph
and guarded forward/reverse patches remain private. The separate r2 input/schema
use template version `PPG-native-word-candidate-v2-binding-r2`; the original schema,
example, configuration, accepted hash and all historical receipts are unchanged.

Fresh exact-target native readback confirms the prior current graph/references
and Draft state are preserved. The live Parse JSON schema equals the original
maintained schema: **the old template hash and version are hard-coded enum values**.
The new input cannot pass that old schema. Its proposed native change is exactly
two enum replacements (templateSHA256/templateVersion); all other actions, trigger,
references and configuration are unchanged. Local validation passes the new
input/schema and selected measured template binding. New-input/old-schema,
old-input/new-schema, missing template hash and wrong source claim all refuse.
Guarded forward application equals the candidate, and guarded reversal restores
the complete preimage exactly. These are local checks, not native save/recovery.

SourceSHA256 remains the fixed fictional operator-supplied claim. The cloud flow
checks that enum and copies provenance into the receipt; it **does not hash source
or template bytes**. The expected new template hash is externally measured. Do not
claim runtime byte verification from a successful Parse or receipt alone.

The existing native details/invoker page opened without usable content. Its initial
snapshot hit the browser's 30-second cap; one bounded cause check found empty
visible text, zero buttons/frames, readyState interactive and no console errors.
No Run form was reachable. This is an invoker/bootstrap availability blocker, not
an observed licence/permission denial. No reload loop, alternative auth client,
flow save/start/run, template/file write or state change was attempted. The r2
candidate remains **unapplied and runtime-unqualified**; existing manual/web outputs
and dated v3 evidence remain usable at their original scopes.

Next, restore the existing native invoker/Run surface through its supported route.
Then re-read exact native preimage/state, apply only the guarded two-value binding
change, verify native schema/references, perform one uniquely identified fictional
run and inspect actual output/receipt lineage. Preserve older/edited outputs and
restore prior Off/Draft state. On uncertainty, reconcile the same native run before
retrying. Roll back only after the current graph still matches the applied candidate;
never reverse unrelated edits. No rollback is needed now because nothing was applied.
Private evidence: `.local/ppg-alm/developer-binding-r2-20261022/`, especially
`candidate-audit.json`, `native-preimage-audit.json`, `invoker-audit.json` and the
forward/reverse test-replace patches. The conditional-feature goal stays blocked.


## Alternate invoker provenance check — 22 October 2026

A newly exposed FlowAgent run contract prompted a bounded offline check before
any target request. Installed configuration points to the inspected server bundle;
its entrypoint constructs composite auth with cloud/endpoints only. The default
non-Connectivity provider is Azure CLI; Connectivity uses a separate MSAL provider.
No required VS Code provider is injected. A no-token list_accounts inventory does
match the existing QH username/tenant and reports identityMismatch false, but
account alignment does not establish the required client/provider provenance.

The retained selected trigger is Request/Button, with accepted JSON serialized in
the top-level text field; it is not Power Apps V2. The installed runner recognizes
Button in its gated-request branch, so this is **not an unsupported-trigger finding**.
Nevertheless the configured provider fails this task's already-qualified-provider
condition. No get_flow/explicit-target read, token acquisition, run, callback,
provider override or cache transfer was attempted. The browser was not retried.
This is a provider-contract hold, not an observed tenant permission/licence denial.

The separate r2 binding, input/schema, guarded patches, historical outputs and
native files remain unchanged. Resume only through an already-qualified supported
invoker with the required provider provenance, or a repaired existing native Run
surface. That route must pass a bounded exact-target read before any guarded r2
binding save and one fictional output/receipt qualification. Do not treat matching
account metadata, a tool description or trigger routing code as runtime access
proof. No replacement client/provider, new login or settings change is implied.
Private configured-source hash/excerpts, trigger and preservation audit:
`.local/ppg-alm/developer-invoker-provenance-20261022/`. The conditional-feature
goal remains separate and blocked.


## Same-client Logic Flows transport check — 22 October 2026

The installed connector-run implementation can be assessed independently of
FlowAgent's unqualified default provider. It discovers shared_logicflows metadata
for the exact environment, takes properties.primaryRuntimeUrl from that response
and uses the API Hub audience for a fresh Button payload. A Flow-resource token
would be wrong. No runtime host may be guessed and no historical input replay
can replace the new r2 binding/input qualification.

The explicitly bounded assessment used the existing **Agents Toolkit mapping in
M365 CLI**, not the separate VS Code Microsoft provider or FlowAgent Azure/MSAL
provider. Its installed SDK selected the one exact existing QH account/app/tenant
and validated SDK identity metadata. Silent acquisition for the Power Platform API
succeeded without an interactive fallback or consent. Normal SDK cache locking
was retained; no selected-connection/profile rewrite, cache reset or credential
transfer occurred, preserving other sessions.

The single exact-environment connector metadata GET then returned **HTTP 401,
AuthenticationFailed** with message “Authentication failed.” The check stopped at
that response. The error does not identify a particular missing permission,
licence, Conditional Access condition or token-audience cause. SDK identity/token
acquisition is not target authorization proof. No alternate API/host/client was
tried, no API Hub audience acquisition followed, and no primaryRuntimeUrl or
qualified invocation URL was obtained. No binding save/start/run, callback or
file write was attempted. The r2 candidate and all historical/native files remain.

This initial check used the DNS-inferred Power Platform API audience and did not
reproduce the installed PPAPI auth contract; the corrected assessment below
supersedes it as the current gate. The original401 evidence remains. Resume only
with evidence that changes that access condition through a supported existing
route, or a repaired already-qualified native Run surface. Do not cycle clients,
request new consent/scopes, guess a runtime URL or treat an unrelated token as API
Hub authorization. Exact private target, SDK identity result, native error and
candidate-preservation hashes are in
`.local/ppg-alm/developer-logicflows-route-20261022/discovery-audit.json`,
`native-error.json` and `qualification-audit.json`. No output/runtime or production
qualification follows; the conditional-feature goal remains separate and blocked.


## Corrected PPAPI audience and preauthorization gate — 22 October 2026

Independent offline inspection corrected the preceding request: the installed
ppapiRequest calls getAccessToken with no resource; composite auth supplies the
commercial default **https://service.flow.microsoft.com**. The per-environment
PPAPI DNS name does not establish its token audience. The earlier api.powerplatform.com
request therefore did not reproduce this contract, and its401 is not correct-
audience target authorization evidence. All earlier raw evidence is preserved.

One changed request attempted supported silent acquisition for that correct Flow
audience through the **same existing Agents Toolkit app/account/tenant**. It failed
with **AADSTS65002 / invalid_request**: the response explicitly requires Microsoft
API-owner preauthorization between the first-party application and resource.
No corrected metadata GET was sent, no runtime URL was discovered, and no API Hub
audience acquisition, binding save, activation, run or output creation followed.
There was no interactive fallback, new consent, scope grant, client/profile switch
or cache transfer. SDK cache access used its normal locking path; other sessions
and the selected connection were not rewritten.

This is now the concrete authorization gate for that same-client transport.
Developer Managed/System Administrator status does not supply API-owner
preauthorization. End-user consent or a licence assignment is not a repair for the
reported65002 condition. Do not cycle app IDs, retry unchanged or infer API Hub
access from another resource's token. The next supported operation is restoration
of the existing permitted native Run surface, or actual changed preauthorization/
access evidence for this same client/resource before a corrected metadata check.
The distinct r2 candidate remains unapplied and its hashes unchanged; last owned
native readback remains Draft, with no subsequent flow-management mutation here.
Private exact source-contract excerpts, silent error and preservation audit:
`.local/ppg-alm/developer-logicflows-flowaudience-20261022/`. The permanent
CHHHSPPGWorkbench/chppg 0.1.0.0 identity, packages and original receipts remain;
no publisher or membership test was repeated. Conditional-feature goal stays blocked.


## Documented Connectivity metadata qualified; API Hub held — 22 October 2026

Microsoft's [Get Connector By Id contract](https://learn.microsoft.com/en-us/rest/api/power-platform/connectivity/connectors/get-connector-by-id)
provides a distinct supported route: global Power Platform API host, Connectivity
environment/connector path, API version 2024-10-01 and required environment filter.
The exact quoted environment-equality filter syntax was checked against the
installed Connectivity URL helper. This is separate from the per-environment
powerautomate route; it uses the Power Platform API OAuth audience, not the denied
Flow audience. Earlier401/AADSTS65002 records remain unchanged for their contracts.

One exact Developer/shared_logicflows GET succeeded through the existing client
and cached silent result, with redirects/retries/fallback disabled. Returned name,
provider ID, Microsoft publisher and isCustomApi false identify the expected
first-party connector. Its primaryRuntimeUrl was obtained from actual metadata,
not guessed from region or copied from another environment. This qualifies that
selected metadata read, not runtime access, a flow run or connector-write authority.

The subsequent separate API Hub silent check initially returned an unverified SDK
result. Source inspection identified a phase/adapter guard collision: the native
GET-only interceptor remained on the SDK's shared HTTP adapter, where it could
block OAuth POSTs; the network shim converts a pre-transport exception to empty400.
That diagnostic is not a policy denial. A single isolated same-client silent
check without a native-operation interceptor then returned the real error:
**AADSTS65002 / invalid_request for https://apihub.azure.com**, requiring Microsoft
API-owner preauthorization for the existing first-party app/resource pair.
No identity guard was relaxed and no native-operation guard was removed from an
invocation. Acquire/validate authorized resource results before installing a
native-only one-send guard; do not let it intercept the owning SDK's OAuth traffic.

The attempt stopped at API Hub preauthorization. No runtime request, binding save,
activation or output/receipt generation occurred. No alternate client, interactive
login, consent, scope grant or unchanged denied-resource retry was attempted.
The r2 candidate and original hashes/receipts remain unchanged. Next: restore the
existing permitted native Run surface, or obtain actual changed API-owner
preauthorization evidence for this same API Hub client/resource before a bounded
runtime preflight. User consent, licence assignment, metadata200 or a token for
another audience is not a substitute. Exact raw metadata/runtime URL, no-token SDK
diagnostic, source-based guard diagnosis and preservation audit remain private in
`.local/ppg-alm/developer-connectivity-route-20261022/`. Conditional-feature goal
remains separate and blocked; the permanent namespace/packages are unchanged.


## r2 published binding verified; output still held — 22 October 2026

The existing native designer became available. Fresh template bytes and identity
matched the distinct r2 binding. One guarded management save created a new draft;
the default management/PAC reads continued to show the older published version.
This was reconciled through native version history and the server-loaded Parse
Code view. No repeat save was sent. The latest draft action matched the candidate
exactly, and native Publish completed. This is technical flow publication only.

The active runtime read added invoker authentication and the two existing
connection names. Those additions were recorded explicitly, rather than treating
raw graph inequality as parity. After one supported stop request returned200,
canonical readback showed **Stopped / Published**, exact candidate definition and
exact original references. The original published version remains in native
history. Logical flow identity, namespace and original schemas/inputs/receipts
are preserved; no new connection, consent, licence or permission was introduced.

The native Test form stalled at Connecting and reported a validation error before
input entry. No input was submitted, Run invoked, run created or output generated.
A fresh details reload became blank. Therefore **current-template output remains
unqualified**, despite the successful binding save/publication. Existing API Hub
preauthorization failures remain separate exact client/resource holds; no denied
resource was retried. Restore the existing native input/run form before the one
unique fictional DOCX and receipt trial. Retain the manual/web route meanwhile.

Earlier dated statements that r2 was unapplied are superseded by this result;
they remain historical evidence. The earlier Developer export still contains the
older published binding and must not be described as a current r2 recovery export.
No package was overwritten or cross-environment import attempted. Conditional
production adoption and the wider goal remain blocked independently.

Private evidence: `.local/ppg-alm/developer-r2-native-trial-20261022/`, especially
`draft-version-reconciliation.json`, `published-parity.json`, raw save/publish/stop
responses and `final-reconciliation.json`. A false raw-parity result in the stop
audit is retained and reconciled by the final canonical candidate/reference check;
it is not an unresolved state or an assertion that no native save occurred.


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


## Current r2 fictional output qualified — 22 October 2026

The fresh details and ordinary native Run form eventually rendered through the
existing signed-in route. After exact current r2/template preflight, one temporary
activation and one unique fictional input produced a Succeeded run with all five
actions successful. No save, publish, resubmission or access change was needed.

Actual DOCX and paired JSON receipt were retrieved and checked: all27 input fields
match the frozen input; output identity/name/size/generation ETag match the receipt;
one row per repeating group, Unicode and optional content appear in complete DOCX
XML. Word opened in Viewing mode with two pages observed; the first page was
visually inspected. This does not claim a new full pagination/zero-many/edit/retry
matrix; the unchanged shape's original dated qualification remains separate.

Viewing changed the DOCX metadata ETag without changing bytes, identity, version1.0,
size or modified time. A second byte read and final metadata bracket prove stability.
The original receipt still retains its generation ETag; it was not overwritten or
silently rebound. Actual template bytes/identity remain exact before/after, and the
prior human-edited output retains its whole-byte hash. The flow is restored to
Stopped, with exact canonical r2 definition and original references. Existing r2
exports remain configuration-current; no repeated export or import was needed.

Retain the raw failed reads/guards: anonymous download401 and browser receipt
read timeouts did not cause another run. The existing authenticated SharePoint
file-read route retrieved the receipt. One SDK cache-persistence error was resolved
with a serialized same-client read. A stop guard initially compared object key order;
it sent no stop request. Canonical exact comparison with the already documented
runtime normalization then permitted one stop200 and verified full readback.

This closes **current fictional Word output qualification**, not production
entitlement/adoption, native restore, managed deployment or human/clinical review.
Source hashes remain operator claims validated by Parse enums; actual source bytes
are not hashed by the cloud flow. Template-byte checks are external pre/post proof.
Private run/input/output/receipt/hash, native Word screenshot, failures and final
readback: `.local/ppg-alm/developer-r2-runtime-20261022/qualification-audit.json`.
