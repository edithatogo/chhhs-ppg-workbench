# Decision and implementation assurance

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Use **Start Here → Decision and implementation assurance**. Native Lists/forms
record human assertions and evidence. They do not assess content, grant approval,
publish a policy, assign people or perform implementation. No waiting flow,
notifications or automatic source/case-status updates are introduced.

## Reuse the existing case and package

Copy the existing **CaseUID** from Review Queue. Keep its route, proposed or
accepted roles, response/conditions, next action and source baseline in that case.
Do not turn a proposed role into an accepted assignment. DocumentReference names
the stable document identity; ReviewedVersionRef identifies the exact reviewed
version, and DocumentSHA256 retains the hash of those exact bytes. Use a stable
version-specific reference and hash, not just a mutable latest-document URL.

Continue using the existing submission assembler and its **completeness.json**
missing-items categories. PackageEvidenceReference links the actual package/index
or completeness report and its revision. File presence is not a human readiness
finding, evidence adequacy or approval. This feature does not rebuild the assembler.

## Record the stages

| Stage | Record and evidence |
|---|---|
| Human readiness | Use the existing PPG Readiness Events List and guide. Record the actual assessor, date, findings, conditions and evidence for this exact version. Not assessed remains valid. |
| Decision | Add an Assurance Event with Stage Decision. Record the actual decision reference, date, actor, outcome, conditions and evidence. Link ReadinessEventUID when applicable. A recorded approval is an assertion about the named version, not software authorisation. |
| Publication | Add a separate Publication event. Link the decision's EventUID in ParentEventUID; record the actual publication URL, published version, date, actor and evidence. Recording this event does not issue or circulate anything. |
| Implementation | Add a separate Implementation event, linked to the relevant decision/publication event. Record short actual actions and evidence, with detail in the linked evidence. Repeat actions can use separate events. |
| Verification | Link the implementation event; record the actual method, date, result, actor and evidence. A failed or inconclusive result remains explicit. |

Every Assurance Event needs a unique EventUID, CaseUID and exact document/version/
hash. Leave RecordState **Unknown** or **Pending evidence** until the assertion and
evidence exist. Recorded and Not applicable require actor, date, short rationale
and evidence. Not applicable is a reasoned assertion, not an evidence bypass.
Use actual recorded roles and actors; Author/Editor shows who entered the record,
not who performed the assessment or decision.

DecisionOutcome is for Decision events only; leave Unknown on other stages.
VerificationResult is for Verification events only; leave Not verified elsewhere.
Open conditions need short notes. NextAction carries the next short manual action.
Longer rationale, action detail and supporting material belong in linked evidence.

After an actual decision, create pending Publication, Implementation and
Verification events for work that remains. The focused views show entered records:
**an absent event or empty view means no recorded evidence, never completion**.
The system does not invent a route or silently create future business tasks.

## Preserve history and version scope

For another decision or finding, create another event and reference the earlier
EventUID in SupersedesEventUID; keep both. ParentEventUID links stage evidence;
SupersedesEventUID records history and does not copy an earlier conclusion.
When resolving a condition on the same event, record the actual resolution
reference/notes and change ConditionsState explicitly. Native version history
retains the earlier open state. A new decision does not silently close old conditions.

For changed document bytes/version, add new events initially pending/not assessed.
Do not retarget an old finding/decision to the new version. Compare the exact case,
document, version and hash before relying on a historical event. The Lists do not
infer the latest operative document or automatically select a final decision.
Save and reopen each record; check its identity, stage, state, evidence and links.

## Focused views

- **Needs assessment** in Readiness Events shows recorded pending findings.
- **Missing stage evidence** includes Unknown and Pending evidence assertions.
- **Outstanding conditions** shows explicitly Open condition records.
- **Awaiting publication**, **Awaiting implementation** and **Awaiting verification**
  show the corresponding pending/unknown stage records.
- **Decision history - version specific** retains all decision assertions, including
  older versions and superseded decisions. It is not a current-approved-policy view.

## Validation boundaries and optional deterministic check

Native required fields, unique EventUID, stage-specific validation and version
history prevent missing identity, duplicate keys and incomplete Recorded entries.
The native hash check is length 64; it does not verify hexadecimal format or byte
correspondence. Native validation also does not authenticate an actor's assertion,
check evidence contents, prove operative authority or verify cross-row links.

The optional local/manual validator checks hexadecimal format, exact document bytes,
case/version matching, parent stage and evidence state, and readiness-event identity.
It never writes, publishes or marks policyApproved true. Download the validator
package, extract it and run with private inputs outside Git:

```sh
.venv/bin/python scripts/ppg_assurance.py --event PRIVATE-EVENT.json --case-uid EXISTING_CASE_UID --document-ref STABLE_DOCUMENT_REFERENCE --version-ref EXACT_VERSION_REFERENCE --document PRIVATE-EXACT-DOCUMENT.docx
```

For a proposed new event, add `--history PRIVATE-PRIOR-ASSURANCE-EVENTS.json` and
`--readiness PRIVATE-READINESS-EVENTS.json`. These are JSON arrays. When checking an
already saved event, exclude that event itself from history; duplicate EventUID
checking is for a proposed addition. Match native internal field names when
exporting. Missing, ambiguous or wrong-version parents remain errors. No local
check proves evidence adequacy, actual policy approval or completion of real work.

## Technical verification and operation

The maintained field/view contract is `config/assurance-recording.json`; additive
same-site provisioning is `tools/assurance/provision.js`. Reapplication adopts the
existing List, fields and views, rejecting schema/choice/view drift. Inherited
permissions and native versioning remain; existing cases/imported fields are not
changed by provisioning. There are no new Teams tabs or approval automations.

The isolated fictional proof saved/reopened a native pending form, retained its
versions 1/2/3, kept two different decisions, linked readiness and all later
stages, and left version 2 pending/not assessed. Eight invalid native submissions
were rejected; focused view counts matched the entered records. Local checks
confirmed old-version decisions do not apply to version 2 and no result grants
policy approval. Detailed receipts and fixture cleanup evidence remain private in
`.local/assurance-readiness/`. Fictional examples under `templates/assurance/`
contain no clinical content and do not establish actual readiness or a decision.
