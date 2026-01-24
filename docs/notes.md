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
