# CHHHS PPG workbench

**A Microsoft 365 workbench for source records, review-package preparation and monthly reporting.**
This is a standalone, value-first Microsoft 365 pilot. It does not replace the
central document-control team or depend on CareOps, Dataverse, AI or Planner.

## Start

Read [AGENTS.md](AGENTS.md), then [the context index](conductor/index.md).
Use [the track registry](conductor/tracks.md) and [follow-on execution queue](conductor/execution-queue.md); do not run setup again.
QW1–QW4 are technically implemented; actual policy review and approval remain
later business work. See [current handoff](conductor/handoff.md) and
[monthly reporting](docs/monthly-reporting.md).
[Guided identity resolution](docs/identity-triage.md) now prepares explicit decisions
and applies accepted packages through the existing guarded importer. Real unresolved
identities remain held for the operator; technical delivery does not decide them.
[Consultation and ownership handoff](docs/consultation-handoff.md) records version-linked
responses, conditions and offered/accepted roles in native forms; it sends no requests
and performs no assignment or transfer.
The workflow visualisation is integrated into the existing Teams channel:
**Clinical Leadership (CHHHS) → Policy (PPG) Management → PPG monthly reporting
workflow** (use the tab overflow menu if hidden). See the
[channel walkthrough](docs/monthly-reporting.md#channel-walkthrough-and-mermaid-diagram).
The [longer-term roadmap](docs/roadmap.md) is deliberately not a task backlog.

```sh
.venv/bin/python scripts/check_setup.py
```

Create/reuse the [project Python environment](docs/tooling.md#standard-project-runtime--18-october-2026) first.
The check uses pinned stable Python 3.15.0 and Git, with no packages or tenant access. It checks
this repository setup, not clinical content or Microsoft deployment. To download
the exact pinned Conductor release on a network-enabled machine:

```sh
.venv/bin/python scripts/bootstrap_conductor.py
```

The repository includes a genuine Git submodule entry at
`.agents/plugins/conductor`, pinned to upstream release `conductor-v0.4.1`.
The current checkout is materialised at that exact pin. Use the bootstrap command
above to restore it when absent. Project context and track files remain usable without
a global Conductor installation. See [tooling](docs/tooling.md).

## What exists

- Completed project context, value-first workflow, agent entry points and four
  separate track specifications/plans.
- Minimal catalogue/queue field configuration, original 25-column source mapping,
  one review-package template, and operation-evidence template.
- Local Git history, exact Conductor pin, setup check, bootstrap and private
  GitHub publishing scripts.

Native Lists/library, protected source synchronisation, draft templates/example
generation, metadata prefilling/structural checks, submission-package assembly,
monthly report preparation and [human readiness recording](docs/human-readiness-recording.md)
are implemented with retained evidence.
Clinically approved review packages remain later business work. Technical
deployment does not establish policy review or approval. Selected AI pilots
remain in progress; preparation is not a deployed assistant.
Use [metadata prefilling](docs/metadata-prefilling.md) for the operational manual
route and [native Word generation](docs/native-document-generation.md) for the
completed fictional Developer pilot and conditional production adoption.

## Follow-on outputs and navigation

These links complement the existing Teams hub and four focused channel surfaces;
they do not introduce another tab or change native permissions.

| Output | Current usable scope | Operator documentation |
|---|---|---|
| Assurance and readiness | Version-linked recording; human decisions remain unperformed | [Assurance](docs/decision-implementation-assurance.md), [readiness](docs/human-readiness-recording.md) |
| Evidence and source comparison | Archive navigation and manual comparison using qualified native inputs | [Navigation](docs/evidence-navigation.md), [comparison](docs/source-change-comparison.md) |
| Policy editions and measures | Fields/views and manual evidence-bound measures; unknown currency/history preserved | [Editions](docs/policy-editions.md), [measures](docs/process-reporting.md) |
| Native Word | Fictional Developer pilot delivered and Off; production conditional | [Four-step guide](docs/native-document-operator-guide.md) |
| Source surveillance | On-demand two-public-page pilot; no schedule or notifications | [Operation](docs/source-surveillance.md) |
| Atlas adapter | Fictional local supporting-evidence adapter; CareOps and hosted/real-data use unqualified | [Operation](docs/careops-atlas-adapters.md) |
| Autofill suggestions | Fictional pilot Off: raw reprocessing overwrites corrections; separate reviewed fields, settled preservation and version-bound apply/recovery verified | [Pilot guide and limits](docs/autofill-suggestions.md) |
| Unattended packages | Native retained-Word packaging, commit-last receipt, automatic paired verification and unchanged replay verified; integrated missing-receipt recovery and edited-output preservation verified; actual overlap and bounded-size acceptance/refusal verified; existing-case native archive/receipt/replay and stale-selection refusal verified; Word invocation and production open | [Progress and limits](docs/unattended-package-generation.md) |

For unfinished work use the [execution queue](conductor/execution-queue.md):
[cited evidence](docs/cited-evidence-assistant.md),
[Dataverse](docs/dataverse-migration.md) remain pilots/preparation until their
actual runtime checks and scoped acceptance are recorded.

## Publish to GitHub

From a connected development machine with GitHub CLI already authenticated:

```sh
.venv/bin/python scripts/publish_github.py --repo edithatogo/chhhs-ppg-workbench --content-review .local/publication-review.json
```

First activate and satisfy [publication protection](docs/publication-protection.md).
Historical binding findings currently block publication; no GitHub sync is claimed.
After those checks and actual content review, this creates a **private** remote for this standalone repository and pushes the
committed main branch. It fails rather than overwrite an existing repository or
use another account. It does not create Issues, change other projects, send mail
or access Microsoft 365. A source-only ZIP must be restored from the included Git
bundle first; the delivered repository ZIP already contains `.git`.

Real registry data, source bindings, policy texts, drafts, correspondence and run
receipts belong in approved work storage or ignored `.local/`, not in GitHub.

[Portfolio and process measures](docs/process-reporting.md) adds live case/history views and manual evidence-bound measures; missing stage history stays not measurable.

The [guided workspace](docs/guided-workspace.md) provides five Start Here task routes, a grouped case form, identity/source navigation and focused follow-up views within existing permissions.

[Status clarity](docs/status-clarity.md) separates reconciliation state, display freshness and three explicit Brisbane clocks, with dated capability execution modes.

For execution conventions and remaining friction, use the [implementation guide](docs/implementation-guide.md).
