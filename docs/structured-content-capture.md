# Structured content capture and reviewer edits

**PPG Structured Content** stores each captured element with its source identity,
ordinal, text, proposed module and provenance. Reviewer text, reviewed module,
block-review state, optional modifiers and stable section ID are separate fields.
The **Draft body modules** view shows body content with editable reviewer fields;
**Historical V6 content** retains headers, footers, comments and empty elements too.

The first capture contains 171 elements from a separate DOCX inspection conversion
of the recovered historical V6 discharge draft, across 15 proposed modules. Its 21
package parts and the original binary DOC remain preserved. This does not establish
conversion parity, current source authority or an accepted current-template mapping.

## Prepare a capture

```sh
.venv/bin/python -m scripts.ppg_structured_content \
  .local/review-intelligence/capture-inputs.json \
  .local/review-intelligence/new-capture-ledger.json
```

Input supplies the catalogue DocumentUID, immutable source inventory, versioned
module definitions and original-source provenance. The command creates a new file
and never writes to Microsoft 365. Schema and proposed modules are in
`config/structured-content-register.json` and `config/ppg-content-modules-v1.json`.
Use the existing provisioning/create-only seed helpers with actual native field
bindings and the qualified CLI request transport. No new licence or consent is
required for the verified List/library target. Other targets need their own checks.

Each content key binds document identity, capture-package hash and source element.
The same capture replays without duplicate records. New source editions or changed
conversion packages require reconciliation; element positions are not stable
cross-version section identities. Assign StableSectionId only after explicit
lineage review. Proposed modules follow source headings and are not final mappings.

Imported SourceText/ProposedModule/provenance are checked exactly on replay.
ReviewText, ReviewedModule, BlockReviewState, StableSectionId and OptionalModifiers
are never seeded. A difference in imported fields stops rather than overwrites an
existing row; source and native history remain available for reconciliation.
SharePoint forms do not enforce source immutability as an access boundary. Use
ReviewText for proposed edits. Empty source text uses native null while retaining
its element ID, ordinal and XML provenance, so blank elements are not dropped.

## Required and conditional content

Module requiredness is unverified and no mandatory policy-content rules are active.
The model can retain required/conditional rules with source/version/hash evidence
and template verification. Verify applicable local rules before enforcement.
Incomplete drafts remain possible. Missing authority, mapping and source evidence
must stay visible before the affected progression step. The block-review state is
independent of policy lifecycle, approval, publication and ownership states.

## Preserve byte-authoritative originals

A native Word upload/download changed the binary bytes in the first capture
attempt. That Word file is an inspection derivative; its README now points to the
qualified successor. Exact originals are retained inside a ZIP with a hash manifest.
The archive was downloaded, its four members verified, and all 21 nested DOCX parts
matched the retained inventory. Never assume a successful Word upload proves
unchanged source bytes or document fidelity.

For a new preservation archive:

```sh
.venv/bin/python -m scripts.ppg_preserve_source_bytes \
  .local/review-intelligence/new-source-archive.zip \
  .local/review-intelligence/original.doc \
  .local/review-intelligence/inspection.docx
```

This command retains exact supplied bytes, records hashes, verifies archive members
and refuses an existing output or duplicate member names. Include inventories and
other required evidence as additional inputs. It preserves supplied files; it does
not prove that a caller supplied every required source. Verify the downloaded ZIP
hash and member hashes after native storage. Preserve raw inputs and changed human
Word files separately; use new capture revisions rather than overwriting them.

## Native evidence and recovery

171 historical records and both views were read back. Source replay created zero
rows. A separate fictional reviewer edit survived recapture with unchanged native
version; stale ETag update returned 412. This proves block-record edit preservation,
not full Word regeneration. Seven companion files downloaded with matching hashes;
file replay created zero. Current-account rendering is checked; ordinary-user
adoption and native copied restoration remain unverified.

