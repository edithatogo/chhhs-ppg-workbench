# Provisional passage-backed review findings

The historical discharge-summary inspection conversion now has three draft
suggestions: clarify audit collection/sampling/reporting intervals; clarify the
post-distribution correction sequence; and separate accountable roles from
individual holders. These are review questions, not current-policy deficiencies,
clinical decisions or accepted changes. Distinct audit intervals may coexist.

`scripts/ppg_passage_findings.py` binds the inventory to actual inspected bytes,
checks every supplied quotation against its exact version-specific locator,
validates criterion/action vocabulary and retains the entire preparation pack.
It rejects fabricated passages, changed bytes, duplicate findings and supplied
human decisions. New output directories preserve human edits on retry.

Run with `.venv/bin/python -m scripts.ppg_passage_findings --preparation ...
--inventory ... --source ... --findings ... --output ...`. Inputs and outputs
containing real document content belong in private evidence, never Git. Preserve
original binary sources and the inspection-conversion archive separately; passage
checks do not establish conversion fidelity or source authority.

The pilot companion retains all985 catalogue entries and their existing comparison
states. Three passage-checked suggestions do not imply whole-catalogue semantic
comparison. Current V7 procedure, current template authority, external requirement
appraisal and human disposition remain open. The companion explicitly holds these
gaps and records no native AI execution, approval, issuance or notifications.

For recovery, retain the source archive, inventory, original preparation, findings
input, generated JSON/README and hash receipt. Generate a successor into a new
folder and reconcile against the same hashes and passage locations. Never replace
an edited pack. Native storage proof is a separate private receipt, not inferred
from local generation. Reconcile these provisional suggestions to the verified
current edition before accepting or incorporating any of them.

Native pilot storage: three companion files downloaded with matching hashes; a
second run created zero files. This is storage/replay evidence, not ordinary-user
acceptance or copied restoration. The receipt embedded in the original pack
truthfully reflects its pre-storage state; subsequent native proof is retained
separately rather than rewriting that immutable output.
