# Unattended package generation

> 23 October closeout: [exact saved-native-body CLI fallback and remaining automatic-flow parity gate](package-closeout-20261023.md). The track is reviewed and archived partial; earlier dated qualifications retain their scope.

For the CLI-only, no-premium-connector preparation/publication increment, use
[CLI package preparation](cli-package-preparation.md). It reuses the selector and
assembler, preserves maintained templates, and verifies create-only SharePoint
package/receipt readback. Automatic Word body population is outside that scope.

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The fixed seven-field cover now has an actual native cloud generation and
packaging proof. Its populated text persists in the saved DOCX; a new fictional
pack includes that cover and the unchanged existing frozen PPG pack. See the
[current cover route and evidence](sharepoint-cover-generation.md). It uses the
existing Standard Office Script packaging runtime, with no AI or premium Word
action. Native request intake and optional Standard PDF conversion are now
qualified for that fixed cover; full combined-document qualification
and the current live-case baseline reconciliation remain open.

Existing-artifact packaging now has native proof for one explicitly frozen case:
case/catalogue/source guards, original-byte assembly, exclusive staged storage,
commit-last receipt, unchanged replay and refusal of stale case/source pins.
The separate local explicit-job runner also remains available. Full unattended
Word generation and production eligibility are still open; the track is active.

The preferred [SharePoint structured document route](native-document-generation.md)
was evaluated first. Existing-account and exact-library form checks have not
established an eligible production generation route. Preserve the current manual
Word route. The qualified existing-artifact assembly records historical authoring as unknown.
The new fixed-field route generates only its own cover and does not establish approval.

The native qualification flow is Off with the accepted legacy definition restored.
The schema2 integration candidate and exact private bindings are retained for the
assigned native writer; upload/run success does not authorize a scheduled service.
No source/case writes, messaging, submission or business review occurs.

## Prepare and run one job

Use the existing Node installation. The maintained source is
`tools/unattended-package/run.cjs`; no package install or network call is needed.
Prepare a JSON job using `templates/unattended-package/job.json` and select actual
files in a dedicated input directory. Supply the existing case reference, title,
candidate version, source baseline and recorded metadata. Do not infer official
identity, roles, approval or evidence categories. Each attachment requires its exact
SHA256 and an assembler evidence role; optional source references remain assertions.

```sh
node tools/unattended-package/run.cjs JOB.json INPUT_DIRECTORY EXISTING_OUTPUT_DIRECTORY
```

Input/output directories must already exist and be disjoint. Inputs are read only;
symlinks resolving outside the input root and traversal paths are refused. Existing
assembler limits apply:200 attachments,100MiB total, safe unique filenames, valid
roles and restricted operator-recorded N/A categories. Missing evidence may remain
in a draft package and is recorded visibly, not silently waived.

The output is `<OUTPUT_DIRECTORY>/<jobId>/package.zip` and `receipt.json`.
The receipt retains raw-job/runner/assembler fingerprint, included input hashes, package
identity/time/hash and DRAFT/missing count. These are technical assembly records;
sourceSnapshot/DocumentUID/business metadata must come from the prepared job, never
be inferred by the runner. It does not discover current native versions or verify
an operator's provenance assertions. No template is populated by this runner;
existing attachment bytes are preserved, and assembler source hash records its version.

## Retry, revision and recovery

A per-job exclusive directory lock serializes cooperating runners. A successful
retry checks selected input hashes and output ZIP hash, then returns replayed without
rewriting output. Changes to job metadata, selected inputs or runner/assembler code require
a new job ID/revision. An edited ZIP causes failure; keep the edited output and use
a new explicit job revision. Extracted working drafts are never touched by this tool.

Output is written in an owned pending directory before final rename. A handled
failure removes only that run's pending directory and lock. A terminated process or
power loss may leave an orphan lock/pending directory. Do not blindly retry or
remove locks: confirm the runner has ended, preserve any partial output for diagnosis,
then remove only the identified orphan artifacts and retry the same frozen job.
No automatic stale-lock takeover, filesystem durability guarantee across power loss,
noncooperating-writer protection or recovery deletion is claimed. Keep one writer for
an output root; do not edit its receipt while a job runs.

## Verification and remaining native work

