from pydantic import BaseModel, validator, HttpUrl
from typing import List, Optional

class SwapiBaseModel(BaseModel):
    url: HttpUrl                    # string -- the hypermedia URL of this resource.
    created: str                    # string -- the ISO 8601 date format of the time that this resource was created.
    edited: str                     # string -- the ISO 8601 date format of the time that this resource was edited.


class Film(SwapiBaseModel):
    title: str                      # string -- The title of this film
    episode_id: int                 # integer -- The episode number of this film.
    opening_crawl: str              # string -- The opening paragraphs at the beginning of this film.
    director: str                   # string -- The name of the director of this film.
    producer: str                   # string -- The name(s) of the producer(s) of this film. Comma separated.
    release_date: str               # date -- The ISO 8601 date format of film release at original creator country.
    species: List[HttpUrl]          # array -- An array of species resource URLs that are in this film.
    starships: List[HttpUrl]        # array -- An array of starship resource URLs that are in this film.
    vehicles: List[HttpUrl]         # array -- An array of vehicle resource URLs that are in this film.
    characters: List[HttpUrl]       # array -- An array of people resource URLs that are in this film.
    planets: List[HttpUrl]          # array -- An array of planet resource URLs that are in this film.
    

class People(SwapiBaseModel):
    name: str                       # string -- The name of this person.
    birth_year: str                 # string -- The birth year of the person, using the in-universe standard of BBY or ABY - Before the Battle of Yavin or After the Battle of Yavin. The Battle of Yavin is a battle that occurs at the end of Star Wars episode IV: A New Hope.
    eye_color: str                  # string -- The eye color of this person. Will be "unknown" if not known or "n/a" if the person does not have an eye.
    gender: str                     # string -- The gender of this person. Either "Male", "Female" or "unknown", "n/a" if the person does not have a gender.
    hair_color: str                 # string -- The hair color of this person. Will be "unknown" if not known or "n/a" if the person does not have hair.
    height: int                     # string -- The height of the person in centimeters.
    mass: int                       # string -- The mass of the person in kilograms.
    skin_color: str                 # string -- The skin color of this person.
    homeworld: HttpUrl              # string -- The URL of a planet resource, a planet that this person was born on or inhabits.
    films: List[HttpUrl]            # array -- An array of film resource URLs that this person has been in.
    species: List[HttpUrl]          # array -- An array of species resource URLs that this person belongs to.
    starships: List[HttpUrl]        # array -- An array of starship resource URLs that this person has piloted.
    vehicles: List[HttpUrl]         # array -- An array of vehicle resource URLs that this person has piloted.


class Vehicle(SwapiBaseModel):
    name: str                       # string -- The name of this vehicle. The common name, such as "Sand Crawler" or "Speeder bike".
    model: str                      # string -- The model or official name of this vehicle. Such as "All-Terrain Attack Transport".
    vehicle_class: str              # string -- The class of this vehicle, such as "Wheeled" or "Repulsorcraft".
    manufacturer: str               # string -- The manufacturer of this vehicle. Comma separated if more than one.
    length: float                   # string -- The length of this vehicle in meters.
    cost_in_credits: int            # string -- The cost of this vehicle new, in Galactic Credits.
    crew: int                       # string -- The number of personnel needed to run or pilot this vehicle.
    passengers: int                 # string -- The number of non-essential people this vehicle can transport.
    max_atmosphering_speed: int     # string -- The maximum speed of this vehicle in the atmosphere.
    cargo_capacity: int             # string -- The maximum number of kilograms that this vehicle can transport.
    consumables: str                # string -- The maximum length of time that this vehicle can provide consumables for its entire crew without having to resupply.
    films: List[HttpUrl]            # array -- An array of Film URL Resources that this vehicle has appeared in.
    pilots: List[HttpUrl]           # array -- An array of People URL Resources that this vehicle has been piloted by.

class Starship(SwapiBaseModel):
    name: str                       # string -- The name of this starship. The common name, such as "Death Star".
    model: str                      # string -- The model or official name of this starship. Such as "T-65 X-wing" or "DS-1 Orbital Battle Station".
    starship_class: str             # string -- The class of this starship, such as "Starfighter" or "Deep Space Mobile Battlestation"
    manufacturer: str               # string -- The manufacturer of this starship. Comma separated if more than one.
    cost_in_credits: int            # string -- The cost of this starship new, in galactic credits.
    length: float                   # string -- The length of this starship in meters.
    crew: int                       # string -- The number of personnel needed to run or pilot this starship.
    passengers: int                 # string -- The number of non-essential people this starship can transport.
    max_atmosphering_speed: int     # string -- The maximum speed of this starship in the atmosphere. "N/A" if this starship is incapable of atmospheric flight.
    hyperdrive_rating: float        # string -- The class of this starships hyperdrive.
    MGLT: int                       # string -- The Maximum number of Megalights this starship can travel in a standard hour. A "Megalight" is a standard unit of distance and has never been defined before within the Star Wars universe. This figure is only really useful for measuring the difference in speed of starships. We can assume it is similar to AU, the distance between our Sun (Sol) and Earth.
    cargo_capacity: int             # string -- The maximum number of kilograms that this starship can transport.
    consumables: str                # *string -- The maximum length of time that this starship can provide consumables for its entire crew without having to resupply.
    films: List[HttpUrl]            # array -- An array of Film URL Resources that this starship has appeared in.
    pilots: List[HttpUrl]           # array -- An array of People URL Resources that this starship has been piloted by.

class Species(SwapiBaseModel):
    name: str                       # string -- The name of this species.
    classification: str             # string -- The classification of this species, such as "mammal" or "reptile".
    designation: str                # string -- The designation of this species, such as "sentient".
    average_height: float           # string -- The average height of this species in centimeters.
    average_lifespan: float         # string -- The average lifespan of this species in years.
    eye_colors: str                 # string -- A comma-separated string of common eye colors for this species, "none" if this species does not typically have eyes.
    hair_colors: str                # string -- A comma-separated string of common hair colors for this species, "none" if this species does not typically have hair.
    skin_colors: str                # string -- A comma-separated string of common skin colors for this species, "none" if this species does not typically have skin.
    language: str                   # string -- The language commonly spoken by this species.
    homeworld: HttpUrl              # string -- The URL of a planet resource, a planet that this species originates from.
    people: List[HttpUrl]           # array -- An array of People URL Resources that are a part of this species.
    films: List[HttpUrl]            # array -- An array of Film URL Resources that this species has appeared in.

class Planet(SwapiBaseModel):
    name: str                       # string -- The name of this planet.
    diameter: int                   # string -- The diameter of this planet in kilometers.
    rotation_period: int            # string -- The number of standard hours it takes for this planet to complete a single rotation on its axis.
    orbital_period: int             # string -- The number of standard days it takes for this planet to complete a single orbit of its local star.
    gravity: str                    # string -- A number denoting the gravity of this planet, where "1" is normal or 1 standard G. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs.
    population: int                 # string -- The average population of sentient beings inhabiting this planet.
    climate: str                    # string -- The climate of this planet. Comma separated if diverse.
    terrain: str                    # string -- The terrain of this planet. Comma separated if diverse.
    surface_water: int              # string -- The percentage of the planet surface that is naturally occurring water or bodies of water.
    residents: List[HttpUrl]        # array -- An array of People URL Resources that live on this planet.
    films: List[HttpUrl]            # array -- An array of Film URL Resources that this planet has appeared in.

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