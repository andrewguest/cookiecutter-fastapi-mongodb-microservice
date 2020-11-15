from fastapi import FastAPI
from motor import motor_asyncio

from routes import ping


api = FastAPI()
mongodb_connection = motor_asyncio.AsyncIOMotorClient('{{ cookiecutter.microservice_slug }}_db', 27017)


api.include_router(
    ping.router
)