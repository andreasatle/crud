### TASK — **D-001-T7: Introduce SQL-Backed Repositories (Delete Operations, Parallel to Fake)**

**Objective**

Introduce **delete operations** to the SQLAlchemy-backed repositories for `Person` and `Address`, mirroring the semantics already defined and enforced by invariants and Fake repositories.

This task completes the **full CRUD surface** for SQL persistence (create, read, update, delete) while **Fake repositories remain the sole test authority**.

---

**Authority**

* Directive: **D-001 — Introduction of SQL Persistence**
* Reference directives:

  * **D-000 — Fake Storage Scaffolding**
  * **D-001-T4 — SQL-Backed Repositories (Create)**
  * **D-001-T5 — SQL-Backed Repositories (Read)**
  * **D-001-T6 — SQL-Backed Repositories (Update)**
* Governing invariants:

  * **I-008 — Person Delete Operation Semantics**
  * **I-009 — Person Lifecycle Closure and Irreversibility**
  * **I-019 — Address Delete Operation Semantics**
  * **I-020 — Address Lifecycle Closure and Dependency**
  * **I-017 — Person–Address Lifecycle Coupling (Cascade Delete)**
* Applicable policies:

  * **P01 — Entity Naming and Role Disambiguation**
  * **P03 — No Global Mutable State**
  * **P05 — SQL-Based Persistence with ORM**
  * **P06 — Domain ↔ Persistence Mapping**

---

**Scope**

* Persistence layer only
* Delete operations only
* SQL repositories only
* Parallel implementation (Fake remains authoritative)

---

**Requirements**

1. Extend existing SQL-backed repositories:

   * `SqlPersonRepository`
   * `SqlAddressRepository`

2. Implement delete operations:

   * `delete(person_id: str) -> None`
   * `delete(address_id: str) -> None`

3. Delete operations MUST:

   * Use SQLAlchemy **2.x Session** semantics
   * Create a new session per operation
   * Locate the target row by primary key
   * Remove the row explicitly
   * Commit on success

4. **Person delete semantics**:

   * Deleting a `Person` MUST delete all owned `Address` rows
   * Cascade behavior MAY be implemented via:

     * database-level foreign key cascade, **or**
     * explicit repository logic
   * No orphaned addresses may remain

5. **Address delete semantics**:

   * Deleting an `Address` MUST NOT affect the owning `Person`
   * Ownership is not reassigned

6. Delete operations MUST fail explicitly if:

   * The target entity does not exist

7. Mapping rules:

   * Identity is determined solely by `id`
   * No resurrection or soft-delete semantics
   * One-directional mapping (domain intent → persistence effect)

---

**Constraints**

* SQLAlchemy version: **>=2.0,<3.0**
* No test migration
* No Fake repository modification
* No global engine, session, or repository instances
* No lifecycle logic beyond delete semantics
* No soft deletes, flags, or tombstones

---

**Non-Goals**

* Do NOT migrate invariant tests to SQL
* Do NOT introduce audit logging or history tables
* Do NOT introduce optimistic locking or versioning
* Do NOT enforce additional invariants beyond deletion semantics
* Do NOT optimize performance or batching

---

**Success Criteria**

* SQL-backed repositories support delete operations for `Person` and `Address`
* Cascading delete semantics are correctly enforced for `Person → Address`
* Address delete leaves owning `Person intact
* All existing tests continue to pass unchanged
* Fake repositories remain the sole test authority
* SQL persistence now supports full CRUD in parallel to Fake
