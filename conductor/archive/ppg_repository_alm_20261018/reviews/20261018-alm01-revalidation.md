# Review Report: ALM-01 enforced Gitleaks and publication checks

## Summary

Local ALM-01 implementation is complete and revalidated after historical cleanup;
remote publication and GitHub-hosted enforcement remain separate release work.

## Verification Checks

- [x] **Plan Compliance**: Yes for selected ALM-01 — staged/index, history, actual push refs, private destination/content-review binding, hooks, publisher and CI configuration reviewed. Other ALM tasks remain open.
- [x] **Style Compliance**: Pass — established Python/JSON/shell; existing project workflow and minimal code conventions retained.
- [x] **New Tests**: No new code behaviour introduced; reused 30 existing publication integration/regression tests.
- [x] **Test Coverage**: Yes for local controls; synthetic secret/binding rejection, exact exceptions, metadata transport bounds and publisher contracts. Hosted GitHub acceptance is unperformed.
- [x] **Test Results**: Passed — all 30 tests; full-history gate passed with 491 files and Gitleaks 8.30.1. Local hooksPath read back as `.githooks`.

## Findings

### Low — fixed: stale Conductor publication hold

- **File**: `conductor/tracks/ppg_repository_alm_20261018/metadata.json`
- **Context**: Metadata still described the 24 historical bindings as an active block, contradicting the completed remediation and fresh passing scan. Following that instruction would unnecessarily stop further development.
- **Fix applied**: Replaced the obsolete hold with passing history status; separated ALM-01 completion from ALM-04 private-destination/content-review/hosted-release checks. Updated implementation identities after history remapping, linked this report, and retained the original review with a current-status pointer.

## Review scope and evidence

Inspected current `scripts/check_publication.py`, `scripts/publish_github.py`,
`scripts/install_publication_hooks.py`, both hooks, detector/exception policy,
`.github/workflows/publication-checks.yml` and `tests/test_publication_checks.py`.
Existing implementation identities are `a593837`, `182d34a` and `2e36a92` after
history remapping; no security implementation change was necessary in this pass.

The gate rejects staged content hidden by unstaged replacements, deleted historical
findings, unsafe/private paths and unsupported objects. It requires the pinned
scanner, retains default detectors, disables inline suppression and rejects
incomplete history scans. Review receipts bind commit/tree/history/policy/repository;
the publisher verifies the actual single push URL and pins the reviewed commit
without force. File-backed bounded Git metadata transport preserves the prior
real-hook deadlock repair. CI has full-history checkout, pinned actions/checksum,
read-only permissions and no persisted checkout credentials or uploaded reports.

Private revalidation receipts: `.local/alm01-revalidation-20261018/`. The local
history gate passing does not attest that every confidential-content category has
been manually reviewed. No review receipt was fabricated, no remote configured,
no upload made and no clinical/operator decision performed. Existing recovery
bundles and old objects remain private; do not publish or restore contaminated refs.

No unresolved implementation defect was identified. Preserve the broad ALM track
in progress for other tasks; do not archive or mark it fully accepted from ALM-01.

## Publisher route verification

The real `publish_github.py --dry-run` passed in an isolated clean clone after
removing the clone's local-source origin. The first attempt correctly refused
that unintended local destination; no external operation was attempted. The
successful dry-run performed the real history gate and repository setup checks:
999 passed, zero failed, one expected unmaterialised Conductor checkout pending.
It made no GitHub, authentication, creation or push call. The shared working copy
contains another writer's context edits; those are excluded and preserved.

### Low — fixed during final verification: core-context size

The expanded handoff exceeded the committed core-context word budget. Replaced
the duplicated handoff section with one compact current-status link; detailed
evidence remains in this report and the track plan. Other writers' context files
remain untouched.
