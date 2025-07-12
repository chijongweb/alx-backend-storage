#!/usr/bin/env python3
"""
This module contains the Cache class and decorators for storing and
retrieving data using Redis, including call counting and history tracking.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    Stores the count in Redis using the method's qualified name as key.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method in Redis lists.
    Inputs stored in `<method.__qualname__>:inputs`
    Outputs stored in `<method.__qualname__>:outputs`
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store the string representation of the input args (ignore kwargs)
        self._redis.rpush(input_key, str(args))

        # Call the original method and get the output
        result = method(self, *args, **kwargs)

        # Store the output as string
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


class Cache:
    """A Redis-based cache class for storing and retrieving data."""

    def __init__(self):
        """Initialize Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key, store the data in Redis, and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally convert it using fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """Retrieve data as a UTF-8 string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve data as an integer."""
        return self.get(key, fn=int)


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.
    Uses Redis keys: <method.__qualname__>:inputs and <method.__qualname__>:outputs.
    Prints the number of calls and each call’s input and output.
    """
    redis_client = redis.Redis()
    method_name = method.__qualname__

    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    inputs = redis_client.lrange(inputs_key, 0, -1)
    outputs = redis_client.lrange(outputs_key, 0, -1)

    call_count = redis_client.get(method_name)
    if call_count is None:
        call_count = 0
    else:
        call_count = int(call_count)

    print(f"{method_name} was called {call_count} times:")

    for input_, output in zip(inputs, outputs):
        input_str = input_.decode("utf-8")
        output_str = output.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")