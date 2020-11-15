import os

from fastapi import FastAPI
from motor import motor_asyncio

from routes import ping


mongodb_servername = os.getenv("MONGODB_SERVNAME")

api = FastAPI()
mongodb_connection = motor_asyncio.AsyncIOMotorClient(mongodb_servername, {{ cookiecutter.mongodb_port }})


api.include_router(
    ping.router
)