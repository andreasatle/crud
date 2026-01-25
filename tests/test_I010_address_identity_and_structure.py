from dataclasses import fields

from crud.address import Address


def test_I010_address_identity_and_structure():
    """
    Invariant I-010 — Address Identity and Structure

    Every persisted Address entity MUST:
    - have a unique, stable id
    - have required non-empty fields
    - MAY have optional fields
    - have no additional required fields
    """

    address = Address(
        id="address-1",
        street="123 Main St",
        city="Springfield",
        postal_code="12345",
        country=None,
    )

    # id
    assert isinstance(address.id, str)
    assert address.id != ""

    # required fields
    assert isinstance(address.street, str)
    assert address.street != ""

    assert isinstance(address.city, str)
    assert address.city != ""

    assert isinstance(address.postal_code, str)
    assert address.postal_code != ""

    # optional fields
    assert address.country is None or isinstance(address.country, str)

    # structural check: no additional required fields
    field_names = {f.name for f in fields(Address)}
    assert field_names == {
        "id",
        "street",
        "city",
        "postal_code",
        "country",
    }
