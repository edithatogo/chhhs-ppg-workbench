# Review Report: Archive reconciliation

## Summary

All four original technical requirements are implemented and verified against recovered original archives and actual native bytes; review fixes are applied and the track is archived complete.

## Verification Checks

- [x] **Plan Compliance**: Yes; AR-01–04 individually audited. Exact originals, per-entry/WARC accounting, native coverage, repeat/preservation/navigation and operator handoff delivered.
- [x] **Style Compliance**: Existing SharePoint archive, standard same-client transport and private receipts. No archive extraction/execution, source-policy write, inferred currency or replacement runtime.
- [x] **New Tests**: Eight member/WARC tests and two archived-dependency tests; existing reconciliation/edition checks retained.
- [x] **Test Coverage**: Eighteen focused tests, actual original ZIP/CRC/payload accounting and659 actual native downloads. Scope excludes clinical judgement and ordinary-user acceptance.
- [x] **Test Results**:18pass. All724 top-level members,1,986 WARC records and606 Office parts accounted. All659 native captured hashes match429,420,904 downloaded bytes; original667 file frames unchanged; all source/metadata/control replays0writes. Two native capture views verified.

## Findings and fixes

### High — Original-media blocker was stale and recoverable — fixed

The original ZIPs were absent from currently mounted media, but another repo
retained network references and a local chat retained a verified backup receipt.
Recovered through that existing route, then matched both independent SHA256/size
identities. Original member/catalogue counters now match the retained666 exactly;
eight WARCs expose two earlier uncatalogued HTML captures. Preserved both separately
with server-side overwrite=false and full metadata/byte/repeat readback. No additional
original document stream is missing. Detailed exclusions remain accounted.

### High — Metadata timestamp presentation could cause an unnecessary repeat write — fixed

The first saved metadata returned Brisbane-local text rather than the submitted
UTC string. Native timezone/field inspection and LocalTimeToUTC establish exact
instant equivalence. Adopted the saved result without rewriting it, completed the
other absent metadata update once, and verified metadata replay0writes. Original
raw evidence and failed presentation checks retained; no timezone/schema changes.

### Medium — Moving a dependency into archive made it disappear from setup validation — fixed

`scripts/check_setup.py` now resolves active and archived dependency metadata
without changing their statuses. Incomplete archived tracks remain incomplete;
missing dependencies remain unknown; duplicate or mismatched identities fail.
Two targeted regressions pass. The edition track retains its dependency and its
own unfinished family requirements; it is not automatically completed.

### Medium — Source change and unsupported archive structures could overstate accounting — fixed

The read-only member auditor keeps duplicate members by ordinal, validates each
stream's CRC/hash/size, rechecks the complete source hash, bounds reads, and records
unsupported members explicitly. WARC parsing verifies bounded headers, lengths,
stored response payload digests and all physical record occurrences. Unknown
record types/digests never become qualified. It exports no HTTP headers and never
extracts or executes members. Eight focused adverse/positive tests pass; actual
CLI refused overwriting its receipt and saved mode600.

## Completion and archive

All4 original technical tasks complete; no archive-reconciliation blocker remains.
Full scoped technical acceptance is true. All review fixes applied and documentation,
per-task audit, dependency handoff and native report/index/guide updated. Raw native
IDs, bytes, full manifests and receipts remain private; prior evidence is retained.
Ordinary-user acceptance and policy identity/printed-edition/authority decisions
remain separate, not passed. Track archived by explicit user request.

Final repository check:3,828 passed,0 failed,0 pending. Original plan history is
byte-identical to its committed preimage; all4 original task audit entries are
complete. Existing unrelated uncommitted work remains outside this commit.
