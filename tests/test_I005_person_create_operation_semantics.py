# tests/test_invariant_I005_person_create_operation_semantics.py

import pytest

from crud.person import Person


def test_I005_person_create_operation_semantics(person_repo):
    """
    Invariant I-005 — Person Create Operation Semantics
    """

    p1 = Person(id="person-1", name="Alice", email=None)

    # First creation succeeds
    person_repo.create(p1)
    assert person_repo.get_by_id("person-1") == p1

    # Creating a Person with the same id must fail
    p_conflict = Person(id="person-1", name="Alicia", email="a@example.com")

    with pytest.raises(ValueError):
        person_repo.create(p_conflict)

    # Creating with a new id creates a new entity
    p2 = Person(id="person-2", name="Bob", email=None)
    person_repo.create(p2)

    assert person_repo.get_by_id("person-2") == p2
