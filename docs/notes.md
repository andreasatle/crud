## How to choose the **right granularity for invariants**

### Core rule (this is the one to remember)

> **An invariant is a unit of repair, not a unit of fact.**

Do **not** ask:

* “How many truths are here?”

Ask:

* **“If this breaks, how many independent fixes would I need?”**

That answer determines invariant boundaries.

---

## What “atomic” really means (corrected)

An invariant is **atomic** if:

* a single task can reasonably restore it
* the fix does not require splitting work across unrelated changes
* the failure signal is coherent and actionable

Atomic does **not** mean:

* one sentence
* one field
* one assertion
* one test line

---

## Practical test (use this every time)

When defining or reviewing an invariant, ask:

1. **If this invariant fails, can I write one bounded task to fix it?**

   * Yes → good invariant
   * No → split it

2. **If I split this invariant, would I still fix both parts together?**

   * Yes → keep it combined
   * No → separate invariants

3. **Would a human naturally say “this one thing is broken”?**

   * Yes → good invariant
   * No → too coarse

---

## Example (Person entity)

❌ Bad (over-atomic, explodes):

* “Person has an id”
* “Person id is unique”
* “Person name exists”
* “Person email optional”

✔ Good (repair-oriented):

> **Invariant: Persisted Person Validity**
>
> All persisted Person entities MUST:
>
> * have a unique stable id
> * have a non-empty name
> * have an optional email field

One invariant.
One test.
One fix.

---

## Example (when to split)

If later you add:

* email format validation
* uniqueness across users
* external verification

Those likely require **different fixes**.

→ New invariant.

---

## Summary to save

> * Invariants are units of repair
> * Atomic means “fixable by one task”
> * Multiple assertions per invariant are normal
> * Split invariants only when fixes diverge
> * Avoid invariants that generate bookkeeping work

---
---

This is a **good and correct refinement**, with one important constraint to keep it safe.

---

## Your proposal (restated precisely)

> The task generator:
>
> * sees **policy headers / one-sentence summaries**
> * decides **which policies are relevant**
> * outputs a **policy selection**
> * the **full policy texts** are then injected verbatim to the coder

This is sound **if and only if** the task generator never rewrites policy content.

---

## Why this is the right abstraction level

### 1. Task generation needs *semantic awareness*, not legal text

At task-generation time, the LLM needs to answer questions like:

* “Is this a domain entity?”
* “Is this boundary-facing?”
* “Is persistence involved?”

It does **not** need:

* exact wording
* edge cases
* enforcement details

So giving it **policy headers / one-line purposes** is exactly right.

This:

* reduces cognitive load
* avoids accidental paraphrasing
* avoids overfitting to policy wording
* keeps task generation focused

---

## 2. Policy *selection* is a reasoning problem (LLM-appropriate)

Choosing *which* policies apply is:

* contextual
* semantic
* non-mechanical

That is an appropriate use of an LLM.

Example for I-001:

* P01 (naming): yes
* P02 (domain vs boundary): yes
* P03 (global state): yes
* P04 (OOP preference): yes (soft)
* P05/P06 (ORM/persistence): **no** (not relevant yet)

That judgment is exactly what the task generator should do.

---

## 3. Policy *injection* must remain mechanical

Once the task generator outputs something like:

```
Applicable policies: P01, P02, P03, P04
```

Then:

* the controller fetches the **full canonical texts**
* injects them verbatim into the coder prompt
* no summarization
* no rewriting
* no AI involved

This preserves authority.

---

## The one critical constraint (do not skip this)

> **The task generator must never output modified policy text.**

Only:

* policy IDs
* optionally: confidence or rationale (for humans)

Never:

* “restated rules”
* “simplified versions”
* “interpretations”

Those belong either:

* in the task itself, or
* nowhere at all.

---

## Why this is strictly better than sending all policies

* reduces prompt bloat
* avoids accidental conflicts
* makes relevance explicit
* keeps coder focused
* improves determinism

And importantly:

* **policy omission becomes a visible decision**, not an accident

---

