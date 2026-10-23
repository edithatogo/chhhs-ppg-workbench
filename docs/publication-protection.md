# Publication protection — ALM-01

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

## What is enforced locally

`check_publication.py` uses Gitleaks 8.30.1 with the default detectors plus selected
operational tenant/account rules. The executable version is checked before use.
Missing scanner/policy, findings, invalid reports, shallow history, Git read errors,
unsupported Git entries and an incomplete history scan refuse the operation.
Git metadata requests are chunked, use file-backed input/output rather than
simultaneously written pipes, and Git object reads have30-second bounds.
Process samples from a recurrent hook stall showed both Python and Git blocked
writing pipes despite the earlier chunking fix; the equivalent file-backed
metadata read completed normally. The bounded-stream regression and actual
pre-commit readback cover this boundary without disabling the publication check.
Console output gives counts/codes; failed redacted reports stay under ignored
`.local/publication-checks/`. Raw detector output is not printed or uploaded.

- Pre-commit scans the complete staged files from Git's index, including staged
  content concealed by an unstaged clean replacement. Untracked local material
  is outside the proposed commit and is not scanned.
- Pre-push scans every reachable local history and the actual supplied push
  commits, including a commit that is no longer on a branch. It also checks the
  current tree, a private confidential-content review receipt and the exact
  destination's private status through `gh repo view`.
- The publishing script runs the full scan before any GitHub command. Actual
  publication requires a clean tree and an exact content-review receipt, verifies
  private destination/account and the actual sole push URL, rechecks HEAD and pushes its reviewed commit
  explicitly without force. Its hook receives the same receipt path.
- CI is configured for push, pull requests and manual execution with full history,
  read-only repository permission, independent verification steps, no persisted checkout credentials, SHA-pinned
  actions and a checksum-verified Gitleaks download. It runs the same history gate
  and focused integration tests. No scan report is uploaded as a CI artefact.

The path gate rejects private directories, environment files, operational document
and credential-file types, unsafe/symlink entries, unexpected submodules and
non-text/binary tracked files. Deleted private paths are also rejected in history.
The existing pinned Conductor gitlink is retained; no submodule content is exported
or silently treated as first-party reviewed source.

## Dataverse and native identifier coverage — 23 October 2026

The extended policy also rejects native Dataverse environment URLs and UUIDs next
to selected operational identity labels (environment, native flow/action/case/record,
source identity, UniqueId, list binding and ETag). These are repository privacy
rules, not a claim that such identifiers are authentication secrets. Public
specification UUIDs without operational labels and private-binding placeholders
remain usable. Context-labelled fictional UUIDs are findings unless they match the reviewed
exact synthetic values in the specifically named fixture files. Other UUIDs in
those same files, and the same synthetic values at unreviewed paths, still fail.
Do not exempt entire test directories or rules.

Regression checks prove rejection of deleted historical URLs/IDs, staged native
identity fields hidden by an unstaged clean replacement, and values/paths outside
the narrow synthetic exception. Default
secret rules, exact digest exceptions and confidential-content review remain active.
The expanded real-history scan now refuses publication. Historical passing scans
used narrower detectors and do not establish that this history is publication-safe.

Gitleaks blocks upload through the installed local hook/publisher; it does not
redact Git objects, remove existing history or catch every identifier or confidential
passage. CI runs after upload. Resolve findings in a separately retained sanitised
publication history, review it, then scan that exact history before publishing.
The original repository and unrelated working changes must remain recoverable.
Six current documentation/metadata files now use private-binding references in
place of the confirmed native values; original objects remain recoverable in the
retained local history. Runtime definitions and safety guards were not changed.
No history rewrite or upload was performed by this policy extension.

## Activate and use

From the project root, with the documented project Python and Gitleaks installed:

```sh
.venv/bin/python scripts/install_publication_hooks.py
.venv/bin/python scripts/check_publication.py --mode staged
.venv/bin/python scripts/check_publication.py --mode history
.venv/bin/python -m unittest discover -s tests -p 'test_publication_checks.py'
```

The installer sets repository-local `core.hooksPath=.githooks`, verifies the saved
value, and refuses to replace existing custom hooks/configuration. Existing hooks
must be explicitly integrated rather than overwritten. Each clone needs activation.
Local hooks can be deliberately bypassed by a Git user; this is not a server-side
security boundary. CI runs after upload and cannot prevent the initial upload.
GitHub rulesets/required checks remain unverified until the intended private remote
is available in ALM-04. No GitHub policy or remote is created by hook installation.

## Reviewed exceptions

[The configuration](../.gitleaks.toml) extends all default rules. A rule-specific
AND exception permits only the exact fictional `exceptionKey` digest on the exact
JSON line in the two identity-resolution fixtures. No complete file/rule is excluded;
another synthetic credential in either file is still rejected. Moving the fixture
to another directory loses the exception. Inline allow comments are disabled.

