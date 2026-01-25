# tests/test_invariant_I004_person_creation_semantics.py

from crud.person import Person


def test_I004_person_creation_semantics():
    """
    Invariant I-004 — Person Creation Semantics

    Creation assigns identity explicitly and produces a complete entity.
    """

    # Identity must be assigned at creation
    p1 = Person(id="person-1", name="Alice", email=None)
    assert p1.id == "person-1"

    # Creation produces a complete entity (I-001–I-003 already satisfied)
    assert p1.name != ""
    assert p1 == Person(id="person-1", name="Alice", email=None)

    # Creating with a new id represents a new entity
    p2 = Person(id="person-2", name="Alice", email=None)
    assert p1 != p2

    # Creating with an existing id represents the same logical entity,
    # not an update (conflict detection is external to the domain)
    p_conflict = Person(id="person-1", name="Alicia", email="a@example.com")
    assert p1 == p_conflict
