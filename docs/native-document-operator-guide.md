# Native Word development pilot

This is a fictional development/test route using the existing Developer environment
and Word Online (Business). The flow is retained **Off** between qualification runs.
Production entitlement and adoption are separate; the working manual generator
and assembler remain the operational route. Do not paste real policy or personal
information into this pilot. It sends no messages and writes no source/case records.

## Prepare one DRAFT in four steps

1. Take accepted structured input. The supplied fictional example matches
   `config/native-document-input.schema.json`; keep technical identity, source and
   template hashes, included identities and revision. Human findings and decisions
   remain explicit pending values. Use arrays for comparison/consultation rows;
   `[]` means no rows, and empty `OptionalContent` excludes optional text.
2. Open the recorded native Word pilot link in its Developer environment. For a
   bounded test, turn on this exact pilot if Off, select **Run**, and paste the JSON
   into **Accepted fictional package JSON**. Do not change connections or templates.
3. Submit once. Retain the native run ID and wait for a terminal result. A successful
   attempt includes Word population, DOCX creation and retained JSON receipt.
4. Open the corresponding `PPG-fictional-<run-ID>.docx` and `.json` in OneDrive →
   Documents → PPG-word-qualification. Check the revision, included rows and source/
   template identity against the receipt. Open/edit in Word and wait for the saved
   version; reopen it to verify. Keep the result DRAFT / HUMAN CHECK REQUIRED.
   Restore the pilot Off when the bounded test ends.

The supplied input is deliberately restricted to one fictional case/source/template.
Changing the bound template requires a new version/hash and native qualification;
do not relax the schema to process operational data incidentally. Record selection,
identity and business decisions stay in their authoritative layers.

## Failure and recovery

- Missing required fields or a mismatched fixed identity/hash fail at Parse accepted
  input before Word/output actions. A failed run is never a completed package.
- If observation times out, inspect the same native run and its exact output paths
  before submitting again. Do not infer failure or restart from an observation timeout.
- Correct invalid accepted input, retain the failed run reference and submit a new
  attempt/revision. An existing DOCX without its receipt is an incomplete attempt;
  preserve it and inspect the failed action before recovery.
- Resubmission deliberately creates another run-specific file and receipt. It does
  **not** provide exactly-once deduplication. Use occurrence/revision plus run ID to
  distinguish attempts; never replace a human-edited file to tidy duplicate attempts.
  Connector file-write retries are disabled; recovery is an inspected new attempt.

## Qualified shape and limits

Empty, one and three repeating paragraph groups, long multiline Unicode, optional
text inclusion/exclusion, editable save/reopen, missing-field rejection and native
resubmission preservation were checked. Long groups can continue across pages.
This is not conditional deletion of arbitrary Word sections, repeating tables,
embedded hyperlink authoring or a policy-content readiness check. Native output
links and same-account access were exercised; no wider audience access is inferred.

Compared with the manual route, this removes local Word population and retains a
native output/receipt pair, but still requires accepted JSON and an explicit run.
Observed fictional runs took approximately 3–4 seconds; end-to-end time savings
and operational benefits were not measured. Keep this Developer pilot for technical
reuse; retain the manual route until production licensing and one actual document
shape are qualified. Re-evaluate the preferred SharePoint structured-document route
when its maker entitlement and feature availability are confirmed.

Exact pilot links are recorded in the private deployment binding and appended to
the hosted copy. See [qualification and evidence](./native-document-generation.md).
