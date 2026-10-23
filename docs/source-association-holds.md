# Retained-source association holds

A retrieval match is a candidate, including a matching document-number stem. It
must not silently substitute a different document when title/content evidence
raises an identity question. One observed association has an unrelated printed
title; its actual record, passages and hashes remain private/native evidence.

`scripts/ppg_source_association.py` adds a `sourceAssociationHolds` record to the
specific catalogue row and original-file hash. It preserves every original field,
retrieval coverage assertion, existing assessment and human note. The record keeps
catalogue/printed titles and identifiers separately, text/original hashes, exact
title passage, evidence reference and an unresolved disposition. It does not
rewrite source identities, decide which assertion is correct or infer a rename.

This is an explicitly evidenced hold, not an automatic semantic-title matcher.
A different title alone can reflect a legitimate rename; resolution needs verified
identity/version evidence. Matching titles are not accepted as conflict evidence.
The helper checks unique catalogue identities and actual printed title/identifier
passages. Exact replay adds nothing; changed evidence or a recorded resolution is
refused instead of overwritten. The pair-review validator refuses the held
original for that row before interpretation, even if a candidate association or
matching identifier could otherwise be supplied. Other originals/rows are not
blocked. Native forms are not constrained by this local gate.

The current companion preserves985 rows and50 existing source comparisons without
claiming another comparison. Thirteen associated rows remain unassessed: twelve
eligible and one held. The original retrieval labels remain dated assertions;
current-document coverage is still unverified. Other versions/unmatched corpus,
922 metadata-only rows and current subject/template/fidelity work remain open.
Future comparisons must start with this companion's additive ledger, rather than
an earlier ledger that lacks the hold. Never use the conflicting PDF as the held
catalogue document or count it as that document's text without resolution evidence.

Five native evidence files have exact byte/identity/version readback and zero-create
replay. Downloaded source archive has10 members, verified CRC/all hashes and a
complete report/ledger reconstruction using archived assembly/validator/inputs.
The current stricter duplicate-identity guard reproduces the same ledger; generation-
time code stays frozen in the archive. Recover predecessor packs separately for
prior finding details. No source register, clinical/operational record, appointment,
permission, notification or workflow component is changed.

Frozen published workflow1.3.0 remains intact. Successor1.4.0 documents the
source-hold preflight and separates local validation from native-form enforcement.
Native guide publication/readback is qualified separately from these source checks.
See the [implementation review](../conductor/archive/ppg_structured_review_pilot_20261018/review-source-association-hold.md).
