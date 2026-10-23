# Separate assessment of a changed fictional revision

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The second fictional revision has its own native consultation and readiness
history. It uses a different file identity, exact content and SHA256 scope from
the original revision. Its native file version remains 1.0; that does not make it
the first fictional document revision or inherit the original file's findings.

The native flow creates four distinct records: pending consultation, consultation
response, pending readiness and readiness finding. The response references its own
new pending consultation; the finding references its own new pending readiness.
All four retain the second revision's exact scope and explicit fictional markers.
No original event is retargeted, edited or superseded across revisions.

## Native verification

The first native run created and read back all four records. Replay succeeded with
all four create actions skipped. A probe deliberately supplied the original file's
expected token while reading the new file: preflight refused the mismatch and all
four create actions were skipped. Neither source file was modified for the probe.
The accepted definition was restored, compared against native readback (excluding
only injected authentication), and the final stopped state was verified.

Exact identities, source text/hash bindings, native readbacks and terminal run
handles remain private under `.local/policy-lifecycle/lc04-revision-*`, with the
new file's independent proof under `lc04-edition-20261018/replacement-pins.json`.
`tools/lifecycle/build_revision_assessment.py` reproduces the stopped definition
from the qualified connector shapes and explicit private request. It checks the
new text/hash and exact event scope before emitting a definition; it does not
perform native operations.

## Limits and next integration

This is a fixed fictional recording qualification, not actual consultation or a
human readiness judgement. Case/source writes, sending, assignment and real policy
authority remain outside this flow. A replacement decision must select the fresh
readiness finding and match the new revision. Selecting the original readiness
finding for the new revision still needs a dedicated native refusal test at the
decision gate. Replacement and withdrawal each need separately saved, explicit
purpose-specific decisions before the edition lane can record their representations.
General operator selection, ordinary-user access and full lifecycle acceptance
remain open.
