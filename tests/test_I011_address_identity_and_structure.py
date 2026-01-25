from crud.address import Address


def test_I011_address_identity_semantics_and_stability():
    """
    Invariant I-011 — Address Identity Semantics and Stability

    Identity is defined solely by `id`.
    """

    a1 = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    a2 = Address(
        id="address-1",
        person_id="person-2",
        street="456 Elm St",
        city="Shelbyville",
        postal_code="54321",
        country="US",
    )

    a3 = Address(
        id="address-2",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    # Identity equality: same id => same logical entity
    assert a1 == a2

    # Identity inequality: different id => different entity
    assert a1 != a3

    # Non-identity fields must not affect identity
    assert a1.person_id != a2.person_id
    assert a1.street != a2.street
    assert a1.city != a2.city
    assert a1.postal_code != a2.postal_code
    assert a1.country != a2.country