## Minimal schema suggestion (optional but clean)

The task generator could emit something like:

```yaml
task: Implement domain entity Person satisfying invariant I-001
policies:
  required:
    - P01
    - P02
    - P03
  advisory:
    - P04
```

That separation is useful, but not strictly required.

---

## Bottom line

Your suggestion is **architecturally correct**:

* summaries → task generator
* full texts → coder
* selection → explicit
* injection → mechanical

This is exactly how you prevent policy drift while still letting the system reason.

If you want next, we can:

* formalize “required vs advisory” policies, or
* define a hard rule for when *no* policies should be injected.

---
---

## Invariant Progression (Compressed Form)

### **Phase 1 — Meaning (What the entity *is*)**

Defines the entity independent of time or behavior.

* Structure (required fields)
* Identity and equality
* Mutation semantics (what may change without identity change)

➡︎ *Pure semantics. No state. No operations.*

---

### **Phase 2 — Lifecycle (When the entity exists)**

Introduces time, but still no system behavior.

* Creation semantics
* Existence vs non-existence
* Conceptual distinction between create and update

➡︎ *Still no executor, but ordering now exists.*

---

### **Phase 3 — Operations (How the system acts)**

Forces state and executability.

* Create semantics
* Read semantics
* Update semantics
* Delete semantics

➡︎ *State becomes unavoidable. Some executor must exist (fake or real).*

---

### **Phase 4 — System Pressure (How reality intrudes)**

Only appears when scale or composition demands it.

* Relationships
* Referential integrity
* Transactions
* Concurrency
* Durability

➡︎ *This is where real persistence becomes forced.*

---

## One-line mental model

> **Meaning → Lifecycle → Operations → Infrastructure**

This is the version you should keep in your head.

---
---
Here is a **concise, durable summary** you can save. It is written to stand on its own and to guide future you (or an automated system) without context.

---

### On the Use of “Fake” Implementations

Fake implementations are **semantic executors**, not prototypes of the final system.

They exist to make **invariants executable** before committing to technology choices such as databases, ORMs, transactions, or concurrency models.

Key principles:

* A Fake enforces **meaning**, not infrastructure.
* A Fake must be **explicitly named** and never masquerade as a real implementation.
* Fakes are **temporary enforcement mechanisms**, not temporary truths.
* Authority always resides in **invariants and their tests**, never in the Fake itself.
* Anything that cannot be enforced by a Fake is **not a domain invariant** and must be deferred.
* Deferred assumptions (e.g. persistence, transactions, concurrency) must be **explicitly acknowledged**, never implied.

Fakes allow correctness to be defined **once**, independently of how it is eventually implemented.

Replacing a Fake with a real implementation must not change invariant meaning—only the enforcement mechanism.

If invariant meaning changes when the Fake is removed, the invariant was underspecified.

---
___

Here is a **very short, symmetric summary** you can save:

---

**Invariants** define what must always be true.
They are timeless, testable, and enforced by tests.

**Directives** define what we choose to do.
They are contextual, revisable, and enforced by review.

Invariants express **correctness**.
Directives express **intent**.

Both are authoritative while active, but only invariants are permanent.

---
---

Short answer: **3 core tasks left**, plus **optional clean-up**.

### D-001 status overview

You’ve completed the **structural and minimal behavioral spine** of SQL persistence:

Completed:

1. **T1** — Persistence skeleton (engine/session/base)
2. **T2** — ORM models (structure only)
3. **T3** — Schema creation (DDL)
4. **T4** — SQL repositories (create)
5. **T5** — SQL repositories (read)

At this point, SQL persistence is **real, usable, and parallel** to Fake.

---

### What is *still missing* for D-001

#### **T6 — Update operations (SQL, parallel to Fake)**

Mirror:

* Person update semantics (I-007)
* Address update semantics (I-018)

Scope:

* `update(person)`
* `update(address)`
* No lifecycle logic
* No test migration

This completes CRUD minus delete.

---

#### **T7 — Delete operations (SQL, parallel to Fake)**

Mirror:

