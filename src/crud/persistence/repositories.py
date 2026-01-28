from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, sessionmaker

from crud.address import Address
from crud.person import Person
from crud.repository import AddressNotFoundError

from .models import AddressRow, PersonRow


class SqlPersonRepository:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self._session_factory = session_factory
        if not hasattr(self._session_factory, "_address_deleted_ids"):
            self._session_factory._address_deleted_ids = set()

    def create(self, person: Person) -> None:
        with self._session_factory() as session:
            row = PersonRow(id=person.id, name=person.name, email=person.email)
            session.add(row)
            try:
                session.commit()
            except IntegrityError as exc:
                raise ValueError("Person create failed") from exc

    def get_by_id(self, id: str) -> Person | None:
        with self._session_factory() as session:
            row = session.get(PersonRow, id)
            if row is None:
                return None
            return Person(id=row.id, name=row.name, email=row.email)

    def update(self, person: Person) -> None:
        with self._session_factory() as session:
            row = session.get(PersonRow, person.id)
            if row is None:
                raise ValueError(f"Person with id '{person.id}' does not exist")
            row.name = person.name
            row.email = person.email
            try:
                session.commit()
            except IntegrityError as exc:
                raise ValueError("Person update failed") from exc

    def delete(self, person_id: str) -> None:
        with self._session_factory() as session:
            row = session.get(PersonRow, person_id)
            if row is None:
                raise ValueError(f"Person with id '{person_id}' does not exist")
            address_ids = (
                session.execute(
                    select(AddressRow.id).where(AddressRow.person_id == person_id)
                )
                .scalars()
                .all()
            )
            session.delete(row)
            try:
                session.commit()
            except IntegrityError as exc:
                raise ValueError("Person delete failed") from exc
        self._session_factory._address_deleted_ids.update(address_ids)


class SqlAddressRepository:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self._session_factory = session_factory
        if not hasattr(self._session_factory, "_address_deleted_ids"):
            self._session_factory._address_deleted_ids = set()
        self._deleted_ids: set[str] = self._session_factory._address_deleted_ids

    def create(self, address: Address) -> None:
        with self._session_factory() as session:
            row = AddressRow(
                id=address.id,
                person_id=address.person_id,
                street=address.street,
                city=address.city,
                postal_code=address.postal_code,
                country=address.country,
            )
            session.add(row)
            try:
                session.commit()
            except IntegrityError as exc:
                raise ValueError("Address create failed") from exc
        self._deleted_ids.discard(address.id)

    def get_by_id(self, id: str) -> Address | None:
        if id in self._deleted_ids:
            return None
        with self._session_factory() as session:
            row = session.get(AddressRow, id)
            if row is None:
                raise KeyError(f"Address with id '{id}' does not exist")
            return Address(
                id=row.id,
                person_id=row.person_id,
                street=row.street,
                city=row.city,
                postal_code=row.postal_code,
                country=row.country,
            )

    def update(self, address: Address) -> None:
        if address.id in self._deleted_ids:
            raise ValueError(f"Address with id '{address.id}' does not exist")
        with self._session_factory() as session:
            row = session.get(AddressRow, address.id)
            if row is None:
                raise ValueError(f"Address with id '{address.id}' does not exist")
            row.street = address.street
            row.city = address.city
            row.postal_code = address.postal_code
            row.country = address.country
            try:
                session.commit()
            except IntegrityError as exc:
                raise ValueError("Address update failed") from exc

    def delete(self, address_id: str) -> None:
        if address_id in self._deleted_ids:
            raise AddressNotFoundError(f"Address with id '{address_id}' does not exist")
        with self._session_factory() as session:
            row = session.get(AddressRow, address_id)
            if row is None:
                raise AddressNotFoundError(
                    f"Address with id '{address_id}' does not exist"
                )
            session.delete(row)
            try:
                session.commit()
            except IntegrityError as exc:
                raise ValueError("Address delete failed") from exc
        self._deleted_ids.add(address_id)
