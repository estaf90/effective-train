from typing import (
    List,
)
from sqlalchemy import (
    String,
    Integer,
    BigInteger,
    Float,
    DateTime,
    Column,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy.types import JSON

Base = declarative_base()


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    episode_id = Column(Integer)
    opening_crawl = Column(String)
    director = Column(String)
    producer = Column(String)
    release_date = Column(String)
    species: Mapped[List[String]] = mapped_column(String)
    starships: Mapped[List[String]] = mapped_column(String)
    vehicles: Mapped[List[String]] = mapped_column(String)
    characters: Mapped[List[String]] = mapped_column(String)
    planets: Mapped[List[String]] = mapped_column(String)
    url = Column(String)
    created = Column(DateTime)
    edited = Column(DateTime)
    dagster_run_id = Column(String)


class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(String)
    eye_color = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(Integer)
    mass = Column(Integer)
    skin_color = Column(String)
    homeworld = Column(String)
    films: Mapped[List[String]] = mapped_column(String)
    species: Mapped[List[String]] = mapped_column(String)
    starships: Mapped[List[String]] = mapped_column(String)
    vehicles: Mapped[List[String]] = mapped_column(String)
    url = Column(String)
    created = Column(DateTime)
    edited = Column(DateTime)
    dagster_run_id = Column(String)


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    vehicle_class = Column(String)
    manufacturer = Column(String)
    length = Column(Float)
    cost_in_credits = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    films: Mapped[List[String]] = mapped_column(String)
    pilots: Mapped[List[String]] = mapped_column(String)
    url = Column(String)
    created = Column(DateTime)
    edited = Column(DateTime)
    dagster_run_id = Column(String)

class Starship(Base):
    __tablename__ = "starships"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    starship_class = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(Integer)
    length = Column(Float)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(Float)
    MGLT = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    films: Mapped[List[String]] = mapped_column(String)
    pilots: Mapped[List[String]] = mapped_column(String)
    url = Column(String)
    created = Column(DateTime)
    edited = Column(DateTime)
    dagster_run_id = Column(String)


class Species(Base):
    __tablename__ = "species"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    classification = Column(String)
    designation = Column(String)
    average_height = Column(Float)
    average_lifespan = Column(Float)
    eye_colors = Column(String)
    hair_colors = Column(String)
    skin_colors = Column(String)
    language = Column(String)
    homeworld = Column(String)
    people: Mapped[List[String]] = mapped_column(String)
    films: Mapped[List[String]] = mapped_column(String)
    url = Column(String)
    created = Column(DateTime)
    edited = Column(DateTime)
    dagster_run_id = Column(String)


class Planet(Base):
    __tablename__ = "planets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String)
    population = Column(BigInteger)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)
    residents: Mapped[List[String]] = mapped_column(String)
    films: Mapped[List[String]] = mapped_column(String)
    url = Column(String)
    created = Column(DateTime)
    edited = Column(DateTime)
    dagster_run_id = Column(String)


def get_model(kind: str):
    match kind:
        case "films":
            return Film
        case "people":
            return People
        case "vehicles":
            return Vehicle
        case "starships":
            return Starship
        case "species":
            return Species
        case "planets":
            return Planet
        case _:
            raise NotImplementedError(f"No model found for {kind}!")