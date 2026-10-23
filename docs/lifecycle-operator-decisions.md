# Native operator decision-outcome pilot

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

The lifecycle now has a native Power Automate run form for recording fictional
rejection, deferral and return-for-change outcomes against the selected, pinned
fictional case. This is an operator-entered pilot, not a general production route.

The form asks for an event reference, outcome, reason, evidence reference and next
action. Native runtime validation rejects unsupported outcomes or missing inputs
before reading the case. It then checks the existing case/source/consultation/
readiness pins, creates or verifies the version-scoped Assurance Event, and rechecks
the case and source. It contains one possible event-create action and no case,
source, publication, notification or assignment action.

## Outcome behaviour

| Operator outcome | Existing stored outcome | Outstanding work |
|---|---|---|
| Rejected | Rejected | Reason and explicit next action retained |
| Deferred | Deferred | Missing evidence and next action retained |
| Return for changes | Deferred | Return disposition retained in title/summary; required revisions retained in next action |

All three retain open conditions and the next action as conditions notes. They do
not advance the case or supersede any earlier decision. The three qualification
records are parallel fictional scenarios, not conflicting real decisions or a new
current-decision selection rule. Do not select a current decision by newest date.

## Native verification on 18 October 2026

All three outcomes were entered and submitted through the actual Power Automate
browser form. Their runs succeeded. Native stored-event readback verified each
outcome, fictional marker, open conditions and nonempty next action. An unsupported
`Approve automatically` input was submitted through the same form; its run failed
at input validation with both case read and event create skipped.

An identical rejection was submitted again through the same native form: it
succeeded with the create action skipped. A changed outcome, reason and next action
under that same event reference failed the retained-event comparison with create
skipped. The complete event readback remained equal to the original in both runs,
including its stored dates and version fields.

The flow was stopped after testing. Native readback confirmed its stopped state
and exact accepted definition, excluding the service-injected authentication member.
Exact bindings, event IDs, timestamps, run/action outputs and stopped definition
remain private under `.local/policy-lifecycle/lc03-operator-*`.

The maintained builder is `tools/lifecycle/build_decision_outcome.py`. It reuses the
previously qualified connector and scope guards from a private definition, requires
an explicitly fictional case binding, and emits a stopped flow definition. It does
not deploy or authenticate. Generated tenant-bound definitions stay outside Git.

## Remaining acceptance

The pilot still pins one fictional case/source and uses the existing connection
owner. Other-case selection, ordinary-user permissions, actor authority and actual
signed evidence are not qualified. Revisions must lead to
new version-scoped consultation/readiness rather than reusing the old findings;
that complete operator cycle remains open. These results do not complete LC03 or
the full lifecycle track.
