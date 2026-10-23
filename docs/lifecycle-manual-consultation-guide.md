# Manual consultation entry — fictional qualification

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

18 October 2026. The existing first-party request and response forms have been
used with fictional cases and verified edited Word revisions. Native recording,
identical retries and version-specific technical coverage passed within that
bounded qualification. Ordinary-user access and real reviewer authority remain
unverified. Use fictional qualification material until operational acceptance.

The form records a consultation request or response about one verified prepared
document revision. It sends no invitations or notifications, assigns no reviewer,
and supplies no content-readiness judgement or policy approval.

## Before entry

Have the case reference, intended prepared draft and supporting evidence available.
The case reference is only a lookup key. Entering it does not establish identity,
ownership, permission or authority, and it does not select a trustworthy document
version by itself. The system must resolve the case and verify its linked prepared
draft, original source, template and technical qualification receipt.

Use the case's prepared draft for consultation. Do not substitute an original
source document or the earlier version simply because it opens. A prepared draft
can be technically usable while its content remains unreviewed.

## Choose the action

| Intended work | Action to choose | What it records |
|---|---|---|
| Record the consultation request for the verified draft | Consultation request | A pending request for that exact prepared revision and the configured fictional role |
| Record an explicit response or its absence | Consultation response | A response linked to that revision's verified request |

The existing forms also support ownership actions. An ownership response and a
consultation response are different records; select the action deliberately.
The consultation request's role and document context come from verified records,
rather than a newly invented assignment. Recording a request does not contact
that role or prove that a person has agreed to review it.

## Response fields

The native seven-field response form uses the labels below. The same form serves
ownership and consultation, so check both Action and Case reference before
submission. If its fields differ or the retained result resolves another case or
revision, stop and reconcile the mismatch before further submissions.

| Field | What to enter |
|---|---|
| Case reference | The existing case lookup reference, checked against the intended case |
| Action | Consultation response |
| Response reference | One unique consultation-response reference, beginning `LC-CONSULT-RESP-`; keep the same reference for an identical retry |
| Response / outcome | Exactly one of Responded, Unanswered, Declined or Conditional |
| Reason / finding | A factual account of the response, missing response or outstanding conditions |
| Evidence reference | The retained evidence supporting that account; a reference does not itself prove that the evidence is adequate |
| Next action | The actual remaining step, including unresolved conditions where relevant; no automatic assignment follows |

The current recording contract requires every response field. Keep the response
reference within 80 characters and use a simple reference without spaces or URL
punctuation. Finding and evidence reference each allow up to 255 characters; next
action allows up to 2,000. Preserve the full next action instead of shortening
away an unresolved condition. Missing evidence is not a reason to invent evidence
or an approval; leave the operation held and resolve the missing information.

## Choose the outcome accurately

| Outcome | Meaning for recording | Effect on technical coverage |
|---|---|---|
| Responded | An explicit response is recorded with no outstanding conditions asserted in this entry | May satisfy the response part of coverage after the request, evidence, history and revision checks pass |
| Unanswered | No response has been received; describe the absence and remaining action | Remains pending with open work |
| Declined | The response explicitly declines; preserve the reason and evidence | Remains incomplete with open work |
| Conditional | A response exists but conditions or work remain unresolved | Remains incomplete with open conditions |

Responded is not a synonym for agreement, content readiness or approval. Do not
choose it to hide unresolved conditions. Conditional may appear in underlying
records as a responded entry with open conditions; those conditions still prevent
coverage completion. Unanswered remains pending rather than becoming a completed
response merely because an entry was saved.

## After submission

Inspect the actual retained result for the intended case and exact prepared
revision. A successful run alone is insufficient. The system must verify the
saved event and recheck the case, source, baseline, prepared file, template,
technical receipt and relevant request/response history.

An exact retry should preserve the original record and create no duplicate. Keep
the reference and all response details unchanged. A changed response under the
same reference, a competing reference for the same request, duplicate history,
missing parent request or uncertain readback requires reconciliation. Do not
choose the most recent date, delete earlier evidence or keep resubmitting until
the display turns green.

If the draft changes, the earlier response stays with its original revision. It
does not automatically apply to the edited version. A stale or mismatched context
must hold the operation. If an event may have been retained before a failure or
context change, preserve it and inspect the actual record before retrying; do not
assume that nothing was written.

## Coverage and later decisions

Technical coverage asks whether each required role has one matching request and
one supported response for the same prepared revision, with complete evidence,
closed conditions and a consistent history. Unanswered, declined, conditional,
duplicate, conflicting or incomplete histories keep coverage open. Uncertain or
partial history is unknown, not complete.

Coverage does not assess content, validate reviewer authority or capacity, approve
a policy, publish it or permit progression. Human readiness and approval remain
separate later activities, supported by the retained evidence.

Maintained implementation context: [coexisting event routes](lifecycle-coexisting-event-routes.md),
[consultation recording](../tools/lifecycle/build_prepared_consultation_events.py)
and [coverage checks](../tools/lifecycle/build_consultation_coverage.py).
The latest fictional occurrence retained one request and one response against its
own edited revision. Identical repeats created zero records and preserved original
dates and payloads. A changed finding under the retained response reference was
held: its creator skipped, and independent full-history readback confirmed the
original response and all earlier records remained unchanged. The held runtime
receipt itself reported an uncertain effect state; independent reconciliation,
rather than the successful run status alone, established preservation.

Both event flows were read back with their exact definitions and connections and
stopped after qualification. Technical consultation coverage does not establish
that a readiness finding has been recorded. The separate fictional readiness entry
was subsequently retained once through the reviewed existing CLI route, after the
push subscription expired and fresh identity, history and file checks passed. A
guard prevented repeated mutation sends and redirects. Actual native readback
verified every field, the stored DateOnly value and fictional marker; the saved
display form was reopened without editing. Original readiness rows and supporting
records were preserved. No subscription or notification settings were changed.
The case-work owner's read-only readiness consumer and later decisions remain
separate steps; this technical finding asserts no substantive content assessment.
