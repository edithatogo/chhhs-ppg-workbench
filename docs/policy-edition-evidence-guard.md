# Edition and publication evidence guard

Implemented 17 October 2026. This is a pure local companion to
`tools/lifecycle/validate.js`, not a native approval or publication mechanism.
Run `node --test tests/test_policy_evidence_guard.cjs tests/test_lifecycle_evidence.cjs`.

`tools/policy-editions/evidence-guard.js` exposes `validateEditionEvidence(input)`.
The executable fictional input is `config/policy-edition-guard-fixtures.json`.
A passing result means only evidence consistency. The caller must also pass the
common lifecycle transition validator; neither result authorises an action.

## Contract

Reuse `PPGDocumentUID` and `PPGPolicyEdition` from existing edition metadata.
Do not infer authority from `PPGCurrency`, upload date, a higher edition number,
or a SharePoint major/minor version. Existing currency findings, authority links,
check dates, evidence notes and native history remain untouched. Printed policy
edition and SharePoint version are separate; the fixture deliberately uses policy
edition 1.1 with different draft and destination native version labels.

The input adds an evidence envelope, not new native List fields:

- `authorised` and `published`: DocumentUID, policyEdition, resourceReference,
  nativeVersionRef, sha256; published also supplies downloadedSHA256,
  receiptReference and readbackAtUtc.
- `decision` and `publication`: selected existing Assurance Events using
  DocumentReference, ReviewedVersionRef, DocumentSHA256, EventUID, ParentEventUID,
  PublicationURL and PublishedVersionRef. The common validator checks their state,
  scope, chronology, conditions and selected parent chain.
- `route`: reference, revision, sourceSHA256, category, requiredRole, and
  currentAuthorityConfirmed. The supplied route must be selected and confirmed by
  the responsible operational process; this guard does not resolve delegation.
- `actorEvidence`: role, decisionEventUID, responderIdentity,
  signatureEvidenceReference and roleEvidenceReference. An entered ActorName or
  native record Author is insufficient. References are required but their truth
  and actual responder authority require independent verification by the caller.
- `replacements`: zero or more replacement/replaced identity-edition-hash pins
  with evidenceReference. This supplements the existing single replacement URL
  for multiple predecessors, without changing it or retiring catalogue records.

Operational mode also requires a confirmed authoritative destination and its
independent destinationEvidenceReference. A hosted archive or working library is
not made authoritative by a passing check. Fictional mode requires FictionalTest
on every envelope component and replacement edge, and reports only fictional
consistency. No fixture grants role authority or establishes a current route.

The current contract requires exact authorised and published bytes. If publishing
transforms the file (for example Word to PDF), hold it until a separately verified
rendition relationship contract exists; do not pretend the hashes should match.
Withdrawal execution and authoritative removal receipts are not implemented here.
No dates, review intervals or native currency decisions are generated.

## Acceptance and next native slice

Ten local guard tests plus twelve existing lifecycle checks pass. Cases cover
changed bytes/revision, missing download proof, actor assertions, fixture escape,
unconfirmed operational sources/destinations, multiple replacements, cycles,
self-links and invalid observation dates. These are fictional local checks only.

Proposed isolated target, subject to Workbench's exact target/event handoff:
`Templates/Native edition history qualification/FICTIONAL-publication-evidence-guard.txt`
in the existing evidence library. Create no real policy publication. Read back
its actual identity/version/downloaded hash and preserve the raw receipt privately;
use it in an explicit fictional envelope, then demonstrate a changed-byte hold and
repeat with no writes. Preserve the existing qualified edition-history fixture.
Native qualification subsequently created exactly one new fictional text file,
version 1.0, 161 bytes. A second browser tab independently read the native file
and downloaded bytes; repeat readback retained the same identity, version, ETag
and hash without writes. The local guard accepted that envelope, held altered
bytes and passed on repeat. This is native file evidence plus local guard
execution, **not guard execution inside Microsoft 365**, actual publication or
common-event acceptance. Detailed identifiers and receipts remain private at
`.local/policy-lifecycle/edition-guard-native-20261017/audit.json`.

