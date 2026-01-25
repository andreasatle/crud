### TASK — Enforce Invariant I-011 (Address Identity Semantics and Stability)

Objective:
Make Address identity semantics match invariant I-011 so that identity is defined solely by `id`.

Scope / Authority:
- Invariant: I-011 — Address Identity Semantics and Stability
- Enforcement test: tests/test_I011_address_identity_semantics_and_stability.py
- Applicable policies: P01, P02, P03, P04

Requirements:
- Update the Address domain entity so that:
  - Equality (`==`) is determined solely by `Address.id`.
  - Non-identity fields (`person_id`, `street`, `city`, `postal_code`, `country`) do NOT affect equality.
- Address instances with the same `id` MUST compare equal.
- Address instances with different `id` values MUST compare unequal.
- Do NOT introduce any persistence, repository, or lifecycle logic.

Constraints:
- Address MUST remain a plain Python dataclass.
- Do NOT use Pydantic.
- Do NOT introduce ORM annotations or metadata.
- Do NOT add new fields.
- No global state.
- No behavioral changes beyond identity semantics.

Non-Goals:
- Do NOT enforce ownership rules.
- Do NOT restrict mutation of non-identity fields.
- Do NOT add update, create, or delete operations.

Success Criteria:
- tests/test_I011_address_identity_semantics_and_stability.py passes.
- All existing Address and Person invariant tests remain passing.
- Identity semantics for Address now mirror those of Person (I-002).
