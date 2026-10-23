# SharePoint property-prefilled PPG cover

Status, 19 October 2026: **native M365 request-to-cover, existing-pack and PDF
processing demonstrated**. The fixed seven-field cover persists its values as
literal text, and the existing Standard flow now freezes the request within M365.
The pack retains the existing frozen fictional evidence bytes. See the latest
M365 route at the end of this guide for operating steps and qualified limits.
Full combined-document output and live-case baseline reconciliation remain open;
Word for the web edit/save/close/reopen is verified; desktop control remains
unavailable but is unnecessary for the working route.

The original SharePoint-property probe populated all seven properties, but saved
body text remained `[Unresolved]` after a desktop save. That route's failed
persistence qualification remains documented below; the new output does not
silently relabel it as a passing native property refresh.

## Preservation finding: folders do not isolate library schema

Adding five optional cover columns to the existing evidence library propagated
new custom XML into two previously qualified lifecycle Word files. Their document
bodies were byte-identical, but archive metadata, lengths, opaque file tokens
and whole-file hashes changed. The displayed version labels did not change. Workbench's existing byte checks correctly held progression.
Independent archive comparison confirmed the new fields in both files.

**Do not add cover columns to a shared evidence/issued-document library.** A folder
is not schema isolation. Future schema changes require a dedicated generation library with
stable schema established before documents are pinned. The fixed-field snapshot
fallback adds no columns and does not require another library. There is no automatic
schema provisioning in the supplied tool. Existing affected files and proofs
must remain preserved while Workbench reconciles the metadata drift; do not delete
columns, restore files or silently repin hashes as a workaround.

A subsequent native Versions read returned only an older, 21,973-byte draft 1.0
and no issued versions. The qualified 25,039-byte draft/issued pair is preserved
in private snapshots but was not available as selectable native historical
versions. Current labels remained draft 2.0 and issued 1.0 despite changed bytes.
Do not claim version-label stability proves binary preservation or native version
history can restore the qualified pair. Any recovery requires the existing owner
to reconcile retained snapshots explicitly and qualify the resulting new state.

## Prepared implementation

`config/sharepoint-cover-mapping.json` maps seven properties: cover title, case,
document identity, source edition, recorded owner, recorded review date and output
revision. New values use optional Text columns (255 characters); missing business
facts are explicitly `Unresolved`. Dates are accepted ISO date-only text. Longer
values are refused rather than truncated.

The existing Open XML SDK template-authoring tool now supports:

```sh
dotnet build tools/native-document-template/TemplateBuilder.csproj --no-restore
dotnet exec --roll-forward Major tools/native-document-template/bin/Debug/net10.0/TemplateBuilder.dll sharepoint-cover seed NEW-SEED.docx
# Separately upload/download the seed in the selected isolated library, so its
# native metadata supplies the actual property namespaces and datastore identity.
dotnet exec --roll-forward Major tools/native-document-template/bin/Debug/net10.0/TemplateBuilder.dll sharepoint-cover bind NATIVE-SEED.docx config/sharepoint-cover-mapping.json NEW-TEMPLATE.docx
```

This is one-time template authoring, not a local runtime population service.
Existing output paths are refused. The authored template passed Open XML schema
validation. Native templates contain private library bindings; keep them outside
public Git.

`scripts/ppg_sharepoint_cover.py` provides a Standard SharePoint qualification-flow
builder, a read-only DOCX inspector and a guarded existing-kernel member adapter.
The builder performs no API call. Its candidate is Off, uses only the supplied
Standard SharePoint connection, pins template identity/ETag, disables mutation
retries and copies with overwrite=false. A destination collision requires
reconciliation; this probe is not a complete production recovery orchestrator.

```sh
.venv/bin/python scripts/ppg_sharepoint_cover.py DOWNLOADED.docx ACCEPTED-VALUES.json --require-rendered
.venv/bin/python tests/test_sharepoint_cover.py
```

The inspector separately checks actual bound-property values and cached visible
Word text. The member adapter refuses stale text, changed document bytes or
mismatching metadata. Its returned member uses the existing cloud-kernel
`path`/`base64` shape; frozen selection/receipt integration remains unfinished.
A passing inspector does not establish visual layout, links or ordinary-user
acceptance.

