### TASK — **D-001-T8: Repository Parity Verification (No Behavior Change)**

**Objective**

Establish and document that SQL-backed repositories now expose the **same operational surface** as the Fake repositories for `Person` and `Address`, completing the persistence scaffolding phase of **D-001**.

This task **does not introduce new behavior**.
It provides **explicit closure** for the SQL persistence introduction by verifying parity of supported operations.

---

**Authority**

* Directive: **D-001 — Introduction of SQL Persistence**
* Reference directives:

  * **D-000 — Fake Storage Scaffolding**
  * **D-001-T4 — Create (SQL)**
  * **D-001-T5 — Read (SQL)**
  * **D-001-T6 — Update (SQL)**
  * **D-001-T7 — Delete (SQL)**
* Governing invariants (reference only, not enforced here):

  * I-005–I-009 (Person CRUD + lifecycle)
  * I-014–I-020 (Address CRUD + lifecycle)
* Applicable policies:

  * **P01 — Entity Naming and Role Disambiguation**
  * **P03 — No Global Mutable State**
  * **P06 — Domain ↔ Persistence Mapping**

---

**Scope**

* Verification and documentation only
* Repository interfaces only
* No test authority shift
* No behavior changes

---

**What “parity” means (precise definition)**

For each entity (`Person`, `Address`), **SQL-backed repositories MUST expose the same callable operations** as their Fake counterparts:

| Operation | Fake Repository | SQL Repository |
| --------- | --------------- | -------------- |
| Create    | ✔︎              | ✔︎             |
| Read      | ✔︎              | ✔︎             |
| Update    | ✔︎              | ✔︎             |
| Delete    | ✔︎              | ✔︎             |

Parity is defined as **surface equivalence**, not semantic enforcement.

---

**Requirements**

1. Verify that:

   * `SqlPersonRepository` supports:

     * `create(person)`
     * `get_by_id(id)`
     * `update(person)`
     * `delete(id)`
   * `SqlAddressRepository` supports:

     * `create(address)`
     * `get_by_id(id)`
     * `update(address)`
     * `delete(id)`

2. Verification MUST be:

   * Explicit
   * Inspectable
   * Recorded (e.g. checklist, comment, or ledger entry)

3. This task MUST NOT:

   * Add new methods
   * Modify existing repository behavior
   * Introduce tests
   * Migrate tests from Fake to SQL
   * Alter invariants or directives

---

**Constraints**

* No code paths become authoritative
* No environment flags or switches
* No dependency injection changes
* SQL repositories remain unused by tests

---

**Non-Goals**

* Do NOT validate correctness of SQL behavior
* Do NOT compare Fake vs SQL outputs
* Do NOT introduce integration tests
* Do NOT remove Fake repositories
* Do NOT shift authority

---

**Validation Criteria (important)**

This task is considered **complete** when:

1. SQL repositories expose **create/read/update/delete** for both entities
2. All existing tests pass unchanged
3. No new behavior is observable from the test suite
4. Ledger records D-001 as **structurally complete**

---

**Outcome**

After this task:

* SQL persistence scaffolding is **structurally complete**
* Fake persistence remains authoritative
* The system is ready for a **single, explicit authority shift directive** (future work)

