#!/usr/bin/env python3
"""docs"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ class """
    def put(self, key, item):
        """put item in cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get item from cache"""
        return self.cache_data.get(key)
