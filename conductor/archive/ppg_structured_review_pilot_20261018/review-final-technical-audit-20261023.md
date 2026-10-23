# Review Report: Structured discharge-summary pilot — final technical audit

## Summary

Historical manual/web implementation and its scoped fixes are reviewed and preserved; current-authority/template reconciliation remains incomplete, and third-party review is transferred rather than passed. Track remains archived with full acceptance false.

## Verification Checks

- [x] **Plan Compliance**: Partial overall — every original task/subtask has an explicit disposition in task-audit-20261023.json. SP-01/SP-01b and technical SP-07b remain open/partial; SP-07d and third-party decisions are transferred unperformed.
- [x] **Style Compliance**: Pass — existing clients/permissions and preferred native route/fallback preserved; no new generator or approvals.
- [x] **New Tests**: No production code added; proportionate existing regression and direct evidence checks.
- [x] **Test Coverage**: Retained coverage, passage findings, interim/consolidated review, structured capture, simplification and change impact.
- [x] **Test Results**: All29 focused tests passed. Both current SP-07b and SP-07d packet ZIPs pass CRC/member hashes. No fresh successful native template/output proof claimed; repository and secret checks recorded at commit.

## Findings and fixes

### Medium — Search viewer URL was used as file path — diagnosed and corrected

- **Context**: The procedure-named template candidate's webUrl ends in Doc.aspx. Passing that viewer path to GetFileByServerRelativePath produces404 and does not establish source absence. Earlier silent CLI failure left this cause unresolved.
- **Fix**: Same-client GET-only diagnosis retained the404, then changed to GetFileById using the actual sourcedoc value observed in that viewer URL. That corrected request held for resource renewal; a bounded normal CLI attempt timed out. No new client, token transfer, denial bypass, grants or source writes. No document was acquired and no current-template claim is made. After existing-session renewal, verify both the file content and its intended local provenance; the filename alone is insufficient.

### Medium — Long historical plan obscured current dispositions — fixed

- **Context**: Dated superseded checkboxes, parent tasks and nested increments made archive/full completion ambiguous and risked treating a transferred user test as passed.
- **Fix**: Retained the preceding plan byte-for-byte in a same-directory history file, exposed eight bounded current items and a22-ID disposition audit. Kept source/technical gaps open, third-party work transferred unperformed and full acceptance false. Overlapping parent/subtask counts are not a workload percentage.

### Medium — Archive must not imply complete implementation — fixed

- **Context**: Historical pilot archive and current technical/source requirements have different completion scopes.
- **Fix**: Plan/metadata/current handoff explicitly report that all original tasks are not implemented, every disposition is reviewed, source/template blockers remain, and the existing archive is retained. Prior reviews retain dated native scope; tests/recovery are not relabelled current authority or new runtime acceptance.

## Remaining elements

1. Existing-client resource renewal and successful intended-template acquisition by observed file identity.
2. Verified current controlled-source provenance for procedure/template/control sources, and complete reconciliation against that intended template. Recovered V7 edition, page/section comparison and historical V6 coverage do not supply this proof.
3. Third-party user tests, actual substantive decisions and benefit observations: user-deferred final track only, no current participant request.
4. Automated structured regeneration and broader Word fidelity remain unqualified; the accepted manual/web fallback is delivered. Qualify any later automation separately rather than replace working output now.

## Disposition

Review fixes applied; current-source work remains blocked/partial and is not falsely closed. Existing historical track remains archived. No native changes, clinical adoption, source repinning, messages or permissions changes occurred. Raw diagnosis remains private under final-technical-audit-20261023.
