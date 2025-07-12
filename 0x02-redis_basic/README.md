# ALX Backend Storage - Redis Basic

## Project Overview

This project demonstrates the basic usage of Redis as a key-value store and simple cache system using Python. It includes a `Cache` class that can store data of various types (strings, bytes, integers, floats) in Redis with randomly generated keys.

## Key Concepts

- **Redis**: An in-memory data structure store used as a database, cache, and message broker.
- **Caching**: Storing data temporarily to speed up access and reduce load on primary data sources.
- **Python Redis Client**: Interacting with Redis using the `redis` Python package.
- **UUID keys**: Generating unique random keys to store data.

## Features

- Initialize Redis and flush the database for clean state
- Store data of multiple types with a random key
- Retrieve stored data by key

## Requirements

- Ubuntu 18.04 LTS (or compatible Linux environment, WSL recommended on Windows)
- Python 3.7+
- Redis server installed and running
- Python `redis` package (`pip3 install redis`)

## Installation & Usage

1. Clone this repository:

   git clone https://github.com/chijongweb/alx-backend-storage.git
   cd alx-backend-storage/0x02-redis_basic

2.Install Redis and Python dependencies:

	sudo apt update
	sudo apt install redis-server python3-pip -y
	pip3 install redis

3. Start Redis server:

	sudo service redis-server start

4.Run the Python script to test caching:

	python3 main.py


 # 0x02. Redis basic

This project is part of the ALX Backend specialization and focuses on using **Redis** with Python for basic caching and storage operations.

## Learning Objectives

By the end of this project, you should be able to:

- Use `redis` and the `redis-py` client for basic Redis operations.
- Use Redis as a simple cache.
- Understand how to store and retrieve various Python data types in Redis.
- Understand serialization and deserialization techniques using callable functions.

## Requirements

- Python 3.7+
- `redis` server running locally (`sudo service redis-server start`)
- `redis-py` module (`pip3 install redis`)
- All functions are type-annotated.
- PEP8 style (pycodestyle 2.5)

## Files

| Filename       | Description                                     |
|----------------|-------------------------------------------------|
| `exercise.py`  | Contains the `Cache` class used for Redis operations. |
| `main.py`      | A sample test file to demonstrate usage of the `Cache` class. |

## Installation

To set up and test this project:


# Install Redis
sudo apt-get update
sudo apt-get install -y redis-server

# Start Redis server
sudo service redis-server start

# Install Python dependencies
pip3 install redis


Usage

python3 main.py


Output

Stored key: 3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
Raw Redis get: b'hello'

=== Task 1 Test Cases ===
Original: b'foo' | Retrieved: b'foo' | Match: True
Original: 123 | Retrieved: 123 | Match: True
Original: bar | Retrieved: bar | Match: True


# Task 2: Storing call history

This task enhances the `Cache` class by adding a `call_history` decorator to track the inputs and outputs of method calls.

## Objective

- Create a decorator `call_history` that stores the history of inputs and outputs of a method in Redis.
- Inputs are stored as strings in a Redis list with key format: `<method_name>:inputs`.
- Outputs are stored as strings in a Redis list with key format: `<method_name>:outputs`.
- Decorate the `Cache.store` method with this decorator.

## Implementation Details

- The decorator uses the Redis `RPUSH` command to append serialized inputs and outputs to their respective lists.
- This allows reviewing the history of all calls made to the decorated method.
- The original return value of the method is preserved and returned normally.

## Usage

When calling the `store` method of the `Cache` class, the following keys will be populated in Redis:

- `Cache.store:inputs` — list of string representations of arguments passed.
- `Cache.store:outputs` — list of string representations of the return values.

## Example


cache = Cache()
cache.store("data1")
cache.store("data2")

inputs = cache._redis.lrange("Cache.store:inputs", 0, -1)
outputs = cache._redis.lrange("Cache.store:outputs", 0, -1)

print(inputs)  # [b"('data1',)", b"('data2',)"]
print(outputs) # [b"<key1>", b"<key2>"]

## Task 4: Storing call history with Redis lists

In this task, we enhanced the `Cache` class by implementing a `call_history` decorator.

### What it does

- Every time the decorated method (e.g., `Cache.store`) is called, the input arguments are serialized and appended to a Redis list with key `<method_name>:inputs`.
- The output returned by the method is serialized and appended to another Redis list with key `<method_name>:outputs`.
- This enables tracking the full history of inputs and outputs for method calls.

