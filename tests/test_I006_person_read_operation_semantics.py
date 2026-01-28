# tests/test_I006_person_read_operation_semantics.py

from crud.person import Person


def test_I006_person_read_operation_semantics(person_repo):
    """
    Invariant I-006 — Person Read Operation Semantics
    """

    p1 = Person(id="person-1", name="Alice", email=None)
    person_repo.create(p1)

    # Successful read by identity
    read_p1 = person_repo.get_by_id("person-1")
    assert read_p1 == p1

    # Read must be non-mutating (repeatable, no side effects)
    read_again = person_repo.get_by_id("person-1")
    assert read_again == p1

    # Read of non-existent entity must be explicit (None = not found)
    not_found = person_repo.get_by_id("person-404")
    assert not_found is None

    # Read must not create entities
    assert person_repo.get_by_id("person-404") is None
