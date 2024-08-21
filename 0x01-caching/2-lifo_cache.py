#!/usr/bin/python3
"""LIFO cache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """lifocach class definition"""
    def __init__(self):
        """init func"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """insert new cache"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discards = self.cache_data.popitem(True)
                    print("DISCARD: {}".format(discards[0]))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """get data func"""
        if key is not None:
            if key in self.cache_data:
                return self.cache_data[key]
        return None
