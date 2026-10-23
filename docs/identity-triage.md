# Guided identity resolution

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Prepare an evidenced identity decision locally, then let the existing source-only
importer apply it. Existing-UID aliases and explicitly authorised new identities
use the same guarded route. The source register and local review cases are never
written by this workflow. Identity acceptance is not policy approval.

## 1. Use current, retained inputs

Open **Start Here → Guided identity resolution** and download the tool ZIP and
this guide. Extract the ZIP before running its commands. Keep operational inputs,
actor names, decisions and receipts in a private directory outside Git.

Use the held run's `qw3-identity-snapshot-RUN.json`, retained raw acquisition and
source version. The latest candidate's `rawRecords` is also supported. The ZIP supplies
`config/identity-application-fields.json`, the native importer's approved field list. A successful
older candidate is not the current source that caused the hold. Reports retain
source/contract hashes, exact source aliases, original values and row numbers for
navigation. Missing UIDs are investigation leads, never identity matches.

Download `qw3-last-successful.json`. When it contains `identityLedger`, use that
checkpoint as the current contract input. Before the first amendment, use the
original `identity-ledger.json` and confirm its alias hash against the checkpoint.
The original ledger remains immutable bootstrap; the checkpoint stores the active
contract after a verified amendment. Never install an exported/staged ledger by
hand or edit a checkpoint to bypass a hold.

## 2. Inspect and record a decision

Commands run from the extracted tool folder. Every output must be new; existing
reports, decisions and evidence are not silently replaced.

```sh
.venv/bin/python scripts/ppg_identity_triage.py --snapshot PRIVATE/current-snapshot.json --ledger PRIVATE/current-contract.json --allowed config/identity-application-fields.json --action html --output PRIVATE/report.html
.venv/bin/python scripts/ppg_identity_triage.py --snapshot PRIVATE/current-snapshot.json --ledger PRIVATE/current-contract.json --allowed config/identity-application-fields.json --action report --output PRIVATE/report.json
.venv/bin/python scripts/ppg_identity_triage.py --snapshot PRIVATE/current-snapshot.json --ledger PRIVATE/current-contract.json --allowed config/identity-application-fields.json --action propose --exception-key EXCEPTION_KEY --output PRIVATE/proposal.json
```

Open the HTML report. Investigate every ambiguity, duplicate or missing identity.
Do not infer continuity from a title, row number or version-bearing code. Edit the
proposal: select `existing_uid` and its evidenced `existingUID`, or
`request_new_uid` with `existingUID: null`. Supply a rationale and supporting
`evidenceReferences`. Leave unresolved/ambiguous records held.

```sh
.venv/bin/python scripts/ppg_identity_triage.py --snapshot PRIVATE/current-snapshot.json --ledger PRIVATE/current-contract.json --allowed config/identity-application-fields.json --action accept --proposal PRIVATE/proposal.json --actor OPERATOR --decision-evidence DECISION_REFERENCE --output PRIVATE/accepted.json
```

Use `--action reject` to record rejection of a proposed decision. Acceptance records
an explicit identity decision only; it does not itself apply anything. The local
tool cannot authenticate the actor or judge the adequacy of their evidence.

## 3. Compile and check the application package

An existing-UID alias uses the supplied empty authorisation array:
`templates/identity-resolution/no-new-authorisations.json`. A new identity needs a
separate JSON array of explicit authorisations, each containing:

```json
[
  {
    "exceptionKey": "EXACT_EXCEPTION_KEY",
    "DocumentUID": "OPERATOR_SUPPLIED_UUID",
    "actor": "RESPONSIBLE_OPERATOR",
    "evidenceReference": "EXPLICIT_NEW_IDENTITY_AUTHORISATION"
  }
]
```

The tool never mints a UID. An existing-UID decision must reference an identity
already present in the active source-qualified contract. A new UID must not
collide with any existing or newly authorised UID.

```sh
.venv/bin/python scripts/ppg_identity_application.py --snapshot PRIVATE/current-snapshot.json --ledger PRIVATE/current-contract.json --allowed config/identity-application-fields.json --proposals PRIVATE/accepted.json --new-authorisations PRIVATE/new-authorisations.json --output PRIVATE/application.json
.venv/bin/python scripts/ppg_identity_application.py --snapshot PRIVATE/current-snapshot.json --ledger PRIVATE/current-contract.json --allowed config/identity-application-fields.json --verify-package PRIVATE/application.json --output PRIVATE/application-check.json
```

`--proposals` accepts one accepted object or an array of accepted proposals. The
compiler rebuilds the complete plan: all unknown aliases must be resolved without
duplicate identities or unacknowledged missing UIDs. Missing source rows never
authorise retirement or blanket count changes. Explicitly evidenced retention
uses the source-absence acknowledgement described below; other source exceptions
must be resolved before application. A package is bound to the exact source,
base contract, source-record fingerprints, allowed fields and approved UID set.
A locally valid package is not proof of native application.

## 4. Submit through the existing importer

Confirm that the assigned importer has no active run and preserve the previous
application file/version and its outcome. Upload the checked package as
`identity-application.json` in the existing **PPG Review Evidence** library.
Do not replace an in-flight or unverified package. The existing hourly importer
picks it up; its existing Run command can initiate a bounded operator run.
No new flow, connection, permissions or schedule is required.

