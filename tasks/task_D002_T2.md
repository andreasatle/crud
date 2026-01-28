### **TASK — D-002-T2: Parameterize Repositories in Invariant Tests**

**Objective**

Refactor invariant tests so they can run **unchanged in logic** against **either Fake or SQL-backed repositories**, by injecting repositories via fixtures instead of constructing them directly.

This task decouples **test intent** from **persistence backend**, enabling a controlled transition of test authority in **D-002**.

---

### **Authority**

* Directive: **D-002 — Switch Test Authority from Fake → SQL**
* Reference work:

  * **D-002-T1 — SQL-Backed Test Fixtures**
  * **D-000 — Fake Storage Scaffolding**
* Governing invariants:

  * All existing invariants **I-001 through I-020**
* Applicable policies:

  * **P02 — Boundary vs Domain Modeling**
  * **P03 — No Global Mutable State**
  * **P07 — Test Authority Must Be Explicit**
  * **P08 — Tests Must Not Encode Infrastructure Choices**

---

### **Scope**

* Test layer only
* Mechanical refactor only
* No behavior changes
* No invariant changes

---

### **Core Rule**

> **Invariant tests must not know which persistence backend they are using.**

The same test logic MUST execute correctly against:

* Fake repositories, and
* SQL-backed repositories.

---

### **Requirements**

1. **Remove direct construction of repositories** in tests:

   * ❌ `FakePersonStore()`
   * ❌ `FakeAddressStore(...)`

2. Replace with **injected fixtures**, e.g.:

   * `person_repo`
   * `address_repo`

3. Introduce **backend-agnostic repository fixtures** that:

   * Yield either Fake or SQL repositories
   * Match the same repository interface

4. Tests MUST:

   * Use only repository methods (`create`, `get_by_id`, `update`, `delete`)
   * Never import Fake or SQL classes directly
   * Never branch on backend type
   * Never reference persistence-specific behavior

5. Parameterization strategy MUST be explicit and readable, e.g.:

   * `@pytest.fixture(params=["fake", "sql"])`
   * or equivalent indirection via composed fixtures

6. Fake repositories MUST continue to work exactly as before.

---

### **Constraints**

* No test logic changes beyond repository acquisition
* No assertion changes
* No invariant renumbering or rewriting
* No SQL-specific assertions
* No conditional logic in tests (`if sql: ...`)
* No duplication of tests per backend

---

### **Non-Goals**

* Do NOT remove Fake repositories
* Do NOT change repository semantics
* Do NOT enforce SQL-only behavior yet
* Do NOT change test names or structure
* Do NOT introduce performance optimizations

---

### **Deliverables**

* Updated invariant tests that:

  * Depend only on injected repositories
  * Are backend-agnostic
* One or more pytest fixtures that:

  * Provide a `person_repo` and `address_repo`
  * Can switch between Fake and SQL backends
* All tests pass against **both** backends

---

### **Success Criteria**

* Each invariant test runs successfully with:

  * Fake repositories
  * SQL repositories
* Test logic is identical for both backends
* No test imports Fake or SQL repository classes directly
* Backend choice is controlled solely by fixtures
* The system is now prepared for **test authority flip** in D-002-T3

---

### **Outcome**

After this task:

* Tests express **pure domain intent**
* Persistence becomes a **plug-in concern**
* Switching authority Fake → SQL becomes a one-line fixture change
* The framework achieves true backend-independence at the test level
