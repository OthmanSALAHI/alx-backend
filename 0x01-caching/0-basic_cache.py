#!/usr/bin/env python3
"""docs"""

import base_caching


class BasicCache(base_caching.BaseCaching):
    """ class """
    def put(self, key, item):
        """put item in cache"""
        self.cache_data[key] = item if key and item else None

    def get(self, key):
        """get item from cache"""
        return self.cache_data.get(key, None)
