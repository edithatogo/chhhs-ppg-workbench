# Versioned review criteria and decision options

The native **PPG Review Criteria** register contains the eight commissioned review
questions, applicability, evidence needed, authority basis and response options.
The separate **PPG Review Decision Options** register contains eleven possible
human dispositions. Both use versioned unique keys and native version history.
Their default views show the definition version and draft status.

These are advisory pilot definitions, not policy approvals or mandatory rules.
The earlier frozen kit remains unchanged. Review runs must retain the criteria
version and definition hash; the human response and decision belong to the review
record, not to the definition register. Document lifecycle, review progress,
approval, publication, ownership and suggestion states remain separate.

## Prepare and reconcile definitions

```sh
.venv/bin/python scripts/ppg_review_criteria.py \
  config/review-intelligence/criteria-v1.json \
  .local/review-intelligence/new-criteria-seeds.json
```

The command creates a new seed file and never writes to Microsoft 365. The schema
is `config/review-criteria-registers.json`; existing register provisioning and
create-only seed helpers are under `tools/review-intelligence/`. Apply actual
StaticName-to-InternalName bindings from native readback before seeding. The CLI
connection can perform these operations through its existing authenticated request
transport; no new connector, licence, consent or browser login is required for the
verified target. Installation alone does not qualify a different target.

Identical seeds are a no-op. A changed same-key definition must stop on exact
readback differences, preserving human edits. Deliberate revisions get a new
criteria version and new versioned keys; preserve old definitions and the frozen
kit. Native forms do not make definitions immutable: retain exported snapshots and
hashes and reconcile direct edits before subsequent runs. Do not promote mandatory
rules through this advisory seed route. Verify local rule authority and scope first.

## Evidence and recovery

On 19 October, the existing CLI connection created/read back two versioned Lists,
15 custom fields and19 definition records. Replay created zero rows; independent
reads matched all generated definition values and verified both default views and
visible columns. Actual field bindings, IDs and receipts are in private deployment
configuration and the dated private evidence directory. No human decisions,
clinical approval, upstream changes, notifications or permission changes occurred.

Export both Lists with their history, versioned keys and definition hashes before
recovery. Recover into a separate qualified target and compare every field to the
retained definitions before repointing consumers. This is a recovery procedure;
native copied restoration and representative ordinary-user access remain unverified.
Local authority reconciliation and full review-run integration remain open under
RF-08/10. These Lists are SharePoint artefacts outside Power Platform solution
packaging; preserve their schemas and bindings in the ALM inventory.

Retained document-control guidance has now been [passage-mapped to advisory pilot
questions](unassociated-source-review.md). Its version/date/policy-title differences
and missing referenced appendices/current template remain unresolved. Criteria1.0.0
and native register versions are preserved; no mandatory flag, approval gate or review
interval changes. Confirm current authority and applicability before any successor
rule definition is proposed.

The retained governing policy now provides further passage-backed document-type,
metadata, role, consultation and implementation evidence. Its review-cycle wording
differs from the retained guideline. Preserve both as unresolved applicability/current-
authority questions; criteria1.0.0/native definitions and due dates remain unchanged.
See [source-only policy companion](unassociated-source-review.md).

## 21 October advisory acceptance

Fresh native schema/items/history/view export verifies all19 records against exact
seed definitions:8 criteria,11 options,19 versions/four views. Five evidence files
read back/replay0; downloaded10-member CRC/hash archive reproduces the comparison
using archived code. RF-08's advisory register deliverable is complete. No mandatory
authority, production prompt approval or substantive human disposition is inferred.
Current-source reconciliation remains explicit before enabling mandatory rules.
See review-criteria-acceptance.md and surveillance-schedule-eligibility.md for the
separate scheduling assessment; no native schedule was created.
