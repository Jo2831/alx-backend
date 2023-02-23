#!/usr/bin/python3
"""
file 0-basic_cache
"""

from basic_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    overrides put() and self()
    """

    def put(self, Key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        value = self.cache_data.get(key)
        return value