The importer rechecks current raw bytes, source version and active contract. It
recomputes aliases/counts rather than trusting supplied staged values. Writes are
serial, use only importer-owned source fields, and conditionally update existing
items. Creation requires an explicitly authorised UID and stores its package hash
in `sourceIdentityDecisionRef`. The database retains unique `DocumentUID` values.
Readback precedes a single final checkpoint write containing the active ledger
and application hash. Cases, drafts and human review decisions remain separate.

## 5. Verify the actual outcome

Retain the run's `qw3-run-RUN.json`, its raw/source/candidate/application evidence,
and the success checkpoint from that same run. Verify the displayed package hash,
source hash, contract hash and complete readback count. Downloaded receipts alone
are not human policy approval.

```sh
.venv/bin/python scripts/ppg_identity_application.py --verify-outcome PRIVATE/application.json --receipt PRIVATE/qw3-run-RUN.json --checkpoint PRIVATE/checkpoint-for-that-run.json --output PRIVATE/outcome.json
```

The result keeps three states distinct:

- **accepted:** complete native application evidence is absent or mismatched.
- **applied:** complete package-specific native readback exists, but its matching
  committed checkpoint has not been established.
- **verified:** receipt and checkpoint agree on the exact run, package, source,
  result contract and complete readback. `policyApproved` remains `false`.

An older accepted proposal does not become applied merely because it was exported.
After later runs, use the archived checkpoint for the application run when checking
historical evidence. An already committed package is recognised on replay; it
cannot create another identity. Unchanged source/candidate replay produces no
source writes.

## Failure and recovery

A failed run preserves the last successful checkpoint. It may have completed some
source writes; retain its receipt and inspect the native per-action readback. For
unchanged source/contract, resume the same accepted package. The creation marker
lets the sole importer recognise its own interrupted creation, preserving the UID
and local edits. Do not mint another UID, delete a created item or reset a checkpoint.

Stale source/contract, ambiguity, collisions or remaining identity exceptions stop
application. If source or contract changed during a partial run, stop and retain
the source, package, creation markers and failure evidence for contract-owner
recovery; do not force the old package onto changed data. To replace a stale pending
package, record its withdrawal/rejection in retained evidence, wait for no active
run, preserve its version and clear the control to `{}` before capturing fresh
inputs and recording a new decision. Never edit hashes merely to make a package pass.

## Technical qualification and operating boundary

### Explicit source absence retention — verified, 17 October 2026

The user authorised separate new identities for the two evidenced new source
records and retention of the two evidenced absent catalogue records. This is an
identity disposition, not clinical rescission or policy approval. Detailed source
identifiers, actor records and evidence remain private.

The schema-2 compiler accepts `--absence-acknowledgements PRIVATE/absence.json`.
Each acknowledgement supplies `DocumentUID`, the exact `sourceSha256` and
`baseContractHash`, `actor`, `evidenceReference`, `decisionEvidence`, and
`effect: "retain_unchanged"`. The acknowledgement set must exactly cover the
remaining absent baseline identities. All aliases and catalogue identities remain
in the contract. New identities still require their separate explicit authority;
unrelated new records must never inherit an absent record's identity.

The bounded native extension compares only active source operations for writing,
retains absent rows outside that write set, and requires their unchanged readback
plus the complete catalogue identity count before committing. An acknowledgement
is tied to the approved source bytes; changed bytes require fresh investigation
and an updated decision before that absence is accepted again. Local verification
alone does not establish native application. The 17 October operational application
verified 985 active source rows and 987 catalogue identities: two new identities
and two absent records retained unchanged. Receipt, source, package, contract and
committed checkpoint agree. Recovery and committed-package replay each recorded
zero writes and zero attempted writes; all non-importer fields were preserved.
The ordinary hourly configuration was restored and a normal metadata-only run
left the catalogue values, ETags and checkpoint unchanged.

Retention readback compares stable item identities, selected substantive values
and mandatory ETags as duplicate-free sets. Request-generated response IDs and
query ordering are not item changes. A recovery may reuse the original retained
acquisition and records references only after their source bytes, record hash,
contract and approved package are independently reverified. The importer still
performs full current readback and commits the checkpoint last; never replace the
original pre-write snapshots with a later baseline or edit a checkpoint manually.

Native fictional checks cover an authorised new UID, existing-UID alias continuity,
partial-write failure with unchanged checkpoint, recovery without duplicates,
zero-write replay, preserved local edits, and stale-source/contract/collision
rejection before writes. Native source/contract verification is separate from the
operator's real identity judgement. The original setup did not perform real identity decisions. The later operational
application above followed the user's explicit identity authorisation. Content
readiness, clinical retirement, policy approval, publication and assignment remain
unperformed by this workflow.

For a purely fictional rehearsal, use the supplied `templates/identity-resolution/`
snapshot/ledger and its smaller `allowed.json` instead of the native field list.
Those specimens cannot be submitted to the real importer.

## Dependent consumer compatibility

The monthly-report and source-comparison consumers still require zero missing
UIDs and do not yet distinguish acknowledged retained absences. They fail closed
for this new contract; qualify that integration before refreshing their outputs.
Existing frozen outputs and schedules remain preserved. Successful reconciliation
does not establish that those consumers support the new retained-absence shape.
