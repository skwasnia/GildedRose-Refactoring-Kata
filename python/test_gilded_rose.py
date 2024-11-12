# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_regular_item(self):
        item_type = "foo"
        items = [Item(item_type, 24, 42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(41, items[0].quality)
        self.assertEqual(23, items[0].sell_in)

    def test_aged_brie_item(self):
        item_type = "Aged Brie"
        items = [Item(item_type, 24, 42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(43, items[0].quality)
        self.assertEqual(23, items[0].sell_in)

class ItemTest(unittest.TestCase):
    def test_item(self):
        item = Item("foo", 0, 0)
        self.assertEqual("foo, 0, 0", str(item))

if __name__ == '__main__':
    unittest.main()
