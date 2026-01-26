# tests/test_I020_address_lifecycle_closure_and_dependency.py

import pytest

from crud.person import Person
from crud.address import Address
from crud.repository import FakePersonStore, FakeAddressStore


def test_I020_address_lifecycle_closure_and_dependency():
    """
    Invariant I-020 — Address Lifecycle Closure and Dependency
    """

    people = FakePersonStore()
    addresses = FakeAddressStore(people)

    # Create person
    person = Person(id="person-1", name="Alice", email=None)
    people.create(person)

    # Create address
    address = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )
    addresses.create(address)

    # Address exists
    assert addresses.get_by_id("address-1") == address

    # Delete address (terminal)
    addresses.delete("address-1")

    assert addresses.get_by_id("address-1") is None

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

    # Re-create same id => new lifecycle allowed
    address2 = Address(
        id="address-1",
        person_id="person-1",
        street="456 Elm St",
        city="Shelbyville",
        postal_code="54321",
        country="US",
    )
    addresses.create(address2)

    assert addresses.get_by_id("address-1") == address2

    # Delete person => cascades to addresses
    people.delete("person-1")

    assert people.get_by_id("person-1") is None
    assert addresses.get_by_id("address-1") is None
