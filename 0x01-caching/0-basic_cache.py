#!/usr/bin/python3
"""basic cache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class definition"""
    def put(self, key, item):
        """insert new data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get data func"""
        if key is not None:
            if key in self.cache_data:
                return self.cache_data[key]
        return None
