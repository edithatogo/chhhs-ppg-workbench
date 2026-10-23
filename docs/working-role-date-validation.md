# Working role calendar-date checks

Five native Text columns now enforce the [qualified calendar checks](native-role-date-validation.md):
EffectiveFrom/EffectiveUntil on assignments and appointments, and EffectiveFrom on
handovers. Optional end dates remain allowed. AcceptedAt is a timestamp and was
not changed. All16 existing date values passed preflight;12 role-input records
retain their business values, identities, audit stamps and versions.

Each working field refused an invalid-date update using the exact item ETag;
readback proves unchanged values, versions and ETags. Exact deployment replay
updates zero fields. List-level validation settings, requiredness, types, versioning
and inherited access remain unchanged. This is date-format/calendar enforcement,
not interval ordering, cross-record overlap/reference, delegation or authority
validation. Real role-holder reconciliation and ordinary-user adoption remain open.

Field metadata exposes no ETag. The serial schema writer compares original schema
and validation properties before setting only ValidationFormula/ValidationMessage,
refuses another validator and verifies readback. It does not provide atomic schema
concurrency protection. Coordinate the existing owner; preserve concurrent changes.
No role record, source, lifecycle actor, permission, flow or notification changes.

Five native evidence files and their six-member archive retain original/current
schema, preflight and refusal proofs. Validate downloaded CRC/all hashes and compare
live state before recovery. Restore only the original validation properties if the
current validator still matches this promotion; never reset the whole schema or
records. Native rollback/copied restoration is not claimed. Private evidence:
role-date-promotion-v1; native companion uses the same name in the evidence library.


Later20October evidence qualifies the validator post-step on the previously copied
role fixture, preserving17 records/20 versions. See
[validator-aware recovery](role-register-recovery.md#validator-aware-follow-up-20october).
This does not claim a fresh full restore or native rollback.
