
from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING

from components.base_component import BaseComponent

from item_factory import ItemFactory

if TYPE_CHECKING:
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.stackable_capacity = 5
        self.items: List[Item] = []
        self.stackable: Dict[Item, int] = {}


    def remove(self, item: Item) -> None:
        """
        removes an item from the inventory
        """
        if not item.stackable:
            self.items.remove(item)
        else:
            # handle stackable items - stackable then item
            count = self.stackable[item]
            if count == 1:
                # remove completely
                self.stackable.pop(item)
                self.items.remove(item)
            else:
                self.stackable[item] = count - 1


    def drop(self, item: Item) -> None:
        """
        removes an item from the inventory and restores it to the game map
        at the player's current location.
        spawning the item which results in a deep copy being added to the game entities list
        """
        item.spawn(self.gamemap, self.parent.x, self.parent.y)
        self.remove(item)


    def add(self, item: Item) -> bool:
        """
        interface to add items to the inventory. this is a precursor to stackable items
        """
        # handle non-stackable items
        if not item.stackable:
            if len(self.items) < self.capacity:
                self.items.append(item)
                self.engine.message_log.add_message(f"You picked up the {item.name}.")
                return True
        else:
            # item is stackable - does the item already exist within inventory?
            use_this_item = ItemFactory.get_instance(item.id)
            # give the item a reference to the inventory
            use_this_item.parent = self

            if (use_this_item in self.items):
                # item does exist - check if we can add it
                count = self.stackable[use_this_item]
                # can we add the item - stackable capacity
                if count < self.stackable_capacity:
                    self.stackable[use_this_item] = count + 1
                    self.engine.message_log.add_message(f"You picked up the {use_this_item.name}.")
                    return True
            else:
                # item does NOT exist - check if we can add it
                if len(self.items) < self.capacity:
                    self.items.append(use_this_item)
                    self.stackable[use_this_item] = 1
                    self.engine.message_log.add_message(f"You picked up the {use_this_item.name}.")
                    return True
        # unable to pick up the item            
        self.engine.message_log.add_message(f"No room in inventory for {item.name}.")
        return False