Workbench retains the shared
case/request writer and the source/edition lane retains its single edition writer.

Detailed captured-source mappings and unresolved source conflicts remain in the
private lifecycle requirements report. Captured references have not established
current operative authority. Source denial must not be bypassed or interpreted as
withdrawal. The original-media audit remains paused; production document generation
remains a separate unqualified route.

## Native workflow adapter — 18 October

`tools/policy-editions/build_publication_qualification.py` builds a separate,
manual, serial, initially Stopped Power Automate definition using the existing
embedded standard SharePoint connection. It does not perform native I/O itself.
Four focused builder tests pass; the generated fictional definition passes
FlowAgent's offline validation. Live FlowAgent connector discovery was unavailable
because its Azure client was not signed in; the existing qualified Microsoft 365
CLI independently read the supported HttpRequest operation and reference flow.
No authentication change was made.

The constrained native profile freezes an explicitly handed-off fictional
Decision event, checks its native cardinality and fields, source ETag before/after
and exact text bytes, and creates an isolated issued representation only if absent.
It reads that copy back, rechecks the source and decision, refuses supersession,
then creates the reserved publication event only if absent and verifies all its
fields. Retry adopts only matching evidence. It writes no case, source, authority,
permissions, real publication destination or existing edition-history fixture.
It does not run the generic JavaScript guard inside Power Automate. Native
byte-for-byte text comparison binds the frozen locally SHA-256-verified source;
independent downloaded byte hashes remain a separate acceptance check.

Workbench released the exact target
`Templates/Native edition history qualification/FICTIONAL-LC04-published-source-20261018.txt`
and event prefix `LC04-PUBLICATION/EDITION-20261018`. The earlier 161-byte guard
fixture cannot represent the shared case's different source bytes. The new copy
must wait for the selected **actually saved** authorisation event and exact field
handoff. Prepared decision material is not a native authorisation receipt.
The following qualification supersedes that initial dependency hold.

Next: consume the coordinator's native Decision readback, generate and validate
the exact separate flow, invoke it through the qualified client, independently
read the saved event and target bytes, exercise repeat/conflict holds, and leave
the flow Stopped. Shared case recovery remains Workbench's responsibility.


### Native qualification result

The coordinator handed off the actually saved fictional final authorisation.
A separate native flow invoked the constrained profile successfully and saved one
fictional Publication event linked to that exact decision. Independent native
readback verified the event and the new issued representation: version 1.0,
187 bytes, matching the frozen source SHA-256. Replay succeeded with both create
actions skipped. A deliberately stale source token failed at SourceChanged before
copy/event writes. The qualified definition was restored and freshly read as
Stopped. Exact identifiers, run handles and downloaded bytes remain private in
`.local/policy-lifecycle/lc04-publication-20261018/`.

An initial run created the isolated copy but was cancelled while its event action
was pending. The initial payload omitted occurrence time and used defaults that
did not satisfy the existing List's publication rules. The corrected payload uses
a frozen occurrence time, DecisionOutcome=Unknown and VerificationResult=Not
verified. The retry preserved and adopted the existing exact-byte copy; no events
were present before retry. Regression checks cover those List requirements.

This qualifies actual native invocation and event/file readback for the fixed
fictional profile. It does not qualify actual responder authority, controlled
publication, dynamic execution of the full JavaScript guard, rendition conversion,
withdrawal, replacement execution, implementation/verification or next occurrence.
No case, original source, existing edition fixture or real currency finding was
written. Further lifecycle slices remain with their assigned writers.

## Replacement and withdrawal evidence — local extension

`validateEditionTransitionEvidence` adds a pure check for explicit `replace` or
`withdraw` evidence. It reuses existing Decision event scope fields and requires
a separate purpose-evidence reference naming the exact subject revision/hash.
Publication approval does not imply permission to replace or withdraw. An effect
receipt must identify that decision and subject, retain history and independently
show the active projection state. A missing URL or 404 cannot prove withdrawal.
Replacement additionally requires consistent publication evidence for the new
edition and an explicit matching replacement pin. The function writes nothing,
generates no policy currency state and does not establish responder authority.

