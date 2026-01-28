### TASK — D-001-T5: Introduce SQL-Backed Repositories (Read-Only, Parallel to Fake)

**Objective**

Introduce **read-only** operations to the SQLAlchemy-backed repositories for `Person` and `Address`, enabling SQL persistence to return persisted data **without changing test authority or system behavior**.

This task completes the **minimum usable read/write surface** for SQL persistence while Fake repositories remain authoritative.

---

**Authority**

* Directive: **D-001 — Introduction of SQL Persistence**
* Reference directives:

  * **D-000 — Fake Storage Scaffolding**
  * **D-001-T2 — ORM Persistence Models**
  * **D-001-T3 — Schema Binding and Table Creation**
  * **D-001-T4 — SQL-Backed Repositories (Create-Only)**
* Applicable policies:

  * **P01 — Entity Naming and Role Disambiguation**
  * **P02 — Boundary vs Domain Modeling**
  * **P03 — No Global Mutable State**
  * **P05 — SQL-Based Persistence with ORM**
  * **P06 — Domain ↔ Persistence Mapping**

---

**Scope**

* Persistence layer only
* Read operations only
* Parallel implementation (Fake remains authoritative)

---

**Requirements**

1. Extend existing SQL-backed repositories:

   * `SqlPersonRepository`
   * `SqlAddressRepository`

2. Implement **read operations only**:

   * `get_by_id(id: str)` for persons
   * `get_by_id(id: str)` for addresses

3. Read operations MUST:

   * Use SQLAlchemy **2.x Session** semantics
   * Create a new session per operation
   * Return a **domain entity** (`Person` / `Address`) constructed explicitly from ORM rows
   * Return `None` if the entity does not exist

4. Mapping MUST be:

   * Explicit
   * One-directional (persistence → domain)
   * Free of domain logic or invariant enforcement

5. Repositories MUST NOT:

   * Implement update or delete
   * Enforce invariants beyond what the database already enforces
   * Modify Fake repositories
   * Alter existing tests

---

**Constraints**

* SQLAlchemy version: **>=2.0,<3.0**
* No global engine, session, or repository instances
* No implicit session scope
* No test changes
* No Fake storage changes
* No cascade or lifecycle logic

---

**Non-Goals**

* Do NOT migrate any tests to SQL
* Do NOT introduce list operations unless already defined in Fake
* Do NOT optimize queries
* Do NOT introduce caching or identity maps
* Do NOT change repository interfaces beyond adding read methods

---

**Success Criteria**

* SQL-backed repositories can retrieve persisted `Person` and `Address` entities by id
* Returned objects match domain model shape
* All existing tests continue to pass unchanged
* Fake repositories remain the sole test authority
* No observable behavior changes occur
