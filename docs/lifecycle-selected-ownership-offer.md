# Selected-case fictional ownership offer

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

## Contract

This consumer embeds the reviewed selected-case context graph inside its own
Microsoft-authenticated native execution. It does not consume operator-pasted
context, case IDs, target URLs, document versions or hashes. Its only possible
runtime mutation is a new proposed ownership event in the existing consultation/
handoff List. Case, source, request, publication, people and notification writes
are absent.

The operator selects a supported fictional occurrence in the Review Queue and
chooses the ownership-offer flow. The existing saved request supplies the proposed
role and deterministic request/occurrence identity; no responsibility is accepted
merely by selecting the row or recording the proposal.

Before the event effect, the flow requires:

- Valid current case/request/source context with exact selected-item agreement,
  bracketed file identity/version and captured source scope.
- An initiated fictional case whose local role remains explicitly UNACCEPTED and
  matches the saved request's proposed fictional role.
- Fresh unchanged case, source and baseline identity/version tokens immediately
  before the create-or-replay branch.

The proposed event retains exact case/document/version/hash, baseline evidence,
selected native item reference and request-derived event identity. The event is
FictionalTest=true, Ownership handoff/Proposed, with simulated actor/from-role text.
It creates no people, assignment or acceptance. Its next action calls for a separate
explicit acceptance or decline against the offer.

One-run concurrency serialises this flow's own Find/Create interval. Existing
matching events are read and verified; duplicates or changed payloads are held
without overwrite. OccurredOn is retained on replay rather than replaced with a
new time. Case/source/baseline are rechecked after event readback.

## Uncertain effects

An error or timeout after a possible create cannot truthfully establish no effect.
The catch-all reports offerRecorded=null and eventWriteCount=null, with an explicit
reconcile-before-retry state. If an event was verified and context subsequently
drifted, it is retained but qualification is false. Only before-write holds report
zero attempted effects. Nothing blindly retries or deletes an uncertain event.

## Maintained source and evidence

[The builder](../tools/lifecycle/build_selected_ownership_offer.py) consumes the
private approved context-definition digest, target reference and event-list
binding. It refuses an unreviewed context or a changed connection, emits a stopped
selected-item definition and performs no native I/O. Exact bindings and generated
definitions remain under `.local/policy-lifecycle/selected-offer/`.

Native qualification on 18 October 2026 used the actual Lists-selected operator
occurrence. The first run created one proposed event; identical replay created
zero and preserved the original event, including its recorded date. Selecting an
unsupported legacy occurrence held before creation. Independent reads confirmed
exactly one matching event and an unchanged case, with its role still UNACCEPTED.
Source and saved request were unchanged. The final native definition matched the
frozen candidate and was Stopped; no run remains pending.

Private native receipts are retained in
`.local/policy-lifecycle/selected-ownership-offer/audit.json`; builder inputs remain
in the separate `selected-offer` directory. The producer's reviewed cases were
reused. Post-create uncertainty paths are configured, but were not native fault
injected and are not claimed as qualified recovery.

## Remaining boundary

This is a bounded fictional known-source path. Accepted ownership and corresponding
case projection are separate work. Ordinary-user access, caller/connection rights,
general production source selection, stronger audit permissions and the complete
operator lifecycle remain unqualified. Site-administrator testing does not clear
those requirements. No clinical review or policy authority is inferred.
