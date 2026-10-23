# Reporting and comparison contract qualification — 17 October 2026

The existing monthly report and manual source-comparison consumers now account
for the committed 985 active source rows plus two explicitly retained absences:
987 catalogue identities. This is compatibility work on existing consumers;
identity application is closed and was not replayed.

## Verified behavior

- The shared validator requires the exact successful source/identity contract,
  complete UID sets, source-bound absence acknowledgements and unchanged native
  retention readback. It rejects unacknowledged, stale, unknown and duplicate
  identities/acknowledgements and malformed count types. Returned known identities
  retain acknowledgement history without consuming stale absence authority.
- The existing monthly flow separates active source rows from retained catalogue
  records, checks active source-field/alias parity and full catalogue accounting,
  and saves a separate retained-absence CSV. Both CSVs are read back before the
  summary is committed. Retained source fields and acknowledgement evidence stay
  visible; absence establishes neither clinical retirement nor current approval.
- The independently checked final native output has 270 reportable active rows:
  213 overdue, 15 current-month, 42 next-three-month; 715 later active rows and 2 retained.
  Source/role fields, retained fields, summary accounting and links all matched.
  Qualification filenames are separate from existing monthly outputs.
- The exact production actions, existing connections, Started state and original
  monthly recurrence/concurrency were read back after qualification. The first
  scheduled result remains unobserved until 1 November 2026, 08:00 Brisbane.
- Source comparison reproduces 24,625 baseline cells, accounts 985 active + 2 retained,
  and finds zero active source-field differences. The existing case has 2 qualified
  active links, zero affected differences and zero unresolved links. Cases linked
  to retained or unknown identities still remain explicitly unresolved in tests.
  Fresh native source metadata matched retained bytes' ETag, identity and length;
  this does not claim a new byte acquisition or policy content review.
- Uniquely named v3 comparison HTML/JSON, guide and tool ZIP were uploaded and
  downloaded byte-for-byte. The downloaded kit reproduced both real outputs
  exactly; member hashes and ZIP CRC passed. The 16 October report and intermediate
  unpromoted v2 assets remain history. Start Here 29.0 uses the v3 route; repeat
  created no additional page version and preserved all 16 unrelated controls.
- All 987 catalogue records and the existing case retained their substantive fields
  and ETags. The successful reconciliation checkpoint stayed unchanged. Only the
  four owned comparison manifest rows changed; capability modes/status policy,
  source/hourly cadence, other native writers, access and notifications stayed
  unchanged. SharePoint page rendering/links were reloaded; no new Teams desktop
  acceptance is claimed.

## Evidence and recovery

Private exact native inputs, definitions, runs, outputs, hashes, hosted-download
proof and preservation receipts are retained in
`.local/retained-consumers-20261017/`. Final monthly native qualification run:
`PRIVATE_RUN_REFERENCE`. Principal receipts:
`final-monthly-output-proof.json`, `final-production-readback.json`,
`hosted-v3-assets-proof.json`, `downloaded-tool-proof.json`,
`preservation-proof.json` and `comparison-v3/comparison.json`.

Earlier definitions, the first successful qualification and its output remain
retained. A stale source/contract, moving checkpoint, unexplained missing record
or failed CSV readback still stops publication; preserve the prior report and
resolve the exact guard through the existing owner. Do not mint identities or
reuse old absence authority inside either consumer. The existing manual tools
and monthly schedule remain the operator routes; no new schedule is required.

Local validation: 213 tests passed, including 7 focused retained-contract tests.
This qualification does not perform substantive policy review, assign roles,
approve readiness, distribute reports or enable an optional pilot.
