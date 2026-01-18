# -*- coding: utf-8 -*-
import hy
import gilded_rose_func


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        gilded_rose_func.update_quality(self.items)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
