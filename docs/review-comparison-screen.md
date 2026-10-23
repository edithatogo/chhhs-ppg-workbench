# Retained-text comparison screen

The screen accounts for every frozen catalogue identity and scans every supplied
text source for literal passage overlap. It binds quotations to source and text
hashes, character offsets and line numbers. Header identifiers on the first page
are acquisition evidence; they do not establish current approval or applicability.
Matching identifiers, other editions and metadata-only entries remain distinct.
All matching and other-edition source indexes survive in the catalogue ledger.

```sh
.venv/bin/python -m scripts.ppg_review_screen \
  .local/review-intelligence/screen-inputs.json \
  .local/review-intelligence/new-screen.json
```

Input contains `subject`, `catalogue` and `sources`. Each text source supplies its
UTF-8 representation and SHA256, original-source SHA256, source path and extraction
coverage. The catalogue supplies its source hash, count and unique record IDs.
Original-byte verification and acquisition receipts belong to the retained source
manifest; the screen validates text hashes and cannot prove an asserted original
hash without the actual original file. Output creation refuses overwrite.

The initial matcher uses twelve-word sequences. Wording recurring in at least
five sources or 5% of the supplied corpus is retained separately as possible common
text. URL-dominated matches are retained there too. These remain evidence, not
silently discarded content. This reduces template boilerplate in the candidate
list; it is not a semantic duplication/conflict assessment. The output retains up to three example pairs per category/source; originals and
frozen inputs retain the full text. No match does not prove absence. Semantic comparison, rationale and human disposition remain
separate work. Suggestions never become decisions automatically.

Sampled OCR is partial coverage and cannot establish first-page identity. Other
text extraction may also omit scanned pages, images or complex content. Preserve
originals, extraction limitations, unmatched sources and unverified editions.
Never mark the complete comparison task finished from a literal screen alone.

## Discharge pilot observation

The historical V6 draft screen accounts for 985 catalogue entries and 273 retained
text sources, with all 273 original hashes independently verified. 37 text sources
are sampled OCR. First-page identifiers associate 40 catalogue entries with the
recorded identifier and 23 with another-edition candidates; 922 remain metadata-only
in this bounded corpus. This describes the corpus, not tenant-wide availability.

Initial bound passage matches were common scope wording and reference URLs.
After separating those, zero specific overlap candidates remain. Seven explicit
reference leads from the historical draft are retained with source passages and
catalogue retrieval candidates. One target remains unidentified; none is an
accepted relationship. The requested V7 edition, current template, complete
semantic comparison and content mapping remain open.

Native companion files contain the catalogue CSV, source manifest, passage ledger,
reference leads, readable summary and hash receipt. The predecessor preparation
and source files are preserved. Retry compares downloaded hashes before accepting
existing files. Native locations, hashes and receipts remain in private deployment
configuration and the dated private evidence directory.
