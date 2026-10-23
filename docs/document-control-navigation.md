# Draft, reference and issued-source navigation

> Current native recovery/reporting increment: [21 October qualification and restart procedure](recovery-qualification-20261021.md). Earlier sections retain their dated scope.

Use the existing List/library view selector; no new app or Teams tab is required.

| Need | Route | Meaning |
|---|---|---|
| Find local drafts | Case List → **Working drafts — case links** | Recorded draft/evidence link first, with missing links explicit. All cases remain visible. |
| Inspect preserved reference copies | Evidence library → **Document control — references and authority** | Captured references and supporting source pages, with provenance and uncertainty visible. |
| Check an issued source | Reference card → **Find version-specific publication evidence — verify issued source** | Existing assurance records filtered to Publication. Verify exact edition, recorded state and authoritative source; a record alone does not authorise issue. |
| Open recorded authority | Reference card → **Open recorded authoritative source — verify exact issued edition** | HTTPS authority link when recorded. Missing evidence remains unresolved; source/capture URLs do not substitute for authority. |
| Find previous editions | Reference card → recorded predecessor or **Browse previous/superseded/withdrawn findings** | Existing evidence-backed predecessor link and historical view. Empty means no recorded finding, not no historical editions. |
| Inspect unresolved edition conflicts | Reference card → source edition and edition-linkage evidence | Blank edition is missing/unresolved. Raw linkage evidence retains conflicting findings; navigation does not choose a winner. |

The reference view covers capture-hash-bearing files under the existing captured
archive, including root and nested files. It excludes similarly named adjacent
folders, templates, control files and working material outside that archive.
Supporting pages are labelled as supporting pages, not policy authority. The case
view uses existing case links rather than guessing drafts from filenames/folders.
No new classification, approval or lifecycle fields are introduced.

## Authority and version distinctions

A blank/Unconfirmed currency remains **Captured reference — authority unconfirmed**.
A recorded verified state without authority link, check date or evidence is
**Recorded finding incomplete — authority unresolved**. Unknown currency values
remain explicitly unknown. A complete recorded current finding prompts verification
of the issued source; historical/withdrawn findings remain reference-only.
These are evidence-completeness labels, not automated judgements about currency,
approval, clinical correctness or whether someone has authority to issue.

Policy edition is the edition stated in source evidence. Native file Version is
workbench revision history; it does not establish original publication dates or
policy currency. Preserve distinct captured bytes, unresolved identity/edition
links, previous findings and human-edited drafts. The existing archive index and
edition views remain available; no original-media completeness, retention or backup
guarantee is added. See [archive reconciliation](archive-reconciliation.md) and
[policy editions](policy-editions.md).

## Configuration and repeat verification

[Configuration](../config/document-navigation.json) and
[compiler](../scripts/ppg_document_navigation.py) reuse the existing guided case
formatter and path/readback validation. Keep actual bindings, IDs and native exports
in ignored `.local/`. Bindings use `site`, `queue_path`, `readiness_path`,
`assurance_path`, `library_path`, `current_view_path` and `historical_view_path`.
Read the latter two from the existing exact-title native edition views; do not
construct or guess their filenames. Fields use native InternalName/TypeAsString.

```sh
.venv/bin/python scripts/ppg_document_navigation.py \
  --bindings .local/records-navigation/bindings.json \
  --library-fields .local/records-navigation/library-fields.json \
  --case-fields .local/records-navigation/case-fields.json \
  --output .local/records-navigation/bundle.json
```

The exclusive output contains `case` and `library` create/formatter definitions;
the library's Scope is separate and must be applied/read back. For verification,
replace `--output` with `--verify-readback` and a private JSON export containing
`case` and `library` arrays of views with expanded ViewFields. The command is
read-only and refuses missing/duplicate titles or property drift, including scope.

Use the qualified same-client CLI route for native operations. Before mutation,
read both exact targets' permissions/schema/current views and preserve item and
library-setting snapshots. Enumerate rules/subscriptions without changing them.
Create only absent exact-title non-default views. Stop on unknown existing drift;
do not overwrite it. Set formatting/scope only on the newly created owned views.
Disable automatic mutation retries/redirects, reconcile uncertain outcomes before
retry, then verify query, ordered fields, formatting, scope, paging and row limits.
Repeat must adopt existing views without writes. Recovery is selection of the
preserved default/existing views; remove only the exact new view IDs if subsequently
required. No original-file restore, content replacement or permissions change.

## Native verification — 18 October 2026

Both views were saved/read back through the qualified CLI. Repeat performed zero
writes. Native queries returned seven cases and 657 distinct captures/supporting
pages; their capture-hash set exactly matches the preserved set. Snapshots of seven case items and 1,197 library items, original fields/views,
defaults and version/approval/checkout settings matched before/after. Current
readback confirms inherited permissions on both resources; no permission operation
was performed. Item writes: zero. There were no source, file-content, authority,
permission, notification or settings changes and no new licence/connection.

Page-target existence and representative reference-file existence were checked
through SharePoint GETs; this does not prove browser rendering, exact filter
interaction or ordinary-user access. No browser login was used. Local tests cover
query boundaries, missing/conflicting evidence labels, additive views, link/path
safety and existing case/date behaviour. Private receipts and bounded deployment
adapter: `.local/records-navigation/20261018/`.

The selected RC-01/RC-02a implementation is delivered. Visual/access observations,
local-complete/upstream-pending lifecycle evidence, broader retention inspection,
recovery proof and exhaustive original-media audit remain separate work. No
custodian handoff was sent and the upstream register remains read-only.
