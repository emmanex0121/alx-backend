#!/usr/bin/env python3

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
       Basic cache class that inherits from BaseCaching class
    """

    def put(self, key, item):
        """ method that assigns the key and item
            to the dict self.cache_data
            Do nothing if key or item is None
        """
        if None in (key, item):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
            return the value in self.cache_data linked to key
        """
        try:
            return self.cache_data.get(key)
        except KeyError as e:
            return None
