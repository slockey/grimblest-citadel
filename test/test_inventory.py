import unittest

from engine import Engine
import entity_factories
from game_map import GameWorld
import copy

from components.inventory import Inventory
from entity import Item

class InventoryTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.player = copy.deepcopy(entity_factories.player)

        self.engine = Engine(player=self.player)

        self.engine.game_world = GameWorld(
            engine=self.engine,
            max_rooms=1,
            room_min_size=6,
            room_max_size=10,
            map_width=40,
            map_height=23,
        )
        self.engine.game_world.generate_floor()


    def test_add_single_item(self):

        """do something in this test"""
        self.player.inventory = Inventory(1)
        self.player.inventory.parent = self.player

        self.player.inventory.add(entity_factories.health_potion)
        # add an item beyond the inventory limit
        self.player.inventory.add(entity_factories.health_potion)

        self.assertEqual(len(self.player.inventory.items), 1)

if __name__ == '__main__':
    unittest.main()
