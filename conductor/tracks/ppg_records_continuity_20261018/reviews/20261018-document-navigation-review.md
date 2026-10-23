# Review Report: RC-01/RC-02a document navigation

## Summary

The selected existing-field navigation is implemented and natively verified;
full records continuity, browser/access acceptance and business authority remain separate.

## Verification Checks

- [x] **Plan Compliance**: Yes for RC-01/RC-02a — mapped existing draft/reference/authority/history resources; saved two non-default views; unknown/conflicting authority retained. No upstream update, issued-file replacement or handoff sending.
- [x] **Style Compliance**: Pass — existing Python/JSON, common path validation, guided formatter and readback verifier; no new dependency or app.
- [x] **New Tests**: Yes — four focused document-navigation tests, including native expression evaluation with synthetic records.
- [x] **Test Coverage**: Partial — 26 focused tests pass; native save/readback, queries, repeat and preservation verified. Browser rendering, actual filter interaction and ordinary-user access unverified.
- [x] **Test Results**: Passed — four document-navigation, eight follow-up and fourteen workspace tests. Native view repeat: zero writes; original seven cases/1,197 library items preserved. Queries: seven cases/657 captured references and pages. Eight page targets exist by API readback.

## Findings

### Medium — fixed before native application: archive folder boundary

- **File**: `scripts/ppg_document_navigation.py`
- **Context**: A simple descendant prefix would exclude files directly in the archive root; a bare archive-name prefix would include similarly named adjacent folders.
- **Fix applied**: Exact root OR slash-delimited descendants, combined with file/capture-hash checks. Synthetic query evaluation covers root, descendants, sibling-prefix collision, folder and missing-hash exclusions. Native query accounts for all 657 captures.

### Low — fixed: draft/evidence reference needed first position

- **File**: `scripts/ppg_document_navigation.py`
- **Context**: Reusing the action-focused case formatter originally put action before the draft link/reference, weakening the selected navigation purpose.
- **Fix applied**: Move the existing recorded draft/evidence reference to the first data row, retaining the missing-link warning and all case context/history links. Test asserts position and all-case visibility.

## Native evidence and boundaries

Exact-target field/permission reads and rule/subscription inventory preceded view
creation through the existing same-client CLI transport. Native mutation was
limited to two new owned views (create then set formatter/scope). No automatic
mutation retries or redirects. Original views, fields, case/library item snapshots,
defaults and version/approval/checkout settings matched before/after. Explicit
readback confirms current inherited permissions on both resources; the native
operation trace contains no permissions changes.
Repeat reconciled exact titles and performed zero view/item writes. Query and
page-existence reads made no content changes. Private receipts and deployment
adapter: `.local/records-navigation/20261018/`.

Current-authority and historical cards describe recorded findings; they do not
claim policy issuance, currency correctness, source completeness or approval.
Supporting pages remain distinct from policies. Existing publication assurance
navigation retains record state/version/evidence; no event or authority decision
was created. Unknown identities/editions and source conflicts remain visible.

No document generator was introduced: this is navigation, not production of a
structured policy/report. Existing templates and the preferred SharePoint document
route remain applicable to later document-generation work. No Purview/retention
policy, record lock, permissions, licence, feature, source register or notifications
were changed. RC-02b and RC-03/04/05 remain open; do not close or archive the full
track based on the selected view slice. Original-media exhaustiveness is not a
prerequisite for this independently verified navigation increment.
