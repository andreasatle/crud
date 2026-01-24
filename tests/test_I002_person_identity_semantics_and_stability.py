# tests/test_invariant_I002_person_identity_semantics_and_stability.py

from crud.person import Person


def test_I002_person_identity_semantics_and_stability():
    """
    Invariant I-002 — Person Identity Semantics and Stability

    Identity is defined solely by `id`.
    """

    p1 = Person(id="person-1", name="Alice", email=None)
    p2 = Person(id="person-1", name="Alicia", email="a@example.com")
    p3 = Person(id="person-2", name="Alice", email=None)

    # Identity equality: same id => same logical entity
    assert p1 == p2

    # Identity inequality: different id => different entity
    assert p1 != p3

    # Non-identity fields must not affect identity
    assert p2.name != p1.name
    assert p2.email != p1.email
