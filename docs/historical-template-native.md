# Historical template: native conversion and editing

20 October 2026. The original binary template behind the authorised candidate was
located in the retained archive. Repeating its earlier textutil conversion gives
exactly the candidate's `word/document.xml`, establishing the derivation without
claiming current authority. The earlier candidate and its158-element map remain
unchanged in frozen review packs.

A separate binary test copy was uploaded into the existing evidence library.
SharePoint changed its container bytes, so exact original bytes are retained in a
ZIP, downloaded and hash-verified. The uploaded binary remains separately retained;
no claim is made that it is byte-identical to the original.

Word for the web opened this binary copy and converted it into a separate DOCX.
CLI readback verified the new object, while the uploaded binary and original ZIP
remained unchanged. This supported native conversion resolves the earlier flattened
candidate's Word-opening failure for the historical development basis.

## What is verified

- Native DOCX opens in Word for the web and exports a three-page PDF. All three
  pages were visually inspected: headers, footers, graphics, tables and placeholders.
- Nine tables (including footer tables), two embedded graphics, seven Word fields
  (three FORMTEXT and four PAGE/NUMPAGES) and four external hyperlinks are retained.
- All four distinct link targets appear in the PDF. Rendered page fields correctly
  show1of3 through3of3. Destination access and authority are not inferred.
- A development-only edit appended in Word saves as native version2.0. The first
  immediate CLI read still returned version1.0; after Word reported saved and the
  copy switched to Viewing, readback confirmed version2.0 and the marker exactly
  once. All previous body text, tables, fields, links and media remain unchanged.
- The edited PDF displays that marker on page3 with correct numbering. No approval
  or consultation field was populated, and no policy content was changed.

The native inventory has70 elements, whereas the flattened candidate has158.
Those inventories use different table/paragraph structures; this is not evidence
that88 elements were lost or that all158 have been reconciled. Both complete files
and inventories are retained. A version-specific mapping must reconcile them before
changing template pins or section identifiers. Legacy FORMTEXT retention does not
qualify every form interaction or the Power Automate content-control contract.

## Use and remaining work

Use this derivative to continue manual template/section mapping and output checks.
The maintained V6 remains the working document; do not replace it with the blank
template, re-run the old flattening conversion, or overwrite human edits. Native
conversion and a saved test edit do not prove V6/template merge, structured
regeneration, variable-length content generation or original-DOC visual parity.
The supporting-documents table header sits at the end of page1, with its rows on
page2; layout refinement remains a separate proposed revision.

SP-04c still requires reconciliation of template elements, a separately generated
proposed revision preserving human edits, and saved V6 DOCX field refresh. Current
procedure/template authority verification remains open and nonblocking. No premium
route, new entitlement, billing, consent, source-register edit, issuance or
notification was introduced. Workflow behaviour is unchanged; frozen workflow1.6
and all held review-run pins remain preserved.

## Recovery and evidence

Private evidence: `.local/review-intelligence/20261020/template-native-v1/`.
Working native copies: `ReviewIntelligence-template-native-v1` in the existing
review-evidence library. Companion: `ReviewIntelligence-template-native-evidence-v1`.
The companion contains this guide, provenance/verification report, baseline and
edited PDFs, and a recovery archive. The archive retains the original binary,
flattened candidate, pre-edit and saved native DOCX, inventories and readback receipts.

Verify the downloaded archive CRC and every manifest hash. Run its `verify.py`
from the extracted directory using the repository Python runtime. This reconstructs
source preservation, conversion provenance and saved-edit checks from archived bytes.
Recover to a separate folder; do not replace a differing or human-edited file.
Actual tenant bindings and source content remain private, outside Git.
