# Review Report: Unattended package generation

## Summary
A newly found blocking-file defect is fixed and the current cloud primitive has actual native execution proof; full track acceptance remains incomplete.

## Verification Checks
- [ ] **Plan Compliance**: Partial — UP-01–03 and current native packaging primitive verified; native selection, Word generation, persisted output/replay/recovery and UP-05 remain incomplete.
- [x] **Style Compliance**: Pass — existing assembler/platform reused, exact source/engine/version separation and private receipts retained.
- [x] **New Tests**: Yes — separate-process FIFO input check verifies bounded termination without a writer.
- [ ] **Test Coverage**: Partial — runner/kernel/assembler paths verified; complete native workflow and required larger-package coverage remain unqualified.
- [x] **Test Results**: Passed — runner, cloud kernel and assembler suites;614repository checks, zero failures/pending. Actual v4 run succeeded and independent native ZIP proof passed.

## Findings

### [Medium] Opening a FIFO could block before type validation — fixed
- **File**: `tools/unattended-package/run.cjs` (readBounded, Lines L12-L18).
- **Context**: O_RDONLY open waits for a FIFO writer before fstat can reject the nonregular file, so a supplied job could hang indefinitely despite bounded reads.
- **Suggestion**: Applied pre-open lstat regular-file check and O_NONBLOCK alongside O_NOFOLLOW; retain opened-handle type validation for races. A spawned runner given a real FIFO exits with INPUT_NOT_FILE within the regression timeout. No source/output modification.

### [High] Full native delivery is still incomplete — open
- **File**: `conductor/archive/ppg_unattended_package_20261016/plan.md` (UP-04/05).
- **Context**: Current v4 native execution and exact input/script/ZIP proof close the stale-kernel gap. They do not supply native input selection, generated editable Word content, create-only native output save, immutable commit-last receipt/replay/recovery, full integration, production entitlement or larger required-package support.
- **Suggestion**: Continue the same owned flow and existing distinct Word writer. Conductor has the completed primitive evidence and remaining-blocker request. Do not archive or narrow acceptance to local assembly/one native primitive.

## Native evidence and changed browser state

The v4 fictional run succeeded in8seconds. Its1494-byte ZIP independently matches
hash, CRC, exact membership, original attachment and frozen job provenance. Native
runtime script ID/inputs match the uploaded revision; actual artifact hash/ETag are
unchanged after the run. Detailed bindings/receipts stay ignored and private.

During later output-persistence action preparation the whole owned browser group
disappeared; tool listing confirmed absent handles. No save/test followed adding
that action, so no saved persistence step or file write is claimed. The run was
already terminal. Reopen the same existing flow, reconcile saved graph and continue;
never rerun/recreate solely because observation/editor handles are missing.

## Decision
Apply and retain the fix and native evidence. Track stays in_progress and archive
stays conditional on full UP-04/05. No clinical/source/case/permission/authentication
or scheduler changes are inferred. Existing Word/template writer remains separate.

## Persistence continuation checkpoint

The reopened editor confirmed the saved v4 trigger/Run script graph. A new
SharePoint create-only action was prepared but never saved or run. The FX editor
rejected the attempted expression; selecting the exposed ZIP field did not add a
reference to Body. No valid saved expression is claimed. The unsaved action was
discarded through the native layout-switch prompt. The same editor then remained
blank for several minutes; one bounded reload did not recover it. Stop that
unchanged route rather than stack unsaved actions or rerun the successful kernel.
The existing authenticated SharePoint route independently returned404 for the
intended output file at09:54UTC. Native file persistence remains unperformed.

Conductor supplied the next implementation protocol: pin an explicitly prepared
immutable job and selected source versions/hashes; reconcile existing package and
receipt before creation; create the package exclusively, read back and verify its
bytes, then exclusively create the completion receipt. A package without a receipt
is incomplete and must be reconciled on retry. A receipt without its exact package,
an edited file or a changed fingerprint must fail closed. Qualify duplicate replay,
failure between package and receipt, and edited-file refusal. Concurrency alone is
insufficient. This protocol is guidance, not deployed or qualified implementation.

The2MB raw/4MB wire bounds are implementation limits, not a demonstrated Microsoft
platform maximum. Conductor has no qualified larger native route or production
Word entitlement to hand over. The existing bounded local fallback remains
available; it does not close the outstanding native acceptance gates.
