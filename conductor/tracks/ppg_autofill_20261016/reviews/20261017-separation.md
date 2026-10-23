# Native correction-separation review — 17 October 2026

The existing pilot now separates disposable Autofill `Suggested*` values from
three `Reviewed*` values plus provenance/operation identity. Reviewed fields have
no AutofillInfo. No canonical-source/case/permission/billing changes or production promotion.
The unchanged fictional AF02 file was deliberately re-uploaded to exercise processing.

## Verified behavior

- Native unchanged AF02 CSV re-upload reaches a new classification timestamp and
  Finished state stable across three reads; both retained fictional corrections
  and provenance remain unchanged. Legacy AF01 correction migrated with provenance.
- Nine focused tests cover owned writes, exact pins, raw prompt drift, stale state,
  canonical-field refusal, native header construction, race refusal and replay.
  Two unchanged authentication-adapter tests pass separately.
- Actual concurrent exact-ETag applies produce one winner and one native409;
  separate old-ETag MERGE returns412 and leaves winner unchanged. A stale operator
  snapshot fails before write. These are distinct native observations.
- Deliberately lost local response after one native commit recovers by exact-
  operation read-only replay; no additional write/version. Changing the request
  under that operation identity is refused by the contract.
- Six original source byte hashes/identities/earlier versions preserved. Final
  raw prompts Off; reviewed/provenance fields still have no AutofillInfo. Native
  inherited permissions and versioning unchanged.
- Existing raw/reviewed view and versioned v0.4 guide/kit downloaded exactly;
  shared manifest update preserves unrelated entries, hub updates only its owned
  control, page checked in/published, repeat reads leave native ETags unchanged.

## Scope and limits

Accept this bounded fictionalCSV ownership-separation/operator route Off. Raw
columns remain unsafe for human corrections. Native form edits outside the guarded
apply command do not enforce its provenance contract; no field-level security is
claimed. Replay confirms a historical recorded operation, not review of a later
source version. Config/prompt changes invalidate old snapshots. Source/version/
raw suggestions are retained as provenance; substantive semantic evaluation and
policy approval remain unperformed. Other shapes and production eligibility are
not established. No automatic promotion, notifications or scheduled processing.

Private proof: `.local/autofill/separation-20261017/separation-summary.json`,
`publication-summary.json`, final native items/fields, retained source histories.
