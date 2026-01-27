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
