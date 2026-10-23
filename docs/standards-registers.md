# Standards registers: operation and recovery

Current operator route: use the [web standards-check guide](standards-web-operator-guide.md)
for a fresh exact-version context through Power Automate. No operator CLI or desktop
Office is required. Native records, supported validation, web execution/readback/
repeat/refusal and copied-record recovery are technically qualified. Actual clinical
applicability and mapping/crosswalk acceptance remain human decisions. Dated sections
below retain their earlier evidence; developer validators are not operator requirements.

Five integration-owned SharePoint Lists now hold framework editions, requirements,
PPG mappings, requirement crosswalks and document relationships. Each has native
version history, a unique stable key and a `Review register` view. The schema is
[standards-registers.json](../config/standards-registers.json); exact IDs, field
bindings and view paths are private in `.local/deployment.json` under
`reviewIntelligence.standards`.

The initial records are two framework editions and eleven standard headings:
eight for NSQHS second edition and three for the identified third-edition draft.
The frozen initial release records that action-level coverage was absent. Draft
and published editions coexist. The Standard6 supplement below extends that
baseline without rewriting it. Source register assertions remain unchanged.

## Use and limits

Record proposed mappings against a document version and requirement key, with a
rationale and evidence. Record crosswalk correspondence explicitly; its default
is Uncertain. Framework status defaults to Draft. Reconcile source assertions
before accepting a mapping. A mapping is never a compliance certificate.

Cross-register identifiers are text references, not enforced SharePoint lookups.
The local `scripts/ppg_standards_contract.py` validator checks known references,
requirement ancestry, edition boundaries, draft-obligation refusal and reviewed
mapping evidence. `scripts/ppg_review_intelligence.py` checks document hierarchy
cycles. These checks are not yet attached to native form saves: direct edits can
create invalid references. Treat native entries as preparation records pending
validation through the supported web check; direct-form enforcement remains unqualified. No automatic approval,
notification, source mutation or policy publication route is connected here.

The existing manual validation step now has a qualified native-snapshot adapter:
`scripts/ppg_native_standards.py`. It reuses those validators plus the known
schema/history checks before producing an exact-version context. The current180
records/180 available versions pass; all eight mappings/eight links remain Proposed.
See [native validation and recovery](native-standards-validation.md). This checks
saved snapshot structure, not future form saves, cited content or actor authority.

## Recovery

1. Inspect the private native journal before retrying an interrupted operation.
   A tool timeout is not proof of failure. Inspect the original page job or exact
   list/key before starting another write.
2. Read existing list schema and actual StaticName/InternalName bindings. The
   provisioning function in `tools/review-intelligence/provision-registers.js`
   creates missing resources, refuses schema drift and checks choice defaults.
   It does not repair existing schemas, alter access or overwrite records.
3. Query each stable key before inserting seeds. If found, compare every expected
   value; retain human changes and stop on differences. Unique keys provide the
   server-side duplicate barrier. Save receipts privately.
4. Export records and available versions before any operational correction.
   Restore into a separate reviewed copy; do not delete or recreate populated
   registers. The current five-register snapshot has qualified copied recovery;
   follow [the scoped runbook](standards-register-recovery.md). This is not full
   disaster, permission or native-form recovery.

Native storage/schema/view readback is qualified for the current account only.
Ordinary-user access, full normative requirements, cross-register acceptance,
recovery beyond the qualified snapshot and operational adoption remain unverified. These lists
are SharePoint artefacts, not automatically included in a Power Platform solution.

## Source-standard reconciliation

The retained985-row source snapshot now has a complete assertion ledger and both
standards-tracking worksheets preserved as cached values. All24625 main-sheet
cells match the exact original workbook; stable document identities are joined
through the existing import candidate, without changing the importer or catalogue.
See [source reconciliation and recovery](source-standard-reconciliation.md).

There are983 numeric1–8 labels with possible second-edition heading correspondence
and two label9 assertions without a supported match. These are retrieval candidates,
not accepted mappings. Neither worksheet identifies a framework edition. The cached
tracking report totals986 rather than985 and differs for Standards4/5/6. Preserve
those differences and investigate source/report scope; never refresh or correct the
upstream workbook as part of this work. The identified third-edition draft remains
separate; no crosswalk or compliance claim is inferred.

## Standard 6 action supplement

[Version1 action index](../config/review-intelligence/nsqhs2-standard6-actions-v1.json)
adds eleven actions from NSQHS second edition, updated May2021. These are brief
non-normative topic summaries. Each links to its official PDF page; consult the
complete action and subclauses before assessment. The checked PDF hash is retained
in the supplement. `scripts/ppg_standard_action_records.py` verifies those bytes
and the existing edition/parent hierarchy before producing seed payloads. Changed
bytes, duplicates and cross-edition parents are refused. Frozen framework and
prompt releases remain unchanged.

