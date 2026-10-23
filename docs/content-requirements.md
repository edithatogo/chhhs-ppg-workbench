# Required and conditional content checks

The existing module definition supports advisory, required and conditional rules.
The new read-only `scripts.ppg_content_requirements` command makes their technical
presence results visible for a selected progression step. It changes no SharePoint
record, lifecycle, approval, publication, permission or notification state.

This CLI is a developer/qualification tool, not an operator prerequisite. The web
workflow uses existing SharePoint records and the stored readable report. It does
not require operators to install Python, use a terminal or open desktop Word.

For development, use a private JSON input containing the existing `definition`, native `records`,
exact `documentUID` and `sourceEditionKey`, `context` and `progressionStep`:

```sh
.venv/bin/python -m scripts.ppg_content_requirements PRIVATE_INPUT.json NEW_REPORT.json
```

The report refuses an existing output, mixed document/edition records, duplicate
content/rule identities and unsupported context/conditions. Preserve input and
report hashes; changed input requires a separate report. Drafts remain editable.

A rule names `ruleId`, existing `moduleKey`, `status`, `progressionSteps` and optional
`conditions`. Supported steps are draft, review, approval and publication; they are
check contexts, not a new lifecycle status. Conditions are explicit lists for
`documentType`, site, population, service or capability. A known nonmatching
condition makes the rule not applicable; otherwise missing context is unknown,
never an assumed exclusion. Conditional rules must declare their conditions.

Verified required/conditional rules need exact authority source/version/hash and
`templateVerified: true`. Proposed rules remain unverified. A definition without
verified requiredness or any rules cannot report cleared presence checks. Authority
metadata is a version-bound assertion supplied by an authorised reviewer, not an
automatic source-authority or clinical judgement.

OptionalModifiers uses a JSON object of nonempty string lists. A block limited
to another site/population/service/capability cannot satisfy the selected scope;
missing block context remains unresolved and malformed modifiers refuse evaluation.
Unmodified common content applies across those scopes.

Only a block with an explicit recognised ReviewedModule, state Reviewed and
nonblank ReviewText counts as reviewed text. SourceText and heading-based proposals
do not silently satisfy a rule. Retained non-text elements still require explicit
review. A present text block proves technical presence, not substantive adequacy.
The report distinguishes present, missing reviewed content, unknown applicability,
not applicable, not due at this step and unverified rule. It cannot approve a PPG.

## Historical pilot and native boundary

Fresh qualified CLI before/after exports account for all171 historical source rows
and preserve reviewer fields. The retained candidate has no verified mandatory
rules, so its actual review-step result is `unverified_rules`; it creates no false
readiness or mandatory local requirement. Seven focused evaluator checks plus four
existing capture checks cover presence, missing content, partial applicability,
unknown authority, identity/version refusal and output preservation. Fictional
verified-rule inputs are local fixtures, never inserted as real tenant rules.

`ReviewIntelligence-content-requirements-v2` retains guide, actual report, scoped
proof and self-contained recovery. Verify exact native files/inherited access,
zero-create replay, downloaded ZIP CRC/all manifest hashes, then `verify.py` and
included regressions in isolation. Recovery preserves actual exports/input,
module definition, evaluator/capture code and fixtures. Restore separately;
never replace changed reports or human records. Existing native owners and frozen
workflow1.6 remain unchanged: this is a manual diagnostic of existing rule contracts,
not a deployed enforcement trigger or permission to advance through a native form.

Version1 remains a preserved narrower qualification snapshot; version2 includes
block modifier scope checks. Use version2 for the maintained evaluator and recovery.
