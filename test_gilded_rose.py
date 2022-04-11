# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_basic_item_decrements_sellin_and_doesnt_drop_quality_below_0(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        self.assertEquals(0, items[0].quality)
        self.assertEquals(-1, items[0].sell_in)

    def test_basic_item_decrements_sellin_and_quality(self):
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        self.assertEquals(0, items[0].quality)
        self.assertEquals(0, items[0].sell_in)
    
    def test_aged_brie(self):
        items = [Item("Aged Brie", 10, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(6, items[0].quality)

        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(1, items[0].quality)

        items = [Item("Aged Brie", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(4, items[0].quality)

    def test_concert_tickets(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(14, items[0].sell_in)
        self.assertEquals(21, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 39)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(41, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 39)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(42, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    def test_the_vest(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("+5 Dexterity Vest", items[0].name)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(19, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(80, items[0].quality)

        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(80, items[0].quality)
    
    def test_mana_cake(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Conjured Mana Cake", items[0].name)
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(4, items[0].quality)

        items = [Item("Conjured Mud Pie", 3, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Conjured Mud Pie", items[0].name)
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