### Implementation details

- The decorator uses Redis' `RPUSH` command to append entries to lists.
- Inputs are stored as strings representing the arguments tuple.
- Outputs are stored as strings representing the return value.
- Only positional arguments are considered for simplicity; keyword arguments are ignored.
- This is useful for debugging, auditing, and replaying method calls.

### Usage example

```python
cache = Cache()

cache.store("first")
cache.store("second")

inputs: [b"(b'hello',)", b"(b'foo',)", b'(123,)', b"('bar',)", b"('This is a string',)", b'(42,)', b"(b'first',)", b"(b'second',)", b"(b'third',)"]
outputs: [b'26094386-dc5b-49d4-bc9c-a2d5b882efdf', b'c7cb1496-4daf-4cf0-96da-f208c56a5786', b'e561b2d7-56ce-40a3-8bcd-59b32e862392', b'c5cf3cc6-a784-415d-a617-46a5ce87fe58', b'5cb55ade-ea0a-4618-b905-b3b6061a5d4e', b'c60a24d2-16bb-48c7-a00d-c8cbbec59ee9', b'fa6af223-d8ad-4ae0-b83a-53921de7eb59', b'01b27d2e-f43c-49cd-9b09-6726d4d71582', b'c0fec980-8dd2-440e-9a3b-3d51d1833d2c']



## Task 5: Retrieving call history with the replay function

This task introduces the `replay` function to display the full history of calls
to a decorated method (such as `Cache.store`).

### Purpose

The `replay` function retrieves and prints:

- How many times the method was called.
- Each call’s input arguments.
- Each call’s output (return value).

This leverages the data stored in Redis lists by the `call_history` decorator and
the call count from the `count_calls` decorator.

### Implementation details

- Uses Redis keys:
  - `<method_name>:inputs` for input arguments.
  - `<method_name>:outputs` for output results.
  - `<method_name>` for call count.
- Fetches and decodes all inputs and outputs.
- Prints a summary showing each call in the format:

Cache.store was called 3 times:
Cache.store(('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20

### Usage example

=== Task 5: replay function output ===
Cache.store was called 9 times:
Cache.store(*(b'hello',)) -> 26094386-dc5b-49d4-bc9c-a2d5b882efdf
Cache.store(*(b'foo',)) -> c7cb1496-4daf-4cf0-96da-f208c56a5786
Cache.store(*(123,)) -> e561b2d7-56ce-40a3-8bcd-59b32e862392
Cache.store(*('bar',)) -> c5cf3cc6-a784-415d-a617-46a5ce87fe58
Cache.store(*('This is a string',)) -> 5cb55ade-ea0a-4618-b905-b3b6061a5d4e
Cache.store(*(42,)) -> c60a24d2-16bb-48c7-a00d-c8cbbec59ee9
Cache.store(*(b'first',)) -> fa6af223-d8ad-4ae0-b83a-53921de7eb59
Cache.store(*(b'second',)) -> 01b27d2e-f43c-49cd-9b09-6726d4d71582
Cache.store(*(b'third',)) -> c0fec980-8dd2-440e-9a3b-3d51d1833d2c


Benefits
Provides clear visibility into method usage and history.

Useful for debugging and auditing cached operations.

Demonstrates combining decorators with Redis to track call metadata.


# Task 5: Implementing an Expiring Web Cache and Tracker

## Description

This task demonstrates how to implement a caching system for web pages using **Redis** in Python. The solution includes:

- Tracking the number of times a given URL is accessed using the Redis key `count:{url}`
- Caching the content of a requested URL for **10 seconds** using Redis
- Utilizing decorators to separate concerns (tracking vs. caching)

This helps avoid repeated HTTP requests for the same URL within a short time frame, reducing latency and bandwidth usage.

---

## File

- `web.py`

---

## Key Components

### `get_page(url: str) -> str`

Fetches the HTML content of a given URL using the `requests` module, with the following behaviors:
- Tracks the number of accesses using `count:{url}` in Redis
- Caches the HTML content in Redis for 10 seconds

### Decorators

- `@count_url_access`: Increments the access count for a given URL
- `@cache_page(expiration=10)`: Caches the page content with a TTL of 10 seconds

---

## How to Test

Use the built-in test script inside `web.py`:

```bash
python web.py

output:

First request (slow, not cached):
<html>...</html>

Second request (should be cached):
<html>...</html>

Access count:
b'2'
