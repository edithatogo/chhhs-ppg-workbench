# Broader source surveillance

> Current [reviewed archive and scheduling condition](surveillance-closeout-20261023.md): original scope complete, SV-04 delivered, SV-05 execution unperformed.

> Current workflow baseline: [versioned register and status reconciliation](workflow-documentation.md). Dated qualification sections below retain their original scope; read the current baseline before treating an earlier limitation as current.

Implemented16October2026 as a bounded on-demand pilot. Capture/comparison and
native output/download/repeat qualification are complete for the selected public
source family. **Start Here → Selected-source surveillance** exposes the frozen
report, evidence JSON, replay/capture kit and run notes.
This extends [register comparison](source-change-comparison.md) to selected raw
source files/pages. It does not reuse register DocumentUIDs for web pages or infer
case links from document titles. No source authority determination is performed.

Quiet monitoring is a PPG review-evidence route. It does not intercept, suppress,
replace or action the organisation's operational safety-notice process. A retained
safety-notice comparison supports keeping those purposes distinct; verify current
authorised routes before operational use. No live notice, response deadline or
alerting integration is configured by that comparison. See
[bounded comparison evidence](retained-text-pair-review.md).

## Select and qualify one family

Choose one named source family, one task and at most five exact canonical HTTPS
URLs. Record a stable explicit sourceKey for each resource and its responsible
publisher; confirm the source is authoritative for the intended question rather
than inferring authority from its hostname. The initial URL/config choice is not
permission to crawl links, process private policy content with AI or index an archive.

Retrieve each selected source using the existing qualified browser/Microsoft route.
The maintained [BrowserOS helper](../tools/source-surveillance/README.md) preserves
exact response bytes; use one selected source per tool call. Its saved native helper
is `selected-source-raw-capture` on the qualified publisher host.
Retain exact bytes, observed canonical URL, UTC capture time, hash and native
ETag/version or modification reference where supplied. A URL/title/search hit is
not content proof. Confirm access/authentication and correct target; sign-in/error
HTML returned with HTTP200 must not be represented as policy content. The local
component cannot independently authenticate an acquisition receipt or detect such
an error page. Preserve that native evidence privately before accepting a capture.

No new authentication, identities, permissions, provider or scheduled process is
introduced. Denied/missing/unsupported/error observations contain no body or cached
version/content fields. Never replace a denied response with stale source bytes.
Raw captures may contain sensitive data; keep operational materials in ignored
`.local/source-surveillance/` with approved storage/access and retention.

## Preserve a capture

The explicit family configuration follows `templates/source-surveillance/family.json`.
An observation array must account for every configured source exactly once:

```json
[{"sourceKey":"fictional-policy","status":"captured",
  "canonicalUrl":"https://example.invalid/policy",
  "capturedAtUtc":"2026-10-16T01:00:00Z",
  "file":"PRIVATE-CAPTURE-FILE","sha256":"EXACT_64_CHARACTER_SHA256",
  "nativeVersionRef":"OBSERVED_VERSION_OR_ETAG",
  "acquisitionRoute":"QUALIFIED_ROUTE_AND_PRIVATE_RECEIPT_REFERENCE"}]
```

For a failed read, retain only sourceKey, status and capturedAtUtc. Missing sources
are exceptions, never deletion or retirement. The canonical URL comes from the
maintained selected configuration. Empty captures or files over10MiB are refused. Inputs must be regular files;
directories, FIFOs and final symlinks are refused before reading. The limit is
enforced while reading even if a file grows after its size check. Stored raw
captures have the same cap; JSON control/snapshot receipts are capped at1MiB.
The component preserves arbitrary bytes; format readability/text extraction remains
an explicit native qualification task, not inferred from successful copying.

```sh
.venv/bin/python scripts/ppg_source_surveillance.py capture --config PRIVATE-FAMILY.json --observations PRIVATE-OBSERVATIONS.json --output .local/source-surveillance/NEW-CAPTURE
.venv/bin/python scripts/ppg_source_surveillance.py compare --baseline PRIVATE-BASELINE-DIRECTORY --candidate PRIVATE-CANDIDATE-DIRECTORY --links PRIVATE-CASE-LINKS.json --output .local/source-surveillance/NEW-REPORT
```

