from pydantic import BaseSettings


class ExampleDatabaseSettings(BaseSettings):
    DB_URL = "mongodb://{{cookiecutter.mongodb_new_username}}:{{cookiecutter.mongodb_new_username_password}}@{{cookiecutter.mongodb_container_name}}:27017/{{cookiecutter.mongodb_database}}?authSource={{cookiecutter.mongodb_database}}"
    DB_NAME = "{{cookiecutter.mongodb_database}}"
    COLLECTION_NAME = "{{cookiecutter.mongodb_collection}}"


example_db_settings = ExampleDatabaseSettings()
