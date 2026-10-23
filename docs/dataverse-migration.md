# Dataverse migration

> Current [23 October closeout](dataverse-closeout-20261023.md): offline scope reviewed/archived partial, nil UUIDs refused; native migration and cutover unperformed.

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Preparation16October2026. No environment, solution or publisher has been selected.
No tenant schema, security role, data import, document relocation, application or
cutover has been performed. The existing SharePoint system continues operating.
The user selected a full migration proposal; see [the full proposal](dataverse-migration-proposal.md).
Exact target discovery and the migration driver remain unresolved.

## Declared-source inventory and proposed target

`config/dataverse-migration.json` derives a proposal from the maintained repository
field contracts, not a fresh native schema export. It covers:

| Current logical dataset | Proposed target role | Preserved business identity |
|---|---|---|
| Catalogue | SourceDocument | DocumentUID; all25 imported source fields and provenance |
| Review queue | ReviewCase | CaseUID; local decisions and source links |
| Readiness events | ReadinessEvent | EventUID plus original CaseUID/version/hash |
| Assurance events | AssuranceEvent | EventUID plus original CaseUID/version/hash |
| Consultation/handoff events | ConsultationEvent | EventUID plus original CaseUID/version/hash |
| Evidence library metadata | EvidenceReference | Native file UniqueId; original URL/version/hash and edition/currency assertions |

These are conceptual table roles, not created Dataverse logical names. Publisher
prefix, ownership model, solution, alternate-key definition and choice mappings
remain unassigned. Keep existing business identifiers even if Dataverse assigns
its own row GUID. [Alternate keys](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-alternate-keys-portal)
can support integration identities; actual key activation and retry behavior need
native qualification before upserts. No title/row-position crosswalk is inferred.

Case/document links require explicit relationships, not a new DocumentUID from a
lookup. Events retain their separate namespaces and recording order/version evidence.
Preserve raw dates and YYYY-MM precision; do not invent a day or reinterpret a raw
Excel serial as an already verified UTC timestamp. Preserve null versus absent,
choice labels, unknowns, unresolved roles and unperformed decisions.

The proposed evidence strategy retains SharePoint files, edit history, URLs,
retention and access. Reference metadata does not reproduce document bytes or ACLs.
Do not flatten the archive, copy sensitive documents to a public store, discard
human edits or claim model-driven app access supplies document access. The preferred
structured Word route and current working generator remain separately qualified.

Identity aliases/decisions, active ledger, successful sync checkpoint, raw snapshots,
flow definitions/connections, views/forms, source acquisition receipts and prior
native item versions require a separate operating/history preservation plan. The
six-dataset checker does not migrate or reconcile those artifacts automatically.

## Offline reconciliation

Requires repo-local Python3.15.1 standard library; no Dataverse login or package installation.
Create a complete normalized export from each side using existing original field
names. Explicitly map target physical columns, lookup GUIDs and choice values back
to this representation in a separately qualified export adapter; that adapter is
not implemented here. Do not omit fields, records or unresolved identities to make
parity pass. Keep native export receipts, completeness counts and projection rules.

```sh
.venv/bin/python scripts/ppg_dataverse_reconcile.py --source PRIVATE-SOURCE.json --target PRIVATE-TARGET.json --output .local/dataverse-migration/NEW-REPORT
```

The maintained fictional example is
`templates/dataverse-migration/fictional-normalized-export.json`. Inputs must declare
all six datasets and an identityExceptions array. Existing UUID identities are
required; duplicates and orphan case/document or event/case links fail visibly.
Populated correction, parent and assurance/readiness references must resolve to
events in the same case; same-history self links and circular parent/correction
histories fail. Populated evidence document references must resolve to the catalogue. Duplicate case document links and JSON
object keys fail rather than being silently collapsed. Optional references are
blank only when absent, null or empty text; false, zero, arrays and objects fail.
These are structural checks; they do not perform substantive event review or validate every stage rule.
Missing/extra target rows and every supplied field difference are reported.
Unknown target fields are differences, not silently discarded system fields.
Source/target file hashes and normalized bundle hashes are retained; destinations
must be new. Detailed reports can contain private identities; keep them ignored.

A structurallyReconciled=true result means parity of supplied normalized values
and checked explicit links only. Two incomplete exports can agree. The checker
cannot prove acquisition/completeness, native security, full history, file access,
version currency or functioning flows. It always records cutoverAuthorised=false;
never promote its result to permission to disable the source or switch writers.

Thirteen focused tests cover parity, missing/extra fields, duplicate/orphan identities,
raw-date/month precision, absent/null, boolean/number differences, exceptions and
source preservation, duplicate JSON keys and valid/broken event references.
The saved fictional CLI result is a local demonstration,
not native import or migration acceptance.

## Native qualification and cutover boundary

First establish the actual Lists limitation and bounded scope, environment URL,
existing licence/capacity, solution/publisher and target security/ownership model.
An account able to manage an environment is not proof it can access its data;
[Dataverse roles](https://learn.microsoft.com/en-us/power-platform/admin/database-security)
control that separately. Copilot or Power Automate entitlement findings from other
tracks do not determine Dataverse eligibility. Do not assign roles, self-elevate,
create a trial/environment or change billing to complete this preparation.

The Dataverse overview skill requires confirmation of the exact environment before
native operations and solution-first metadata. Preserve one writer per native
object. After target qualification, stage fictional parent records before lookup
children, verify saved keys/relations/choices/date behavior and least-privilege
read/write behavior. Test denied writes and rollback without changing access to
force a pass. Actual metadata changes must be exported/unpacked into the repository
through the selected solution route; no source-of-truth schema may live only in a portal.

A full migration additionally needs a consistent source snapshot/delta boundary,
serial retry/readback, reconciled history/files/ACLs/flows, documented interruption
recovery and a rehearsed rollback. Cutover must name the source writer stop, target
writer start and post-switch verification; preserve original source data/history
and working outputs until accepted parity/recovery. No cutover or deletion follows
from the roadmap, a successful local test or the existence of a target environment.
