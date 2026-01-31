# SQL persistence is authoritative post–D-002; repository behavior is frozen and
# must preserve the observable semantics enforced by invariants.
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, sessionmaker

from crud.address import Address
from crud.person import Person
from crud.repository import AddressNotFoundError

from .models import AddressRow, AddressTombstone, PersonRow


class SqlPersonRepository:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self._session_factory = session_factory

    def create(self, person: Person) -> None:
        # Transaction is operation-scoped; do not share sessions across operations.
        # Shared/cached/ambient sessions or cross-operation reuse is forbidden without a directive.
        with self._session_factory() as session:
            row = PersonRow(id=person.id, name=person.name, email=person.email)
            session.add(row)
            try:
                session.commit()
            except IntegrityError as exc:
                # Error semantics are intentional; do not "clean up" without a directive.
                raise ValueError("Person create failed") from exc

    def get_by_id(self, id: str) -> Person | None:
        # Returns None when missing (I-006); no KeyError here by design.
        # Transaction scope MUST end with this method; no session reuse.
        with self._session_factory() as session:
            row = session.get(PersonRow, id)
            if row is None:
                return None
            return Person(id=row.id, name=row.name, email=row.email)

    def update(self, person: Person) -> None:
        # Updates only non-identity fields; missing id is ValueError (frozen).
        # One operation == one transaction; do not pass sessions between methods.
        with self._session_factory() as session:
            row = session.get(PersonRow, person.id)
            if row is None:
                raise ValueError(f"Person with id '{person.id}' does not exist")
            row.name = person.name
            row.email = person.email
            try:
                session.commit()
            except IntegrityError as exc:
                # Error semantics are intentional; do not "clean up" without a directive.
                raise ValueError("Person update failed") from exc

    def delete(self, person_id: str) -> None:
        # Cascade authority: DB ON DELETE CASCADE is authoritative.
        # Tombstones are reinforcing lifecycle tracking and MUST NOT be removed or reordered.
        # Missing id is ValueError (frozen); do not normalize with KeyError.
        # Each call owns its transaction boundary; no ambient or shared sessions.
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
            for address_id in address_ids:
                if session.get(AddressTombstone, address_id) is None:
                    session.add(AddressTombstone(id=address_id))
            session.delete(row)
            try:
                session.commit()
            except IntegrityError as exc:
                # Error semantics are intentional; do not "clean up" without a directive.
                raise ValueError("Person delete failed") from exc


class SqlAddressRepository:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self._session_factory = session_factory

    def create(self, address: Address) -> None:
        # Ownership fields are persistence-only; domain identity is defined solely by id.
        # Operation-scoped transaction; session reuse is forbidden.
        with self._session_factory() as session:
            tombstone = session.get(AddressTombstone, address.id)
            if tombstone is not None:
                session.delete(tombstone)
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
                # Error semantics are intentional; do not "clean up" without a directive.
                raise ValueError("Address create failed") from exc

    def get_by_id(self, id: str) -> Address | None:
        # Missing id: KeyError if never existed, None if deleted (tombstoned).
        # This distinction is intentional; do not collapse to None or KeyError.
        # Transaction scope is limited to this method; no shared sessions.
        with self._session_factory() as session:
            row = session.get(AddressRow, id)
            if row is None:
                if session.get(AddressTombstone, id) is not None:
                    return None
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
        # Missing id is ValueError; do not alter identity.
        # Never-existed vs deleted is not exposed here by design.
        # One operation per transaction; no session reuse across calls.
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
                # Error semantics are intentional; do not "clean up" without a directive.
                raise ValueError("Address update failed") from exc

    def delete(self, address_id: str) -> None:
        # Tombstone tracking is defensive lifecycle state; do not collapse into DB-only semantics.
        # Already-deleted vs never-existing must remain distinct; AddressNotFoundError is intentional.
        # This method owns its transaction boundary; cross-operation reuse is forbidden.
        with self._session_factory() as session:
            if session.get(AddressTombstone, address_id) is not None:
                raise AddressNotFoundError(
                    f"Address with id '{address_id}' does not exist"
                )
            row = session.get(AddressRow, address_id)
            if row is None:
                raise AddressNotFoundError(
                    f"Address with id '{address_id}' does not exist"
                )
            session.add(AddressTombstone(id=address_id))
            session.delete(row)
            try:
                session.commit()
            except IntegrityError as exc:
                # Error semantics are intentional; do not "clean up" without a directive.
                raise ValueError("Address delete failed") from exc
