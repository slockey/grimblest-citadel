import unittest

from item_factory import ItemFactory


class ItemFactoryTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # put setup stuff here
        print("setup")
    
    # TODO: add more/better tests here

    def test_add_single_stackableitem_twice(self):
        # do something
        item1 = ItemFactory.get_instance("health_potion")
        item2 = ItemFactory.get_instance("health_potion")

        print(item1)
        print(item2)

