### Task — Enforce Invariant I-005 (Person Create Operation Semantics) Using In-Memory Persistence

**Objective**
Implement an explicit, in-memory persistence mechanism for `Person` entities that enforces **Invariant I-005 — Person Create Operation Semantics**.

**Scope / Authority**

* Invariant: **I-005**
* Enforcement mechanism:
  `tests/test_invariant_I005_person_create_operation_semantics.py`
* Applicable policies: **P01, P02, P03, P04**
  (P05–P06 are intentionally out of scope.)

**Requirements**

* Introduce an explicit repository object (e.g. `InMemoryPersonRepository`).
* The repository MUST:

  * Provide a `create(person: Person)` operation.
  * Provide a `get_by_id(id: str)` operation.
* Creating a `Person` with a previously unused `id` MUST succeed.
* Creating a `Person` with an `id` that already exists MUST fail explicitly (e.g. raise an exception).
* The repository MUST NOT:

  * silently overwrite an existing entity
  * treat creation as an update
* Identity comparison MUST rely solely on `Person.id` (per I-002).
* The repository MUST preserve compliance with **I-001–I-004**.

**Constraints**

* No global mutable state (repository instances must be explicit and test-scoped).
* No database, ORM, or persistence framework.
* No Pydantic models.
* No API or CRUD layer abstractions beyond the repository itself.
* No additional behavior beyond what is required to satisfy the test.

**Non-Goals**

* Do NOT implement update or delete operations.
* Do NOT introduce persistence identifiers separate from `Person.id`.
* Do NOT anticipate future database or ORM structure.
* Do NOT enforce concurrency or transactional semantics.

**Success Criterion**

* `tests/test_invariant_I005_person_create_operation_semantics.py` passes.
* All existing invariant tests (I-001–I-004) continue to pass.
* No policy violations are introduced.
