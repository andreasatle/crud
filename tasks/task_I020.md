### TASK — Enforce I-020 (Address Lifecycle Closure and Dependency)

**Objective**
Enforce **Invariant I-020 — Address Lifecycle Closure and Dependency**, ensuring that `Address` lifecycle is correctly coupled to `Person` lifecycle.

---

### Authority

* **Invariant**: I-020 — Address Lifecycle Closure and Dependency
* **Enforcement test**:
  `tests/test_I020_address_lifecycle_closure_and_dependency.py`
* **Applicable policies**: P01, P02, P03, P04
  (P05–P06 remain out of scope)

---

### Required Behavior

The system MUST satisfy all of the following:

#### 1. Explicit Repository Dependency

* `FakeAddressStore` MUST accept a `FakePersonStore` instance at construction time.
* No global state or implicit lookup is allowed.

#### 2. Cascading Delete Semantics

* When a `Person` is deleted:

  * All `Address` entities with matching `person_id` MUST be deleted.
  * Deleted addresses MUST become unobservable.

#### 3. Address Lifecycle Closure

* Once an `Address` is deleted:

  * It MUST NOT be readable.
  * It MUST NOT be updatable.
  * Re-deletion MUST fail explicitly.

#### 4. Re-Creation Semantics

* Re-creating an `Address` with the same `id` after deletion:

  * MUST start a **new lifecycle**
  * MUST NOT resurrect prior state

#### 5. Existing Semantics Preserved

* All invariants **I-010 through I-019** MUST continue to hold.
* No behavior outside I-020 may change.

---

### Constraints

* No database
* No ORM
* No event system
* No observer pattern
* No background processes
* No implicit coupling
* No additional public API surface

Repositories must remain:

* explicit
* test-scoped
* deterministic
* minimal

---

### Non-Goals

* Do NOT introduce update semantics beyond what already exists.
* Do NOT introduce bidirectional ownership.
* Do NOT model transactions or isolation.
* Do NOT anticipate future persistence layers.

---

### Success Criteria

* `tests/test_I020_address_lifecycle_closure_and_dependency.py` passes.
* All prior invariant tests remain passing.
* Address lifecycle is provably dependent on Person lifecycle.
* No policy violations are introduced.
