# Review: versioned advisory criteria registers

Plan compliance: partial RF-08/10. Native definition storage and readable views
are delivered; mandatory local authority and full review-run integration remain
open. No human decision or policy approval is inferred from seeded options.

Verified: two versioned Lists, 15 custom fields, eight criteria and eleven
options. Independent CLI reads match all generated seed values and both default
views/columns. Identical provisioning/seed replay creates zero rows. Versioned
unique keys and exact comparison preserve existing definitions on drift.

Fourteen focused tests passed; setup1517 passed/0 failed. Tests cover duplicate
identifiers, rejected mandatory/approved seed states, fingerprint changes,
candidate/subject separation and retained human edits. No credentials or native
bindings are committed. Source definitions and frozen kit remain unchanged.

The initial independent read omitted explicit request headers and returned403;
one correction restored the standard qualified request headers and exact reads
succeeded. No authentication mutation, new consent or permission change occurred.

Limitations: native forms are not immutable, so export/version/hash reconciliation
is required. Copied native restoration and ordinary-user access are unverified.
These limits are documented; no blocking defect found in this bounded increment.
