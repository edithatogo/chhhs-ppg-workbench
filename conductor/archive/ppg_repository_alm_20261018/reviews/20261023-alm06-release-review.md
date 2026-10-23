# Review Report: ALM-06 release and recovery

## Summary

The versioned sanitised source and bounded native release/recovery path meet ALM-06 for the selected solution snapshot; production acceptance remains separate.

## Verification Checks

- [x] **Plan Compliance**: Yes — source, hashes, private settings, build/dependency order, deployment/readback and exact-artifact recovery covered.
- [x] **Style Compliance**: Pass — existing Python CLI, JSON manifest and Markdown conventions.
- [x] **New Tests**: Yes — 11 release-source tests, including real Git checkout line-ending verification.
- [x] **Test Coverage**: Yes — byte fidelity, malformed/incomplete bindings, tampering, path/symlink/collision safety, private settings, managed flag, email refusal and receipt preservation.
- [x] **Test Results**: Passed — 25 release/email/inventory tests; setup and committed recovery verification recorded in the handoff.

## Resolved findings

Native byte fidelity required reading bytes before UTF-8 decoding; scoped Git attributes prevent text normalization. Hashes are checked against staged blobs and clean committed source. Receipt collision now fails before materialisation. Hydrated known email actions are refused before output. Managed builds alter only the manifest flag. XML comparisons preserve semantic content while allowing only identified unordered component collections and formatting; archive byte identity is explicitly not claimed.

Full definitions/reference readback after import and after uninstall/absence/reimport binds native evidence to the rebuilt managed SHA-256. Final service/run readbacks verify 18 Stopped and zero runs. Private raw evidence/settings are retained outside Git. No unresolved blocking finding within the bounded scope. Production rollback, connected operation and external-object recovery are not accepted by this review.

Committed recovery: `c34dec6ee5e9dafd56ebf5f626dd613f5b8bce6d`, tree `3f99ed2da9536076c27eccb75f50407fedef0742`; both 38-file variants byte-exact, 25 tests passed in a clean checkout. Setup 4,031 passed; staged Gitleaks scan 1,545 files passed. Scoped whitespace attributes recognize preserved native CRLF without changing bytes. The initial review preceded publication; completed exact-commit evidence follows.

Publication continuation: source variants with 206 private bindings reconstruct the same native bytes; native reference logical names, a schedule, server-relative paths and fixed evidence keys were additionally removed. Both original native qualification and private evidence are preserved. Public-copy local tests: 63 passed; setup: 3,065 passed, zero failed, two source-only pending. Confidential-content review and hosted verification are recorded separately for the exact publication commit.

## Publication review completion

All publication findings resolved: native reference names, schedule, server-relative source paths and fixed evidence keys were additionally replaced; 206 private bindings reconstruct the exact original native bytes. Source commit5056528 and runtime commit2fc5dbf were genuinely agent-reviewed and published through the guarded route. Remote commit/tree/complete inventory parity verified; hosted CI39945869444 succeeded with actual repo-local Python3.15.1 and 64 tests. Fresh GitHub-clone source recovery and 64 tests passed; 39 additional application-builder tests passed. Hooks now refuse missing or mismatched repo interpreters; synthetic negative tests still reach the real scanner. No detector exception was widened. No unresolved blocking publication finding. No production/clinical/branch-enforcement claim. Original evidence and dirty work preserved. See the release handoff for exact identities and private evidence paths.