`node tests/test_unattended_package.cjs` exercises actual generation and replay,
changed job/input/output refusal, input traversal/symlink escape, occupied lock and
disjoint roots. Existing assembler tests also pass. Independent Python ZIP readback
checks CRC, manifest member hashes/sizes, receipt package hash and exact attachment
bytes on the saved fictional output; raw proof stays `.local/unattended-package/`.
The fictional package has seven missing evidence categories and remains DRAFT.

Native selection/generation requires the actual qualified Microsoft route, source
and template versions, generated editable output, access/link readback, human-edit
preservation and retry proof. Scheduling, triggers, destination uploads, messages,
submission, role assignment and production cutover remain unperformed. Nothing in
this runner changes case/catalogue records, sends a package or supplies approval.

## Cloud continuation — 16 October 2026

Conductor identified two separate existing-platform candidates: Developer Word
for fictional output qualification, and Standard Excel Online (Business) Run script
from a SharePoint library for bounded ZIP assembly. The latter uses a PPG-owned
Office Script, not a Microsoft-provided ZIP operation. The kernel is
`scripts/ppg_cloud_package.ts`; the existing source-sync script/workbook/flow are
untouched. It consumes exact ordered members and technical provenance, checks
SHA-256/size, rejects unsafe/colliding paths and malformed base64, and produces
ZIP32 STORE with CRC32, UTF-8 names and an immutable provenance member. It never
reads/writes workbook content or calls a network service.

