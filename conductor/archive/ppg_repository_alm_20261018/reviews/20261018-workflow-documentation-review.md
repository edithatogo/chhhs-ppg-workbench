# Workflow documentation release 1.0.0 — review and native publication

18 October 2026. User commissioned complete current-workflow documentation,
a versioned register/diagrams, SharePoint operator publication, reconciliation,
review and commit. Delivered as ALM-03/ALM-06 documentation slices; the broader
ALM track remains in progress. Current native workflow/file owners retained.

## Coverage and current baseline

Register covers all 27 manifest capabilities exactly once, including manual and
scheduled processes, 12 lifecycle operation references, and three separately
labelled conditional integrations. Every capability has trigger, input, ordered
steps, output, maintainer lane, failure/recovery rule, evidence status, source and
instructions. Twenty-seven Mermaid diagrams and matching PNG reading aids show
stages and holds. The lifecycle diagram includes all thirteen connected stages
and a separately evidenced replacement/withdrawal branch. These are workflow
maps, not a claim to export every WDL action or qualify every adverse branch.

Historical stage documents retain their original evidence with current-baseline
pointers. The reconciliation table supersedes old closure/next-review limitations
for the connected fictional example, old unenforced-Gitleaks and alpha-runtime
observations, meeting/channel prerequisites and misleading complete-native-flow
inventory assumptions. It preserves real authority, ordinary-user and production
limits. The later repeated ownership on the next review is not another complete
cycle or second PPG configuration; the guide does not label it unaccepted.

## Versioning and review fixes

Git versions maintained source/instructions. Register/guide/diagrams share a
frozen release; release checksums identify those exact bytes and the referenced
instruction snapshots. Source/page/file/deployed-flow versions remain distinct.
Deployed definition hashes are explicitly null: no live native flow inventory or
solution-membership completion is claimed. Existing owners' private receipts are
required before recording actual deployed version parity.

Review found and fixed two material verification issues. SharePoint serializes
same-origin URLs relatively, HTML void tags without a closing slash, and drops
a final newline. A semantic token comparison now verifies resolved link/image
targets, text, structure and attributes; regression controls reject changed links
or text. No second page creation or replacement was attempted after the initial
strict mismatch. Reconciliation verified the already-saved page.

During publication, the lifecycle owner legitimately updated a referenced live
instruction file. Frozen-release validation now refuses corruption inside the
release, but reports external-instruction drift separately. One referenced
instruction and the live artefact inventory have advanced since the frozen release snapshot; it is not silently
repinned or overwritten. New documentation releases use a new version directory;
the builder refuses to overwrite an existing release manifest. Actual generated
PNG availability is required. No new dependency installation occurred.

## Native publication and recovery

Preferred SharePoint structured Word generation was considered using retained
exact-account eligibility evidence. Production maker/Premium connector
entitlement remains unqualified. Supported native page plus existing-library
files used; no new licence, consent, environment, settings or permission changes.
Fresh target reads verified existing library/page versioning and no content
moderation boundary; current qualified M365 client reused without auth mutation.

Thirty new immutable version-named assets (27 PNGs, register, downloadable guide,
checksums) used server-side overwrite=false and single-attempt, redirect-disabled
same-client transport. Every stored file downloaded with exact byte length/hash
parity. Native guide page1.0 saved/check-in/readback/repeat verified. Start Here
page31.0 links that exact guide; all17 controls and16 unrelated controls retained,
repeat content unchanged. No cases, source records, drafts, lifecycle flows or
business statuses were modified. Existing content/permissions were preserved.

Browser followed the actual hub link and displayed the correct guide. All27
rendered diagram elements completed with positive native image widths. Guide
headings, current-state explanation and three download targets rendered. Screenshot,
preimages, assets/native versions, raw receipts and publication proof remain in
`.local/workflow-docs/20261018/`; no tenant bindings or account details in Git.
Current-account rendering is verified; another user's access remains unverified.

Recovery: retain immutable release assets and prior page versions/preimages. If
a documentation correction is needed, prepare a new register version and images,
verify files/page, then conditionally change only the owned hub link. Do not
rebuild/re-upload a frozen published release or replace a human-edited file.
Reverting documentation links is not rollback of native workflows or records.

## Repeatable maintenance

Copy the maintained register into a new numeric version directory, update its
release/as-of, row versions and diagram paths, then revise changed workflows.
Run `.venv/bin/python scripts/ppg_workflow_docs.py --release VERSION --render`
once to build the new baseline. Use `--release VERSION --check` afterward;
inspect external reference drift without replacing old snapshot hashes. Qualify
native create-only assets/page, preserve native identity/version/readback proof
privately, and point Start Here to the verified new version. CLI guards and the
actual release's bounded publication journal are retained in the private evidence
directory for the existing owner. No general automated deployment is claimed.

Validation: nine targeted documentation tests, nine artefact/recovery tests and
fourteen workspace checks passed. Checks cover full coverage, missing/duplicate
capabilities, real instruction paths, diagram-step consistency, immutable bytes,
external drift, HTML normalization negatives, safe release paths and overwrite
refusal. Gitleaks/publication hook and clean-snapshot setup results are recorded
with the final commit. No unresolved high-severity finding in this documentation
slice; native deployed-definition/solution reconciliation remains separate work.

Final isolated candidate setup: 1,077 checks passed, zero failed, one expected
unmaterialised upstream checkout pending. A harmless trailing blank line in the
frozen downloaded guide is preserved for exact published-byte parity; the builder
normalizes that for future releases. Private deployment bindings now retain the
actual guide/register native identities/versions and all27 diagram locations.

The publication hook correctly refused binary PNGs. Rendered reading aids remain
untracked/ignored locally and version-named in SharePoint; editable Mermaid and
all expected reading-aid hashes are in Git. No gate exception or binary bypass
was added. `--check` reports missing generated reading aids separately and still
refuses missing/changed immutable text. `--render-images` can materialise missing
images only if the installed renderer reproduces frozen hashes; it never replaces
a differing file. Native downloads are the fallback if renderer versions differ.

Final clean-checkout correction: generic Markdown link validation originally
reported the intentionally untracked PNGs as broken links. Setup now classifies
only exact versioned PNG paths registered in the frozen checksum manifest with
an intact matching Mermaid source as unmaterialised reading aids. Unknown image
paths, missing/changed text diagrams and other broken links still fail. Added
regression controls for those boundaries. Final clean checkout: 1,179 passed,
zero failed, two pending (27 generated reading aids and upstream submodule).
Nine documentation tests pass in both the working tree and fresh checkout.
Main release commit: `3030e72`; staged Gitleaks8.30.1 passed for556 files.
