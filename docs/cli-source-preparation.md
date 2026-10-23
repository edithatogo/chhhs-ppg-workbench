# CLI assistant source preparation and deterministic evaluation

For one named entrypoint and restart instructions, use the [guided CLI](guided-cli.md).

Prepare immutable evidence copies, upload them through the existing delegated
SharePoint client, check extraction/search visibility and evaluate source/citation
integrity. This uses no premium connector or paid AI runtime. Conversational AI
retrieval, agent publication, semantic review and operative policy authority remain
outside this increment.

The supported formats here are those of [CLI evidence lookup](cli-evidence-lookup.md):
UTF-8 TXT/Markdown, DOCX body/table paragraphs and text-bearing PDF through an
existing `pdftotext` executable. This does not establish that a native assistant
accepts every format; in particular, CLI TXT support is not native knowledge-source
eligibility. Do not replace the native assistant's outstanding acceptance gates.

## 1. Freeze a preparation job

Reuse maintained originals and recorded source versions. Never edit an original,
infer current authority from its title, or rename an unsupported capture to make
it appear supported. Preparation copies existing files; it does not populate a
Word body, create a new document generator or change a clinical document's status.

The maintained fictional sample is
`templates/cited-evidence/source-preparation-job.json`. It pins the existing
three-file evaluation corpus and can be run without actual policy material:

```sh
.venv/bin/python scripts/ppg_source_preparation.py prepare \
  --job templates/cited-evidence/source-preparation-job.json \
  --input templates/cited-evidence --output NEW_PRIVATE_PREPARATION_DIRECTORY
```

For other explicit selections, use the same job fields:

- `preparationId`: a new immutable batch/revision identifier.
- `sourceId` and `file`: an explicit source identity and relative input path.
- `sha256`: pinned original bytes; `expectedTextSHA256`: pinned extracted UTF-8 text.
- `originalReference`, `originalVersionRef`, `sourceEdition`: provenance from the
  existing source record/capture, rather than an invented policy identity.
- `authorityLabel`: `captured-reference-unconfirmed` or `draft-unapproved`.
- `evaluationNeedle`: a known literal excerpt for deterministic verification.
- `ingestionPolicy`: defaults to `exact-bytes`; the narrow DOCX exception below
  is an explicit per-source option, not a global relaxation.

Select one to five sources, each within the existing 2 MB source/text limits.
Input and output roots must be disjoint; output must be new. For PDF input add
`--pdf-tool /absolute/path/to/existing/pdftotext`. No software installation occurs.

The tool validates provenance, expected original/text hashes, extraction and the
literal evaluation needle, then writes prefixed copies, extraction/locator records
and `manifest.json` last. Input originals remain unchanged. A failed preparation
retains diagnostic partial files and no committed manifest. Never infer success
from a copied file's existence.

## 2. Upload source copies and commit a receipt

Reuse the private client/site/folder configuration from
[CLI package preparation](cli-package-preparation.md). The folder must already
exist. Add `pythonExecutable` pointing to this repository's qualified
`.venv/bin/python`, and `pdfTextExecutable` for the existing PDF extractor when used.
No new application, permission, licence, folder, metadata column or agent is created.

```sh
node tools/cited-evidence/publish-sources.mjs \
  PRIVATE_CONFIG.json PRIVATE_PREPARATION_DIRECTORY \
  NEW_PRIVATE_JOURNAL.jsonl NEW_SELECTED.json > NEW_PUBLICATION.json
```

The same-client transport checks the saved account, app and tenant and uses normal
silent SDK acquisition for that existing SharePoint resource. It sends create-only
binary uploads, disables redirects and does not blindly retry a POST. The synced
private journal records attempts and actual native hashes/pins without credentials.

All known source/receipt paths are reconciled before writes. A conflicting source
or receipt is preserved and refused. Each source copy is downloaded and verified;
the final `PREPARATION_ID.sources.json` receipt is written last. It includes the
prepared manifest, original/native hashes, source provenance, ingestion proof and
native identities/versions. A complete stable readback precedes success.

`NEW_SELECTED.json` supplies the exact uploaded file UUIDs/paths to the evidence
reader. A successful CLI result and complete journal are required; a stdout file
created by shell redirection is not proof of success.

### Qualified SharePoint DOCX ingestion

Default publication requires exact bytes. Native qualification found that
SharePoint updated its content-type schema metadata within a copied DOCX while
leaving its document body and all other parts unchanged. This is not byte identity.

