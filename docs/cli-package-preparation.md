# CLI package preparation without premium connectors

> 23 October closeout: [exact saved-native-body CLI fallback and remaining automatic-flow parity gate](package-closeout-20261023.md). The track is reviewed and archived partial; earlier dated qualifications retain their scope.

For one named entrypoint and restart instructions, use the [guided CLI](guided-cli.md).

This route prepares and stores existing files. It validates an explicit job,
preserves attachment bytes, assembles a versioned ZIP with manifest and mechanical
completeness report, and publishes the package plus its receipt to an existing
SharePoint folder. It uses Node, the maintained assembler and the installed M365
CLI's saved SDK client. No Power Automate connector, AI runtime, new consent,
licence assignment or automatic Word body population is involved.

## Select and freeze records

For an existing case, reuse the read-only selector:

```sh
.venv/bin/python scripts/ppg_package_selection.py \
  --deployment PRIVATE_DEPLOYMENT.json --case-id CASE_ITEM_ID \
  --case-uid EXPECTED_CASE_UUID --output NEW_PRIVATE_SELECTION_DIRECTORY
```

It pins the exact case and linked catalogue records, requires the recorded
baseline to match those catalogue records, downloads the existing baseline and
Word draft, and checks before/after native versions, ETags, sizes and ZIP CRC.
An absent or mismatched baseline refuses selection; do not repin it merely to
make a package pass. No catalogue, case or source-register field is written.

Prepare a private metadata JSON containing the recorded `caseUID`, `title`,
candidate `version` and `sourceBaseline`. Case identity and baseline must match
the selection. Other existing assembler metadata can be included; missing evidence
and unconfirmed roles remain visible. Convert the frozen selection to a job:

```sh
node tools/unattended-package/prepare-selected.cjs \
  SELECTION_DIRECTORY/selection.json RECORDED_METADATA.json NEW_JOB.json job-new-revision
```

The bridge verifies the frozen file hashes, preserves native source/version
references, includes the selection itself as evidence, and records selected
catalogue identities. It creates the job exclusively. Historical authoring stays
unknown. A frozen selection proves the captured occurrence, not continuing source
currency or substantive approval.

An explicit prepared job can instead use the existing
`templates/unattended-package/job.json` contract. Include the source baseline,
included record identities, candidate/output revision and any maintained template
version/hash in its metadata. Every selected file requires its exact SHA-256 and
evidence role. Copy a maintained Word template unchanged as supporting evidence
when needed; do not treat an unpopulated template as a completed proposed document.

## Assemble locally

```sh
node tools/unattended-package/run.cjs JOB.json INPUT_DIRECTORY EXISTING_OUTPUT_DIRECTORY
```

The existing runner provides bounded reads, input/output separation, per-job locks,
engine/input fingerprints and unchanged replay. Output is
`OUTPUT_DIRECTORY/JOB_ID/package.zip` and `receipt.json`. The ZIP includes its
attachment index, completeness report and member manifest. Both complete and
incomplete evidence collections remain **ASSEMBLED DRAFT / HUMAN CHECK REQUIRED**.

## Publish and read back

Keep this configuration private. Resolve the values from the existing qualified
client and destination records; do not introduce a new authentication client.

```json
{
  "siteUrl": "https://TENANT.sharepoint.com/teams/SITE",
  "folder": "/teams/SITE/EXISTING_LIBRARY/EXISTING_FOLDER",
  "sdkDirectory": "/absolute/path/to/@pnp/cli-microsoft365/dist",
  "connectionName": "EXISTING_SAVED_CONNECTION",
  "identity": {
    "username": "EXPECTED_WORK_ACCOUNT",
    "tenantId": "EXPECTED_TENANT_UUID",
    "appId": "EXISTING_CLIENT_UUID",
    "objectId": "EXPECTED_USER_UUID"
  }
}
```

```sh
node tools/unattended-package/publish-sharepoint.mjs \
  PRIVATE_CONFIG.json OUTPUT_DIRECTORY/JOB_ID NEW_PRIVATE_JOURNAL.jsonl
```

The command verifies the saved client/account and obtains a token silently through
that same SDK. It refuses mismatches or unavailable authentication. It requires an
existing destination folder and does not create folders, permissions or schema.
Supported site paths are `/teams/SITE` and `/sites/SITE`; special folder characters
outside the bounded contract are refused.

It preflights both native names, uploads `JOB_ID.zip` with server-side
`overwrite=false`, verifies stable metadata and exact downloaded bytes, then
creates `JOB_ID.receipt.json` last. It rechecks both files before success. The
private, synced journal records attempts, hashes and native identities/versions;
it contains no bearer tokens. Only the package and receipt are written remotely.

The adapter uses direct single-request transport, with redirects disabled, rather
than the installed CLI's mutation retry/upload wrappers. No premium HTTP/custom
connector is involved. Existing authentication, SharePoint permissions and service
policy still apply; this route does not bypass them.

## Retry and recovery

- Use the same frozen local job/output and a **new journal filename** on each retry.
- An unchanged remote pair is read back and returned as `replayed`, with no writes.
- If only the package exists and matches exactly, the missing receipt can be created
  after readback. A process/network failure never authorises a blind second POST.
- Conflicting package or receipt bytes are preserved and refused before new writes.
  Use a new explicit job/output revision for changed content; never overwrite edits.
- Concurrent creation is refused by SharePoint. Reconcile with a subsequent read;
  there is no automatic retry, distributed lock or atomic two-file transaction.
- A failed final verification leaves the journal incomplete. Do not describe the
  pair as verified from the receipt's existence alone.

No schedule, messaging, submission or clinical approval is performed. The local
runner's existing 100 MiB attachment limit and the publisher's 128 MiB artifact
limit remain enforced; larger native transfers have not been qualified.

## Qualification — 22 October 2026

One fictional explicit-job package was assembled and published through the saved
M365 client to the existing qualification folder. Actual native ZIP 33,048 bytes
and receipt 1,252 bytes read back exactly. Replay preserved both files' IDs, version
1.0 and ETags. Independent CLI download/Python ZIP inspection passed CRC, complete
manifest membership, all sizes/hashes and original attachment bytes, including the
unchanged 22,377-byte maintained Word template. Eleven missing evidence/metadata
items stayed visible; no substantive content readiness was inferred.

Focused local tests cover create-only receipt-last ordering, unchanged replay,
package-before-receipt recovery, remote edits/conflicts, uncertain-write
reconciliation, local tampering, native-pin changes and frozen-selection bridging.
The existing record selector's eleven tests also pass. Native recovery/collision
behaviour is retained in the earlier packaging qualification; the new publisher's
fault cases are locally tested, not newly exercised against live edits.

Private inputs, native journals, downloaded ZIP and independent audit:
`.local/unattended-package/cli-publish-20261022/`. This completes the bounded CLI
preparation/publication increment; it does not close broader Word-generation,
AI-runtime, scheduling or business-use requirements in the parent track.
