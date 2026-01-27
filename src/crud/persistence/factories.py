from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


def create_engine_from_url(url: str) -> Engine:
    return create_engine(url)


def create_session_factory(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine)


def create_declarative_base() -> type[DeclarativeBase]:
    class Base(DeclarativeBase):
        pass

    return Base
