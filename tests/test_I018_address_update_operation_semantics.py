import pytest

from crud.address import Address
from crud.repository import FakePersonStore, FakeAddressStore
from crud.person import Person


def test_I018_address_update_operation_semantics():
    """
    Invariant I-018 — Address Update Operation Semantics

    Updating an Address:
    - requires existence
    - preserves identity and ownership
    - mutates only non-identity fields
    """

    people = FakePersonStore()
    addresses = FakeAddressStore()

    # Setup owning person
    person = Person(id="person-1", name="Alice", email=None)
    people.create(person)

    # Create address
    original = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )
    addresses.create(original, people)

    # Update address fields (non-identity)
    updated = Address(
        id="address-1",
        person_id="person-1",
        street="456 Elm St",
        city="Shelbyville",
        postal_code="54321",
        country="US",
    )

    addresses.update(updated)

    # Identity preserved
    stored = addresses.get_by_id("address-1")
    assert stored == original
    assert stored.id == "address-1"
    assert stored.person_id == "person-1"

    # Fields updated
    assert stored.street == "456 Elm St"
    assert stored.city == "Shelbyville"
    assert stored.postal_code == "54321"
    assert stored.country == "US"

    # Updating a non-existent Address must fail
    missing = Address(
        id="address-missing",
        person_id="person-1",
        street="X",
        city="Y",
        postal_code="Z",
        country=None,
    )

    with pytest.raises(ValueError):
        addresses.update(missing)
