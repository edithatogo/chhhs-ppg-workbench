# Follow-up views

23 October closeout: all three saved configurations pass fresh CLI readback. Current-account browser rendering verifies action/ownership/date presentations, unknown/conditional targets and CaseUID-bound hrefs. A direct server-relative browser navigation was rejected as invalid; it was not worked around and is not a fresh history-navigation pass. Prior operator navigation proof stays dated; ordinary-user acceptance is user-deferred. Dated open items below are superseded only to this scope. See the [final review](../conductor/archive/ppg_review_followup_20261018/review.md).

These existing case views remain available. The21 October
[native follow-up/history and digest route](followup-native-web.md) adds separate
versioned history and completed-snapshot views, including stage-entry and human
priority columns. It does not rewrite the case fields described below.

The existing case List has three additional public, non-default views:

| View | First information shown |
|---|---|
| Next actions and preparation gaps | Next action, source snapshot and draft/evidence reference |
| Ownership and handoff checks | Recorded content-review role; accepted ownership requires the case's consultation/handoff history |
| Date exceptions and agreement checks | Raw target and strict calendar/date check |

Select these by name from the case List view menu. All cases remain visible,
including unknown statuses and incomplete records. These are focused presentations,
not exceptions-only filters or an overdue work count. Text/Note fields and the
absence of an agreed terminal-state contract make automatic filtering misleading.
The existing Missing action or evidence view remains available for blank-field checks.

Dates reuse the guided workspace formatter: exact valid YYYY-MM-DD dates, with a
Brisbane end-of-day boundary; missing, invalid and conditional targets are distinct.
A past recorded date does not establish an agreed deadline. A free-text role does
not prove a person has accepted the work. Whitespace is retained as recorded text,
not silently normalised or treated as accepted ownership.

## Configuration and repeat operation

`config/followup-views.json` defines the three titles, fields and stable Created/ID
ordering. `scripts/ppg_followup_views.py` compiles create bodies and formatter
properties using the existing guided workspace helper. It does no authentication
or network operations and refuses missing fields, incompatible text fields and
unsafe/out-of-site bindings. Use the qualified current field export, not an
assumed schema. Keep bindings and generated output under ignored `.local/`.

```sh
.venv/bin/python scripts/ppg_followup_views.py \
  --bindings .local/review-followup/bindings.json \
  --fields .local/review-followup/fields.json \
  --output .local/review-followup/bundle.json
```

Bindings contain `site`, `queue_path`, `readiness_path` and `assurance_path`.
The last three are server-relative paths within the site; obtain them from the
existing object bindings. The output must not already exist.

Before a native apply, read exact-target permissions, fields, views and case items
through the existing qualified M365 client. Inventory `GetAllRules()` with both
include flags and list subscriptions separately from alerts. Reconcile each exact
title: duplicates or unexpected query/fields/formatter are a drift stop. Create
only missing views using `/views/add` and the generated `create` body; set the
new view's CustomFormatter from its `formatter` body. Do not overwrite an unknown
existing view. Use a single-attempt transport and disable redirects for mutations;
a timeout/uncertain result requires GET reconciliation before another write.

Read back query, fields, formatter, paging, row limit and non-default status.
Repeat reconciliation must create nothing. Compare existing views and case records
before/after. There are no item, source, schema, permission, notification or default
view changes. Recovery is selection of the preserved default/existing view;
remove only the exact newly created view IDs if removal is subsequently needed.

## Evidence on 18 October 2026

The qualified same-client CLI transport saved all three views, verified exact
query/field order/formatter and non-default status, then repeated with no creation.
Case snapshots and existing views matched before/after. Current case-list rule and
subscription enumeration returned zero each. Current field and exact-target
permission reads succeeded. No new licence, consent, connection or application
was introduced. The implementation uses existing SharePoint Lists presentation.

Detailed native bindings, receipts and the single-attempt deployment adapter are
retained privately at `.local/review-followup/20261018/`. No clinical content or
operational binding is included in the versioned bundle.

The original BrowserOS check reached organisation sign-in. No browser or new login
was used during revalidation. The selected configuration implementation is complete;
visual rendering, filtered-link behaviour and ordinary-user usability remain open
acceptance checks. These do not block independent development. API readback is not
visual acceptance, and no measured benefit or accepted workload is inferred.

## CLI revalidation — 18 October 2026

A fresh qualified CLI export contains all three expected views among nine existing
views and 94 fields. Reusable readback verification checks exact fields/order,
query semantics, formatter, paging/row limit and public/non-default status:

```sh
.venv/bin/python scripts/ppg_followup_views.py \
  --bindings .local/review-followup/bindings.json \
  --fields .local/review-followup/fields.json \
  --verify-readback .local/review-followup/views.json
```

Export the views with their expanded ViewFields through the existing qualified
CLI route. Keep actual bindings/exports private. Verification does no network
access or writes and refuses missing, duplicate or changed views. Input binding
validation rejects protocol-relative/external paths, backslashes and controls.

CLI GETs also verified that the case form, readiness and assurance pages and
three saved view pages exist. This is target-existence proof, not a browser/link
interaction or ordinary-user-access check. There were no native mutations in this
pass. Eight follow-up and fourteen workspace tests passed. Private receipts:
`.local/review-followup/revalidation-20261018/`.
