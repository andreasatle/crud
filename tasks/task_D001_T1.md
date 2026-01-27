### Task — D-001-T1: Introduce SQLAlchemy 2.x Persistence Skeleton

**Objective**
Begin the transition from Fake in-memory persistence to real SQL-backed persistence by introducing a **minimal, non-invasive SQLAlchemy 2.x skeleton**, without changing domain invariants or tests.

**Directive Authority**

* **D-001 — SQL Persistence Introduction**
* References **D-000 — Fake Persistence Baseline**

**Applicable Policies**

* **P02 — Boundary vs Domain Modeling**
* **P03 — No Global Mutable State**
* **P05 — SQL-Based Persistence with ORM**
* **P06 — Domain ↔ Persistence Mapping**

**Requirements**

1. **ORM Selection & Versioning**

   * SQLAlchemy **2.x semantics are mandatory**.
   * Accepted versions: `>=2.0,<3.0`.
   * Legacy 1.x patterns (`session.query`, implicit engine execution, etc.) are forbidden.

2. **Scope of This Task**

   * Introduce:

     * SQLAlchemy engine creation
     * declarative base
     * session factory
   * No domain entities may import SQLAlchemy.
   * No Fake storage may be removed or modified.

3. **Isolation**

   * ORM code MUST live in a new persistence module (e.g. `src/crud/persistence/`).
   * Domain (`Person`, `Address`) remains unchanged.
   * Tests continue to use Fake stores.

4. **No Behavioral Changes**

   * Do NOT wire SQL persistence into application logic.
   * Do NOT replace Fake stores.
   * Do NOT add migrations or schemas yet.

**Constraints**

* No global sessions or engines.
* No implicit configuration.
* No side effects at import time.
* No test rewrites.

**Non-Goals**

* Do NOT persist real data yet.
* Do NOT enforce invariants via the database.
* Do NOT introduce CRUD repositories backed by SQL.
* Do NOT remove Fake implementations.

**Success Criteria**

* SQLAlchemy 2.x infrastructure exists and imports cleanly.
* All existing invariant tests still pass unchanged.
* Fake persistence remains the active execution path.
* No policy violations introduced.

