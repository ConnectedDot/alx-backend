#!/usr/bin/env python3
<<<<<<< HEAD
"""Module for task 0.
=======
"""Basic caching module.
>>>>>>> 317e96a2a5b7d9d3ea935f9eb02500ea2f70f863
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
<<<<<<< HEAD
    """A caching system that inherits from BaseCaching and does not have a
    limit on the number of items it can store.
    """
    def put(self, key, item):
        """Assigns the item value to the key in the dictionary self.cache_data.
        If key or item is None, this method should not do anything.

        Args:
            key (any): param1.
            item (any): param2.
=======
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """Adds an item in the cache.
>>>>>>> 317e96a2a5b7d9d3ea935f9eb02500ea2f70f863
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
<<<<<<< HEAD
        """Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key, None)
=======
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
>>>>>>> 317e96a2a5b7d9d3ea935f9eb02500ea2f70f863
