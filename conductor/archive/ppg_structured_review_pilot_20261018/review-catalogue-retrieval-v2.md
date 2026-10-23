# Review Report: catalogue retrieval successor2

## Summary

Eleven source representations are safely staged for comparison; five remain unresolved.

## Verification Checks

- [x] **Plan Compliance**:985 identities/source assertions and65 historical comparisons
  preserved. All16 leads attempted;11 unverified candidates/five explicit refusals.
  No full-text comparison, current authority or clinical acceptance claimed.
- [x] **Style Compliance**: existing pure helper gains explicit matching-identifier
  mode and short-code support; default prior output shape unchanged. No new runtime.
- [x] **New Tests**: four synthetic regressions cover short exact IDs, case-only
  identifiers, variant bucket separation, changed evidence/mode/title/version,
  unrelated numeric collisions and ambiguous duplicate complete IDs.
- [x] **Test Coverage**: additive copied screen, exact duplicate-free retry, original/
  text hashes, independent versions and quoted strict title tokens remain required.
  Matching full IDs select uniquely across the catalogue; variants require unique
  numeric-code evidence. Existing held evidence cannot be bypassed.
- [x] **Test Results**:66 focused tests pass. All16 source pairs reverified from
  downloaded recovery ZIP; all11 candidates and five refusal results reconstructed.
- [x] **Native Evidence**: nine create-only files, exact byte/GUID/version readback,
  inherited access and zero-create replay. No catalogue/native source-list writes.
- [x] **Recovery**:41-member archive CRC/hash checks, archived validators and all
  inputs reproduce complete screen and reconciled corpus. Other260 raw pairs remain
  external; frozen byte facts are not present availability proof.

## Findings and disposition

Initial candidate execution correctly refused an otherwise unique printed identifier
because an unrelated family reused its numeric suffix. Matching-ID mode now requires
unique complete case-insensitive ID, rather than unique numeric suffix. Synthetic
regression proves unrelated suffix reuse passes but duplicate full IDs fail.

Five source title/version differences remain unresolved and unlinked; no inference
or source correction closes them. Eleven staged texts await semantic comparison.
Metadata-only919→908;65 previous pairs/19 source-only reviews remain unchanged.
Current V7/template/authority, remaining catalogue retrieval and Word fidelity remain
open. No blocking defect found within this bounded technical retrieval increment.