Destinations must be new. Snapshot raw files/hash receipts are preserved; existing
captures are never overwritten. A partial filesystem failure may leave an incomplete
new directory: preserve it for diagnosis and use a new destination. A snapshot
without its complete receipt or intact raw hashes cannot be loaded successfully.
There is no active checkpoint update, automatic baseline promotion or stale-cache
fallback. Compare only the same family/key/URL scope; older candidate capture times
are refused. Use explicit new baseline qualification if the selected scope changes.

## Interpret the report

`surveillance.json` and its readable `surveillance.html` companion distinguish unchanged, captured-bytes-changed,
version-reference-changed, baseline-unavailable and source-unavailable-exception.
Byte changes may be navigation, formatting or dynamic page content; they do not
establish a substantive policy change. Human examination of preserved before/after
captures is required. A complete pair can be eligible for manual baseline review;
`baselinePromotionAllowed` is only a technical completeness signal and never an
authority/current-policy decision. `baselineAdvanced` always remains false.

The standalone report retains family identity, each canonical URL, both native
version references and capture times/hashes, plus SHA256 of each exact snapshot
receipt. Match those hashes to the preserved `snapshot.json` files to resolve the
comparison outside its invocation directory. The canonical case-link payload hash
binds the supplied case scope. HTML escapes all supplied text; JSON retains the
structured values. Failed observations cannot carry stale content/version fields,
including when loading a stored receipt. These are technical provenance bindings,
not an independent authentication of an operator-supplied acquisition receipt.

Supply explicit existing CaseUID/sourceKeys links when known. A supplied case must have nonempty known source links; unknown/empty case links
fail visibly. An empty overall case-link array is allowed and means case impact
is unassessed; the tool does not infer unaffected cases from omitted input.
The output lists only supplied cases and potentially affected flags, not the entire
case population. No case is reopened, assigned, approved, retired or notified.

## Evidence and operating limits

Sixteen focused tests cover byte preservation/integrity, changes/repeats, failed reads,
missing-baseline holds, scope/link/time drift, bounded reads/nonregular inputs, standalone version/receipt
provenance, escaped HTML and denied-content rejection. These
fictional checks are separate from the actual native pilot evidence below.


## Qualified two-source pilot — 16 October 2026

Conductor resolved source selection with one Queensland Health public directive/
guideline family and the named technical task: capture exact selected sources,
retain immutable baseline/candidate evidence, compare bytes/version references and
handle unavailable acquisition without losing the baseline. Public pages require
no source sign-in. Existing authenticated SharePoint access was separately verified
for delivery and retrieval; public acquisition is not labelled authenticated source
access. No linked/QHEPS document, local-policy compliance or authority is qualified.

Both selected pages were acquired through fresh same-origin browser GETs. Independent
base64/hash/size checks preserved109558-byte and102527-byte baselines. The guideline
candidate read was identical; the directive candidate was an actual acquisition-error
observation with no body/version. Subsequent BrowserOS wall-clock timeouts are retained
as transport-only observations. No denied/stale body was used to fill the gap. No
native ETag/Last-Modified was supplied, so native version references remain null.
Printed identifiers/dates remain distinct from those absent response headers.

The report accounts for both selected sources, holds baseline promotion and leaves
case impact unassessed: no existing CaseUID/source mapping was verified. This is a
usable failure-reporting result, not a healthy-family or zero-affected-cases claim.
Actual case relationships and authority decisions are later evidence-backed use;
fictional explicit-link tests verify the software path without inventing mappings.

Four distinct create-only report/JSON/kit/run-note files are retained in the existing
qualified evidence-library area. Exact bytes, identities and ETags were read back;
repeat made no writes and preserved those identities/versions. A changed-content
collision was refused and final native identities/versions remained unchanged. The
actual SharePoint kit download passed ZIP CRC and hash checks; its downloaded tool
reproduced the frozen JSON and HTML exactly. The downloaded report was also rendered
and inspected. Private records: `.local/source-surveillance/native-20261016/`.

Refresh is manual/on demand. Retry the directive only with a new bounded acquisition
through the qualified route when the transport/request is available; keep its prior
failure and create a new snapshot/report revision. A successful read may make a pair
eligible for manual baseline review; it does not make promotion automatic. Never
rewrite this run's outputs or claim a fresh check from the same stored snapshots.
No watcher, schedule, crawl, AI processing, permissions, invitations, notifications,
source/case/checkpoint changes or substantive policy decisions are part of this pilot.

