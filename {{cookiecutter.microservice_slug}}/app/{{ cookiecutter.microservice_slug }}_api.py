from fastapi import FastAPI
from motor import motor_asyncio

from routes import ping


api = FastAPI()
mongodb_uri = 'mongodb://{{cookiecutter.mongodb_new_username}}:{{cookiecutter.mongodb_new_username_password}}@{{cookiecutter.mongodb_container_name}}:27017/{{cookiecutter.mongodb_database}}?authSource={{cookiecutter.mongodb_database}}'
mongodb_connection = motor_asyncio.AsyncIOMotorClient(mongodb_uri)


api.include_router(
    ping.router
)
