# PPG roadmap decision matrix — 15 October 2026

Advisory assessment for user decision; this does not commission deployment.
Based on current repository roadmap, manifest, delivery records and a three-agent
panel: practical delivery, governance/data integrity, and Microsoft frontier capabilities.
No tenant entitlement or preview availability was tested in this assessment.

## Recommendation

Build an operator-assisted identity-exception path, then a thin decision-to-implementation
assurance increment including human content-readiness evidence. Keep Lists and the
existing evidence library as canonical resources and use the current Teams surfaces.
For a bounded frontier experiment, test native form-driven Word generation before
a broad autonomous agent. Evidence navigation is the fastest independent improvement.

## Comparison method

5 means simplest, quickest or highest potential impact. Scores are engineering
judgements, not measured benefits. Rank considers observed need and dependencies,
rather than an arithmetic total. Days are focused engineering effort for one developer
with existing authorised connections, including bounded tests/native readback; they
exclude waiting for licences, tenant enablement, source access, operational decisions
and actual policy assessment. Larger workflow scope will increase the estimates.
Rows overlap; do not add estimates or create separate products automatically.

## Capability matrix

| Rank | Capability | Origin | Simplicity | Speed | Impact | Engineering days | Smallest implementation | Recommendation |
|---|---|---|---|---|---|---|---|---|
| 1 | Guided identity-exception resolution | Roadmap candidate | 4 | 4 | 5 | 2–4 | List/view or guided report; proposed mapping plus guarded reconciliation | Do next: addresses an observed hold; never automatically mint identity |
| 2 | Decision → publication → implementation → verification | Roadmap | 4 | 4 | 5 | 3–6 | Extend existing Review Queue and evidence links; short event-driven flows | Best substantive next build; record exact document/version and decision evidence |
| 3 | Human content-readiness record and case checklist | Additional | 4 | 4 | 4 | 1–3 | Version-linked assessor/date/findings/evidence fields; reuse assembler checks | Combine with row 2; files present does not mean reviewed or approved |
| 4 | Evidence finder and task-oriented archive navigation | Additional | 5 | 5 | 3 | 0.5–2 | Existing metadata/views/search; canonical archive links | Fastest standalone improvement; test actual search before adding AI |
| 5 | Source change comparison and affected-case view | Additional | 3 | 3 | 4 | 3–6 | Deterministic before/after comparison with DocumentUID and provenance | Useful follow-on to identity triage; do not change local decisions |
| 6 | Structured consultation and ownership handoff | Roadmap | 3 | 3 | 4 | 4–8 | Reuse current roles/response fields; add linked response records only if needed | After assurance; recording first, messaging/assignments separately selected |
| 7 | Broader reporting and process measures | Roadmap | 4 | 4 | 3 | 1–3 | List views first; Power BI semantic model/report if recurring cross-list need | Do not duplicate monthly report; collect stage history before turnaround measures |
| 8 | Authority/currency evidence register | Surveillance refinement | 3 | 3 | 4 | 2–4 | Canonical link/version/effective-date evidence and last human verification | Precedes broad surveillance or authoritative AI answers |
| 9 | Form-driven native Word draft generation | Additional / preview option | 3 | 3 | 4 | 2–5 | SharePoint structured document generation with existing templates | Best bounded preview pilot if licensing/tenant support; no replacement of preserved originals |
| 10 | Cited read-only evidence assistant / SharePoint skill | AI roadmap refinement | 3 | 3 | 3 | 3–7 prototype | Scoped SharePoint Copilot skill or Copilot Studio retrieval | Conditional experiment; supported formats, archive labels, citations and permissions must be tested |
| 11 | AI evaluation and promotion pack | Additional enabling work | 4 | 4 | 4 | 1–3 | Fixed questions/expected sources; archive/authority, permission, unknown and no-write cases | Required with any AI pilot; evaluate benefit and failure behavior before promotion |
| 12 | Suggested document metadata with Autofill | Additional / AI pilot | 3 | 3 | 3 | 2–4 prototype | Derived category/date/identifier suggestion columns; human validation | Conditional pilot; never overwrite source/identity/decision fields |
| 13 | Unattended review/submission package generation | Additional | 3 | 3 | 3 | 3–6 | Existing templates/assembler plus qualified native generation and readback | Defer until repeated manual use demonstrates friction; generated output remains draft |
| 14 | Broader authoritative-source surveillance | Roadmap | 2 | 2 | 4 | 5–10 per source family | Qualified source access, snapshots, deterministic diff and review queue | Start one source family; access/currency qualification dominates effort |
| 15 | Federation / CareOps / Atlas / process adapters | Roadmap | 2 | 2 | 2 | 5–15 per adapter | Explicit consumer contract and optional adapter | Defer until concrete consumer exists |
| 16 | Scoped Dataverse migration / model-driven app | Roadmap | 1 | 1 | 2 | 10–25+ | Selective migration only for demonstrated relational/security need | Defer; retain IDs/provenance and reconcile before cutover |

