# Teams workspace

The PPG channel is an entry point to canonical SharePoint resources. Keep the
source catalogue, local review decisions and supporting evidence separate.
Technical lifecycle never establishes content readiness, operative currency or
policy approval. Keep notifications off and preserve current permissions.

## Contract and extension

`config/workspace-manifest.json` is the version 1 capability/artefact/surface
manifest. `config/workspace.schema.json` specifies those records and the status
projection contract. `python3 scripts/ppg_workspace.py` validates stable keys,
required fields and cross-references. Use a JSON Schema 2020-12 validator for the
full structural contract. Exact native identifiers and receipts stay in the
existing `.local/deployment.json` workspace binding and `.local/workspace/`.

Register future capabilities with a stable key, purpose, technical lifecycle,
execution mode, responsible role, dependencies, resources and acceptance criteria.
Register their artefacts with canonical resource and provenance references,
location and explicit content status. Add a hub link by default; add a tab only
when needed for a frequent task. Validate references and access, implement through
existing native tools, record save/run/readback evidence, then mark the capability
live. Planned and pilot records must not be presented as working services.

## Surfaces

- Start Here: published navigation page, native Quick Links and status List web part.
- Review Queue and Catalogue: existing Lists, using Teams' supported native UI.
- Evidence & Templates: existing library, preserved examples, manual tools and archive.
- PPG monthly reporting workflow: the adopted existing Loop Page tab in
  Clinical Leadership (CHHHS) / Policy (PPG) Management. It displays the rendered
  Mermaid diagram and six operator steps. Use the tab overflow menu if hidden;
  see [viewing and maintenance](monthly-reporting.md#channel-walkthrough-and-mermaid-diagram).

Inventory current tabs before adding anything. Match by canonical target, adopt
existing matches, and retain unrelated tabs. Disable the tab announcement checkbox.
SharePoint page/list tab configuration is not supported through Graph: use Teams'
SharePoint/Lists UI. Do not invent private Teams API calls or use website tabs as
an unverified substitute. Resource access still follows SharePoint permissions;
a private channel does not change the parent site's access boundary.

## Quiet status

The separate Power Automate flow runs every 15 minutes, concurrency one. It reads
the existing source-state, successful checkpoint and latest durable run receipt.
Its only write is the uniquely keyed `source-sync` presentation row. The importer,
identity ledger, source records and review queue are never changed by this flow.
Generate its private definition with `python3 scripts/build_workspace_status_flow.py`.
Adopt the bound existing flow on subsequent deployments; do not create a duplicate.

Observed and committed source versions are compared directly. A newer failed
attempt with no attempted writes and a source mismatch is held. Other failed
attempts are failed; incomplete, inconsistent, future-dated or overdue evidence
cannot produce healthy. A matching verified baseline is healthy. A later metadata
poll cannot clear a mismatch. Display status becomes stale after 30 minutes without
a projection update; the native view evaluates age when loaded/refreshed. Source
checks older than 90 minutes cannot produce healthy. Projection failure writes
unknown where possible; if that write also fails, the stale timestamp exposes it.

## Captured archive

Native edition/currency columns and grouped current/historical/unconfirmed views
are available in the same library; see [policy editions](policy-editions.md).
The built-in SharePoint Version column records workbench changes, separately
from the edition stated in a captured policy.

The primary corpus contains 533 files. Preserve bytes, original URLs, capture dates,
filenames, lengths and SHA-256 hashes. Downloads are checked against original bytes.
Office files use an appended `.captured` suffix because SharePoint modifies some
Office files on ingestion. Download and remove only this suffix to open the exact
original; the manifest retains both original and hosted filenames. Do not change
Office property-promotion settings for the shared library.

The CMO view is navigation, not a role assignment: 178 primary-corpus files match
the earlier 258-item selection. The other 80 supporting items lie outside the
primary corpus and are identified as such in the selection index. Captured files
are labelled “Captured reference copies—current authority unconfirmed.” Never
advertise the archive as a complete current policy portfolio.

## Verification and recovery

Keep local validation, native configuration, run/readback and desktop acceptance
as separate receipts. Check the four canonical targets, existing permissions,
archive count/size/hash matches, explicit draft/archive/manual labels, held/error/
unknown/stale status, future registration and reapplication without duplicates.
A local test or a successful flow save alone does not establish native acceptance.
On partial transfer, retain per-file receipts and resume by name plus expected
hash; never overwrite a different existing file. Recycle only newly created
transfer artefacts after their canonical preserved replacement is verified.
