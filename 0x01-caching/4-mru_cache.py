#!/usr/bin/python3
"""MRU cache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRUCache class definition"""
    def __init__(self):
        """init func"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """insert new cache"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discards = self.cache_data.popitem(last=True)
                    print("DISCARD: {}".format(discards[0]))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """get data func"""
        if key is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
                return self.cache_data[key]
        return None