[The fingerprint list](../.gitleaksignore) contains one exact historical prose-only
finding from the binary-publication guide. Current wording uses opaque ETags and
avoids that false positive. No whole commit or path is ignored. Every new exception
requires exact-content review and a scoped negative check.

## Confidential-content review before publication

Gitleaks and the path rules do not establish that policy text, personal information
or every operational identifier is safe to publish. Before an actual push, review
all reachable history and the current tracked tree for those content classes.
Keep that review record private. It is a publication-content check, not clinical
approval or a transfer of authority. Do not mark it complete from a scanner result.

The JSON receipt at `.local/publication-review.json` must contain:

| Field | Required value |
|---|---|
| schemaVersion | 1 |
| scope | all-reachable-history-and-head |
| reviewedCommit | Exact reviewed HEAD from git rev-parse |
| reviewedTree | Exact reviewed HEAD tree |
| historySHA256 | `history_hash(ROOT)` from the gate module |
| policySHA256 | `policy_hash(ROOT)` from the gate module |
| repository | Exact intended owner/repository |
| reviewer | Actual reviewer identifier; keep private |
| reviewedAtUtc | Actual completed review timestamp with timezone, not in the future |
| confidentialContentReviewed | Boolean true only after actual review |

New commits, newly reachable branch history, policy changes or a different
destination invalidate the receipt. Symlinked or nonprivate receipt files are
refused. The gate does not manufacture review findings or attest to uninspected
content. A receipt is an attestation, not cryptographic proof of review.

After all findings have been resolved and the actual review is recorded, the
existing publication route is:

```sh
.venv/bin/python scripts/publish_github.py --repo edithatogo/chhhs-ppg-workbench --content-review .local/publication-review.json
```

For a verified existing matching origin use its documented `--resume` option.
For an ordinary `git push`, the hook uses `.local/publication-review.json` by default;
`PPG_CONTENT_REVIEW` can name another reviewed private receipt. Only supported
GitHub HTTPS/SSH remote forms are accepted, and an unverified/public destination
is refused. A dry run also scans history but performs no GitHub operation.

## Actual qualification and remaining publication restriction

The 24 historical operational SharePoint-binding findings were resolved on
18 October 2026 by sanitising two historical fixture blobs. All 397 commits were
retained; 164 descendant commit identities changed. The current implementation
source tree was identical before/after the historical transformation. Only those
two fixture paths changed across the mapped historical trees. The existing exact
prose exception fingerprint was remapped to its new commit identity without
broadening its file/rule/line scope. No operational-binding exception was added.

The candidate full-history gate passed with Gitleaks 8.30.1 and 491 current files;
30 publication regression tests passed. The adopted branch also passed the full-history gate after integration. A private verified original-history bundle, commit map, transformation
and receipts are retained under `.local/history-remediation-20261018/`. There is
no backup ref pointing to unsanitised history in the active repository. Original
objects/reflogs may remain locally for recovery; these are not sanitised exports.
Do not upload the private bundle or restore old refs into a publication candidate.
Historical commit references in older documentation identify the pre-remediation
history; use the private map or recovery bundle when resolving them.

This is repository release maintenance, independent of policy-review operations.
It does not require clinical assignment/date decisions or tenant administration.
No source, native object, permissions, credentials or clinical content was changed.
Other uncommitted work is preserved. No remote, actual upload, history force-push
or credential rotation is performed. ALM-04 still requires private destination,
content review and hosted enforcement verification before publication.

The integration suite uses disposable repositories, synthetic credentials and
mocked GitHub calls. It exercises staged/index mismatch, historical/deleted findings,
private paths/binary/symlink refusal, missing/wrong scanner, exact fixture exceptions,
inline-ignore refusal, shallow/incomplete history, receipt invalidation, existing
hook preservation and actual hook execution. Destination privacy and reviewed-commit
push contracts are checked without an external push. CI is configured, not observed
running on GitHub; hosted enforcement stays with ALM-04.

## Explicit public visibility — 23 October 2026

The user subsequently authorised making this sanitised repository public.
Private remains the publisher's default. Public publishing requires
`--visibility public` and a genuine exact-scope receipt with `visibility: public`.
Legacy receipts without that field apply only to private publication. Changing
visibility invalidates the applicable receipt; content/history/policy/destination
bindings, scanners, private receipt storage and exact-commit non-force push remain
required. The hook receives the same visibility through
`PPG_PUBLICATION_VISIBILITY`; a mismatch with the receipt or actual remote refuses.
The publisher does not silently change an existing repository's visibility.

```sh
.venv/bin/python scripts/publish_github.py --resume --visibility public --content-review .local/publication-review.json
```

The visibility change applies only to the separate reviewed publication copy.
The original checkout/history, operational evidence and uncommitted work remain
local. Public source is not clinical publication, a public licence grant or native
production acceptance. Older private-only qualification sections retain their
historical scope and are superseded for this expressly authorised destination.
