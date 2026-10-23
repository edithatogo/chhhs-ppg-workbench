# Recover standards registers into separate targets

Recover the five known registers together: framework editions, requirements,
PPG mappings, requirement crosswalks and document relationships. Keep stable
business keys and working bindings intact. A recovery copy does not accept a
mapping, create a current obligation or authorise policy publication.

## Preserve and plan

Use the existing qualified CLI account/site. Export all current items, every
available version, field XML/definitions, list version settings and nonhidden
view definitions/field order. Account for empty registers too. Refuse partial
inventories or attachments needing separate preservation. Preserve original
platform IDs, GUIDs, authors, timestamps and version labels in the backup.
Upload/download the backup and verify its bytes, CRC and every member hash before
planning from those downloaded bytes.

Run the read-only planner from the repository root using private paths:

```sh
.venv/bin/python -m scripts.ppg_standards_recovery \
  --input .local/recovery/source-export.json \
  --output .local/recovery/new-standards-plan.json
```

The planner requires the five known schemas and matching source/export identity.
It checks native field bindings, types, required/unique flags, choice/default
values and plain notes; additional list-owned fields need explicit mapping.
Missing originals, gapped histories, changed stable keys, latest-state drift,
unsupported values and paged results are refused. Existing output is never
replaced. It reuses the tested record-history planner; role-planner defaults and
its existing CLI remain unchanged. There is no native writer in either planner.

## Reconstruct and reconcile

Use separate, clearly named recovery Lists. Verify versioning, known field
contracts and different list identities before inserting data. Set NoCrawl=true
and OnQuickLaunch=false first. Verify inherited site/list/item access matches the
qualified scope; this is not permission restoration or a new access grant.
Never swap production bindings or recreate populated working Lists as part of
qualification.

Create each stable key from its original business payload and replay later
available versions in order with exact ETags. Read back every field/version.
Preserve original platform provenance separately; new platform identities and
audit stamps belong to recovery and must not impersonate original actors.
Existing copied rows/history must match exactly; changed or extra records require
reconciliation, never resetting to original seeds. Disable mutation retries and
redirects; after uncertain responses inspect actual keys/history before another
send. Retain first-run and replay journals separately.

Restore field order, queries, row limits, paging and default views. Nonempty
custom formatters need separate qualification. Compare all business values and
available versions, validate copied standards references and compare version-bound
relationship contexts. Empty crosswalks must stay empty; proposals remain
proposals. Replay must create/update zero records and change zero views/settings.
Fresh full working-source exports must prove that original records, schemas,
histories and exported views remain unchanged.

## Qualified snapshot and limits

The20 October exercise restores180 records/180 available major versions in five
separate Lists with37 known custom fields and11 views. Six custom views are
created. All copied values, source keys and versions match; all180 copied GUIDs
are new. Record replay creates/updates zero; view/settings replay changes zero.
Both original and recovered standards references validate, and nine relationship
contexts match. Original source exports compare unchanged. Source/target Lists
and all180 items inherit the same web access; no ACL changes occur.

Retain exact targets, mappings, source archive, first/replay and schema/access
proofs in the private standards-recovery evidence supplement. Original backup
pins remain frozen; the later stricter schema check produces the identical plan.
Current-code CLI refuses an existing output without altering it. Twenty focused
recovery/action/contract tests pass.

This proves copied recovery of this snapshot. It does not prove full disaster
recovery, evicted history, attachments, forms/formatters, retention policies,
permission migration, production cutover, ordinary-user acceptance or clinical
applicability. All mappings/relationships remain Proposed; both framework editions
remain distinct. Preserve frozen workflow releases: record restoration does not
change the existing review/acceptance workflow.

The downloaded qualification evidence archive verifies34 members. Keep the
original backup nested inside it so original planner/schema pins remain available
alongside the later stricter compatible checker.
