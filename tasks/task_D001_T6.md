### TASK — D-001-T6: Introduce SQL-Backed Repositories (Update Operations, Parallel to Fake)

**Objective**

Introduce **update operations** to the SQLAlchemy-backed repositories for `Person` and `Address`, mirroring the semantics already defined and enforced by Fake repositories and invariants.

This task completes the SQL persistence surface for **create, read, and update**, while **Fake repositories remain authoritative**.

---

**Authority**

* Directive: **D-001 — Introduction of SQL Persistence**
* Reference directives:

  * **D-000 — Fake Storage Scaffolding**
  * **D-001-T4 — SQL-Backed Repositories (Create)**
  * **D-001-T5 — SQL-Backed Repositories (Read)**
* Governing invariants:

  * **I-007 — Person Update Operation Semantics**
  * **I-018 — Address Update Operation Semantics**
* Applicable policies:

  * **P01 — Entity Naming and Role Disambiguation**
  * **P02 — Boundary vs Domain Modeling**
  * **P03 — No Global Mutable State**
  * **P05 — SQL-Based Persistence with ORM**
  * **P06 — Domain ↔ Persistence Mapping**

---

**Scope**

* Persistence layer only
* Update operations only
* SQL repositories only
* Parallel implementation (Fake remains authoritative)

---

**Requirements**

1. Extend existing SQL-backed repositories:

   * `SqlPersonRepository`
   * `SqlAddressRepository`

2. Implement update operations:

   * `update(person: Person) -> None`
   * `update(address: Address) -> None`

3. Update operations MUST:

   * Use SQLAlchemy **2.x Session** semantics
   * Create a new session per operation
   * Locate the existing row by primary key (`id`)
   * Update **only non-identity fields**
   * Commit changes on success

4. Update operations MUST fail explicitly if:

   * The target entity does not exist
   * The update would violate database constraints

5. Mapping rules:

   * Identity is determined solely by `id`
   * No identity reassignment
   * Mapping is explicit and one-directional (domain → persistence)

---

**Constraints**

* SQLAlchemy version: **>=2.0,<3.0**
* No lifecycle logic
* No cascade behavior
* No invariant enforcement beyond DB constraints
* No Fake repository modification
* No test changes
* No global session, engine, or repository instances

---

**Non-Goals**

* Do NOT implement delete operations
* Do NOT migrate tests to SQL
* Do NOT introduce optimistic locking, versioning, or concurrency control
* Do NOT enforce ownership or lifecycle invariants here
* Do NOT change repository interfaces beyond adding update methods

---

**Success Criteria**

* SQL-backed repositories support update operations for `Person` and `Address`
* Update semantics mirror Fake behavior (I-007, I-018)
* Existing tests continue to pass unchanged
* Fake repositories remain the sole test authority
* No observable system behavior changes occur
