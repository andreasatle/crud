from crud.address import Address


def test_I013_address_creation_semantics():
    """
    Invariant I-013 — Address Creation Semantics

    Creation assigns identity and ownership explicitly
    and produces a complete Address entity.
    """

    # Identity and ownership must be assigned at creation
    address = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    assert address.id == "address-1"
    assert address.person_id == "person-1"

    # Creation produces a complete entity (I-010–I-012 already satisfied)
    assert address.street != ""
    assert address.city != ""
    assert address.postal_code != ""

    # Creating with a new id represents a new entity
    address2 = Address(
        id="address-2",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    assert address != address2

    # Creating with the same id represents the same logical entity,
    # not an update (conflict handling is external to the domain)
    address_conflict = Address(
        id="address-1",
        person_id="person-1",
        street="456 Elm St",
        city="Shelbyville",
        postal_code="54321",
        country="US",
    )

    assert address == address_conflict
