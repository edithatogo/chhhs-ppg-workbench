# Review Report: validator-aware recovery follow-up

## Summary
Post-restore calendar checks preserve recovered histories and cannot be silently omitted by provisioning.

## Verification Checks
- [x]17 copied records/20 versions/audit values and stored snapshots unchanged.
- [x]Five invalid conditional writes refused; migration replay0.
- [x]Read-only working schema checks and actual missing/drifting-validator refusals.
- [x]Explicit archived-schema CLI path plans real older17/20 backup; no native writes.
- [x]18 role tests cover compatibility, schema mismatch and output preservation.
- [x]Nine native files/replay0, downloaded12-member CRC/hashes and isolated report reproduction.
- [ ]Fresh full native restore/rollback, cross-record rules and ordinary-user adoption unqualified.

Frozen workflow1.5.1 remains the behavior baseline. This closes the post-restore
validator proof gap, not wider recovery or clinical acceptance. Raw IDs/data private.
