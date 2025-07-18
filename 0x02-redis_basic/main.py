#!/usr/bin/env python3
"""
Main file to test the Cache class with all implemented tasks.
"""

import redis
from exercise import Cache, replay

cache = Cache()

# Task 0: Store binary data
data = b"hello"
key = cache.store(data)
print(f"Stored key: {key}")
local_redis = redis.Redis()
print(f"Raw Redis get: {local_redis.get(key)}")  # Expected: b'hello'

# Task 1: Retrieve original types
print("\n=== Task 1 Test Cases ===")
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    result = cache.get(key, fn=fn)
    print(f"Original: {value} | Retrieved: {result} | Match: {result == value}")
    assert result == value

print("\nTesting get_str and get_int methods:")

key_str = cache.store("This is a string")
print(f"get_str: {cache.get_str(key_str)}")

key_int = cache.store(42)
print(f"get_int: {cache.get_int(key_int)}")

# Task 3: Test count_calls decorator on store method
print("\n=== Task 3: count_calls decorator test ===")

cache.store(b"first")
count = cache.get(cache.store.__qualname__)
print(f"store called {count} time(s)")

cache.store(b"second")
cache.store(b"third")
count = cache.get(cache.store.__qualname__)
print(f"store called {count} time(s)")

# Task 4: Test call_history decorator inputs/outputs
print("\n=== Task 4: call_history decorator test ===")

inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

print(f"inputs: {inputs}")
print(f"outputs: {outputs}")

# Task 5: Test replay function
print("\n=== Task 5: replay function output ===")
replay(cache.store)