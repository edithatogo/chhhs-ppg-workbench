# Native standards validation and review context

Use the existing manual reference-validation step before accepting or using
standards/relationship records in a review. The implementation is
`scripts/ppg_native_standards.py`; it makes no tenant writes. It reads a complete,
versioned native export and the catalogue identity inventory through the existing
qualified CLI export route. No premium action, new connection, consent, licence,
permission or clinical decision is introduced.

## What it checks

The known five-register schema/history validator checks37 custom fields, unique
record keys, complete record/history inventories, required values and unchanged
latest history. The adapter checks actual choice values, known framework/requirement
keys, same-edition ancestry, requirement cycles and accepted document hierarchy.
Reciprocal ordinary references remain valid. Endpoint version labels are mandatory.

| Condition | Result |
|---|---|
| Unknown framework/requirement or accepted hierarchy cycle | Refuse context |
| Incomplete export, history drift or unknown choice | Refuse context |
| Draft framework asserted as a current obligation | Refuse context |
| Proposed document endpoint missing from identity inventory | Retain visible unresolved reference |
| Reviewed/Accepted endpoint missing from identity inventory | Refuse context |
| Reviewed mapping/crosswalk or Accepted relationship without separate decision reference | Refuse context |
| Source citations without a decision reference | Remain evidence; cannot satisfy recorded acceptance |

`EvidenceRef` may retain existing prose or source JSON. A reviewed/accepted record
must additionally contain a nonempty string `reviewEvidenceRef` in its JSON, linking
to the separately recorded human decision. That is a presence check only: it does
not authenticate the actor, open/verify the decision, establish clinical authority
or certify compliance. Existing lifecycle authority/decision owners retain their
roles. No actual reviewed/accepted clinical rows were created during qualification.

The checker uses the known complete-history snapshot contract. Evicted histories,
unregistered external document identities or a changed native schema need explicit
reconciliation; they are not silently omitted or repaired. Direct SharePoint saves
remain unconstrained. Re-export before a later acceptance/use and preserve changed
records; a previous passing snapshot is not a live lock or approval.

## Historical labels and the requested edition

Current qualification covers180 native records/180 available versions: two framework
editions,162 requirements, eight Proposed mappings, no crosswalks and eight Proposed
document links. All referenced document identities resolve against the retained
catalogue inventory. Full before/after records, schema, histories and views match.

Historical mappings use a descriptive V6 inspection label; the document links use
an inspection-hash label. The exact-version context keeps both original labels.
Supplying the verified inspection bytes additionally groups eight mappings/eight
links whose evidence explicitly binds that same inspection hash. This proposal-only
grouping never merges accepted graphs, rewrites stored labels, establishes original
conversion fidelity or applies the material to the requested current V7.

The separate requested-edition context has zero exact-version mappings/links and
retains the eight historical mappings/links separately. A catalogue version assertion
does not verify the requested procedure's bytes, currency or authority. Earlier
review-pack pins, source mappings and workflow releases remain unchanged.

## Run and recover

Use a fresh private complete export from the existing five original register
bindings, including definitions, fields, items, available histories and views. The
collector is the existing recovery-export route; retain its native receipt. The
catalogue file is a complete native `value` page containing `DocumentUID`, including
retained absent identities needed for historical references. Do not silently mix
recovery-target IDs into the working register export.

```sh
.venv/bin/python -m scripts.ppg_native_standards \
  --snapshot /private/path/native-export.json \
  --catalogue /private/path/catalogue.json \
  --document-uid "$PPG_DOCUMENT_UID" \
  --document-version "$PPG_DOCUMENT_VERSION" \
  --inspection-file /private/path/historical-inspection.docx \
  --output /private/path/new-context.json
```

Omit `--inspection-file` for the separate requested-edition context. Supplying it
only adds hash-bound historical proposals; it does not verify an edition. Existing
outputs are refused unchanged. Identical inputs produce identical contexts in a
new path. All native identities, input snapshots and detailed receipts remain private.

Six versioned files are in the existing evidence library's
`ReviewIntelligence-standards-validation-v1`: guide, summary, full validation report,
historical context, requested-edition context and recovery ZIP. Byte/identity/version
readback and zero-create replay pass. The folder inherits existing evidence access.
Private receipts are under
`.local/review-intelligence/20261020/standards-validation-v1/`.

The22-member ZIP contains native before/after exports, catalogue inventory, inspection
bytes, output contexts/report, proofs, generation-time code/tests/schema and hash
manifest. Verify downloaded CRC and every member hash before reconstructing into a
separate private directory. Both contexts/report rebuild identically from those
downloaded inputs. Never overwrite a human-edited output or execute document content.
The current checker also excludes contradictory inspection-hash assertions from
the grouped proposals, while retaining the original relationship in its exact
context. This stricter guard reproduces both frozen contexts identically. The
archive keeps its original generation-time code/tests; they are not silently repinned.

The published workflow1.3 already includes manual reference/hierarchy validation;
this qualifies its implementation, with no new decision, trigger or native writer.
The companion supplements the frozen review pack. Full comparator coverage, verified
current subject/template, clinical review and later ordinary-user adoption remain
separate work.
