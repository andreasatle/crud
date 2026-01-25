### Task — Enforce Invariant I-007 (Person Update Operation Semantics)

**Objective**
Extend the existing fake, in-memory persistence mechanism to support an explicit update operation that enforces **Invariant I-007 — Person Update Operation Semantics**.

**Scope / Authority**

* Invariant: **I-007**
* Enforcement mechanism:
  `tests/test_I007_person_update_operation_semantics.py`
* Applicable policies: **P01, P02, P03, P04**
  (P05–P06 remain out of scope.)

**Requirements**

* Extend `FakePersonStore` with an explicit `update(person: Person)` operation.
* The update operation MUST:

  * Fail explicitly if no existing entity with the same `id` exists.
  * Preserve entity identity (`id` MUST NOT change).
  * Update only non-identity fields (`name`, `email`).
* The update operation MUST NOT:

  * Create a new entity as a side effect.
  * Change the identity of an existing entity.
  * Silently upsert or overwrite creation semantics.
* After a successful update, a subsequent read (`get_by_id`) MUST return the updated entity.
* Identity comparison MUST rely solely on `Person.id` (per I-002).
* The solution MUST preserve compliance with **I-001–I-006**.

**Constraints**

* No global mutable state.
* No database, ORM, or persistence framework.
* No Pydantic models.
* No API or CRUD layer abstractions beyond the fake store.
* No additional behavior beyond what is required to satisfy the test.

**Non-Goals**

* Do NOT implement partial updates or patch semantics.
* Do NOT introduce versioning, timestamps, or audit history.
* Do NOT anticipate concurrency, locking, or transactional behavior.
* Do NOT refactor the fake store into a reusable repository interface.

**Success Criterion**

* `tests/test_I007_person_update_operation_semantics.py` passes.
* All existing invariant tests (I-001–I-006) continue to pass.
* No policy violations are introduced.
