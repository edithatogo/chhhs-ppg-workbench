# QW3 — Refresh without losing local work

## Outcome
Build one source-to-mirror import, then enable the requested hourly metadata
 checks/daily reconciliation after bounded readbacks. Do not write back to the master.
 Process an isolated XLSB copy. This is the one active automation increment; QW2
 clinical preparation progresses independently.

## Inputs / dependencies
Exact PPG source/destination operations and an extractor working against a copy. Use standalone synthetic targets while QW1 is being prepared; bind once without racing shared resources.

## Deliverable and completion
The intended source-to-mirror flow runs and reconciles, preserves local work on replay/change, exposes failure and has the requested cadence verified. Local designs alone do not close it.

## Boundaries
Follow ../../workflow.md. Preserve source/local separation, actual authority and
private records. No additional programme approval or mandatory broad test suite.

## Out of scope
Enterprise platforms, integration with CareOps siblings, all-history cleaning,
new clinical publication authority and roadmap implementation.

## Evidence
Observed output, evidence level, private receipt reference, open conditions and
next action. Relevant intended outcomes: O3, O7. No measured benefit is assumed.
