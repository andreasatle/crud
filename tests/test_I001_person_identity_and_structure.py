# tests/test_invariant_I001_person_identity_and_structure.py

from dataclasses import fields
from typing import Optional

import pytest

from crud.person import Person


def test_I001_person_identity_and_structure():
    """
    Invariant I-001 — Person Identity and Structure

    Every persisted Person entity MUST:
    - have a unique, stable id
    - have a non-empty name
    - MAY have an email
    - have no additional required fields
    """

    person = Person(
        id="person-1",
        name="Alice",
        email=None,
    )

    # id
    assert isinstance(person.id, str)
    assert person.id != ""

    # name
    assert isinstance(person.name, str)
    assert person.name != ""

    # email
    assert person.email is None or isinstance(person.email, str)

    # structural check: no additional required fields
    field_names = {f.name for f in fields(Person)}
    assert field_names == {"id", "name", "email"}
