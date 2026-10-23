# CLI evidence lookup and citation validation

For one named entrypoint and restart instructions, use the [guided CLI](guided-cli.md).

For versioned source preparation, create-only upload and deterministic evaluation,
use [CLI assistant source preparation](cli-source-preparation.md). It reuses this
reader and preserves native assistant/runtime acceptance as a separate boundary.

This is a deterministic, read-only evidence tool using the existing delegated
M365 CLI session. It searches a selected SharePoint folder, retrieves at most five
explicitly selected files, extracts supported text, creates exact excerpts and
checks their citations. No premium connector, AI model, embeddings, new consent,
permissions, background indexing or paid AI runtime is required.

It is separately commissioned CLI functionality. It does not substitute for or
close the parent track's unqualified SharePoint/Copilot Studio assistant runtime.
It quotes captured evidence; it does not answer clinical questions, determine
operative authority, perform substantive review or approve a document.

## Existing client and selected scope

Keep exact bindings, source selections and outputs in private approved storage.
Reuse the saved account/client and existing site/library access. A private config:

```json
{
  "siteUrl": "https://TENANT.sharepoint.com/teams/SITE",
  "folder": "/teams/SITE/EXISTING_LIBRARY/SELECTED_FOLDER",
  "connectionName": "EXISTING_SAVED_CONNECTION",
  "identity": {
    "username": "EXPECTED_WORK_ACCOUNT",
    "tenantId": "EXPECTED_TENANT_UUID",
    "appId": "EXISTING_CLIENT_UUID"
  },
  "pdfTextExecutable": "/absolute/path/to/existing/pdftotext"
}
```

The command checks CLI status against the intended account, tenant, application
and connection. It then uses only explicit GET requests through that client.
It never invokes login, switches identity, exports tokens or changes permissions.
Actual target reads prove access separately from the connection banner. Omit the
PDF setting when that existing executable is unavailable; PDFs are then explicitly
unsupported. There is no automatic installation or alternate extraction service.

A private selection JSON is an array of up to five entries:

```json
[
  {
    "sourceId": "selected-reference",
    "path": "/teams/SITE/EXISTING_LIBRARY/SELECTED_FOLDER/reference.docx",
    "authorityLabel": "captured-reference-unconfirmed"
  }
]
```

Use `draft-unapproved` for drafts. Neither label declares current operative
authority. Where an already-recorded SharePoint file UUID is available, add
`nativeUniqueId`. The reader resolves that identity and records its current path
only if it remains inside the selected folder. A missing path alone is reported
missing; the tool does not guess another file from its title. Discovery links and
the retained archive index can supply an explicit new selection without broad
archive ingestion.

## Search and retrieve

```sh
.venv/bin/python scripts/ppg_evidence_cli.py lookup \
  --config PRIVATE_CONFIG.json --query 'literal search phrase' \
  --selected PRIVATE_SELECTION.json --output NEW_PRIVATE_BUNDLE_DIRECTORY
```

The query is a bounded literal phrase with a folder Path restriction. Raw KQL,
quotes and backslashes are refused. Search saves at most twenty in-scope results
and the reported total; it does not download discovered hits automatically.
An empty selection array supports discovery before choosing sources.

Search results are discovery, not citations. A selected direct read proceeds even
when search returns no matches or is denied. Each source reports whether it was
returned by that particular bounded search. `not-returned-by-this-query;
indexing-unconfirmed` is explicit uncertainty: a result limit, query behaviour or
indexing can explain a miss. It is not proof of absence or an indexing failure.
No recrawl/settings change is attempted.

The reader checks native UUID, path/name, ETag, version, length and modification
time before and after content retrieval. Changed sources are discarded. Successful
sources retain their original bytes, canonical URL, native pin, UTC retrieval time,
conservative authority label, extracted text and line-to-source locator map.

Supported extraction is deliberately explicit:

| Format | Extraction and locator | Limits |
|---|---|---|
| UTF-8 TXT/Markdown | Original decoded text and source lines | Invalid UTF-8/control-byte content is refused. |
| DOCX | Main body/table paragraphs, tabs and line breaks; body paragraph/line locators | Main document part is resolved through OPC relationships, including nondefault names. No Word page numbers, headers, footnotes, comments, image/OCR or layout assurance. Deleted runs are excluded; inserted/cached field text does not imply accepted changes or refreshed fields. |
| Text-bearing PDF | Existing `pdftotext -layout` output; PDF page/line locators | No OCR or reading-order/visual-layout assurance. Empty text pages are reported; files without extractable text are unsupported. |

