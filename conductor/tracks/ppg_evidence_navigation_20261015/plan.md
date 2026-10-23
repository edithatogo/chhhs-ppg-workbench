# Evidence finder and archive navigation — executable plan

Read ../../workflow.md and this track’s spec/metadata before execution. Implementation selected by the active user goal. Record local proof, native readback and operational acceptance separately.

- [x] **EN-01 — Baseline the four discovery tasks.**
  - [x] Action: Inspect current hub, views and indices; record navigation/search results and gaps against the four tasks in the spec.
  - [x] Verification: Reuse successful paths; do not repeat the full archive download/hash audit unless bytes have changed.
- [x] **EN-02 — Implement only the navigation gaps.**
  - [x] Action: Add task-oriented Quick Links, minimal derived labels or filtered views using existing metadata. Preserve CMO relevance as navigation only.
  - [x] Verification: Canonical resource references and original bytes remain unchanged; unsupported search formats have an honest fallback.
- [x] **EN-03 — Verify native tasks and repeat safety.**
  - [x] Action: Open all four paths in Teams web/SharePoint; verify existing view counts and labels and rerun provisioning. Attempt desktop only if capture works.
  - [x] Verification: No duplicate navigation, access changes or altered originals; record desktop gaps separately.
- [x] **EN-04 — Hand off and register.**
  - [x] Action: Update manifest navigation if required, operator guidance, private receipts and sanitised handoff; commit the bounded increment.
  - [x] Verification: Report discovery outcomes and remaining coverage gaps; no authority or measured-saving claim.

## Current verification evidence

Hub version 9.0 is published with four task links. Teams web renders the four
paths; SharePoint policy preview, source-sync view and actual template/example/
index downloads passed. All 533 index rows match preserved provenance; archive
views remain 533 all / 178 CMO relevance. The source-sync view includes checkpoint
evidence. A second native save/publish adopts the same view/control identities
with no duplicate tasks, controls or views. Existing inheritance/versioning remain;
no original archive writes, new tabs or announcements. Hosted manifest readback
matches the registered live capability. PDF search succeeded; one known Office
capture had zero exact search results, with the explicit CSV fallback verified.
Desktop capture failed with ScreenCaptureKit -3811 and remains unverified.
Private receipts: `.local/evidence-navigation/`. No content authority or measured
saving is inferred. Local contract/setup checks and bounded commit complete EN-04.

## Revalidation — 16 October 2026

Published hub 12.0 retains the four reachable paths and exactly one task/guidance
control. Exact archive view membership remains 533 all / 178 CMO; index provenance
rows and template/example/index hashes match. Checkpoint is visible, manifest is
live, inheritance/versioning preserved. No further implementation was needed;
previous repeat-save and Teams web/search proof was retained. Private dated audit
is `.local/evidence-navigation/reaudit-20261016.json`. Desktop remains unverified.
