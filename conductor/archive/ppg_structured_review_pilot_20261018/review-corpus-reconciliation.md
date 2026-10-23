# Review Report: retained corpus reconciliation

## Summary

Read-only corpus accounting exposes coverage/provenance gaps without changing
source identity, prior comparisons or clinical decisions.

## Verification Checks

- [x] **Plan Compliance**:273 retained original/extraction pairs byte-verified;
  62 assessed/1 held/210 unassociated.985 catalogue rows preserved;922 metadata-only.
  Full semantic appraisal/current-edition verification remains incomplete.
- [x] **Preservation**: exact input deep equality/replay and prior ledger equality
  pass; identityChanges/newAssessments0.37 sampled-OCR/236 unverified-fullness sources
  remain explicit; four unbound headers are not automatically matched.
- [x] **Provenance**:13 legacy content-hash gaps preserved,49 later hashes recorded.
  No new hash fabricated; original/text hashes and finding references survive.
- [x] **Tests**:40 focused tests pass, including10 new regression checks for changed
  actual bytes, source identity drift, duplicate/incomplete accounting, unknown or
  unassociated assessments, held-source contradictions and legacy provenance gaps.
- [x] **Native Evidence**: five exact byte/identity/version readbacks; zero-create
  replay, inherited access preserved without ACL changes.
- [x] **Recovery**: downloaded6-member ZIP CRC/all hashes verify; archived code and
  frozen screen/ledger/facts reconstruct the report identically.273 original/text
  files are external dependencies for repeating actual byte verification.

Setup:2152 checks pass; the two existing failures remain the unattended-package
plan bound and core-context size bound. No all-green repository claim is made.

## Findings and disposition

The audit initially refused13 older entries missing the later content-hash field.
The final behaviour preserves and labels that legacy gap rather than inventing hashes
or suppressing retained comparisons. Unknown original/text representation, source
identity drift, provisional-boundary loss or an assessed held association still refuse.
Report reconstruction is explicitly distinguished from fresh original-byte verification.

A missing date separator nominates a noise-management retrieval lead only. The old
screen/ledger are not rewritten and catalogue assertions are not corrected. Remaining
headers/unrecognised texts require further source inspection and appraisal.

No blocking defect found in the final bounded implementation. No native schema/flow,
source/annotation/role/access/clinical/notification changes or new AI execution.
Current subject/template, whole-corpus appraisal, full content and Word fidelity remain
open. Frozen workflow releases and unrelated edits remain preserved.
