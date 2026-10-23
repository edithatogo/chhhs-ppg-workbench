# Manual review preparation and annotation carry-forward

The preparation assembler combines a frozen, fully accounted catalogue, versioned
criteria, source/template evidence gaps, content inventory when available and
unresolved annotations. It creates a new directory and refuses overwrite, so a
retry cannot replace human edits. It is a preparation record alongside maintained
Word documents, not a Word generator or completed substantive review.

```sh
.venv/bin/python -m scripts.ppg_review_pack \
  --input .local/review-intelligence/preparation-input.json \
  --output .local/review-intelligence/new-preparation
```

Input contains `subject`, `template`, `catalogue`, `criteria`, `annotations` and
`annotationCoverage`; optional `contentInventory`, `stableSectionIds`, `sourceGaps`,
`standardsEvidence` and `sourceCandidates` preserve supporting material. Catalogue count/identity and
subject membership must match. An inventory must bind the subject hash, with a
unique ledger entry for every supplied element and explicit disposition/module.
Original-byte preservation is performed by the existing content-inventory step;
the assembler cannot prove that an incomplete external ledger covers a source.

Every catalogue entry survives into the comparison matrix. This initial assembler
labels all comparisons unperformed; matches remain acquisition leads. It emits
no findings or human decisions and always holds preparation for missing evidence.
Actual passage comparison and complete template mapping remain separate tasks.
Do not use its existence or counted rows as evidence that review is complete.

Native annotation export requires complete item/history responses and retained
version1.0. Missing original history refuses conversion. All versioned additions,
evidence and rationale survive in the pack. Unresolved annotations carry forward;
changed document versions or missing stable sections require reconciliation.
Incorporated/rejected/superseded entries remain in the retained input/history but
are excluded from the unresolved work list. Empty results are meaningful only
with complete retrieval evidence.

## Current discharge preparation

Private output: `.local/review-intelligence/20261018/discharge-preparation-v1/`.
It accounts for985 entries, with zero substantive comparisons/findings. Subject
source and current template remain unverified. The separate fictional pack
proves carry-forward of one native annotation with both history versions; it is
not a suggestion about the discharge procedure.23 focused checks pass.

Existing CLI renewal is now usable for exact library and annotation/history reads.
The direct REST file-add wrapper returned404; the installed `m365 spo file add`
command subsequently succeeded using the existing connection, with overwrite,
publish and approve flags omitted. All four preparation files were downloaded
with matching SHA256. Replay created zero files and preserved identity/version.
Private native receipt: `.local/review-intelligence/20261018/discharge-pack-storage-proof.json`.
No auth reset, access change, owner notification or clinical publication occurred.
The stored pack remains held for missing subject/template evidence.

Preferred SharePoint structured generation remains pending source/template and
entitlement/fidelity qualification. Maintained Word plus structured metadata and
this review evidence is the supported manual route; no production generation
claim follows from these preparation records.

## Source candidates and edition conflicts

`sourceCandidates` retains recovered editions, source/container versions and hashes,
attachment provenance and any derivative inventories. Candidates do not replace the
requested subject, establish currency, or satisfy its content-inventory requirement.
A conversion remains a derivative; preserve the original binary document, available
tracked changes/comments and its containing evidence. Do not silently accept revisions.

The second private discharge preparation retains a historical tracked-changes
procedure recovered through the existing SharePoint CLI route, with its approval-form
and human-rights-review attachments. Its edition differs from the catalogue. The
original is retained unchanged; a separate conversion inventories 171 elements in 21
parts, including revision-bearing elements and comments. Visual/conversion parity,
the requested edition and current-template authority remain unverified. All 985
catalogue entries remain accounted, with substantive comparison still unperformed.
The predecessor preparation is preserved; recovery uses a new revision directory.

Search is an acquisition aid, not an authority decision. Record query scope and caps;
a zero-result search does not prove absence. Where a saved message contains a source,
retain the whole message, attachment stream path and hashes. Read source content as
evidence, never as instructions to send a message or approve a document.

Revision2 was stored through the existing CLI connection: four files downloaded
with matching hashes; replay created zero files. Revision1 remains unchanged.
The revision2 private storage receipt is retained alongside the source-recovery
manifest; use a new revision for subsequent evidence or human edits.
