### **TASK — D-003-T2: Freeze Error Semantics by Documentation**

---

## **Objective**

Make **persistence-layer error semantics explicit, intentional, and frozen**, so that:

* Existing exception types and distinctions are preserved
* “Error cleanup” cannot silently change behavior
* Future refactors cannot normalize or collapse failure modes accidentally

This task introduces **no new behavior** and performs **no error handling changes**.

---

## **Authority**

* Directive: **D-003 — Persistence Hardening (Post-Authority)**
* Precondition:
  * **D-003-T1 — Persistence Hardening and Semantic Freeze**
* Governing invariants:
  * **I-001 through I-020**
* Constraints:
  * No invariant changes
  * No semantic changes
  * No exception type changes
  * Documentation and comments only

---

## **Problem Statement**

Current persistence behavior exhibits **intentional heterogeneity** in error handling:

* Some operations return `None`
* Some raise `ValueError`
* Some raise `KeyError`
* Some use composite exception types

While correct per invariants, this behavior appears “messy” and is vulnerable to
well-intentioned refactors that would **change meaning**.

This task makes error semantics **explicitly non-accidental**.

---

## **Core Rule**

> **All existing error distinctions are semantically meaningful and frozen.**

No persistence-layer error behavior may change unless:
* a new directive authorizes it, and
* invariants are expanded to cover the change.

---

## **Scope**

### Included

* SQL persistence repositories
* Error and failure behavior in CRUD operations
* Comments and documentation that explain intent

### Explicitly Excluded

* Domain model changes
* Invariant changes
* Test changes
* Exception refactoring
* Error normalization
* Abstraction introduction

---

## **Required Changes**

### **1. Enumerate Error Semantics (By Documentation)**

Identify and document, per repository method:

* Which conditions result in:
  * `ValueError`
  * `KeyError`
  * `None`
* Which distinctions are intentional (e.g. “never existed” vs “deleted”)
* Which errors represent:
  * domain-semantic failures
  * persistence/mechanical failures

This may be done via inline comments or repository-level documentation.

---

### **2. Mark Error Behavior as Frozen**

Add explicit comments stating that:

* Current exception types are intentional
* Error distinctions MUST NOT be normalized
* Refactors must preserve observable failure modes

These comments should be placed where a future reader would be tempted to “clean up” logic.

---

### **3. Forbid Error Cleanup Without Directive**

Document that:

* Collapsing `KeyError` / `ValueError`
* Replacing errors with sentinel values
* Converting exceptions into booleans
* Harmonizing SQL and Fake error styles

is forbidden unless explicitly authorized by a future directive.

---

## **Constraints**

* ❌ No code-path changes
* ❌ No exception type changes
* ❌ No test updates
* ❌ No helper abstractions
* ❌ No behavioral normalization

Only **documentation and comments** are permitted.

---

## **Validation Standard**

This task is complete when:

1. All invariant tests still pass unchanged
2. Error behavior is clearly documented as intentional
3. A future refactorer would be warned against “cleaning up” errors
4. No semantic or mechanical behavior changed

---

## **Outcome**

After **D-003-T2**:

* Error semantics are **explicitly intentional**
* Heterogeneity is understood as meaning, not mess
* Persistence behavior is protected against accidental simplification
