# Review Report: Dataverse migration

## Summary
Offline reconciliation fixes are verified; full migration remains incomplete and is not eligible for archival.

## Verification Checks
- [ ] **Plan Compliance**: Partial - DV-02/03 delivered; DV-01 target qualification and DV-04/05 native acceptance remain incomplete.
- [x] **Style Compliance**: Pass - existing Python standard library, synthetic tests and private operational receipts.
- [x] **New Tests**: Yes - malformed optional references, circular histories and a valid 1000-event chain with shared references.
- [x] **Test Coverage**: Partial - offline behavior checked; no native import/security/recovery acceptance claimed.
- [x] **Test Results**: Passed - 13 focused tests, 160 full-suite tests, 618 setup checks and diff whitespace check; actual CLI valid parity and cycle rejection verified.

## Findings

### Medium — False-valued optional identities bypass validation (fixed)
- **File**: `scripts/ppg_dataverse_reconcile.py` (Lines L33-L35, L86-L96)
- **Context**: False, zero, empty arrays and empty objects were treated as blank lookup values. Identical malformed exports incorrectly passed reconciliation.
- **Suggestion**: Applied explicit absent/null/empty-text handling; other values must pass UUID validation.
```diff
- if not row.get(field):continue
+ if not populated_reference(row.get(field)):continue
```

### Medium — Circular event histories pass matching-export reconciliation (fixed)
- **File**: `scripts/ppg_dataverse_reconcile.py` (Lines L38-L54)
- **Context**: Two existing correction events could refer back to one another. Resolution and same-case checks alone accepted the impossible append-only history.
- **Suggestion**: Applied iterative dependency validation across parent/correction links. Valid shared ancestors and long histories remain supported without recursion limits.
```diff
+ validate_history(indexed[dataset], history_fields)
```

### High — Full native migration acceptance is not implemented (open)
- **File**: `conductor/archive/ppg_dataverse_20261016/plan.md` (Lines L3-L12)
- **Context**: No confirmed migration destination, selected solution/publisher, native schema/import/readback, least-privilege parity, full history/file/flow reconciliation or recovery/cutover proof exists. Candidate reads and green local tests do not supply these deliverables.
- **Suggestion**: Keep track in progress. Resolve the existing exact-target decision, qualify the dedicated PPG container/environment and complete DV-04/05 with native receipts. Preserve SharePoint and unrelated native objects. Archive only after actual completion; the user's review instruction does not identify a target or waive its qualification.
```diff
  - [ ] DV-04 native pilot acceptance
  - [ ] DV-05 full migration parity and recovery
```

Review scope: initial offline implementation a80af0d and Dataverse-specific continuations through f0fa073; reviewed only this track's code, mapping, tests and documentation, preserving unrelated concurrent edits. Prior dated proof is historical; current assertions use this review's local execution and existing candidate receipt only. No native/authentication mutations performed during review.
