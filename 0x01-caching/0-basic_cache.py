#!/usr/bin/python3

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        """put item in cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        self.cache_data.get(key)
