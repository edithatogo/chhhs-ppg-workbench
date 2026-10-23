# Human content-readiness recording

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The native readiness-events List, recording form, version history and filtered
views are verified. It records human findings for exact document versions; it
performs no content assessment or policy approval. Start Here version 11.0 links the List and guide in the existing Teams workspace.

## Record an assessment

In the existing Teams channel, open **Start Here → Human readiness — recording
only → Record or inspect version-specific readiness findings**. This opens
**PPG Readiness Events** in the existing workbench site. A readiness record is
an assertion supplied by a human, separate from assembler completeness and policy
approval. Existing case status and imported source fields are unchanged.

1. Add a new item. Enter a unique EventUID, existing CaseUID, document reference,
   exact reviewed version reference and SHA-256 of those document bytes. Use a
   stable version-specific reference, not just a mutable latest-document URL.
   Title can briefly identify the event. Do not invent an identity or assessor.
2. Leave **Not assessed** when the assessment has not occurred. For an actual
   finding, choose **Needs changes**, **Ready for decision** or **Not applicable**,
   and enter the actual assessor, assessment date, short finding/rationale and
   evidence reference. Use the linked evidence for detail beyond the short field.
   Not applicable needs its actual rationale; it is not a completeness bypass.
3. Record conditions as **Unknown**, **None recorded**, **Open** or **Resolved**.
   Describe open conditions and the next action. These values record assertions;
   they do not allocate responsibility or send a notification.
4. Save and reopen the record. Confirm its document/version/hash, human finding,
   evidence, conditions and date. Author/Editor audit fields identify who recorded
   the item; they do not prove that person performed the assessment.
5. For a later finding, add another event and optionally reference the earlier
   EventUID in SupersedesEventUID. Preserve the earlier event. Version history is
   enabled for corrections, but is not a substitute for separate assessment events.
6. A changed version/hash requires a new assessment event, initially Not assessed.
   An old finding applies only to its recorded version. The List does not infer
   the current document version or roll a finding forward automatically.

Use **All readiness events**, **Needs assessment**, **Open conditions**, and
**Ready findings - version specific** views. The last view includes historical
findings: compare the exact version/hash and later events before using one.
It is not a list of currently approved policies. Readiness evidence does not
replace the established consultation, endorsement, authorisation or issue route.

## Validation and evidence levels

Native required fields and unique EventUID prevent missing identity/version
references and duplicate event keys. List validation requires assessor, date,
summary and evidence for any finding other than Not assessed. The hash column
checks length 64; native formula support did not permit the stronger format check
tested. Native validation does not verify link content, actual assessment,
signatures, hash correspondence, current authority or conditions adequacy.

For deterministic format and exact-byte comparison, use the read-only helper:

```sh
.venv/bin/python scripts/ppg_readiness.py --event PRIVATE-EVENT.json --version-ref EXACT-REVIEWED-VERSION --document PRIVATE-REVIEWED-DOCUMENT.docx
```

It validates hexadecimal SHA-256, open-condition notes and human evidence fields,
then compares the document's actual bytes and version reference. A mismatched
version reports Not assessed / Unknown; no result sets policyApproved to true.
This optional local check does not write records, generate documents or assess
content. No additional operator runtime is needed for the native List form.

## Provisioning and qualification

`config/readiness-recording.json` is the maintained field/choice contract.
`tools/readiness/provision.js` runs only within an already-qualified same-site
browser context; it adopts the existing uniquely named List, checks field types
and required flags, enables version history and EventUID uniqueness, and adopts
views. Exact resource bindings and detailed receipts stay private under
`.local/assurance-readiness/`. Existing permissions are inherited; no grants,
assignments, messages, source/catalogue/queue writes or approval flows are added.

Native API proof retained three labelled fictional events: version 1 has two
separate findings, while version 2 remains Not assessed. Missing evidence,
duplicate EventUID, short hash and N/A without rationale were rejected with
specific validation errors. Four local tests also pass. These are system tests,
not actual content readiness, clinical acceptance or a completed policy decision.
All four known fictional test records were archived privately and recycled after
verification; readback confirmed an empty List. No real finding was recorded.

This goal commissions the readiness-recording slice. Broader decision,
publication, implementation and verification recording remains in the existing
assurance track; it is not silently marked complete by this slice.

## Native closeout evidence — 16 October 2026

The native form saved and reopened a Not assessed item with blank human finding
fields. A fictional assessed item's summary was edited through the form, saved,
and reopened; native version history retains both 1.0 and 2.0. Separate later
findings remain separate events; version 2 did not inherit version 1's finding.
Provisioning was reapplied with the same List/field/view identities and no new
fields. Native view queries returned the expected fictional Needs assessment,
Open conditions and version-specific Ready subsets before cleanup. Existing
queue identity/status match preflight. Four local tests pass. Exact resource,
UI, history, repeat-provisioning, view and cleanup receipts are private.

Start Here was independently read back as published version 11.0, with one managed
readiness section and live/native-interactive manifest registration. The rendered
link opened the native List. The hosted guide matches its prepared bytes. Broader
assurance remains a separate in-progress deliverable.
