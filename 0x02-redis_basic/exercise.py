#!/usr/bin/env python3
"""
This module contains the Cache class for storing data in Redis.
"""

import redis
import uuid
from typing import Union, Optional, Callable

class Cache:
    """A simple Redis cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the given data in Redis using a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and optionally apply a conversion function.

        Args:
            key: Redis key to retrieve
            fn: Optional function to apply to the retrieved data

        Returns:
            The original data type if fn is provided, otherwise bytes or None
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a UTF-8 decoded string from Redis.

        Args:
            key: Redis key to retrieve

        Returns:
            The string value or None
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key: Redis key to retrieve

        Returns:
            The integer value or None
        """
        return self.get(key, fn=int)