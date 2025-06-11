from sqlmodel import Session
from database import engine, create_db_and_tables
from models import Person, Hotel
from client import create_room

def createPersons():
    with Session(engine) as session:
        persona1 = Person(name="Juan Perez", email="juanperez@example.com")
        persona2 = Person(name="Maria Lopez", email="marialopez@example.com")
        session.add(persona1)
        session.add(persona2)
        session.commit()
        session.refresh(persona1)
        session.refresh(persona2)

def createHotels():
    with Session(engine) as session:
        hotel1 = Hotel(name="Hotel Grand", address="Calle Mayor 1, Barcelona")
        hotel2 = Hotel(name="Hotel Oasis", address="Avenida Central 5, Madrid")
        session.add(hotel1)
        session.add(hotel2)
        session.commit()
        session.refresh(hotel1)
        session.refresh(hotel2)

def main():
    create_db_and_tables()
    createPersons()
    createHotels()
    create_room()

if __name__ == "__main__":
    main()
