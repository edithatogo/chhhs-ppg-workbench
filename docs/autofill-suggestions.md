# Suggested metadata using Autofill

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

A SharePoint-native **fictional pilot, currently disabled**, is configured and has produced actual
metadata through the existing service. It is separate from the production
workbench evidence library and archive. Find the retained results from **Start Here → Suggested
metadata — fictional pilot**. This is not production adoption or policy review.

## Correction-preserving continuation — 17 October 2026

The three `Suggested*` fields are disposable machine-owned raw output. Native
Autofill can overwrite them on reprocessing. Human corrections now belong in
`ReviewedTopic`, `ReviewedPurpose` and `ReviewedDocumentKind`; those fields have
no Autofill configuration. `ReviewProvenance` and `ReviewOperationId` retain the
version-bound technical review record. No values are promoted to the source
catalogue, identity, authority/currency, readiness or approval fields.

Use **Start Here → Suggested metadata → Raw and reviewed suggestions** to compare
raw output with retained reviewed values. The previous Pilot suggestions view
remains available. Views are navigation, not field-level access control. Use the
guarded apply command for provenance-bound updates; ordinary native form edits
are not claimed to enforce this contract.

The working command uses the existing named Microsoft 365 CLI connection. Retain
bindings, snapshots, values and receipts in private approved storage:

```sh
.venv/bin/python scripts/ppg_autofill_review.py --binding PRIVATE_BINDING.json --output NEW_SNAPSHOT.json snapshot --item EXISTING_ITEM_ID
.venv/bin/python scripts/ppg_autofill_review.py --binding PRIVATE_BINDING.json --output NEW_RECEIPT.json apply --snapshot NEW_SNAPSHOT.json --values REVIEWED_VALUES.json --actor "OPERATOR_LABEL" --operation-id NEW_UUID
```

The values file contains exactly the three `Reviewed*` names. Recording a
fictional qualification operator is not an actual policy review. Production
adoption and substantive review remain unperformed.

Snapshot verifies the exact versioned fictional library, separate field ownership,
native prompt text, item ETag, file identity/version/ETag/bytes/hash, completed
processing and raw suggestions. It rechecks item/file pins after downloading.
Apply revalidates the snapshot and writes only the five reviewed/provenance fields
in one native MERGE with the exact expected item ETag. A stale snapshot is refused;
a competing update can return a native conflict (409) or precondition failure
(412). Do not retry with `*`, omit If-Match or silently recapture and reapply.
Obtain a fresh snapshot and deliberately review the new state instead.

Provenance keeps source identity/version/hash, raw suggestion snapshot, prompt and
review-contract versions, expected item ETag, reviewed values, operator label,
operation UUID and request fingerprint. Repeating the same operation after an
uncertain response verifies the committed record and returns read-only replay;
changing its values or request under the same UUID is refused. Replay confirms a
historical recorded apply, not that later source versions are reviewed. A new
correction uses a fresh snapshot and operation UUID. Existing receipts are never
overwritten. Keep source file history and previous provenance versions.

The original 16 October finding below remains true for corrections made directly
in raw `Suggested*` columns; separate reviewed fields address that ownership gap.
All native prompts remain Off after qualification. No production rollout,
provider/consent/billing/access change, notification or source/case write follows.

## Separation qualification — 17 October 2026

The existing AF01 legacy correction was copied into separate reviewed fields with
its prior raw snapshot/provenance. AF02 then received a distinct fictional reviewed
correction before its unchanged source CSV was re-uploaded. A new classification
timestamp reached Finished and remained stable across three native reads; both
reviewed corrections/provenance survived while raw processing completed. All three
raw prompts were disabled and independently read back Off afterward.

Two simultaneous exact-ETag applies produced one winner and one native409 conflict;
the winner remained intact. An additional old-ETag native MERGE returned412 without
changing it. An older operator snapshot was refused before write. A deliberately
lost local response after one successful native commit recovered through read-only
operation replay; no second write/version was created. The final AF02 correction
was restored through a new explicit operation. All six original file identities,
source byte hashes and earlier versions remain present. Reviewed/provenance fields
have no Autofill configuration. These are fictional technical checks, not human
semantic acceptance or a general production guarantee.

Private detailed receipts: `.local/autofill/separation-20261017/`. Nine focused
review/apply tests supplement the native proof; they do not substitute for it.

## What is available

| Field | Native type | Purpose |
|---|---|---|
| SuggestedTopic | Text, 120 characters | Subject of the explicitly stated purpose, or Unknown |
| SuggestedPurpose | Multiple lines of plain text | Explicit purpose sentence, or Unknown |
| SuggestedDocumentKind | Choice | Policy / Procedure / Guideline / Other / Unknown |

The dedicated pilot library has versioning enabled and inherits the existing
parent-site permissions. It contains six clearly fictional examples and a
**Pilot suggestions** view showing the three suggestions, processing status,
processing time and SharePoint version. No new Teams tab or access grant is needed.
The archive, source catalogue and review cases are not Autofill targets.

`config/autofill-suggestions.json` maintains prompt version **0.3.0** (same extraction prompts as 0.2; disabled after the recovery test). Suggestions
must remain separate from DocumentUID, imported facts, dates, authority/currency,
responsible people, readiness and decisions. No flow promotes these suggestions.
Existing [manual metadata prefilling](metadata-prefilling.md) remains available.

## Original raw-column qualification — 16 October 2026

The first prompt version returned generic fixture titles as subjects and repeated
the missing-purpose sentence instead of Unknown. Those actual outputs were retained.
The revised prompts were saved, read back and exercised on unchanged original bytes.

