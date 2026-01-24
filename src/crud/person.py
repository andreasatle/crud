from dataclasses import dataclass
from typing import Optional


@dataclass(eq=False)
class Person:
    id: str
    name: str
    email: Optional[str] = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.id == other.id
