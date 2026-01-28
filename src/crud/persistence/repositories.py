from sqlalchemy.orm import Session, sessionmaker

from crud.address import Address
from crud.person import Person

from .models import AddressRow, PersonRow


class SqlPersonRepository:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self._session_factory = session_factory

    def create(self, person: Person) -> None:
        with self._session_factory() as session:
            row = PersonRow(id=person.id, name=person.name, email=person.email)
            session.add(row)
            session.commit()

    def get_by_id(self, id: str) -> Person | None:
        with self._session_factory() as session:
            row = session.get(PersonRow, id)
            if row is None:
                return None
            return Person(id=row.id, name=row.name, email=row.email)


class SqlAddressRepository:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self._session_factory = session_factory

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
            session.commit()

    def get_by_id(self, id: str) -> Address | None:
        with self._session_factory() as session:
            row = session.get(AddressRow, id)
            if row is None:
                return None
            return Address(
                id=row.id,
                person_id=row.person_id,
                street=row.street,
                city=row.city,
                postal_code=row.postal_code,
                country=row.country,
            )
