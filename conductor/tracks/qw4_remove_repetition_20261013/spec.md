# QW4 — Monthly due and overdue report preparation

## Commission and outcome

On 15 October 2026 the user selected monthly due/overdue reporting from the
policy-derived task list and instructed implementation. The retained Controlled
Document Management Policy v3.1 pp9–10 and guideline p12 specify monthly reporting.
This explicit commission supersedes the earlier unselected/repetition gate.
The coordinator/custodian benefit is replacement of report assembly and collation;
no observed manual-time saving or operational acceptance is inferred.

## Deliverable

A working Microsoft-native flow prepares a monthly summary and role-grouped CSV
from the last verified catalogue. It accounts for overdue, current-month, following
three-month, invalid/missing-date and later rows, preserving month precision,
identities, source fields, source assertions of roles, raw references and provenance.
The first real report must be generated and independently checked. The saved flow
must have monthly recurrence, concurrency one and repeat-safe report destinations.
A source hold/stale check must be visible. An incomplete/mismatched catalogue or
moving successful checkpoint must stop generation. No operator Python is required.

## Boundaries and evidence

Read catalogue/checkpoint/candidate/source metadata; write only the two monthly
report files in the existing evidence library. Preserve source/case records,
identities, permissions, current importer and other agents' workspace resources.
No distribution, recipients, reminders, assignments, policy judgements or approval.
Follow ../../workflow.md: software completion is distinct from later business use.

Retain native save/run/readback, complete row/source/role comparison, date-boundary
and formula protection probes, repeat file/version proof, and saved active schedule
privately. Record operational acceptance, measured benefit and future scheduled
execution as unobserved. Guidance belongs in docs/monthly-reporting.md.