Export source and reviewer fields with version history, source archives, receipts,
module version and section-lineage records. Recover into a separate qualified target
and compare exact keys, original bytes and reviewer text before changing bindings.
Retain the fictional proof row outside the source-specific views. The requested
catalogue edition, current template, complete semantic comparison and complete
mapping remain open under SP-01–04; no clinical decision or issuance follows.


20 October Word preservation diagnostic narrows the original upload mismatch:
fresh stable read shows all six original binary-DOC compound streams unchanged,
with four added MsoDataStore XML streams (SharePoint form/content-type schema and
datastore properties). Whole file hash/size still differs. No original stream removed/
replaced; no rendering/conversion/editing/regeneration proof or source promotion.
Exact-original ZIP and superseded direct-Word navigation exclusion remain intact.
The same companion accounts175unassociated texts with exact hashes and bounded
first-page/6000character title phrases (>=3meaningful words):9sources/11hits, mostly
related instrument/reference prefixes. No title-only identity, link or review credit;
negative/short-title cases remain unresolved, not excluded.985rows/76pairs/
908metadata-only,24source-only reviews/175unappraised/1held/five identities deferred
unchanged. Eight native files byte/GUID/version/inherited-access verified; replay0.
Downloaded183-member CRC/all-hash archive reconstructs compound/XML reports and
complete175-text discovery audit using archived analysis; modified/missing inputs
refused. Existing7z version recorded as external diagnostic dependency; no new
runtime or generator.42focused tests pass. No source/draft/role/flow/run/permission/
notification/issuance or frozen workflow1.4 change. Current V7/template/control
source and full Word behavior remain unverified. See word-preservation-diagnostics.
Next qualify native Word rendering/editing/recovery on a separate derivative through
supported available routes; preserve originals/human edits and verify current inputs.


## 20 October — native Word viewing boundary

A separate clearly labelled historical working copy opens in authenticated Word
on the web and renders the procedure with a twelve-page indicator. The displayed
first page includes its historical version, title, purpose and scope. This proves
viewing of that copy, not full twelve-page visual parity, current authority,
editing, conditional generation or preservation during regeneration.

The qualified CLI resolves the existing site, evidence drive and exact historical
file. Its PDF conversion request returns a redirect; the tokenless redirected
download returns401. No credential forwarding, authentication change or repeated
unchanged denial is authorised. Word's supported Download as PDF UI reaches
“Your document is ready”; selecting Download closes the dialog, but the browser
provides no download within the bounded observation. No exported PDF was recovered
or inspected. This UI route remains unqualified for export.

Private evidence: native-word-render-v1 contains the read journal, original and
working-copy identities/hashes, create-only recipe and viewer screenshot. Re-run
the working-copy recipe only in verification mode once its proof exists: it
refuses changed bytes or versions and never overwrites. Preserve the exact-original
ZIP and previous frozen releases. Recover into a separate working location; do not
replace a maintained draft or infer current-source verification from this test.
Next qualify an actual editable output and edit-preserving recovery through a
supported route. Current procedure/template and full-catalogue retrieval gaps stay
explicit. No approval, issuance, access or notification changes occurred.


## 20 October — native conversion and saved test edit

Word's native conversion creates a separate DOCX while retaining the working DOC.
The UI explicitly warns that layout may have changed. The converted copy opens
with twelve pages and editing mode is available. An explicit development-only,
unapproved-content marker was appended to the isolated copy, then viewing mode
was selected. An input deadline left partial text; inspection preceded completion,
so the marker was not blindly repeated.

CLI download confirms the converted DOCX advanced from1.0 to2.0. ZIP CRC passes;
the marker occurs once, all preceding body text remains exactly unchanged, and all
three embedded media files retain their bytes. The separate original working DOC
remains version1.0 with its prior bytes. Private native-word-render-v1 retains
before/after DOCX, read-only inventory recipe, edit-proof.json and screenshot.
This proves a saved native edit with retained original and body/media preservation,
not full conversion/layout parity, regeneration, restore execution or current
procedure/template authority. Preserve the edited2.0 output; do not rerun conversion
or the original single-file inventory writer against this now two-file folder.
For recovery inspect both file identities/versions and preserve changed drafts;
restore a selected historical version only to a separate location until verified.
Next qualify complete conversion content/layout and recovery, using these exact
before/after files. No clinical content decision, approval, issuance or notification.


