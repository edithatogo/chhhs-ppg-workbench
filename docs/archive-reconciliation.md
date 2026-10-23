# Archive reconciliation and edition preservation

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

## Current completion — 23 October 2026

[All4 tasks are implemented, reviewed and archived](archive-reconciliation-closeout-20261023.md).
Both original ZIPs recovered with exact independent backup identities;724 members,
8 WARCs/1,986 records and606 Office parts accounted. Two earlier HTML captures
were separately preserved. All659 native captures independently downloaded and
hash-verified (637 documents22 pages); original667 file frames preserved and every
source/metadata/control replay0writes. The original-media blocker is resolved.
Older counts, unavailable-media statements and partial receipts below are dated
history; do not rerun those recoveries. Edition-family/authority decisions and
user-deferred third-party testing remain separate.

As of the completed public recovery on 17 October 2026, native readback records
657 distinct captures: 637 documents and 20 supporting pages. The complete expected
SHA-256 set matches native readback. All 105 distinct document byte streams in the
retained inventories of the two named archives are represented. Those 105 streams
are a subset of the 637-document collection, not a count of the expanded corpus.
All 44 previously missing streams were recovered from their original public CHHHS
URLs, matched to archived hashes and sizes, and uploaded/read back successfully.
No known document-byte gap remains in those retained inventories.

The original 533-file import covered the retained expanded corpus, not both named
ZIPs exhaustively. The named-archive inventories contain 666 source occurrences
and 548 distinct resources. Of their 105 document streams, 104 were absent from the
original import: 60 retained copies were uploaded first, alongside 20 supporting
pages; the later 44 public recoveries completed the known document-byte set.
Uploads preserved original bytes without overwrite. Subsequent capture-metadata
edits create native history without replacing those bytes.

The remaining original-media gate is full ZIP/WARC/member exhaustiveness: the
retained inventories cannot establish whether the original archives contain further
uncatalogued documents or editions. DM remains unavailable in the latest device
readback. Do not repeat completed recovery uploads or infer policy currency.
Retained evidence and native receipts are in `.local/archive-reconciliation/`;
`online-recovery/completion-audit.json` pins the five final recovery receipts.
The Conductor tracks remain open for the original-media audit.

## Native edition model

Reuse the existing evidence library, native file history and seven policy-edition
fields. Each distinct byte stream is a separately preserved capture. Identical bytes
may be stored once with all source occurrences retained. Never collapse different
bytes because their filename, URL, document code or printed edition is the same.
A SHA-256 identifies captured content; established DocumentUID identifies a policy.
These identities are deliberately separate. Source URL grouping is navigation only.

Eight additive optional capture fields expose SHA-256, original filename, exact URL,
recorded capture time, source occurrences, source-URL grouping key, document/page
kind and separate edition-link evidence. Capture timestamps are stored in UTC and shown using SharePoint regional settings.
Unknown capture times remain blank; the archive date stays in provenance.
Native policy currency and identity fields are not inferred or overwritten.

Use **Archive captures — provenance** to inspect these fields, or **Archive
captures — source locator** to group by the exact source URL. Existing policy
edition/current/historical views retain their identities and now exclude explicitly
labelled supporting pages. Documents without a recorded capture kind remain visible. Neither document kind nor a policy view proves
that an item is an operative policy. Index/control files are excluded from the
new capture views by requiring a populated capture SHA-256.

Metadata application uses the exact item ETag, refuses differing nonblank values,
reads back all intended fields, preserves policy decision fields, and hashes the
actual bytes. Reruns adopt matching fields/views/files and avoid unchanged metadata
writes. Never overwrite a capture or use Restore to manufacture policy history.

## Supported capabilities and boundaries

Existing native versioning retains500major versions; existing permissions, approval,
checkout settings, source importer and case data remain unchanged. The live library
contains Document and Folder content types. Document Sets are not configured here;
no feature activation or migration was undertaken. Keeping independently preserved
captures is appropriate while policy-family identities remain unresolved.

Autofill can extract suggestions, but existing isolated pilot prompts remain Off.
Microsoft currently documents Copilot licensing and, for advanced site-wide
processing, usage-based billing prerequisites. No new entitlement, processing,
settings or billing authority is implied by this archive increment.

References checked17October2026:
- https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-get-started
- https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-create-autofill-columns
- https://learn.microsoft.com/en-us/graph/api/resources/documentset

## Continue when originals are available

