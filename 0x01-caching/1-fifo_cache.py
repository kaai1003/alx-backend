#!/usr/bin/python3
"""FIFO cache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifocach class definition"""
    def __init__(self):
        """init func"""
        super().__init__()

    def put(self, key, item):
        """insert new cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                fifo_key = next(iter(self.cache_data))
                self.cache_data.pop(fifo_key)
                print("DISCARD: {}".format(fifo_key))
            self.cache_data[key] = item

    def get(self, key):
        """get data func"""
        if key is not None:
            if key in self.cache_data:
                return self.cache_data[key]
        return None
