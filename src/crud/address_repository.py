from __future__ import annotations

from typing import Dict, Optional, Set

from crud.address import Address


class FakeAddressStore:
    def __init__(self) -> None:
        self._addresses: Dict[str, Address] = {}
        self._deleted_ids: Set[str] = set()

    def create(self, address: Address) -> None:
        self._addresses[address.id] = address

    def get_by_id(self, id: str) -> Optional[Address]:
        if id in self._deleted_ids:
            return None
        return self._addresses.get(id)

    def delete(self, id: str) -> None:
        if id in self._deleted_ids or id not in self._addresses:
            raise KeyError(f"Address with id '{id}' does not exist")
        del self._addresses[id]
        self._deleted_ids.add(id)
