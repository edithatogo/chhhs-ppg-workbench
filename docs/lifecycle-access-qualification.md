# Lifecycle operator access: verified limits and remaining checks

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

A fresh read-only native SharePoint check on 18 October 2026 established that the
currently qualified test principal is a site administrator. Its successful flow
runs, reads and event writes therefore prove this principal's route only. They do
not establish an ordinary operator's or reader's experience.

## Observed configuration

| Target | Native observation | What it proves |
|---|---|---|
| Current principal | Site administrator | Administrator execution/readback only |
| Assurance and Readiness lists | Versioning enabled; inherit site permissions | Versioning is configured; no separate list boundary was observed |
| Site | Separate group bindings include Read, Edit and Full Control | Different role configurations exist; no member's runtime was tested |
| Assurance list | ReadSecurity and WriteSecurity both reported 1 | Exact item-security settings retained; this is not an append-only acceptance result |

All reads returned successfully. No people were enumerated, credentials copied,
users assigned, permissions changed or denial bypassed. Exact native settings,
private bindings and observation times are retained under
`.local/policy-lifecycle/operator-access/`.

Version history alone does not prove that an ordinary user cannot edit/delete an
event or alter an issued document. The append-only recording convention in the
operator guides and the flows' absent-only creates are distinct from SharePoint
permission enforcement. No stronger enforcement claim is made from these reads.

## Concrete remaining acceptance

Use existing authorised identities and existing access, with user-controlled
sign-in where necessary. Do not create an account or change permissions merely to
make a test pass.

1. An existing reader opens the operator entry, retained case, relevant evidence
   and history. Verify the actual recording restriction without changing a record.
2. An existing operator opens the intended native form and records an isolated
   fictional event within its permitted role. Reload the exact stored event.
3. Verify the intended restriction on changing another actor's recorded finding,
   case transition and issued file, using a non-destructive permission check or
   isolated fixture. Administrator success cannot substitute for this check.
4. Check which actor/connection identity is retained by the native flow and event,
   and document its distinction from the asserted assessment/approval actor.
5. Verify native run-only access and document/file access independently. A visible
   shared page or flow link alone proves neither.

The shared integration owner has received this exact limitation and the request
for an existing qualified lower-privilege route. Permission changes, if actually
needed after these checks, require a concrete scoped proposal through that owner.
No extra access workflow or hypothetical licensing requirement is introduced.
Full ordinary-user and lifecycle acceptance remain open.
