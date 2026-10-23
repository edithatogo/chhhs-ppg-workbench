# Production generation-to-package verification

Production generation remains unqualified. The existing package flow and legacy
kernel are unchanged. This document and `scripts/ppg_generation_contract.py` prepare
the missing validation boundary; they do not produce Word documents or establish
an entitlement. No alternate document runtime, source writer or new track is added.

## Native prerequisite — checked 17 October 2026

Evaluate the preferred SharePoint structured-document route first. Microsoft
currently documents `SubmitDocGenForm` (preview), with site, library, form and
field inputs. Form creators require a Microsoft Copilot licence and library Edit
access. A published form from an existing licensed maker may therefore be a
candidate; its exact form type, published template, access and output still need
qualification. An upload form with a promising title is not that candidate.

Fresh inspection of the existing PPG evidence library's Native Word Qualification
entry shows an Upload file field and the ordinary library-column form designer.
No input was changed and no form was submitted. This does not establish that a
generation form is unavailable elsewhere in the tenant.

The separate existing Default-environment Word connection reports Error, target
Token, Unauthenticated. FlowAgent Connectivity can read that state, while its
connector-operation search reports Azure CLI not-logged-in. Neither observation
proves a production licence. No reconnect, consent, billing, entitlement or flow
change was performed. The earlier PAC53003 denial remains a separate boundary;
do not retry it or transfer authentication caches.

Supported alternatives remain an existing eligible Word Online (Business) route
or verified exact-flow production Process allocation. Developer output success is
development evidence, not production entitlement. Workbench retains the native
package writer and shared objects; the retained v7 flow stays Off and unchanged.

## User confirmation — 18 October 2026

The user confirmed there is no existing published generation form or
production-licensed Word flow to nominate. This closes the request for a supplied
link; it does not prove tenant-wide absence or establish eligibility for a new
flow. Preserve the working document/package outputs while the production route
remains unqualified. No licence purchase, assignment, consent or connection repair
has been authorised by that answer.

The independently verified fictional lifecycle date file and locally composed
read-only closure observer support lifecycle integration. They do not generate a
Word document and do not satisfy the production-generation acceptance steps below.

## Read-only local contract

Run from the repository with explicit private files:

```text
python3 scripts/ppg_generation_contract.py \
  --request <frozen-request.json> --receipt <downloaded-generation-receipt.json> \
  --input <frozen-input.json> --template <downloaded-template.docx> \
  --document <downloaded-generated.docx> --observation <native-readback.json>
```

The command reads these files and prints a binding; it does not write them or call
a native service. A binding always says `local-binding-verification-only` and
`productionQualificationRequired: true`. Never present it as native acceptance.

The frozen request records document kind, CaseUID, occurrence, output revision,
source snapshot/hash, included identities, exact template identity/opaque ETag/
version/size/hash, frozen input hash, and the environment/flow/action/operation.
Reuse the existing selector's `caseBinding`, `catalogueBinding` and `sources` as
`sourceBindings`; do not recreate source selection, identity or business decisions.
The request must match its selected case, catalogue identities and baseline hash.
For SharePoint generation, retain a `formBinding` with form ID, normalized kind
`document-generation`, output format `docx`, and the actual metadata response hash.
These are adapter-normalized contract names, not invented native API properties.
The native adapter is not yet implemented or qualified.

A generation receipt must identify a successful actual invocation, nonempty run
ID and completion time, the exact request fingerprint and actual output native
identity/version/opaque ETag/size/hash. Retain it as a distinct package member.
An existing-artifact/schema2 receipt cannot satisfy this contract. Do not turn its
unknown historical authoring/null receipt into a generated-document claim.

Independent native observations must match the invocation/output, input hash and
before/after source/template/form bindings. Obtain them through the existing
qualified native reader; never manufacture them by copying expected values.
Downloaded template and output bytes must match their recorded hashes/sizes. The
output must be a structurally readable, CRC-clean DOCX, distinct from the template
and every preserved source. Any human edit or different native pin stops assembly;
prepare an explicit new revision instead of overwriting or restoring it.

Package roles are recorded baseline, generated draft, generation receipt and
selection record, plus package provenance. The retained legacy/schema2 kernel is
unchanged. Its generic schema1 assembly already supports these four members;
the read-only adapter now prepares that input after validating generation evidence.
Native orchestration and package receipt integration still need the exact-target
handoff and native qualification below.

