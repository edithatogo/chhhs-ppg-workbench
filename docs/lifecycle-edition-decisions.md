# Native fictional replacement and withdrawal decisions

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Two distinct native Assurance Decision records now represent separate fictional
purposes. The replacement decision is scoped to the second revision and references
its fresh readiness finding. The withdrawal decision is scoped to the original
revision and its issued representation; it does not borrow the earlier approval
or readiness as withdrawal authority.

Each record retains a purpose-specific title, rationale and decision reference.
The existing NextAction note contains structured purpose evidence for this bounded
technical profile. For replacement it records `purpose: replace`, exact original
`retainedSubject` pins and exact new `replacement` pins. For withdrawal it records
`purpose: withdraw`, exact original pins and the original `issuedReference`.
These are technical qualification records, not real delegated authorisations.
The note is not presented as a prose next-action instruction by this profile.

## Native checks and observed results

The flow reads the new revision, selected consultation response and readiness
finding, retained original source and stable case. It compares exact scopes,
source bytes and before/after tokens. Both events are verified after create or
retained-record lookup; final guards recheck the case and both sources.

Before any intended decision creation, the old readiness finding was deliberately
selected against the new revision. Native preflight refused it and both create
actions were skipped. With the fresh new-revision finding selected, both distinct
decisions were created and read back. Replay succeeded with both creates skipped
and the complete original event readbacks unchanged. The final stopped state and
accepted definition were verified, excluding only platform-injected authentication.

Exact private request bindings, negative/positive/replay runs and event readbacks
are under `.local/policy-lifecycle/lc04-edition-decisions-*`.
`tools/lifecycle/build_edition_decisions.py` reproduces this stopped definition and
rejects mismatched scope, missing structured predecessor evidence, borrowed
readiness or a withdrawal carrying the original readiness as its authority. It
performs no native operations. These local refusal checks supplement the native
cross-revision refusal test; they do not replace it.

## Consumer handoff and limits

The edition lane must create and verify the second revision's own fictional issued
representation and publication event before accepting a replacement relationship.
It must retain original issued history and use the separate withdrawal-purpose
decision for its isolated withdrawal scenario. These scenarios do not remove a
real policy, alter the authoritative clinical publisher or set real current flags.

This fixed profile has no case/source/issued-file writes, assignments, notifications
or access changes. Actual authority, signatures, ordinary-user permissions,
general operator selection and complete lifecycle acceptance remain open.
