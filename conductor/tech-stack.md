# Tech Stack

## Now
SharePoint Lists/libraries and ordinary Microsoft 365 interfaces. Power Automate
for bounded source ingestion. Existing work-account operations are qualified per
resource; prefer the qualified CLI route, with native UI for unsupported actions.
No custom app registration, tenant administration or external service is assumed.

Python 3.15.0 stable is pinned for local development; 3.11+ remains the documented
compatibility floor. Use `.venv/bin/python` for setup, builders and offline checks.
GitHub CLI handles publication after its protection gate. Some current manual
utilities require local execution; do not describe them as cloud services.

## Source handling
Original XLSB read through SharePoint metadata/content actions. Read ranges or
create a temporary table only in an isolated working copy. If the actual XLSB
connector action is unsupported, use a permitted existing extraction/conversion
route; do not rename an extension or assume a Dataverse destination solves reading.

## Introduce only to remove demonstrated work
Basic Planner task projection; existing-template document population; approved AI
runtime after evidence retrieval. Dataverse and CareOps remain optional later.
Use source-qualified persistent IDs and exportable JSON/CSV to preserve migration.

Pin Conductor by commit. Do not auto-update tools, adopt every language style guide,
install new dependencies or build a generic orchestration engine for the pilot.
