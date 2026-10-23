# Minimal implementation conventions

Use the established language/tool for the task; small functions and explicit
names. Keep source facts, local work and configuration separate. Use UTF-8,
ISO-8601 UTC event times and persistent IDs independent of source row position.
Check schema/payload assumptions and fail visibly rather than invent defaults.
Avoid whole-workbook scans per row, duplicate writes and broad last-write-wins.
Log codes and counts, not sensitive narrative. Never embed secrets or operational
IDs. Use synthetic examples in Git. Add a small regression check when fixing
identity or data-loss behaviour; no blanket coverage target or new framework.
