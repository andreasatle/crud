### **TASK — D-002-T1: Introduce SQL-Backed Test Fixtures**

**Objective**

Introduce reusable **SQL-backed pytest fixtures** that provide a fully initialized persistence environment for invariant tests, using **SQLite + SQLAlchemy 2.x**, with **no Fake persistence involved**.

This task establishes the foundation required to shift test authority from Fake → SQL in **D-002**.

---

**Authority**

* Directive: **D-002 — Switch Test Authority from Fake → SQL**
* Supersedes reliance on:

  * **D-000 — Fake Storage Scaffolding** (for test authority only)
* Reference work:

  * **D-001 — Introduction of SQL Persistence**
* Applicable policies:

  * **P01 — Entity Naming and Role Disambiguation**
  * **P03 — No Global Mutable State**
  * **P05 — SQL-Based Persistence with ORM**
  * **P06 — Domain ↔ Persistence Mapping**
  * **P07 — Test Authority Must Be Explicit**

---

**Scope**

* Test infrastructure only
* SQL-backed persistence only
* No domain or repository behavior changes

---

**Requirements**

1. Introduce pytest fixtures that provide:

   * A **SQLite in-memory database**
   * A SQLAlchemy **Engine**
   * Bound ORM metadata (schema created)
   * A **Session factory**
   * SQL-backed repositories:

     * `SqlPersonRepository`
     * `SqlAddressRepository`

2. Database properties:

   * Use **SQLite in-memory** (`sqlite:///:memory:`)
   * Schema MUST be created fresh per test
   * No shared state across tests

3. Fixtures MUST:

   * Be deterministic
   * Avoid global state
   * Avoid side effects at import time
   * Be isolated per test invocation

4. Repositories returned by fixtures MUST:

   * Be fully functional for:

     * create
     * read
     * update
     * delete
   * Match the Fake repository surface exactly

5. Fixtures MUST NOT:

   * Import or reference Fake repositories
   * Modify existing tests yet
   * Change any invariant tests
   * Introduce behavior or lifecycle logic

---

**Constraints**

* SQLAlchemy version: **>=2.0,<3.0**
* pytest fixtures only (no unittest)
* No monkeypatching
* No dependency injection frameworks
* No test parametrization yet (that comes later)

---

**Non-Goals**

* Do NOT switch any tests to SQL yet
* Do NOT remove Fake repositories
* Do NOT introduce dual-backend testing
* Do NOT enforce invariants here
* Do NOT optimize performance

---

**Deliverables**

* One or more pytest fixtures (e.g. in `tests/conftest.py`) providing:

  * `sql_engine`
  * `sql_session_factory`
  * `sql_person_repo`
  * `sql_address_repo`
* Fixtures are importable and reusable by invariant tests
* All existing tests continue to pass unchanged

---

**Success Criteria**

* SQL-backed fixtures create a fresh, isolated database per test
* ORM schema is created correctly
* SQL repositories operate correctly when used manually
* No Fake persistence is involved anywhere in these fixtures
* Test suite passes without modification

---

**Outcome**

After this task:

* SQL persistence is **test-ready**
* Test authority can be shifted safely in later tasks
* Fake persistence is no longer required for new tests
* The system has a clear, explicit transition path from Fake → SQL
