# Submission-package assembly and completeness checks

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

This is the second administrative increment commissioned on 15 October 2026.
It supports custodian/coordinator preparation, before actual submission or approval.
Policy references are the retained Controlled Document Management Policy v3.1,
pp6–10, and Controlled Documents Guideline pp7–12. Those captured copies have not
been revalidated as current operative instruments. Applicable route, form sections
and evidence adequacy remain human checks.

## Operator workflow

1. In Teams, use Start Here or Evidence & Templates to download
   `PPG-submission-assembler.html`. Open the downloaded file in a current browser.
   Use the direct download link; SharePoint's sandboxed HTML preview cannot run
   this workflow. It is a self-contained local utility, with no installation or
   server required.
2. Record the existing case reference, candidate version and source baseline.
   Record document type/scope, custodian role, applicable matrix route and next
   action. A proposed role/route must stay explicitly proposed. Official document
   identifiers are recorded only if already assigned through the established route.
3. Select the actual attachments together and assign their evidence categories.
   Record original URLs/record references where known. The checks cover proposed
   document, approval form, consultation, endorsement, conditional risk/HRA evidence,
   communication/implementation plan, audit/evaluation strategy and comparison/log.
   Supporting files can be included without treating them as required evidence.
4. Select Check completeness. Missing presence/metadata items stay visible. Only
   conditional risk/HRA evidence can have an operator-recorded N/A reason; the tool
   does not determine applicability. A filename/category selection cannot verify
   signatures, form sections, currency, actual consultation or endorsement.
5. Download the draft ZIP, extract it and open `index.html`. It contains the
   attachment index, missing-items table and human-check list. `completeness.json`
   preserves the detailed result; `manifest.json` records file hashes and sizes.
   Attachment bytes are copied unchanged. A `.captured` Office original retains
   its bytes and suffix; remove the suffix only on a separate working copy to open.
6. Save the package in approved work storage and use the established coordinator
   handoff when actually authorised. Nothing is submitted, assigned or sent by the
   tool. It does not alter the source register, catalogue, queue or policy route.

The output always says **ASSEMBLED DRAFT / HUMAN CHECK REQUIRED**, including when
all file-presence checks pass. Incomplete draft packages are useful preparation
outputs; they are not ready-for-approval claims. Complete required form sections,
assess evidence, verify actual signatories/version and confirm the route manually.

## Reuse and preservation

If the browser asks about a download, use its normal file-save controls. A visible
download link remains after assembly if the automatic download was blocked.

Download the input record to retain typed metadata and file-category/reference
mappings. Reload it for later preparation, then reselect the actual files. Presence
is rechecked; saved assignments never stand in for actual files. A new package ID
is generated each time, so an earlier package or local edits are not overwritten.
No automatic case, task, invitation, notification or new reviewer is created.
The ZIP is a plain portable ZIP (no external compression library); duplicate names,
unsafe paths, more than 200 attachments and more than 100 MiB are rejected.

## Implementation and verification

Sources: `tools/submission-package/page.html` and `assembler.js`.
Build: `python3 scripts/build_submission_assembler.py` (maintainer only).
Focused checks: `node tests/test_submission_assembler.cjs`; independent Python
`zipfile` readback checks member CRC, every hash/size, Unicode and binary bytes.
Browser verification uses the retained IETP example, without changing its facts
or claiming substantive acceptance. The browser-generated example retains six
missing evidence categories. Detailed inputs, ZIPs and receipts stay private under
`.local/submission-package/`. Hosted tool/guide readback is distinct from browser
functional proof. Business acceptance and measured time savings are unperformed.

## Metadata prefilling extension

Section 4 of the same tool now prefills the existing review template and an editable
metadata cover, and checks edited review-package structure. See
[metadata prefilling](metadata-prefilling.md). The cover is supporting preparation
material, not the official approval form; generated files never establish approval.
