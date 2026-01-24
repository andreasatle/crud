from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    id: str
    name: str
    email: Optional[str] = None
