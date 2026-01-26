### TASK — Enforce Invariant I-014 (Address Create Operation Semantics)

**Objective**

Introduce an explicit create operation for `Address` entities that enforces **I-014 — Address Create Operation Semantics**.

---

**Authority / Inputs**

* Invariant: **I-014 — Address Create Operation Semantics**
* Enforcement test:
  `tests/test_I014_address_create_operation_semantics.py`
* Applicable policies: **P01, P02, P03, P04**
* Out of scope: **P05–P06** (no real persistence)

---

**Requirements**

* Introduce a fake, in-memory persistence mechanism for addresses:

  * Class name: `FakeAddressStore`
  * Location: `src/crud/repository.py` (or equivalent repository module)

* `FakeAddressStore` MUST provide:

  * `create(address: Address, people: FakePersonStore) -> None`
  * `get_by_id(id: str) -> Optional[Address]`

* The create operation MUST enforce:

  * **Explicit creation** (construction ≠ registration)
  * **Uniqueness**:

    * Creating an `Address` with an existing `id` MUST fail
  * **Ownership existence**:

    * Creating an `Address` MUST fail if `address.person_id` does not refer to an existing `Person`
  * **Invariant enforcement**:

    * The `Address` passed to `create` MUST already satisfy invariants I-010–I-013

* On successful creation:

  * The `Address` MUST become observable via `get_by_id`

---

**Constraints**

* No global mutable state
* No database
* No ORM
* No API layer
* No Pydantic
* No concurrency or transaction semantics
* Repository instances MUST be explicit and test-scoped

---

**Non-Goals**

* Do NOT implement:

  * update operations
  * delete operations
  * list operations
* Do NOT anticipate future persistence or schema design
* Do NOT add lifecycle logic beyond creation

---

**Success Criteria**

* `tests/test_I014_address_create_operation_semantics.py` passes
* All existing invariant tests (I-001–I-013) continue to pass
* `FakeAddressStore` is minimal, explicit, and obviously fake
* No policy violations are introduced
