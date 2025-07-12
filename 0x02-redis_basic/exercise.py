#!/usr/bin/env python3
"""
This module contains the Cache class for storing data in Redis.
"""

import redis
import uuid
from typing import Union

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
