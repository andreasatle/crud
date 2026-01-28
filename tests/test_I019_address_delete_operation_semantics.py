# tests/test_I019_address_delete_operation_semantics.py

import pytest

from crud.person import Person
from crud.address import Address


def test_I019_address_delete_operation_semantics(person_repo, address_repo):
    """
    Invariant I-019 — Address Delete Operation Semantics
    """

    address = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    # Create succeeds
    person_repo.create(
        Person(
            id="person-1",
            name="Alice",
            email=None,
        )
    )

    address_repo.create(address)

    assert address_repo.get_by_id("address-1") == address

    # Delete succeeds
    address_repo.delete("address-1")

    # Deleted address is nonexistent
    assert address_repo.get_by_id("address-1") is None

    # Deleting again must fail explicitly
    with pytest.raises(KeyError):
        address_repo.delete("address-1")

    # Deleting a never-existing address must fail
    with pytest.raises(KeyError):
        address_repo.delete("nonexistent-address")
