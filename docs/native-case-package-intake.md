# Native case-to-package intake

> 23 October closeout: [exact saved-native-body CLI fallback and remaining automatic-flow parity gate](package-closeout-20261023.md). The track is reviewed and archived partial; earlier dated qualifications retain their scope.

The existing manual M365 package flow has a separate request type for read-only
case intake. It prepares the maintained full-review Word draft and evidence ZIP
inside the existing Office Script runtime. Optional Standard PDF conversion stays
downstream of the usable core output. The original fixed-cover default and earlier
full-review requests keep their scripts and fingerprints.

## Operating steps

1. Select the maintained request for the case, using the private operator handoff.
2. For a new output, change its existing output-revision library property. Reuse
   the same revision to verify/recover an unchanged job.
3. Open the existing package flow, enter that request item ID and choose **Run**.
   Read the saved Word/ZIP completion and the separate PDF outcome.

One-time request setup copies the existing configuration and supplies the native
case item ID, expected CaseUID and selection mode. The generation template and
existing connection bindings are reused. Source-pack manifests, Word population
and field-value files are not prepared locally for each generation.

## Explicit selection contracts

| Mode | Required source | Interpretation |
|---|---|---|
| `recorded-baseline` | UUID case, retained successful selection, exact original baseline identity/version/hash, current linked catalogue identities and separately observed draft | Historical baseline; catalogue refresh is context, never a silent case repin. The selected draft is a fresh snapshot and is not asserted to equal its earlier historical bytes. |
| `catalogue-current` | UUID case with baseline matching every linked current catalogue row, ZIP or JSON capture and an existing DOCX draft | Consistent source snapshot; operative policy currency remains unassessed. Matching native capture was exercised 23 October, but output-byte parity and unchanged replay failed; see dated result below. |
| `fictional-initiated-source` | Existing initiated fictional occurrence, its matching initiation JSON, exact original TXT source/version/hash, and complete empty assurance/consultation/readiness sets | New source-only full draft. No prior acceptance, findings or decisions are inherited; no candidate draft is assumed. |

Case, catalogue and file pins are read again before output writes and before the
completion receipt. Initiated-case event sets are also rechecked. Missing identities,
incomplete reads, changed scope, stale source or a mismatch refuse the selected
operation. The current selector's mismatch guard is retained. No case, source,
catalogue or business-status writer is introduced.

The generated body records selected facts and unresolved findings. Original source
bytes remain in the ZIP, with their actual extensions and provenance. Historical
draft bytes and earlier receipts remain retained separately. These technical
packages are DRAFT/unissued; generation is not policy review or authority to issue.

## Qualification and limits

The dated case has actual saved DOCX/ZIP/PDF proof, exact 25-field comparison,
schema validation, inspected two-page rendering, original baseline/draft member
hashes/CRC and an unchanged native retry with every creation skipped. The initiated
fictional adapter also has actual DOCX/ZIP/PDF, exact-field/source-byte/schema and
inspected layout proof. Its retry skips every creation. Current-mode mismatch
refuses before all writers, leaves no output files and preserves both source cases.
### Catalogue-current native qualification attempt — 23 October 2026

A bounded fictional case now matches the current source capture and catalogue
identity: Review Queue item 30 (`PRIVATE-NATIVE-BINDING-04`) links
catalogue item 23 (`PRIVATE-NATIVE-BINDING-05`), and both name the
same captured JSON baseline. Request item 3437 was read by the existing manual
flow. The capture and draft pins, catalogue identity, case binding, and source
hash checks passed.

The first native run (`PRIVATE_RUN_REFERENCE`) created a DRAFT DOCX
and ZIP, then failed the `SAVED_BYTES` guard before writing a completion receipt.
The separately saved DOCX is 65,922 bytes (UniqueId
`PRIVATE-NATIVE-BINDING-08`, ETag `"{PRIVATE-NATIVE-BINDING-08},3"`).
The ZIP is 2,867,471 bytes (UniqueId
`PRIVATE-NATIVE-BINDING-09`, ETag
`"{PRIVATE-NATIVE-BINDING-09},2"`). It is a valid ZIP and retains
the exact 2,741,393-byte capture and selected 63,695-byte draft. Its embedded
`document/PPG-review-DRAFT.docx` is 45,099 bytes and does not match the separate
DOCX bytes; the two documents render the same extracted text, but binary parity
is a required guard and is not met. The flow's `Create_cover` action input was
60,745 bytes, matching the 45,099-byte DOCX encoded in base64; SharePoint saved
65,922 bytes. The saved DOCX differs in `customXml/item1.xml` (the library's
content-type schema version/field IDs and indexed `PPGCurrency` metadata),
`customXml/itemProps1.xml` (data-store item ID), and an added `[trash]/0003.dat`.
This locates the discrepancy at native library persistence, not at catalogue or
case identity selection.

Same-run resubmission (`PRIVATE_RUN_REFERENCE`) failed safely at
`OUTPUT_EDITED`; claim/cover/package writers were skipped. A post-replay native
readback confirmed both output ETags and lengths unchanged. The failed pair is
preserved, with no completion receipt. Do not reuse or overwrite it. The lane
remains open until the route packages the exact SharePoint-saved DOCX bytes (or
uses a qualified output location that preserves the generated bytes), then passes
native readback and unchanged replay under a fresh output revision. Any revised
claim must bind the actual packaged DOCX and must not overwrite this failed pair.
No source, catalogue, or case records were changed by the runs.

Fourteen focused local intake, flow-builder, and full-document tests pass. This
does not override the failed native output-parity gate or establish policy
currency, substantive review, approval, or authority to issue.

The new adapter permits at most 3MB complete raw package content and retains the
4MB serialized invocation/response guard. Existing cover/full/frozen-package
routes retain their 2MB raw limit. A retained current JSON capture of about 2.74MB
produces a locally measured response of about 3.91MB; this is not a native
large-capture acceptance claim or a provider maximum. Oversize refuses before
writers; it does not truncate or silently omit source bytes.

The maintained full-review shape, its original edit-preservation and recovery
guards remain in use. Arbitrary binary attachment merging and new conditional
document shapes are separate scope. No licence, billing, permission, schema,
schedule, application, approval or notification workflow was added.

Private native receipts: `.local/unattended-package/combined-word-20261020/intake/`.
The broader unattended-package track stays open for acceptance not yet evidenced.
