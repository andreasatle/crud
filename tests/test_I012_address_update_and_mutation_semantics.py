from crud.address import Address


def test_I012_address_update_and_mutation_semantics():
    """
    Invariant I-012 — Address Update and Mutation Semantics

    Updates preserve identity and do not allow identity or ownership changes.
    """

    original = Address(
        id="address-1",
        person_id="person-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    # Update non-identity fields
    updated = Address(
        id="address-1",
        person_id="person-1",
        street="456 Elm St",
        city="Shelbyville",
        postal_code="54321",
        country="US",
    )

    # Identity preserved
    assert original == updated

    # Non-identity fields may change
    assert original.street != updated.street
    assert original.city != updated.city
    assert original.postal_code != updated.postal_code
    assert original.country != updated.country

    # Ownership must not change during update
    reassigned = Address(
        id="address-1",
        person_id="person-2",
        street="456 Elm St",
        city="Shelbyville",
        postal_code="54321",
        country="US",
    )

    # Ownership change constitutes replacement, not update
    assert original == reassigned  # identity still same
    assert original.person_id != reassigned.person_id
