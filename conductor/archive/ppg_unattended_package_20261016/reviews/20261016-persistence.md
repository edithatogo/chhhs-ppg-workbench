# Review Report: Unattended package generation

## Summary
Native binary persistence is corrected and independently verified for a fictional happy path; full native lifecycle acceptance remains incomplete.

## Verification Checks
- [ ] **Plan Compliance**: Partial — local runner and native packaging/persistence happy path pass; UP-04/05 remain incomplete.
- [x] **Style Compliance**: Pass — existing connector, script, assembler and object owners retained; raw bindings stay private.
- [x] **New Tests**: Yes — actual binary transport failure reproduced and corrected native stored output checked independently.
- [ ] **Test Coverage**: Partial — local suites, actual binary persistence and destination-collision preservation pass; full native recovery remains unqualified.
- [x] **Test Results**: Passed for implemented components — focused suites and617 repository checks; actual corrected native run and ZIP verification pass.

## Findings

### [High] HTTP string body corrupted binary ZIP — corrected
- **File**: `docs/unattended-package-generation.md` (native persistence correction; native flow's output action).
- **Context**: The initial persistence run succeeded but stored1504bytes instead of the1494-byte runtime ZIP. Its replacement sequences are reproduced exactly by UTF-8 decode/re-encode. Successful run status was insufficient.
- **Suggestion**: Applied binary Create file in new empty controlled staging plus Move file with actual native Fail conflict option. The fresh exact run's inputs and output match downloaded ZIP bytes, CRC, membership, source member hashes and frozen job provenance. A deliberate collision preserves final identity/ETag/bytes and the staged duplicate. The flow is Off with no pending run; preserve these artifacts and implement receipt/recovery before further operation. Do not use string-body HTTP upload or overwrite an existing revision.

### [Medium] Private latest-run pointers still described historical failure — corrected
- **File**: `.local/unattended-package/cloud-qualification/native-bindings.json` (ignored private evidence).
- **Context**: Current execution was falsely recorded unverified and an older script ID was selected despite retained v4 proof.
- **Suggestion**: Independently reverified artifact/ZIP hashes and reconciled latest execution separately from first failure and historical revision fields. The current v5 persisted-output proof is separate from remaining native selection/replay/Word gates.

### [High] Complete native lifecycle is not delivered — open
- **File**: `conductor/archive/ppg_unattended_package_20261016/plan.md` (UP-04/05).
- **Context**: Static fictional job inputs and one saved ZIP do not implement native source selection, immutable commit-last receipt/replay/recovery, full Word behavior, required native size coverage, production entitlement or integration.
- **Suggestion**: Continue the existing owned graph using the retained Conductor protocol and distinct Word writer. Archive remains conditional on actual full acceptance; never replace missing runtime evidence with local tests or narrow the scope silently.