The cloud candidate currently rejects complete jobs above2MB raw bytes or4MB
request/response payloads, including all members, provenance and base64 overhead.
These conservative bounds sit below the Excel connector's documented5MB request
limit. They are not a replacement for the local assembler's100MiB contract. A
larger required package remains blocked until an appropriate approved runtime is
qualified; no attachments may be dropped or split to imply whole-package success.
See [Excel limits](https://learn.microsoft.com/en-us/connectors/excelonlinebusiness/)
and [Office Scripts limits](https://learn.microsoft.com/en-us/office/dev/scripts/testing/platform-limits).

Local verification: `node --disable-warning=ExperimentalWarning tests/test_cloud_package.cjs`.
Independent Python ZIP readback verifies CRC, complete membership, exact binary/
Unicode/empty content, source hashes and provenance; deterministic replay and
negative paths are checked. This is not native runtime proof.

A distinct helper workbook and exact script were uploaded to an isolated PPG
qualification folder. SharePoint injected metadata parts into the empty helper;
its downloaded package was retained and unchanged worksheet verified. The script
read back byte-for-byte. The first-party UI resolved its two parameters and saved
one manual fictional qualification flow; a saved flow/checker is not a successful
run. Private bindings and status live in `.local/unattended-package/cloud-qualification/`.
No source/case writes, permissions, new authentication, production Word rights or
scheduled/business operation are implied. UP-04/05 remain incomplete until actual
native execution, selection, output readback, replay/recovery and integration pass.

Native ZIP kernel qualification has now produced an actual1254-byte ZIP in a
seven-second Standard Excel connector run. Independent Python readback verified
package SHA-256, ZIP CRC, exact two-member membership, original attachment bytes
and frozen job provenance. Raw action output and decoded ZIP are retained in
`.local/unattended-package/cloud-qualification/native-v2-independent-proof.json`
and adjacent files. The first failed run exposed a string/object response-schema
mismatch; the object-return revision corrected it. Native SharePoint output saving,
record selection, unattended trigger, edit/replay/recovery and full integration are
still unperformed. The subsequent encoded-request cap correction remains locally
tested and must be deployed/read back before claiming that revision qualified.

## Review corrections — 16 October 2026

The local runner now fingerprints both its own source and the exact assembler
bytes executed, independently of Node's module cache. A loaded engine refuses
changed files until restarted; a restarted changed engine refuses replay of an
older revision. Existing receipts made with the earlier assembler-only fingerprint
are preserved and refused for replay; use a new explicit job revision. No automatic
receipt upgrade or output replacement occurs.

Job, attachment and replay-artifact reads enforce byte limits while reading, not
only from an earlier stat. Final-file symlinks in jobs/replay artifacts are refused
on the qualified POSIX route. Existing single-writer/root ownership requirements
remain; this is not protection against a hostile process swapping parent folders.
The cloud kernel also counts generated provenance in its complete raw-byte cap
and escaped JSON parameters in its request cap. These latest source corrections
are locally verified, not native-qualified or automatically deployed. File/directory
path collisions (for example `a` alongside `a/b`) are also refused so extraction
cannot silently lose a member.


## Continued review/native proof — 16 October 2026

The local runner also checks regular-file type before opening, then opens with
nonblocking/no-follow flags and validates the opened handle. This prevents a FIFO
job file from blocking before its earlier regular-file check. A separate-process
regression demonstrates prompt refusal; source and existing outputs are preserved.

The current cloud source was packaged as a new exclusive v4 script revision and
executed successfully through the existing owned Standard Excel flow. The1494-byte
native ZIP passed independent SHA256/CRC, exact membership, attachment bytes and
job/engine-reference provenance checks. Actual runtime script ID/inputs match;
script artifact hash/ETag are unchanged before/after. No Word output is represented:
job metadata explicitly names an unpopulated fictional authoring template.

This closes the corrected-kernel primitive execution gap. Native job selection,
create-only SharePoint output persistence, commit-last receipt/replay/edit recovery,
qualified Word integration, required package-size coverage and production entitlement
remain open. The kernel run was terminal before its browser group disappeared;
unsaved persistence-action preparation is not a saved/deployed/executed action.
The exact existing flow is reopened for saved-state reconciliation. Do not rerun a
successful job or create another flow merely because its editor handle disappeared.

## Native persistence correction — 16 October 2026

A successful HTTP-action run produced a corrupt stored ZIP:1494 valid output bytes
became1504 bytes after upload. UTF-8 replacement exactly reproduces the corruption.
The failed file is retained as evidence, not accepted output. The SharePoint
[HTTP action](https://learn.microsoft.com/en-us/connectors/sharepointonline/#send-an-http-request-to-sharepoint)
has a string body; changing Content-Type does not make that parameter binary.

The corrected fictional revision uses native SharePoint
[Create file](https://learn.microsoft.com/en-us/connectors/sharepointonline/#create-file)
(binary content) in a new, journalled empty staging folder, then native
[Move file](https://learn.microsoft.com/en-us/connectors/sharepointonline/#move-file)
to the existing output folder. The actual selected conflict option is **Fail this
action**; its generated parameter is0 in this qualified graph. Do not infer the
number or overwrite behavior of another action. Create file is confined to fresh
controlled staging, not used as a create-only operation at a stable final path.

The corrected native run succeeded. A fresh exact-run view reconciles the new
job inputs, script identity and output bytes; the earlier in-editor preview had
shown stale prior-run values. Downloaded final ZIP bytes equal the current runtime
result, with matching SHA256, CRC, exact membership, attachment hashes and frozen
job provenance. Script bytes/hash/ETag remain unchanged. The bad earlier output is
preserved. Private evidence: `.local/unattended-package/cloud-qualification/native-v5-*`.

The deliberate same-destination collision failed at native Move file. Final file
identity, ETag, size and SHA256 were unchanged; the duplicate staging file retained
the correct ZIP bytes. The isolated manual qualification flow is Off with no pending
runs. Do not blindly rerun against the populated staging folder or delete evidence.

This proves bounded fictional binary persistence and final-name conflict refusal.
Commit-last completion receipts, native frozen source selection and retry/edit/failure
recovery require their own proof. The distinct Word owner has
verified a repaired single-row fictional DOCX; broader shape/edit/recovery/operator
qualification and production entitlement remain open. No schedule or full-track
completion follows from these results.

## Native frozen-manifest selection — 16 October 2026

The owned manual qualification flow now reads a new, exclusively created fictional
manifest from SharePoint. The manifest supplies exact jobJson/membersJson strings;
the existing kernel verifies member contracts and a frozen job-SHA guard precedes
binary file creation. The successful native run produced a stored1506byte ZIP with
verified CRC, member hashes and exact frozen-job provenance. Source manifest and
script identity/version/hash readback remained unchanged. The flow is Off.

Observed connector behavior matters: Get file content using path returned parsed
application/json, not a binary content envelope. The first expression failed before
creation; bindings now use its actual parsed fields. This proof covers the frozen
fictional manifest, not live case/register selection or arbitrary source acquisition.
The new output has no completion receipt. Reconcile it without recreation before
adding commit-last receipt verification, replay, edited-output refusal and recovery.
Full native Word/operator qualification, required package-size coverage, production
entitlement and end-to-end unattended operation remain incomplete.

## Native existing-output recovery and replay — 16 October 2026

The same owned qualification flow now has a **recovery-only** revision: read the
frozen manifest, calculate expected bytes using the original pinned kernel, read
existing ZIP bytes and package/manifest/script metadata, read the exact completion
receipt path, then commit or replay. Original generation run/definition evidence
remains retained. Recovery has no package create/move actions.

Before receipt creation, typed-binary ZIP base64 must equal the deterministic kernel
result, expected job/package SHA pins must match, and all three native identities,
versions, names, ETags and lengths must match. Only an actual404 at the qualified
receipt path permits exclusive AddUsingPath(overwrite=false); failed/unknown reads
are not assumed absent. Receipt-write retries are None. An uncertain create or
collision requires paired readback/reconciliation, never overwrite or blind retry.
The native1247byte completion receipt was created after those checks and its actual
UTF-8 bytes read back exactly. It binds original job, output revision, package
identity/version/hash, manifest identity/version/hash and original generation pins.

A valid existing receipt selects GET only. Native unchanged replay succeeded with
both artifacts' identities, versions, ETags and hashes preserved. ZIP and receipt
responses exposed different shapes from the parsed manifest: both actual binary
$content envelopes are compared without UTF-8 decoding ZIP bytes or stringifying
an envelope. The initial receipt-shape assumption caused a safe guard failure;
the corrected saved expression and successful native replay are retained.

The edited-output negative case appends an explicit fictional marker to the v6ZIP.
Native version2.0 and its edited bytes remain intact; actual native version1.0
can still be downloaded and its original hash matches. The recovery guard refuses
version2.0 while retaining the original receipt. Thus the latest v6package/receipt
pair is intentionally **not accepted**. Receipt alone is never completion proof.
A deliberate duplicate receipt-create API request also failed with already-exists,
leaving its identity/ETag/hash unchanged. No automatic restoration was performed.

The flow is Off. Independent post-commit/replay readbacks are verified; automatic
native paired rechecks before success remain to implement. This recovery revision
is not yet an integrated fresh-generation pipeline. Actual live-case selection,
Word/package integration, required native package-size coverage and production
eligibility remain open. The separate fictional Developer Word/operator pilot
is qualified; reuse [its guide](native-document-operator-guide.md) and preserved
source/output/template/input pins without moving its connections or ownership.

## Native Word source reads and production-route investigation — 16 October 2026

The package flow's existing SharePoint connection successfully read the retained,
unchanged Developer Word DOCX, its generation receipt and both native file identities.
The actual binary DOCX is9531bytes and matches the preserved original SHA-256;
the actual receipt is2168bytes, whose native UTF-8 bytes were separately hashed
and retained. Its compact serialization differs from the formatted local receipt.
This resolves source access for the next fictional package revision. No Word flow,
source content or connections were changed. The existing v6 edited-output guard
still refused that run as expected; no new package was generated. Fresh details
confirm the qualification flow is Off.

Direct inspection of the signed-in account's assigned subscriptions shows Microsoft
365 E3 and Power Automate for Office365, with neither Power Automate Premium nor
Microsoft365 Copilot listed. Power BI Premium Per User is also listed and does not
qualify Word automation. The package flow's own Details shows its plan is the user
who runs the flow, rather than an established Process allocation. These observations
do not enumerate tenant capacity or rule out another allocated Process flow.
Conductor has no qualified existing production candidate to hand over.

The existing evidence-library Forms pane still exposes the earlier qualification
entries and a server-save error; their names/Live labels do not establish a usable
document-generation form. The prior inspected Word qualification entry opened a
file-upload form. No new form was created or submitted during this investigation.

Production eligibility therefore remains unresolved. The preferred
[SharePoint route](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation)
requires a licensed form maker; the alternative
[Process route](https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/types)
requires actual allocation to the flow. Neither prerequisite can be inferred from
a successful Developer run. Continue native package integration and automatic pair
rechecks independently; retain the current operational manual generation route.
Private assigned-subscription readback and native source-byte/identity receipts are
retained locally. No purchase, assignment, trial or consent change was made.

## Integrated native Word-artifact package — 16 October 2026

The new fictional v7 revision now completes native assembly, guarded storage,
commit-last receipt creation and automatic final pair verification. It consumes
the preserved Developer Word output and its actual generation-receipt bytes;
it does not invoke Word or establish production Word entitlement.

The frozen manifest carries the upstream CaseUID, source snapshot/hash, template
version/hash, included identities and generation revision/run, plus both native
source identities, versions, ETags, lengths and hashes. Attachment bytes come from
the existing SharePoint connector reads. The unchanged packaging kernel verifies
their contracts and generates the ZIP. Independent local and native outputs match.

Creation requires actual404 responses for both the package and receipt, the exact
job/package hashes and captured source pins. Its branch acquires an exclusive
per-job claim with overwrite=false, creates a run-specific staging folder, writes
typed binary bytes and moves the ZIP with collision behavior Fail. Claim, file
write and move have retries None. The claim is retained as attempt evidence; it
is not completion proof. An uncertain claim or incomplete attempt requires
reconciliation rather than deleting the claim or overwriting an artifact.

Both fresh creation and existing-output paths read the saved package and native
metadata before receipt handling. Only matching package bytes, job/hash contracts,
manifest/script pins and source pins permit a receipt operation. An actual missing
receipt permits exclusive creation; an existing exact receipt selects GET only.
The receipt captures the actual output identity/ETag/version and frozen provenance.
Afterward the flow reads package bytes, native metadata and receipt again. Its
final guard requires unchanged metadata, exact ZIP bytes and exact receipt bytes
before the run can succeed. This is checked multi-file completion, not an atomic
cross-file transaction.

| Native proof | Result |
| --- | --- |
| Fresh integrated run | Succeeded: claim, staging folder, binary file, collision-refusing move, completion receipt and all final paired checks. Initial package/receipt reads actually returned404. |
| Actual stored ZIP | 15,119 bytes; exact expected bytes, CRCs, two original attachments and DRAFT provenance independently verified. |
| Actual completion receipt | 2,362 bytes; output native identity, version, ETag, length/hash and upstream provenance agree with independent readback. |
| Unchanged integrated replay | Succeeded; all four creation actions Skipped, recorded receipt method GET, final paired checks Succeeded. Receipt bytes and five native file metadata rows unchanged. |
| Final state | Stopped/Off; exact saved integrated definition and original owner/connection pins verified. Accepted v7 and intentionally edited v6 are preserved. |

An existing Microsoft365 CLI session now qualifies this exact flow's read and
definition update, as well as scoped SharePoint artifact downloads. The UI changes
were saved and reconciled first; a full preimage and rollback were retained.
An initial rejected update left the definition unchanged. The corrected update
uses a shorter receipt expression and explicitly preserves existing connection
references. Fresh readback verified the complete definition before execution.
No authentication, consent, owner, connection or licensing change was needed.

Private native-v7 definition/preimage, runtime action records, stored ZIP/receipt,
replay metadata and integration proof remain in the existing evidence folder.
The v6 recovery proof does not substitute for exercising package-before-receipt
recovery in this integrated graph. That recovery case, integrated negative cases,
required size coverage, live-case selection, actual Word generation orchestration
and production eligibility remain open. The full track is not ready to archive.

## Integrated recovery and edited-output preservation — 16 October 2026

A distinct frozen v8 revision now qualifies package-before-receipt recovery in
the integrated graph. The first run deliberately stops at a read-only guard after
the ZIP is moved and verified, before any receipt write. Its final verification
actions skip and the run fails visibly. Independent readback confirms the exact
15,119-byte ZIP, retained claim and absent receipt; all five accepted-v7 file pins
remain unchanged.

After restoring the normal graph, recovery succeeds with all four creation actions
Skipped. The recorded receipt operation is POST, followed by successful automatic
final paired verification. The original package, claim and all earlier native pins
remain unchanged. The new receipt agrees with the original package identity,
version, ETag, length/hash, job and upstream provenance. Recovery does not recreate
the package or bypass its retained claim.

The fictional v8 ZIP was then intentionally edited. Native version2.0 retains the
same file identity; independent download matches the explicit test edit. Native
version1.0 remains available and its actual REST content download exactly matches
the original ZIP. The CLI's legacy history URL returned401, while the supported
version-content REST route succeeded through the same authenticated client.

An integrated run against the edited output fails at the package guard. All four
creation actions skip; the recorded receipt action is GET to the rejection guard,
and final verification skips. Independent readback confirms the edited bytes,
native version/ETag and original receipt are unchanged. No automatic restoration
or replacement occurs. The latest v8 pair is intentionally **not accepted**.

The accepted v7 definition is restored and verified Stopped/Off with unchanged
owner/connection pins. Its five file metadata rows remain unchanged. Edited v6/v8
and their original histories/receipts stay available as preservation evidence.
Private native-v8 run/action records, definitions, stored pair/history bytes and
recovery-preservation proof remain in the existing evidence folder.

Overlapping native attempts/claim collision, required size coverage, live selection,
actual Word invocation and production eligibility remain open. These completed
fictional recovery tests do not close the full track or permit archive.

## Overlapping attempts and bounded size — 16–17 October 2026

The distinct frozen v9 revision qualifies actual overlapping native attempts.
A temporary60second hold follows successful claim acquisition, before staging.
The contender reaches its claim while the winning run is still in that hold.
SharePoint returns actual400/already-exists for the exclusive claim; contender
staging, file, move, receipt and final-verification actions all skip. The winning
run completes its package, receipt and automatic final pair successfully. The
retained claim names that winning run and remains native version1.0.

Independent winner ZIP bytes/CRC and receipt/native-pin checks pass. Subsequent
post-collision replay succeeds with all five creation/hold actions skipped and
recorded receipt method GET. Receipt bytes and all13 captured file metadata rows
remain unchanged, including the earlier accepted and intentionally edited cases.
The temporary hold is removed after qualification; it is not a scheduled service.

The v10 revision adds a separately attributed fictional binary size fixture to the
two preserved native Word artifacts. It does not attribute that fixture to the
Word generator or count it as substantive evidence. Native reads check its actual
identity/version/ETag, and the unchanged kernel checks its hash and size.

| Size proof | Observed result |
| --- | --- |
| Raw attachments | 1,991,699 bytes across three exact attachments. |
| Actual stored ZIP | 1,996,107 bytes, four members including provenance; exact expected bytes and CRCs verified independently. |
| Serialized kernel parameters/result | 2,659,705 / 2,661,872 bytes. These measure the selected shape, not provider maximum limits. |
| Native completion | Creation, commit-last receipt and automatic final paired verification Succeeded; receipt agrees with actual native output and separately attributed fixture pins. |
| Complete-package oversize | A separate frozen v11 probe uses the same attachments with enough explicitly fictional provenance to exceed the complete raw-package cap. The native kernel itself fails with complete_package_oversize; all downstream actions skip and all18 existing file pins remain unchanged. |
| Local regression | A legal near-limit1,995,000byte binary member now has an independent Python ZIP/CRC/exact-byte check, alongside existing oversize and escaped-wire rejection tests. |

These checks qualify the selected shape close to the conservative2MB complete-raw
and4MB serialized-wire guards; they do not claim the platform's theoretical maximum
or a throughput/load qualification. The negative probe is not a valid output
candidate and was removed after its specific kernel error was verified.

The accepted v7 definition is restored and freshly verified Stopped/Off, with
original owner/connection pins. Accepted v7/v9/v10 artifacts and edited v6/v8
remain preserved. Detailed v9 overlap/action/claim proof and v10/v11 native size
proof, bytes and definitions stay in the existing private evidence folder.

Live-case selection still requires an exact authorised case and matching frozen
source/draft receipts. Conductor has routed that dependency to the existing
Workbench owner; fictional Word identities cannot be relabelled as a real case.
Actual Word invocation/orchestration and production eligibility also remain open.
The full track remains active and is not ready to archive.


## Existing-case artifacts — 17 October 2026

`scripts/ppg_package_selection.py` reads one explicit case and expected CaseUID
through the already authenticated M365 CLI. Supply the private deployment file,
case item ID, expected GUID and a new private output directory. It makes no
source/case writes or authentication changes. Source files are resolved by exact
native GUID, checked before/after download, bounded and independently hash/CRC
checked. Case/catalogue pins are rechecked before selection.json is written last.
A failed attempt retains diagnostic evidence without a completed selection.
Catalogue projection excludes volatile response-wrapper annotations; actual item
ETags and source references remain part of the comparison.

The cloud kernel's schema2 `existing-artifacts` variant is explicitly separate
from legacy schema1 Word-generation provenance. It requires exactly the recorded
baseline, existing manual draft and selection record roles, and pins
`templates/unattended-package/existing-artifacts-format.json` as the assembly
format. Historical Word authoring remains `unknown` with a null generation receipt;
the assembly-format fingerprint must never be represented as a Word-template
fingerprint. Mixed provenance modes or invented generation receipts are rejected.

At this preparation checkpoint, the selector/kernel and uploaded v5 artifact
were verified but native schema2 execution/integration was still pending. The
subsequent native sections below record successful existing-artifact assembly,
storage, receipt/replay and stale-selection refusal. Accepted v4/v7 remain
preserved Off. Full fresh Word orchestration and production eligibility remain
open; existing-library form inspection did not establish that route. No scheduling,
publication or full-track completion is claimed.


## Native existing-artifact kernel — 17 October 2026

The distinct v5 kernel now has native execution proof for the selected shape.

- Fresh read-only selection matches frozen case/catalogue/source pins exactly.
  New manifest uploaded exclusively; native v5 script uses its own distinct ID.
- Temporary four-action probe reads frozen manifest and actual baseline/draft
  through SharePoint, then runs v5. No persistence, claim or receipt actions.
  Initial definition validation rejected an extra expression parenthesis before
  save; corrected candidate saved/read back before the single native run.
- Native run Succeeded. Exact runtime script ID/job/member strings reconcile
  with frozen inputs. Entire result and decoded ZIP match independent expected
  bytes:1,694,459bytes,4members, clean CRCs, exact baseline/draft/selection bytes.
  Provenance explicitly says existing-artifacts, unknown authoring/null generation
  receipt and no Word generation; no historical Word-template claim is invented.
- Probe disabled; accepted v7 definition restored and fresh API confirms Off.
  This qualifies native acquisition/assembly only. Integrated schema2 persistence,
  native source/case guards and receipt/replay remain next; full Word generation,
  production entitlement, UP-04/05 and archive stay open.

Detailed native definition/actions/input/result/ZIP and proof remain private under
.local/unattended-package/live-selection/v12-*. No source/case/Word writer changes.

Postflight read-only selection also matches all frozen case/catalogue/source pins;
v4/v5 script and manifest native identity/version/ETag/length pins are unchanged.


## Integrated existing-case archive and stale-selection refusal — 17 October 2026

Native source selection, storage, receipt and replay now have combined proof.

- Reused the accepted persistence skeleton with the separately qualified v5 kernel
  and frozen schema2 job. Actual case, linked catalogue, original source files,
  manifest and engine identities/opaque ETags/versions/lengths are checked natively
  before source acquisition and again before the completion receipt is considered.
- Fresh native run Succeeded through exclusive claim, run-specific stage, binary
  CreateFile, MoveFail, actual receipt POST and automatic final paired verification.
  Independently downloaded ZIP equals expected1,694,459bytes,4CRC-clean members;
  original baseline/draft/selection bytes and explicit unknown authoring preserved.
- Stored5,259byte receipt equals the expected UTF-8 bytes and binds actual output
  identity/ETag/version/hash, case/catalogue/source pins, manifest and engine.
  It records existing-artifacts, null generation receipt and no Word generation.
- Unchanged replay Succeeded: all4 creation actions Skipped, actual receipt method
  GET, automatic final pair Succeeded. Receipt identity/version/ETag unchanged
  from the original create response; exact stored pair independently reverified.
- Separate stale-case and stale-draft ETag expectation probes each Failed at the
  intended native selection guard. The real case and source were untouched.
  All10 dependent source/assembly/package/receipt/final actions Skipped in each.
- After both probes, all5 output/receipt/claim/manifest/script native pin rows and
  independently downloaded ZIP/receipt bytes are unchanged. Accepted v7 definition
  restored with original connector bindings; fresh readback confirms Stopped/Off.

Private v13/v14 candidates, runtime records, stored pair and correlated proof stay
under .local/unattended-package/live-selection/. This closes the existing-artifact
integration increment. It does not invoke Word or establish a production Word
entitlement. Full UP-04/05 acceptance and archive remain open; operator handoff and
that production-generation prerequisite must retain their actual evidence levels.

## Native per-job preparation and optional PDF — 19 October 2026

The owned M365 flow now reads the maintained SharePoint request and prepares the
frozen job in its existing Office Script invocation. Per-run local manifests are
no longer required for the cover-and-existing-frozen-pack route. Native receipt,
replay and actual output evidence qualify this bounded route independently of
the still-held live-case consumer and full combined-document requirements.
See [the current operating steps](sharepoint-cover-generation.md#m365-request-to-output-route--19-october-2026).
The script accepts its existing two parameters; `m365-cover-request-v1` adds the
native intake contract, and `scripts/ppg_native_package_flow.py` builds the owned
manual-only flow without making API calls or storing tenant bindings in source.