QW1–QW4, the Teams workspace, archive, manual review generator and submission
assembler are already implemented; they are the foundation, not new candidates.
The remaining verification items are separate from this feature ranking.

## Panel synthesis and differences

- Practical delivery preferred a case checklist as the smallest first addition,
  then assurance; it warned against rebuilding the existing assembler's checks.
- Governance prioritised identity recovery because a real hold exists, then
  version-linked decisions, human readiness evidence, publication and implementation.
- Frontier research supported native form generation and scoped retrieval pilots,
  while recommending deterministic write controls and evaluation before AI promotion.
- Synthesis: use a small identity report/form first; combine readiness with assurance.
  A thin case extension scores 4/4 for simplicity/speed; a full approval/routing
  engine would score nearer 3/3 or below. These are different scopes, not proof
  that an entire governance process takes a few days.
- None found an evidenced reason to migrate the whole workbench or introduce broad
  agent orchestration now. Identity recovery is a system improvement; resolving
  the particular held record remains an explicit operational decision.

## Current and frontier Microsoft options

| Option | Documented position checked 15 October 2026 | Fit and boundary |
|---|---|---|
| SharePoint Lists/forms/views and Power Automate | Existing deployed foundation | Best default for assurance, readiness and triage; preserve source/local boundaries. |
| Copilot in SharePoint and reusable site skills | GA rollout began 30 September; mixed preview/rollout wording remains in current docs. Skills are reusable Markdown assets. | Good bounded evidence-summary/checklist experiment. No custom code/external-system execution through skills; advanced work may consume credits. Tenant availability unverified. [S1][S2] |
| Structured document generation | SharePoint form-to-Word generation; associated flow trigger/actions explicitly Preview | Most promising native replacement for some manual draft preparation. DOCX template and maker Copilot licence required; verify output and repeat safety. [S3] |
| Autofill metadata suggestions | Documented library extraction capability; output requires checking | Useful pilot for separate suggested metadata, never canonical identity or approval fields. [S15] |
| Copilot Studio agent flows | Deterministic workflows; converting an existing flow is one-way and changes billing | No reason to convert the working importer/reporting flows. [S16] |
| Copilot Studio computer use | Microsoft GA announcement published May 2026 | Fallback capture route only; configured Windows runtime adds burden compared with supported source APIs. [S17] |
| Copilot Studio human-in-loop / multistage approvals | Connector actions explicitly Preview | Possible later consultation/approval UX. Sending requests changes the quiet operating model and requires a chosen recipient/route. AI approval is not clinical authority. [S4] |
| Power Apps Code Apps | Generally available; end-user Premium/pay-as-you-go/App Pass/auto-claim options documented | Potential richer triage UI if native forms prove inadequate; adds licensing and maintenance. Not SharePoint custom-form integration. [S5][S6] |
| Copilot Managed Runtime / Copilot Studio Apps / Cowork app builder | Runtime and Studio Apps Preview; Cowork builder requires Frontier enrollment | Watch or disposable prototype with fictional inputs; new runtime/billing is not justified by this workbench yet. [S7] |
| Teams custom agent/tab apps | Platform supports shared/private channel apps with current manifest requirements | Distinct from built-in Channel Agent. Custom installation/access tests required; preserve canonical parent-site permissions. [S8] |
| Teams built-in Channel Agent | Documentation excludes private channels | Does not fit the current channel. Do not change channel/access simply to enable it. [S9] |
| Power Automate Teams posting / Adaptive Cards | Connector documentation still excludes private-channel posting | Not a shortcut for this channel; existing quiet tabs/status remain appropriate. [S10] |
| Power BI | Semantic-model/Desktop routes remain alternatives; old Visualize the List/Library retired December 2025 | Use only for a defined recurring question; no legacy integration dependency. [S11] |
| Copilot Studio agent hooks | Preview | Logging/tool checks may help an experiment; documented hook timeout/failure can continue agent execution, so never sole protection for identity/approval writes. [S12] |

