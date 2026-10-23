# Selected-case fictional ownership response

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The selected-item flow collects an explicit Accepted or Declined response, unique
response reference, reason, evidence reference and next action. Case, request,
document pins, role and parent offer identity come from authenticated native reads;
the operator cannot override them through this form.

The flow embeds the reviewed selected-case context graph. It derives the offer
reference from the verified saved request and requires exactly one fictional
proposed offer with matching case/document/version/hash, subject role and from-role.
New responses require the case to remain initiated with an unaccepted proposed
role. The flow rechecks source/request/case tokens and brackets the parent with exact
nonempty native item ETags. The only mutation is an appended event in the existing
consultation/handoff list; the case and original proposal are not changed.

One-run concurrency serialises this flow's Find/Create interval. An existing
response permits only the identical response-reference retry. Another response
against that offer holds before the creator; no latest-date selection or implicit
correction can turn conflicting records into accepted ownership. A correction or
new offer requires a separately qualified explicit workflow.

An identical retained response can also be returned after the case advances.
Every payload field except the original occurrence timestamp must match before
this path can bypass the initial-stage restriction. Context, parent, scope,
response-history and fresh-token guards remain required. The receipt labels this
as `historicalReplay`, reports the current initial-stage test separately, and
explicitly grants no progression. A historical receipt cannot authorise another
case update or a new response.

Accepted records an acceptance assertion; Declined records open conditions and a
next action. A matching assertion is not a case projection, authenticated role
authority, assignment, notification or real transfer of responsibility. Uncertain
post-create effects remain unknown and require reconciliation before retry.

The full next action is retained in its multiline field. When it exceeds the
conditions field's 255-character limit, the bounded reason supplies the conditions
note instead. Short-input payloads retain their earlier representation so existing
response identities can still be retried exactly; no text is silently truncated.

## Native input qualification

A write-free probe verified the actual selected-item identity and all five entered
values in the same native execution. The native form requires an object schema
with `properties.rows.items.properties`; the inherited input-free trigger's bare
`rows` schema did not display fields. The probe has no connector or write actions.

Native acceptance recorded one response against the existing fictional offer.
Identical retry returned the same event and original timestamp with zero creates.
A competing Declined response held before the create branch. A qualification
profile substituting a different existing proposal also held before the branch;
its observed case, subject role and parent identity were wrong. The actual parent
offer was not edited. The saved selected case and all operator inputs were real
native form inputs, rather than an API-injected selection.

Independent SharePoint reads verified exactly one response for the offer and
unchanged case fields, ETag and modified time. The accepted profile was restored,
compared with native readback excluding only injected authentication, and stopped.
The private `audit.json` records these bounded results; this is not full lifecycle
acceptance or a case-ownership update.

Maintained builder: [selected response](../tools/lifecycle/build_selected_ownership_response.py).
Private definitions, run/action outputs and independent receipts remain under
`.local/policy-lifecycle/selected-response/`.

## Native retry after case projection

The integration owner separately projected the matching fictional acceptance onto
the case. An actual selected-row retry then returned the original response with
`historicalReplay=true`, initial-stage compatibility false and zero creates. A
changed reason under that same response identity was held before the create branch
on the advanced case. The original event, timestamp and content were preserved.

Independent SharePoint reads verified exactly one response and preserved the
integration owner's projected case fields, ETag and modified time. The updated
profile matched native readback and was stopped. These additional receipts remain
private under `.local/policy-lifecycle/selected-response-retry/audit.json`.

## Native decline recording

A separate operator-created fictional occurrence received one proposed offer and
one explicit Declined response through actual selected-row forms. The response
retained Open conditions and its next action; its case stayed initiated with an
unaccepted role. Identical retry returned the same decline and original timestamp
with zero creates. The case-update owner independently verified that this decline
is held before any journal, conditional case update or commit.

The live conditions field was confirmed as Text with a 255-character limit. Native
output preserved the complete 445-character next action and the separate bounded
84-character reason as its conditions note. A regression run also returned the
earlier accepted response as an unchanged historical retry under this same profile.
Independent reads verified one decline response and the unchanged decline case;
both event flows were stopped and their saved definitions compared with their
qualified candidates. Private evidence: `.local/policy-lifecycle/ownership-decline/audit.json`.

## Remaining boundaries

Ordinary-user access and actual responder authority remain unqualified. Case writes
belong to the [separate projection](lifecycle-selected-ownership-projection.md).
This response profile still uses one fixed fictional source. Explicit corrections,
new proposals after a decline, cross-writer race handling, post-create failure
recovery and the complete operator
cycle remain unqualified. The integration owner retains all case writes.
