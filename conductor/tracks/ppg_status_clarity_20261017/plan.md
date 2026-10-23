# Implementation plan

- [x] US-01 Inventory status fields, receipt/checkpoint inputs and capability modes; confirm target rights and existing object writer.
- [x] US-02 Define plain-language labels, timestamp meanings and action links using existing status semantics and manifest.
- [x] US-03 Implement presentation changes; change the existing status projection only if necessary and exact access is verified, otherwise use dated fallback.
- [x] US-04 Check healthy/held/failed/stale/unknown and manual/pilot examples; read back timestamps and confirm unchanged source, decisions and cadence.
- [x] US-05 Reapply without duplicate rows/controls; update operator explanation, private receipts and Conductor and commit.

Native operations are conditional on exact-target access. Record a supported fallback
and its limitations when necessary; never mark the unavailable operation verified.


## US-01/US-02 preparation handoff — 17 October 2026
Frozen mapping: `config/status-clarity.json` v1.0.0; explanation:
`docs/status-clarity.md`. Five existing CLI GET operations succeeded: status schema,
adopted status item, source-state, last-success checkpoint and linked latest attempt.
All11 status field names/types and four action resource references match; thresholds
match the existing manifest and projection builder. No native mutation or auth change.
Native writes remain with Workbench after Guided Workspace; only read access is
qualified here. US-03–05 and healthy/held/failed/stale/unknown/manual/pilot native
presentation/repeat acceptance remain incomplete. Local future-ProjectedAt guard gap
and failure-branch baseline-unavailable behavior are explicitly handed over.

## Native acceptance — 17 October 2026

This supersedes the historical preparation gaps above. US-03–05 are complete.

- Existing CLI session expired with AADSTS70043 before writes. User completed
  browser sign-in; intended account, exact status target and existing inherited
  rights were verified through that same browser. No shared credential transfer,
  new consent, permissions or licence changes.
- Existing status view/ID and one adopted status row retained. Two already-existing
  version fields added only to view selection. Field types, requiredness and global
  formatters unchanged; no status-row, source, case, importer or flow writes.
- Native held state, retained reason, independent freshness and three explicit
  AEST clocks render in the List and embedded Start Here. UTC readback matches the
  formatted last check, last-success baseline and projection time. Background
  projection advanced normally; old verified baseline/count remained unchanged.
- Nested-loop clock variants did not render on this route; the qualified shallow
  epoch-arithmetic layout replaces them. No browser-local date getter or assumed
  extra offset is used. Four focused tests include ten generated-expression
  fixtures for healthy/held/failed/stale/unknown, future/invalid/missing clocks,
  30/90-minute boundaries, version mismatch, leap date and year rollover. These
  fixtures are local proof, not fabricated live status rows.
- Published Start Here27.0 updates two owned status/capability controls; fourteen
  unrelated identified controls and the non-control record remain exact,17total.
  Guided workspace/OU guide routes and the existing status web part are retained.
  Actual native table shows interactive/manual/pilot-Off/conditional/unavailable
  route meanings with dated qualification and explicit runtime unknowns.
- Three Autofill prompt Off states freshly read. Word/package Off observations
  remain explicitly dated qualification, not a new runtime-state claim.
- Native guidev1 and final mappingv1.2 uploaded exclusively and downloaded exactly;
  actual hub link opens the rendered guide. Earlier mappingv1.1 is preserved as
  the qualification-stage record. Additive native manifest registration preserves
  every unrelated record and the existing15/30/90-minute policy.
- Repeated view hash/page/manifest/file pins/readback unchanged; no duplicate view,
  status row, flow, schedule, notification, tab or permission change. Original
  case5.0 and checkpoint exact. Existing flow remains the sole status-row writer.

Private audit: `.local/usability/us/native-20261017/completion-audit.json`.
Native proof covers the actual held display; other states are meaningful local
fixtures under the specification's acceptance rule. No independent-user access,
substantive review, policy approval or automated desktop proof is claimed.
