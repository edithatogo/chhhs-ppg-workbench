# Source surveillance remediation — 16 October 2026

Both Medium findings in the original review are corrected in the maintained code.
Acquired and stored captures use regular-file checks, size-before-read and bounded
limit+1 reads; FIFOs/directories/final symlinks are rejected. JSON controls and
snapshot receipts are bounded, including before destination creation. A stale-stat
regression proves actual reads reject growth; source bytes remain unchanged.

Standalone report schema2 binds family identity, canonical URLs, before/after
native versions, capture times/content hashes, exact snapshot receipt hashes and
canonical case-link payload hash. Stored failed observations cannot leak stale
version/content metadata. A readable HTML companion escapes supplied fields.
Sixteen surveillance and seven comparison tests pass. The repository check passed
609 checks before the final receipt-size regression was added; rerun is recorded
in the track handoff when the increment is committed.

These corrections do not select a live source or establish native access/output.
SS-01/04/05 remain open until actual source-family and destination qualification.
No source/case/checkpoint/permission/flow writes or schedule were performed.


## Native continuation

Conductor supplied a concrete two-public-page pilot. Exact baseline bytes for both
sources are preserved; one fresh candidate matches and one actual acquisition
failed without body/version. Later Neo wall-clock timeouts are transport-only.
The failure candidate correctly holds promotion. Four distinct native files passed
exact byte/identity readback, unchanged repeated deployment and rejection of changed
content; final UID/ETag checks are unchanged. Actual downloaded ZIP CRC/hash and
execution reproduce JSON/HTML byte-for-byte; downloaded HTML was rendered. Final
helper version qualified with a fresh successful guideline read and saved for reuse.
No source/case/checkpoint/flow/access/schedule/notification effects were introduced.
Sixteen surveillance/seven comparison tests and610repository checks pass. Shared
hub/resource integration completed through the existing owner in c4d5546. Independent
native readback verifies published19.0, one block/four exact links and all15 prior
controls preserved. The bounded pilot acceptance is complete; current upstream
request availability and real case authority/mappings remain explicit unknowns,
not inferred healthy-source or business-completion claims.
