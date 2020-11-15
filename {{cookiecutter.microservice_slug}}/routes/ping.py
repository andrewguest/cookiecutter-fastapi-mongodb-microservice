from fastapi import APIRouter

from app import {{ cookiecutter.microservice_slug }}_api


router = APIRouter()


@router.get('/ping', status_code=200)
def ping():
    return {'ping': 'pong'}


@router.get('/mongo', status_code=200)
async def test_mongo():
    data = []
    collection = {{ cookiecutter.microservice_slug }}_api.mongodb_connection['test']['test_collection']
    async for result in collection.find():
        del result['_id']
        data.append(result)
    return {'Mongo data': data}
