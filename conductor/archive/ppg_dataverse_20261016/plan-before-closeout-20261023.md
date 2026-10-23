# Dataverse migration implementation plan

- [~] **DV-01 — Qualify need, scope and target.**
  - User selected full migration proposal. Read-only PAC environment discovery attempted; Conditional Access expiry requires existing-session renewal in @Browser. No target selected or tenant write performed.
- [x] **DV-02 — Prepare inventory and preservation mapping.**
  - Two primary Lists, three event histories, evidence reference fields and technical identity/checkpoint/history exclusions documented. All25 source fields preserved in proposal; no physical table prefix assigned.
- [x] **DV-03 — Implement offline reconciliation and fictional checks.**
  - Duplicate/orphan/schema/count/value/date/identity holds; source and local values preserved. Six focused tests and actual fictional CLI output; no native acceptance.
- [ ] **DV-04 — Qualify solution/schema/security and staged native pilot.**
  - Requires exact environment/solution/publisher, data permissions, licensing/capacity and fictional import/readback/retry/rollback proof.
- [ ] **DV-05 — Reconcile full migration and cutover/recovery plan.**
  - Preserve original operating system; native data/history/file/ACL/flow parity and rollback before scoped cutover decision. No production migration or cutover performed.

## Review — 16 October 2026
Offline increment `a80af0d` reviewed: [report](reviews/20261016.md). No actionable
defects within stated scope. Six focused tests and598 repository checks pass;
all25 source/three event-field mappings and additional case-date drift check verified.
DV-01 target/scope and DV-04/05 native migration/cutover remain incomplete.

## Full proposal — 16 October 2026
[Full proposal](../../../docs/dataverse-migration-proposal.md) covers all workbench
records, events, identity/sync state, retained SharePoint documents/history, access,
workflow parity, staged import, writer transition and rollback preserving new work.
Native scope remains incomplete. CLI profile inventory is cached; live enumeration
failed AADSTS70043. Supported renewal is pending user password entry in @Browser.

## Implementation continuation — 16 October 2026

- Hardened DV-03: populated correction/parent/readiness references must resolve
  within their case, evidence references resolve to catalogue, and duplicate case
  links/JSON keys fail closed. Ten focused tests pass; actual CLI parity passes
  and identical orphan exports fail before writing a report.
- Current managed PAC discovery still fails AADSTS70043; standalone Dataverse CLI
  has no active profile. No authentication change or tenant write attempted.
- Conductor routed read-only candidate inventory to the existing PPG native owner
  through its qualified session. This supersedes repeating expired PAC discovery.
  Candidate inspection does not select a migration destination or authorise import.
- No measured Lists limitation is recorded. The user commission supports a
  fictional comparative technical pilot; the migration benefit remains a hypothesis.
- DV-04/05 remain open. Target/container, capacity/licensing/security, actual native
  import/readback/recovery and full migration parity/cutover remain unqualified.

### Candidate inventory received
Existing PPG owner's current successful reads found no PPG-named solution in the
scoped query and no selected PPG publisher. Own System Administrator/Basic User
roles observed; capacity, region and production entitlement remain unqualified.
[Proposal](../../../docs/dataverse-migration-proposal.md) now records the exact
Developer candidate and a fictional comparative pilot. Exact target confirmation
and a qualified distinct PPG solution/publisher precede native metadata writes.

## Phase: Review Fixes — 16 October 2026
- [x] Task: Apply review suggestions `cc41745` — reject malformed optional
  references and circular histories; preserve valid shared/long histories.
- [x] Task: Verify fixes — 13 focused tests, 160 full-suite tests, 618 setup
  checks; actual CLI valid reconciliation and cycle failure before report creation.
- [ ] Task: Complete DV-01/04/05 native qualification and migration acceptance.
  Exact target decision remains pending; no native write/import/cutover performed.
  [Review report](reviews/20261016-remediation.md) records the open completion gap.
  Archive is authorised only after completion and has not been performed.
