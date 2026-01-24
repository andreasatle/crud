### Task — Enforce Invariant I-001 (Person Identity and Structure)

**Objective**
Ensure that the domain entity `Person` satisfies invariant **I-001 — Person Identity and Structure** exactly as specified.

**Scope / Authority**

* Invariant: **I-001**
* Enforcement mechanism: `tests/test_invariant_I001_person_identity_and_structure.py`
* Applicable policies: **P01, P02, P03, P04**
  (P05–P06 are not applicable at this stage.)

**Requirements**

* Provide a domain-level `Person` entity importable as `from crud.person import Person`.
* `Person` MUST be a plain Python domain model (no Pydantic, no ORM, no global state).
* The structure of `Person` MUST satisfy all parts of I-001 simultaneously:

  * `id`: required, type `str`, non-empty.
  * `name`: required, type `str`, non-empty.
  * `email`: optional, type `Optional[str]`.
  * No additional required or optional fields beyond `{id, name, email}`.
* Entity naming and module structure MUST comply with POLICY-P01.
* No boundary, persistence, or ORM concerns may appear in the domain model (POLICY-P02, P05, P06).
* No global mutable state may be introduced (POLICY-P03).
* Class-based structure is preferred but no additional behavior is required (POLICY-P04).

**Non-Goals**

* Do NOT add persistence logic, validation frameworks, I/O models, or mapping code.
* Do NOT introduce additional attributes, methods, or abstractions.
* Do NOT enforce uniqueness or stability of `id` beyond what is structurally expressible at the entity level.

**Success Criterion**

* `tests/test_invariant_I001_person_identity_and_structure.py` passes with zero failures.
* No additional policy violations are introduced.

This task is **atomic**: partial compliance is not acceptable.
