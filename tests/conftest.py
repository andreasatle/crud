import pytest

from crud.persistence import create_engine_from_url, create_session_factory
from crud.persistence.models import Base
from crud.persistence.repositories import SqlAddressRepository, SqlPersonRepository


@pytest.fixture
def sql_engine():
    engine = create_engine_from_url("sqlite:///:memory:")
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
