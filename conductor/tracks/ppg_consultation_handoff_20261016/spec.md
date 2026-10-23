# Consultation and ownership handoff

Implement a usable native recording route for multiple consultation responses and
explicit ownership handoff assertions linked to an existing case and exact document
version. Reuse Review Queue roles/route/context and the existing evidence library.
A separate event List is justified because each case can have multiple respondents,
responses, conditions and successive proposed/accepted/declined handoffs; one case
field cannot preserve those independent histories.

## Deliverables and acceptance

Record unique EventUID, CaseUID, stable document reference, exact version/hash,
consultation versus ownership-handoff kind, requested/responding or offered/receiving
role, state, actual actor/date, rationale, response/evidence, conditions, next action
and supersession/parent links. Distinguish pending/no-response, responded, proposed, accepted,
declined/withdrawn and explicitly superseded assertions. No response means unknown,
never acceptance. New versions require new records; historical assertions do not
transfer. Corrections retain version history and explicit supersession.

Use native forms, required/choice/unique/validation controls and focused views for
pending responses, unresolved conditions and unaccepted handoffs. Optional local
validation may strengthen cross-record/version checks, never replace a usable native
path. Show native limitations honestly: actor assertions and linked evidence are
human records, not authenticated endorsements. Preserve case/source/importer fields.

Prove fictional consultation, pending and received response, conditions, proposed and
accepted/declined handoffs, old/new version separation, duplicate/repeat safety,
native save/reopen/history and invalid submissions. Verify canonical Start Here
navigation and repeat adoption without unrelated-control changes. Update manifest,
operator instructions and delivery evidence; retain private receipts and clean up
fictional fixtures within tenant retention constraints.

## Boundaries

Recording only: no notifications, invitations, actual role assignment/transfer,
clinical approval, source edits, automatic case-state writes or unattended decisions.
No new flow, custom app, permission/licence changes or third-party processing.
Structured Word generation is preferred if a maintained document is needed; this
increment records structured List events and links existing evidence, so no new
document generator is required. Real consultation and ownership acceptance remain
operational work. Existing IETP content and decisions remain untouched.
