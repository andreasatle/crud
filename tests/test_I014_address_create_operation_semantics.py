import pytest

from crud.address import Address
from crud.person import Person


def test_I014_address_create_operation_semantics(person_repo, address_repo):
    """
    Invariant I-014 — Address Create Operation Semantics
    """

    # Create owning person
    person = Person(id="person-1", name="Alice", email=None)
    person_repo.create(person)

    # Creating an Address for an existing Person succeeds
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

    # Creating an Address with the same id must fail
    conflict = Address(
        id="address-1",
        person_id="person-1",
        street="456 Elm St",
        city="Shelbyville",
        postal_code="54321",
        country="US",
    )

    with pytest.raises(ValueError):
        address_repo.create(conflict)

    # Creating an Address for a nonexistent Person must fail
    orphan = Address(
        id="address-2",
        person_id="missing-person",
        street="789 Oak St",
        city="Nowhere",
        postal_code="00000",
        country=None,
    )

    with pytest.raises(ValueError):
        address_repo.create(orphan)
