#!/usr/bin/env python3
"""Function to store key and value pair to redis"""


import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str,
            fn: Callable[None]) -> Union[str, bytes, int, float]:
        """Read from redis and recover the data type"""
        data = self._redis.get(key)
        if fn(data) is not None:
            ans = fn(data)
        else:
            ans = data
        return data

    def get_str(self, key: str) -> str:
        """Parametize Cache.get to a str"""
        val = self.get(key)
        return val.decode('utf-8') if isinstance(val, bytes)

    def get_int(self, key: str) -> int:
        """Parametize Cache.get to an int"""
        val = self.get(key)
        return val.decode('utf-8') if isinstance(val, bytes)

