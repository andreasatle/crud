### Task — Enforce Invariant I-002 (Person Identity Semantics and Stability)

**Objective**
Update the domain entity `Person` so that it satisfies **Invariant I-002 — Person Identity Semantics and Stability**.

**Scope / Authority**

* Invariant: **I-002**
* Enforcement mechanism:
  `tests/test_invariant_I002_person_identity_semantics_and_stability.py`
* Applicable policies: **P01, P02, P03, P04**
  (P05–P06 are not applicable at this stage.)

**Requirements**

* `Person` identity MUST be defined solely by its `id`.
* Two `Person` instances with the same `id` MUST compare as equal.
* Two `Person` instances with different `id` values MUST compare as unequal.
* Differences in non-identity fields (`name`, `email`) MUST NOT affect identity.
* The solution MUST NOT introduce:

  * persistence logic
  * ORM dependencies
  * Pydantic
  * global state
* The solution MUST preserve compliance with **Invariant I-001**:

  * exactly the fields `{id, name, email}`
  * no additional required or optional fields

**Non-Goals**

* Do NOT add database constraints or persistence-layer enforcement.
* Do NOT require a specific equality or immutability mechanism beyond what is needed to satisfy the test.
* Do NOT change the public structure of `Person` beyond what is required for identity semantics.

**Success Criterion**

* `tests/test_invariant_I002_person_identity_semantics_and_stability.py` passes with zero failures.
* All previously passing tests (including I-001) continue to pass.
* No policy violations are introduced.
