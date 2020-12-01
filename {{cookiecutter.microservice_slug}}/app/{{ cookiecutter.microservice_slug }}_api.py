from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from motor import motor_asyncio

from routes import ping


api = FastAPI()
mongodb_connection = motor_asyncio.AsyncIOMotorClient('mongodb://{{cookiecutter.mongodb_new_username}}:{{cookiecutter.mongodb_new_username_password}}@{{cookiecutter.mongodb_container_name}}:27017/{{cookiecutter.mongodb_database}}?authSource={{cookiecutter.mongodb_database}}')


# This is just an informational route. It can be removed if unwanted/unneeded
@api.get('/', response_class=HTMLResponse)
async def index():
    return """
    <html>
        <title>{{cookiecutter.microservice_name}} microservice</title>
        <body>
            <p>Verify FastAPI is working correctly with a simple ping/pong route:</p>
            <p><a href="/ping" target="_blank" rel="noopener noreferrer">ping/pong check!</a></p>
            <br />
            <p>Verify FastAPI can communicate with the MongoDB database container:</p>
            <p><a href="/mongo" target="_blank" rel="noopener noreferrer">Mongodb check!</a></p>
            <p>There won't actually be any data in the MongoDB to be returned, but you should get an empty list, a 200 response code, and not see any errors. This is mainly what we're shooting for with this route.</p>
        </body>
    """


api.include_router(
    ping.router
)
