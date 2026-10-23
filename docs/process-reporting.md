# Portfolio and recorded process measures

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Use the existing **Start Here** tab in **Policy (PPG) Management**, then **Portfolio
and process measures**. The three native views read current List rows. The HTML,
JSON and CSV measures files are dated manual snapshots; check their captured
as-of time before use. Download the tool ZIP to repeat a snapshot locally.

This answers where recorded cases sit, what follow-up information is missing,
and what elapsed calendar time the existing evidence supports. It complements
the monthly source-policy due/overdue report without changing that report or its
schedule. Recorded roles may be proposals with acceptance/capacity pending; they
are not assigned workloads. All cases are included because the free-text status
field does not define a reliable terminal-state contract.

## Live views

- **Portfolio by recorded status** groups the Review Queue by its recorded text.
- **Oldest recorded cases and follow-up** orders case creation dates and displays
  recorded role statements, next actions and target text. Age since creation is
  not stage turnaround or active working time.
- **Process stage history by case** groups assurance rows by CaseUID and displays
  stage, date, state, exact version, parent link and evidence. Fictional test rows
  are excluded. Empty history means no recorded history, not completion.

These views retain existing access and editing rights. The setup does not update
items, grant access, set a default view or notify anyone. A view is navigation,
not a new security boundary or an assurance that a user cannot edit the List.

## Definitions and missing evidence

The versioned dictionary is `config/process-measures.json`, also downloadable
from Start Here. Counts include recorded cases, missing role/next-action text,
unconfirmed targets, qualified past-target dates, age and evidence coverage.
A nonblank role statement is not proof that someone accepted a role. Blank or
non-ISO target text remains unconfirmed. Only exact valid `YYYY-MM-DD` targets
enter the past-target denominator; a pending statement is never an overdue date.

Stage timing uses three explicit relationships: readiness-to-decision,
decision-to-publication, and implementation-to-verification. Each endpoint must
be a validated recorded assertion with an actual event date, linked by
ReadinessEventUID or ParentEventUID to the same case, document, version and hash.
A readiness endpoint must say Ready for decision. Pending, not-applicable,
invalid, future, negative, ambiguous and mismatched-version pairs are excluded
with reasons. No Created date replaces a missing event date.

Results give sample count, distinct case count and median calendar days. Multiple
explicit pairs for one case are multiple samples, not a deduplicated case cycle.
Dates use Australia/Brisbane calendar days; no working-time, SLA or causal claim
is made. A same-day qualified pair can correctly be zero days; zero eligible pairs
must display **Not measurable**, never zero days. A recorded verification event
can report Failed or Inconclusive; elapsed time does not imply success.

Counts describe the current event rows, including retained repeated assertions.
They are not a reconstruction of every SharePoint item version or historical
portfolio trend. Native version history remains available on the existing Lists.
No time saving, throughput trend, content review, current-policy status or clinical
approval is inferred. Unknown source freshness is separate and never becomes green
because process data were successfully read. Consultation/handoff events can be
considered individually later with explicit definitions; they are not silently
added to this cohort or treated as equivalent to readiness/approval.

## Capture and repeat

`tools/process-reporting/native.js` reads all pages of the three existing Lists,
checks item counts, uses uncached reads and repeats metadata/items before accepting
the export. Capture stops on a changed/incomplete source. This is a guarded
read window, not a transactional multi-List snapshot. Keep real exports, IDs,
source details and deployment receipts in ignored `.local/process-reporting/`.
Do not put them in Git or use a smaller subset as a complete portfolio.

Run Python 3.11+ (standard library only):

```sh
python3 scripts/ppg_process_measures.py \
  --input templates/process-reporting/input.json \
  --output .local/process-reporting/example-1
```

The bundled example is explicitly fictional, including its output banner and
CSV datasetKind. Operational capture defaults to operational and excludes
fictional flags/case IDs. Never mix a fictional example into operational results.
The tool validates duplicate/nonblank identities, complete export accounting,
existing readiness/assurance rules and explicit stage links. HTML escapes source
text; CSV contains fixed measure keys and numeric values, avoiding formula-valued
source text. Input files are never modified. Output directories must be new;
existing reports and human edits are never overwritten.

For operational use, pass the complete native export instead. Inspect exclusions,
source context, sample sizes and dates before hosting a new uniquely named report.
Retain previous snapshots and update only the managed Start Here block. Use the
existing evidence-library access and workspace deployment route. Local generation
is manual, not an executable Teams button or a new scheduled flow. Downloadable
HTML is a technical projection; it performs no case or source writes.

## Microsoft route and scope

SharePoint structured document generation was evaluated first. Its maintained
Word-template/form route remains the preference for a later formal business-report
shape, subject to actual entitlement and output qualification. Here the deliverable
is live List views and a technical data projection. No new Word generator, licence,
Power BI model/capacity, approval flow or runtime is needed. Existing working
monthly outputs and in-flight document-pilot work remain intact.

References: [SharePoint structured document generation](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation)
and [native CAML grouping](https://learn.microsoft.com/en-us/sharepoint/dev/schema/groupby-element-query).

## Verification

The track plan records native schemas/views, query/readback, real input accounting,
actual downloaded-tool execution, Teams web navigation, repeat adoption and
preserved original items. Local tests separately cover linked and unlinked
endpoints, empty history, date/timezone boundaries, changed versions, pending/not
applicable states, invalid parents, duplicate/partial exports, fictional isolation
and escaped source text. Teams desktop acceptance was closed by the user on
17 October 2026; the earlier capture failure remains historical evidence, not
automated desktop inspection.

## Matched task observation kit — 18 October 2026

The same command now accepts `--observations` instead of `--input` for the existing
operator CSV. This adds hands-on/wait/count arithmetic and strictly matched
baseline/workbench task comparisons without changing portfolio or event measures.
Use the [maintained observation guide](operator-usability-observation.md) and
`config/observation-measures.json`. Blank/fictional observations do not establish
real benefit. Output is private CSV/JSON instrumentation, not a new dashboard,
report generator, schedule or clinical decision path.