* Person delete (I-008, I-009, cascade via DB or repo)
* Address delete (I-019, I-020)

Important:

* This is where **foreign keys + cascade rules** get exercised
* Still no test authority shift

---

#### **T8 — Repository parity verification (no behavior change)**

Not code-heavy.

Purpose:

* Assert that SQL repositories now support **the same surface** as Fake:

  * create
  * read
  * update
  * delete

This is the *closure* of D-001.

---

### Optional (but clean) follow-ups (not D-001)

* **D-002** — Switch test authority from Fake → SQL
* **D-003** — Remove Fake (or demote to test-only)
* **D-004** — Migrations, constraints, indexing

---

### Why the number is small (important insight)

D-001 is **not** “implement persistence”.
It is:

> *Introduce SQL as a peer to Fake, without changing authority.*

That makes it:

* finite
* mechanical
* low-entropy

You’re already ~70% done.

If you want, next we can:

* enumerate **exact method signatures** for T6/T7, or
* decide whether cascade delete belongs in DB or repository logic (design fork).

---
---

Here is a **clean, complete task list for D-002**, aligned with everything you’ve already built and fixed.

No prose fluff, just structure.

---

## **D-002 — Switch Test Authority from Fake → SQL**

**Goal**
Make SQL persistence authoritative **without changing invariant semantics**.

Fake remains available only as:

* a reference implementation
* a fallback / debugging aid
* not the source of truth

---

## **Task List**

### **D-002-T1 — Introduce SQL-backed test fixtures**

**Purpose**
Create reusable test fixtures that provide:

* SQLite engine
* schema creation
* session factory
* SQL repositories

**Notes**

* In-memory SQLite
* Fresh DB per test
* No Fake involved

---

### **D-002-T2 — Parameterize repositories in tests**

**Purpose**
Allow tests to run against **either** Fake or SQL repositories.

**Mechanics**

* Replace direct `FakePersonStore()` / `FakeAddressStore()` usage with injected repo fixtures
* Same test logic, different backend

**Rule**

> Tests must not know *which* persistence they use.

---

### **D-002-T3 — Dual-run verification (Fake vs SQL)**

**Purpose**
Prove semantic equivalence.

**Action**
Run each invariant test:

* once with Fake
* once with SQL

**Outcome**

* Any divergence is a SQL bug, not a test change

---

### **D-002-T4 — Promote SQL to default test backend**

**Purpose**
Flip authority.

**Action**

* SQL-backed fixtures become default
* Fake fixtures become optional / secondary

**Rule**

> Invariants now validate SQL behavior.

---

### **D-002-T5 — Remove Fake from invariant tests**

**Purpose**
Enforce authority shift.

**Action**

* Delete Fake usage from invariant tests
* Keep Fake only in:

  * reference tests
  * diagnostics
  * documentation

---

### **D-002-T6 — Lock Fake behind directive**

**Purpose**
Prevent regression.

**Action**

* Mark Fake persistence as:

  * non-authoritative
  * deprecated for invariants
* Add directive note:

  * “Fake must never be reintroduced as test authority”

---

### **D-002-T7 — SQL lifecycle enforcement audit**

**Purpose**
Confirm DB-level guarantees now back invariants.

**Check**

* foreign keys
* cascade deletes
* uniqueness
* nullability

**No new behavior**
Only confirm alignment with I-001 → I-020.

---

### **D-002-T8 — Ledger + directive closure**

**Purpose**
Close the loop formally.

**Action**

* Update ledger:

  * Fake → SQL authority transition complete
* Close D-002
* Reference D-001 as superseded for test authority

---

## **Resulting State**

After D-002:

* ✅ Invariants test **real persistence**
* ✅ SQL is authoritative
* ✅ Fake is explicitly non-authoritative
* ✅ No “null-space” code paths
* ✅ Surface growth is measurable and enforced

If you want, next we can:

* compress this into a **single migration task**, or
* draft **D-003 — Persistence Hardening** (indexes, constraints, perf), or
* formalize the **“mechanical refactor” task class** so this never bites again.