| Test | Observed result |
|---|---|
| Six fictional CSVs | Finished; supported kinds, meaningful topics and explicit purposes |
| Missing subject/purpose | Unknown in all three columns after prompt refinement |
| Untrusted instruction in DRAFT | Procedure and equipment-check metadata; no approval claim or source-policy action |
| New fictional upload | Automatically processed; correct meeting-room metadata |
| Deliberately unreadable PDF | Failed, no suggestion values; never treated as factual Unknown or successful extraction |
| Corrected topic then re-upload | Late processing overwrote the correction; history/export retained it. All prompts disabled and correction restored. |
| Downloaded original files | All six SHA-256 hashes match the preserved originals |
| Test cleanup | Extra new-upload and unreadable-file fixtures recycled; six examples/history retained |

The temporary v0.2 guide/bundle reported preservation from an early read; that claim
is withdrawn. The final settled read showed overwrite. Use this v0.3 guide and its
Off-state receipts. No safe automatic reprocessing over corrected values is claimed.

These are observed technical pilot checks, including an agent comparison with the
fixed fictional sources. They are not independent human semantic acceptance,
clinical validation, permission trimming for other principals, or proof that every
file type preserves edits. Native confidence remained absent; no score was invented.
The SharePoint version and classification time are distinct from a policy edition.

## Operating the pilot

1. Use only fictional material in the dedicated pilot library. Review the maintained
   field prompts and the exact saved `AutofillInfo` before processing. Do not enable
   prompts in the production evidence library as an eligibility test.
2. Export the selected input bytes/hash, native file ID/version, prompt version,
   raw suggestions and native processing status. New uploads can process
   automatically; a folder does not isolate a library-wide configuration.
3. Review the suggestions against the source. Finished is a processing state,
   not factual adequacy or approval. Keep Failed, pending/no status, unsupported
   content and Unknown distinct. Do not infer a confidence score.
4. Preserve original suggestions, corrected values and native history before
   reprocessing. The correction test showed that late processing can replace a manual edit.
   All three prompts are now disabled; do not re-enable them over corrected values.
   If any correction is lost, stop processing, restore
   from the captured values/history, and qualify recovery before continuing. The
   tested recovery restored the exact corrected topic while retaining source bytes.
5. Retain prior prompt/output revisions. Apply any future updates serially to the existing
   three fields; read back exact prompts/enabled states. Keep the pilot Off unless
   a later bounded run is explicitly commissioned with correction protection. Adopt existing matching
   resources, and stop on drift rather than creating another library or field.
6. Keep human source-review findings and any later production-rollout decision
   separate from this technical pilot. No actual policy-readiness work is performed.

Expected cases and original bytes are in `templates/autofill/`. Detailed receipts,
actual identifiers, raw responses and authentication results stay in `.local/autofill/`.
The [AI evaluation pack](ai-evaluation-pack.md) evaluates cited-evidence responses;
it does not score Autofill output. This pilot uses its own fixed expected cases.

## CLI route and sign-in correction

This feature uses **CLI for Microsoft 365**, not FlowAgent. The maintained
[`spp autofillcolumn set`](https://pnp.github.io/cli-microsoft365/cmd/spp/autofillcolumn/autofillcolumn-set/)
command supports existing library/field IDs, prompts and enabled state. The initial
creation call returned exit 0 with no saved AutofillInfo. A readback caught that
failure. The CLI's update endpoint, used through `m365 request` for initial setup,
saved the prompt; subsequent ordinary `spp autofillcolumn set` calls and readback
succeeded. Never accept exit 0 alone as native save proof.

Stock CLI browser sign-in with the Agents Toolkit application returned AADSTS70007.
Source inspection found the exact protocol mismatch: the installed Toolkit uses
MSAL interactive authentication with PKCE and response mode `form_post`. Empty or
`query` response modes failed. The same MSAL interactive API with `form_post`,
inside the CLI's own process/cache, established the named QH connection and passed
an exact-site read. No tokens were copied between VSCode, browsers and CLI; no
new app registration, consent, licence or tenant setting was created.

`tools/autofill/cli-msal.mjs` preserves that narrow compatibility route. It changes
only the browser token-acquisition step for the installed CLI. Set absolute
`PPG_M365_CLI_ROOT` (installed package directory) and `PPG_AUTH_URL_FILE` (private
URL delivery file), then invoke it with `login`, the existing approved `--appId`,
`--tenant`, `--connectionName` and `--authType browser`. Open the exact generated
URL in the authorised browser, select the intended account, and leave password,
MFA and new consent with the user. Do not put authentication IDs in public examples.
Verify the named identity and exact SharePoint target before writes. This adapter
is qualified with the observed installed version, not every future CLI/MSAL version.

## Licensing and limits of the finding

[Microsoft Learn](https://learn.microsoft.com/en-us/SharePoint/copilot-in-sharepoint-get-started)
describes Microsoft365 Copilot licensing and additional usage billing for advanced
work. The [document-processing route](https://learn.microsoft.com/en-us/microsoft-365/documentprocessing/autofill-setup?view=o365-worldwide)
also documents pay-as-you-go enablement. CLI/browser access does not supply an
entitlement. The account's assigned-product page showed E3 without Microsoft365
Copilot; admin-centre access was denied. Nevertheless, the subsequent exact native
pilot saved configuration and produced results, proving this bounded processing
route works. Tenant billing configuration, cost attribution and general production
entitlement were not audited. No billing, licence, site-AI or permission change was
made. Do not use the earlier missing UI as a claim that the service cannot run.
