#!/usr/bin/env python3
"""Function to store key and value pair to redis"""


import redis
import uuid
from funtools import wraps
from typing import Union, Callable


class Cache:
    """Create a Cache class."""
    def __init__(self):
        """Initialize the object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        @wraps(methos)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @countcalls
    def store(self, data: Union[int, float, str, bytes]) -> str:
        """Function to store the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable[[bytes], Union[int, float, str, bytes]] = None):
        """Read from redis and recover the data type"""
        data = self._redis.get(key)
        if data is not None:
            if fn is not None:
                return fn(data)
            else:
                return data
        return None

    def get_str(self, key: str) -> str:
        """Parametize Cache.get to a str"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Parametize Cache.get to an int"""
        return self.get(key, fn=lambda d: int(d))
