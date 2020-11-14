from fastapi import FastAPI
from motor import motor_asyncio


api = FastAPI()
mongodb_connection = motor_asyncio.AsyncIOMotorClient({{ cookiecutter.project_slug }}_db)