## Current operator path

Use the M365 request-to-output steps at the end of this guide. The following
sections retain the earlier property-refresh investigation and fixed-cover proof;
the latest native evidence supersedes their earlier PDF/intake qualification holds.
Workbench retains ownership of lifecycle-file and live-case reconciliation.

## Desktop refresh test completed — 19 October 2026

After the user enabled editing through the existing Word account, the original
fictional cloud cover was opened from desktop Word's Recent list. All seven
bound values appeared correctly in Word for Mac, including the long Unicode
title, case/document identities, source edition, date and revision. The missing
owner remained the explicit value `Unresolved`. No field text was typed by the
agent. The exact cloud document was reselected using fresh accessibility controls
and File > Save invoked.

An independent same-client SharePoint download after that command verified the
expected file identity, stable metadata around the download and all seven values
in the custom XML property store. However, every cached control text in
word/document.xml remained `[Unresolved]`; its bytes matched the pre-save cloud
read. This completes the requested test with a mixed outcome: desktop dynamic
rendering works; persisted body-text qualification does not pass. It does not
prove the populated appearance will survive other renderers or unattended PDF
conversion. Package admission remains refused and the broader increment stays
partial. No licence purchase/assignment, schema change, flow change or other
document edit was performed during this test.

Private proof: `.local/unattended-package/cover-refresh-explicit-save-20261019T104316Z/`
contains exact metadata, downloaded DOCX, seven-field inspection and completion
audit; the earlier readback is retained separately.

## Fixed-field snapshot fallback — 19 October 2026

The native property route was tested first. Its saved-body persistence failure
justifies a bounded fallback in the **existing Standard Excel Online (Business)
Office Script packaging runtime**. This is deterministic fixed-field mapping;
it does not invoke Word Online Business, AI Builder, Copilot or a premium HTTP
connector. It does not establish general Word-template or repeating-table support.

`scripts/ppg_cover_snapshot.py` compiles the maintained blank, bound template into
pinned parts once when preparing a template revision. `ppg_cloud_package.ts`
accepts the existing two native script parameters; an explicit
`standard-cover-input-v1` envelope selects the new route. At run time the script
checks the frozen template parts and seven accepted values, writes escaped
literal text into the seven controls, and detaches their property bindings in
the **new output only**. The maintained template is unchanged. Missing owner
stays `Unresolved`; the fixed DRAFT label remains. The result is a revision
snapshot: later SharePoint metadata changes cannot replace those body values.

The same invocation assembles that cover and the unchanged selected evidence
using the existing bounded ZIP kernel. No local per-run document generation or
desktop save is needed. The source template, manifest and included evidence are
pinned; the native persistence graph retains exclusive claims, staging,
non-overwriting moves, receipt-last commit and final byte-pair verification.
The historical authoring of existing evidence is not attributed to the new route.

The live-case probe correctly refused case/catalogue baseline drift before
creation. Do not repin a case silently or change its records to pass a test.
The separate fictional qualification reuses the already frozen fictional PPG
pack as an unchanged ZIP evidence member. It does not establish that the held
live case is current. The operator opens the new cover in the outer ZIP; the
original evidence remains inside `evidence/existing-ppg-pack-v7.zip`.

PDF remains separately unqualified. A saved populated DOCX and successful ZIP
are not proof of PDF layout or full combined-document generation. Word visual
inspection can also remain independently held when desktop capture fails.

### Native result and shortest use

The actual native script generated a 53,724-byte, four-member package. Independent
SharePoint downloads verified the generated DOCX's seven literal body values,
unchanged existing evidence ZIP, both ZIP CRCs, input/output hashes and actual
native package identity in the completion receipt. The standalone saved cover
also retained identical bytes on repeat download. Word for Mac opened it with all
seven values on one page; Editing and Save were available. A complete ordinary
client edit/reopen trial is not claimed after intermittent desktop-control capture
failures.

Same-job native replay reused the original package and receipt, skipped all four
creation actions and used GET for receipt reuse. A separate edited-cover fixture
was refused and preserved byte-for-byte. A separate package-before-receipt fixture
recovered by adding only its missing receipt. These fixtures did not overwrite the
working pack, cover, template or original evidence. The qualification flow's
original definition and references were restored exactly Off after these runs.

