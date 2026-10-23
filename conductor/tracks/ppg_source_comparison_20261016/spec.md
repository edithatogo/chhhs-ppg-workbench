# Source-change comparison and affected cases

User selected roadmap candidate 5 on 16 October 2026. Deliver a read-only,
local/manual comparison of prepared source plans and a projection of affected
cases, using existing persistent DocumentUID links. Compare all preserved raw
source fields, retain exact before/after values and source/input provenance.
Row moves alone must not become content changes. Missing rows remain exceptions;
unknown aliases must not be matched by title or row. Expose incomplete case links.

No importer, identity ledger, catalogue, case, readiness or approval writes. This
metadata comparison does not compare policy document bodies or establish currency.
Output is a technical JSON/HTML report, not a maintained business document, so no
Word generation route is required. Native scheduling/hosting is a separate later
integration: do not claim deployment from repository checks.

Acceptance: deterministic output, changed and missing records linked to cases,
held/partial states visible, unsafe input rejected, escaped HTML, input preservation,
repeat-safe output and documented operation. Keep four Teams tabs unchanged.
