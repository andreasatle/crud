import pytest

from crud.person import Person
from crud.address import Address


def test_I017_person_address_lifecycle_coupling_cascade_delete(person_repo, address_repo):
    """
    Invariant I-017 — Person–Address Lifecycle Coupling

    Deleting a Person must delete all owned Addresses atomically.
    """

    # Create person
    person = Person(id="person-1", name="Alice", email=None)
    person_repo.create(person)

    # Create addresses owned by the person
    a1 = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    a2 = Address(
        id="address-2",
        person_id="person-1",
        street="456 Elm St",
        city="Springfield",
        postal_code="54321",
        country=None,
    )

    address_repo.create(a1)
    address_repo.create(a2)

    assert address_repo.get_by_id("address-1") == a1
    assert address_repo.get_by_id("address-2") == a2

    # Delete person (must cascade)
    person_repo.delete("person-1")

    # Person no longer exists
    assert person_repo.get_by_id("person-1") is None

    # Owned addresses must no longer exist
    assert address_repo.get_by_id("address-1") is None
    assert address_repo.get_by_id("address-2") is None

    # Further operations on deleted addresses must fail
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
