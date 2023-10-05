from sqlalchemy import create_engine

db_url = "postgresql://postgres:postgres@localhost:5432/swapi"


def engine_factory():
    return create_engine(db_url)
