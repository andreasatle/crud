# tests/test_I019_address_delete_operation_semantics.py

import pytest

from crud.address import Address
from crud.address_repository import FakeAddressStore


def test_I019_address_delete_operation_semantics():
    """
    Invariant I-019 — Address Delete Operation Semantics
    """

    repo = FakeAddressStore()

    address = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    # Create succeeds
    repo.create(address)
    assert repo.get_by_id("address-1") == address

    # Delete succeeds
    repo.delete("address-1")

    # Deleted address is nonexistent
    assert repo.get_by_id("address-1") is None

    # Deleting again must fail explicitly
    with pytest.raises(KeyError):
        repo.delete("address-1")

    # Deleting a never-existing address must fail
    with pytest.raises(KeyError):
        repo.delete("nonexistent-address")
