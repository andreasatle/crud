### TASK — Enforce Invariant I-017 (Person–Address Lifecycle Coupling)

**Objective**
Enforce cascading delete semantics between `Person` and `Address` entities such that deleting a `Person` deletes all owned `Address` entities atomically.

---

### Scope / Authority

* Invariant: **I-017 — Person–Address Lifecycle Coupling (Cascading Delete Semantics)**
* Enforcement test:
  `tests/test_I017_person_address_lifecycle_coupling.py`
* Applicable policies: **P01, P02, P03, P04**
* Explicitly builds on:

  * I-008 — Person Delete Operation Semantics
  * I-016 — Address Ownership Referential Integrity

---

### Requirements

#### Person deletion

* Extend the `Person` delete operation so that:

  * Deleting a `Person` deletes **all Address entities owned by that Person**.
  * No owned `Address` remains after the delete completes.

#### Address invalidation

* After a `Person` is deleted:

  * All previously owned `Address` entities MUST be treated as nonexistent.
  * Read, update, or delete operations on those `Address` entities MUST fail explicitly.

#### Atomicity (logical)

* The delete operation MUST behave as a single logical transition:

  * The system MUST NOT expose a state where:

    * the `Person` is deleted but owned `Address` entities still exist, or
    * owned `Address` entities are deleted while the `Person` still exists.

---

### Enforcement Mechanism

* Use existing in-memory repositories:

  * `FakePersonStore`
  * `FakeAddressStore`
* The cascade MUST be explicit:

  * `FakePersonStore.delete(...)` may accept a reference to `FakeAddressStore`
  * No global state is allowed

---

### Constraints

* No database, ORM, or persistence framework.
* No Pydantic.
* No API layer.
* No concurrency or transaction primitives.
* No additional lifecycle semantics beyond cascade delete.
* No resurrection logic.

---

### Non-Goals

* Do NOT implement soft delete.
* Do NOT implement history or audit logging.
* Do NOT introduce bidirectional references.
* Do NOT change identity semantics for either entity.
* Do NOT enforce ordering of physical deletes beyond logical atomicity.

---

### Success Criteria

* `tests/test_I017_person_address_lifecycle_coupling.py` passes.
* All existing invariant tests (I-001–I-016) continue to pass.
* Cascading delete semantics are enforced only where required.
* No new policy violations are introduced.
