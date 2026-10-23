# Out-of-session review annotations

The integration-owned **PPG Review Annotations** List accepts suggestions independently of a current review. Open its **Unresolved review suggestions** view. Enter a short Title, the catalogue Document UID, the exact document version, a section identifier where available, suggestion text and evidence links. Author/time are captured by SharePoint. An optional unique Annotation key supports integrations; manual users can rely on the native item ID.

Suggestions start Received. Triaged, Deferred and Accepted remain unresolved until incorporated or otherwise disposed of. Rejected, Incorporated and Superseded are excluded from the unresolved view, not deleted. Record decision rationale and the incorporated document version when relevant. These states are suggestion dispositions, never policy approval, publication or a responsibility transfer.

Suggestion text, evidence and rationale use append-only notes; version history retains the original and later additions. Read original wording from the initial version, not the latest note value alone. Current native history limit is50 versions; long-term retention/export remains an open records-continuity requirement. Administrators can manage history: this is not an immutable compliance archive or a permission boundary.

## Technical qualification — 18 October 2026

Created one new List with versioning and nine custom fields. Actual internal field names differed from requested names: the field adapter resolves by StaticName and validates type/required status. Do not recreate fields based on guessed internal names. Field setup timed out at the browser transport; readback reconciled all nine saved fields before any retry. The original missing-field lookup400 was replaced by field enumeration.

A labelled fictional annotation was created, updated to Triaged with an added note/rationale, and read back across versions1.0/2.0. Exact original and added text were verified. Stale ETag update returned412; duplicate key returned the explicit SharePoint duplicate-values error (HTTP500) and count remained one. The unresolved view's query/fields were read back and its fictional row/status/add-item entry rendered under the current account. No real policy suggestion or decision was created, no ACL change or send was performed.

Native binding and receipts are private. config/review-annotations.json is the portable field contract. scripts/ppg_annotation_adapter.py resolves native names and normalises original history into the local carry-forward contract. It does not claim a deployed automatic review-pack trigger. Changed document versions/sections require reconciliation before incorporation.

## Recovery and remaining work

Before retrying creation, query the unique integration key and compare payload/history. Before changing a record, read and use its exact ETag. A transport timeout does not prove failure. Preserve drift for review; never overwrite it. Export all required versions before any retention change; do not delete the fictional fixture during concurrent qualification.

Ordinary-user access, mandatory rationale enforcement, long-term retention and automatic review-pack triggering remain open. Manual export and pack integration are qualified in the dated increments below. No reminders, subscriptions or AI processing were enabled. Use the manual register while those integrations are implemented.

## Passage-findings integration — 19 October 2026

Three historical draft suggestions now use the live register. Each explicitly
identifies assistant authorship, historical inspection scope, proposed action,
effort, dependencies and uncertainty. The version field binds the inspected
content hash; the section field is a version-specific locator, not a claimed
stable section. Current-edition reconciliation is required. No rationale,
incorporation version or human decision is supplied by this integration.

`scripts/ppg_findings_annotations.py` revalidates source bytes and quotations before
preparing insertion payloads. Run `.venv/bin/python -m scripts.ppg_findings_annotations`
with `--pack`, `--inventory`, `--source`, `--pack-reference` and a new `--output`
file. This CLI prepares private payloads; it does not itself write to SharePoint.
Qualified native insertion resolves actual internal fields, verifies the unique
key/versioning/append-only contract, and checks first-version wording/evidence.
The stable key binds document identity, inspected bytes and finding identity.
Replay never appends duplicate notes or resets a human's current review state.
Identity or original-contribution drift stops the operation for reconciliation.

Native creation/readback verified all three originals; replay created zero.
Complete four-item histories, including the unchanged fictional proof, were
exported. The successor pack carries only the three relevant unresolved records,
all flagged for reconciliation, with native author/time and additions preserved.
It also includes the proposed standards mappings and complete catalogue accounting.
Pack storage/readback/replay has separate private receipts. Native AI, automatic
scheduling, human triage, ordinary-user acceptance and current-V7 applicability
are not established by this technical integration.

