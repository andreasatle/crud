import pytest

from crud.person import Person
from crud.address import Address
from crud.repository import FakePersonStore
from crud.repository import FakeAddressStore


def test_I017_person_address_lifecycle_coupling_cascade_delete():
    """
    Invariant I-017 — Person–Address Lifecycle Coupling

    Deleting a Person must delete all owned Addresses atomically.
    """

    people = FakePersonStore()
    addresses = FakeAddressStore(people)

    # Create person
    person = Person(id="person-1", name="Alice", email=None)
    people.create(person)

    # Create addresses owned by the person
    a1 = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    a2 = Address(
        id="address-2",
        person_id="person-1",
        street="456 Elm St",
        city="Springfield",
        postal_code="54321",
        country=None,
    )

    addresses.create(a1, people)
    addresses.create(a2, people)

    assert addresses.get_by_id("address-1") == a1
    assert addresses.get_by_id("address-2") == a2

    # Delete person (must cascade)
    people.delete("person-1", addresses)

    # Person no longer exists
    assert people.get_by_id("person-1") is None

    # Owned addresses must no longer exist
    assert addresses.get_by_id("address-1") is None
    assert addresses.get_by_id("address-2") is None

    # Further operations on deleted addresses must fail
    with pytest.raises(ValueError):
        addresses.delete("address-1")

    with pytest.raises(ValueError):
        addresses.update(
            Address(
                id="address-1",
                person_id="person-1",
                street="X",
                city="Y",
                postal_code="Z",
                country=None,
            )
        )
