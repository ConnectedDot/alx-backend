#!/usr/bin/env python3
<<<<<<< HEAD
"""Module for task 1.
=======
"""First-In First-Out caching module.
>>>>>>> 317e96a2a5b7d9d3ea935f9eb02500ea2f70f863
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
<<<<<<< HEAD
    """A caching system that inherits from BaseCaching and uses a FIFO
    algorithm to discard items.

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """Initializes the cache and calls the parent class's init method.
=======
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
>>>>>>> 317e96a2a5b7d9d3ea935f9eb02500ea2f70f863
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
<<<<<<< HEAD
        """Assigns the item value to the key in the dictionary self.cache_data.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, the oldest item is discarded using a FIFO
        algorithm and a message is printed.

        Args:
            key (any): param1.
            item (any): param2.
=======
        """Adds an item in the cache.
>>>>>>> 317e96a2a5b7d9d3ea935f9eb02500ea2f70f863
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.
        """
<<<<<<< HEAD
        return self.cache_data.get(key, None)
=======
        return self.cache_data.get(key, None)
>>>>>>> 317e96a2a5b7d9d3ea935f9eb02500ea2f70f863
