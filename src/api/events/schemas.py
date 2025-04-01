from pydantic import BaseModel, Field
from typing import List, Optional



class EventCreateSchema(BaseModel):
    page: str
    description: Optional[str] = Field(default="", max_length=1000)

class EventUpdateSchema(BaseModel):
    description: str

class EventSchema(BaseModel):
    id: int
    page: Optional[str] = ""
    description: Optional[str] = ""

class EventListSchema(BaseModel):
    result: List[EventSchema]
    count: int