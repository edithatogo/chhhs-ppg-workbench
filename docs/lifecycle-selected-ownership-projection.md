# Selected-case fictional ownership projection

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The separate projection flow consumes the actual Lists-selected fictional case and
its verified saved request. It derives the proposal from that request, requires
exactly one response, and accepts only the privately bound Accepted response with
matching case, document, version, hash, subject role and initiating role. Both
records must be fictional ownership events without supersession; the response must
retain its reason, evidence and next action. Declined, missing, conflicting or
unverified evidence cannot qualify a case update.

This is a technical simulation. Recording the assertion or projecting it into a
fictional case establishes no real responder authority, assignment, notification
or transfer of clinical responsibility.

## Native update and retry

The maintained [builder](../tools/lifecycle/build_selected_ownership_projection.py)
reuses the reviewed authenticated context graph and the existing qualified
connection. An explicit private binding fixes the fictional case identity,
original opaque case token, response identity and existing native destinations.
The builder performs no native I/O and emits a stopped definition. Exact native
identifiers and generated definitions remain outside Git.

The operation serialises its own runs. It creates a before journal without
replacement, then refreshes the case, proposal, response, source and baseline.
The conditional case update serialises the exact journaled patch and changes only
`accountableRole` and `caseStatus`. It uses the fresh, exact original case ETag;
wildcard tokens and automatic retries are absent. Protected case fields and
source/baseline/event identities and tokens are checked again after the write.
Only then is a create-only commit saved.

An identical retry reads the retained commit, verifies its case token and protected
fields against the current case, and checks the current baseline and event tokens.
It returns the original successful run reference without another update or file
creation. An uncommitted journal holds for reconciliation: the flow never assumes
that a timed-out update did not happen. Post-effect failures report unknown effects,
retain their evidence and do not blindly resubmit. The separately maintained
response flow also qualified actual historical assertion replay after this stage
change: the original response returned with zero creates and no progression
granted; changed content under its identity held before creation.

## Bounded native qualification — 18 October 2026

All three entries used the actual selected SharePoint row:

- A stale original-case token held with journal, case update and commit actions
  skipped.
- The accepted profile created its journal, applied one two-field conditional
  update, verified the protected after-state and saved its commit.
- Identical replay returned the original run with all three effect actions skipped.

Independent SharePoint reads confirmed case version 2.0 with only the intended
business fields changed. Proposal and response fields were preserved. The source
bytes retained their original hash, and the saved request retained its identity
and version. Downloaded journal and commit matched their native recorded contents.
The final saved definition matched the frozen candidate and was stopped, with all
qualification runs terminal. The earlier initiation profile remains retained
privately; this qualification reuses its existing flow rather than creating one.

Private evidence: `.local/policy-lifecycle/selected-projection/audit.json` and the
adjacent native action outputs, independent readbacks and original flow profile.

## Remaining limits

This qualifies one supported fictional case/source profile under the current
administrator principal. It does not qualify ordinary-user access, real actor
authority, general source selection or the full operator lifecycle. Positive Declined recording is tracked separately in the event writer's
[response qualification](lifecycle-selected-ownership-response.md). Journal interruption and
post-create uncertainty branches are configured but were not fault injected in
this slice; general native reconciliation remains open. Preserve human edits and
held states rather than inferring a current decision from the latest timestamp.

## Declined-state refusal

A separate fictional occurrence was created through the qualified five-field
initiation form, preserving the accepted occurrence. After its own offer and
explicit Declined response existed, a private qualification binding targeted that
actual case, response and current case token. The selected row, case identity,
source/version/hash, subject role, parent proposal and initial case stage matched.
The response was Declined with open conditions, so the Accepted/None-recorded
requirements refused progression before the journal, case update or commit.

All three effect actions were skipped. Independent reads preserved both the
declined and accepted cases' fields, tokens and modified times, and confirmed that
no test journal or commit file existed. The refusal profile matched native saved
readback and was stopped; the original accepted-case projection profile was then
restored exactly and left stopped. This proves a declined-state refusal, rather
than a wrong-case identity test. Private proof:
`.local/policy-lifecycle/decline-projection-refusal/audit.json`.
