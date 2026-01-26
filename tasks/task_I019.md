### TASK — Enforce I-019 (Address Delete Operation Semantics)

**Objective**
Implement explicit delete behavior for `Address` entities that satisfies **Invariant I-019 — Address Delete Operation Semantics**.

---

**Scope / Authority**

* Invariant: **I-019 — Address Delete Operation Semantics**
* Enforcement test:
  `tests/test_I019_address_delete_operation_semantics.py`
* Applicable policies: **P01, P02, P03, P04**
* Persistence model: **in-memory fake store**

---

**Requirements**

* Introduce or extend an explicit repository for `Address` (e.g. `FakeAddressStore`).

* The repository MUST provide:

  * `create(address: Address)`
  * `get_by_id(id: str)`
  * `delete(id: str)`

* Delete semantics MUST satisfy:

  * Deleting an existing `Address` removes it from the store.
  * After deletion, the `Address` MUST be treated as nonexistent.
  * Deleting an already-deleted or nonexistent `Address` MUST fail explicitly (e.g. raise `KeyError`).
  * Delete MUST NOT affect the owning `Person`.

---

**Constraints**

* No database or ORM.
* No API layer.
* No global mutable state.
* Repository instances MUST be explicit and test-scoped.
* Address identity MUST continue to be defined solely by `Address.id` (I-011).
* Do NOT implement cascading delete here (that is governed by I-017).

---

**Non-Goals**

* Do NOT make delete idempotent.
* Do NOT silently ignore missing ids.
* Do NOT introduce soft-delete flags.
* Do NOT add update or read behavior beyond what already exists.

---

**Success Criteria**

* `tests/test_I019_address_delete_operation_semantics.py` passes.
* All existing Address and Person invariant tests remain passing.
* Address deletion semantics are explicit, terminal, and isolated.
