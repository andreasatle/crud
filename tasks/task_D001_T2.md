### TASK — D-001-T2: Introduce ORM Persistence Models for Person and Address (Structure Only)

**Objective**

Introduce SQLAlchemy 2.x ORM persistence models for `Person` and `Address` that represent persisted state **without introducing any behavior**.

This task establishes the **structural persistence layer** that will later be wired into repositories and operations.

---

**Authority**

* Directive: **D-001 — Introduction of SQL Persistence**
* Reference: **D-000 — Fake Storage Scaffolding**
* Applicable policies:

  * **P01 — Entity Naming and Role Disambiguation**
  * **P02 — Boundary vs Domain Modeling**
  * **P03 — No Global Mutable State**
  * **P04 — Object-Oriented Structure Preference**
  * **P05 — SQL-Based Persistence with ORM**
  * **P06 — Domain ↔ Persistence Mapping**

---

**Scope**

* Persistence layer only
* Structure only (schema representation)
* No behavioral semantics

---

**Requirements**

1. Define ORM-mapped classes using SQLAlchemy **2.x DeclarativeBase**:

   * `PersonRow`
   * `AddressRow`

2. `PersonRow` MUST define:

   * `id` — primary key
   * `name`
   * `email`

3. `AddressRow` MUST define:

   * `id` — primary key
   * `person_id` — foreign key referencing `PersonRow.id`
   * `street`
   * `city`
   * `postal_code`
   * `country`

4. ORM models MUST:

   * Be persistence-only representations
   * Contain **no domain logic**
   * Contain **no invariant enforcement**
   * Contain **no CRUD operations**

5. ORM models MUST NOT:

   * Import domain models
   * Reference Fake stores
   * Create sessions or engines
   * Bind metadata or create tables

6. Naming MUST:

   * Clearly distinguish persistence models from domain entities
   * Use a `Row` suffix (`PersonRow`, `AddressRow`)

---

**Constraints**

* SQLAlchemy version: **>=2.0,<3.0**
* No Pydantic
* No global mutable state
* No side effects at import time

---

**Non-Goals**

* Do NOT implement repositories
* Do NOT wire Fake storage to SQL
* Do NOT modify or add tests
* Do NOT introduce lifecycle or cascade behavior
* Do NOT remove Fake storage

---

**Success Criteria**

* ORM models are defined and importable
* They accurately represent the persisted schema
* All existing tests continue to pass unchanged
* No behavior is introduced beyond structure
