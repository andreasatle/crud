import pytest
from sqlalchemy import event

from crud.persistence import create_engine_from_url, create_session_factory
from crud.persistence.models import Base
from crud.persistence.repositories import SqlAddressRepository, SqlPersonRepository
from crud.repository import FakeAddressStore, FakePersonStore


def _create_sqlite_engine():
    engine = create_engine_from_url("sqlite:///:memory:")

    @event.listens_for(engine, "connect")
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    return engine


@pytest.fixture
def sql_engine():
    engine = _create_sqlite_engine()
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def sql_session_factory(sql_engine):
    return create_session_factory(sql_engine)


@pytest.fixture
def sql_person_repo(sql_session_factory):
    return SqlPersonRepository(sql_session_factory)


@pytest.fixture
def sql_address_repo(sql_session_factory):
    return SqlAddressRepository(sql_session_factory)


@pytest.fixture(params=["fake", "sql"])
def backend(request):
    return request.param


@pytest.fixture
def person_repo(backend, sql_session_factory):
    if backend == "fake":
        return FakePersonStore()
    return SqlPersonRepository(sql_session_factory)


@pytest.fixture
def address_repo(backend, person_repo, sql_session_factory):
    if backend == "fake":
        return FakeAddressStore(person_repo)
    return SqlAddressRepository(sql_session_factory)


@pytest.fixture
def person_repo_factory(backend):
    if backend == "fake":
        def _factory():
            return FakePersonStore()
        return _factory

    def _factory():
        engine = _create_sqlite_engine()
        Base.metadata.create_all(engine)
        session_factory = create_session_factory(engine)
        return SqlPersonRepository(session_factory)

    return _factory