The pilot proposes three mappings, for audit/improvement, patient identifiers and
minimum handover content. Evidence retains exact historical inspection passages
and both source hashes. These are partial relevance proposals against historical
V6, not full action coverage, current V7 mappings or compliance certificates.
They do not overwrite source assertions, accept a mapping, create a crosswalk or
change the third-edition draft. Human validation and current-edition reconciliation
remain required. Native save/readback and replay receipts are private; local tests
alone do not establish native delivery.

Native independent inventory confirms two framework editions, eleven original
standard headings, eleven new actions and three Proposed mappings. All14 added
records replayed with zero creates and exact stored-value matches. No mapping
was accepted. Detailed journals and independent exports remain private.

Six Proposed historical reference records and one unresolved target are now
accounted in the [document relationship review](document-relationship-review.md).
Native records/replay and the proposed-reference view are verified; accepted
hierarchy, consolidation and current-edition applicability are not inferred.

## Clinical Governance action supplement

[Standard1 version1 index](../config/review-intelligence/nsqhs2-standard1-actions-v1.json)
adds all33 action codes under the existing second-edition Clinical Governance
heading. Brief non-normative topic labels link to exact official PDF pages; they
are retrieval aids, not complete action/subclause wording or a compliance
checklist. Filter the existing requirement view by ParentRequirementKey equal to
the second-edition Standard1 key. Full action text, applicability and evidence
must be reviewed before proposing or accepting a mapping.

The canonical official PDF was reacquired on20 October and its bytes match the
retained May2021 edition. Every action code and PDF/printed-page locator was
checked. The existing validator produces33 create-only payloads, retaining
edition/parent identities; the Standard6 supplement and draft third edition are
unchanged. Thirteen focused contract/index tests pass. No new source assertions,
PPG mappings, accepted compliance, requirement crosswalks or clinical decisions
are inferred from indexing an action.

Native readback now has55 requirement records:11 original headings,33 Standard1
actions and11 Standard6 actions. All33 new records retain unique keys, exact field
values and version1.0. Replay creates zero. Complete before/after exports preserve
all original five-register records, field definitions and views; the two framework
editions, three Proposed mappings and eight Proposed document relationships are
unchanged. Exact target bindings and receipts remain private. Five evidence files
have hash/identity/version readback and zero-create replay; the downloaded source
archive retains the checked PDF, acquisition/page receipts, native snapshots and
generation-time definitions/code. Verify its manifest before recovering separately.

This is a new index supplement within the existing workflow, not a schema change,
mandatory-rule activation or native acceptance enforcement. Frozen framework,
prompt and workflow releases remain intact. Remaining standards/actions, current
PPG relevance, source-standard reconciliation, crosswalks, reference/acceptance
validation and copied standards-register recovery remain open.

## Consumer partnership action supplement

[Standard2 version1 index](../config/review-intelligence/nsqhs2-standard2-actions-v1.json)
adds fourteen non-normative action topics under the existing second-edition
consumer-partnership heading. It reuses the same20 October checked official PDF;
all codes and PDF/printed-page locators verify. Use the existing requirements view
filtered by the Standard2 parent key. Consult the full official actions and
subclauses before appraisal; these labels are retrieval aids, not normative text.

Two additional Proposed mappings relate the historical V6 inspection to shared
care planning and understandable ongoing-care/discharge information. Six exact
inspection passages, the inspection hash, official edition hash and action-page
links are retained. Current V7/template, conversion fidelity, implementation and
complete action coverage remain unverified. No sourceStandard assertion or old
mapping is replaced. The frozen earlier review pack remains a dated snapshot;
use this companion alongside it rather than silently updating its evidence pins.

Native inventory now contains69 requirements (11 headings/58 action indexes) and
five Proposed mappings. The14 action records and two new mapping records have
exact field/unique-key/version1.0 readback; replay creates zero. All previous
records, field definitions/views, both editions, eight Proposed document links
and crosswalk state remain unchanged. Fourteen focused tests pass. Six native
evidence files verify with zero-create replay; their recovery archive retains
original source bytes, six passage checks, before/first/replay exports and
creation-time definitions/code. Hash/CRC-check the downloaded archive before
restoring separately. No accepted mapping, compliance decision, permission,
notification or policy issuance occurs. Other action coverage, source reconciliation,
native reference/acceptance validation and copied standards recovery remain open.

## Medication Safety action supplement

[Standard4 version1 index](../config/review-intelligence/nsqhs2-standard4-actions-v1.json)
adds fifteen non-normative action topics with official PDF/printed-page locators.
It reuses the checked second-edition source bytes; consult all official action
subclauses before appraisal. Filter the existing requirements view by the
Standard4 parent key. These labels are retrieval aids, not prescribing guidance,
complete normative requirements or a compliance checklist.

Two Proposed historical-V6 mappings link discharge medicines-list continuity and
a reconciliation dependency for investigation. Five exact unrevised inspection
passages, document version and both source hashes are retained. Manual list entry
and a field for changed medicines do not prove best-possible-history reconciliation,
discrepancy resolution, list accuracy or receipt by patients/receiving clinicians.
Those questions require current subject/template, medicines-policy and workflow
evidence. No current clinical rule or full action coverage is established.

