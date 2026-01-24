[INIT]
Created the project.
```bash
mkdir src tests tasks policies invariants
touch ledger.md README.md
uv init .
uv add pytest
```
Wrote the `README.md`.

[HELP-DOC]
Created a document `docs/HELP-DOCUMENT.md`. I noted that the output of invalid input is non-existent, but want to see what happens when we invalidate invariants later.

[POLICY]
Write 6 different policies.

[BOOTSTRAP]
Initialized `src/crud/api.py` with api-functions raising `NotImplementedError`.

[INVARIANT]
I-001 — Person Identity and Structure

[TEST]
test_I001_person_identity_and_structure

[TASK]
task_I001