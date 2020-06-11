# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, currentRoom):
        self.current_room = currentRoom

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") != None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
            print("\n")
        else:
            print(
                f"You search to the {direction}, but don't find a way to travel!")
            print(self.current_room)
            print("\n")
