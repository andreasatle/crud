from dataclasses import dataclass
from typing import Optional


@dataclass(eq=False)
class Address:
    id: str
    street: str
    city: str
    postal_code: str
    country: Optional[str] = None

    def __init__(
        self,
        id: str,
        street: str,
        city: str,
        postal_code: str,
        country: Optional[str] = None,
        person_id: Optional[str] = None,
    ) -> None:
        self.id = id
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.person_id = person_id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Address):
            return NotImplemented
        return self.id == other.id
