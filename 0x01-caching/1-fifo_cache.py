#!/usr/bin/env python3
""" FIFO Caching Module """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        a class FIFOCache that inherits from BaseCaching
        and is a caching system
    """

    def __init__(self):
        """ Init method """
        super().__init__()

    def put(self, key, item):
        """
            assign to the dictionary self.cache_data
            the item value for the key
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.list_dict = list(self.cache_data.keys())
                print(f"DISCARD {self.list_dict[0]}")
                del self.cache_data[self.list_dict[0]]

    def get(self, key):
        """
            return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
