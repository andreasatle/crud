### TASK — Enforce Invariant I-015 (Address Read Operation Semantics)

**Objective**
Implement read semantics for `Address` entities that enforce **Invariant I-015 — Address Read Operation Semantics**.

---

### Scope / Authority

* Invariant: **I-015 — Address Read Operation Semantics**
* Enforcement test:
  `tests/test_I015_address_read_operation_semantics.py`
* Applicable policies: **P01, P02, P03, P04**
* Explicitly **out of scope**:

  * ownership validation
  * cascading delete behavior
  * person–address lifecycle coupling

---

### Requirements

* Provide a read operation for `Address` entities.
* The read operation MUST:

  * Return the persisted `Address` when it exists.
  * Fail explicitly when the requested `Address` does not exist.
* Reading an `Address` MUST NOT:

  * mutate state
  * create entities
  * resurrect deleted entities
* Returned `Address` MUST:

  * Preserve identity semantics (I-011).
  * Reflect the last persisted state.

---

### Enforcement Mechanism

* Use an explicit in-memory repository (e.g. `FakeAddressStore`).
* The repository MUST expose:

  * `create(address: Address)`
  * `get_by_id(address_id: str)`

---

### Constraints

* No database, ORM, or persistence framework.
* No global mutable state.
* No Pydantic.
* No API layer.
* Repository instances must be test-scoped.
* No additional behavior beyond what the test requires.

---

### Non-Goals

* Do NOT enforce that an Address must belong to a Person.
* Do NOT validate `person_id`.
* Do NOT introduce delete or update logic.
* Do NOT anticipate cascading semantics.

---

### Success Criteria

* `tests/test_I015_address_read_operation_semantics.py` passes.
* All existing invariant tests (I-010–I-014) continue to pass.
* Read behavior is well-defined for:

  * existing addresses
  * nonexistent addresses
