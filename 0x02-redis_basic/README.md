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
