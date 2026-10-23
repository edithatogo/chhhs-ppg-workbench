# Metadata prefilling and structural checks

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Third administrative increment, commissioned 15 October 2026. This extends the
existing submission assembler; it adds no service, scheduled job or new sign-in.
Use the same tool download from Start Here / Evidence & Templates, then open the
downloaded HTML locally. SharePoint's sandboxed preview is unsuitable.

## Operator workflow

1. Record metadata once in section 1, or reload the assembler input record saved
   earlier. Existing case reference, candidate version and source baseline are
   required; do not enter approval or acceptance that has not occurred.
2. Optionally import one source-record JSON in section 4. It must have the existing
   DocumentUID and source fields, either directly or in a `fields` object. Arrays,
   bulk candidates and missing/invalid identities are refused; identity is never
   guessed. This is a supplied/captured source assertion, not a live currency check.
   Only empty title, baseline and document-type fields can be prefilled. Conflicts
   are displayed and existing local values retained. Source custody, dates, status,
   identifiers and provenance remain a separate source-facts record. Source alias
   strings are never converted to a new official identifier, role assignment,
   candidate version, review interval, effective date or approval.
3. Select **Download prefilled drafts ZIP**. It contains:
   - `review-package-DRAFT.md`: the existing reusable review template, with header,
     source assertions and recorded/proposed role/route/next-action fields filled.
   - `metadata-cover-DRAFT.docx`: an editable metadata cover sheet with separate
     local/source tables and seven human decision/signature fields left blank.
   - `structural-checks.json` and `prefill-manifest.json`: structural results,
     template/file hashes and provenance. All outputs remain DRAFT/human-check.
4. Extract the ZIP and edit working copies. To recheck an edited review package,
   select its Markdown/text file and choose **Check edited package structure**.
   Check for missing/repeated/out-of-order required sections, unresolved markers,
   loss of the draft label and disagreement with the recorded title/case/baseline/
   version header. A structural pass does not assess content or evidence adequacy.
5. Add generated preparation files to the submission package as **Supporting /
   unclassified** if required. They are not the proposed controlled document or
   actual approval evidence. The applicable official approval form and its real
   sections/signatures still need to be provided through the established route.

## Form and authority boundaries

The DOCX is a local preparation cover, **not Form 5 or another official approval
form**. The retained `Approval-application-archived.docx` contains the publication
approval application, including its governance, consultation, endorsement and
human-rights sections. Its current authority has not been confirmed; the cover
does not replace it. The retained application is preserved unchanged. No signature, reviewer response, operative-version confirmation, role
acceptance/capacity, finding, endorsement, authorisation or agreed date is inferred.
The existing review template's corresponding fields remain visibly not recorded.

Prefilling uses a fresh package ID. It never overwrites an edited output/template,
posts a message, assigns a person, changes the register/case or submits a package.
Source facts saved in an input record remain source assertions on reload; they do
not become decisions. Unsupported metadata/source keys cannot populate protected
fields. Month precision and raw date values are retained without inventing a day.

## Verification and maintenance

`tools/submission-package/prefill.js` implements the rules; the existing build
embeds it and the current `templates/review-package.md` into the same download.
`node tests/test_metadata_prefill.cjs` covers preservation/conflicts, protected
fields, identity checks, marker refusal and each structural defect. Existing
submission-assembler checks also pass. ZIP/XML/hash checks and the macOS DOCX
parser independently read the generated cover; all seven human fields are blank.
Browser proof uses retained IETP metadata/source input. The generated ZIP passed;
a deliberately edited document exposed four independent defects. Private inputs,
outputs and receipts are retained in `.local/metadata-prefill/`. Native hosting
readback is separate from business acceptance, which remains unperformed.

## Preferred native route qualification — 15 October 2026

SharePoint structured document generation is the preferred route for maintained
Word templates and structured inputs. [Microsoft prerequisites and operation](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation)
require an assigned Copilot maker licence, library Edit permission and a DOCX
template. Documentation is not proof of tenant availability.

The exact existing evidence library’s Forms entry point was inspected. Its
Create new form path opened a file-upload form with a mandatory Upload file field,
not a document-generation template picker or field-mapping experience. A distinct
fictional qualification folder was created, verified empty and recycled with a
404 absence readback; no real input, response or generated document was submitted. No Document generation form choice was observed on this
path. The maker licence and feature eligibility remain unverified; this is a
specific unavailable entry point in the tested UI, not a tenant-wide denial.

Keep the working manual assembler as the bounded fallback while the preferred
route remains unqualified. Do not migrate current output until a maintained DOCX
shape has actual field/output parity, variable-length and optional-section checks,
editable save/readback, working access/links, and retry preserving human edits.
Keep calculations, identities, source facts and decisions in their existing layers.
Do not purchase/assign a licence, enable a feature, request new consent or change
settings to qualify this route.

Delivery readback: the final hosted HTML and its actual SharePoint download are
byte-identical. The downloaded tool generated a ZIP with the current template hash
and verified member hashes, and detected all four deliberately introduced editing
defects. The metadata guide, assembly guide, labelled example ZIP and workspace
manifest were saved/read back in the existing library. The hosted assembly guide
uses its library-local metadata-guide filename; the repository guide uses its
repository-relative link. Existing Start Here download navigation is unchanged.
