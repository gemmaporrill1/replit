rooms = [
  {"room_number": 1, "bed_type": "double", "smoking": False, "availability": True},
  {"room_number": 2, "bed_type": "single", "smoking": False, "availability": False},
  {"room_number": 3, "bed_type": "double", "smoking": True, "availability": True},
  {"room_number": 4, "bed_type": "queen", "smoking": False, "availability": False},
  {"room_number": 5, "bed_type": "queen", "smoking": False, "availability": True},
        ]

# 1. add rooms

def add_room(rooms, room_number, bed_type="Double", smoking=False):
  new_room = {"room_number": room_number, "bed_type": bed_type, 
              "smoking": smoking, "availability": True}
  rooms.append(new_room)
  return rooms
print(add_room(rooms, 6))

# 2. book room

def book_room(rooms, preferred_bed_type="double", smoking=False):
  for room in rooms:
    if room["bed_type"] == preferred_bed_type and room["smoking"] == smoking:
        room["availability"] = False
        return room
    return None
print(book_room(rooms))
  

# 3. list available rooms 
def list_available_rooms(rooms):
  available_rooms = []
  for room in rooms:
      if room["availability"]:
          available_rooms.append(room)
  return available_rooms

available_rooms_list = list_available_rooms(rooms)

if available_rooms_list:
  print("Available rooms:")
  for room in available_rooms_list:
      print(f"Room {room['room_number']} is available.")
else:
  print("No available rooms.")
