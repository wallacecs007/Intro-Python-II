# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, currentRoom):
        self.current_room = currentRoom
        self.items = []

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

    def get_item(self, object):
        item_to_get = None
        room_items = self.current_room
        room_items = room_items.items
        # print(getattr(self.current_room, "items"))
        for item in room_items.items:
            if item.name == object:
                item_to_get == item
        if item_to_get is not None:
            item_to_get.on_take()
            room_items.items.remove(item_to_get)
            self.items.append(item_to_get)
            self.current_room.items = room_items
        else:
            print(f"There is no item with that name to pick up!")

    def drop_item(self, object):
        item_to_drop = None
        print(self.items)
        for item in self.items:
            if item.name == object:
                item_to_drop == item
        if item_to_drop is not None:
            item_to_drop.on_drop()
            self.current_room.items.append(item_to_drop)
            self.items.remove(item_to_drop)
        else:
            print(f"There is no item with that name to drop!")
