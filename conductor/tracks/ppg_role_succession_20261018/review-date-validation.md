# Review Report: RO-02/03 canonical role dates

## Summary

The local projection now refuses noncanonical date inputs without changing valid historical or current results.

## Verification Checks

- [x] **Plan Compliance**: Partial — enforces existing effective-date contract; transfer application and remaining acceptance stay open.
- [x] **Style Compliance**: Pass — shared validator, explicit failures, no native writer or data in Git.
- [x] **New Tests**: Yes — malformed inputs across date fields, leap-day and historical-boundary checks.
- [x] **Test Coverage**: Partial — local resolver/projection/snapshot checks plus current native export comparison; native forms are not validated by this code.
- [x] **Test Results**: Passed — eighteen focused tests; three valid projections unchanged, invalid CLI invocation creates no output.

## Evidence and limits

Before the fix, compact and week-date as-of strings were accepted and echoed as output identities. The shared parser now requires ASCII YYYY-MM-DD plus a valid Gregorian date. Start/end and handover fields use the same guard. False/zero end values cannot become open intervals. Null/missing/empty ends retain documented behavior.

Fresh read-only CLI exports match all five original fictional source records across four registers. No native records, snapshots, assignments, access or historical actors changed. Private receipts preserve source hashes and exact before/after projections. Future snapshot implementation hashes change by design; existing evidence is not repinned. This is enforcement of the documented contract, with no new workflow route or alteration to frozen releases.

The track remains in progress. This review does not establish current real-role assignments, native form enforcement, portfolio-transfer application, copied recovery or ordinary-user acceptance.
