import pytest

from crud.address import Address
from crud.person import Person


def test_I018_address_update_operation_semantics(person_repo, address_repo):
    """
    Invariant I-018 — Address Update Operation Semantics

    Updating an Address:
    - requires existence
    - preserves identity and ownership
    - mutates only non-identity fields
    """

    # Setup owning person
    person = Person(id="person-1", name="Alice", email=None)
    person_repo.create(person)

    # Create address
    original = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )
    address_repo.create(original)

    # Update address fields (non-identity)
    updated = Address(
        id="address-1",
        person_id="person-1",
        street="456 Elm St",
        city="Shelbyville",
        postal_code="54321",
        country="US",
    )

    address_repo.update(updated)

    # Identity preserved
    stored = address_repo.get_by_id("address-1")
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
        address_repo.update(missing)