To prepare the two existing kernel arguments, add all four options to the command
above: `--package-baseline <downloaded-baseline.zip>`,
`--package-selection <frozen-selection.json>`, `--job-id <new-job-id>` and
`--created-at <UTC-time>`. The command prints `job` and base64 `members`; it does
not upload, run the kernel or write files. Treat this output as private evidence.
The selection must match the request's actual case, catalogue and source bindings;
the baseline must match its frozen hash and native length. The embedded generation
binding retains occurrence, revision, template/output pins, input hash, invocation
and receipt hash. The generation receipt remains a distinct unchanged ZIP member.

This adapter is the local validation boundary. Calling the generic kernel directly
with an arbitrary `generationBinding` does not validate a generation claim. Native
integration must perform equivalent checks against actual independent observations
before passing inputs to the kernel, and recheck source/output pins before commit.
Neither the adapter nor the kernel establishes production entitlement or Word
layout. They continue to label production qualification as required.

## Remaining executable qualification

1. Identify and read back one genuinely eligible existing production form/flow and
   its template, connection and destination. Establish exact access/entitlement;
   creating the contract is not that evidence.
2. Use the existing frozen case/input selection and maintained template. Read the
   actual form metadata/connector specification before mapping any dynamic fields.
3. Invoke generation natively and retain actual run/action/output evidence and a
   distinct generation receipt. Never overwrite templates, manual drafts or earlier
   generated revisions. Reconcile a timed-out invocation before any new attempt.
4. Inspect the full Word output: mapped values, empty/one/many repeating groups,
   optional sections, links, Unicode, page layout and edit/reopen preservation.
   For SharePoint structured generation, test the actual automated path as well
   as the form: form visibility rules are not applied by Power Automate. Make
   fields optional where required for that supported path; do not infer a section
   is absent because its field was hidden in the form. In Word on the web,
   changing a field does not recalculate conditional sections. Preserve the edited
   file and create a separate revision if regeneration is needed; inspect the new
   section layout before selecting that revision.
5. Under explicit Workbench native handoff, add generated-document provenance and
   integration in a separate candidate, preserving legacy/schema2 behavior and
   the accepted flow. Qualify native claim/stage/commit-last receipt/final-pair
   readback, replay, recovery, changed inputs, stale pins and edited-output refusal.
6. Compare source/case/template/output pins, downloaded ZIP membership/CRC/hashes
   and the actual receipt. Only then update the operator route and shared status.
   Production deployment remains distinct from policy approval or circulation.

Focused tests exercise receipt/input/source/template/run/output tampering, false
existing-artifact generation, form-type confusion, invalid DOCX and ambiguous JSON.
Their fixtures are explicitly synthetic in-memory containers, not native Word
outputs or proof of layout, entitlement, throughput or production behavior.
The package handoff test executes the actual retained TypeScript kernel and uses
Python's independent ZIP reader to check CRCs, exact membership/bytes and embedded
generation provenance. Changed selection, baseline length/bytes and human-edited
output are refused. Repeated preparation is deterministic and preserves inputs.

References checked 17 October 2026:
- https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation
- https://learn.microsoft.com/en-us/connectors/sharepointonline/
- https://learn.microsoft.com/en-us/connectors/wordonlinebusiness/

Private prerequisite, native form and local CLI evidence:
`.local/unattended-package/production-generation-20261017/`.


## Preferred-route behavior refresh — 18 October 2026

The [current Microsoft instructions](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation)
still require a Copilot licence for the form maker, library Edit access and DOCX
input. They distinguish form field visibility from generated document content,
and describe the Word-on-the-web conditional-section limitation reflected in
step4 above. This refresh changes the output checks, not the recorded tenant
eligibility: no existing production form, entitlement or healthy Word connection
has been newly established. Retain the qualified manual fallback and current
native owner. A new document revision must preserve human edits and issued history.


## Exact-environment entitlement read — 22 October 2026

The existing PAC entitlement command succeeded for the originating Developer and
the new isolated Developer target. Both snapshots report zero allocated,
auto-allocated, available and pay-as-you-go entitlement for the selected Copilot
AI/messages/sessions indicators and Process/per-flow indicators. These scoped
capacity results are not a tenant-wide licence inventory or proof about every
maker account. Successful Developer Word execution does not establish production
entitlement or SharePoint document-generation maker eligibility.

The same exact Default entitlement read returned403. Its allocation remains
unknown; no unchanged retry, client switch, activation, licence assignment, billing
policy or capacity allocation followed. Ordinary qualified Default flow/SharePoint
access remains a separate proven route. These results hold only the conditional
production/AI step, and do not reopen completed Word output/managed recovery work.

Retain manual production/evidence preparation. Resume the affected runtime after
changed exact-target allocation or an eligible existing route is demonstrated.
Private native responses and scoped read audit:
`.local/ppg-alm/conditional-entitlements-20261022/qualification-audit.json`.
