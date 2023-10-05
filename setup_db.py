from sqlalchemy_utils import create_database, database_exists

import swapi_dagster.db_models as db_models
from swapi_dagster.db import engine_factory

engine = engine_factory()

# Create database if not already exists
if not database_exists(engine.url):
    create_database(engine.url)

# Drop tables if exists!
db_models.Film.__table__.drop(bind=engine, checkfirst=True)
db_models.People.__table__.drop(bind=engine, checkfirst=True)
db_models.Vehicle.__table__.drop(bind=engine, checkfirst=True)
db_models.Starship.__table__.drop(bind=engine, checkfirst=True)
db_models.Species.__table__.drop(bind=engine, checkfirst=True)
db_models.Planet.__table__.drop(bind=engine, checkfirst=True)

# # Create all tables defined (TODO: Add error handling)
db_models.Base.metadata.create_all(engine)