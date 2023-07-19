#!/usr/bin/env python3
"""Function to store key and value pair to redis"""


import redis
import uuid
from typing import Union


class Cache:
    """Create a Cache class."""
    def __init__(self):
        """Initialize the object"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data: Union[int, float, str, bytes]) -> str:
        """Function to store the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