1. Open `PPG-fictional-cover-r5.docx` in the existing qualification output folder,
   or download `PPG-0-fictional-cover-pack-r5.zip`.
2. Extract the outer ZIP and open `cover/PPG-fictional-cover-r5.docx`. No property
   refresh or desktop save is required to see the populated values.
3. Open `evidence/existing-ppg-pack-v7.zip` for the unchanged original evidence.
   Keep DRAFT; edits belong to a new output revision.

For another case, use the existing frozen-selection preparation and the retained
fixed-cover native candidate through its assigned owner. The current live case
must first have its case/catalogue baseline discrepancy reconciled by the owner;
no case change is implied by this example. PDF and full combined-document work
remain separate. The technical private binding/run/output audit is retained at
`.local/unattended-package/cover-snapshot-20261019/`; do not publish it.

## M365 request-to-output route — 19 October 2026

The per-job intake now runs in the existing owned Power Automate flow. The
operator edits a maintained request file's existing seven SharePoint properties,
selects a new output revision and runs **PPG | Generate cover and existing pack**.
The optional request-item ID defaults to the maintained fictional request. This
is a manual start followed by unattended processing; no scheduler is configured.
Native links and exact deployment bindings are in the private handoff.

The flow reads the maintained request/configuration, template, compiled template
parts, existing frozen pack, its frozen job and completion receipt. It verifies
native versions and source hashes, freezes the job in M365, invokes the maintained
Office Script, then stores DOCX, ZIP, immutable claim and completion receipt in
SharePoint. No locally prepared JSON or local generator is needed for each run.
Compiling a changed maintained template remains a one-time authoring task.

The request is a snapshot of recorded facts. Blank optional owner/date values
remain `Unresolved`. It does not infer review, approval or current source currency.
Only the **existing-frozen-package** selection is qualified by this increment.
A live-case mismatch cannot be bypassed by describing the source as current.

The optional PDF step runs after the verified DOCX/package commit. It copies the
cover to the existing OneDrive scratch folder, waits briefly for availability,
uses Standard **Convert file** with at most two bounded retries, and stores and
reads back the actual PDF in SharePoint. Its separate create-only success receipt
pins the parent cover/package and saved PDF. Same-job PDF replay verifies/reuses
the receipt and file identity/version rather than converting again. A changed PDF
is retained and reported. A conversion failure leaves the core receipt, DOCX and
ZIP usable; the flow records a separate `pdf-failed-<run>.json` status and exposes
`PDF_outcome` in run history. Retry the same unchanged revision to recover PDF.

The deployed connector inventory is Standard SharePoint, Excel Online (Business)
and OneDrive for Business. No Word Online Business, premium HTTP, AI Builder or
Copilot action is present. The preferred SharePoint structured-generation route
still requires separate tenant/template/entitlement qualification for broader
shapes; this fallback does not establish that availability.

Operating steps:

1. Open the maintained request in SharePoint and edit its existing cover
   properties. Keep the frozen case identity consistent with the selected pack.
2. Enter a new lower-case output revision (letters, digits and hyphens, at most
   40 characters). Preserve the previous revision when changing inputs or editing
   its output.
3. Run **PPG | Generate cover and existing pack**. Leave the optional ID blank for
   the maintained request. Read `Core_complete` and `PDF_outcome` in run history;
   the saved DOCX, ZIP and receipts are in the existing qualification folder.
4. Download/open the ZIP for its cover and unchanged evidence pack, or open the
   separately saved DOCX/PDF. All generated documents remain DRAFT.
5. For a transient failure, run the same revision again. Completed matching
   outputs are reused. Input changes or altered output are refused; enter a new
   revision rather than replacing the retained document.

This route is bounded to the existing kernel's 2 MB complete raw-package / 4 MB
wire guards. Full combined Word output, repeat groups and conditional sections
remain separate work. A separate generated copy passed ordinary Word for the web edit/save/close/reopen:
the typed edit and all seven original values persisted in an independently
downloaded cloud DOCX and appeared in the reopened viewer. Desktop Word control
continued to time out; no desktop refresh is required by this route.