Recovery retains the source archive, immutable original pack, exact payloads,
unique keys, native item IDs and complete history export. Reconcile uncertain
creation by key before retrying. Preserve current human dispositions and notes;
never recreate a changed record to force an expected result. This increment adds
no notification action and does not alter the upstream catalogue.


## Historical state and binding context —20October

The normalised export now preserves each version's review state, document UID and
version, section locator, incorporated version, native Author/Editor objects and
Modified timestamp. This accompanies the existing original wording, additions,
evidence, rationale and timestamp. The native Editor is recorded platform provenance,
not proof of clinical authority or the identity of every person quoted in a note.

Historical context is taken from that version, never from today's row. Missing
fields in older/partial evidence are listed in `missingHistoryFields`, with null
values retained as unknowns. A present invalid state, ambiguous field or duplicate
version identity stops normalisation. No missing rationale or incorporation value
is invented. These checks do not enforce native form transitions or extend retention.

Fresh read-only CLI export16 records/18 history versions contains every added field;
all prior contribution fields remain identical. Full native before/after exports
are unchanged.26 related tests pass, including changed section/version/actor/status,
missing actor, invalid historical state and duplicate version rejection. Earlier
packs retain their original bytes; future assemblies use the enriched adapter.

Four companion files read back with inherited access and replay creates0. The
same-named `annotation-history-context-v1` private/native companion contains the
normalised history and a seven-member recovery archive. Validate CRC/all member
hashes, extract separately and call archived `annotations_from_export` on the saved
native export. Isolated replay reproduces the result and unchanged older fields.
Do not import snapshots as new annotations or overwrite human dispositions. Actor
records and tenant bindings remain private. Frozen workflow1.5.1 is preserved:
no operational transition, clinical decision, permission or notification changed.


## Assisted disposition preparation — qualification

Use `.venv/bin/python -m scripts.ppg_annotation_disposition` with private `--input`
complete annotation/history export, `--item-id`, explicit `--target`, `--rationale`,
a fresh UUID `--operation-id` and a new `--output` path. Incorporated additionally
requires `--incorporated-version`. The CLI prepares a patch; it performs no native
write and makes no substantive decision. Only state, rationale and, when applicable,
incorporated-version fields can appear in the patch. Originals/bindings stay unchanged.

The selected input item must contain its exact native ETag (`__metadata.etag` or
an OData etag property); ordinary no-metadata exports omit it and are refused.
Read the exact item using the existing qualified verbose native route and reconcile
identity/version/section with the complete history export. Before applying a patch,
re-read the item, match those fields and ETag, and use exact IF-MATCH. Never replace
it with `*`. On timeout, reconcile native history before retrying. An observed
operation marker with identical contents returns already_recorded, without resetting
any later human state. Reused operation identity with different contents refuses.

One new labelled fictional fixture demonstrates Received->Incorporated with explicit
technical rationale/fictional version, two preserved versions, stale412 and replay0.
All16 earlier annotations/18 histories are unchanged.28 related tests pass. This is
assisted-route qualification; native forms still permit incomplete dispositions,
there is no deployed trigger/general writer or clinical incorporation, and operator
rationale/authority checks remain required. Broader promotion needs a workflow-guide
successor; frozen1.5.1 and existing packs remain unchanged.

Five companion files verify native bytes/identity/version/inherited access and replay0.
The13-member recovery archive reproduces prepared/replay outputs using archived code,
and history-aware original/source checks. READBACK-CLARIFICATION.md preserves a raw
false latest-note diagnostic: append-only current suggestion is empty after a
rationale-only update, while original1.0 is intact. Do not use latest note equality
as a preservation test. Recover privately into a separate directory; never apply
archived ETags/patches to live records or re-create a fixture to repair evidence.
Private/native companion: annotation-disposition-v1. Actor records/IDs remain outside Git.
