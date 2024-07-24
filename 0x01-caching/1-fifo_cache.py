#!/usr/bin/env python3
""" FIFO Caching Module """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        A class FIFOCache that inherits from BaseCaching
        and is a caching system implementing FIFO (First-In-First-Out)
        eviction policy.
    """

    def __init__(self):
        """ Initialize the FIFO cache """
        super().__init__()

    def put(self, key, item):
        """
            Assign the item value to the key in self.cache_data.
            If the number of items exceeds MAX_ITEMS, discard the oldest one.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.list_dict = list(self.cache_data.keys())
                print(f"DISCARD: {self.list_dict[0]}")
                del self.cache_data[self.list_dict[0]]

    def get(self, key):
        """
            Return the value in self.cache_data linked to the key.
        """
        return self.cache_data.get(key, None)
