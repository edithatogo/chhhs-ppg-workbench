# Review — vacancy evidence correction

Requirement: missing/unknown appointments must not become confirmed organisational
vacancies. The old resolver inferred vacant from no matching appointment or a blank
holder, contrary to the source-assertion and explicit-authority contracts.

Corrected: unconfirmed for absent/unnamed evidence; vacant only for explicit accepted
evidenced vacancy. Vacancy-with-holder is rejected. Existing ambiguity, interval,
delegation and assignment checks remain in place. No new vocabulary or transition.

Evidence:21 focused tests pass. Five real local CLI scenarios distinguish missing,
unnamed, confirmed vacancy, proposed vacancy and missing evidence. Fresh12-record
native input projection matches previous output; history/handovers remain unchanged.
Four native files read back and replay0. Downloaded20-member archive CRC/all hashes
pass; isolated archived code reproduces five outputs and baseline comparison.

Review result: no unresolved defect in this bounded correction. Native role records,
stored snapshots, ACLs, source registers and notifications unchanged. Evidence is
private/native, sanitised code and documentation only in Git. Frozen workflow1.5.1
preserved. Current procedure/template, full Word fidelity and ordinary-user acceptance
remain unverified; this does not close the overall track or goal.
