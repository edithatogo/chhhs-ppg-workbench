# QW4 implementation plan — Monthly reporting

- [x] 1. **Select task and value test.** User commissioned monthly report preparation;
  recurrence evidenced by policy. Beneficiary is coordinator/custodian preparing
  reports for the stated governance roles. Manual-time saving remains unmeasured.
- [x] 2. **Build the replacement.** Native read-only acquisition, exact successful
  candidate/catalogue reconciliation, verified source-role join, month buckets,
  grouped CSV, summary, freshness warning and bounded versioned report writes.
- [x] 3. **Check real output and repeat safety.** Native successful runs and CSV
  readback; independent comparison of all 985 identities/source/role values;
  12 native date cases, two formula probes and five focused local checks.
  Repeat uses the same file identity, versions 1.0/2.0; final focused CSV is 3.0. No source/case writes.
- [x] 4. **Enable cadence and hand off.** Active monthly recurrence from 1 November
  2026 at 08:00 Brisbane, concurrency one, read back after removal of probes.
  Operator guidance and private receipts retained. Stop this increment here.

## Completion record — 15 October 2026

October output: 985 rows; 233 overdue, 15 current month, 42 following three months,
695 later, zero invalid/missing review months. The working CSV contains the 290
reportable rows; all source/role values independently match. The 695 later rows
are accounted for in summary totals. Known newer source version is
prominently flagged; output represents the last successful catalogue only.
Native guard failed before writes during qualification, then passed all 18 checks
once SharePoint row-number numeric representation was normalised to integer.

The first scheduled November execution, business acceptance and measured time
saving remain unobserved. Distribution is outside this report-preparation scope.
Detailed native bindings/receipts are in ignored `.local/monthly-report/`.
