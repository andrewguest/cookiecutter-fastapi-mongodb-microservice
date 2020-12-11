from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from motor import motor_asyncio

from database import mongo_config
from routes import ExampleRoutes


api = FastAPI()


# This is just an informational route. It can be removed if unwanted/unneeded
@api.get("/", response_class=HTMLResponse)
async def index():
    return """
    <html>
        <title>{{cookiecutter.microservice_name}} microservice</title>
        <body>
            <p>Verify FastAPI is working correctly with a simple ping/pong route:</p>
            <p><a href="/ping" target="_blank" rel="noopener noreferrer">ping/pong check!</a></p>
            <br />
            <p>Play with some tasks:</p>
            <p><a href="/task" target="_blank" rel="noopener noreferrer">Create, List, Update, and Delete fake tasks!</a></p>
            <br />
            <p>Verify FastAPI can communicate with the MongoDB database container:</p>
            <p><a href="/mongo" target="_blank" rel="noopener noreferrer">Mongodb check!</a></p>
            <p>There won't actually be any data in the MongoDB to be returned, but you should get an empty list, a 200 response code, and not see any errors. This is mainly what we're shooting for with this route.</p>
            <br />
            <p>API documentation:</p>
            <p><a href="/docs" target="_blank" rel="noopener noreferrer">Swagger UI documentation!</a></p>
            <p><a href="/redoc" target="_blank" rel="noopener noreferrer">ReDoc documentation!</a></p>
        </body>
    """


# Connect to the MongoDB container when the FastAPI app is started.
# The MongoDB connection information is pulled from database/mongodb_config.py
@api.on_event("startup")
async def startup_db_client():
    api.mongodb_client = motor_asyncio.AsyncIOMotorClient(
        mongo_config.example_db_settings.DB_URL
    )
    api.mongodb = api.mongodb_client[mongo_config.example_db_settings.DB_NAME]
    api.mongodb_collection = api.mongodb[mongo_config.example_db_settings.COLLECTION_NAME]


# Close the MongoDB connection when the FastAPI app is shutdown
@api.on_event("shutdown")
async def shutdown_db_client():
    api.mongodb_client.close()


api.include_router(ExampleRoutes.router, tags=["Test Routes"])
