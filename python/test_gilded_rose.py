# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_regular_item(self):
        item_type = "foo"
        items = [Item(item_type, sell_in=24, quality=42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(41, items[0].quality)
        self.assertEqual(23, items[0].sell_in)

    def test_item_after_sell_in(self):
        item_type = "foo"
        items = [Item(item_type, sell_in=0, quality=8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(6, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_item_quality_never_negative(self):
        item_type = "foo"
        items = [Item(item_type, sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_aged_brie_item(self):
        item_type = "Aged Brie"
        items = [Item(item_type, sell_in=24, quality=42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(43, items[0].quality)
        self.assertEqual(23, items[0].sell_in)

    def test_quality_never_above_50(self):
        item_type = "Aged Brie"
        items = [Item(item_type, sell_in=24, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(50, items[0].quality)
        self.assertEqual(23, items[0].sell_in)

    def test_sulfuras_item(self):
        item_type = "Sulfuras, Hand of Ragnaros"
        items = [Item(item_type, sell_in=24, quality=42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(42, items[0].quality)
        self.assertEqual(24, items[0].sell_in)

    def test_back_stage_ticket(self):
        item_type = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_type, sell_in=24, quality=42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(43, items[0].quality)
        self.assertEqual(23, items[0].sell_in)

    def test_back_stage_ticket_quality_after_10_days(self):
        item_type = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_type, sell_in=10, quality=42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(44, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_back_stage_ticket_quality_after_5_days(self):
        item_type = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_type, sell_in=5, quality=42)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_type, items[0].name)
        self.assertEqual(45, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

class ItemTest(unittest.TestCase):
    def test_item(self):
        item = Item("foo", 0, 0)
        self.assertEqual("foo, 0, 0", str(item))

if __name__ == '__main__':
    unittest.main()
