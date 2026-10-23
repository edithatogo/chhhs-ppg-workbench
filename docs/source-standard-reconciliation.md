# Source standards: reconciliation and recovery

The integration-owned reconciliation supplement preserves every `sourceStandard`
assertion in the retained985-row catalogue snapshot. It is separate from the
eight Proposed passage-backed historical mappings in the standards registers.
It neither replaces those mappings nor changes the source/importer fields.

All25 raw fields per row reproduce the exact retained XLSB:24625 cells,985 stable
document identities and both standards-tracking worksheets. Two retained absent
identities remain outside the active985-row count; no retirement is inferred.
The original workbook is retained unchanged, including macros/links; only cached
values are read. No macro, calculation, refresh or external link is executed.

| Source label | Assertions | Reconciliation |
|---|---:|---|
| 1 | 301 | Candidate heading; edition unverified |
| 2 | 24 | Candidate heading; edition unverified |
| 3 | 66 | Candidate heading; edition unverified |
| 4 | 250 | Candidate heading; edition unverified |
| 5 | 191 | Candidate heading; edition unverified |
| 6 | 82 | Candidate heading; edition unverified |
| 7 | 17 | Candidate heading; edition unverified |
| 8 | 52 | Candidate heading; edition unverified |
| 9 | 2 | Unmapped; meaning needs confirmation |

The numeric1–8 labels permit983 heading retrieval candidates against the checked
second-edition index. They do not establish the source edition, current obligation,
action-level relevance or compliance. Strings, booleans, blanks and compound labels
are preserved without coercion into numeric candidates. No draft-edition crosswalk
is inferred. Stable assertion keys bind snapshot, document identity and exact
source value; row numbers are locators, not permanent document identities.

## Cached report discrepancies

`STANDARDS TRACKING` caches986 total against985 retained main rows. Its Standard4
count is252 against250; Standard5 is189 against191; Standard6 is83 against82.
The other six numeric labels agree. The cause is unverified: do not assume a missing
document, changed classification or stale formula as an established explanation.
`OVERDUE BY STANDARD` is preserved separately; its filter scope is unverified and
its counts must not be presented as totals for the active catalogue. The source's
original labels and report values remain intact for investigation.

## Use and recover

Use the existing approved evidence library's
`ReviewIntelligence-source-standards-v1/README.md`. Five native versioned files hold
the readable scope, aggregate summary, per-document ledger, cached worksheet/raw
extract and recovery ZIP. Native paths, identities and receipts are private under
`.local/review-intelligence/20261020/source-standard-reconciliation-v1/`.

The ZIP contains11 members: original workbook, exact import candidate, framework
definitions, field map, extraction/ledger/summary/guide, generation-time utility
and test, plus member-hash manifest. Before recovery, verify downloaded ZIP CRC,
every member hash and original-source hash. Extract only into a separate private
directory; do not execute workbook content. Reconstruct with the preserved inputs
and compare the complete ledger/extract. That downloaded-input reconstruction has
been verified to produce identical results.

The utility is `scripts/ppg_source_standards.py`. Reuse the qualified local Python
and existing read-only pyxlsb1.0.10 extractor, for example:

```sh
uv run --no-project --python .venv/bin/python --with pyxlsb==1.0.10 \
  python -m scripts.ppg_source_standards \
  --candidate /private/path/candidate.json \
  --workbook /private/path/original.xlsb \
  --definitions /private/path/frameworks-v1.json \
  --mapping /private/path/source-field-map.csv \
  --output /private/path/new-reconciliation
```

The utility refuses changed snapshot/raw values, incomplete or misbound identities,
unknown heading definitions and an existing output directory. Retry into a new
private directory and compare outputs; do not overwrite prior evidence. Native
publication uses the existing qualified CLI same-client adapter, server-side
create-only files and exact byte/identity/version readback. Identical retry creates
zero files; changed content is retained for reconciliation rather than overwritten.
The supplement inherits existing evidence access; no ACL change is made.

No native mapping, flow, solution component, source correction, clinical decision,
notification or policy issuance is introduced. This completes source assertion
accounting and exposes mapping/report gaps; confirming source taxonomy and accepting
clinical mappings remain explicit later judgements. Native reference/acceptance
validation and current procedure/template verification remain separate open work.