Original files are limited to 2 MB, extracted text to 2 MB and DOCX expanded parts
to 20 MB/500 members. Unsupported Office/captured formats are not renamed, rendered
or executed. DOCX external main relationships and XML DTD/entity declarations are
refused. PDF extraction is bounded by a twenty-second timeout.

`sources.json` records `retrieved`, `denied`, `missing`, `unsupported`,
`changed-during-read` or `error`, with an actionable reason. Failed reads expose
no file text/native metadata and leave no raw source artifact. Unsupported formats
remain unknown; transient/read errors are distinguished from unsupported content.

The new private directory contains `search.json`, `sources.json`, successful
`SOURCE_ID.raw` files and the final `run.json`. Existing directories are refused.
Failed operations are not silently resumed or overwritten; preserve their
evidence and use a new directory for a fresh read.

## Produce exact excerpts

```sh
.venv/bin/python scripts/ppg_evidence_cli.py excerpt \
  --bundle PRIVATE_BUNDLE_DIRECTORY --config PRIVATE_CONFIG.json \
  --needle 'literal text' --context 1 --output NEW_EXCERPTS.json
```

This first rechecks the captured bytes and extraction, then selects up to three
literal, case-insensitive matches per retrieved source. Context is zero to three
lines. Claims contain the exact quote, not generated paraphrases. Every citation
binds URL, native UUID/version, text and binary hashes, extraction method, authority
label, exact line range and paragraph/PDF-page locators. Missing/unsupported reads
remain visible and produce a partial result. No matches produce `unknown` with
no claims. Source instructions are treated as literal text, never executed.

`sha256` fingerprints UTF-8 retrieved/extracted text for compatibility with the
existing citation checker. `binarySHA256` separately fingerprints original native
file bytes. A DOCX/PDF binary hash is never substituted for its text hash.

## Validate captured consistency and current native versions

```sh
.venv/bin/python scripts/ppg_evidence_cli.py validate \
  --bundle PRIVATE_BUNDLE_DIRECTORY --config PRIVATE_CONFIG.json \
  --answer EXCERPTS_OR_COMPATIBLE_ANSWER.json --output NEW_VALIDATION.json
```

The default validates the existing citation contract, original raw hashes, repeated
extraction, native-pin correspondence, exact quotes/locators and fresh SharePoint
metadata for every retrieved source. A denied, moved, changed or missing current
source fails live validation; cached text does not establish continuing access.
Nothing is overwritten or corrected automatically.

Use `--offline` explicitly to check captured consistency without native calls.
The report labels that weaker scope. A mechanical pass does not establish semantic
entailment, content completeness, relevance, clinical adequacy, operative currency
or lower-privilege permission trimming. Human/third-party acceptance remains
separate from this software increment.

## Qualification — 22 October 2026

Current saved-client native search returned twenty bounded results for a broad
fictional query. A narrower query returned no indexed matches while direct reads
still retrieved selected fictional TXT, DOCX and PDF evidence. The DOCX's preserved
UUID resolved its renamed path, and its actual nondefault `word/document2.xml`
part exposed and qualified relationship-based extraction. The initial 404 and
unsupported-part observations remain in the private evidence, not erased.

The final native bundle retrieved all three supported examples, explicitly refused
a known ZIP and reported a fictional missing path. Nine exact excerpts across the
three formats passed the existing citation checker and the new raw-byte,
re-extraction, locator and fresh-native-version checks. No SharePoint writes or
paid AI runtime occurred. No native denial was induced or lower-privilege testing
claimed; denial/drift/tamper cases have local fault-test evidence.

Focused tests cover UTF-8/Unicode, DOCX body/table/break handling, nondefault main
parts, forbidden XML, PDF page locators/no text, denied/missing/read errors, drift,
source/locator/citation tampering, identity-resolved rename/scope refusal, bounded
search, injection-as-text and GET-only existing-client transport. The existing
browser reader, citation checker and AI evaluation tests remain separate checks.
Raw proof stays `.local/cited-evidence/cli-lookup-20261022/`.