## 20 October — separate-copy native Word recovery verified

Restored the preserved pre-edit native DOCX into a separate evidence folder,
with an exact-snapshot ZIP and recovery guide. Three files have matching native
readback hashes, stable identities/versions and inherited access. Replay creates
zero. Before/after reads prove the original working DOC1.0 and edited DOCX2.0
retain their respective identities, versions and bytes; the edit is not overwritten.
The restored DOCX exactly matches the captured pre-edit file.

The downloaded seven-member archive passes CRC and every manifest hash. Its own
before/after DOCX reconstruct the single development marker, unchanged prior body
text and all three embedded media. The archived check-edit.py also references the
original external DOC pair: those raw files are not in this snapshot ZIP; use the
private original preservation evidence for that separate assertion. Do not claim
this archive alone reproduces the original-DOC compound diagnostic.

Native companion: ReviewIntelligence-native-word-recovery-v1/README.md in the
approved review evidence library. Private native-word-render-v1 retains recovery
storage/source-preservation receipts, downloaded ZIP and check-recovery.py/result.
Recover snapshots to a new location, validate manifest and identities, preserve
later edits and refuse changed targets. This is separate-copy snapshot recovery,
not native version-history restore, automated regeneration or complete visual
conversion parity. Current-source/template and catalogue gaps remain open.
Frozen review packs/workflow unchanged; no clinical approval, issuance, source,
access or notification changes.


## 20 October — conversion reconciliation, with unresolved fidelity differences

Compared the preserved inspection DOCX and pre-edit native DOCX: both contain
nine tables, three byte-identical media files, two comments and eight elements
with tracked revisions. Of171 comparable source elements,168 map by exact visible
text/part/kind; three retain explicit differences: first-paragraph text-box ordering
and two cached page-field footers. Native caches ten pages although Word displays
twelve. Two matched elements also differ in empty deletion/insertion-run segmentation;
revision semantics are not accepted as identical. No silent replacement of the
existing171-element capture. Native's179 inventory includes additional separator
foot/endnotes and comment-extension records, not eight new substantive sections.

One hyperlink is represented as a native field instruction instead of an external
relationship. A stale attached-template file URI is retained but not opened or
verified as current-template authority. Preserve both conversions and binary DOC;
full visual parity, field refresh, hyperlink interaction and revision semantics
remain unresolved. Equal counts do not prove fidelity.

Native companion ReviewIntelligence-native-conversion-reconciliation-v2 contains
five byte/identity/version/inherited-access checked files. Its downloaded seven-
member archive passes CRC/all hashes and isolated archived analysis reproduces
both summary and reconciliation without network access. The first v1 archive had
absolute paths; safe extraction refused it. It remains diagnostic with a native
RECOVERY-HOLD notice pointing to corrected v2. Never bypass path validation.
Private native-word-render-v1 holds inputs, analysis, receipts and recovery result.
Frozen review packs/workflow and current drafts unchanged; no source/access/clinical
approval/issuance/notification changes. Next resolve conversion fidelity and verify
current procedure/template authority; current catalogue coverage gaps remain open.


## Read-only required-content diagnostic

[Content presence checks](content-requirements.md) evaluate existing module rules,
reviewed text and explicit scope without changing records or lifecycle. The actual
historical171-row snapshot remains unchanged and reports unverified_rules because
mandatory authority/template rules are not verified. Missing applicability never
becomes an exclusion; content from another scoped variant does not satisfy a rule.
This is developer qualification plus stored web evidence, not a new CLI requirement
for operators or deployed native form enforcement.
