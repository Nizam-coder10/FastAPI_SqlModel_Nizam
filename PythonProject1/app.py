from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

rooms_db = []

class Room(BaseModel):
    id: int
    room_number: str
    room_type: str
    price_per_night: float
    is_available: bool = True

@app.post("/rooms/", status_code=201)
def create_room(room: Room):
    rooms_db.append(room)
    return room

@app.get("/rooms/", response_model=List[Room])
def list_rooms():
    return rooms_db

@app.get("/rooms/{room_id}", response_model=Room)
def get_room(room_id: int):
    for room in rooms_db:
        if room.id == room_id:
            return room
    raise HTTPException(status_code=404, detail="Room not found")

@app.put("/rooms/{room_id}", response_model=Room)
def update_room(room_id: int, updated: Room):
    for i, room in enumerate(rooms_db):
        if room.id == room_id:
            rooms_db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Room not found")

@app.delete("/rooms/{room_id}", status_code=204)
def delete_room(room_id: int):
    for i, room in enumerate(rooms_db):
        if room.id == room_id:
            rooms_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Room not found")

@app.patch("/rooms/{room_id}/availability", response_model=Room)
def update_availability(room_id: int, is_available: bool):
    for room in rooms_db:
        if room.id == room_id:
            room.is_available = is_available
            return room
    raise HTTPException(status_code=404, detail="Room not found")
