# Native role-date validation qualification

An isolated versioned List qualifies two Text-column validators using existing
SharePoint access. Working role, source, lifecycle and recovery Lists are unchanged.
The [portable definition](../config/review-intelligence/role-date-validation-v1.json)
is marked prototype-only. It uses native [column validation](https://support.microsoft.com/en-us/sharepoint/lists/data-and-lists/create-a-column-in-a-list-or-library)
and [field validation properties](https://learn.microsoft.com/en-us/dotnet/api/microsoft.sharepoint.client.field.validationformula?view=sharepoint-csom).
Documentation is not tenant proof: actual creation, readback and saves below supply it.

The formula checks exact YYYY-MM-DD spelling and Gregorian calendar validity,
including century leap rules. End date may be blank. It does not use locale-sensitive
date parsing or serial-date conversion. Native formula readback removes brackets
around simple column references; the verifier permits that specific representation
and checks every other formula/message character.

Eighteen actual native cases passed: five valid dates saved; thirteen invalid
inputs refused. Tests cover leap/century dates, years0001/9999, invalid month/day,
compact/week/timestamp/whitespace forms, missing start and invalid optional end.
Native replay creates zero valid records. Only the exact SPListDataValidationException
is recognised as expected refusal; this target returns it under HTTP500. Other500s
remain failures. The native form displays the intended calendar-format message;
after cancellation, CLI confirms no invalid UI item was saved.

The qualification List has three custom fields/five fictional records, NoCrawl=true,
no Quick Launch entry and inherited web access. Seven evidence files have exact
byte/identity/version/readback and replay proof. Downloaded seven-member archive
passes CRC/all hashes and verifies formula/18-case/final-record evidence. It is
archived-proof verification, not an executed copied-native restore. Detailed URLs,
identities, receipts and screenshot remain private role-date-native-v1 and the
same-named companion in the approved review evidence library.

Do not apply this definition automatically to working Lists. First verify exact
field bindings and existing dates, preserve settings/records and qualify selected
writes/retries. Date ordering, overlap/reference/delegation/authority rules remain
separate; the existing role projection rejects ambiguity. No published workflow,
clinical role grant, source record, permission, notification or policy issue changed.


Later20October promotion: selected calendar checks are now applied to five working
role columns; see [working scope and recovery](working-role-date-validation.md).
The prototype definition and its qualification evidence remain unchanged.
