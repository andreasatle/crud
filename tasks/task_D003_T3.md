### **TASK — D-003-T3: Declare Cascade Authority Explicitly**

## **Objective**

Make **cascade-delete authority explicit and non-removable**, so that:

* The authoritative cascade mechanism is unambiguous
* Redundant or reinforcing mechanisms are clearly labeled
* “Cleanup” or simplification cannot silently change lifecycle semantics

This task introduces **no new behavior** and performs **no cascade logic changes**.

---

## **Authority**

* Directive: **D-003 — Persistence Hardening (Post-Authority)**
* Precondition:
  * **D-003-T1 — Persistence Hardening and Semantic Freeze**
  * **D-003-T2 — Freeze Error Semantics by Documentation**
* Governing invariants:
  * **I-017, I-019, I-020** (and related lifecycle invariants)
* Constraints:
  * No invariant changes
  * No semantic changes
  * No cascade logic changes
  * Documentation and comments only

---

## **Problem Statement**

Current cascade behavior relies on **multiple cooperating mechanisms**, including:

* Database-level foreign keys (`ON DELETE CASCADE`)
* Repository-level logic (e.g. tombstones, ordering, explicit deletes)

While correct per invariants, this redundancy:

* appears accidental
* invites “simplification”
* risks breaking lifecycle closure if altered casually

This task makes cascade authority **explicit and defended**.

---

## **Core Rule**

> **Cascade semantics are frozen; the authoritative mechanism must be explicit.**

No cascade-related logic may be removed, reordered, or simplified unless:
* a new directive authorizes it, and
* invariants are expanded to cover the change.

---

## **Scope**

### Included

* SQL persistence models
* SQL repository cascade-related logic
* Documentation and comments explaining cascade authority

### Explicitly Excluded

* ORM mapping changes
* Repository logic changes
* Invariant changes
* Test changes
* Performance or cleanup refactors

---

## **Required Changes**

### **1. Declare the Authoritative Cascade Mechanism**

Add explicit documentation stating:

* Which mechanism is **authoritative** for cascade semantics  
  (e.g. database foreign-key `ON DELETE CASCADE`)
* Which mechanisms are:
  * reinforcing
  * defensive
  * lifecycle-tracking (e.g. tombstones)

This declaration must be placed where a reader would expect to “simplify” logic.

---

### **2. Mark Redundant Cascade Logic as Intentional**

For any non-authoritative cascade-related code:

* Add comments stating it is:
  * intentional
  * semantically required
  * not removable without directive approval

Do **not** justify via performance or convenience — only semantics.

---

### **3. Forbid Cascade Cleanup Without Directive**

Document explicitly that the following are forbidden without a new directive:

* Removing repository-level cascade logic
* Relying solely on ORM defaults
* Collapsing multi-step deletes into a single mechanism
* Reordering delete operations

---

## **Constraints**

* ❌ No cascade behavior changes
* ❌ No ORM remapping
* ❌ No repository refactors
* ❌ No test updates
* ❌ No abstraction introduction

Only **documentation and comments** are permitted.

---

## **Validation Standard**

This task is complete when:

1. All invariant tests pass unchanged
2. Cascade authority is unambiguous in code comments
3. A future refactorer would be warned against “simplifying” cascade logic
4. No lifecycle semantics changed

---

## **Outcome**

After **D-003-T3**:

* Cascade semantics are **explicitly defended**
* Authority is clear and singular
* Lifecycle closure cannot be accidentally broken by cleanup
