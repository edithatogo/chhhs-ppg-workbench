# CareOps / Atlas adapters

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The selected adapter is implemented for **Atlas evidence → supporting attachments
in one fictional PPG review package**. Conductor selected this consumer and direction
under the implementation commission. It reuses the existing Atlas application and
PPG submission assembler. CareOps simulation integration is not implemented.

## Usable local qualification

Run from this repository with the existing Atlas environment; no dependency install,
service, credential or native Microsoft object is created:

```sh
/path/to/atlas/.venv/bin/python scripts/qualify_atlas_adapter.py --atlas-root /path/to/atlas
```

The command verifies the exact Atlas commit and rich contract hash, refuses changed
consumer source, creates an ephemeral fictional DuckDB using Atlas's existing test
fixture, and calls the actual `create_app(ReadOnlyQueryService(...))` through its
existing FastAPI TestClient. The only request is GET `/api/v1/evidence` against the
qualified in-process origin, with explicit concept/assertion identity and valid/observed
clocks. Redirects and unqualified origins are refused. Provenance URLs are not followed.
No CaseUID, local narrative or private source data is sent to Atlas.

`ppg_atlas_adapter.py` validates the captured response with the actual Atlas
`EvidenceResponse` model in strict JSON mode and binds it to its captured byte hash
and request. It emits two `supporting` attachments: the unchanged raw response and
a receipt linking it to local CaseUID `PPG-ATLAS-FICTIONAL-001`. The receipt retains
request/commit/schema pins, response hash, clocks, pagination and each assertion's
namespace, jurisdiction, dimension, state and provenance. The raw response retains
native terminology, uncertainty and all other contract fields without remapping.

The fixture concept `rx:1` is not crosswalked to a named real medicine. Three records
are retained separately. Missing source hash/version stays null; receipt items are
explicitly `sourceIntegrity: unverified`, with a reason and `sourcePinsComplete`.
Even populated source pins are attributed references: this adapter does not retrieve
source bytes or claim source-byte verification. Response-byte integrity is a separate
claim. No medicine equivalence, regulatory/funding/formulary qualification, policy
approval, publication rights or simulation validity is inferred.

The qualification uses the existing explicit-job runner to assemble these attachments.
It independently opens the actual saved ZIP and verifies CRC, exact attachment bytes
and manifest hashes. All eight required evidence categories and five required metadata
items remain missing in this supporting-only example. It remains an assembled DRAFT,
not a complete review or approval package. Raw fictional response, actual ZIP and
qualification receipt are retained under ignored `.local/adapters/fictional-qualification/`.

## Integrity and recovery

Refuse absent evidence without a negative conclusion; denied/unavailable lookup,
schema/version drift, malformed hash, mismatched concept/clocks, contradictory source
pins, incomplete pagination and responses above1MiB produce no supporting output.
A captured response hash detects subsequent byte changes. It does not authenticate an
unqualified service or establish that an attributed source hash matches source bytes.

The existing runner provides per-job locking, frozen input/engine hashes, staged
commit and same-job replay verification. Replaying the same captured response returns
the existing package. A new API response, changed job or edited output requires a
new explicitly prepared job revision; the old output is preserved. The demonstration
checks replay, edited-output refusal, a new revision preserving the edit, and an
unchanged fictional database. It performs no source/case writes or delivery.

## Exact consumer qualification and remaining boundaries

Atlas checkout HEAD: `d75e8d06cd3d772cfa1fee4fe150eab318ef231b`.
Rich contract: `contracts/openapi-readonly-v1.json`, SHA256
`306dee770fb9a3b2a14757a392aafa759bb3e279f906b0d3479ea4e684aca8a2`.
The sparse `openapi-v1.json` alone is not the exchange schema. A changed commit or
contract requires requalification; the command refuses drift before importing code.

Atlas's current README explicitly records that no hosted API/service is published.
This release supports its in-process fictional client only. Production requires an
actual deployment-owned endpoint, governed data, access, rights and current contract
qualification. No new receiving endpoint or remote transport is commissioned here.
Atlas public federation requires public/ungated datasets and cannot receive private
PPG operational exports; the selected lookup sends no such export.

CareOps's saved original checkout is absent and its previously inspected worktree Git
pointer is broken. Conductor has no qualified current consumer checkout/service to
supply. A future scenario-assumption evidence adapter needs a valid current checkout,
a selected scenario and assumption ID, exchange direction and accepted receiving
contract. Do not reconstruct Git pointers, invent IDs or change model parameters to
remove this prerequisite. This separate candidate is pending; it is not a dependency
of the selected Atlas-to-PPG fictional adapter.

The portable `careops-ppg` toolkit is not a deployed CareOps receiving service. No real
records/history are copied into it. Native PPG hub integration retains its existing
owner; no SharePoint field, case status, policy, role or permission is changed here.
