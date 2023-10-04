import json
import requests
from pathlib import Path

import pandas as pd
from pydantic.error_wrappers import ValidationError

from . import data_models

from dagster import (
    AssetExecutionContext,
    MetadataValue,
    asset,
    get_dagster_logger,
)

base_url = "https://swapi.dev/api/"
data_path = Path().joinpath("data")
logger = get_dagster_logger()

def get_data(kind: str, context: AssetExecutionContext) -> None:

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


def validate_data(kind: str, context: AssetExecutionContext):
    data_ok = []
    data_nok = []
    with open(str(data_path.joinpath(f"raw_{kind}.json")), "r") as fo:
        data = json.load(fo)
    
    data_model = data_models.get_model(kind)
    # Validate data
    for item in data:
        try: 
            data_ok.append(dict(data_model(**item)))
        except ValidationError as e:
            logger.info(e)
            item["error_message"] = str(e)
            data_nok.append(item)
    
    df_data_nok = pd.DataFrame(data_nok)

    context.add_output_metadata(
        metadata={
            "num_ok": len(data_ok),
            "num_nok": len(data_nok),
            "preview_nok": MetadataValue.md(df_data_nok.head().to_markdown()),
        }
    )

    data_path.mkdir(exist_ok=True)
    with open(str(data_path.joinpath(f"validated_{kind}_ok.json")), "w") as fo:
        json.dump(data_ok, fo)
    with open(str(data_path.joinpath(f"validated_{kind}_nok.json")), "w") as fo:
        json.dump(data_nok, fo)

@asset(deps=[get_films])
def validate_films(context: AssetExecutionContext):
    validate_data("films", context)

@asset(deps=[get_people])
def validate_people(context: AssetExecutionContext):
    validate_data("people", context)

@asset(deps=[get_vehicles])
def validate_vehicles(context: AssetExecutionContext):
    validate_data("vehicles", context)

@asset(deps=[get_starships])
def validate_starships(context: AssetExecutionContext):
    validate_data("starships", context)

@asset(deps=[get_species])
def validate_species(context: AssetExecutionContext):
    validate_data("species", context)

@asset(deps=[get_planets])
def validate_planets(context: AssetExecutionContext):
    validate_data("planets", context)