A documented product release is not proof of CHHHS tenant availability, licensing,
data-processing permission, supported geography or native acceptance. No spending,
preview enablement, notifications, permission changes or clinical assessment is
part of this research.

## Implementation principles if selected

1. Reuse current case fields and assembler categories before adding tables/forms.
2. Tie readiness findings and decisions to the exact document version and evidence.
3. Preserve source identities, raw snapshots and last successful baseline. New identity
   proposals must go through the existing contract and guarded reconciliation.
4. Record process state durably; do not leave a months-long policy process waiting
   in one flow run. Approval routing is a separate deliberate choice. [S13]
5. Keep archived originals unchanged. The 71 Office originals hosted with a
   .captured suffix may not ingest as supported knowledge formats; test first.
   If needed, create labelled derived search copies with manifest links/hashes.
6. Register any chosen increment in the existing capability manifest; retain four
   focused tabs and update canonical navigation/status instead of making parallel copies.
7. For an AI pilot, test cited answers, missing/unknown evidence, archived-vs-current
   distinctions, permissions, no-write behavior and repeatability with a fixed corpus.
   Promote only if it beats ordinary search/template use on an agreed task.
8. Build the readiness/approval recording system; responsible people perform the
   substantive review later. Package completeness is never content approval.

## Official sources

- [S1] [Copilot in SharePoint rollout, prerequisites and billing](https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-get-started)
- [S2] [SharePoint skills](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-skills)
- [S3] [Structured document generation and preview flow actions](https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-structured-document-generation)
- [S4] [Human in the loop connector and preview actions](https://learn.microsoft.com/en-us/connectors/advancedapprovals/)
- [S5] [Code Apps generally available — Microsoft February 2026 update](https://www.microsoft.com/en-us/power-platform/blog/power-apps/whats-new-in-power-platform-february-2026-feature-update/)
- [S6] [Code Apps requirements and limitations](https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview)
- [S7] [Copilot Managed Runtime preview](https://learn.microsoft.com/en-us/microsoft-365/managed-apps/)
- [S8] [Custom apps in shared and private channels](https://learn.microsoft.com/en-us/microsoftteams/platform/build-apps-for-shared-private-channels)
- [S9] [Built-in Channel Agent limitations](https://learn.microsoft.com/en-us/microsoftteams/set-up-channel-agent-teams)
- [S10] [Teams connector limitations](https://learn.microsoft.com/en-gb/connectors/teams/)
- [S11] [Retired Visualize the List/Library and alternatives](https://techcommunity.microsoft.com/blog/spblog/deprecation-of-power-bi-integration-within-sharepoint-lists-and-libraries/4455659)
- [S12] [Copilot Studio hooks preview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/hooks-overview)
- [S13] [Power Automate approvals and long-running patterns](https://learn.microsoft.com/en-us/power-automate/modern-approvals)
- [S14] [Copilot Studio supported SharePoint knowledge and limits](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas)

## Proposed decision

Select identity triage plus a thin assurance/readiness increment as the next core work.
Select evidence navigation if only a very small increment is wanted.
Separately select a form-to-Word pilot if exploring new Microsoft capabilities is
a priority. Leave broad surveillance, AI actions, federation and migration uncommissioned.

- [S15] [Autofill columns](https://learn.microsoft.com/en-us/microsoft-365/documentprocessing/autofill)
- [S16] [Agent flow mechanics, billing and conversion](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview)
- [S17] [Computer-use GA announcement](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427)
