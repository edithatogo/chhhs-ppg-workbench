# Selected-source acquisition helper

`capture-browser.js` is a BrowserOS Neo helper function, not a Node fetcher. Use an
already qualified browser page on the selected publisher's HTTPS origin. Open and
settle the page separately, then call the helper with **one** explicitly selected
resource per tool call. The full family remains limited to five resources in the
capture/comparison contract. Do not follow links or extend the allowlist implicitly.

Inputs follow `templates/source-surveillance/browser-input.example.json`. The
expected title and printed identifier are target/format checks, not semantic review
or authority/currency decisions. Keep actual selected bindings and raw responses in
ignored approved storage. The helper has an eight-second fetch/body deadline and
a10MiB streaming cap; BrowserOS has its own30-second tool limit. An outer timeout
with no result is a transport observation, not an HTTP403 or fresh source capture.

For the qualified host, the saved Neo helper is `selected-source-raw-capture`.
Its maintained function remains here for inspection/reuse. On another host, use the
same function only after qualifying that exact source/access route. No credentials,
cookies, tokens or authentication profiles are read/exported by this helper.

A successful result includes exact response-body base64, SHA256, size, canonical
URL, UTC, observed ETag/Last-Modified if supplied and an acquisition-route record.
Read the tool's saved output file when a large result is spooled; do not refetch
merely to recover bytes from a successful operation. Decode and independently
verify hash/length, then supply the local file path to the capture CLI. Keep the
original browser receipt privately. Do not infer a native version when headers
are absent or substitute a printed edition date for an HTTP version header.

Failures have only sourceKey/status/capture time, with no stale body/version. A
failed fetch is `error`; HTTP401/403 is `denied`;404/410 is `missing`; unsupported
content/identity is `unsupported`. Each status refers to that acquisition attempt.
Never fall back to a prior body or silently promote the baseline. Preserve uncertain
transport effects and use one cause-specific changed approach rather than a loop.

The final one-source/eight-second helper was exercised against an exact selected
public HTML guideline and independently matched the retained original bytes.
Private proof remains with the source-surveillance native qualification receipts.
