### TASK — D-001-T4: Introduce SQL-Backed Repositories (Create-Only, Parallel to Fake)

**Objective**

Introduce SQLAlchemy-backed repository implementations for `Person` and `Address` that support **create operations only**, operating **in parallel** with existing Fake repositories.

This task makes SQL persistence **usable** without altering system behavior or test authority.

---

**Authority**

* Directive: **D-001 — Introduction of SQL Persistence**
* Reference directives:

  * **D-000 — Fake Storage Scaffolding**
  * **D-001-T2 — ORM Persistence Models**
  * **D-001-T3 — Schema Binding and Table Creation**
* Applicable policies:

  * **P01 — Entity Naming and Role Disambiguation**
  * **P02 — Boundary vs Domain Modeling**
  * **P03 — No Global Mutable State**
  * **P05 — SQL-Based Persistence with ORM**
  * **P06 — Domain ↔ Persistence Mapping**

---

**Scope**

* Persistence layer only
* Repository abstraction only
* Create operation only
* Parallel implementation (Fake remains authoritative)

---

**Requirements**

1. Introduce repository classes:

   * `SqlPersonRepository`
   * `SqlAddressRepository`

2. Repositories MUST:

   * Use SQLAlchemy **2.x Session** semantics
   * Accept an explicit `session_factory` or `Session` provider
   * Create a new session per operation

3. Implement **create operations only**:

   * `create(person: Person)` for persons
   * `create(address: Address)` for addresses

4. Create operations MUST:

   * Persist data via ORM models (`PersonRow`, `AddressRow`)
   * Commit on success
   * Fail explicitly on constraint violations (e.g. duplicate primary key)

5. Repositories MUST NOT:

   * Implement read, update, or delete
   * Enforce invariants beyond database constraints
   * Contain domain logic
   * Import Fake repositories
   * Modify or remove Fake repositories

6. Mapping between domain entities and ORM rows MUST be:

   * Explicit
   * One-directional (domain → persistence)

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
* Do NOT remove Fake persistence
* Do NOT implement read/update/delete
* Do NOT introduce dependency injection frameworks
* Do NOT optimize performance

---

**Success Criteria**

* SQL-backed repositories exist and are importable
* Create operations persist rows correctly to SQLite
* Existing tests continue to pass unchanged
* Fake repositories remain the sole test authority
* No observable behavior changes occur
