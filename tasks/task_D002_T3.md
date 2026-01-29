### **TASK — D-002-T3: Flip Test Authority to SQL and Remove Fake-Specific Crutches**

---

## **Objective**

Make **SQL repositories the authoritative implementation for invariant tests**, while keeping Fake repositories only as **auxiliary scaffolding**.

After this task:

* SQL behavior defines correctness
* Fake behavior must *conform* to SQL semantics
* No test logic compensates for backend differences
* No adapter logic exists in production code or tests

This completes **D-002: Test Authority Migration**.

---

## **Authority**

* Directive: **D-002 — Switch Test Authority from Fake → SQL**
* Precondition tasks:

  * **D-002-T1 — SQL-Backed Test Fixtures**
  * **D-002-T2 — Parameterize Repositories in Tests**
* Governing invariants:

  * **I-001 through I-020**
* Scope-limiting constraints:

  * No invariant rewrites
  * No semantic loosening
  * No backend-specific branching in tests

---

## **Problem Statement**

After D-002-T2:

* Tests are backend-agnostic
* SQL and Fake both run
* BUT:

  * Some SQL behavior required adapters / deleted-ID tracking
  * Fake and SQL error semantics were not fully aligned
  * SQL delete / read / cascade semantics were being patched instead of defined

This task **eliminates those compensations** and **locks SQL as ground truth**.

---

## **Core Rule (New Authority Rule)**

> **Invariant tests express SQL semantics. Fake repositories must conform.**

This is a **one-way constraint**:

* Tests do **not** adapt to Fake
* Fake adapts (or is removed later)

---

## **Scope**

### Included

* Repository implementations
* Test fixtures
* Removal of temporary compatibility logic

### Explicitly Excluded

* Invariant changes
* Test logic changes
* New features
* Performance work
* Production APIs

---

## **Required Changes**

### **1. Remove Adapter / Compatibility Logic**

Eliminate **all SQL-only compensations**, including:

* Deleted-ID tracking
* Session-factory state hacks
* “Fake-like” behavior emulation inside SQL repositories

**SQL repositories must rely only on:**

* Database state
* Constraints
* Explicit error handling

---

### **2. Normalize Repository Semantics (Authoritative Set)**

Repositories MUST implement the following semantics consistently:

#### **Address.get_by_id**

| State                          | Behavior      |
| ------------------------------ | ------------- |
| Exists                         | Return entity |
| Never existed                  | `KeyError`    |
| Deleted (explicit or cascaded) | `None`        |

#### **Address.delete**

| State           | Behavior   |
| --------------- | ---------- |
| Exists          | Delete     |
| Already deleted | `KeyError` |
| Never existed   | `KeyError` |

#### **Person.delete**

| Requirement                                        |
| -------------------------------------------------- |
| Cascades to all owned addresses                    |
| Atomic (no partial state)                          |
| Post-delete: person and addresses are unobservable |

These semantics already exist in tests — SQL must satisfy them **natively**.

---

### **3. Enforce Cascade via Database, Not Python**

* Use **foreign keys with `ON DELETE CASCADE`**
* No manual address deletes
* No post-hoc tracking

SQLAlchemy mappings must express lifecycle rules, not repositories.

---

### **4. Remove Backend Parameterization (SQL-Only by Default)**

Modify test fixtures so that:

* **SQL is the default and primary backend**
* Fake may remain:

  * As an optional param
  * Or behind a clearly labeled switch
* CI must run SQL tests unconditionally

This may be as simple as:

```python
@pytest.fixture
def person_repo(sql_session_factory):
    return SqlPersonRepository(sql_session_factory)
```

Fake usage must no longer be implicit.

---

### **5. Make Fake Repositories Conform (Minimal Work)**

Fake repositories must:

* Match SQL semantics exactly
* Raise the same exceptions
* Exhibit the same lifecycle behavior

If this is non-trivial:

* Add TODO markers
* Do **not** bend SQL to match Fake

---

## **Constraints**

* ❌ No adapters
* ❌ No state shadowing
* ❌ No test branching
* ❌ No invariant edits
* ❌ No “temporary” logic

Everything removed in this task must be **monotonic deletion**.

---

## **Deliverables**

* SQL repositories that pass **all invariant tests without adapters**
* Clean test fixtures with SQL authority
* Removal of:

  * Deleted-ID tracking
  * Adapter classes
  * SQL-specific hacks added in D-002-T2
* Fake repositories either:

  * Conformant, or
  * Explicitly marked as secondary / deprecated

---

## **Success Criteria**

* All invariant tests pass with **SQL only**
* Deleting a person cascades via DB, not Python
* Deleted addresses are unobservable, not error-masked
* No repository inspects test state
* No repository stores cross-request memory

---

## **Outcome**

After D-002-T3:

* SQL is the **source of truth**
* Tests express **domain invariants only**
* Persistence semantics are **real**, not simulated
* The system is ready for:

  * Removing Fake entirely (future task)
  * Introducing additional backends safely
  * Trustworthy production behavior
