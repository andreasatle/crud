### **TASK — D-003-T4: Defend Transaction Boundaries**

## **Objective**

Make **transaction boundaries explicit, owned, and non-negotiable**, so that:

* Each CRUD operation defines its own transactional scope
* No refactor can introduce shared or ambient sessions
* Persistence semantics cannot leak across operations

This task is **documentation-only**.  
It introduces **no new behavior** and makes **no session-handling changes**.

---

## **Authority**

* Directive: **D-003 — Persistence Hardening (Post-Authority)**
* Preconditions:
  * **D-003-T1 — Persistence Hardening and Semantic Freeze**
  * **D-003-T2 — Freeze Error Semantics by Documentation**
  * **D-003-T3 — Declare Cascade Authority Explicitly**
* Governing invariants:
  * **All persistence-related invariants (I-001–I-020)**
* Constraints:
  * No semantic changes
  * No transaction changes
  * No ORM or repository refactors

---

## **Core Rule**

> **Each CRUD operation owns its transaction boundary.**

Transactions are:
* operation-scoped
* explicitly entered
* explicitly committed or failed

No transaction state may outlive a single repository method call.

---

## **Scope**

### Included
* SQL repository methods
* Session acquisition and usage sites
* Inline documentation defending transaction boundaries

### Excluded
* Session factory changes
* ORM configuration changes
* Retry logic
* Concurrency semantics
* Test changes

---

## **Required Changes**

### **1. Declare Operation-Scoped Transactions**

Add explicit comments stating that:

* Each repository method:
  * opens its own session
  * defines its own transaction boundary
* Transaction scope MUST NOT extend beyond the method body

---

### **2. Forbid Shared or Ambient Sessions**

Document explicitly that the following are forbidden without directive-level approval:

* Shared sessions across repository calls
* Long-lived or cached sessions
* Ambient or implicit transactions
* Passing sessions between methods
* Cross-operation transaction reuse

These prohibitions must be placed where a refactorer might attempt reuse.

---

### **3. Mark Transaction Semantics as Frozen**

Add comments stating that:

* Current transaction scoping is intentional
* Refactors must preserve one-operation / one-transaction semantics
* Any change requires a new directive and new invariants

---

## **Constraints**

* ❌ No session-handling changes
* ❌ No behavioral changes
* ❌ No retries
* ❌ No abstraction layers
* ❌ No future-facing preparation

Only **comments and documentation** are permitted.

---

## **Validation Standard**

This task is complete when:

1. All invariants pass unchanged
2. Transaction ownership is explicit in repository code
3. A future refactorer is warned against session reuse
4. No transactional behavior changed

---

## **Outcome**

After **D-003-T4**:

* Transaction boundaries are **explicit and defended**
* Persistence operations are isolated by design
* Semantic drift via session reuse is structurally discouraged