The preferred SharePoint structured-document route was assessed in the existing
native-document track and lacks production entitlement on the tested account.
This report retains the working structured JSON/readable HTML route; it does not
introduce another document runtime or migrate maintained Word outputs.


Shared integration was completed by the existing owner in `c4d5546`. Independent
native readback verifies published Start Here19.0, one surveillance entry/four exact
artifact links and preservation of all15 earlier controls. Capability lifecycle is
`pilot`, execution mode `local-manual`; this does not imply an autonomous service.
The bounded implementation has no remaining technical blocker. Future source
availability/case-link/current-authority inputs retain their explicit unknown or
held states until evidence resolves them; they are not fabricated to close setup.

## Shared manifest reconciliation — 16 October 2026

The guarded shared-manifest update now includes the existing `source-surveillance`
capability and all four report/data/tool/guide artefacts, unchanged from the local
manifest. The final native manifest hash matches the exact target bytes; unrelated
entries were preserved. Repeat deployment left hub and manifest versions unchanged.
This closes registration drift for the delivered on-demand pilot, without adding
schedules, notifications, authority judgements or case-impact determinations.
Private proof: `.local/autofill/final-deployment-and-repeat.json` and
`native-manifest-v03-target.json`.

## Review-intelligence extension — 19 October 2026

The versioned selected source register is
[NSQHS surveillance sources v1](../config/review-intelligence/surveillance-sources-v1.json).
It identifies the Commission, intended question, jurisdiction, framework edition,
source representation and applicability limits for each exact source. The second-
edition reference and third-edition development page remain separate; draft
material is not an adopted obligation. The register is stored with versioned
SharePoint evidence; it is a supported manual file register, not a new live List.
Other legislation/funding/directive/evidence sources remain to be selected and
qualified rather than silently included in this bounded scope.

Two fresh bounded public CLI captures per source retain exact response bytes,
headers, final URL, capture time, content type, HTTP result, hash and available
ETag. A redirect on the first PDF attempt was held as a changed URL binding; the
new official canonical path was then qualified in a separate pair. Its bytes
match the edition already checked for Standard6 actions. The initial attempt was
preserved, not rewritten into success. The HTML target/representation and absence
of the observed challenge/error patterns were checked; acquisition checks do not
establish the currency or clinical applicability of all source content.

Both selected sources are unchanged across this pair. Exact raw hashes and
snapshot receipt bindings pass. Three Proposed standards mappings provide one
historical document-version review lead for the second edition. There are no
recorded third-edition document mappings; affected scope is unassessed. No new
annotations are generated for unchanged sources, and baseline advancement remains
false. This is not an entire-catalogue impact or no-change-in-obligations claim.

### Quiet proposal bridge

```sh
.venv/bin/python -m scripts.ppg_surveillance_annotations \
  --registry config/review-intelligence/surveillance-sources-v1.json \
  --baseline PRIVATE-BASELINE-SNAPSHOT --candidate PRIVATE-CANDIDATE-SNAPSHOT \
  --links PRIVATE-NATIVE-STANDARDS-AND-ANNOTATION-EXPORT.json \
  --output PRIVATE-NEW-PROPOSALS.json
```

The bridge reuses the existing integrity-checked capture comparator. Explicit
requirement-to-framework-to-source relationships produce review leads only.
Rejected/superseded mappings are excluded; missing references fail. Multiple
requirement paths are grouped into one candidate per source change and document
version. A content/version fingerprint suppresses already-known annotation keys,
without appending duplicate notes or resetting human dispositions. Failed reads
and missing baselines stay acquisition exceptions; changed sources without links
remain unassessed. Proposed links and historical document versions never become
verified current applicability. The CLI prepares payloads, not native queue writes.
Use the qualified unique-key/original-history annotation route before inserting
actual new candidates. This unchanged native pair required zero queue inserts.

Six native companion files hash-match on download; exact replay creates zero
files. The downloaded ZIP passes CRC and all18 member hashes, both snapshot
receipt hashes and four raw capture hashes. Twenty-seven focused comparator/
relationship/exception tests pass. Versioned source evidence and readable report
are usable; native changed-event insertion, broader source families and scheduled
execution remain unqualified by this no-change pair.

