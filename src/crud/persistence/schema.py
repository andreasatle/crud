from sqlalchemy.engine import Engine

from .factories import create_engine_from_url
from .models import Base


def create_sqlite_schema(database_url: str) -> Engine:
    engine = create_engine_from_url(database_url)
    Base.metadata.create_all(engine)
    return engine
