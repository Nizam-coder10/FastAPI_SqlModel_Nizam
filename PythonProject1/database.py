from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlmodel import SQLModel
from pathlib import Path


db_path = Path("db")
db_path.mkdir(exist_ok=True)

sqlite_file_name = db_path / "hotel.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

def create_db_and_tables():

    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hotel API funcionando"}
