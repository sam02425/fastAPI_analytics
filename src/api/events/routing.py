import os
from fastapi import APIRouter
from .schemas import (
    EventSchema,
    EventListSchema,
    EventCreateSchema,
    EventUpdateSchema
    )


router = APIRouter()
from api.db.config import DATABASE_URL
#list view
# GET /api/events/
@router.get("/")
def read_events()-> EventListSchema:
    print(os.environ.get("DATABASE_URL"))
    return {
        "result":[
            {"id":1},{"id":2},{"id":3}
            ],
        "count": 3
    }

# sending data
# create view
# POST /api/events/

@router.post("/")
def create_event(payload:EventCreateSchema)-> EventSchema:
    data = payload.model_dump() # payload -> dict -> pydantic
    return {"id":1234, **data}

# GET /api/events/{event_id}/

@router.get("/{event_id}")
def get_event(event_id: int)->EventSchema:
    return {
        "id": event_id
    }

# PUT /api/events/{event_id}/

@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpdateSchema)->EventSchema:
    data = payload.model_dump() # payload -> dict -> pydantic
    return {
        "id": event_id,
        **data
    }

