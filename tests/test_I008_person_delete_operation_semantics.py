# tests/test_I008_person_delete_operation_semantics.py

import pytest

from crud.person import Person


def test_I008_person_delete_operation_semantics(person_repo):
    """
    Invariant I-008 — Person Delete Operation Semantics
    """

    p1 = Person(id="person-1", name="Alice", email=None)
    person_repo.create(p1)

    # Successful delete of existing entity
    person_repo.delete("person-1")

    # Deleted entity must no longer be observable
    assert person_repo.get_by_id("person-1") is None

    # Deleting a non-existent entity must fail
    with pytest.raises(ValueError):
        person_repo.delete("person-1")

    # Update after delete must fail
    updated = Person(id="person-1", name="Alicia", email="a@example.com")
    with pytest.raises(ValueError):
        person_repo.update(updated)

    # Re-creating with the same id is a new creation
    p2 = Person(id="person-1", name="Bob", email=None)
    person_repo.create(p2)
    assert person_repo.get_by_id("person-1") == p2
    assert person_repo.get_by_id("person-1").name == "Bob"
