# Monthly due and overdue report

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

QW4 automates report preparation required by the retained Controlled Document
Management Policy v3.1, pp9–10 and Controlled Documents Guideline p12.
The user selected this increment on 15 October 2026; recurrence is documented by
policy, while observed effort savings and business acceptance remain unmeasured.

## Use

In the existing PPG Review Evidence library, open `PPG-monthly-review-YYYY-MM.md`
and its matching CSV in Excel. Due/overdue/date-exception rows are already
selected; filter recorded roles if needed. The native flow runs monthly from 1 November 2026 at
08:00 Brisbane time. An initial current-month report is generated during deployment.
No Python is needed for routine use. A maker can rerun the existing flow; do not
create another flow or send the output automatically.

- Earlier review months are overdue. The current month is due this month.
- The following three calendar months are due soon, inclusive of the third month.
- Missing/malformed review months are date exceptions; later months remain in the
  summary totals, outside the working CSV. Every active source row is accounted for,
  without status exclusions.
- Dates retain YYYY-MM precision. No day or new risk-based review interval is
  inferred. The policy/guideline interval discrepancy does not affect this report.
- Roles, source statuses and comments are imported assertions. Status/extension
  comments can disagree with date classification; no review date is silently changed.
  Recorded roles do not establish current responsibility or a recipient list.

## Integrity and freshness

The report reads the successful sync checkpoint and its named candidate, then
compares all importer-owned catalogue fields and DocumentUIDs with that candidate.
It checks count, unique/nonblank identities, pagination, source/identity hashes and
the matching raw-row projections before joining authorising/operational roles.
The row position is only a verified join within this captured snapshot, never
permanent identity. If the successful checkpoint changes during acquisition, or
any reconciliation check fails, no report is written. Resolve the underlying
source-sync issue through the existing owner; do not extend identities here.

Source metadata that differs from the checkpoint creates a prominent warning:
**last verified catalogue only**. A missing/old metadata check is also flagged.
An unchanged observed version is not a judgement that a policy is operative.
CSV rows retain snapshot hash, last successful reconciliation, report month,
generation timestamp and freshness status. Source references and all raw evidence
are preserved. The CSV automatically selects reportable/date-exception rows and groups recorded roles and protects text against spreadsheet
formula interpretation. Readback must exactly match both generated CSVs before the
summary is written. Repeat runs overwrite the same month's files using existing
library version history; there are no task, case or catalogue creates/updates.

A run failure can leave the previous month's report or the previous successful
version in place. Always check the month and Generated UTC in the CSV, and verify
that the summary timestamp matches. The flow run history is the technical failure
surface. This flow adds no notification or distribution mechanism.

## Maintenance

`scripts/ppg_monthly_report.py` builds a private deployment request from existing
bindings under `.local/`. Default output is `.local/monthly-report/create.json`.
`--manual` creates the temporary qualification trigger; production uses monthly
recurrence with concurrency one. Native flow ID, receipts, report bytes and tenant
bindings remain private. Keep the importer, case state, policy publication route,
permissions and other agents' workspace objects unchanged.

## Channel walkthrough and Mermaid diagram

In Teams, open **Clinical Leadership (CHHHS) → Policy (PPG) Management →
PPG monthly reporting workflow**. If the tab is hidden at the current window
width, open the tab overflow menu (observed as **“6 more tabs”**) and select it.
The visualisation is embedded in that channel’s Loop tab; no separate diagram
application or local server is needed to view it. The existing blank Loop Page tab was adopted and renamed; no
channel post or new permission was created. Its Mermaid code block is saved in
Preview mode, with a six-step operator walkthrough and the human handoff.
Reopening the tab verified both the rendered diagram and all six saved steps.
The editable source is [monthly-reporting-workflow.mmd](monthly-reporting-workflow.mmd).
Native verification is retained privately in `.local/workspace/loop-workflow-receipt.json`.

For maintenance, edit the Mermaid block in the existing Loop page and return it
to Preview mode. Keep the editable source linked above consistent with the saved
diagram, then reopen the channel tab to verify rendering and the six steps. Reuse
this tab rather than creating a duplicate. The diagram explains report preparation
and the human handoff; it does not execute a flow or establish policy approval.
Channel tab presence was rechecked on 15 October 2026; rendering and saved steps
were verified in the earlier reopen receipt. Teams desktop acceptance remains
unverified; these are web checks.

## Retained-absence accounting — 17 October 2026

The committed baseline contains 985 active source rows and two explicitly
acknowledged retained absences: 987 catalogue identities in total. The monthly
flow compares only active records with the current candidate and accounts for
retained records separately. It requires the exact committed ledger, source and
identity contract, matching active alias pairs, unique complete catalogue UIDs,
source-bound acknowledgements and successful unchanged-retention readback.
Unexplained gaps, unknown/duplicate acknowledgements and changed active fields
still stop generation.

The normal summary now links both `PPG-monthly-review-YYYY-MM.csv` and
`PPG-monthly-review-YYYY-MM-retained.csv`. The retained CSV preserves original
recorded source fields and references; the summary retains acknowledgement
evidence. These records do not enter active-source date buckets. Their absence
is not a clinical retirement, current approval or instruction to change a case.
Both saved CSVs must match the generated values before summary publication.

Qualification uses separate filenames so existing monthly outputs remain history.
The independently checked 17 October result contains 270 reportable active rows
(213 overdue, 15 current-month, 42 next-three-month), 715 later active rows and two
retained rows. All source and recorded-role values matched, including retained
fields. The original monthly recurrence and connections are retained; the first
scheduled result remains unobserved until 1 November, 08:00 Brisbane.
