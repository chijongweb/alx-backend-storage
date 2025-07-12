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
