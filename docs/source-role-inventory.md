# Recorded role assertions

The retained985-record catalogue snapshot now has a complete inventory of four
role-related source fields and two independent lifecycle assertions. Exact values,
stable document identity, source row and snapshot are preserved. A source row is
provenance, not permanent document identity. Each field/value pair gets a repeatable
content key; no whitespace, spelling or person/role equivalence is assumed.

```sh
.venv/bin/python -m scripts.ppg_source_roles \
  .local/private-candidate.json .local/new-role-inventory.json
```

The output refuses duplicate/missing identities, incomplete operations, missing
fields, unsupported values and overwriting an existing output. It preserves raw
scalars and classifies missing/non-text assertions without inventing vacancies.
The source catalogue lacks appointments, accepted handovers and authoritative
fields for several responsibility types. Use confirmed evidence and the existing
14-type contract for later reconciliation; custodian does not imply author.
Lifecycle assertions are not approval, publication or current ownership decisions.

The candidate was recovered from the previously validated source-standard archive
and verified against its manifest. This is a dated retained snapshot, not a fresh
live-tenant ownership claim. Detailed labels and document bindings stay outside Git.
Five native evidence files and their seven-member recovery archive have hash,
identity/version and inherited-access proof; exact replay creates zero. Isolated
archived-code execution reproduces the full inventory. Five focused tests pass.

Private proof: source-role-inventory-v1. Native companion:
ReviewIntelligence-source-role-inventory-v1 in the approved review-evidence library.
Recover separately, validate CRC/all manifest hashes and rerun archived inventory;
retain the earlier workbook archive as external provenance. No native roles,
assignments, appointments, handovers, source records, access or notifications change.
