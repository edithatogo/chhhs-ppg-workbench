# QW2 implementation plan — Review workflow and templates

Scope corrected by the user's 15 October systems-build clarification. Earlier
business plan/history is [preserved](history/business-plan.md); all example sources,
v0.4/v0.5 packages, draft0.2 instruments and direction endorsement remain unchanged.

## Technical delivery

- [x] 1. **Reconcile scope and evidence.** Replace policy-work completion gates with usable template/workflow demonstration. Inspect retained native file/case receipts and source/draft artifacts; preserve business history.
- [x] 2. **Make the template reusable.** Default to DRAFT; capture provenance, comparison/change links, ownership assertions, route and unperformed business response fields. Provide an offline population command and operator workflow.
- [x] 3. **Verify a representative example.** Generate/read back a populated editable package with pending business fields. Confirm edits survive replay, invalid status input is rejected, original-source bytes remain, editable Word packages are valid and retained native example readback matches current artifact hashes/state.
- [x] 4. **Deliver technical handoff.** Supply the consuming QW1 owner one completion result with revision, evidence, reproduction and limitations; no new tenant writes or reviewer requests.

## Technical completion — 15 October 2026

Reusable template: `templates/review-package.md`.
Offline population: `generate_package.py` in this track; usage in [workflow](workflow.md).
Standard-library Python only, no tool installation/authentication/new application.
Output is editable Markdown; native example rendering/link integration remains QW1-owned.

Actual populated example/inputs and generation/technical-verification receipts:
`.local/review-package/technical-demo/`. Generation succeeds without actual reviewer,
acceptance, capacity, date or operative-policy confirmation. An operator edit was
retained when replay refused to overwrite the output. An unpermitted CHECKED status
field was rejected without output creation. Template/input/source bytes unchanged.

Current example Word draft hashes match retained native readback for both drafts,
direction JSON and change log. The canonical package's retained native version 6.0
has semantic/text parity; Office container byte equality is not falsely asserted.
Case receipt proves existing identity/field preservation and records direction
endorsement separately from pending content review. These are recorded native
readbacks, not new native operations in this closeout.

Proof: `.local/review-package/technical-demo/technical-verification.json`, plus
`.local/workbench/review-integration-v0.5/native-files-readback.json` and
`case-native-readback.json`. Originals/source provenance remain in the private
archive collection. System setup is complete; actual policy review, readiness,
authorisation, publication and operational acceptance remain unperformed.

## Next action

QW1 integrates this technical completion into the shared registry/handoff and
operator navigation. Later authorised users can populate/edit a package and record
actual business events. No responsible-review input is requested for build closure.

## Commissioned submission-assembly increment — 15 October 2026

- [x] Build one local/manual assembler for the custodian/coordinator handoff,
  with indexed attachments, recorded metadata, explicit missing items and hashes.
- [x] Preserve draft/human-check status; reject identity gaps, duplicate names,
  unsafe paths and invalid N/A bypass; flag empty evidence and unsuitable draft formats.
- [x] Verify ZIP members independently and an actual browser download using
  retained IETP example files. Both original attachments remain byte-identical;
  six missing categories stay visible. No substantive review or approval inferred.
- [x] Host the reusable HTML tool, guide and labelled example in the existing
  Evidence & Templates library with exact byte readback.
  Operator navigation/readback and handoff: published Start Here
  version 6.0 links the tool; all three hosted files match their local SHA-256.

Private proof: `.local/submission-package/`; operator guide:
[submission-package-assembly](../../../docs/submission-package-assembly.md).

## Commissioned metadata-prefilling increment — complete

Implemented locally: recorded metadata/source-fact separation, conflict-safe
prefill of the existing review template, editable metadata cover, seven blank
human fields, structural checks and input/template/member provenance. Both focused
Node suites pass. Browser ZIP and independent DOCX parsing provide output proof;
the final hosted/downloaded build also generated a verified ZIP and detected all
four deliberate structural defects. Template and member hashes matched; seven
human fields remained blank. Native macOS DOCX parsing succeeded.

Preferred SharePoint route checked first after the user preference: the exact
library’s Forms creation path exposed file-upload forms rather than document
generation. Feature/licence eligibility is unproven. Retained approval application
was located and preserved; current authority remains unconfirmed. See
[operation and qualification](../../../docs/metadata-prefilling.md).
Delivery: the existing tool download, both guides, labelled prefill example and
workspace manifest have native readback. The empty qualification folder was
recycled and absence verified. Existing tool navigation is preserved. No
source/case decisions changed. Preferred native production remains unqualified;
this completed increment executes local/manual, without a new runtime or sign-in.
