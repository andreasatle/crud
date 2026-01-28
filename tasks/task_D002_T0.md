### TASK — One-Time Refactor: Enforce Mandatory Person Context in Address Tests

**Objective**

Mechanically refactor all Address-related tests so that `FakeAddressStore` is **always constructed with an explicit `FakePersonStore`**, reflecting the now-closed domain where an `Address` cannot exist without a `Person`.

This task eliminates legacy ambiguity introduced before ownership invariants (I-016, I-017, I-020) fully closed the model.

---

**Authority**

* Governing invariants:

  * **I-016 — Address Ownership Referential Integrity**
  * **I-017 — Person–Address Lifecycle Coupling**
  * **I-020 — Address Lifecycle Closure and Dependency**
* Reference:

  * Consolidation of Fake repositories into `crud.repository`
* Classification:

  * **Mechanical refactor**
  * **Non-authoritative**
  * **One-time cleanup**

---

**Scope**

* Tests only
* Fake repositories only
* Address-related tests only

---

**Required Changes**

1. For **every test** that instantiates `FakeAddressStore`:

   * Replace:

     ```python
     repo = FakeAddressStore()
     ```

     with:

     ```python
     people = FakePersonStore()
     repo = FakeAddressStore(people)
     ```

2. Where an `Address` is created:

   * Ensure the owning `Person` exists in `people` **before** address creation:

     ```python
     people.create(Person(...))
     ```

3. Ensure **no test** constructs `FakeAddressStore` without a `FakePersonStore`.

---

**Constraints**

* Do NOT change invariant statements
* Do NOT modify Fake repository behavior
* Do NOT change test intent or assertions
* Do NOT introduce new helper fixtures
* Do NOT refactor production code
* No new tests

---

**Non-Goals**

* Do NOT reinterpret earlier invariants
* Do NOT introduce optional ownership
* Do NOT add default arguments or fallbacks
* Do NOT “fix” historical ledger ordering

---

**Success Criteria**

* All tests pass without conditional logic
* No occurrence of `FakeAddressStore()` without arguments remains
* Test suite reflects a **single closed domain model**
* No behavioral change beyond test setup

---

**One-Time Nature (Important)**

This task is **not reusable** and **must not be repeated**.

It exists solely to reconcile:

* early open-world test scaffolding
* with later closed-world invariants

After completion:

> All Fake-based tests assume mandatory Person → Address ownership.
