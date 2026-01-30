from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class PersonRow(Base):
    __tablename__ = "person"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str | None] = mapped_column(String, nullable=True)


class AddressRow(Base):
    __tablename__ = "address"

    # Authoritative cascade: DB ON DELETE CASCADE defines lifecycle coupling.
    id: Mapped[str] = mapped_column(String, primary_key=True)
    person_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("person.id", ondelete="CASCADE"),
        nullable=False,
    )
    street: Mapped[str] = mapped_column(String, nullable=False)
    city: Mapped[str] = mapped_column(String, nullable=False)
    postal_code: Mapped[str] = mapped_column(String, nullable=False)
    country: Mapped[str | None] = mapped_column(String, nullable=True)


class AddressTombstone(Base):
    __tablename__ = "address_tombstone"

    # Tombstones are intentional to preserve delete semantics (I-019/I-020).
    id: Mapped[str] = mapped_column(String, primary_key=True)
