from setuptools import find_packages, setup

setup(
    name="swapi_dagster",
    packages=find_packages(exclude=["swapi_dagster_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pandas",
        "sqlalchemy-utils"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest", "psycopg2-binary"]},
)
