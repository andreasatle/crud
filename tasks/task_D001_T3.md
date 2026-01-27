### TASK — D-001-T3: Bind Metadata and Create Tables (SQLite, No Repositories)

**Objective**

Activate the SQLAlchemy persistence schema by binding metadata and creating database tables, using SQLite, **without introducing any domain behavior or repository logic**.

This task validates that the ORM models introduced in **D-001-T2** form a coherent, realizable schema.

---

**Authority**

* Directive: **D-001 — Introduction of SQL Persistence**
* Reference directives:

  * **D-000 — Fake Storage Scaffolding**
  * **D-001-T2 — ORM Persistence Models**
* Applicable policies:

  * **P01 — Entity Naming and Role Disambiguation**
  * **P03 — No Global Mutable State**
  * **P05 — SQL-Based Persistence with ORM**

---

**Scope**

* Persistence infrastructure only
* Schema activation only
* No behavioral semantics

---

**Requirements**

1. Use SQLAlchemy **2.x semantics** exclusively.

2. Create a SQLite database using:

   * an explicit database URL
   * the existing engine factory (`create_engine_from_url`)

3. Bind ORM metadata explicitly:

   * Use `Base.metadata`
   * No implicit binding
   * No global state

4. Create tables via:

   * `Base.metadata.create_all(engine)`

5. The task MUST:

   * Operate in an explicit function or script
   * Be callable without side effects on import

---

**Constraints**

* SQLAlchemy version: **>=2.0,<3.0**
* SQLite only (file-based or in-memory)
* No repositories
* No sessions used for CRUD
* No domain model imports
* No Fake storage modification
* No test changes

---

**Non-Goals**

* Do NOT introduce repository classes
* Do NOT migrate tests to SQL
* Do NOT drop or modify tables
* Do NOT introduce lifecycle, cascade, or constraint logic beyond schema creation
* Do NOT remove or bypass Fake persistence

---

**Success Criteria**

* Database tables corresponding to:

  * `PersonRow`
  * `AddressRow`
    are successfully created.
* Schema creation completes without error.
* All existing tests continue to pass unchanged.
* No behavioral semantics are introduced.
