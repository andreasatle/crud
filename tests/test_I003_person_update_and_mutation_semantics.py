# tests/test_invariant_I003_person_update_and_mutation_semantics.py

from crud.person import Person


def test_I003_person_update_and_mutation_semantics():
    """
    Invariant I-003 — Person Update and Mutation Semantics

    Updating a Person preserves identity.
    Identity fields are immutable under update semantics.
    Non-identity fields may change.
    """

    p1 = Person(id="person-1", name="Alice", email=None)

    # Simulate an update by creating a new instance
    # representing the updated state of the same logical entity
    p_updated = Person(id="person-1", name="Alicia", email="a@example.com")

    # Identity must be preserved
    assert p1 == p_updated

    # Non-identity fields may change
    assert p1.name != p_updated.name
    assert p1.email != p_updated.email

    # Changing identity constitutes a different entity
    p_replacement = Person(id="person-2", name="Alice", email=None)
    assert p1 != p_replacement
