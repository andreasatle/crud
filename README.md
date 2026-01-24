# CRUD — Framework Validation Project

## Purpose

This project exists to **test a concrete development framework**, not to build a feature-complete CRUD application.

The goal is to evaluate whether the framework:

* constrains AI-generated code effectively
* prevents drift and circular changes
* keeps human effort bounded and meaningful
* remains usable over time

The CRUD application is deliberately simple and serves only as a **testbed**.

---

## What Is Being Tested

The framework under evaluation consists of the following elements:

### 1. Help Doc (Single, Non-Authoritative)

* Defines **scope** and **public entrypoints**
* Describes what the system *is* and *is not*
* Serves only as **input** for deriving invariants
* Does **not** enforce behavior

There is exactly **one** such document.

---

### 2. Invariants

* An invariant is a statement that must **never regress**
* Invariants are derived:

  * initially from the help doc (Phase 1)
  * later from running the system and discovering semantic truths
* Invariants are not speculative
* Invariants exist **only if enforced by tests**

---

### 3. Tests (Only Authority)

* Tests are the **only enforceable authority**
* One invariant maps to one test function (with one or more assertions)
* If a test passes, the invariant holds
* If a test fails, work is required

Anything not enforced by a test is guidance only.

---

### 4. Tasks

* Tasks are explicit instructions for implementation
* A task is created when:

  * a test fails, or
  * a human observes a “feel” problem (structure, readability, UX)
* Feel-level tasks do **not** require invariants or tests

Tasks do not invent requirements; they execute decisions already made.

---

### 5. Policies

* Policies guide **how** code is written
* Policies are forward-looking only
* Policies do not retroactively invalidate code
* A policy affects existing code only if a human creates a retrofit task

Policies are not enforced automatically.

---

### 6. Ledger

* `ledger.md` is an append-only log of human decisions
* It records:

  * what was changed
  * why it was changed
  * which mechanism was used (invariant, task, policy)
* The ledger is observational, not authoritative

The ledger exists to study the human role in the loop.

---

## Workflow

The framework uses a single loop:

```
observe → decide → record → act
```

Decision paths:

* **Semantic issue**
  → invariant → test → task → code → validation

* **Feel / structural issue**
  → task → code → validation

The distinction is intentional.

---

## Project Structure

```
src/        # implementation (coder-controlled)
tests/      # tests (only authority)
tasks/      # explicit execution instructions
policies/   # implementation guidance
ledger.md   # human decision log
```

No other directories are considered authoritative.

---

## Phases

### Phase 1 — Invariant Extraction

* Read the help doc
* Derive all obvious invariants
* Stop when invariants are no longer obvious

### Phase 2 — Execution Loop

* Run the code
* Observe behavior
* Decide:

  * invariant (semantic)
  * or task (feel)

Phase 2 repeats indefinitely.

---

## Non-Goals

This project does **not** aim to:

* fully specify behavior upfront
* eliminate human judgment
* encode UX decisions as invariants
* automate architectural design
* optimize performance

---

## Success Criteria

This framework is considered successful if:

* invariants converge instead of exploding
* tests prevent regression and circular changes
* policies remain advisory, not coercive
* the human role is clear and bounded
* the ledger provides insight into real decisions

Feature completeness is irrelevant.

---

## Important Constraint

**The framework itself must not change during this experiment.**

Only after running it end-to-end and reviewing the ledger will changes be considered.
