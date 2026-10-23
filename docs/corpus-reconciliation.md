# Retained corpus reconciliation

The read-only helper `scripts/ppg_corpus_reconciliation.py` reconciles the frozen
screen, latest additive comparison ledger and actual original/extraction byte pairs.
It assigns no document identities and makes no content, authority or clinical decisions.
This is a local audit utility, not a cloud service or automatic classifier.

`inspect_sources(screen)` reads each original and UTF-8 extraction from its retained
path and checks both hashes. `reconcile(screen, ledger, facts)` produces a repeatable
report from those frozen observations. Source rows, catalogue assertions, prior
assessments, holds and human notes remain unchanged. Unknown/duplicate representations,
invalid associations, inconsistent catalogue identity assertions and a held association
with an assessment are refused. OCR/fullness limitations remain explicit.

The 20 October snapshot accounts for273 original/extraction pairs:62 have provisional
retained-text assessments,1 is held,210 remain unassociated/unappraised. All985
catalogue entries are retained;922 are metadata-only in this corpus.37 extractions
are sampled OCR and236 have unverified fullness. A literal-overlap screen, byte
verification or an unmatched title does not establish a semantic comparison or absence.

Four unassociated sources have header assertions. One noise-management identifier
has a date-separator difference from a catalogue assertion; this is a manual retrieval
lead, without changing the source code or accepting identity. The other headers
remain unbound. Sources without recognised headers also remain available for further
appraisal; they are not silently excluded or counted as new active catalogue policies.

Thirteen legacy assessment entries lack the content-hash field introduced later.
Their original/extraction hashes and finding references are preserved;49 later entries
have recorded content hashes. The audit exposes the gap without fabricating a hash,
overwriting earlier evidence or downgrading all source accounting to zero. Reconcile
legacy finding content against its frozen evidence before claiming that later field's
qualification for those entries.

Five native evidence files retain the report, README, receipts and6-member recovery
archive. Exact native bytes/identities/versions and zero-create replay verify.
Downloaded ZIP CRC/member hashes and archived report reconstruction pass. The archive
contains the frozen screen, ledger, byte facts and generator/recipe, **not the273
originals or extractions**. Report reconstruction reproduces historical observations;
repeating actual byte verification requires those separately retained files at the
screen paths. Preserve prior comparison and source-hold evidence companions too.

Next: inspect the four header leads and remaining unassociated texts without forcing
identity; record any verified retrieval candidates additively. Preserve source holds,
current-subject/template gaps and existing human edits. No source write, native List/
flow/schema, permission, annotation, AI or notification change is involved. Frozen
workflow1.4.0 remains unchanged. Current V7/template and full-content/Word fidelity
remain open; this report does not complete the pilot or prove operational adoption.

## Optional source-only companion

The default helper still reproduces this frozen report exactly. Optional validated
[source-only review envelopes](unassociated-source-review.md) now track appraisal of
unassociated sources without assigning identities or changing catalogue comparisons.
The retained guidance companion records1 such review and209 unappraised texts; the
original210-unappraised snapshot remains unchanged. Envelope/hash checks do not replace
passage validation or prove current authority/visual fidelity.
