# Review Report: RF-01/RF-03a follow-up views

Original deployment checkpoint. See [current CLI revalidation](20261018-followup-views-revalidation.md) for implementation and acceptance separation.

## Summary

Three additive native views are saved and technically verified; visual acceptance
and remaining track scope are explicitly incomplete.

## Verification Checks

- [x] **Plan Compliance**: Partial — selected existing-field slice implemented; browser rendering and ordinary-user acceptance remain open. No RF-02 transitions or optional app introduced.
- [x] **Style Compliance**: Pass — existing Python/JSON and shared presentation helper; no new dependency, secrets or operational bindings in tracked changes.
- [x] **New Tests**: Yes — five synthetic follow-up tests.
- [x] **Test Coverage**: Partial — schema drift, injection bindings, view focus, additive/non-default scope and date categories covered; actual browser links/rendering not verified.
- [x] **Test Results**: Passed — five follow-up tests plus fourteen existing workspace tests. Native same-client readback and repeat passed; current rules/subscriptions zero each.

## Findings

### Medium — Visual acceptance remains unavailable

- **File**: `docs/followup-views.md`
- **Context**: BrowserOS reaches organisation sign-in. Saved JSON and native API metadata do not prove rendered cards or navigation.
- **Disposition**: Keep RF-03a and the wider track in progress; next operation is authenticated-browser rendering and link verification. No extra licence or consent required by this implementation.

### Low — Setup validation caught documentation integration gaps

- **File**: `conductor/tracks/ppg_review_followup_20261018/plan.md`
- **Context**: Initial validation found the not-yet-written review link and an evidence checklist exceeding the bounded plan task limit.
- **Disposition**: Added this report and changed evidence subitems to ordinary evidence bullets; retain the original seven task slices.

## Native evidence and scope

Private receipts: `.local/review-followup/20261018/`. Three exact-title views were
created; queries, ordered fields, formatter, row limit 30, paging and non-default
status read back. Repeat reused all three without mutation. Case-item snapshots
and existing views were preserved. Same-client transport suppressed automatic
mutation retries and redirects; no credentials transferred between clients.

Current case fields and exact-target permissions were read before mutation.
Rules enumeration included quicksteps/automatic rules; subscriptions read
separately. Empty current inventories do not establish the absence of every
external automation. No record, permission, assignment, source, default view or
notification mutation occurred. All cases remain visible; dates are agreement
checks and roles are recorded text. Event-contract gap mapping remains RF-01 work.

Review scope is only the selected follow-up changes, not other lifecycle work.
Retain the track; neither archive nor full-track completion is justified.