### Scheduling and recovery

Keep SV-05 open: two immediate captures do not establish sustained availability,
useful accepted change suggestions or false-positive performance. No scheduler,
alert, owner notification, AI execution or baseline promotion was enabled. Preserve
raw acquisitions, redirect/failure receipts, source register, complete relationship
scope, source snapshots and immutable comparison outputs. Use new directories and
native revisions; never replace edited evidence or advance a baseline after a
failed read. Native-generation route eligibility is assessed separately in
[native document generation](native-document-generation.md); earlier dated blanket
entitlement observations must not be applied to every SharePoint-native route.


## 20 October — changed-signal native annotation qualification

SV-04 now has a bounded fictional changed-event integration proof. Offline
baseline/candidate bytes and two Proposed fictional requirement mappings yield
one document-version proposal. A clearly labelled fictional record is inserted
into the existing versioned annotation List, using a fictional DocumentUID and
section. Exact original wording/evidence/identity read back; native retry creates
zero and preserves Received/version1.0. Existing unique-key/schema/append-only
history guards are checked before insertion. The fixture remains for traceability;
no actual source change, applicability, clinical finding or human decision implied.

Six create-only native evidence files in ReviewIntelligence-quiet-change-native-v1
have exact bytes/identities/versions and inherited access; evidence replay creates
zero. Downloaded eleven-member archive passes CRC/all hashes; isolated archived
helper execution reproduces the labelled proposal and zero-proposal keyed replay.
Two mapping paths collapse to one annotation. Notifications and automatic baseline
promotion remain false. No flow, trigger, source fetch, schedule, real appointment,
source-register/mapping edit, owner notification or clinical approval is introduced.
Twenty focused surveillance checks pass. Real changed-source relevance/usefulness,
wider sources and ordinary-user acceptance remain unverified; SV-05 stays held.
Private quiet-change-native-v1 retains fixture, native proof and recovery result.
Recovery uses archived registry/links/snapshots/helpers in a separate directory;
never rerun the fictional insertion script as a production importer. Existing
real-policy review packs and frozen workflow1.4 remain unchanged: this qualifies
an existing manual helper path, not a new deployed workflow.


### Fresh selected-source comparison — 22 October 2026

Both exact selected official URLs were freshly captured through the existing public
browser route. Raw bodies, HTTP metadata, UTC time, hash/size and immutable capture
receipts were independently checked. The fixed-edition PDF is byte-identical and
its ETag is unchanged. The development page has changed raw HTML/ETag, but retained
article text and links are unchanged: its whole article matches after substituting
only two generated accordion instance IDs (28 and12 occurrences respectively).
The pilot announcement was already present in the retained baseline.

The first browser snapshot represented ETags without the earlier CLI `etag:` prefix,
creating a spurious PDF version-reference signal. That snapshot/report is preserved;
a separate aligned snapshot renders the exact actual header using the retained
prefix and correctly reports the PDF unchanged. No baseline was rewritten.

This is a measured source-noise result, not an accepted useful substantive change,
clinical applicability finding or schedule qualification. Retain on-demand capture;
no source/mapping/case write, baseline promotion, schedule or notification occurred.
Private raw snapshots, aligned comparator output, exact article comparison and
qualification audit: `.local/source-surveillance/current-20261022/`.


### Fresh on-demand comparison and replay — 23 October 2026

The already selected Queensland Health patient-safety directive and clinical-
incident guideline were captured again through the existing same-origin BrowserOS
helper, one URL per call. Both exact raw captures match the immutable 16 October
baseline byte-for-byte. The existing CLI captured the pair and produced an
unchanged comparison for both sources. A separate copy of the candidate snapshot
was then replayed through the CLI; its report and candidate receipt hash exactly
match the first comparison.

This qualifies repeatable on-demand capture/comparison and local recovery for this
unchanged pair. It does not demonstrate a genuinely relevant source change, useful
case impact or human applicability: no such change appeared, and no explicit case
links were supplied. No source/case writes, baseline promotion, schedule or
notifications occurred. Keep SV-05 conditional and scheduling disabled until an
actual relevant change is observed and manually assessed. Evidence and immutable
captures/reports: `.local/source-surveillance/current-20261023/`.
