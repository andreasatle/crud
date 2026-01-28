from __future__ import annotations

from typing import Dict, Optional, Set

from crud.address import Address
from crud.person import Person


class AddressNotFoundError(ValueError, KeyError):
    pass


class FakePersonStore:
    def __init__(self) -> None:
        self._people: Dict[str, Person] = {}
        self._address_stores: Set[FakeAddressStore] = set()

    def _register_address_store(self, addresses: FakeAddressStore) -> None:
        self._address_stores.add(addresses)

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

    def delete(self, id: str, addresses: FakeAddressStore | None = None) -> None:
        if id not in self._people:
            raise ValueError(f"Person with id '{id}' does not exist")
        address_stores = (
            [addresses] if addresses is not None else list(self._address_stores)
        )
        for address_store in address_stores:
            owned_ids = [
                address_id
                for address_id, address in address_store._addresses.items()
                if address.person_id == id
            ]
            for address_id in owned_ids:
                address_store.delete(address_id)
        del self._people[id]


class FakeAddressStore:
    def __init__(self, people: FakePersonStore | None = None) -> None:
        self._addresses: Dict[str, Address] = {}
        self._deleted_ids: Set[str] = set()
        self._people = people
        if self._people is not None:
            self._people._register_address_store(self)

    def create(self, address: Address, people: FakePersonStore | None = None) -> None:
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
        effective_people = self._people if self._people is not None else people
        if effective_people is None:
            raise ValueError("Address store requires a person store")
        if effective_people.get_by_id(address.person_id) is None:
            raise ValueError(f"Person with id '{address.person_id}' does not exist")
        if address.id in self._deleted_ids:
            self._deleted_ids.remove(address.id)
        self._addresses[address.id] = address

    def get_by_id(self, id: str) -> Optional[Address]:
        if id in self._deleted_ids:
            return None
        if id not in self._addresses:
            raise KeyError(f"Address with id '{id}' does not exist")
        return self._addresses[id]

    def update(self, address: Address) -> None:
        if address.id in self._deleted_ids or address.id not in self._addresses:
            raise ValueError(f"Address with id '{address.id}' does not exist")
        self._addresses[address.id] = address

    def delete(self, id: str) -> None:
        if id in self._deleted_ids or id not in self._addresses:
            raise AddressNotFoundError(f"Address with id '{id}' does not exist")
        del self._addresses[id]
        self._deleted_ids.add(id)
