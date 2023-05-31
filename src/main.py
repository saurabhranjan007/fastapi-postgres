from fastapi import FastAPI, Depends
from schema import CreateEventRequest
from sqlalchemy.orm import Session
from database import get_db
from models import Event


app = FastAPI()

# CREATE EVENT 
@app.post("/create/")
def create_event(details: CreateEventRequest, db: Session=Depends(get_db)):
    print(db)
    to_create = Event(
        title = details.title,
        desc = details.desc
    )
    db.add(to_create)
    db.commit()

    return { "success": True, "created_event": to_create.id }

# GET EVENT (ONE)
@app.get('/event')
def get_event(id: int, db:  Session=Depends(get_db)):
    return db.query(Event).filter(Event.id == id).first()

# GET EVENT ALL 
@app.get('/events')
def get_events(db: Session=Depends(get_db)):
    return db.query(Event).all()

# DELETE EVENT 
@app.delete('/delete/')
def delete_event(id: int, db: Session=Depends(get_db)):
    db.query(Event).filter(Event.id==id).delete()
    db.commit()
    return {"success": True}
