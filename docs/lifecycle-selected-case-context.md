# Native selected-case context

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

An operator can select an actual Review Queue row and open the read-only context
flow through **More → Integrate → Flows**. The native SharePoint selected-item
trigger supplies the item identity. No case reference, target URL, version or hash
is entered by the operator. Microsoft documents that selected-item flows appear
in this menu from the [default environment](https://learn.microsoft.com/en-us/connectors/sharepointonline/#power-automate).
The actual configured menu and row invocation were verified here.

## Context contract

The flow reads the selected item from the fixed existing Review Queue, then:

1. Requires a positive selected native item ID, exact returned-item agreement and
   a supported operator-created fictional CaseUID and a saved-request URL
   within the existing same-site template folder and expected request-file prefix.
   Unknown/legacy baselines and path/query overrides are held before file reads.
2. Reads saved-request metadata/content/metadata. Checks its kind, schema,
   qualification flag, derived occurrence/CaseUID, exact request-file reference,
   linked DocumentUID and already-qualified source reference/version/hash. Baseline
   ETags must be nonempty/nonwildcard; UniqueIds must be nonempty and exactly stable
   across before, after and final metadata reads. Missing tokens cannot compare equal.
3. Reads that fixed qualified source's metadata/content/metadata and compares exact
   text, observed native source identity and exact version tokens. This is not a generic Office extractor or native
   hash service.
4. Rechecks the selected case's exact connector header ETag and the saved request.
   It emits a native read-only context with identity, occurrence, document scope,
   source pins, baseline UniqueId, opaque tokens, observation time and explicit limits.

A valid context does not establish accepted ownership, readiness, approval or actor
authority. The qualified operator-created case still has an unaccepted proposed
role. Context resolution deliberately does not turn that proposal into acceptance.
Unknown, mismatched, changed or unreadable bindings return an explicit held result;
there is no fallback lookup, broader search, source override or write action.

## Native verification on 18 October 2026

- The actual selected-row input check succeeded and received the selected native
  item identity through the SharePoint trigger.
- The complete context flow ran from the operator-created case row. Case, saved
  request, occurrence, linked source and before/after checks passed; the native
  context retained exact opaque tokens and no authority inference.
- Selecting the older fictional case returned an unsupported-baseline hold. Saved
  request and source reads were skipped; the selected case was not changed.
- A deliberately stale expected source token returned a source/version hold and
  skipped valid-context emission. The actual source file was not changed.
- The reviewed definition passed a fresh positive run, returning matching selected
  and observed item IDs plus the saved request's stable file identity.
- Separate native fault profiles omitted the saved request's ETag or UniqueId;
  each returned a hold rather than accepting equal missing values.
- A read-only replacement simulation returned a different existing file's metadata
  on the second request-metadata read. Its identity mismatch held before source
  reads. No file was actually replaced.
- Selecting the older row while a fault profile returned the newer row held on
  selected-item mismatch, before any saved-request or source read.
- A synthetic two-document link projection held before source reads. This proves
  the native ambiguity predicate; it does not claim that a real case's links were
  changed or that ordinary-user editing was tested.
- The accepted context definition was restored and compared with native readback,
  excluding only platform-injected authentication. Final state was Stopped.

The flow contains nine native SharePoint GET actions and no native mutation action.
Exact trigger/designer observations, definitions, input/output, runs and receipts
remain private under `.local/policy-lifecycle/selected-context/`.
`reviewed-qualification-audit.json` retains the corrected positive and five focused
hold results, the exact restored candidate checksum and stopped-state readback.
`tools/lifecycle/build_selected_case_context.py` reproduces the stopped definition
from the observed trigger and explicit private binding; it does not deploy.

The embedded run frame was loaded while the browser accessibility snapshot still
showed a spinner. Inspecting that rendered frame and clicking its visible Run
button verified the actual Lists route. Native run history and output, rather
than the click alone, prove execution.

## Remaining integration

This resolves multiple possible operator-created fictional occurrences against one
qualified source profile. Only the current administrator was tested. Ordinary-user
run-only access and connection/caller boundaries remain unqualified; no sharing,
permissions, people or authentication changes were made.

Event entry must obtain and revalidate native context within its own authenticated
execution; an operator-pasted context object is not trusted evidence. It must
separately check actual matching
ownership and stage evidence before any event/case effect. Consumers must recheck
its case/source tokens before acting. Unknown legacy cases remain held until their
binding is explicitly qualified. General production source selection, editable
preparation, closure, recovery and the full connected lifecycle remain open.
