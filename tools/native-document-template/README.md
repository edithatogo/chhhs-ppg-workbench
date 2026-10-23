# One-time PPG Word template authoring

This .NET command authors an unpopulated DOCX from the maintained review-package
Markdown. It uses Microsoft's Open XML SDK 3.5.1 (locked dependency), validates
against Office2013 and refuses existing output or source hash drift. It performs
no network/native operation and is not an operational document-population service.

From the repository root, with an existing compatible .NET SDK/runtime:

```sh
# Use the tool-directory restore/build instructions below; then execute the
# resulting DLL with the explicitly qualified stable host.
```

23 October stable runtime qualification supersedes the earlier preview-only
host observation. The tool-local `global.json` pins **10.0.402**, rejects previews
and disables SDK roll-forward. The existing host-wide11RC installation is unchanged.
An isolated install is available at `.local/runtimes/dotnet-10/`; do not assume it
exists on another checkout. Use Microsoft's official installer with exact version
10.0.402 and a project-local install directory, without modifying the shared PATH.
See [runtime qualification](../../docs/alm-closeout-20261023.md).

Run restore/build with the tool directory as the working directory so its SDK pin
is honoured (SDK resolution uses the working directory, not `--project`):

```sh
cd tools/native-document-template
../../.local/runtimes/dotnet-10/dotnet restore --locked-mode
../../.local/runtimes/dotnet-10/dotnet build --no-restore
```

From the repository root, use the explicit stable host for execution:

```sh
.local/runtimes/dotnet-10/dotnet exec tools/native-document-template/bin/Debug/net10.0/TemplateBuilder.dll templates/review-package.md EXPECTED_SOURCE_SHA256 NEW_OUTPUT.docx
```

Locked restore/build passed in an isolated source copy with zero warnings/errors;
the existing manual-population preservation/refusal tests passed under this host.
The shared utility binaries and live runtimes were not replaced. Generated candidates and proof stay in
ignored `.local/`. All maintained placeholders, two repeated paragraph groups and
an optional-content field are present. OptionalContent is plain multiline text;
blank content does not prove removal of a section. Native mapping, repeated/empty/
long Unicode behavior, editable output, link/access readback and preservation/
recovery require the actual qualified Word connector or preferred SharePoint route.
Local schema validity is not output proof. Developer qualification is not a
production entitlement or a licence assignment.

## Explicit manual population fallback

The original authoring command above remains separate. The `populate-manual` mode
fills a **new copy** of the exact maintained 34-control DOCX, using a separately
reviewed binding and accepted input. It uses the same locked SDK and installed
runtime; it is newly implemented local preparation, not native generation or an
unattended service. Check the preferred SharePoint route before selecting it.

```sh
# Build from the tool directory using the pinned stable SDK as above.
.local/runtimes/dotnet-10/dotnet exec tools/native-document-template/bin/Debug/net10.0/TemplateBuilder.dll populate-manual BINDING.json EXPECTED_BINDING_SHA256 INPUT.json TEMPLATE.docx SOURCE NEW_OUTPUT.docx NEW_RECEIPT.json
python3 tests/test_manual_docx_population.py
```

The binding pins the exact serialized input bytes, source/template hashes, case,
occurrence, request, job, output revision and document kind. Use the reviewed input
serialization whose hash matches the binding; do not quietly repin changed input.
Source/template/edited outputs are never regenerated over. Output and receipt must
be distinct absent paths. A receipt-write failure preserves the generated output;
reconcile its reported digest and missing/partial receipt before continuing.

All template controls must be accounted for. Repeated rows clone their prototype
with unique numeric IDs. Empty arrays omit their block and nested controls;
one comparison row plus empty consultation yields 29 named output controls from
34 original definitions. Optional blank text leaves no placeholder. Only
`word/document.xml` may change; styles, relationships and other package member
bytes must remain identical. Office2013 validation is required. The utility is
specific to this maintained control shape, not an arbitrary Word merge engine.

The local receipt always says `generationRoute=local-manual-fallback` and
`nativeGenerationQualified=false`. Independently compare actual values and shape,
upload only to the commissioned absent-only destination, download exact bytes,
inspect native rendering/access, make and save a scoped technical edit, retain
initial and edited version/hash separately, and verify retry preserves the edit.
Neither local success nor native editing supplies policy findings or approval.

The second candidate uses native Title/Heading styles, human-readable labels
within the repeating paragraph groups and no Markdown table scaffolding. All
control names and numeric IDs remain compatible with the first candidate.
OptionalContent has no unconditional label; empty text can still leave a blank
paragraph. Create a new candidate filename and qualify actual native generation
and rendered pages before adopting it. Never replace an earlier candidate/output.

## SharePoint property-bound cover qualification

The `sharepoint-cover seed` and `sharepoint-cover bind` modes author an unpopulated
cover using actual native-library property bindings. See
[qualification and preservation limits](../../docs/sharepoint-cover-generation.md).
Do not add columns to a shared evidence library: metadata propagation changed
existing DOCX hashes during qualification. Saved visible values remain unqualified.

## Standard native full-review fallback

`scripts/ppg_full_document.py` compiles this maintained control shape once for the
existing M365 Office Script runtime. It does not populate cases locally. The
native kernel fills scalars, clones each repeat item, assigns unique control IDs,
omits empty repeat groups and writes a detached revision. Generated hyperlink
content uses rich-text output controls; the maintained input template remains
unchanged. Read-only `validate-docx FILE.docx` checks Office2013 schema, but actual
Word rendering/editing and saved-output readback are independently required.
See [route and qualification limits](../../docs/full-review-word-generation.md).
