# Invariants — Core Domain (v1)

This document defines **authoritative invariants** for the address book system.
If any invariant is violated, the system is considered **incorrect**, regardless of implementation intent.

Each invariant MUST be enforceable by one or more tests.

---

* I-001 — Person Identity and Structure
* I-002 — Person Identity Semantics and Stability
* I-003 — Person Update and Mutation Semantics
* I-004 — Person Creation Semantics
* I-005 — Person Create Operation Semantics
* I-006 — Person Read Operation Semantics
* I-007 — Person Update Operation Semantics
* I-008 — Person Delete Operation Semantics
* I-009 — Person Lifecycle Closure and Irreversibility
* I-010 — Address Identity and Structure
* I-011 — Address Identity Semantics and Stability
* I-012 — Address Update and Mutation Semantics
* I-013 — Address Creation Semantics
