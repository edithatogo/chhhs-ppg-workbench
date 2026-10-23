# Native lifecycle initiation, ownership and recovery qualification

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Fixed fictional occurrences ran within M365 using the existing standard SharePoint
connection and an isolated manual, serial flow. This qualifies bounded native
plumbing; general operator delivery, real assignment and full lifecycle acceptance
remain open. The owned flow was returned to Stopped with its saved definition
verified. No real case/catalogue, source, permissions or connections changed.

## Current scope reconciliation — 23 October 2026

The initial qualification below is historical. General two-source entry and two
configured fictional cycles later qualified; see the [current closeout](lifecycle-closeout-20261023.md).
Earlier open statements are not instructions to rerun those completed slices.
Uncovered recovery/edition controls and operational authority remain separate.

## Initiation and ownership

- Synthetic CaseUID `LC-FICTIONAL-20261017-01` and occurrence
  `fictional://ppg-lifecycle/20261017/occurrence-01` were initiated once; native replay
  retained the same case with createdCount0.
- A separate187byte fictional source was independently downloaded and byte/hash
  verified. Runtime checks exact text and its native metadata ETag. Exact native
  identity, version and hash pins remain in private evidence.
- Stale-token refusal skipped all event/case mutations. Connector response headers
  provide the exact CAS token; CLI metadata is not interchangeable.
- Fictional proposal and acceptance events bound the case/source/version/hash,
  matching roles and parent chain. Conditional case mutation and semantic native
  readback verified the accepted fictional role and case state.
- Native receipt persisted after readback. Replay checked the unchanged case token
  and role, returned the retained receipt exactly and skipped all mutation actions.
  Actor authority remains unqualified; realPolicyEffects=false.

## Changed request and interrupted-write recovery — 18 October 2026

A native control-file read compares the complete frozen fictional request before
any effects. Journal-before-write, exact-token CAS, durable after-state proof and
a commit-last receipt protect the qualified recovery window.

- Changed next action under the same request identity was refused before case read;
  all writes skipped. Original control content was restored with native history retained.
- Injected interruption saved a prepared journal, performed one nextAction-only case
  write, verified the after-state and saved its proof, then failed before the final
  receipt. Independent library read verified journal/proof present and receipt absent.
- Recovery matched native request/journal/source/current-case pins to that proof.
  The completed case write and journal/proof creation were skipped. The receipt
  retained the original interrupted run identity; caseWritesThisRun=0.
- Committed replay returned the exact retained receipt with every write skipped.

Only the fictional nextAction changed; its native case version advanced2.0→3.0.
Owner, status, target date, identities, baseline and other local fields were unchanged.
Independent source download matched the original bytes/hash. No event, catalogue,
source, notification, access or authentication writes occurred. Final flow was
Stopped, fault injection disabled. Original ownership evidence was preserved.

## Maintained source and private bindings

[The recovery builder](../tools/lifecycle/build_recovery_qualification.py) consumes
an explicit private qualification binding through `--binding`, a private request,
the existing qualified reference-flow snapshot and the fictional source text. It
requires the frozen request and native target to match that binding; it performs
no native I/O. The private binding is retained beside the original recovery audit
at `.local/policy-lifecycle/recovery/qualification-binding.json`.

[Request example](../templates/lifecycle/recovery-qualification-request.json),
[initiation example](../templates/lifecycle/native-initiation-qualification.json) and
[ownership example](../templates/lifecycle/native-ownership-qualification.json) are
unbound examples with private-value placeholders. They are not deployable native
fixtures or production deployment packages. Exact definitions, operational IDs,
bindings, run handles and receipts remain under `.local/policy-lifecycle/`; the
original recovery proof is pinned by `.local/policy-lifecycle/recovery/audit.json`.

The source/prose privacy correction reproduced the accepted private definition
exactly, without redeployment or another native run. Original audits/history remain intact.

## Remaining acceptance and ownership

Recovery is qualified after durable after-proof and before final receipt. A crash
between case mutation and saving that proof still fails closed and needs
reconciliation; automatic recovery in that gap is unqualified. General initiation/
ownership, ordinary-user operator/access and full lifecycle remain open. Production
generation, controlled publication and operative policy-source conflicts remain open.

Workbench retains case/request/shared integration. Other lanes own only their
explicitly handed-off fictional event records and separate flows; they preserve
the case, source, ownership evidence and stopped Workbench flow.

## Read-only uncertain-write classification

[The reconciliation checker](../tools/lifecycle/reconcile_uncertain_write.py) applies
the conservative unknown-save pattern: inspect the original request/journal, exact
native run/action inputs and acknowledgement, current protected fields and native
history; never resubmit an uncertain write. It is developer evidence tooling with
local inputs/output, not a deployed M365 classifier or automatic recovery workflow.

One existing interrupted write was classified `committed-no-resubmit` without using
its after-proof: the attributable native action succeeded with204, its exact URI/
CAS/body matched the prepared request, current state matched the intended change
and preserved other protected fields, native history retained both versions and
source pins matched. A fresh REST/history read corroborated the retained connector
observation without normalising different ETag formats. No new native trial or
write was induced. Five synthetic missing-acknowledgement/attribution/drift checks
held; the not-applied classification has no additional native qualification.

Private `.local/policy-lifecycle/recovery/reconciliation/` retains the evidence
bundle, result, audit and usable manual-continuation instructions. The existing
committed receipt remains untouched. Ambiguity stays held; missing-receipt follow-up
requires a separately guarded continuation and cannot replay the mutation or
manufacture proof. Native general operator reconciliation remains open.
