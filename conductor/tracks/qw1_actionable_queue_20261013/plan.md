# QW1 implementation plan — Workbench and example-case navigation

The 15 October user clarification defines system setup as the deliverable.
Business policy work is outside this build. Follow [specification](./spec.md).

- [x] 1. **Bind workspace and snapshot.** Existing destination qualified; untouched raw source and all extracted columns retained with provenance.
- [x] 2. **Create the persistent workbench.** Two Lists/library, versioning, required indexed unique identities and useful views read back; all 985 source records reconciled without duplicate creation.
- [x] 3. **Demonstrate an example case.** Existing IETP case exposes role, outcome, next action, date/status and evidence fields. Editable proposed/pending values demonstrate workflow states; actual reviewer assignment, currency judgement and business acceptance are not required.
- [x] 4. **Verify and hand off the system.** Native case/navigation, draft/evidence links and operator status/failure/ownership guidance verified. Handoff explicitly separates technical readiness from later business use.

## Technical completion — 15 October 2026

Fresh bounded native audit confirms catalogue 985 items, queue one retained case,
versioned library, required/indexed/unique DocumentUID and CaseUID, default views
and workflow fields. Previous full baseline/zero-write replay proof is retained;
no duplicate replay or source/flow/checkpoint write was needed for this correction.
Case identity and business state remain unchanged. Existing v0.5/draft 0.2 sources,
drafts and direction endorsement are preserved as examples. Native operator
handoff now explains that no business response is needed to finish system setup.

QW1 is technically complete; no concrete software gap remains in this bounded
scope. Reviewer/capacity/date/source-currency/readiness/approval are unperformed
business states, not build blockers. Earlier business-gated plan is retained in
history/. See [delivery](../../../docs/workbench-delivery.md) and
[operator handoff](../../../docs/operator-reviewer-handoff.md). Private proof:
`.local/workbench/operator-handoff/system-scope-technical-audit.json` and retained
creation, catalogue replay, case, document and handoff receipts.
