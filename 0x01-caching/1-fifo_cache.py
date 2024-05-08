#!/usr/bin/python3
""" docuemtation module"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache system """

    def __init__(self):
        """doc doc doc"""
        super().__init__()

    def put(self, key, item):
        """ docs """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = next(iter(self.cache_data))
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """ docs """
        return self.cache_data.get(key)