Seven fictional transition tests pass alongside the ten publication-guard tests.
These are local tests only. Workbench reserved absent-only fictional relationship
and withdrawal receipt JSON files in the existing qualification folder. Native
execution still requires the coordinator's actual saved purpose-specific fictional
decisions and exact second-revision handoff. No replacement/withdrawal receipts,
second revision, catalogue updates or real authority/currency changes have been
written for this extension.

### Second-revision preparation

The isolated fictional replacement source has now been created absent-only, using
the original 187 bytes followed by the explicitly commissioned fictional revision
marker. Independent native metadata and downloaded bytes confirm 279 bytes and
native file version 1.0. That native version is distinct from fictional revision
2. Original source identity, ETag and byte hash match before and after preparation.
The actual new source identity/version/hash pins were handed to Workbench for the
coordinator's fresh version-scoped readiness and purpose-specific decisions.
Earlier revision evidence cannot satisfy the new document reference/version/hash.

Detailed pins and byte-preservation evidence remain private at
`.local/policy-lifecycle/lc04-edition-20261018/replacement-pins.json` and `audit.json`.
No relationship or withdrawal receipt, active projection or policy currency state
was written during preparation. This updates the earlier local-extension snapshot;
remaining dependent writes still require the actual matching decision handoff.

The replacement transition decision is scoped to the new authorised revision;
withdrawal is scoped to the affected existing revision. Replacement purpose
evidence must additionally retain exact predecessor pins. The native consumer
contract requests structured purpose/predecessor/replacement pins in the existing
NextAction note, rather than interpreting free text as a relationship assertion.
The new revision still requires a separately verified fictional publication
representation before its replacement relationship can be accepted.

## Native edition receipt profile

`tools/policy-editions/build_edition_receipts.py` builds a constrained fictional
native profile. It requires four frozen source/issued file pins and four actual
saved decision/publication event snapshots. It checks exact source bytes and
versions, selected event fields, absence of supersession, structured purpose and
predecessor pins, then saves two absent-only JSON receipts. Readback must match
the frozen request; replay retains the original receipt and run provenance.
Replacement is linked to the separately verified new-revision publication event;
withdrawal is linked to its own purpose-specific existing-revision decision.

The two receipts describe **separate isolated fictional projection scenarios**.
Their `activeProjectionState` does not change the real catalogue, document currency,
source publication destination or any current-policy finding. Both source and
issued revisions remain intact. There is no physical deletion, role assignment,
actual controlled withdrawal or security-retention claim.

The initial combined native guard exceeded 12,000 characters and its save was
rejected. Splitting the same checks into bounded expressions allowed native save
and invocation; regression tests retain all checks while bounding their sizes.
Six focused builder tests cover incorrect purpose, missing decisions, changed
bytes, wildcard tokens, wrong replacement publication and expression size.


### Terminal native edition qualification

The new revision's isolated issued representation and Publication event were saved
and independently verified. Its replay created no copy or event. The receipt
profile then saved both reserved JSON receipts; independent downloads matched the
frozen purpose-specific requests. Receipt replay skipped both creates, and a stale
source token failed before either write. Final independent readback matched all
four preserved source/issued files and both receipts, including their identities,
versions, ETags and downloaded hashes. The owned flow was restored to its original
qualified publication definition and freshly read as Stopped.

Exact file identities, run handles and raw receipt hashes remain private in
`.local/policy-lifecycle/lc04-edition-20261018/receipts/audit.json`; new-publication
proof remains in its adjacent `publication-v2` folder. This completes the bounded
fictional edition receipt slice, not actual policy supersession or withdrawal,
operational acceptance of the full lifecycle, or dynamic execution of the generic
JavaScript guard. No real catalogue/current-authority flags were changed.
