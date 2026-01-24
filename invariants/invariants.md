# Invariants — Core Domain (v1)

This document defines **authoritative invariants** for the address book system.
If any invariant is violated, the system is considered **incorrect**, regardless of implementation intent.

Each invariant MUST be enforceable by one or more tests.

---

## I-001 — Person Identity and Structure

**Statement**

Every persisted `Person` entity MUST satisfy all of the following:

1. It has an `id` that is:

   * unique among all Persons
   * stable over time
2. It has a non-empty `name`
3. It MAY have an `email`
4. No additional required fields exist

**Rationale**

This invariant defines what a `Person` *is* at the domain level.
All other behavior depends on this being true.

