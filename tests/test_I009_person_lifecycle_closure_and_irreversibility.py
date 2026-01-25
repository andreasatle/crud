import pytest

from crud.person import Person
from crud.repository import FakePersonStore


def test_I009_person_lifecycle_closure_and_irreversibility():
    """
    Invariant I-009 — Person Lifecycle Closure and Irreversibility
    """

    store = FakePersonStore()
    person = Person(id="person-1", name="Alice", email=None)

    # nonexistent → read/update/delete must fail
    assert store.get_by_id("person-1") is None

    with pytest.raises(ValueError):
        store.update(person)

    with pytest.raises(ValueError):
        store.delete("person-1")

    # create
    store.create(person)
    assert store.get_by_id("person-1") == person

    # read/update allowed
    updated = Person(id="person-1", name="Alicia", email="a@example.com")
    store.update(updated)
    assert store.get_by_id("person-1") == updated

    # delete is terminal
    store.delete("person-1")
    assert store.get_by_id("person-1") is None

    # deleted → read/update/delete must fail
    with pytest.raises(ValueError):
        store.update(updated)

    with pytest.raises(ValueError):
        store.delete("person-1")

    # re-create with same id is a NEW lifecycle (fresh store)
    new_store = FakePersonStore()
    resurrected = Person(id="person-1", name="Bob", email=None)
    new_store.create(resurrected)

    assert new_store.get_by_id("person-1") == resurrected
