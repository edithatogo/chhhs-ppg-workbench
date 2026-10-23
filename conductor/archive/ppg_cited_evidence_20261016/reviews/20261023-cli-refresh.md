# CLI licence, capacity and native-route refresh — 23 October 2026

The authorised read-only refresh found no newly qualified native assistant route.
The track remains archived/deferred. Existing deterministic CLI lookup is usable:
all nine retained citations passed fresh native version validation after one
unclassified read failure was reconciled. Raw results and hashes are private in
`.local/cited-evidence/cli-refresh-20261023/qualification-audit.json`.

| Check | Actual CLI result | Implication |
| --- | --- | --- |
| Current account licence details | Same four products: Microsoft 365 E3, Power BI Premium Per User, Power BI Free and Teams Audio Conferencing; included PVA/Flow plans enabled | No assigned standalone Copilot or Microsoft 365 Copilot product observed; included service plans are not exact native grounding/publication proof. |
| Accessible environment enumeration | Default and the two existing Developer environments | Scoped to this authenticated identity; not a tenant-wide inventory. |
| Developer capacity | Five selected Copilot indicators each have zero allocated, auto-allocated, available and pay-as-you-go entitlement | No qualified capacity in this target. |
| Isolated Developer capacity | Same zero values | No qualified capacity in this target. |
| Default capacity | HTTP 403 | Unknown; no repeated denial or client switch. |
| Environment billing-policy reads | HTTP 404 for each of the three exact environment requests | These routes returned no linked-policy result; do not infer tenant-wide absence of billing or capacity. |
| Copilot inventory | No agents in the two Developers; two rows in Default, including the retained fictional PPG pilot | Retained pilot exists; unrelated agent untouched. |
| Retained pilot status | `pac copilot status` fails on nonexistent `componentstate_Property`; exact `pac org fetch` succeeds after omitting `top`, which conflicts with CLI paging | Active/Provisioned and component-state Published describe the Dataverse row. They do not prove a callable published agent, retrieval or entitlement. |
| SharePoint agent resources | Agent Assets list missing; checked `SiteAssets/Copilots` folder readable but empty | No existing agent file found in these locations; not site-wide or tenant-wide absence. |
| Existing CLI fallback | Nine citations pass final live metadata/version, byte, extraction and locator checks | Current-account deterministic evidence route works; no conversational AI, semantic review or lower-privilege acceptance inferred. |

## Resolution and remaining work

The first live fallback validation reported an unclassified failure on one TXT
metadata read. A targeted fresh metadata request succeeded; a second full live
validation passed all nine citations. Both results are retained. No source was
changed, repinned or silently overwritten to achieve the pass.

There is no identified eligible target in which to perform native runtime work
under current evidence. No activation, evaluation run, publishing, premium
connector, new billing, licence assignment, capacity allocation, permission,
consent or authentication change was attempted. Existing drafts and source copies
are retained. Human review and relevant-principal access testing remain deferred.

Resume only when an assigned Microsoft 365 Copilot route or existing usable
Copilot Studio/SharePoint capacity and authoring access is demonstrated for the
exact target. Then qualify source bindings/extraction, actual native answers and
citations, all twelve evaluation questions, human source review, relevant-principal
permissions and supported publication/launch/recovery. The included Teams service
plan alone does not establish eligibility for the requested generative SharePoint
grounding; no separate Teams runtime was created to bypass the existing gate.

## Reusable CLI checks

Reuse the current PAC profile and saved M365 client. Keep exact URLs, account,
agent IDs and output files private. No command below creates or enables resources:

```sh
pac env list
pac licensing get-many-environment-entitlements --environment EXISTING_TARGET_URL
pac licensing get-environment-billing-policy --environment EXISTING_TARGET_URL
pac copilot list --environment EXISTING_TARGET_URL
m365 request --method get --url 'https://graph.microsoft.com/v1.0/me/licenseDetails' --filePath NEW_PRIVATE_LICENSE_FILE --output json
```

For the current installed PAC status defect, use an exact-ID FetchXML read via
`pac org fetch --environment EXISTING_TARGET_URL --xmlFile PRIVATE_QUERY.xml`
selecting only the retained bot's ID/name/component/state/status fields. Omit
`top` because PAC applies paging. Preserve the error and do not substitute this
row-state read for actual runtime proof. Use the maintained
[CLI validation command](../../../../docs/cli-evidence-lookup.md#validate-captured-consistency-and-current-native-versions)
for the fallback. All native operations in this refresh were reads.

Repository verification: 3,793 setup checks passed; the same eight pre-existing
failures in other active plans/shared context remain. Archive/status links and
staged whitespace checks pass. No executable source changed in this increment;
the actual nine-citation live readback is its functional verification.
