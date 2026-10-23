# Status clarity — reconciliation, freshness and execution modes

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Use the existing Start Here status card. It separates the recorded reconciliation
state, freshness of the display, and the three underlying clocks. Refresh the page
to re-evaluate freshness; doing so does not reconcile source data or resolve a hold.

## Read the clocks separately

| Label | Meaning |
|---|---|
| Last source check | Source inspected; no successful import is implied. |
| Latest reconciliation attempt | Recorded attempt outcome; metadata polling is different. |
| Last verified reconciliation | Readback-verified baseline time; it is never replaced by a later check/display time. |
| Status display updated | Presentation row refreshed; this does not freshen its baseline. |

The three dates display explicitly as **AEST (UTC+10), Australia/Brisbane**. Receipt
values remain UTC. Date conversion uses epoch arithmetic, not browser-local date
formatting plus an assumed offset. Missing/invalid dates show unavailable; neither
today nor a guessed baseline is inserted. The verified-record count belongs to the
last baseline, not necessarily the current source.

## State, freshness and next action

- Source matches the last verified reconciliation: valid recent evidence and matching
  observed/committed versions support the healthy label.
- Source change detected—reconciliation held: keep the last verified baseline and
  follow the identity-resolution guide. A successful poll does not resolve identity.
- Latest reconciliation failed or remains unverified: keep the last verified
  baseline and inspect the same attempt before retrying.
- Reconciliation state cannot be confirmed: evidence is missing, invalid, future,
  inconsistent, unavailable or cannot support a healthy claim. Inspect existing evidence.

Display freshness is separate. **Strictly older than30minutes** is stale; exactly
30minutes is not stale. Missing/invalid/future display time is unknown. The retained
recorded state and reason remain visible even when freshness is stale/unknown.
A source check **strictly older than90minutes** prevents a healthy claim; it does
not erase an explicit recorded hold/failure. Future clocks or clocks newer than
the projection cannot support a confirmed state. The card provides the existing
identity guide and evidence links; it does not create a new decision path.

The existing presentation refresh remains15minutes. This increment changes only
view/page presentation. It creates no status row, flow, schedule or notification
and does not change the importer. The local `display_status` reference's future/
non-string timestamp guard was repaired in `e0a30cb`; native formatting is
qualified separately from that local reference.

If the existing projection fails to read/parse receipts, its established failure
branch clears the baseline presentation fields. The card then shows unavailable,
not an invented retained date/count. A separately dated earlier receipt can be
inspected through evidence; it does not silently become the current baseline.

## What can actually be used

Start Here shows lifecycle, execution mode and runtime evidence separately:

| Mode | Operator meaning |
|---|---|
| Native interactive | Use the existing Lists/forms and evidence links. |
| Manual operator tool | Download and run the documented local tool; a ZIP/link is not a Teams execution button. |
| Configured scheduled automation | Existing cadence/configuration is recorded; inspect actual receipts for recent execution. |
| Pilot / Off | Limited qualification and explicit Off evidence; this is not production adoption. A dated last-Off observation is not a fresh runtime check. |
| Conditional | Required runtime, entitlement, target or acceptance evidence remains open. |
| Unavailable on the checked route | The specific operation/route failed; it is not a tenant-wide availability verdict. Use the supported qualified fallback. |

The Autofill pilot's three prompts are Off on the17October native readback.
Developer Word and unattended packaging retain their dated last-verified Off
qualification; current runtime is not revalidated merely by rendering this page.
Production Word, cited-assistant runtime/evaluation and native Dataverse migration
retain their own gates and owners. Technical status does not establish policy
approval, currency, human readiness or accepted ownership.

The17October CLI expiry (`AADSTS70043`) was a session boundary. The user completed
browser sign-in and the intended account/exact SharePoint targets were qualified
through that existing browser session. No token/cache transfer, new consent,
permission, licence or administrator change was used. This is an operator recovery
example; it does not claim that every client is currently authenticated.

## Maintenance and proof

`config/status-clarity.json` maintains the labels, field meanings and15/30/90-minute
policy. `scripts/ppg_status_clarity.py` prepares the native JSON and a read-only
reference projection. It has no tenant writes. Only two existing version fields
were added to the existing view's field selection; field types/requiredness and
status-row values remain unchanged by this increment. The existing flow remains
the sole status-row writer.

A nested-loop clock candidate did not render on the checked native route. The
maintained shallow arithmetic layout replaces it. Local expression fixtures cover
healthy/held/failed/stale/unknown, invalid/future/missing clocks, exact thresholds,
version mismatch and calendar boundaries. Native current held state, three clocks,
links, page embedding, preserved objects and repeat adoption require separate
readback. No fake healthy status or test row is inserted into the live status list.
Detailed dated receipts remain private in `.local/usability/us/native-20261017/`.

Reference: [Microsoft native formatting syntax](https://learn.microsoft.com/en-us/sharepoint/dev/declarative-customization/formatting-syntax-reference).
