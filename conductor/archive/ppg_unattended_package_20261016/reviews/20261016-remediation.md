# Review Report: Unattended package generation

## Summary
Review corrections are implemented and locally verified; the full native workflow remains incomplete and must not be archived.

## Verification Checks
- [ ] **Plan Compliance**: Partial — UP-01–03 implemented; UP-04/05 native selection, generation, persistence, replay/recovery and integration incomplete.
- [x] **Style Compliance**: Pass — existing assembler reused, synthetic regression inputs and private native receipts retained; source/case/approval boundaries preserved.
- [x] **New Tests**: Yes — engine drift/restart, oversized and growing files, replay symlink refusal, encoded request/provenance limits and file/directory collisions.
- [ ] **Test Coverage**: Partial — implemented local/kernel paths verified; latest native script and end-to-end Word/save/recovery/access remain unqualified.
- [x] **Test Results**: Passed — runner, cloud kernel and assembler suites; 608 repository checks, zero failures/pending. Retained native v2 ZIP independently reverified for SHA256/CRC/bytes/job provenance. No new live run inferred.

## Findings

### [High] Full native workflow is not complete — open acceptance gap
- **File**: `conductor/archive/ppg_unattended_package_20261016/plan.md` (UP-04/05).
- **Context**: A saved qualification flow and one primitive ZIP run do not implement native frozen record selection, generated Word output, output persistence, replay/edit recovery or integrated unattended operation. The newest corrected kernel is not native-qualified. Production Word entitlement and coverage above the cloud size cap remain unresolved.
- **Suggestion**: Keep the existing track in progress. Qualify each remaining native behavior through the assigned writers, retain actual output/readback and resolve entitlement/required-size coverage before completion and archive. Do not narrow the acceptance contract to local assembly. No code-only patch can establish these external facts.

### [Medium] Runner changes did not invalidate old job revisions — fixed
- **File**: `tools/unattended-package/run.cjs` (Lines L4-L9, L33-L36, L56-L57).
- **Context**: The previous engine fingerprint included only assembler bytes read from disk; runner changes could replay an older revision, and module caching could execute different assembler bytes from those hashed.
- **Suggestion**: Applied: execute the exact captured assembler source, bind both runner/assembler hashes, refuse in-process drift and fail closed for old receipts. Regression copies prove loaded-engine refusal and restarted-engine revision conflict. Existing output is preserved.

### [Medium] File-size checks did not bound actual reads — fixed
- **File**: `tools/unattended-package/run.cjs` (Lines L12-L24, L29, L48, L56-L58).
- **Context**: Job files were read before size rejection; attachment stat checks could be invalidated by growth. Replay artifacts were unbounded and could follow final symlinks.
- **Suggestion**: Applied: bounded handle reads enforce limits during reading and refuse final symlinks on the qualified POSIX route. Oversized/simulated-growth and replay-symlink regressions pass. This does not claim hostile parent-directory swap protection or power-loss durability.

### [Medium] Cloud bounds excluded generated provenance and escaped request overhead — fixed locally
- **File**: `scripts/ppg_cloud_package.ts` (Lines L27-L29, L66-L70).
- **Context**: Raw attachment totals alone allowed the complete uncompressed content to exceed the advertised cap; string parameters expand again when JSON-encoded for the connector.
- **Suggestion**: Applied: count escaped request parameters and provenance bytes before ZIP construction. Near-limit provenance and quoted-input regressions fail visibly. Actual connector qualification of this revision is still required.

### [Medium] File/directory ZIP collisions could prevent full extraction — fixed locally
- **File**: `scripts/ppg_cloud_package.ts` (Lines L49-L54).
- **Context**: Exact-name checks allowed both `a` and `a/b`, including a child beneath the reserved provenance filename. ZIP readers can list both while extraction cannot preserve both as files.
- **Suggestion**: Applied: refuse normalized, case-insensitive ancestor/descendant collisions in either order, including the reserved provenance path. Regression fixtures cover both orders and reserved ancestry.

## Decision
All identified code fixes in the implemented components are applied. Keep the
track `in_progress`; archive is conditional on completed UP-04/05, not review-only
closure. Conductor received a scoped blocker/solution request; its update says the
separate Developer Word USE-only connection handoff is being resolved. That update
is not PPG output proof or production entitlement. Existing native object ownership,
working manual outputs and source-sync objects remain unchanged.

Review scope includes runner/kernel, focused tests, one-time template authoring,
operator documentation and track acceptance. Unrelated concurrent working-tree
changes were excluded. Earlier review at441647e remains historical evidence, not
acceptance of subsequent native work.
