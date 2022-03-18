# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # we don't need to do anything with Sulfuras because it's Ledgend...(wait for it)...dary
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name == "Aged Brie":
                # Limit quality to 50
                if item.quality < 50:
                    item.quality += 1
                # if the Brie's sell_in days are 0 or less, add an extra quality because rotten cheese is apparently better
                if item.sell_in < 1 and item.quality < 50:
                    item.quality += 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    # backstage passes increase in quality as sell_in days are reduced
                    if item.quality < 50:
                        item.quality += 1
                    # if sell_in is 10 or less add 1 extra quality - two total
                    if item.sell_in < 11 and item.quality < 50:
                        item.quality += 1
                    # if sell_in is 5 or less, add another quality - three total
                    if item.sell_in < 6 and item.quality < 50:
                        item.quality += 1
                    if item.sell_in < 1:
                        item.quality = 0
            else:
                # everything except Brie and backstage passes lose quality
                if item.quality > 0:
                    item.quality -= 1
                    # if this is a conjured item, take one more from quality
                    if "conjured" in item.name.lower() and item.quality > 0:
                        item.quality -= 1

            # decrement sell_in for every item
            item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
