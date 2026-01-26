from __future__ import annotations

from typing import Dict, Optional

from crud.address import Address
from crud.person import Person


class FakePersonStore:
    def __init__(self) -> None:
        self._people: Dict[str, Person] = {}

    def create(self, person: Person) -> None:
        if person.id in self._people:
            raise ValueError(f"Person with id '{person.id}' already exists")
        self._people[person.id] = person

    def get_by_id(self, id: str) -> Optional[Person]:
        return self._people.get(id)

    def update(self, person: Person) -> None:
        if person.id not in self._people:
            raise ValueError(f"Person with id '{person.id}' does not exist")
        self._people[person.id] = Person(
            id=person.id,
            name=person.name,
            email=person.email,
        )

    def delete(self, id: str) -> None:
        if id not in self._people:
            raise ValueError(f"Person with id '{id}' does not exist")
        del self._people[id]


class FakeAddressStore:
    def __init__(self) -> None:
        self._addresses: Dict[str, Address] = {}

    def create(self, address: Address, people: FakePersonStore) -> None:
        if not isinstance(address.id, str) or address.id == "":
            raise ValueError("Address id must be a non-empty string")
        if not isinstance(address.street, str) or address.street == "":
            raise ValueError("Address street must be a non-empty string")
        if not isinstance(address.city, str) or address.city == "":
            raise ValueError("Address city must be a non-empty string")
        if not isinstance(address.postal_code, str) or address.postal_code == "":
            raise ValueError("Address postal_code must be a non-empty string")
        if address.country is not None and not isinstance(address.country, str):
            raise ValueError("Address country must be a string or None")
        if not isinstance(address.person_id, str) or address.person_id == "":
            raise ValueError("Address person_id must be a non-empty string")
        if address.id in self._addresses:
            raise ValueError(f"Address with id '{address.id}' already exists")
        if people.get_by_id(address.person_id) is None:
            raise ValueError(f"Person with id '{address.person_id}' does not exist")
        self._addresses[address.id] = address

    def get_by_id(self, id: str) -> Address:
        if id not in self._addresses:
            raise KeyError(f"Address with id '{id}' does not exist")
        return self._addresses[id]
