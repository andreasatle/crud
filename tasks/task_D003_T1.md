### **TASK — D-003-T1: Persistence Hardening and Semantic Freeze**

---

## **Objective**

Defend and freeze **SQL-backed persistence semantics** after the authority flip in **D-002**, ensuring that:

* All currently observable behavior is intentional
* No accidental refactors can change meaning
* SQL persistence remains the single authoritative substrate

This task introduces **no new behavior**.  
It exists solely to **make existing semantics explicit and non-removable**.

---

## **Authority**

* Directive: **D-003 — Persistence Hardening (Post-Authority)**
* Precondition:
  * **D-002 — Switch Test Authority from Fake → SQL**
* Governing invariants:
  * **I-001 through I-020**
* Constraints:
  * No invariant changes
  * No semantic changes
  * No new abstractions
  * Monotone deletions only

---

## **Problem Statement**

After D-002:

* SQL behavior is authoritative
* Invariants pass
* BUT:

  * Some semantics are implicit
  * Some error behavior looks accidental
  * Some persistence choices appear “clean-up-able”
  * Future refactors could silently change meaning

This task **locks intent** so that correctness cannot erode accidentally.

---

## **Core Rule**

> **Anything that currently passes invariants is intentional and frozen.**

No persistence behavior may change without:
* a new directive
* new or expanded invariants

---

## **Scope**

### Included

* SQL persistence layer
* Repository error behavior
* Cascade and lifecycle semantics
* Transaction boundaries
* Documentation comments that defend intent

### Explicitly Excluded

* Domain model changes
* Invariant additions or edits
* Test logic changes
* Migrations
* Concurrency
* Performance work
* New backends

---

## **Required Changes**

### **1. Declare SQL Persistence Authority Explicitly**

Add a **central, explicit declaration** (comment-level) stating that:

* SQL-backed repositories define invariant semantics
* Behavior is frozen post–D-002
* Refactors must preserve observable behavior

No logic changes.

---

### **2. Freeze Error Semantics**

Document (without changing behavior):

* Which operations raise `ValueError`
* Which raise `KeyError`
* Which return `None`
* Where mixed or composite errors are intentional

Add comments forbidding “error cleanup” without directive-level approval.

---

### **3. Declare Cascade Authority and Non-Removal**

Explicitly document:

* Which cascade mechanism is authoritative
* Why redundant mechanisms (if any) exist
* That cascade behavior MUST NOT be simplified casually

Do NOT remove or change cascade logic.

---

### **4. Defend Transaction Boundaries**

Add comments asserting:

* Each CRUD operation owns its transaction
* Sessions are operation-scoped
* Shared or ambient sessions are forbidden

No session-handling changes allowed.

---

### **5. Mark Non-Obvious Persistence Decisions as Intentional**

Identify and document persistence choices that appear accidental but are required, such as:

* Ownership fields not present in domain dataclasses
* Tombstone usage
* Identity semantics defined solely by `id`

These MUST be treated as fixed semantics.

---

### **6. Monotone Deletion of Dead Scaffolding (Optional but Allowed)**

If Fake persistence or helpers are clearly unused and non-authoritative:

* Delete them, OR
* Mark them explicitly as non-authoritative scaffolding

No abstraction or refactor allowed.

---

### **7. Invariant Stability Check**

Run all invariants **I-001 through I-020** against SQL persistence.

Confirm:
* No assertion changes
* No semantic drift
* No new behavior introduced

---

### **8. Ledger Entry**

Add a ledger entry stating:

* D-003 completed
* Persistence semantics frozen
* No new behavior introduced
* SQL authority defended

---

## **Constraints**

* ❌ No adapters
* ❌ No backend branching
* ❌ No semantic “cleanup”
* ❌ No preparatory refactors
* ❌ No future-facing abstractions

All removals must be **monotone deletions**.

---

## **Success Criteria**

* All invariants pass unchanged
* SQL persistence behavior is explicitly defended
* Accidental refactors would visibly violate comments or structure
* No ambiguity remains about persistence authority
* No new semantics were introduced

---

## **Outcome**

After D-003-T1:

* SQL persistence semantics are **frozen and defended**
* Correctness is explicit, not emergent
* The system is safe to evolve without silent drift

