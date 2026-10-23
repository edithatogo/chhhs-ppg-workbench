# Historical template element reconciliation

20 October 2026. This supplements the [native template qualification](historical-template-native.md)
and frozen pack11. The accepted historical basis remains unverified for current
use; current-version confirmation stays open and nonblocking.

The earlier candidate flattened tables, headers and field instructions into158
source elements. The native Word derivative restores those structures into70
inventory elements. A version-bound reconciliation now accounts for every element
in both representations, retaining both complete packages and their package-part
hashes.

| Earlier candidate elements | Result |
|---|---:|
| Unique exact text/link correspondence proposed |56|
| Blank or structural blocks retained |72|
| Repeated/ambiguous candidates retained with all matching locators |28|
| Unmatched blocks retained explicitly |2|
| Total accounted |158|

All70 native elements have reverse entries, including elements without a source
text candidate. Nested paragraphs and table rows have locators within their native
parent inventory element. Small adjacent-paragraph spans account for flattened
cell combinations. Correspondence normalises whitespace only, except flattened
HYPERLINK instructions: those require the same visible text and the same target
on the specific native paragraph/row/span. A matching URL elsewhere does not qualify
that span. No fuzzy text equivalence or arbitrary duplicate selection occurs.

The two unmatched blocks are the combined accreditation-label/link paragraph and
an INCLUDEPICTURE field instruction. Their source content remains in the unchanged
candidate. Native link retention and embedded graphics have separate evidence;
that does not automatically establish these two element correspondences. Blank
blocks can carry layout, so they are retained rather than discarded as noise.

## Operator use

Use the companion's reconciliation JSON or CSV to navigate from the old source
locator to proposed native locators. Inspect candidates in the retained Word files
before accepting a correspondence. Counts describe technical accounting, not56
approved mappings or a loss of88 elements. Reverse entries allow inspection of
native structures that the flattened representation did not express separately.

No existing reviewer text, stable section ID, source key, template pin, held-run
reference or annotation is migrated by this utility. Every proposal remains
unaccepted. Accepting and applying a mapping requires an explicit recorded
reconciliation; retain old versions and unresolved annotations. The maintained
V6 document and its171-element capture remain unchanged.

The next output check is saved V6 DOCX field refresh and a separately proposed
revision that preserves human edits. This reconciliation is not native structured
regeneration, an approved template or a substantive policy decision.

## Evidence and recovery

Private evidence is in `.local/review-intelligence/20261020/template-map-v2/`.
Native companion: `ReviewIntelligence-template-map-v2` in the existing review-
evidence library. It contains this guide, the full version-bound reconciliation,
a navigation CSV and a recovery ZIP with both source representations and code.

Verify the ZIP CRC and all manifest hashes, then run `python verify.py` in the
extracted archive. It recomputes the complete map from archived bytes and compares
it exactly with the archived result. The archived regression tests also check
ambiguous text, changed wording, field/link target checks and source preservation.
Restore to a new folder, preserving differing/human-edited files. Real text,
locators and tenant bindings remain outside Git. No workflow transition or runtime
behaviour changed; frozen workflow releases and earlier review packs are preserved.

Version2 supersedes the interim version1 correspondence report. Review found that
same-table paragraph/span alternatives could be collapsed too broadly. Version2
collapses only identical paragraph-node coverage, retaining13 additional ambiguities.
The earlier snapshot is preserved; neither report applied a mapping or changed records.