The explicit `sharepoint-schema-attributes-v1` policy permits only:

- Changes inside `customXml/item1.xml` with the SharePoint content-type schema
  root, limited to metadata `versionID`, `fieldsID` and Boolean `indexed` attributes.
- A valid changed datastore `itemID` UUID at the root of
  `customXml/itemProps1.xml`.

ZIP membership/CRC, XML tree structure, tags/text/tails, all other attributes and
every other package part must remain unchanged. Supported extracted text, source
locators and extraction method must match. DTD/entity declarations and unsupported
changes are refused. Original and native hashes remain distinct in the receipt;
the original bytes are retained privately. A changed document body, image,
relationship, field value or unrelated schema attribute does not pass this rule.
The package ZIP publisher remains strictly byte-exact.

## 3. Check native extraction and search visibility

```sh
.venv/bin/python scripts/ppg_evidence_cli.py lookup \
  --config PRIVATE_CONFIG.json --query PREPARATION_ID \
  --selected NEW_SELECTED.json --output NEW_PRIVATE_LOOKUP_DIRECTORY
```

This performs real scoped SharePoint search and selected native reads, preserving
original native bytes, stable UUID/version/ETag pins, extracted text and locators.
Missing, denied, unsupported and changed sources are explicit exceptions. A bounded
search miss is `indexing-unconfirmed`, not absence. No recrawl, settings change,
background watcher or repeated polling is introduced. A later visibility check
uses a new output directory with the same saved selection.

## 4. Evaluate source integrity and exact citations

```sh
.venv/bin/python scripts/ppg_source_preparation.py evaluate \
  --preparation PRIVATE_PREPARATION_DIRECTORY --bundle PRIVATE_LOOKUP_DIRECTORY \
  --config PRIVATE_CONFIG.json --publication NEW_PUBLICATION.json \
  --output NEW_EVALUATION.json
```

The default independently reads the native receipt and checks its bytes/stable
pin, exact source membership, original/native integrity, extraction hashes,
authority labels, destination UUIDs/versions and search observations. Each source's
known literal needle generates exact citations, checked against raw bytes,
re-extraction, locators and fresh native versions.

Deterministic negative checks deliberately alter quotes, versions, UUIDs, binary
hashes and source text; denied/missing/unsupported/changed inputs must produce
unknown/no-claim results. Embedded instructions are quoted as evidence and never
executed. These are integrity/failure tests, not AI answers or human semantic review.

`sourcePreparationQualified` requires the live receipt and all deterministic checks.
`searchDiscoveryObserved` separately records whether every selected source appeared
in that bounded query; a preparation pass does not imply a search-discovery pass.
`conversationalRetrievalQualified` stays false. `--offline` explicitly omits native
checks and cannot qualify native preparation, even when deterministic checks pass.

## Replay, failure and recovery

Retain the frozen input/job/preparation directory. Use new journal, selected-output
and result filenames for each invocation. An unchanged complete batch replays with
reads only; an incomplete batch can reuse exact already-uploaded copies and create
only missing artifacts. A receipt with missing sources, changed committed pins or
edited content is refused. After an uncertain write, reconcile native effects
before another attempt. There is no automatic deletion, rollback, stale-lock
takeover or transaction across all files.

Changed inputs, extraction expectations, provenance or policy require a new
preparation ID/revision. Preserve the old batch and diagnostic evidence. No original
source is overwritten, no failed batch is relabelled successful, and no messages,
approval, clinical publication or agent binding occurs.

## Native qualification — 22 October 2026

Five fictional sources were prepared from the maintained edition-1/edition-2/draft
corpus and previously captured DOCX/PDF evidence. The first strict batch stopped
on the DOCX metadata byte change after creating four source copies; its uncommitted
artifacts remain preserved. A separately revisioned batch used the explicitly
qualified schema rule and successfully uploaded all five sources plus the receipt.

After same-client sign-in-frequency renewal, all five were independently retrieved
and observed in SharePoint search. Seven exact citations and all deterministic
source-integrity/negative checks passed, with distinct original/native DOCX hashes
and unchanged supported text/locators. No native AI, original source writes, new
permissions or paid connectors were involved. Native replay and the existing
package transport regression are recorded in the private completion audit.

Detailed source/job/receipt/raw/renewal/failed-batch proof remains private under
`.local/cited-evidence/source-preparation-20261022/`. This completes source
preparation/evaluation software; it does not qualify conversational retrieval,
clinical currency, semantic adequacy or lower-privilege access.
