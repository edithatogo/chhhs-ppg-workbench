# Review-package workflow — system operation

This lane builds and demonstrates the template workflow. Actual reviewer
acceptance, agreed dates, policy judgements and approval are later business work,
not gates to technical completion. Preserve the IETP drafts and decision history.

## Generate and edit a package

Use an existing case and dated baseline. Keep real inputs/outputs outside Git
under `.local/review-package/`. In a local JSON object supply every placeholder
in [the template](../../../templates/review-package.md), each as a string.
Table-row strings can contain Markdown rows. Use `Not recorded` for pending
business responses; retain source URLs/version assertions/hashes without editing
the original bytes. Do not infer current approval or a role assignment.

From the repository root:

```sh
python3 conductor/tracks/qw2_checked_review_20261013/generate_package.py \
  --template templates/review-package.md \
  --inputs .local/review-package/technical-demo/inputs.json \
  --output .local/review-package/technical-demo/generated.md
```

The command returns input/template/output hashes after readback and creates an
editable Markdown DRAFT. Existing outputs are refused, preserving user edits on
replay. Use a new candidate filename for another generation. No case, assignment,
invitation, notification or tenant write is created. Edit the separate candidate
and link editable instrument drafts/change logs; original source stays unchanged.

## Native handoff and evidence

QW1 owns rendering, library writes and case linkage. Supply candidate version/hash,
existing case identity, source/draft links and link map. The current renderer is
an IETP-specific example adapter, not an unattended multi-case service; additional
case wiring remains with its owner. This reusable template/population workflow
does not need a new application or framework.

Retained native receipts demonstrate example rendered text, ordered links/table
headers, editable draft bytes, original-source archive fidelity and existing
case identity/state fields. Reuse those receipts; do not re-upload to manufacture
proof. Office reading/working bytes may change during ingestion, so retain the
exact original-source archive separately.

## Later operational states

Generation always starts DRAFT / AWAITING REVIEW. The response fields capture
actual reviewer findings, operative-version confirmation, acceptance/capacity,
decision/authority evidence and action/date when later supplied. A direction
endorsement remains distinct from content readiness, authorisation, publication
and implementation. Native case fields demonstrate that distinction. Missing
business decisions do not prevent the system from generating, editing, linking
and storing a package. Do not ask people to do policy work to close this build.
