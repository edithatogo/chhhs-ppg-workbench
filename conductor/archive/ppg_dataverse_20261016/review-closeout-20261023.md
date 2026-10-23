# Review Report: Dataverse migration

## Summary

Offline preparation is usable with nil-identity refusal fixed; native migration remains unperformed and track archived partial.

## Verification Checks

- [x] **Plan Compliance**: Partial — DV-02/03 delivered; DV-01 partial, DV-04/05 unperformed. All five dispositions reviewed.
- [x] **Style Compliance**: Pass — small existing validator change; source/local values and conceptual target separation preserved.
- [x] **New Tests**: Yes — regression covers nil primary identities across six datasets and populated relationship references.
- [x] **Test Coverage**: Partial — offline validation/reconciliation and CLI refusal covered; no native pilot, import, security, recovery or cutover proof.
- [x] **Test Results**: Passed — 14 focused tests; actual fictional CLI parity, source preservation and nil-identity failure before output creation.

## Findings

### High — fixed: nil UUID accepted as a persistent identity

- **File**: `scripts/ppg_dataverse_reconcile.py`
- **Context**: A syntactically parseable all-zero UUID could stand in for an existing document/case/event/file identity and pass identical-export comparison.
- **Fix applied**: Reject UUID integer zero in the existing shared identity validator; primary and reference regression coverage added. Valid shared/long histories remain accepted.

### Medium — fixed: stale discovery and archive-state instructions

Current same-day PAC evidence enumerates four environments; old expiry and two-candidate observations are historical. Proposal/plan now distinguish discovery from selected migration destination and existing ALM ownership. Explicit user archive request supersedes the historical completion-only restriction; full acceptance stays false.

### Remaining scope gaps

No demonstrated Lists limitation or exact migration target/container selected. Native schema/security/pilot, production entitlement, full export/history/file/workflow/access parity and cutover/rollback are unperformed. No credential, permission, billing, native schema/data or source change occurred. [Closeout and next steps](../../../docs/dataverse-closeout-20261023.md).