Identify DM from the live disk listing, mount read-only if necessary, verify both
ZIP hashes and enumerate every original member/resource. Compare actual bytes to
the retained inventories, including duplicates, failed captures and unselected
items. Extract and upload every missing document byte stream; account explicitly
for non-document site assets rather than calling them policies. Preserve distinct
versions at changed URLs as well as at a single URL. Resolve source-stated editions
and established policy identities only from supporting evidence. Record current or
superseded status only after actual currency verification, which remains later
business work. Finish native count/hash/repeat/navigation and preservation checks
before closing either track.

## Exact edition linkage

Fresh first-page PDF extraction is constrained to a single explicit Document Number
header and a single printed Version. Link only an exact, unique live-catalogue
source alias to its already-established DocumentUID. Do not strip versions, merge
families by title or create identities. Conflicting code/printed editions remain
unresolved. The source PDF SHA-256, extracted header hash, exact alias, catalogue
item and existing UID are retained separately in Edition linkage evidence. These
checks qualified and recorded40exact links; remaining candidates and the full original ZIP audit
are not thereby resolved. The native link writer rechecks the catalogue at the
point of application, uses an exact item ETag, refuses existing differing values,
and preserves currency, verification, replacement and authority fields.

## Earlier available-collection acceptance — 17 October 2026, before public recovery

All613unique capture hashes were read back natively:593documents and20supporting
source pages. Original533and additional80byte hashes and provenance metadata passed.
Forty exact edition/identity links were saved/read back; their full native repeat
made zero metadata writes and retained exact file pins. Reapplying the80additional
files adopted all80existing files, downloaded matching hashes and uploaded no new
files. The sample displays source edition4.0 alongside native Version3.0 and an
existing DocumentUID; its older native history1.0/2.0 downloads match the original
SHA-256. Native policy views return593all/unconfirmed,0verified current and0historical,
with no supporting pages included. Twelve unrelated views and all library settings
were preserved during the four-view filter adjustment.

At this earlier checkpoint, 44 known document byte streams were unavailable and
ZIP/WARC/member completeness needed original-media access. The later public recovery
below supersedes that missing-byte finding; the original-media audit remains open.
The 613-capture counts and policy-view counts above are historical readbacks.

## Public website recovery — 17 October 2026

All44known missing document byte streams were downloaded from their original public
CHHHS URLs and match the retained archive SHA-256 and size exactly (40,583,077bytes).
These are exact recoveries, not newer substitutes. Downloads retain HTTP final URL,
ETag/Last-Modified when supplied, retrieval time and original archive occurrences.
They include governance terms of reference, privacy/service plans, research forms,
clinical alerts, surveillance updates, registers and other supporting documents;
not all are policies. Recovery removes the known missing-byte dependency on DM.
Original ZIP/WARC/member exhaustiveness remains unverified until media access.

Native recovery receipts and the URL-by-URL report are retained under
`.local/archive-reconciliation/online-recovery/`. Original archive indexes and
earlier613-capture guidance remain dated snapshots, superseded by this recovery
for the missing-byte finding. No policy currency finding follows from a public URL.

The44recoveries are now uploaded and native byte/metadata verified. Native counts
are657distinct captures:637documents and20supportingpages. The complete expected
SHA-256 set matches native readback. All105distinct document streams in the retained
named-archive inventories are therefore represented; raw ZIP/WARC exhaustiveness
is still unproven. Public-website-recovery-20261017.md/.json in the reconciled capture
folder supersede the earlier44missing-byte finding. Currency remains unconfirmed.

## Native edition history — user clarification, 17 October 2026

The user explicitly requested editions within SharePoint version history, beyond
separate capture files. Original captures remain the immutable evidence layer;
a family history is a separate, clearly labelled navigation projection in the
same library. It does not become an approved/current document. Source publication
edition, capture date and native import version/time remain distinct.

`scripts/ppg_edition_history.py` plans histories only from established DocumentUID
and evidenced printed editions. It orders numeric editions, preserves duplicate
occurrences and holds same-edition/different-content conflicts. Similar filenames,
titles or version-stripped codes never establish identity. Its private input rows
contain `documentUID`, `identityEvidence`, `sourceEdition`, `sha256`, `bytes` and
canonical `sourcePath`. Run it with private input/output JSON paths. Its `ready`
records contain ordered editions; `singletons` are not multi-edition histories.
Bind library ID and target path privately before native application.

