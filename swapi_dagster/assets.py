import json
import requests
import pandas as pd
from pathlib import Path

from dagster import (
    AssetExecutionContext,
    MetadataValue,
    asset
)

base_url = "https://swapi.dev/api/"
data_path = Path().joinpath("data")

def get_data(kind: str, context) -> None:

    data = []
    r = requests.get(f"{base_url}{kind}").json()
    data.extend(r["results"])

    while r["next"] is not None:
        r = requests.get(r["next"]).json()
        data.extend(r["results"])

    data_path.mkdir(exist_ok=True)
    with open(str(data_path.joinpath(f"raw_{kind}.json")), "w") as fo:
        json.dump(data, fo)
    
    context.add_output_metadata(
        metadata={
            "num_items": len(data),
        }
    )

@asset
def get_films(context: AssetExecutionContext) -> None:
    get_data("films", context)

@asset
def get_people(context: AssetExecutionContext) -> None:
    get_data("people", context)

@asset
def get_planets(context: AssetExecutionContext) -> None:
    get_data("planets", context)

@asset
def get_species(context: AssetExecutionContext) -> None:
    get_data("species", context)

@asset
def get_starships(context: AssetExecutionContext) -> None:
    get_data("starships", context)

@asset
def get_vehicles(context: AssetExecutionContext) -> None:
    get_data("vehicles", context)
