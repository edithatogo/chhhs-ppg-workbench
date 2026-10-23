# Dataverse migration closeout — 23 October 2026

Reviewed and archived **partial** at the user's request. DV-02 mapping/inventory and DV-03 offline reconciliation are delivered. DV-01 remains partial because migration need and exact target/container are unresolved. DV-04 native pilot/schema/security and DV-05 migration/cutover/recovery remain unperformed. All five task dispositions reviewed; full acceptance is false.

## Delivered and corrected

The full hybrid proposal preserves structured records and explicit relationships while retaining SharePoint documents, native versions, history and access. Its conceptual mapping includes all 25 imported source fields, local case decisions, three event histories, evidence references and explicit identity/checkpoint/history exclusions. It does not assign physical Dataverse names or prove a complete current native export.

Offline comparison preserves exact supplied values, absence/null/date distinctions, event namespaces and references. Duplicates, orphans, cross-case links, malformed optional references and circular histories refuse reconciliation. Identical normalized inputs alone cannot establish source completeness, actual import, security/history/file parity or cutover readiness.

Review found that the all-zero UUID was accepted as a persistent identity. The existing identity validator now refuses it for primary keys and populated references. A regression covers all six dataset keys plus case-document, readiness and evidence references. Fourteen focused tests pass. Repository setup validation passes 3,846 checks with zero failures or pending checks. An actual CLI reconciliation of the retained valid fictional export reports structural parity while keeping native import, security/history parity and cutover flags false. Identical nil-identity inputs fail before creating an output directory. Original input bytes are preserved. Private test/CLI audit is retained under `.local/dataverse-migration/closeout-20261023/`.

## Current discovery and scope

The latest same-day successful PAC enumeration, retained under `.local/cited-evidence/closeout-20261023/environments.txt`, exposes four environments to the existing Queensland Health identity. It supersedes the old expiry/two-candidate statements for discovery only. No authentication change or repeated native enumeration was needed for this closeout. Existing ALM/Word qualification environments and solution/publisher work have their own ownership and components; visibility does not select them for migration or qualify their use as an isolated migration target.

The previously selected publisher namespace for ALM does not itself select a migration solution, establish table ownership or justify adding migration components. Historical proposal statements about no PPG-named solution/publisher are not current collision checks. Refresh exact target solution/publisher inventory only when a specific migration experiment is selected. No schema/data/environment, role, licence, connection, source or checkpoint mutation occurred here.

## Remaining decisions and implementation

| Task | Remaining requirement | Supported next step |
|---|---|---|
| DV-01 | No reproducible Lists limitation, desired measurable improvement or selected exact destination | Record the actual relationship/security/operating constraint and outcome; compare with the existing Lists route. Select a migration target only if justified. A fictional comparative experiment may test feasibility, not invent production benefit. |
| DV-04 | Native physical mapping, keys/choices/relationships/security, licensing/capacity and pilot unqualified | In the selected exact container, qualify current maker/data operations and applicable end-user/runtime licensing; then fictional create/readback, duplicate/orphan behavior, repeat, interrupted-write recovery and rollback with source preservation. |
| DV-05 | Full native export/reconciliation and file/history/access/workflow/writer parity absent | Rehearse with independent exports and preserved SharePoint references; prove rollback preserving new human work before a separately scoped cutover. No production transfer or deletion follows from offline parity. |

The current proposal does not justify migrating a working system merely because Dataverse is visible. Retain existing SharePoint operation and the prepared proposal. A Dataverse data/API capability is not proof that a Power Automate Dataverse connector is non-premium; no premium connector dependency is introduced or qualified here. Technical feasibility, licensing, security and production benefit remain separate.

The latest request explicitly authorises archival, superseding the historical plan's archive-only-after-completion restriction. Archival preserves incomplete states rather than marking migration delivered. Participant access/benefit observations remain in the final adoption archive; they do not substitute for native technical migration evidence. [Archived plan](../conductor/archive/ppg_dataverse_20261016/plan.md) and [proposal](dataverse-migration-proposal.md).
