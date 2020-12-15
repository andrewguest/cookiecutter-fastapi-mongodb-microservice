from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.models.ExampleTask import TaskModel, UpdateTaskModel


router = APIRouter()


@router.get('/ping', status_code=200)
def ping():
    return {'ping': 'pong'}


@router.get('/mongo', status_code=200)
async def test_mongo(request: Request):
    data = []
    # api.mongodb_collection is set in main.py
    async for result in request.app.mongodb_collection.find():
        del result['_id']
        data.append(result)
    return {'Mongo data': data}


# CREATE a new task and store it in the Mongo database
@router.post('/task', response_description="Add new task")
async def create_task(request: Request, task: TaskModel = Body(...)):
    task = jsonable_encoder(task)
    # write the new task in the "tasks" collection inside the DB specified in main.py
    new_task = await request.app.mongodb["tasks"].insert_one(task)
    created_task = await request.app.mongodb["tasks"].find_one(
        {"_id": new_task.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_task)


# GET a list of tasks
@router.get('/task', response_description="List all tasks")
async def list_tasks(request: Request):
    tasks = []
    for doc in await request.app.mongodb["tasks"].find().to_list(length=100):
        tasks.append(doc)

    return tasks


# GET a specific task by "id" field (_id inside the MongoDB)
@router.get("/task/{id}", response_description="Get a single task")
async def show_task(id: str, request: Request):
    if (task := await request.app.mongodb["tasks"].find_one({"_id": id})) is not None:
        return task

    raise HTTPException(status_code=404, detail=f"Task {id} not found")


# Update an existing task
@router.put("/task/{id}", response_description="Update a task")
async def update_task(id: str, request: Request, task: UpdateTaskModel = Body(...)):
    task = {k: v for k, v in task.dict().items() if v is not None}
    if len(task) >= 1:
        update_result = await request.app.mongodb["tasks"].update_one(
            {"_id": id}, {"$set": task}
        )
        if update_result.modified_count == 1:
            if (
                updated_task := await request.app.mongodb["tasks"].find_one({"_id": id})
            ) is not None:
                return updated_task
    if (
        existing_task := await request.app.mongodb["tasks"].find_one({"_id": id})
    ) is not None:
        return existing_task

    raise HTTPException(status_code=404, detail=f"Task {id} not found")


# DELETE a task
@router.delete("/task/{id}", response_description="Delete Task")
async def delete_task(id: str, request: Request):
    delete_result = await request.app.mongodb["tasks"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Task {id} not found")
