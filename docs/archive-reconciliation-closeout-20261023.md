# Archive reconciliation — completed 23 October 2026

All four original technical tasks are implemented, reviewed and archived.
[Archived plan](../conductor/archive/ppg_archive_reconciliation_20261017/plan.md),
[task audit](../conductor/archive/ppg_archive_reconciliation_20261017/task-audit-20261023.json)
and [review](../conductor/archive/ppg_archive_reconciliation_20261017/review-closeout-20261023.md).

## Original-media blocker resolved

A search including ignored evidence folders found the clinical-hub repository's
archive references and another local chat's independently verified backup receipt.
The unmounted network copy was not needed: the existing configured backup route
returned both originals. Downloaded bytes and sizes exactly match that earlier
receipt: cairns-intranet-evidence-20260921.zip and
cairns-public-website-mirror-20260907.zip. Originals and hashes are retained privately
under `.local/archive-closeout-20261023/originals/`. No new account, consent,
permission, connector, licence or source write was required.

## Complete accounting and native result

| Requirement | Verified result |
|---|---|
| ZIP identity and members | Both original identities exact; all724 top-level members hashed and CRC-checked. |
| Original source catalogue | All666 occurrences match retained archive/member/hash tuples exactly;105 distinct document streams covered. |
| WARC exhaustiveness | All8 containers parsed;1,986 physical records accounted, including986 response occurrences with exact SHA256 payload digests. Combined/component duplicates retain their separate provenance and are not counted as new editions. |
| Office packages | All16 unique captured Office ZIP containers accounted;606 internal parts CRC-verified. Whole document packages remain intact. |
| Earlier uncatalogued content | Two earlier HTML source-page captures found in objects/WARCs, separately preserved with their original provenance. No new document stream was missing. |
| Native content | All659 captures independently downloaded and SHA256/pin-verified:429,420,904 bytes. Final637 documents and22 supporting pages. |
| Preservation | Original667 native file metadata/pin records remain exact. Supporting pages remain distinct from policy documents; no currency, family, approval or retirement inferred. |
| Native writes/replay | Two absent-only source-page creates and two metadata updates;3 new accounting/index/guide files. Every replay creates0files and changes0metadata. Existing indexes/history preserved. |
| Navigation | Both existing Archive captures — provenance and Archive captures — source locator views verified natively; published member CSV maps represented content to native capture paths. |

Every top-level member and WARC record has a private accounted disposition.
Captured non-document resources retain their existing exclusions/provenance;
archive code, replay assets, indexes and control files remain preserved in the
original ZIPs without being represented as policies. Distinct byte streams and
all duplicate occurrences remain separately accounted. No URL/title deduplication.
The report/CSV/guide were created without overwrite in the existing archive folder,
downloaded with exact hashes and replayed with zero creates.

The first metadata readback exposed the existing DateTime field's Brisbane-local
presentation of a submitted UTC timestamp. Native field/timezone reads and
LocalTimeToUTC proved the original instant exactly. Reconciliation adopted the
first saved metadata without another write; the second update then completed.
Raw and canonical date evidence is retained. No timestamp, timezone or schema
was changed to force a check to pass. Initial same-process SDK account guards
also stopped before creation; separate existing-client operations completed the
work without credential transfer or permission changes.

Private final proof: `.local/archive-closeout-20261023/qualification-audit.json`.
It binds the source/ZIP/WARC accounting, all659 actual byte receipts, original-file
frame preservation, repeated source/control receipts and final native readback.
Earlier17October receipts remain unchanged and keep their original dated limits.

## Reusable read-only audit

The added CLI never extracts an archive, opens embedded content as code or writes
the source. It retains duplicate names by ordinal, validates expected identity,
CRC/size, byte limits and post-read archive identity, and creates private receipts
without overwrite. It parses stored WARC response payloads and checks their
SHA256 digests. Unknown record types/digests, malformed/truncated records, changed
archives, symlinks and resource limits remain explicit unverified outcomes.
It does not replay HTTP or infer policy identity/authority. ZIP/WARC accounting
alone always reports fullOriginalArchiveAcceptance=false; the separate native
reconciliation audit supplies the full scoped acceptance above.

```sh
.venv/bin/python scripts/ppg_archive_member_audit.py ORIGINAL.zip .local/NEW-private-audit.json --expected-sha256 REVIEWED_SHA256
PYTHONPATH=scripts .venv/bin/python -m unittest tests.test_archive_member_audit tests.test_archive_reconciliation tests.test_archive_editions tests.test_archived_dependencies
```

Eighteen focused tests and3,828 repository checks pass, including corruption, duplicate names/content,
unsafe extraction paths, symlinks, limits, changing input, WARC digests/truncation
and archived dependency identity. Actual CLI create-only receipt and600 permissions
were also checked. The repository checker now resolves archived dependencies
without treating incomplete archival status as completion or silently dropping
unknown dependencies. Duplicate/mismatched identities fail closed.

## Handoff and remaining boundaries

There are **no remaining archive-reconciliation implementation blockers**.
The edition-management dependency now points to this completed archived track;
its obsolete original-media blocker is removed. Existing44 qualified singleton
links and1 printed-edition conflict are preserved; real family resolution and
native family migration remain that separate track's work. Capture evidence does
not establish current policy authority or clinical approval. All third-party
access/usefulness/adoption testing remains in the final user-deferred adoption
track, unperformed. No additional participant review is claimed by this closeout.
