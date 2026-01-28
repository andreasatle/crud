# tests/test_I020_address_lifecycle_closure_and_dependency.py

import pytest

from crud.person import Person
from crud.address import Address


def test_I020_address_lifecycle_closure_and_dependency(person_repo, address_repo):
    """
    Invariant I-020 — Address Lifecycle Closure and Dependency
    """

    # Create person
    person = Person(id="person-1", name="Alice", email=None)
    person_repo.create(person)

    # Create address
    address = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )
    address_repo.create(address)

    # Address exists
    assert address_repo.get_by_id("address-1") == address

    # Delete address (terminal)
    address_repo.delete("address-1")

    assert address_repo.get_by_id("address-1") is None

    with pytest.raises(ValueError):
        address_repo.delete("address-1")

    with pytest.raises(ValueError):
        address_repo.update(
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
    address_repo.create(address2)

    assert address_repo.get_by_id("address-1") == address2

    # Delete person => cascades to addresses
    person_repo.delete("person-1")

    assert person_repo.get_by_id("person-1") is None
    assert address_repo.get_by_id("address-1") is None
