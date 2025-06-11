import requests

BASE_URL = "http://127.0.0.1:8000"

def create_room():
    data = {"room_type": "Suite", "price": 200.0, "is_available": True}
    response = requests.post(f"{BASE_URL}/rooms/", json=data)
    print("Created Room:", response.json())

def list_rooms():
    response = requests.get(f"{BASE_URL}/rooms/")
    print("Room List:", response.json())

def get_room(room_id):
    response = requests.get(f"{BASE_URL}/rooms/{room_id}")
    print(f"Details of Room {room_id}:", response.json())

def update_room(room_id):
    data = {"room_type": "Suite Deluxe", "price": 250.0, "is_available": False}
    response = requests.put(f"{BASE_URL}/rooms/{room_id}", json=data)
    print(f"Updated Room {room_id}:", response.json())

def delete_room(room_id):
    response = requests.delete(f"{BASE_URL}/rooms/{room_id}")
    print(f"Deleted Room {room_id}:", response.json())

if __name__ == "__main__":
    create_room()
    list_rooms()
    get_room(1)
    update_room(1)
    delete_room(1)
