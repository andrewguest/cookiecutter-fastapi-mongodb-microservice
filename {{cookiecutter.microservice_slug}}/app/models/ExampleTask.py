from typing import Optional
import uuid

from pydantic import BaseModel, Field


# Define a MongoDB model called "TaskModel" that has 3 properties:
#   id, name, and completed
class TaskModel(BaseModel):
    """
    MongoDB uses _id, but in Python, underscores at the start of attributes have special meaning. If you have an attribute on your model that starts with an underscore, pydantic—the data validation framework used by FastAPI—will assume that it is a private variable, meaning you will not be able to assign it a value! To get around this, we name the field id but give it an alias of _id. You also need to set allow_population_by_field_name to True in the model's Config class.
    """

    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    completed: bool = False

    # "schema_extra" defines an example that will be shown in the docs (/docs) page.
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "My important task",
                "completed": True,
            }
        }


class UpdateTaskModel(BaseModel):
    name: Optional[str]
    completed: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "My important task",
                "completed": True,
            }
        }
