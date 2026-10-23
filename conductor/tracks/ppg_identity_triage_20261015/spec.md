# Guided identity-exception resolution

Provide a usable operator path from a held source record to an evidenced identity-resolution proposal. Beneficiary: the operator maintaining source reconciliation. Prefer a report and existing List/form over a new app. The real hold motivates the feature, but technical demonstration uses fictional data unless a responsible operator supplies a real resolution.

The subsequent IR-08 instruction extends delivery through native application.
That route is qualified; the earlier proposal-only fallback below is historical.
Actual real-record decisions remain excluded.

## Contract and deliverables

Read existing failed-run evidence, raw snapshot, candidate, frozen identity contract and successful checkpoint using private bindings. Display source-qualified aliases, relevant record values, snapshot hash/version and possible matches; record ambiguity instead of guessing. Row number/title/version-bearing code must never become permanent identity.

A resolution proposal records exception key, source fingerprint, contract hash, proposed existing UID or request for a new UID, rationale, supporting references, operator decision and status. Keep proposed, accepted, applied, verified and rejected separate. Do not copy operational values into Git. Reuse evidence files or a minimal List only if required for usable operation.

An operator can prepare/export a proposal without changing the ledger. Any later application requires an explicit recorded identity decision, current source/contract preconditions and the existing integration/importer ownership handoff. Reuse guarded serial reconciliation with readback and commit-last checkpoint; never introduce a second importer. Reject stale/ambiguous proposals, duplicate aliases and UID collisions before any write. If the current importer cannot safely consume an amendment, stop at a usable reviewed proposal and name the exact missing apply step; do not claim end-to-end application complete.

## Acceptance

A fictional unknown record produces a traceable proposal; conflicting/stale/duplicate proposals cannot write. A valid fictional resolution is reconciled through the supported path with readback. Replay is idempotent, local case fields survive, and failed/readback-mismatched writes retain the last good checkpoint. UI/report exposes unresolved state and next action. Register the capability and canonical link only at its evidenced lifecycle. Capture local and native results separately.

## Exclusions

No unattended UID minting, blanket baseline/count extension, missing-row retirement, source-register edits, actual business identity decisions, permissions, notifications, new runtime, or broad importer rewrite. Real exception resolution remains operator work supported by this system.
