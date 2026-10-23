# Identifier-variant retrieval candidates

`scripts/ppg_source_association.py::propose_identifier_variant` adds an evidence-bound
retrieval candidate to a copied screen. It does not write files, change the catalogue
ledger, resolve identity, accept current authority or assess document content.

The bounded route requires complete/consistent catalogue accounting, exact retained
original/text hashes, a printed header identifier, a quoted title passage, matching
title tokens beyond instrument/function words, one unique numeric document-code
family, same issuer and independent matching printed/catalogue version evidence.
The bounded header check uses the first30 extracted lines. It retains the original identifier spelling and version/date/punctuation differences.
It refuses missing evidence, conflicting titles/versions, ambiguous catalogue families,
existing holds or competing links. Changed prior candidate evidence is refused rather
than replaced. Exact replay adds no duplicate. It cannot establish identity from a
title or filename alone, and does not qualify every possible identifier variation.

The copied row uses the established `other_edition_candidate` retrieval bucket and
`otherEditionSourceIndexes`; those legacy field names do not prove a different actual
edition. The added evidence is explicitly `unverified_identifier_variant`. Original
source ID/title and corpus assertions remain intact. Preserve the old screen and
compare available text through the existing provisional pair-review route next.

Observed pilot: three previously metadata-only rows have candidates, reducing that
retrieval gap from922 to919. Existing catalogue comparisons remain62 and source-only
reviews15. Of276 retained sources, three await associated comparison and195 remain
unassociated/unappraised:198 still await comparison, plus one held conflict. No source
register edit or accepted current identity is implied by the improved retrieval count.

Seven create-only evidence files in `ReviewIntelligence-identifier-retrieval-v1`
replay with unchanged bytes/identities/versions. Downloaded29-member archive rebuilds
all three candidates/staged screen/corpus status using archived inputs/validators,
preserves the unchanged ledger and reproduces actual PDF text derivations. Other273
corpus byte pairs remain external fresh checks. Detailed bindings/receipts stay private.
Nine fictional regressions and48 focused tests pass. Current V7/template, pending
comparisons, authority and full Word-output qualification remain open.

## Subsequent comparison result

Batch24 compares all three staged candidates while retaining their unverified
identifier status. The original retrieval receipt remains at its earlier scope.
Current ledger65 pairs/128 findings; corpus195 unassociated unappraised/one held,
with no unheld associated source left awaiting comparison. Catalogue metadata-only
remains919. See [comparison scope](retained-text-pair-review.md). No source identifier
or current authority is accepted merely because a comparison has been recorded.
