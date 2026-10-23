# Policy editions and native SharePoint document management

> 23 October 2026: [archive edition closeout](archive-edition-closeout-20261023.md) records qualified native interruption/recovery and zero-write replay. Real-family migration remains pending established evidence (zero eligible families). Earlier dated limitations below are historical.

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Implemented 15 October 2026 in the existing evidence library. Use the library's
view selector: **Policy editions — all**, **unconfirmed**, **verified current**
or **historical**. Existing all-files and CMO archive views also display source
edition, policy currency and the built-in SharePoint Version column.

## Two distinct kinds of version

**Policy edition** records the version stated in the source policy. Each captured
edition remains a separate preserved file, linked/grouped by established policy
DocumentUID. A capture date, larger edition number or later upload alone does not
establish current authority. Older editions remain discoverable alongside newer
ones; use **Replaces edition** only when the relationship is evidenced.

**SharePoint Version** is native file/item history in this workbench. Versioning
was already enabled (500 major versions); native metadata edits create historical
versions. It does not reconstruct publication history before capture. No historical
capture was uploaded over another file, backdated, renamed or promoted to current.
The inherited version limits remain unchanged; this is not a new retention policy.

## Native columns

| Column | Meaning |
|---|---|
| Policy document identity | Established DocumentUID shared by the policy's editions; unresolved stays blank |
| Policy edition (source stated) | Version printed in the policy; separate from SharePoint Version |
| Policy currency | Unconfirmed, Verified current, Verified superseded or Verified withdrawn |
| Replaces edition | Link to the earlier preserved edition this file demonstrably replaces |
| Authoritative source | Canonical source supporting the currency finding |
| Currency checked on | Date of actual verification, not capture/upload date |
| Currency verification evidence | Who checked, findings, exact version and supporting references |

All are native SharePoint library columns, defined in
[field configuration](../config/policy-edition-fields.json). They are optional
because the library also holds templates and operational receipts. A blank currency
displays **Unconfirmed** and is included in the unconfirmed view. All 533 captured
policy files are currently unconfirmed, with no inferred identity assignments.
Verified-current and historical views are empty until actual findings are recorded.
The views filter the captured-policy area and current supported archive formats
(PDF and preserved Office `.captured` files); index/manifests are excluded.

## Add an older or newly captured edition

1. Preserve its original bytes as another distinctly named capture, together with
   source URL, capture date, filename/size and SHA-256 in the existing archive
   manifest/index workflow. Preserve the existing Office `.captured` convention.
2. Record a known policy identity and source-stated edition only with supporting
   evidence; leave unknowns blank. Never mint catalogue identities here.
3. Retain Unconfirmed until a person checks currency. Record the source, date,
   checker/findings and evidence for a verified state. These fields record a human
   finding; no automated substantive review or approval workflow was added.
4. Link a demonstrated predecessor through Replaces edition. Keep both captures;
   use native grouped views to see the editions together.
5. Native Version history records later edits to each captured file's metadata.
   Do not use Restore on an archive original as a way to manufacture policy history.

Future maintained working documents can use a canonical file with native revision
history after their editing/issuance route is qualified. The archive remains
preserved reference evidence. Native content approval/check-out and permissions
were not changed: enabling them across this mixed library could affect existing
working flows and visibility. A verified currency finding is not a policy approval.

## Verification and limits

- Native schema readback confirms seven fields and expected types/choices.
- Four native views render counts 533 all, 533 unconfirmed, zero verified current,
  zero historical. Reapplication adopts the same seven fields/four view identities.
- A disposable fictional file retained native versions 1.0, 2.0 and 3.0 across
  two metadata updates; its bytes stayed unchanged. The fixture was recycled.
- Library versioning, approval/check-out settings and inherited permissions match
  the preflight. No original archive item or catalogue identity was updated.
- One downloaded archive file matched its preserved SHA-256. This is a spot check,
  not a repeated full 533-file audit; the previous complete audit remains evidence.
- SharePoint web shows the native columns/grouped archive view. No new Teams
  desktop acceptance or policy-currency assessment is claimed.

Native bindings, field/view provisioning snippets and detailed readbacks remain
private in `.local/policy-versions/`. Future acquisitions must update the archive
manifest and verify their bytes; adding these fields alone does not discover or
upload further historical versions.

