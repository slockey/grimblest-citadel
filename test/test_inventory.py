import unittest

from typing import List, TYPE_CHECKING

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


    def test_add_single_nonstackableitem(self):
        """Add a single non-stackable item to the inventory"""
        self.player.inventory = Inventory(capacity=1)
        self.player.inventory.parent = self.player

        add_result = self.player.inventory.add(entity_factories.dagger)

        self.assertTrue(add_result)
        self.assertEqual(len(self.player.inventory.items), 1)


    def test_add_single_stackableitem(self):
        """Add a single stackable item once to the inventory"""
        self.player.inventory = Inventory(capacity=1)
        self.player.inventory.parent = self.player

        add_result = self.player.inventory.add(entity_factories.health_potion)

        self.assertTrue(add_result)
        self.assertEqual(len(self.player.inventory.items), 1)
        self.assertEqual(len(self.player.inventory.stackable), 1)
        self.assertEqual(self.player.inventory.stackable[entity_factories.health_potion], 1)


    def test_add_same_stackableitem(self):
        """Add a stackable item twice to the inventory"""
        self.player.inventory = Inventory(capacity=1)
        self.player.inventory.parent = self.player

        self.add_result: List[bool] = []        

        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))

        self.assertEqual(5, sum(self.add_result))
        self.assertEqual(len(self.player.inventory.items), 1)
        self.assertEqual(len(self.player.inventory.stackable), 1)
        self.assertEqual(self.player.inventory.stackable[entity_factories.health_potion], 5)


    def test_fail_add_single_nonstackableitem_zeroinventory(self):
        """Fail to add a single non-stackable item to the inventory"""
        self.player.inventory = Inventory(capacity=0)
        self.player.inventory.parent = self.player

        add_result = self.player.inventory.add(entity_factories.dagger)

        self.assertFalse(add_result)
        self.assertEqual(len(self.player.inventory.items), 0)


    def test_fail_add_single_nonstackableitem_fullinventory(self):
        """Fail to add a single non-stackable item to the inventory"""
        self.player.inventory = Inventory(capacity=1)
        self.player.inventory.parent = self.player
        # setup by pre-adding item to fill the inventory
        self.player.inventory.add(entity_factories.dagger)

        # add an item beyond the inventory limit
        add_result = self.player.inventory.add(entity_factories.dagger)

        self.assertFalse(add_result)
        self.assertEqual(len(self.player.inventory.items), 1)


    def test_fail_add_single_stackableitem_zeroinventory(self):
        """Fail to add a single stackable item once to the inventory"""
        self.player.inventory = Inventory(capacity=0)
        self.player.inventory.parent = self.player

        add_result = self.player.inventory.add(entity_factories.health_potion)

        self.assertFalse(add_result)
        self.assertEqual(len(self.player.inventory.items), 0)
        self.assertEqual(len(self.player.inventory.stackable), 0)


    def test_add_same_stackableitem_beyond_capacity(self):
        """Add a stackable item 28 times to the inventory"""
        self.player.inventory = Inventory(capacity=1)
        self.player.inventory.parent = self.player

        self.add_result: List[bool] = []        

        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))
        self.add_result.append(self.player.inventory.add(entity_factories.health_potion))

        self.assertEqual(28, len(self.add_result))
        self.assertEqual(5, sum(self.add_result))   # there were 5 successful adds
        self.assertEqual(len(self.player.inventory.items), 1)
        self.assertEqual(len(self.player.inventory.stackable), 1)
        self.assertEqual(self.player.inventory.stackable[entity_factories.health_potion], self.player.inventory.stackable_capacity)


if __name__ == '__main__':
    unittest.main()
