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
test_I001_person_identity_and_structure, failed

[TASK]
task_I001

[IMPLEMENTATION]

[VALIDATION]
test pass

[INVARIANT]
I-002 — Person Identity Semantics and Stability

[TEST]
test_I002_person_identity_semantics_and_stability, failed

[TASK]
task_I002

[IMPLEMENTATION]

[VALIDATION]
test pass

[INVARIANT]
I-003 — Person Update and Mutation Semantics

[TEST]
test_I003_person_update_and_mutation_semantics, passed

[INVARIANT]
I-004 — Person Creation Semantics

[TEST]
test_I004_person_creation_semantics, passed

[INVARIANT]
I-005 — Person Create Operation Semantics

[TEST]
test_I005_person_create_operation_semantics, failed

[TASK]
task_I005

[IMPLEMENTATION]

[VALIDATION]
test pass

[INVARIANT]
I-006 — Person Read Operation Semantics

[TEST]
test_I006_person_read_operation_semantics, passed

[INVARIANT]
I-007 — Person Update Operation Semantics

[TEST]
test_I007_person_update_operation_semantics, failed

[TASK]
task_I007

[IMPLEMENTATION]

[VALIDATION]
test pass

[INVARIANT]
I-008 — Person Delete Operation Semantics

[TEST]
test_I008_person_delete_operation_semantics, failed

[TASK]
task_I008

[IMPLEMENTATION]

[VALIDATION]
test pass

[INVARIANT]
I-009 — Person Lifecycle Closure and Irreversibility

[TEST]
test_I009_person_lifecycle_closure_and_irreversibility, passed

[INVARIANT]
I-010 — Address Identity and Structure

[TEST]
test_I010_address_identity_and_structure, failed

[TASK]
task_I010

[IMPLEMENTATION]

[VALIDATION]
test pass

[INVARIANT]
I-011 — Address Identity and Structure

[TEST]
test_I011_address_identity_and_structure, failed

[TASK]
task_I011

[IMPLEMETATION]

[VALIDATION]
test pass

[INVARIANT]
I-012 — Address Update and Mutation Semantics

[TEST]
test_I012_address_update_and_mutation_semantics, passed

[INVARIANT]
I-013 — Address Creation Semantics

[TEST]
test_I013_address_creation_semantics, passed

[INVARIANT]
I-014 — Address Create Operation Semantics

[TEST]
test_I014_address_create_operation_semantics, failed

[TASK]
task_I014

[IMPLEMETATION]

[VALIDATION]
test pass

[INVARIANT]
I-015 — Address Read Operation Semantics

[TEST]
test_I015_address_read_operation_semantics, failed

[TASK]
task_I015

[IMPLEMENTATION]

[VALIDATION]
test pass

[NOTE]
I realized that I-013 and I-014 has to be hardened.
An address require a person, and that person has to exist.
We can add an invariant instead of going back.

[INVARIANT]
I-016 — Address Ownership Referential Integrity

[TEST]
test_I016_address_ownership_referential_integrity, passed

[INVARIANT]
I-017 — Person–Address Lifecycle Coupling (Cascading Delete Semantics)

[TEST]
test_I017_person_address_lifecycle_coupling_cascade_delete, failed

[TASK]
task_I017

[IMPLEMENTATION]

[VALIDATION]
test pass

[INVARIANT]
I-018 — Address Update Operation Semantics

[TEST]
test_I018_address_update_operation_semantics, passed

[INVARIANT]
I-019 — Address Delete Operation Semantics (precise definition)

[TEST]
test_I019_address_delete_operation_semantics, failed

[TASK]
task_I019

[IMPLEMENTATION]

[VALIDATION]
test passed

[INVARIANT]
I-020 — Address Lifecycle Closure and Dependency

[TEST]
test_I020_address_lifecycle_closure_and_dependency, failed

[TASK]
task_I020

[IMPLEMENTATION]

[VALIDATION]
test passed

[NOTE]
* The first round of invariants are done.
* Next is to transfer the persistence to SqlAlchemy 2.0.
* We introduced the notion of directives that takes the place of invariants.
* We wrote a backtracked Fake storage directive for the existing scaffolding.
* I'm not sure how that would have been introduced, if it would have at all.

[DIRECTIVE]
D-001 - Introduction of SQL Persistence

[PREREQUISITE]
PR-001 — SQLAlchemy 2.x availability
```
uv add "sqlalchemy>=2.0,<3.0"
```
[TASK]
Task — D-001-T1: Introduce SQLAlchemy 2.x Persistence Skeleton