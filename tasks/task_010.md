TASK — Enforce Invariant I-010 (Address Identity and Structure)

Objective:
Implement a domain-level Address entity that satisfies invariant I-010 — Address Identity and Structure.

Scope / Authority:
- Invariant: I-010
- Enforcement test: tests/test_I010_address_identity_and_structure.py
- Applicable policies: P01, P02, P03, P04

Requirements:
- Introduce a new domain entity Address importable as:
  from crud.address import Address
- Address MUST be a plain Python dataclass.
- Address MUST define exactly the following fields:
  - id: str (required, non-empty)
  - street: str (required, non-empty)
  - city: str (required, non-empty)
  - postal_code: str (required, non-empty)
  - country: Optional[str] (optional)
- No additional required fields are permitted.
- No behavior, lifecycle logic, or persistence logic may be added.

Constraints:
- Do NOT use Pydantic.
- Do NOT introduce ORM annotations.
- Do NOT introduce relationships to Person or other entities.
- Do NOT introduce equality overrides or identity semantics beyond structure.
- No global state.

Success Criteria:
- tests/test_I010_address_identity_and_structure.py passes.
- All existing invariant tests remain passing.
- No policy violations are introduced.