Microsoft references: [native version history](https://support.microsoft.com/en-us/sharepoint/lists/documents-and-library/how-versioning-works-in-lists-and-libraries),
[versioning configuration](https://support.microsoft.com/en-us/sharepoint/lists/documents-and-library/enable-and-configure-versioning-for-a-list-or-library),
[version history limits](https://learn.microsoft.com/en-us/sharepoint/document-library-version-history-limits).

## Maintenance and revalidation — 16 October 2026

The existing seven fields and four view identities were revalidated against the
live library. Native queries account for 533 all/unconfirmed captures and zero
verified-current/historical captures; no policy identities or currency findings
were assigned. The blank-currency formatter and archive/CMO version columns remain
present. Library settings, original metadata and view identities are preserved.
A native archive item still exposes its 1.0 history and matches its preserved
byte hash. The earlier disposable three-version fixture proof was inspected and
retained; it was not recreated or presented as a new substantive currency check.

The maintained [view contract](../config/policy-edition-views.json) complements the
[field contract](../config/policy-edition-fields.json).
[The maintenance audit](../tools/policy-editions/maintain.js) runs in the existing
authenticated SharePoint page with private `base`/`libraryId` bindings and both
configuration objects. It reads and adopts matching fields/views without edits;
missing objects, unexpected choices/columns or query/settings drift stop the
check. It is read-only, not an automatic repair/provisioning command. Use the
existing qualified native setup route to resolve actual drift; do not rewrite
archive originals to make a check pass.

The guide, field contract and optional maintenance ZIP are available in the
existing evidence library's Templates folder and through the existing Start Here
archive guidance. The maintenance ZIP contains this guide and both configurations;
it downloads for operator/developer use, not execution in Teams. Repeating the
audit creates no columns, views, documents or status rows. Deployment receipts and
live tenant identifiers stay private in `.local/policy-versions/revalidation-20261016/`.

These fields record actual human verification when later performed. They do not
enforce substantive review or prove that a selected currency value is justified.
Record the canonical source, exact edition, real check date, checker/findings and
evidence before using a verified state. The fields remain optional across this
mixed library; hosting/uploading a capture does not make it operative. Additional
historical acquisitions follow the existing manifest/byte-verification workflow.

## Archive expansion — 17 October 2026

The completed public recovery records 657 distinct preserved captures: 637 documents
and 20 supporting pages, with no currency findings. All 105 distinct document byte
streams in the retained named-archive inventories are represented within that larger
collection. The 44 previously missing streams were recovered from original public
URLs with exact archived hash/size matches, uploaded, and byte/metadata read back.
There is no remaining known document-byte gap in the retained inventories.

Forty source-header editions link to exact existing catalogue identities; no new
identities, replacement relationships or currency findings were inferred. Eight
additive capture/evidence columns and two provenance/source-locator views complement
the seven edition fields. Distinct captured bytes remain separate even when URLs,
filenames, document codes or printed editions match; identical bytes retain all
known source occurrences. Native file history remains separate from policy editions.

The earlier 17 October checkpoint recorded 613 captures (593 documents and 20 pages)
and 44 missing document streams. Its native policy-view readback was 593 all/unconfirmed,
zero current and zero historical, excluding supporting pages. Those counts describe
that checkpoint, not a fresh view-count query after recovery. Existing view IDs and
original bytes remain preserved.

Only original ZIP/WARC/member exhaustiveness remains gated by original-media access;
additional uncatalogued editions cannot yet be ruled out. See
[archive reconciliation](archive-reconciliation.md) and the private
`.local/archive-reconciliation/online-recovery/completion-audit.json` with its pinned
native upload, metadata and final-inventory receipts. Actual policy currency and
approval remain later business work.

## Native histories for source editions — 17 October 2026 clarification

Separate captures and per-capture edit history do not alone satisfy the user's
request for each policy's editions within one SharePoint version history. The
edition-history planner and native checkout/append/check-in writer are documented
in [archive reconciliation](archive-reconciliation.md#native-edition-history--user-clarification-17-october-2026).
Two fictional source editions were saved and downloaded as native versions 1.0 and
2.0; repeat produced no extra versions. This is a qualified technical fixture,
not a claim that real policy families have been migrated. At that first qualification checkpoint, forty exact linked captures had forty
different DocumentUIDs, so there was no evidenced multi-edition family among them. Preserve unresolved captures and original
bytes until identity and edition ordering are established. Do not present native
import times or native version labels as original publication dates/editions.

The later full-page check now records45identity links:44with an unambiguous printed
edition and1held because header2.0 conflicts with footer3.0. Five additional links
passed native save/readback and zero-change repeat; one previously automatic edition
value was cleared with its prior evidence preserved, retaining the valid identity.
The current planner has44singletons/1unresolved and no ready multi-edition family.
This supersedes the earlier40-link count; see the expanded edition-evidence section
in the reconciliation guide for correction and preservation receipts.
