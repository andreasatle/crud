from __future__ import annotations

from typing import Dict, Optional

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
