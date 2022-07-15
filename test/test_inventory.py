import unittest
import entity_factories

from components.inventory import Inventory
from entity import Item

class InventoryTestCase(unittest.TestCase):

    def test_add_single_item(self):
        """do something in this test"""
        inventory = Inventory(10)
        inventory.add(entity_factories.health_potion)

        self.assertEquals(inventory.__sizeof__(), 1)

if __name__ == '__main__':
    unittest.main()
