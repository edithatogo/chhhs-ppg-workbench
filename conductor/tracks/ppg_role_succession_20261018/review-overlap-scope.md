# Review Report: overlapping appointment scope

## Summary
Ambiguous appointments cannot expose an arbitrary selected delegation scope.

## Verification Checks
- [x]Both orderings retain ambiguous state, no holder/scope and both candidate IDs.
- [x]Single-appointment scope checks and historical input preservation remain intact.
- [x]Fresh12-row native qualification export projects unchanged.
- [x]19 role tests and actual synthetic-scenario CLI outputs pass.
- [x]Six native files/readback/replay0; downloaded13-member archive reproduces regression/fix/baseline.
- [ ]Actual native overlap creation and ordinary-user acceptance are not claimed.

Synthetic overlap is local only; stored role records/snapshots/actors unchanged.
This corrects the existing hold contract and introduces no workflow transition,
authority, permission or notification. Operational details remain private.
