import pytest

from crud.address import Address
from crud.person import Person
from crud.repository import FakePersonStore, FakeAddressStore


def test_I015_address_read_operation_semantics():
    """
    Invariant I-015 — Address Read Operation Semantics
    """

    people = FakePersonStore()
    addresses = FakeAddressStore(people)

    # Create owning person
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

    addresses.create(address, people)

    # Reading an existing address succeeds
    result = addresses.get_by_id("address-1")
    assert result == address

    # Reading does not mutate state
    result_again = addresses.get_by_id("address-1")
    assert result_again == address

    # Reading a nonexistent address must fail
    with pytest.raises(KeyError):
        addresses.get_by_id("missing-address")