Native inventory now has84 requirements (11 headings/73 actions) and seven
Proposed mappings. Fifteen action/two mapping records read back exactly at1.0;
replay creates zero and complete post-insertion five-register exports match.
All previous records, schemas/views, both framework editions, eight Proposed
document links and crosswalk state are preserved. Fourteen focused tests pass.
Six evidence files verify/replay unchanged; the downloaded source/native-history
archive retains original bytes, five passage bindings, payload/contract and
creation-time definitions/code. Verify all hashes/CRC and restore separately.
Earlier review packs remain dated snapshots, without new mapping pins inserted.
No sourceStandard replacement, accepted obligation, permission, notification or
issuance occurs. Remaining actions, current sources, native acceptance/reference
validation and copied standards recovery stay open.

The Medication Safety supplement also validates all84 native requirement
parent/edition references and seven Proposed mapping references at the exported
snapshot. This point-in-time proof does not enforce future native form saves.
Its22-member recovery archive retains the explicit reference-validation receipt.

## Complete second-edition action-code index

The checked May2021 edition now has a complete151-code action index across all
eight standards. Four new supplements finish the index without rewriting the
initial headings or earlier supplements:

| Standard | Action codes | Supplement |
|---|---:|---|
| Clinical Governance | 33 | [Standard1](../config/review-intelligence/nsqhs2-standard1-actions-v1.json) |
| Partnering with Consumers | 14 | [Standard2](../config/review-intelligence/nsqhs2-standard2-actions-v1.json) |
| Preventing and Controlling Infections | 19 | [Standard3](../config/review-intelligence/nsqhs2-standard3-actions-v1.json) |
| Medication Safety | 15 | [Standard4](../config/review-intelligence/nsqhs2-standard4-actions-v1.json) |
| Comprehensive Care | 36 | [Standard5](../config/review-intelligence/nsqhs2-standard5-actions-v1.json) |
| Communicating for Safety | 11 | [Standard6](../config/review-intelligence/nsqhs2-standard6-actions-v1.json) |
| Blood Management | 10 | [Standard7](../config/review-intelligence/nsqhs2-standard7-actions-v1.json) |
| Acute Deterioration | 13 | [Standard8](../config/review-intelligence/nsqhs2-standard8-actions-v1.json) |

This is complete action-code retrieval coverage for that fixed edition, not full
normative subclause text, complete criteria nesting, applicability or compliance
appraisal. Brief non-normative labels link to verified PDF/printed pages. Every
code is unique and belongs to the correct edition/standard parent. The separate
third-edition draft remains Draft; no crosswalk or current obligation is inferred.
Use current official supporting advice and applicable rules during substantive
review rather than treating a frozen index as all later accreditation guidance.

Seventy-eight new action records and one Proposed historical-V6 relevance mapping
to comprehensive discharge/follow-up planning extend the existing native Lists.
Four exact unrevised inspection passages support partial relevance; current
V7/template, actual care plans, patient-selected supporters, agreed goals and full
action coverage remain unknown. Existing mappings are not replaced.

Native totals are162 requirements (11 original headings/151 actions) and eight
Proposed historical mappings. All79 added records read back at1.0; replay creates
zero and complete five-register post-insertion exports match. Earlier records,
field definitions/views, both editions, eight Proposed document links and crosswalk
state remain unchanged. Actual exported requirement-parent/edition and mapping
references pass the contract at this snapshot; future form-save enforcement is
still unqualified. Fourteen focused tests pass. Six native evidence files and a
downloaded source/native-history archive preserve all eight index definitions,
source/page/code checks, original/first/replay exports and creation-time code.
Verify CRC/member hashes before separate recovery; never replace human edits,
old keys, earlier report pins or the working bindings. No approval, notification,
permission or source-register change occurs.

Action-code indexing for this edition is complete. Source-standard reconciliation,
current PPG applicability/mapping, criteria nesting if needed, crosswalk review,
native reference/acceptance enforcement and copied standards recovery remain
separate unfinished work. Frozen framework/prompt/workflow releases stay intact.

The complete-index recovery archive verifies30 members, including all eight
supplement bytes/hashes and151 native-field/page comparisons. Preservation reads
cover complete current item payloads plus selected field binding/type/required/
unique and view-definition properties; they are not a full form/formatter export.

## Copied recovery qualification

The [copied-recovery runbook](standards-register-recovery.md) now has native proof
for all five working registers:180 records/180 available versions,37 custom fields
and11 views restored separately. Original schemas/values/histories/exported views
compare unchanged. All copied business values match; nine relationship contexts
and standards references match/validate. Record replay writes zero; view/settings
replay changes zero. Lists/items inherit the same site access, without ACL edits;
recovery targets stay off search/Quick Launch and no working bindings change.
This closes the earlier copied-record gap for this snapshot, not full disaster,
permission/form/retention recovery, production adoption or acceptance enforcement.
Source/current-applicability work remains open. Preserve original platform audit
provenance in the archive instead of copying it into new native audit stamps.
