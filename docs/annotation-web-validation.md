# Native web annotation validation — qualification

The web route uses the existing Microsoft Lists form. The proposed additive
Disposition summary is single-line text (255 characters); version history records
its prior values. The existing append-only Decision rationale remains for detailed
discussion. No old rationale, source binding or suggestion is converted or replaced.

The portable contract is config/review-annotation-web-validation.json. Native
list validation permits Received without a summary. Every other suggestion state
requires a nonblank summary, and Incorporated also requires an incorporation
version. This validates presence, not evidence quality, reviewer authority or
clinical approval. Existing rows are not silently backfilled with invented reasons.

Microsoft documents the supported formula types, including single-line text and
choice; multiline notes are excluded. See [formula types](https://support.microsoft.com/en-US/SharePoint/libraries/introduction-to-sharepoint-formulas-and-functions)
and [list validation](https://support.microsoft.com/en-us/sharepoint/lists/data-and-lists/edit-list-settings).
Actual target qualification is required in addition to that documentation.

## Observed 21 October

A separate fictional SharePoint qualification List has the existing annotation
shape plus the summary field, versioning and list validation. Native cases prove:
Received creation without a summary; missing/whitespace Triaged summary refusal;
Accepted with summary save; Incorporated without version refusal; Incorporated
with summary/version save. Three saved versions preserve the original suggestion.
Rejected writes preserve ETag and every stored field. Native validation failures
return HTTP500 with SPListDataValidationException; generic server errors must not
be treated as validation success.

An initial preservation diagnostic compared a per-response metadata identifier
and failed. Private before/after evidence shows only that response identifier
changed. The corrected comparison excludes only __metadata.id and retains ETag,
item GUID, stored fields and version checks. Original failed diagnostics remain.

The successor qualification now includes browser refusal and successful save,
verified natively as version4.0 with original1.0 preserved. The browser requires a
new Suggestion and additions entry on edit because that append-only field is
required; add a meaningful transition note rather than copying the original.
The working register now has the additive field and exact validated rule. Its17
records/20 histories and item ETags remain unchanged; no item writes were made.
The summary field is visible in its current-account native edit form. Broader
ordinary-user use and workflow-guide successor remain separate.
The history adapter now retains optional current/historical summaries without
inventing values for versions predating the field; legacy exports remain valid.
Twelve annotation/disposition/pack tests pass. The preparation CLI accepts an
explicit --summary for the new binding and never truncates a detailed rationale.
When omitted, a rationale up to255 characters supplies the summary; longer reasons
require an explicit short summary. Older bindings/operation histories remain valid.

## Remaining implementation and recovery

Browser saving and live schema deployment are verified at the scopes above.
Publish a successor workflow description and native recovery companion before
promoting this as the completed operator route. Developer exports must resolve
DispositionSummary by StaticName and include its actual internal name in binding;
legacy exports do not assert the field exists.
Do not change permissions, notifications, original notes or historical decisions.

Private qualification retains created-list identity, schema/formula bindings,
case preimages/readbacks/refusal bodies and full fixture versions under
20261021/annotation-web-validation-v1. Recovery should first disable only this new
rule if it prevents authorised saving, preserving the summary column and all
history; never delete notes or recreate records. Copied restoration and the live
rule rollback are not qualified yet. Desktop Word is not involved.

## Deployment reconciliation

Exact list ETag guarded the rule save. The first post-save preservation check
flagged volatile deferred history links. Fresh read-only reconciliation against
the saved preimage verifies all stored fields, item ETags and20 histories; only
per-response metadata and deferred navigation references are excluded. Original
failed diagnostics remain private. No original text, actor, status, document
binding or timestamp was ignored. Replay performs no schema or item writes.
The existing rule endpoint probe returned404 and is not evidence of zero rules;
no item change or new notification action was made by this deployment.


## Published recovery and workflow

The native annotation-web-validation-v1 companion has README, portable contract,
verification summary and recovery ZIP. Exact native readback/replay creates0.
Downloaded ZIP CRC/all23 member hashes pass; isolated archived-code reproduction
retains17 records/20 histories and prepares a summary-bound exact-ETag patch with
nativeWrites0. Workflow release1.8.0 adds the web disposition diagram and recovery
navigation; frozen1.7.0 remains preserved. These close the documented manual route,
not native rollback/copy restoration, ordinary-user adoption or clinical authority.
