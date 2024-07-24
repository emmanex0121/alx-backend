#!/usr/bin/env python3
""" LIFO Caching Module """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        A class FIFOCache that inherits from BaseCaching
        and is a caching system implementing FIFO (First-In-First-Out)
        eviction policy.
    """

    def __init__(self):
        """ Initialize the FIFO cache """
        super().__init__()
        self.list_dict = list(self.cache_data.keys())

    def put(self, key, item):
        """
            Assign the item value to the key in self.cache_data.
            If the number of items exceeds MAX_ITEMS,
            discard the last item put in cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.list_dict.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # self.list_dict = list(self.cache_data.keys())
                print(f"DISCARD: {self.list_dict[-2]}")
                del self.cache_data[self.list_dict[-2]]
                self.list_dict.pop(-2)
            # self.cache_data[key] = item

    def get(self, key):
        """
            Return the value in self.cache_data linked to the key.
        """
        return self.cache_data.get(key, None)
