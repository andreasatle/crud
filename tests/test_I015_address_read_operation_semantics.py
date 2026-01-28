import pytest

from crud.address import Address
from crud.person import Person


def test_I015_address_read_operation_semantics(person_repo, address_repo):
    """
    Invariant I-015 — Address Read Operation Semantics
    """

    # Create owning person
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

    # Reading an existing address succeeds
    result = address_repo.get_by_id("address-1")
    assert result == address

    # Reading does not mutate state
    result_again = address_repo.get_by_id("address-1")
    assert result_again == address

    # Reading a nonexistent address must fail
    with pytest.raises(KeyError):
        address_repo.get_by_id("missing-address")
