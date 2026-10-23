# Freshness and capability status clarity

Selected by the user on 17 October 2026 as an existing-permissions usability increment.

## Outcome

Make the existing quiet status surface explain what data can be relied on and
which capabilities can actually be used. This is a presentation increment over
existing receipts/checkpoints and the workspace manifest, not a second monitor.

## Deliverables

- Clearly distinguish last source check, last successful reconciliation, current
  identity hold, and the as-of time of the status projection.
- Show operational, manual, pilot/Off, conditional and unavailable capability modes
  using existing manifest facts and dated evidence. A completed fictional pilot
  does not become a live production service. Unknown evidence stays unknown.
- Explain a hold in plain language with a link to the delivered resolution path;
  preserve unknown/failed/stale states and existing freshness rules. A recent poll
  must never make an older successful checkpoint appear fresh or clear a hold.
- Reuse existing status row, views, page controls and flow. First inspect current
  fields: prefer labels/formatting over runtime changes. If a missing datum needs
  a status projection change, retain its sole writer and separately verify that
  exact existing flow operation before altering it. No importer edits.

## Acceptance

Demonstrate healthy, identity-held, failed, stale, unknown, manual and pilot/Off
presentations with existing proof or local fixtures. Verify time zone labels and
missing/future/inconsistent timestamp handling. Read back displayed native values
against their source receipts. A static fallback carries an explicit as-of date;
it cannot claim live freshness. No new schedule, notification or source/case write.
Repeat application preserves native identity, cadence and unrelated controls.

## Fallbacks

If status-flow access is unavailable, improve labels/help text using existing
fields and link a dated explanation; leave runtime unchanged. If evidence cannot
be read, display unavailable/unknown and the last-known date rather than healthy.
Production licence eligibility is not inferred from UI access or a developer run.

## Existing-permissions execution contract

Use [the shared permission and delivery contract](../../../docs/usability-delivery-plan.md).
Before a native change, read the exact existing target with the intended account,
record the available operation and preimage privately, and confirm its writer.
Recorded historical access is a starting point, not current operation proof.
Use only existing site/List/library rights and qualified clients. No tenant admin,
new consent/app registration, licence purchase/assignment, access changes, premium
runtime, new site, schedule or notification is required or authorised.
An unavailable operation takes its documented fallback; record the limitation and
continue independent tasks. Never call a fallback the unavailable native feature.
Preserve source fields, case decisions, original files, version history, unrelated
controls/views and inherited permissions. Native save/readback and repeat safety
are separate from local checks. No new deployment is claimed by this plan.
