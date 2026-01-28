import pytest

from crud.person import Person
from crud.address import Address


def test_I016_address_ownership_referential_integrity(person_repo, address_repo):
    """
    Invariant I-016 — Address Ownership Referential Integrity

    An Address must reference an existing Person.
    """

    # Existing person
    person = Person(id="person-1", name="Alice", email=None)
    person_repo.create(person)

    # Creating an address with an existing person succeeds
    address = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    address_repo.create(address)
    assert address_repo.get_by_id("address-1") == address

    # Creating an address with a non-existent person must fail
    invalid_address = Address(
        id="address-2",
        person_id="missing-person",
        street="456 Elm St",
        city="Shelbyville",
        postal_code="54321",
        country=None,
    )

    with pytest.raises(ValueError):
        address_repo.create(invalid_address)
