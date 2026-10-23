# Review Report: historical template reconciliation

## Summary

Complete accounting and exact correspondence proposals are usable; semantic
acceptance and generated-output qualification remain separate.

## Verification Checks

- [x] **Plan Compliance**: SP-04c2 accounts for all158 earlier and70 native elements, including blank/ambiguous/unmatched content, without changing frozen references.
- [x] **Style Compliance**: Small read-only utility using existing inventories and Python standard library; sensitive outputs stay private.
- [x] **New Tests**: Seven regression tests exercise adjacent table cells, ambiguous repetition, changed wording, link targets and link scope within a partial row; inputs remain unchanged.
- [x] **Test Coverage**: Seventeen focused local tests pass. Actual archived source bytes reproduce the full reconciliation, beyond synthetic tests.
- [x] **Test Results**: Downloaded12-member archive passes CRC/all hashes, exact map recomputation and seven isolated tests.
- [x] **Native evidence**: Four companion files read back exactly with inherited access; replay creates zero with identities/versions preserved.

56 unique candidates are proposals, not approved mappings.72 blank/structural,
28 ambiguous and2 unmatched blocks stay explicit. No source IDs, reviewer records,
held-run pins or maintained Word are changed. Correspondence is not full visual or
regeneration parity. The pre-edit native template snapshot is the hash-bound target;
the separately retained development edit does not silently become that target.
No unresolved code defects found within this bounded read-only scope.

Review correction: table-level de-duplication could hide distinct paragraph/span
locations within the same table. Fixed by comparing actual paragraph-node coverage;
a regression test preserves that ambiguity. Successor version2 retains13 additional
ambiguous entries; version1 remains a frozen interim snapshot and applied no mappings.
