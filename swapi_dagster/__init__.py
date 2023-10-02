from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

from . import assets

all_assets = load_assets_from_modules([assets])

all_assets_job = define_asset_job("all_assets_job", selection=AssetSelection.all())

all_assets_schedule = ScheduleDefinition(
    job=all_assets_job,
    cron_schedule="0 0 * * *",  # Run job 00:00 every day.
)

defs = Definitions(
    assets=all_assets,
    schedules=[all_assets_schedule],
)
