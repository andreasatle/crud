from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    id: str
    street: str
    city: str
    postal_code: str
    country: Optional[str] = None
