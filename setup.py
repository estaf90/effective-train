from setuptools import find_packages, setup

setup(
    name="swapi_dagster",
    packages=find_packages(exclude=["swapi_dagster_tests"]),
    install_requires=[
        "dagster",
        "dagster-webserver",
        "dagster-cloud",
        "pandas",
        "sqlalchemy-utils",
        "psycopg2-binary"
    ],
    extras_require={"dev": ["pytest"]},
)
