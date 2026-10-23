# Conductor setup and tool pin

Upstream: `gemini-cli-extensions/conductor` (also used by the CareOps parent).
Latest published non-prerelease release checked: `conductor-v0.4.1`.
Exact commit: `7a5c560a4fdf5297be58594cc37527eb12790272`.
The GitHub latest-release response and independently resolved tag agreed on
2026-10-13. This is the latest published release checked, not a claim that it is
the latest main-branch commit. Development forks were inspected but not required.

The commit is stored as a Git **160000 gitlink**, not a directory with copied
files, and is repeated in `conductor/conductor.lock.json`. There is no branch
tracking or automatic update instruction. Upgrades are explicit pin changes.

## Setup method
The standard project and per-track files were created directly from the pinned
Conductor artifact/index protocol and the already supplied brief. An interactive
CLI `/conductor:setup` session was not run. Its questions are already answered.
The local workflow intentionally replaces repetitive approvals, mandatory TDD,
coverage quotas and checkpoint ceremony. Upstream files remain unmodified.

## Materialise the tool on a connected machine

```sh
.venv/bin/python scripts/bootstrap_conductor.py
.venv/bin/python scripts/check_setup.py --require-submodule
```

The first command runs `git submodule update --init --depth 1 --
.agents/plugins/conductor`, then checks HEAD and the tool manifest against the pin.
It never follows `main`, updates to a newer release or installs global plugins.
The current checkout was verified on 18 October with the submodule materialised
at that exact pin. Earlier archive-only startup observations are historical.
Submodule presence does not establish installation into every agent client.
Project context/track execution is usable directly.

## Native command syntax at this pin
The release contains `commands/conductor/setup.toml`, `newTrack.toml`,
`implement.toml`, `status.toml`, `review.toml`, and `revert.toml`.
A compatible Gemini installation can link the hydrated local extension with:

```sh
gemini extensions link .agents/plugins/conductor
```

This optional link is not executed by the bootstrap script and should be used only
where that CLI is available/permitted. At this release the documented commands
are `/conductor:implement` and `/conductor:status`. Do not copy newer main-branch
command names into a pinned-release instruction. Other agents can follow
`AGENTS.md` and the local `ppg-deliver` skill directly; no global client setup is
required. Adapters are thin pointers, not a claim that every client was run here.

## GitHub publication
The 18 October audit found no configured Git remote and could not resolve the
expected repository using the intended GitHub account. Local commits are not
publication proof. Follow [publication protection](publication-protection.md) before publishing;
local hooks/gates are implemented and historical binding findings currently block it. `scripts/publish_github.py` uses an already authenticated
GitHub CLI on the user's machine, creates a private repository and pushes committed
files. It is included but no authenticated publication was performed here.

Public references: GitHub release/tag APIs recorded in the lock file; upstream
`GEMINI.md` (index protocol), `commands/conductor/newTrack.toml` (track artifacts),
`templates/workflow.md` (customisable defaults); GitHub CLI `gh repo create` manual.

## Standard project runtime — 18 October 2026

`.python-version` pins stable 3.15.0. The current private installation and `.venv`
were created without changing global Python or an existing environment. Python
reports releaselevel `final`; 39 representative offline tests passed (source sync,
monthly report, generation contract, prepared decision outcome). This is scoped
compatibility evidence, not full test-suite or native acceptance.

For a new checkout with no existing `.venv`, using the installed uv:

```sh
uv python install 3.15.0 --install-dir .local/runtimes --no-bin --cache-dir .local/uv-cache
UV_PYTHON_INSTALL_DIR=.local/runtimes uv venv --no-project --managed-python --python 3.15.0 .venv
.venv/bin/python -c 'import sys; assert sys.version_info[:3] == (3,15,0) and sys.version_info.releaselevel == "final"'
.venv/bin/python scripts/check_setup.py
```

Inspect/reuse an existing environment; never add `--clear`/`--force` to get past a
conflict. The package uses the standard library, so no pip dependency installation
is required for these checks. On Windows use the corresponding venv Scripts path.
The `.venv` and runtime downloads remain ignored. Bare `python`/`python3` in older
historical examples denotes their original runtime; use the explicit project
interpreter for new work. Preserve live automation's existing interpreter until
its exact owner qualifies migration.

Latest stable Python 3.15.0 was checked against
[Python.org](https://www.python.org/downloads/release/python-3150/).
[NuGet](https://www.nuget.org/packages/DocumentFormat.OpenXml/) still lists the
already pinned Open XML 3.5.1 as current. Stable .NET SDK selection/qualification
remains ALM-02 work; do not claim the shared .NET 11 RC was upgraded. Recheck new
releases for security/compatibility and adopt in isolated project scope, not by
blindly updating shared CLIs/authentication or the pinned upstream submodule.
