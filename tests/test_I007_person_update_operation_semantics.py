# tests/test_I007_person_update_operation_semantics.py

import pytest

from crud.person import Person


def test_I007_person_update_operation_semantics(person_repo):
    """
    Invariant I-007 — Person Update Operation Semantics
    """

    p1 = Person(id="person-1", name="Alice", email=None)
    person_repo.create(p1)

    # Successful update of existing entity
    updated = Person(id="person-1", name="Alicia", email="a@example.com")
    person_repo.update(updated)

    read_back = person_repo.get_by_id("person-1")
    assert read_back == updated
    assert read_back.name == "Alicia"
    assert read_back.email == "a@example.com"

    # Update must preserve identity
    assert read_back.id == "person-1"

    # Updating a non-existent entity must fail
    missing = Person(id="person-404", name="Ghost", email=None)
    with pytest.raises(ValueError):
        person_repo.update(missing)
