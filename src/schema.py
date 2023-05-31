from pydantic import BaseModel

class CreateEventRequest(BaseModel):
    title: str
    desc: str 