`tools/archive-capture/edition-history.js` exports the page-context function
`reconcileEditionHistory(base, manifest, state)`. Production targets are restricted
to `PPG Review Evidence/Policy Edition Histories/<DocumentUID>.captured` within the
bound site. Prepare that inherited-permission folder through the existing qualified
SharePoint route only when there is a qualified multi-edition family. The writer
checks native source identity/edition evidence, all source hashes and library
versioning settings before writing. It creates the first edition without overwrite,
then explicitly checks out the target, rechecks its content, appends and checks in
with source-edition/hash comments. Existing captures are read-only. It downloads
all native historical bytes, maps native version labels to source editions, and
adopts only a complete known prefix. Reapplication makes no writes when complete.
Maintain one native writer per target, including sessions using the same account.

Do not rely on `If-Match` alone for binary updates: an isolated fictional native
qualification accepted a deliberately stale marker with HTTP 204. That earlier
fixture remains clearly fictional as diagnostic evidence. The replacement checkout
route saved two fictional editions as versions 1.0 and 2.0; both downloaded hashes
matched, originals retained their pins/bytes, and a full repeat made zero writes.
The native version-history page rendered both entries and the edition/hash comment.
This proves the two-edition text fixture; real PDF/Office family application still
requires that family's qualified inputs and downloaded-output readback.

On failure after checkout, retain the exact task state and target. Do not discard,
restore, delete or blindly retry it. Read back checkout owner, content, history and
receipt before explicit recovery/check-in; preserve any unrecognised edits. A
network observation timeout does not establish that the append failed. Read the
same operation handle and native target before retrying.

At the first native-history qualification checkpoint, native discovery found
40 linked captures across 40 established identities, with no multi-edition family. No real policy history was
fabricated from these singletons. The remaining captures retain unresolved family
links. Qualification receipts, the live discovery and private planning output are
in `.local/archive-reconciliation/native-version-history/`. This increment leaves
real family histories and the original ZIP/WARC/member audit open.

Supported API references checked 17 October 2026:
- https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/working-with-folders-and-files-with-rest
- https://learn.microsoft.com/en-us/sharepoint/version-overview

Full retained-capture discovery on17October checked657hash-verified local originals;
550werePDFs and97had recognisable first-page document-number headers. No multi-edition
candidate group emerged from that header comparison. This does not establish identity
for headerless/non-PDF captures or prove original-media exhaustiveness. Native final
readback still matches the exact657capture hash set (637documents20pages), with no
currency findings. Increment receipts are pinned in `native-version-history/increment-audit.json`
under the private archive-reconciliation evidence directory.

## Expanded edition evidence and conflict correction — 17 October 2026

Full first-page revalidation now checks for conflicting printed editions beyond the
1,500-character primary header window. Equivalent numeric forms such as 3 and 3.0
agree; 2.0 and 3.0 do not. Identity still comes only from an exact unique native
catalogue alias, never a title or version-stripped code. The additional discovery
produced five new exact edition/identity links, saved and read back; their repeat
made zero changes. Five of the thirteen additional candidates passed the full-page checks; eight
remain unresolved.

Of the earlier forty links, thirty-nine passed full-page revalidation. One source
has header edition 2.0 and footer edition 3.0. Its exact existing identity remains
linked, but the previously automatic edition value was cleared using an exact item
ETag after confirming the prior automatic fields/evidence were unchanged. The new
unresolved evidence retains the original automatic evidence, both conflicting
values, source/header hashes and correction time. Native item-history readback confirms edition2.0 in version3.0 and the unresolved
correction in version4.0, preserving the earlier field value. Source bytes and all currency/authority fields are intact.
No decision was made about which printed edition is correct.

The latest native state is **45 identity links: 44 with an unambiguous source edition,
one with edition unresolved**. The native-history planner reports zero ready
multi-edition families, 44 singletons and one unresolved record. This supersedes
40 as the current link count; earlier receipts remain dated history. The exact
657-capture hash set is unchanged: 637 documents and 20 supporting pages, with zero
currency findings. No real policy family history has yet been created.

Private current evidence is under `native-version-history/` in the existing archive
reconciliation evidence directory: `additional-five-native-proof.json`,
`edition-conflict-correction.json`, `prior40-first-page-revalidation.json`,
`latest-edition-readback.json`, `latest-history-plan.json` and
`expanded-edition-audit.json`. Remaining original-media and unresolved-family gates
are unchanged. Recovered bytes do not need to be uploaded again.
