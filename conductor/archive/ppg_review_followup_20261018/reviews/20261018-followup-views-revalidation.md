# Review Report: RF-03a existing-field follow-up views

## Summary

The selected views are implemented and revalidated through the CLI; visual and
ordinary-user acceptance remain explicitly unverified and do not block independent development.

## Verification Checks

- [x] **Plan Compliance**: Yes for selected RF-03a configuration slice — three existing-field, public/non-default views saved and read back; existing source/case state preserved by the original deployment. The wider RF track remains incomplete.
- [x] **Style Compliance**: Pass — existing standard-library Python/JSON and shared guided-workspace formatter; no dependency, application or tenant schema added.
- [x] **New Tests**: Yes — root-site navigation validation and native readback drift checks; eight follow-up tests in total.
- [x] **Test Coverage**: Partial — 22 focused tests cover date categories, identity/navigation construction, field/schema assumptions, binding safety and saved properties. Browser rendering and actual filtered-link behaviour are not established by API checks.
- [x] **Test Results**: Passed — eight follow-up tests and fourteen workspace tests. Fresh exact-target CLI read returned nine views/94 fields; all three selected views matched expected configuration. Six navigation targets exist according to SharePoint file metadata.

## Findings

### Medium — fixed: root-site external navigation bindings

- **File**: `scripts/ppg_followup_views.py`
- **Context**: With a root-level site binding, the original prefix test accepted a protocol-relative `//other-host/...` path. Backslashes and other control characters were also not consistently refused.
- **Fix applied**: Reject protocol-relative paths, backslashes and all ASCII control characters. Synthetic regressions cover those rejected inputs. Current native bindings remain valid; native view formatting required no change.

### Low — fixed: repeat verification was private-only

- **File**: `scripts/ppg_followup_views.py`
- **Context**: The saved-view reconciliation logic was only retained in a private deployment adapter, making repeat verification unnecessarily dependent on that local file.
- **Fix applied**: Added reusable `verify_views` and `--verify-readback` for qualified native exports. It refuses missing/duplicate titles, changed fields/order/query/formatter, personal/default views, changed paging or row limit. Tests exercise every drift category and harmless XML/JSON serialization differences.

## Acceptance and scope

The authoritative execution queue defines this slice as save/readback of useful
views using current fields. That implementation is complete. Preserve the open
visual/ordinary-user checks as acceptance follow-up; they cannot become prerequisites
for unrelated schema/continuity/adoption development. The prior report's browser
sign-in observation is historical; no browser or new login was used in this pass.

Fresh native operations were bounded GETs through the same qualified M365 client.
No case item, source, rule, subscription, view, permission or notification was
written. Current case-form, readiness/assurance pages and the three selected view
pages exist under the intended site. File existence does not prove rendered cards,
CaseUID filtering, ordinary-user access or accepted human ownership/date agreement.
Detailed receipts remain private at `.local/review-followup/revalidation-20261018/`.

All cases remain visible: these are focused views, not a clinically prioritised or
exceptions-only work queue. Missing/conditional/invalid/past dates remain distinct;
role text remains separate from accepted responsibility. RF-02 data/transition
work, RF-03b optional form assessment and operational observations are separate.
No full-track completion, measured benefit, new licence or business approval claimed.
